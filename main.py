
from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")


def createfile():
    try:
        readfileandfolder()
        name = input("Please tell your file name :-")
        p = Path(name)
        if not p.exists():
            with open(p , "w") as fs:
                data = input("what you want to write in this file :-")
                fs.write(data)
            
            print(F"FILE CREATED SUCCEESFULY !")
        else:
            print("this file already exist")    

    except Exception as err:
        print(f"An error occured as {err}")


def readfile():
    try:
        readfileandfolder()
        name = input("Which file want to read :-")
        p = Path(name)
        if not p.exists() and p.is_file():
            with open(p , "r") as fs:
                data = fs.read()  
                print(data)

            print("READED SUCCESSFULY!")
        else:
             print("The file doesnot exist")
    except Exception as err:
        print(f"An error occured as {err}")  


def updatefile():
    try:
        readfileandfolder()
        name = input("which update to file :-")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing the name of your file :-")
            print("Press 2 for overwriting the name of your file :-")
            print("Press 3 for appending some content in your file :-")

            res = int(input("tell your response :"))

            if res == 1:
                name2 = input("tell your new file name")
                p2 = Path(name2)
                p.rename(p2)
            
            if res == 2:
                with open(p,"w") as fs:
                    data = input("tell what you want to write this is overwrite the data")
                    fs.write(data)

            if res == 3:
                    with open(p,"r") as fs:
                         data = input("tell what you want to write this is append the data")
                         fs.write(""+data)

    except Exception as err:
                    print(f"an error occoured as {err}")


def deletfile():
    try:
        readfileandfolder()
        name = input("which file want to delete :-")
        p = Path(name) 
        if p.exists() and p.is_file():
             os.remove(p)

             print("FILE REMOVE SUICCESFULLY")
        else:
             print("No such file exist")

    except Exception as err:
         print(f"An error occured as {err}") 

print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deletion a file")

check = int(input("Please tell your response :-"))

if check == 1:
    createfile()

if check == 2:
     readfile()

if check == 3:
     updatefile()

if check == 4:
     deletfile()          
