import os
import re
import json
import webbrowser
from websockets.sync.server import ServerConnection, serve
from pathlib import Path
from shutil import copytree, copy, rmtree
from jinja2 import Environment, FileSystemLoader
from util.nodes import Folder
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
        if node.type() == 'Document':
            norm_path = destination / node.path.relative_to(root.path)
            norm_path.parent.mkdir(exist_ok=True, parents=True)

            if node.path.suffix == '.md':
                ext_refs = []
                int_refs = []

                for child in node.walk():
                    if child.type() in ['Reference', 'Image']:
                        if child.target.find('http') > -1:
                            ext_refs.append(child)
                        else:
                            int_refs.append(child)

                rel_path = Path(os.path.relpath(root.path, node.path))
                page_file = norm_path.with_suffix('.html')

                logger.info(f'Render {page_file.as_posix()}')
                page_file.open('w+').write(page_template.render(
                    root=root,
                    node=node,
                    rel_path=rel_path,
                    ext_refs=ext_refs,
                    int_refs=int_refs))

            else:
                logger.info(f'Copying {node.path.as_posix()} -> {norm_path.as_posix()}')
                copy(node.path, norm_path)


def search(root: Folder, term: str):
    results = {}
    regex = re.compile(term)

    file = ''
    for node in root.walk():

        if node.type() == 'Document':
            norm_path = node.path.relative_to(root.path)
            file = str(norm_path.with_suffix('').as_posix())

            for match in re.finditer(regex, file):
                if file not in results:
                    results[file] = []

                results[file].append({
                    'begin': file[:match.start()],
                    'match': match.group(),
                    'end': file[match.end():]
                })

        elif node.type() in ['Text', 'Reference', 'Code']:
            text = node.text
            for match in re.finditer(regex, text):
                if file not in results:
                    results[file] = []

                results[file].append({
                    'begin': text[:match.start()],
                    'match': match.group(),
                    'end': text[match.end():]
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
