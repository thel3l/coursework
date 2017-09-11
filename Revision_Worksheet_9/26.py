Num = [3, -5, 1, 3, 7, 0, -15, 3, -7, -8]
negativeStack = []
positiveStack = []

for n in Num:
    if(n>=0):
        positiveStack.append(n)
    else:
        negativeStack.append(n)

resultStack = negativeStack + positiveStack