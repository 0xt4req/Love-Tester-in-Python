import random, pyttsx3, playsound


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


def greetings_speak():
    robot = pyttsx3.init()
    robot.say("Welcome to Love Tester. I am programmed by Md. Tareq Ahamed Jony. Just input two names & I will test "
              "the love between you. So, are you ready?")
    robot.runAndWait()


def in_91_to_100():
    robot = pyttsx3.init()
    robot.say("You guys are made for each other! If you guys haven't married, than get married.")
    robot.runAndWait()


def in_81_to_90():
    robot = pyttsx3.init()
    robot.say("You are made for each other. You are love birds!")
    robot.runAndWait()


def in_71_to_80():
    robot = pyttsx3.init()
    robot.say("You are a success Lover! Your Love is in the air!")
    robot.runAndWait()


def in_61_to_70():
    robot = pyttsx3.init()
    robot.say("Your love is Growing! Don't Leave each Other.")
    robot.runAndWait()


def failure():
    robot = pyttsx3.init()
    robot.say("Your love is poor! Try hard to be a success lover!")
    robot.runAndWait()


def love_tester():
    rand_num = random.randint(50, 99)
    print(f"Your love is {rand_num}%")
    if rand_num >= 60 and rand_num <= 70:
        print("Your love is Growing!")
        in_61_to_70()
    elif rand_num >= 71 and rand_num <= 80:
        print("Your love is in the Air!")
        in_71_to_80()
    elif rand_num >= 81 and rand_num <= 90:
        print("You are Love Birds!")
        in_81_to_90()
    elif rand_num >= 91 and rand_num < 100:
        print("You guys are made for each other!")
        in_91_to_100()
    else:
        print("Try Hard to be a success Lover!")
        failure()


print("Loading......")
greetings_speak()

while True:
    name1 = input("Enter First Name  : ")
    name2 = input("Enter second Name : ")
    love_tester()
