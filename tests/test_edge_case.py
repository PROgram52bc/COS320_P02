""" This script checks if certain output file has the valid plan for its given cost """
import sys
import fileinput

def cost(nverse, avgverse):
    return pow(nverse-avgverse, 2)

if len(sys.argv) != 3:
    print("Usage: python3 {} [input_file] [output_file]".format(sys.argv[0]))
    print("Test whether the output file is a valid output for the input file")
    print("Returns 100 when parameters do not match")
    print("Returns 101 when day number does not match")
    print("Returns 102 when chapter number does not match")
    print("Returns 103 when cost does not match")
    sys.exit(100)

inFileName, outFileName = [ f for f in sys.argv[1:] ]

with fileinput.input(files=(inFileName)) as f:
    inLines = [ line.rstrip('\n') for line in f ]

with fileinput.input(files=(outFileName)) as f:
    outLines = [ line.rstrip('\n') for line in f ]

outChapterPerDay = [ int(line) for line in outLines[2:] ]

m,n,average = [ int(n) for n in inLines[0].split(" ") ]

if len(outChapterPerDay) != n:
    sys.exit(101) # day number doesn't match

if sum(outChapterPerDay) != m:
    sys.exit(102) # chapter number doesn't match

# Check if the total cost match the given schedule
outCost = int(outLines[0])
actualCost = 0
inVersePerChapter = [ int(line) for line in inLines[1:] ]

inVersePerChapterIt = iter(inVersePerChapter)

for nChapter in outChapterPerDay:
    verses = 0
    for _ in range(nChapter):
        verses += next(inVersePerChapterIt)
    actualCost += cost(verses, average)

if actualCost != outCost:
    sys.exit(103) # cost doesn't match

