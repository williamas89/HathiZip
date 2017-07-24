import argparse
import os
import shutil

import hathizip
from hathizip import process, configure_logging
from hathizip.utils import has_subdirs


def get_parser()->argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=hathizip.__description__)

    parser.add_argument(
        '--version',
        action='version',
        version=hathizip.__version__
    )

    parser.add_argument(
        "path",
        help="Path to the HathiTrust folders to be zipped"
    )
    parser.add_argument(
        "--remove",
        action="store_true",
        help="Remove original files after successfully zipped"
    )

    debug_group = parser.add_argument_group("Debug")

    debug_group.add_argument(
        '--debug',
        action="store_true",
        help="Run script in debug mode")
    debug_group.add_argument("--log-debug", dest="log_debug", help="Save debug information to a file")

    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    logger = configure_logging.configure_logger(debug_mode=args.debug, log_file=args.log_debug)
    if not has_subdirs(args.path):
        logger.error("No directories found at {}".format(args.path))
    for folder in filter(lambda x: x.is_dir(), os.scandir(args.path)):
        process.compress_folder(folder.path, dst=args.path)
        if args.remove:
            shutil.rmtree(folder.path)
            logger.info("Removing {}.".format(folder.path))


if __name__ == '__main__':
    main()
