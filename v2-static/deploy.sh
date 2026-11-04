#!/bin/sh
# Copy the built static site to the server. Refuses to copy if a forbidden phrase
# is in the built pages (see check_phrases.py). Run build.py first after editing master.html.
set -e
cd "$(dirname "$0")"
python3 check_phrases.py
rsync -av --exclude '.git' --exclude '*.py' --exclude '__pycache__' --exclude 'deploy.sh' --exclude 'master.html' \
  ./ root@47.89.176.201:/opt/regent-v2/
