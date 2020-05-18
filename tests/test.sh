#!/bin/bash
# The purpose of this file is to test the correctness of a given solution based on test files in the current directory

DIR="$(dirname ${BASH_SOURCE[0]})"
cd "$DIR"

# specify the target solution to be tested
TARGET_SCRIPT="python3 ../solution1.py"
# specify the edge case tester
EDGE_CASE_TESTER="python3 test_edge_case.py"
echo "testing on $TARGET_SCRIPT"

for INFILE in *.in; do
	ROOT=${INFILE%\.in}
	OUTFILE=${ROOT}.ans
	OUTPUT=$(eval $TARGET_SCRIPT < ${INFILE})
	# compare given output file with the generated output
	eval diff $OUTFILE <(echo "$OUTPUT") 2>&1 1>/dev/null
	ret=$?
	if [ $ret -eq 0 ]; then
		echo "PASSED...${ROOT}"
	elif [ $ret -eq 1 ]; then
		# compare first line (cost)
		if eval diff <(head -n 1 $OUTFILE) <(echo "$OUTPUT" | head -n 1) 2>&1 1>/dev/null; then
			echo "TESTING EDGE CASE...${ROOT}"
			eval $EDGE_CASE_TESTER ${INFILE} <(eval $TARGET_SCRIPT < ${INFILE})
			edge_ret=$?
			if [ $edge_ret -eq 0 ]; then
				echo "PASSED EDGE CASE"
			elif [ $edge_ret -eq 101 ]; then
				echo "FAILED EDGE CASE: day number doesn't match"
			elif [ $edge_ret -eq 102 ]; then
				echo "FAILED EDGE CASE: chapter number doesn't match"
			elif [ $edge_ret -eq 103 ]; then
				echo "FAILED EDGE CASE: cost doesn't match"
			else
				echo "Unknown edge case error"
			fi
		else
			echo "FAILED: incorrect cost...${ROOT}"
		fi
	elif [ $ret -eq 2 ]; then
		echo "ERROR...${ROOT}"
	else
		echo "UNKNOWN ERROR...${ROOT}"
	fi
done
