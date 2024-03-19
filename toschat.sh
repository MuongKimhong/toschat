#!/bin/bash


RED='\033[0;31m'
NC='\033[0m' # No Color


if [ -d "$HOME/toschat" ]; then # if toschat exists in home dir, remove
    source $HOME/toschat/.venv/bin/activate
    python3 $HOME/toschat/src/main.py
else
    echo -e "${RED}\n[TosChat error] toschat not found. Please install toschat first.${NC}"
    exit 0
fi