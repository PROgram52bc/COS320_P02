import sys
import random

if len(sys.argv) != 3:
    print("Usage: python3 {} [chapters] [days]".format(sys.argv[0]))
    print("Generate input values with uniform distributions")
    print("days must be less than or equal to chapters")
    sys.exit()


chapters, days = [ int(num) for num in sys.argv[1:] ]
minVerse = 1
maxVerse = 50

if days > chapters:
    print("days must be less than or equal to chapters")
    sys.exit(-1)

verseCounts = []
for _ in range(chapters):
    verseCounts.append(random.randint(minVerse, maxVerse))

average = round(sum(verseCounts) / (len(verseCounts)-1))

print("{} {} {}".format(chapters, days, average))
for verseCount in verseCounts:
    print(verseCount)
