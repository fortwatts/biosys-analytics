#!/usr/bin/env bash
#catch common errors:
set -u

DIR=$1
FILES=$(mktemp)
find "$DIR" -type f -name \*.fast[aq] > "$FILES"
NUM_FILES=$(wc -l "$FILES" | awk '{print $1}')

if [[ $NUM_FILES -lt 1 ]]; then
    echo "No usable files in $DIR"
    exit 1
fi

echo "Found $NUM_FILES in $DIR"

i=0
while read -r FILENAME; do
    let i++	
    BASENAME=$(basename "$FILENAME")
    printf "%3d: %s\n" $i "$BASENAME"

done < "$FILES"
