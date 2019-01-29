#!/usr/bin/env bash

set -u

if [[ $# -lt 1 ]] || [[ $# -gt 2 ]]; then
    printf "Usage: %s files/sonnet-29.txt \n" "$(basename "$0")"
    exit 1
fi

if [[ ! -f $1 ]]; then
    printf "Files/sonnet-29.txt is not a file\n"
    exit 1
fi

FILE=$1

i=0
while read -r LINE; do
    if [[ i -lt 10 ]]; then
	let i++
        printf "%3d: %s\n" $i "$LINE"
    else
        exit 1
    fi
done < "$FILE"
