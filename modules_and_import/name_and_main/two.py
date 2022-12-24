#two.py 

import one

one.one()

def two():
    print("I am the two.py file function")

print("I am the two.py file")

if __name__ == "__main__":
    print("Two.py is called directly")
else:
    print("two.py is being imported in the other file")

