import sys
import signal
from threading import Thread
from argparse import ArgumentParser, ArgumentTypeError
from pathlib import Path
from util.nodes import Folder, Document
from formats.md import MD
from util.lexer import Lexer
from export.html import export_html, serve_http_server, serve_ws_server
from util.logging import get_logger


logger = get_logger(__name__)


def sigint_handler(signal, frame):
    sys.exit(1)

signal.signal(signal.SIGINT, sigint_handler)


def traverse(path: Path, base: Path) -> Folder:
    root : Folder = Folder(path)

    for entry in path.glob('*'):
        if entry.is_file():
            if entry.suffix == '.md':
                logger.info(f'Processing {entry.relative_to(base).as_posix()}')
                tokens = Lexer(entry).tokenize()
                document = MD(entry, tokens).parse()
                root.add(document)
            else:
                root.add(Document(entry))
        else:
            root.add(traverse(entry, base))
    
    return root


def Port(port):
    port = int(port)
    if 0x0400 < port < 0xffff:
        return port
    raise ArgumentTypeError(f'Port must be between {0x0400} and {0xffff} but is {port}')


def main():
    parser = ArgumentParser(
        'Markdown Export',
        description='Export a collection of structured markdown files to another format.')

    parser.add_argument('-f', '--folder', required=True, type=Path,
                        help='Folder with markdown files to process.')
    
    parsers = parser.add_subparsers(dest='export')

    # sqlite_parser = parsers.add_parser('SQLite')
    # sqlite_parser.add_argument('-d', '--database', required=True, type=Path,
    #                            help='File to export the database')

    html_parser = parsers.add_parser('HTML')
    html_parser.add_argument('-a', '--assets', required=False, type=Path,
                             help='Folder to the assets files.')
    html_parser.add_argument('-c', '--clear', required=False, action='store_true', default=True,
                             help='Clear existing files before exporting.')
    html_parser.add_argument('-d', '--destination', required=True, type=Path,
                             help='Folder to write the export.')
    html_parser.add_argument('-p', '--port', required=False, type=Port,
                             help='HTTP port to serve the files written to the destination.')
    html_parser.add_argument('-t', '--templates', required=True, type=Path, default=9000,
                             help='Folder to the template files.')

    args = parser.parse_args()

    root : Folder = traverse(args.folder, args.folder)

    if args.export == 'HTML':
        export_html(args.assets, args.templates, args.destination, args.clear, root=root)

        if args.port:
            http_thread = Thread(target=serve_http_server, args=(args.port, args.destination))
            ws_thread = Thread(target=serve_ws_server, args=(args.port, root))

            try:
                http_thread.start()
                ws_thread.start()
            except KeyboardInterrupt:
                http_thread.join()
                ws_thread.join()


if __name__ == '__main__':
    main()
