#!/bin/bash
DIR="$(dirname ${BASH_SOURCE[0]})"

DEST="${DIR}/../tests"
INPUT_SCRIPT="python3 ${DIR}/generate_input.py"
OUTPUT_SCRIPT="python3 ${DIR}/../solution1.py"

function generate() {
	for ((i=0; i<COUNT; i++)); do
		echo "writing input to '${DEST}/${PREFIX}_${i}.in'..."
		eval $INPUT_SCRIPT $CHAPTERS $DAYS > "${DEST}/${PREFIX}_${i}.in"
		echo "writing output to '${DEST}/${PREFIX}_${i}.ans'..."
		eval $OUTPUT_SCRIPT < "${DEST}/${PREFIX}_${i}.in" > "${DEST}/${PREFIX}_${i}.ans"
	done
}

# easy ones with no failure
PREFIX="easy"
COUNT=20
CHAPTERS=10
DAYS=5
generate

# # small numbers (possibly with impossibles)
# PREFIX="small"
# COUNT=10
# GOAL=10
# MIN=0
# MAX=3
# generate
# 
# # generate big sized input (possibly with impossibles)
# PREFIX="big_size"
# COUNT=5
# GOAL=500000
# MIN=0
# MAX=10
# generate
