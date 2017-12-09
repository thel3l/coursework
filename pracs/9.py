i = input

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

def doLinearSearch():
    index = linearSearch(i("Enter list: "), i("Enter target: "))
    print("Index of item: " + str(index))

def doBinarySearch():
    index = binarySearch(i("Enter sorted list: "), i("Enter target: "))
    print("Index of item: " + str(index))

def menu():
    functs = [doLinearSearch, doBinarySearch]
    print '1. Linear Search\n2. Binary Search'
    functs[i("Do something: ")-1]()
    
menu()