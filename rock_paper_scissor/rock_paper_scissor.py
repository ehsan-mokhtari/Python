import random
while True:
    print("What is your choice?\n1.Rock  2.Paper  3.Scissor  4.exit")
    choice = int(input())
    while choice!=1 and choice!=2 and choice!=3 and choice!=4:
        print("Enter valid value")
        choice = int(input())
    #rock 1  paper 2 scissor 3
    rpc = random.randint(1,4)
    if choice == 4:
        break
    elif choice==1 and rpc==1:
        print("you=rock  computer=rock  its draw!")
    elif choice==1 and rpc==2:
        print("you=rock  computer=paper  you lost!")
    elif choice==1 and rpc==3:
        print("you=rock  computer=scissor  you win!")
    elif choice==2 and rpc==1:
        print("you=paper  computer=rock  you win!")
    elif choice==2 and rpc==2:
        print("you=paper  computer=paper  its draw!")
    elif choice==2 and rpc==3:
        print("you=paper  computer=scissor  you lost!")
    elif choice==3 and rpc==1:
        print("you=scissor  computer=rock  you lost!")
    elif choice==3 and rpc==2:
        print("you=scissor  computer=paper  you win!")
    elif choice==3 and rpc==3:
        print("you=scissor  computer=scissor  its draw!")     
    print("#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")    