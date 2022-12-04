
from random import shuffle

my_list = [' ' , '0' , '']

def suffle_list():
    shuffle(my_list)
    return my_list
# shuffle(my_list)
suffle_list()
def take_input():
    inp = input("please guess between 0,1 or 2 =")
    return  int(inp) 

def guess_ball(guess_list):
    inp = take_input()
    while not (inp <= 2 and inp >=0):
        inp = take_input()
    if guess_list[int(inp)] == '0':
        print(" you made it ")
    else:
        print(" wrong guess!")

guess_ball(my_list)





