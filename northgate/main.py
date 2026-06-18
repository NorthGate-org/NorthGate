# Set up logging
import sys
import argparse

from .logger import logger


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
    args = parser.parse_args()

    # Set logging level based on user input
    loglevel = args.logging_level
    logger.setLevel(loglevel)

    # Start the application
    logger.info("Python version: {}".format(sys.version))


if __name__ == "__main__":
    main()
    