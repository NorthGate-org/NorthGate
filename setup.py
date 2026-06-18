from setuptools import setup, find_packages
from northgate import __version__

def get_install_requires():
    with open("requirements.txt") as f:
        return f.read().splitlines()

setup(
    name="northgate",
    version=__version__,
    description="NorthGate - p2p web sharing",
    author="NorthGate-org",
    packages=find_packages(),
    install_requires=get_install_requires(),
    python_requires=">=3.15",
    entry_points={
        "console_scripts": [
            "northgate=northgate.main:main",
        ],
    },
)
