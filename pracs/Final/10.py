i = input

def selectionSort(List):
    SortedList = []
    while(len(List)>0):
        minimum, minimumIndex = 9999, -1
        for i in range(len(List)):
            if List[i]<minimum:
                minimum, minimumIndex = List[i], i
        SortedList.append(List.pop(i))
    return SortedList
    
def bubbleSort(List):
    sortedFlag = False
    while(not sortedFlag):
        sortedFlag = True
        for i in range(len(List)-1):
            if(List[i]>List[i+1]):
                sortedFlag = False
                List[i], List[i+1] = List[i+1], List[i]
    return List
    
def insertionSort(List):
    separator = 0
    
    
def doSelectionSort():
    print("Sorted list: " + str(selectionSort(i("Enter list"))))

def doBubbleSort():
    print("Sorted list: " + str(bubbleSort(i("Enter list"))))
    
def doInsertionSort():
    print("Sorted list: " + str(insertionSort(i("Enter list"))))

def menu():
    functs = [doSelectionSort, doBubbleSort, doInsertionSort]
    print '1. Selection Sort\n2. Bubble Sort\n3. Insertion Sort'
    functs[i("Do something: ")-1]()
    
menu()