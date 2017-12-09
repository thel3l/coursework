i = input
List = []
def insert():
    List.append(i('Element to insert: '))

def delete():
    List.remove(i('Element to delete: '))

def display():
    print List

def menu():
    functs =[insert, delete, display]
    print '1. Insert\n2. Delete\n3. Display'
    functs[i("Do something: ")-1]()
    menu();
    
menu()