# NorthGate
P2P web hosting with end-to-end encryption.

## Requirements

- Git client
- Python >= `3.15`

## Installation

```bash
# Clone the repository
git clone git@github.com:NorthGate-org/NorthGate.git
cd NorthGate

# Install virtual environment and run for Windows
run_windows.bat

# Install for Mac or Linux
pip -m venv env
source env/bin/activate
pip install -r requirements.txt

# Or install the package
pip install -e .
```

## Usage

### Basic Usage

```bash
# Run on Windows
run_windows.bat

# Run directly in folder
python -m northgate.main --logging-level INFO --web-port 8000

# Run as installed package
northgate --logging-level INFO --web-port 8000
```

# Documentation

- [Phase 1: Summary](docs/phase%201/summary.md)
- [Contributing guide](CONTRIBUTING.md)

More coming soon.
