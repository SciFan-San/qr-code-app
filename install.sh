#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate
which python
python3 -m ensurepip --upgrade
echo "*" > .venv/.gitignore
pip install -r requirements.txt