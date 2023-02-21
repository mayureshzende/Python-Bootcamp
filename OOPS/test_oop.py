class Main():
    def __init__(self):
        print("Main class is created")
    
    def  say(self):
        print('i am saying from main class')
    

class Child(Main):

    def __init__(self):
        Main.__init__(self)
        print("child class is created")
    
    def ch_meth(self):
        print("child class method")

# my_child = Child()
# my_child.ch_meth()

class Fruit():

    def __init__(self, name):
        self.name = name

    def colour(self):
        return NotImplementedError("please implement it after inherting")


class Apple(Fruit):

    def __init__(self , name ):
        Fruit.__init__(self, name )
    
    def colour(self):
        print( "I am {1} and red in color {0}".format(self.name , "test"))

my_apple = Apple("Iapple")
my_apple.colour()

class Mango(Fruit):

    def __init__(self, name):
        Fruit.__init__(self, name )
    
    def colour(self):
        print("i am {} and king of friuts".format(self.name))


my_mango = Mango("mannnngggooo")
my_mango.colour()


for func in [my_mango, my_apple]:
    func.colour()


class Book():

    def __init__(self, name, pages):
        self.name = name 
        self.pages = pages
    
    def __str__(self):
        # print(" this is {} book".format(self.name))
        return "this is {} book".format(self.name)
    
    def __len__(self):
        # print("lenght is {} pages".format(self.pages))
        return self.pages


my_book = Book('Mayureshsa' , 777 )
s = str(my_book)
l = len(my_book)
print(s)
print(l)
