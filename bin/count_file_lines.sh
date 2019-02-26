#!/usr/bin/env bash
#catch common errors:
set -u


FILE=$1
while read -r LINE; do
echo "LINE \"$LINE\""
done < "$FILE"

#i=0
#while read -r FILENAME; do
#    echo "entered while loop."
#    let i++	
#    BASENAME=$(basename "$FILENAME")
#    printf "%3d: %s %s\n" $i "$BASENAME"
#done < "$FILE"
