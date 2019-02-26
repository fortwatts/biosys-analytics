#!/usr/bin/env bash

set -u

if [[ $# -lt 1 ]] || [[ $# -gt 2 ]]; then
    printf "Usage: %s FILE [NUMLINES]\n" "$(basename "$0")"
    exit 1
fi

FILE=$1
NUM_ITERATIONS=${2:-3}

if [[ ! -f "$FILE" ]]; then
	printf "$FILE is not a file\n"
	exit 1
fi

i=0
while read -r LINE; do
    if [[ i -lt $NUM_ITERATIONS ]]; then
    i=$((i+1))
    printf "%s\n" "$LINE"
    fi
done < "$FILE"

