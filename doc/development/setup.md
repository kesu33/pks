# Linux Development Setup

## Requirements
- Linux, Python 3.10+, Git

## Install (Ubuntu/Debian)
    sudo apt update
    sudo apt install -y python3 python3-venv python3-pip git

## Activate
    cd /mnt/external/proj/pks
    source .venv/bin/activate

## Start API
    uvicorn app.main:app --reload

## Tests
    pytest -q

## VS Code
    code /mnt/external/proj/pks
