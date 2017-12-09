i = input
o = open

def _getFileString(path):
    return o(path, "r+").read()
def _createFile(fileName, content):
    o(fileName, "w").write(content)

def createFile():
    _createFile(i('Enter FileName'), i('Enter contents'))

def countThings():
    fileString = _getFileString(i('Enter FileName'))
    c = fileString.count
    vovels, words, numbers = sum[c(v) for v in 'aeiou'], len(fileString.split(' ')), sum[c(d) for d in '1234567890']
    print("Vovels: " + str(vovels), "Numbers: " + str(numbers), "Words: " + str(words))
        
def replaceSpaces():
    fileName = i('Enter FileName')
    fileString = _getFileString(fileName)
    _createFile(fileName, fileString.replace(' ', '#'))
    
def menu():
    functs =[createFile, countThings, replaceSpaces]
    print '1. Create File\n2. Count vovels, digits, and words\n3. Replace spaces with #'
    functs[i("Do something: ")-1]()
    
menu()