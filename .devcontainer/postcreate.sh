#!/bin/env bash
git config --global --add safe.directory "$(git rev-parse --show-toplevel)"
git config --local --get include.path | grep -e ../.gitconfig || git config --local --add include.path ../.gitconfig

# Instruct the container to always load your environment on startup
pushd "$(git rev-parse --show-toplevel)" || exit 1
if [ -f "requirements.txt" ];then 
  pip3 install --break-system-packages --user -r requirements.txt || echo No "requirements.txt" file
fi
if [ -f "Pipfile" ];then
  pipenv install || echo no "Pipfile" file
fi
popd || exit 1
