import random

print("\n")
print("############################################################")
print("#    Code For       : Love Parcentage Tester               #")
print("#    Code Language  : Python                               #")
print("#    Code Author    : Md. Tareq Ahamed Jony                #")
print("#    Member OF      : Knight Squad                         #")
print("#    Position       : Learner (Knight_VIII)                #")
print("#    Team           : Knight Squad                         #")
print("#    Team Leader    : Noman Prodhan                        #")
print("############################################################")
print("\n")

def love_tester(name1,name2):

    rand_num = random.randint(50,98)
    print(f"Your Love Parcentages Are {rand_num}%\n")


while True:
    name1 = input("Enter Name (Male) : ")
    name2 = input("Enter Name (Female) : ")
    love_tester(name1,name2)