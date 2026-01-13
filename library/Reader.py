#This will help to find path of the books
from pathlib import Path
#we are giving the program its own location to executr 
# "Path" is the class we got from pathlib i think 
# "__file__" gives the path of the Python file that is being executed
# .parent takes us 1 location behind like cd:hehe\download becomes cd:\hehe 
Project_location = Path(__file__).parent
#here we are giving the location of the folder where we give books
#Project_location gives location of whole folder
#and we are specifying folder books in it
Books_location = Project_location/"Books"

#def stands for define function
#function name is_pdf_safe
#we are checking if the pdf is safe of not
#we are taking path storing in file_name 
#and checking true or false
def is_pdf_safe(file_path: Path) -> bool:
    #now will be giving conditions to check safe or not
    #is the file is not file return false
    #.is_file checks if it is a file or not
    if not file_path.is_file():
        return False
    #if suffif is not lower return false
    if file_path.suffix.lower != ".pdf":
        return False
    #.hello.pdf see this is what we talk about
    if file_path.name.startswith("."):
        return False
    if file_path.stat().st_size == 0:
        return False
    return True

def list_books():
    if not Books_location.exists():
        print("Book not found")
        return []
    
    #we made a directory here when the book is safe it is saved here
    safe_books =[]
#all filees in books folder are iterated looped
    for file in Books_location.iterdir():
#fromthe previos function after checking that the file is safe 
        if is_pdf_safe(file):
            #add to the dictionary
            safe_books.append(file)
        else:
            print("file looks suspicious")
    return safe_books
