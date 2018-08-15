
u_door = None
print("You are stuck in an infinite loop! You need to find your way out! Wait! \
I smell a break around here! Go find it before you go insane in this horrible\
 place!You can start by choosing one of these three doors i guess?")

def choose_door(current_room):
    global u_door
    u_door = int(input("What number of door would you like to open?"))
    (current_room)(u_door)

def room_0(u_door):
    if u_door == 1:
        print('You made it!')
        riddle1()
        choose_door(room_1)

    elif u_door == 2:
        print('oh no its a trap')

    elif u_door == 3:
        print('oh no its a trap')


def room_1(u_door):
    if u_door == 1:
        print('oh no its a trap')

    elif u_door == 2:
        print('You made it!')
        choose_door(room_2)

    elif u_door == 3: 
        print('oh no its a trap')


def room_2(u_door):

    if u_door == 1:
        print('oh no its a trap')

    elif u_door == 2:
        print('You made it!')
        

    elif u_door == 3:
        print('oh no its a trap')           


def riddle1():
    print("How many trees are cut down per year for toilet paper?")
    print(" 1 = 2000, 2 = 12000, 3 = 27000, 4 = 120000")
    user_answer = int(input("What number would you like to choose?"))
    if user_answer == 3:
        print('HINT: in room 2 the second door is the best')
    else:
        print('wrong! better luck next time')

def riddle2():
    print("how many sea creaturs die due to plastic polution each year?")
    print("1 =100,000, 2 =500,000 , 3=750,000 , 4 =1,000,000")
    user_answer= int(input("what number would you like to choose?"))
    if user_answer == 4:
       print("HINT:in room number 4 the third door is the best")
    else:
        print('wrong! better luck next time')

def riddle3():
    print("how old are the world's oldest trees?")
    print("1 =3,000, 2 =4,600 , 3=7,200 , 4 =12,050")
    user_answer= int(input("what number would you like to choose?"))
    if user_answer == 2:
       print("HINT:In room number 3 the first door is the best")
    else:
        print('wrong! better luck next time')

def riddle2():
    print("how many plastic water buttles used in year??")
    print("1 =50 billion,  2 =20 billion , 3=billion , 4 =1,000,000")
    user_answer= int(input("what number would you like to choose?"))
    if user_answer == 1:
       print("HINT:In room number 1 the second door is the best")
    else:
        print('wrong! better luck next time')
                     
                     
                     
                                          
                     
                     
choose_door(room_0)


     
        
    
    
