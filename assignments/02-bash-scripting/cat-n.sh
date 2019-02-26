#!/usr/bin/env bash

set -u

if [[ $# -lt 1 ]] || [[ $# -gt 2 ]]; then
    printf "Usage: %s FILE \n" "$(basename "$0")"
    exit 1
fi

if [[ ! -f $1 ]]; then
        printf "%s is not a file\n" "$1"
    exit 1
fi

FILE=$1

i=0
while read -r LINE; do
    #if [[ i -lt 10 ]]; then
        i=$((i+1))
        printf "%s %s\n" $i "$LINE"
    #fi
done < "$FILE"

