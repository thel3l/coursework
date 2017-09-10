N = int(raw_input("Enter the number of terms: "))
VectorAddition = 0
for i in range(N):
    GarbageString = list(i)
    GarbageStringLength = len(GarbageString)
    for x in range(0,GarbageStringLength):
        Vector = GarbageString[x]
        VectorAddition = VectorAddition + Vector**3

    if i == VectorAddition:
        print "We've got an Armstrong number at ", i
