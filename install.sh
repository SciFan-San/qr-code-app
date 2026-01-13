#!bin/sh
python -m venv .venv
source .venv/bin/activate
which python
python -m ensurepip --upgrade
echo "*" > .venv/.gitignore
pip install -r requirements.txt