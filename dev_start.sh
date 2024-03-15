#!/bin/bash


git pull origin master

ttab "cd $PWD; source .venv/bin/activate; textual console"

ttab "cd $PWD; source .venv/bin/activate"

code .
