#!/bin/bash
DIR="$(dirname ${BASH_SOURCE[0]})"
cd "$DIR"

TARGET_SCRIPT="python3 ../solution1.py"
echo "testing on $TARGET_SCRIPT"

for INFILE in *.in; do
	ROOT=${INFILE%\.in}
	OUTFILE=${ROOT}.ans
	eval $TARGET_SCRIPT < ${INFILE} | diff $OUTFILE -
	ret=$?
	if [ $ret -eq 0 ]; then
		echo "PASSED...${ROOT}"
	elif [ $ret -eq 1 ]; then
		echo "FAILED...${ROOT}"
	elif [ $ret -eq 2 ]; then
		echo "ERROR...${ROOT}"
	else
		echo "UNKNOWN ERROR...${ROOT}"
	fi
done
