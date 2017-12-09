def linearSearch(target, numbers):
    for i in range(len(numbers)):
        if numbers[i]==target:
            return i
            
def binarySearch(sortedList, item, start=None, end=None):
    if(start>end): return(False)
    if(start==None): start = 0
    if(end==None): end = len(sortedList)-1
    midpoint = (start+end)/2
    
    if(item == sortedList[midpoint]): return(midpoint)
    elif(item > sortedList[midpoint]): return(binarySearch(sortedList, item, midpoint+1, end))
    elif(item < sortedList[midpoint]): return(binarySearch(sortedList, item, start, midpoint-1))