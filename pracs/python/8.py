i = input

List = []

def insert():
    x = int(i("Enter int"))
    for c in range(len(List)):
        if(x>List[c]):
            List.insert(i, c)
def delete():
    

def menu():
    functs = [insert, delete]
    print '1. Insertion in a sorted list \n2. Deletion of an element from a list'
    functs[i("Do something: ")-1]()
    
menu()