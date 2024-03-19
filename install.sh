#!/bin/bash

RED='\033[0;31m'
CYAN='\033[0;36m'
GREEN='\033[0;32m'
HEART_ICON='\u2665'
NC='\033[0m' # No Color


echo -e "${GREEN}[INFO] Start TosChat installation\n${NC}"

echo -e "${GREEN}[INFO] Cloning toschat repository\n${NC}"

if [ -d "$HOME/toschat" ]; then # if toschat exists in home dir, remove
    rm -rf "$HOME/toschat"
fi

repo_url="https://github.com/MuongKimhong/toschat.git"

git clone "$repo_url" "$HOME/toschat"


echo -e "${GREEN}[INFO] Creating TosChat python3 environment...\n${NC}"

if [ -d "$HOME/toschat/.venv" ]; then # if .venv/ exists in home dir, remove
    rm -rf "$HOME/toschat/.venv"
fi

python3 -m venv $HOME/toschat/.venv

source $HOME/toschat/.venv/bin/activate

pip3 install -r $HOME/toschat/requirements.txt


# Download toschat.sh
echo -e "${GREEN}[INFO] Setting up toschat...\n${NC}"
sudo curl -o /usr/local/bin/toschat "https://raw.githubusercontent.com/MuongKimhong/toschat/master/toschat.sh"
sudo chmod +x /usr/local/bin/toschat


echo -e "${CYAN}[INFO] Installation completed\n${NC}"
echo -e "${CYAN}[INFO] To open the application run command: toschat\n${NC}"

echo -e "${CYAN}[Important Message] Code with Love ${HEART_ICON} \n${NC}"

echo -e "${CYAN}Visit https://github.com/MuongKimhong/toschat for more info.${NC}"