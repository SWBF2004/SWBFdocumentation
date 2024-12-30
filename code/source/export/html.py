import os
import re
import json
import webbrowser
from websockets.sync.server import ServerConnection, serve
from pathlib import Path
from shutil import copytree, rmtree
from jinja2 import Environment, FileSystemLoader
from md.nodes import Folder
from http.server import HTTPServer, SimpleHTTPRequestHandler
from util.logging import get_logger


logger = get_logger(__name__)


def export_html(assets: Path, templates: Path, destination: Path, clear: bool, root: Folder):
    env = Environment(loader=FileSystemLoader(templates))
    env.filters['join'] = lambda children: ''.join(list(map(lambda node : node.text, children)))

    if clear:
        try:
            rmtree(destination)
        except FileNotFoundError:
            pass

    logger.info(f'Create directory {destination.as_posix()}')
    destination.mkdir(exist_ok=True, parents=True)

    if assets:
        logger.info(
            f'Copying {assets.as_posix()} -> {(destination / assets.name).as_posix()}')
        copytree(assets, destination / assets.name, dirs_exist_ok=True)

    index_template = env.get_template('index.html.j2')
    index_file = destination / 'index.html'

    logger.info(f'Render {index_file.as_posix()}')
    index_file.open('w+').write(index_template.render(root=root))

    page_template = env.get_template('page.html.j2')

    for node in root.walk():
        if node.type() == 'Document' and node.path.suffix == '.md':
            rel_path = destination / node.path.relative_to(root.path)
            rel_path.parent.mkdir(exist_ok=True, parents=True)
            page_file = rel_path.with_suffix('.html')

            logger.info(f'Render {page_file.as_posix()}')
            page_file.open('w+').write(page_template.render(
                root=root, node=node, rel_path=Path(os.path.relpath(root.path, node.path))))


def search(root: Folder, term: str):
    results = []
    regex = re.compile(term)  # TODO

    def highlight(text: str):
        return f'<span class="highlight">{text}</span>'

    file = ''
    for node in root.walk():

        if node.type() in ['Folder', 'Document']:
            file = str(node.path.as_posix())
            pos = file.find(term)
            if pos > -1:
                results.append({
                    'match': f'{file[:pos]}{highlight(term)}{file[pos + len(term):]}',
                    'file': f'{file}'
                })

        elif node.type() in ['Text', 'Heading', 'Reference', 'Code']:
            text = node.text
            pos = text.find(term)
            if pos > -1:
                results.append({
                    'match': f'{text[:pos]}{highlight(term)}{text[pos + len(term):]}',
                    'file': f'{file}'
                })

    return results


def serve_http_server(port: int, destination: Path):
    def http_handler(path: Path):
        class HttpHandler(SimpleHTTPRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, directory=path, **kwargs)

        return HttpHandler

    logger.info(
        f'Starting HTTP server at port {port} with {destination.as_posix()}')
    http_server = HTTPServer(('', port), http_handler(destination))
    webbrowser.open(f'http://localhost:{port}/index.html')
    http_server.serve_forever()


def serve_ws_server(port: int, root: Folder):
    def ws_handler(websocket: ServerConnection):
        msg = json.loads(websocket.recv())
        while msg:
            results = search(root, msg['term'])
            websocket.send(json.dumps(results))
            msg = json.loads(websocket.recv())

    logger.info(f'Starting Websocket server at port {port + 1}')
    ws_server = serve(ws_handler, 'localhost', port + 1)
    ws_server.serve_forever()
