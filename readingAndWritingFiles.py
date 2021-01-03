import os
a= os.path.join('usr', 'bin', 'spam')
print(a) #usr/bin/spam
#On Windows, paths are written using backslashes (\) as the separator between folder names. OS X and Linux, however,
# use the forward slash (/) as their path separator. If you want your programs to work on all operating systems, you will have to write your Python scripts to handle both cases. Fortunately, this is simple to do with the os.path.join() function. If you pass it the string values of individual file and folder names in your path, os.path.join() will return a string with a file path using the correct path separators.

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('/Users/dibozit', filename))
# /Users/dibozit/accounts.txt
# /Users/dibozit/details.csv
# /Users/dibozit/invite.docx

#current working directory
print(os.getcwd()) #get current working directory /Users/dibozit/PycharmProjects/AutomateTheBoringStuffWithPython
# print(os.chdir('/Users/dibozit')) #change direction (değiştirmedim değişmesini istemediğim için

#Relative Paths

# A single period (“dot”) for a folder name is shorthand for “this directory.” Two periods (“dot-dot”) means “the parent folder.”
# current folder is bacon:
#abs path                 relative path
# C:\                     >   ..\
# C:\bacon                >   .\
# C:\bacon\fizz           >   .\fizz
# C:\bacon\fizz\spam.txt  >   .\fizz\spam.txt
# C:\bacon\spam.txt       >   .\spam.txt
# C:\eggs                 >   ..\eggs
# C:\eggs\spam.txt        >   ..\eggs\spam.txt
# C:\spam.txt             >   ..\spam.txt

#make directions:
#os.makedirs('./delicious/walnut/waffles') bir defa oluşturdu, tekrar tekrar çalışmıyor

print(os.path.abspath('.')) #converts relative path to absolute path
print(os.path.abspath('./delicious/walnut')) #converts relative path to absolute path
print(os.path.isabs('.')) #return true if the argument is an abs path, this case false
print(os.path.isabs(os.path.abspath('.'))) #true
print(os.path.relpath('/Users/dibozit/PycharmProjects/AutomateTheBoringStuffWithPython/delicious/walnut',
                      '/Users/dibozit/PycharmProjects/AutomateTheBoringStuffWithPython')) #delicious/walnut
print(os.path.relpath('/Users/dibozit/Documents/Adobe',
                      '/Users/dibozit/PycharmProjects/AutomateTheBoringStuffWithPython')) #../../Documents/Adobe
#Calling os.path.relpath(path, start) will return a string of a relative path from the start path to path. If start is not provided, the current working directory is used as the start path.

path = '/Users/dibozit/PycharmProjects/AutomateTheBoringStuffWithPython/everybodyGotChoices.py'
print(os.path.basename(path)) #everybodyGotChoices.py
print(os.path.dirname(path)) #/Users/dibozit/PycharmProjects/AutomateTheBoringStuffWithPython
print(os.path.split(path)) #('/Users/dibozit/PycharmProjects/AutomateTheBoringStuffWithPython', 'everybodyGotChoices.py')
print(path.split(os.path.sep)) #['', 'Users', 'dibozit', 'PycharmProjects', 'AutomateTheBoringStuffWithPython', 'everybodyGotChoices.py']

print(os.path.getsize(path)) #gives path size
print(os.listdir('/Users/dibozit/PycharmProjects/')) #list of filename strings for each file in the pathcargument

#belli bi direction'daki tüm dosyaların toplam boyutunu öğrenmek için:
totalSize = 0
for filename in os.listdir('/Users/dibozit/PycharmProjects/'):
    totalSize += os.path.getsize(os.path.join('/Users/dibozit/PycharmProjects/',filename))
print(totalSize)

#check path validity
a= os.path.exists('/Users/dibozit/PycharmProjects/AutomateTheBoringStuffWithPython')
b= os.path.exists('/Users/dibozit/PycharmProjects/madeUp')
c= os.path.isdir('/Users/dibozit/PycharmProjects/AutomateTheBoringStuffWithPython')
d= os.path.isfile('/Users/dibozit/PycharmProjects/AutomateTheBoringStuffWithPython/everybodyGotChoices.py')
e= os.path.exists('/Volumes') #checks whether there is a dvd or flash drive currently attached to the computer,
# /volumes external mounted'ları gösterir

print(a) #true
print(b) #false
print(c) #true
print(d) #true

#opening files, reading and writing content
helloFile = open('/Users/dibozit/PycharmProjects/AutomateTheBoringStuffWithPython/hello.txt') #will open the file in reading plaintext mode
helloContent = helloFile.read()
print(helloContent) #içinde yazanı getiriyor, bizimkinde Hello world! yazıyor

sonnetFile = open('sonnet29.txt')
print(sonnetFile.readlines()) #böyle çağırdığımda satırlar halinde output alıyorum

baconFile = open("bacon.txt", 'w') #böyle bir text yoktu, 'w' ile çağırdığım için öncelikle dosyayı yarattı
baconFile.write('Hello World!\n') #içine bunu ekledi
baconFile.close() #kaydedip kapattı

baconFile = open("bacon.txt", 'a') #append modda açtım, şimdi içine ekleme yapıcam, write ile çağırsaydım eklemez,
# direkt olarak üstüne yazardı
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
baconFile = open("bacon.txt")
content = baconFile.read()
baconFile.close()
print(content)

#Saving Variables with the SHELVE MODULE

import shelve
shelfFile = shelve.open('mydata')
cats = ['Nada', 'Kedis', 'Morty', 'Casper']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
type(shelfFile)  #<class 'shelve.DbfilenameShelf'> type'ını gördük
shelfFile['cats'] #['Nada', 'Kedis', 'Morty', 'Casper'] , kontrol etmek için açtık
shelfFile.close()

# Just like dictionaries, shelf values have keys() and values() methods that will return list-like values of the keys
# and values in the shelf. Since these methods return list-like values instead of true lists, you should pass them to the list() function to get them in list form.

shelfFile = shelve.open('mydata')
list(shelfFile.keys()) #['cats']
list(shelfFile.values()) #[['Nada', 'Leo', 'Pamuk', 'Kedis', 'Morty', 'Casper']]
shelfFile.close()

#Saving Variables with the pprint.pformat() function
# pprint.pprint() function will “pretty print” the contents of a list or dictionary to the screen, while the pprint.pformat() function will return this same text as a string instead of printing it. Not only is this string formatted to be easy to read, but it is also syntactically correct Python code. Say you have a dictionary stored in a variable and you want to save this variable and its contents for future use. Using pprint.pformat() will give you a string that you can write to .py file. This file will be your very own module that you can import whenever you want to use the variable stored in it.

import pprint
cats = [{'name':'Nada', 'desc':'best cat ever'}, {'name':'Leo', 'desc': 'fluffy beauty'}]
print(pprint.pformat(cats)) #[{'desc': 'best cat ever', 'name': 'Nada'}, {'desc': 'fluffy beauty', 'name': 'Leo'}]
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n') #böyle py dosyası olarak kaydetti
fileObj.close()

import myCats
print(myCats.cats) #[{'desc': 'best cat ever', 'name': 'Nada'}, {'desc': 'fluffy beauty', 'name': 'Leo'}]
print(myCats.cats[0]) #{'desc': 'best cat ever', 'name': 'Nada'}
print(myCats.cats[0]['name']) #Nada
