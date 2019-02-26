#!/usr/bin/env bash
#catch common errors:
set -u

echo "Hello World!"
NAME="Newman"
echo "Hello," $NAME
NAME="Jerry"
echo "Hello, $NAME"

ARG=$1
if [[ -f "$ARG" ]]; then
    echo "number of lines in your input file is:"
    wc -l "$ARG"
    exit
else
    echo "$ARG must be a file"
    exit 1
fi

