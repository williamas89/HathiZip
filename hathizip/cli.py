import argparse
import os
import logging

from hathizip import process, configure_logging
import hathizip

GOOD_FOLDER = r"D:\hathigood"


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
    # TODO: Add argument to delete folder when done
    parser.add_argument(
        "--save-report",
        dest="report_name",
        help="Save report to a file"
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
    logger.info("Starting")
    for folder in filter(lambda x: x.is_dir(), os.scandir(GOOD_FOLDER)):
        process.compress_folder(folder.path, dst=GOOD_FOLDER)
        # TODO: delete file after if requested


if __name__ == '__main__':
    main()
