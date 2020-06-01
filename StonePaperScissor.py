from random import randint
rlist=['1', '2', '3']
uvalue='5'
print ("Press 4 to quit game")
while 1==1:
    uvalue=input("Stone(Press 1), Paper(Paper 2), Scissor(Press 3) :)  ??")
    cvalue=rlist[randint(0,2)]
    if cvalue == '1':
        dcvalue = 'Stone'
    if cvalue == '2':
        dcvalue = 'Paper'
    if cvalue == '3':
        dcvalue = 'Scissor'
    if uvalue == '1':
        duvalue = 'Stone'
    if uvalue == '2':
        duvalue = 'Paper'
    if uvalue == '3':
        duvalue = 'Scissor'
    
    if uvalue==cvalue:
        print ("Your value: ",duvalue, "  Computer value:", dcvalue)
        print("Draw....Lets try again")
    elif uvalue == '1' and cvalue == '2':
        print ("Your value: ",duvalue, "  Computer value:", dcvalue)
        print("Computer Won :D")
    elif uvalue == '1' and cvalue == '3':
        print ("Your value: ",duvalue, "  Computer value:", dcvalue)
        print("You Won :(")
    elif uvalue == '2' and cvalue == '3':
        print ("Your value: ",duvalue, "  Computer value:", dcvalue)
        print("Computer Won :D")
    elif uvalue == '2' and cvalue == '1':
        print ("Your value: ",duvalue, "  Computer value:", dcvalue)
        print("You Won :(")
    elif uvalue == '3' and cvalue == '1':
        print ("Your value: ",duvalue, "  Computer value:", dcvalue)
        print("Computer Won :D")
    elif uvalue == '3' and cvalue == '2':
        print ("Your value: ",duvalue, "  Computer value:", dcvalue)
        print("You Won :(")
    elif uvalue == '4':
        break
    else:
        print("invalid entry!!!!!")


print ("Had great time playing :) see you soon :)")
