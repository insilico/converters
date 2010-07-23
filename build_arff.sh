#!/bin/bash

if [[ $# -lt 3 ]]; then
	echo Usage: $0 CHROMOSOME_1 CHROMOSOME_2 OUT_FILE
	exit
fi

rel=`mktemp -p ~/scratch/tmp`
dat=`mktemp -p ~/scratch/tmp`

echo @RELATION $1$2 > rel
echo @DATA > dat

cat rel ~/scratch/formats/attr/{combos/$1$2,Class}.attr dat ~/scratch/formats/data/combos/$1$2.data > $3

rm rel dat
