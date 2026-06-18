from setuptools import setup, find_packages

setup(
    name="northgate",
    version="0.1.0",
    description="NorthGate - p2p web sharing",
    author="NorthGate-org",
    packages=find_packages(),
    install_requires=[
        "attrs==26.1.0",
        "Automat==25.4.16",
        "certifi==2026.6.17",
        "charset-normalizer==3.4.7",
        "constantly==23.10.4",
        "hyperlink==21.0.0",
        "idna==3.18",
        "Incremental==24.11.0",
        "ipaddress==1.0.23",
        "netifaces==0.11.0",
        "ntplib==0.4.0",
        "packaging==26.2",
        "pyp2p==0.8.3",
        "pyroute2==0.9.6",
        "requests==2.34.2",
        "Twisted==26.4.0",
        "typing_extensions==4.15.0",
        "urllib3==2.7.0",
        "win-inet-pton==1.1.0",
        "zope.interface==8.5",
    ],
    python_requires=">=3.15",
    entry_points={
        "console_scripts": [
            "northgate=northgate.main:main",
        ],
    },
)
