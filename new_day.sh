#!/bin/bash
# creates a new dayN project with uv and a src/main.py layout
set -e

if [ -z "$1" ]; then
    echo "usage: ./new_day.sh <day_number>"
    exit 1
fi

DIR="projects/day$1"

if [ -d "$DIR" ]; then
    echo "error: $DIR already exists"
    exit 1
fi

mkdir -p "$DIR"
cd "$DIR"
uv init --no-workspace
mkdir src
mv main.py src/main.py

echo "created $DIR"
