import requests

from .logger import logger
from .constants import LAST_VERSION_URL

# Get latest version of NorthGate from GitHub
def get_last_version():
    try:
        logger.debug("Fetching latest version from: {}".format(LAST_VERSION_URL))
        response = requests.get(LAST_VERSION_URL)
        logger.debug("Received response with status code: {}".format(response.status_code))
        if response.status_code == 200:
            content = response.text
            for line in content.splitlines():
                if line.startswith("__version__"):
                    latest_version = line.split("=")[1].strip().strip('"')
                    return latest_version
    except Exception as e:
        logger.error("Error fetching latest version: {}".format(e))
    return None
