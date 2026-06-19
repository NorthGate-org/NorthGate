# Phase 1 summary

## Application goal

NorthGate aims to provide peer-to-peer web sharing for small static websites. In Phase 1, the application should let a site owner define local websites, publish selected sites over a P2P service, and allow other P2P users to request those sites securely.

The Phase 1 goal is to support static website sharing only: HTML, CSS, and image files served through `GET` requests. Dynamic backends, write requests, JavaScript APIs, forms, databases, and server-side application logic are outside the Phase 1 scope.

## Tech stack used so far

- Python package: `northgate`
- Python entry point: `northgate.main:main`
- CLI and argument parsing: Python `argparse`
- Logging: Python `logging` with a custom colored formatter
- HTTP/version metadata lookup: `requests`
- Static site configuration format: YAML through `site.yaml`
- Packaging: `setuptools` with `setup.py`
- Dependency management: `requirements.txt`
- Windows launcher: `run_windows.bat`
- Planned P2P layer dependencies already listed: `pyp2p`, `Twisted`, `websockets`, `netifaces`, `ntplib`, and related networking packages
- Planned encryption dependencies already listed: `cryptography`, `cffi`, and `pycparser`
- Local database with `sqlite`, self-created and migrated at start

## General project structure

```text
NorthGate/
├── northgate.db
├── README.md
├── requirements.txt
├── run_windows.bat
├── setup.py
├── docs/
│   └── phase 1/
│       └── summary.md
├── northgate/
│   ├── __init__.py
│   ├── constants.py
│   ├── logger.py
│   ├── main.py
│   └── utils.py
├── sites/
│   └── Example 1/
│       ├── index.html
│       ├── site.yaml
│       └── assets/
└── tests/
```

### Important paths

- `northgate/`: main Python package for the application code.
- `northgate/app.py`: Application endpoints.
- `northgate/main.py`: CLI startup point for NorthGate.
- `northgate/logger.py`: shared logger configuration.
- `northgate/constants.py`: shared constants such as the latest-version URL.
- `northgate/utils.py`: utility functions, currently including latest-version lookup.
- `sites/`: local folder where owner-created sites are stored.
- `sites/<site name>/site.yaml`: per-site metadata and sharing configuration.
- `sites/<site name>/index.html`: default HTML entry file for a shared site.
- `sites/<site name>/assets/`: static CSS, image, and other supported asset files.
- `tests/` : The TDD and unit tests.
- `docs/`: development and planning documentation.

## Phase 1 feature scope

### P2P service

Phase 1 should introduce a P2P service that allows NorthGate users to discover and request owner-published static sites without relying on a traditional central web host.

The service should expose only sites that the owner has chosen to make public. Private sites should remain local and should not be announced to other peers.

### Local website serving

NorthGate should open a local website server on an available port. The default port should be `8000`, and the application should fall back to another available port if `8000` is already in use.

This local server is responsible for serving owner-created static sites from the `sites/` directory.

### Website list

The application should maintain a list of owner-created sites by reading the folders under `sites/` and their `site.yaml` files.

Each site should have enough metadata to support listing, visibility, access control, and P2P sharing.

### Public and private sites

Each site should be configurable as either public or private.

- Public sites can be announced through the P2P service and requested by other peers.
- Private sites remain local and should not be visible to other P2P users.

### Password-protected sites

Phase 1 should allow a site owner to add a password requirement to a site. When a password is configured, a peer must provide the correct password before receiving the site content.

Password protection is separate from P2P encryption: encryption protects peer-to-peer transport, while the site password controls access to an individual site.

### Static GET request support

Phase 1 should only support `GET` requests for static files.

Supported file types:

- HTML files
- CSS files
- Image files

Unsupported in Phase 1:

- `POST`, `PUT`, `PATCH`, and `DELETE` requests
- Server-side scripts
- Dynamic API routes
- Database-backed pages
- File uploads

### End-to-end encryption

Phase 1 should add end-to-end encryption between P2P users. Each user should generate a public key and a private key.

- The public key can be shared with other peers.
- The private key must remain local to the user.
- P2P traffic should be encrypted so that site data is protected while it moves between peers.

### Site definitions with `site.yaml`

Each shared website should be defined by a `site.yaml` file inside its site folder.

Expected folder pattern:

```text
sites/
└── My Site/
		├── site.yaml
		├── index.html
		└── assets/
				├── styles.css
				└── image.png
```

The `site.yaml` file should describe the site metadata and sharing settings, such as:

```yaml
name: My Site
visibility: public
password: null
entry: index.html
allowed_extensions:
	- .html
	- .css
	- .png
	- .jpg
	- .jpeg
	- .gif
	- .webp
```

## Phase 1 completion target

Phase 1 is complete when NorthGate can discover local site folders, read their `site.yaml` files, serve supported static files locally on port `8000` or the next available port, publish public sites through the P2P service, keep private sites hidden, enforce optional site passwords, and encrypt P2P communication with generated public/private keys.

