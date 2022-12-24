#one.py 

# we are using the __name__ == "__main__"
# this is to check weather the file is called directly or is being imported in the other file 

def one():
    print("this is the one function ")

print("I am the one.py file")

if __name__ == "__main__":
    print("one file is being run directly")
else:
    print("one file is being imported and then used the funtions")