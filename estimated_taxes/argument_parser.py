import argparse

from . import __version__


def get_parser():
    parser = argparse.ArgumentParser(
        prog="estimated-taxes",
        usage="%(prog)s [<options>] [--] <input file>",
        description="Estimated taxes calculator",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "filename",
        type=str,
        help=argparse.SUPPRESS,
        metavar="<input file>",
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s " + __version__,
    )

    return parser
