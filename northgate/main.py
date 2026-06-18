# Set up logging
import sys
import argparse

from . import __version__
from .logger import logger
from .utils import get_last_version


def main():
    parser = argparse.ArgumentParser(
        description='NorthGate - p2p web sharing'
    )
    parser.add_argument(
        '--logging-level',
        required=False,
        help='Set the logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)',
        default='INFO',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    )
    parser.add_argument(
        '--web-port',
        required=False,
        help='Set the web server port',
        default=8000,
        type=int
    )
    args = parser.parse_args()

    # Set logging level based on user input
    loglevel = args.logging_level
    logger.setLevel(loglevel)

    # Start the application
    logger.info("Python version: {}".format(sys.version))
    logger.info("NorthGate version: {}".format(__version__))
    
    # Check for updates
    last_version = get_last_version()
    if last_version and last_version != __version__:
        logger.warning("A new version of NorthGate is available: {}. " \
            "You are using version {}.".format(last_version, __version__))

if __name__ == "__main__":
    main()
    