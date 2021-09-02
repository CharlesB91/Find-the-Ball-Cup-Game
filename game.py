from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess():
    quess = ""
    while quess not in ["0", "1" , "2"]:
        quess = input("pick a number: 0,1 o4 2")
    
    return int(quess)
    
       
def check_quess(mylist, quess):
    if mylist[quess] == "0":
        print("Correct")
    else:
        print("Incorrect")
        print(mylist)
        

mylist = [" ", "0", " "]

mixedup_list = shuffle_list(mylist)

quess = player_guess()

check_quess(mixedup_list, quess)
