#!/bin/bash

set -u

if [[ $# -eq 0 ]]; then
    REGEX='A-Z'
#    echo "REGEX is set to: $REGEX because args = 0"
elif [[ $1 =~ ^['['] ]]
then
    REGEX=$1
    REGEX=${REGEX//[}
    REGEX=${REGEX//]}
#    echo "REGEX has had brackets removed: $REGEX"
else
    REGEX="$1"
fi

UPPERCASEREGEX=${REGEX^^}
#echo "UPPERCASEREGEX is set to : $UPPERCASEREGEX"

i=0
for FILENAME in $(ls -f1 ../../data/gapminder | sort); do
    if [[ $FILENAME =~ ^[$UPPERCASEREGEX] ]]; then
        BASENAME=$(basename $FILENAME '.cc.txt')
	i=$((i+1))
        echo "$BASENAME"
    fi
done

if [[ $i -eq 0 ]]; then
    echo "There are no countries starting with \"$REGEX\""
    exit 1
fi
