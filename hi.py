import random
comp = random.randint(0,2)
def user():
    print("Welcome to snake, water and gun game!")
    user = int(input("Enter 0 for snake, 1 for water, 2 for gun:"))
    while (user>=3 or user<1):
        user = int(input("Enter 0 for snake, 1 for water, 2 for gun:"))
    if comp == user:
        print("Its a draw")
        print(f'User,Comp=={user}')
    elif comp ==0 and user ==1:
        print("You lost")
        print(f'User = {user} and Computer ={comp}')
    elif comp == 0 and user == 2:  
        print("You won")
        print(f'User = {user} and Computer ={comp}')
    elif comp ==1 and user == 0:
        print("You won")
        print(f'User = {user} and Computer ={comp}')
    elif comp == 1 and user ==2:
        print("You lost")
        print(f'User = {user} and Computer ={comp}')
    elif comp == 2 and user == 0:
        print("You lost")
        print(f'User = {user} and Computer ={comp}')
    else:
        print("You won")
        print(f'User = {user} and Computer ={comp}')


user()
        
