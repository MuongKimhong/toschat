#!/bin/bash


git pull origin master

ttab "cd $PWD/websocket/; npm start"

ttab "cd $PWD; source .venv/bin/activate; python3 server/manage.py runserver" 

ttab "cd $PWD; source .venv/bin/activate; textual console"

ttab "cd $PWD; source .venv/bin/activate"

code .
