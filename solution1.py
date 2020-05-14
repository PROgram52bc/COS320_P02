from itertools import accumulate
import fileinput

lines = [ line.rstrip('\n') for line in fileinput.input() ]
m,n,average = [ int(n) for n in lines[0].split(" ") ]
verseCounts = [0]

if m == n:
    print(pow(int(lines[1]) - average, 2) * m)
    print()
    for i in range(m):
        print('1')
else:
    for num in lines[1:]:
        verseCounts.append(int(num))
        

    ## test data
    # m = 10
    # n = 5
    # average = 6
    # average = round(sum(verseCounts) / (len(verseCounts)-1))
    # verseCounts = [0,1,5,9,2,3,4,4,8,10,11]

    cumVerseCounts = list(accumulate(verseCounts))
    print(cumVerseCounts)

    def cost(start, end, average=average):
        """ return the cost of reading from start to end (inclusive), calculating against average

        :start: the starting chapter. 0<start<=m
        :end: the ending chapter. 0<start<=m
        :average: an average to be calculated against
        :returns: the cost

        """
        if end < start:
            raise ValueError("end cannot be greater than start")
        return pow((cumVerseCounts[end]-cumVerseCounts[start-1])-average, 2)


    table = {}
    table[1] = {}
    # calculate the cost of reading everything using one day
    # ni = 1
    for mi in range(1, m+1):
        table[1][mi] = { 'cost': cost(1, mi), 'submi': 0 }



    # ni: the current day being calculated
    # mi: the number of chapters considered
    for ni in range(2, n+1):
        table[ni] = {}
        for mi in range(ni, m+1):
            subni = ni - 1 # previous day is the subni'th day
            # iterate through the possible number of chapters read on that day
            # if reading subni chapters in the previous subni days
            submi = subni
            table[ni][mi] = { 'cost': table[subni][submi]['cost'] + cost(ni, mi), 'submi': submi }
            
            # now compare with reading more chapters in the previous subni days
            for submi in range(
                    subni+1, # starting from reading subni+1 chapters
                    mi, # ending with mi-1 chapters (1 chapter left for the current day)
                    ):
                # The cost of reading submi chapters in the previous subni days
                # plus the cost of reading the remaining chapters on the current day
                newCost = table[subni][submi]['cost'] + cost(submi+1, mi) 
                if newCost < table[ni][mi]['cost']:
                    table[ni][mi]['cost'] = newCost
                    table[ni][mi]['submi'] = submi

    cost = table[n][m]['cost']
    print(table)
    submis = [m]
    submi = m
    subni = n
    while subni > 1:
        submi = table[subni][submi]['submi']
        submis[0] -= submi # change from cumulative to normal
        submis.insert(0, submi)
        subni -= 1

    print(cost)
    print()
    for submi in submis:
        print(submi)
