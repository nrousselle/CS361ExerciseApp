import random

def menu():
    print("\nHere are your options:\n")
    print("Option 1: generate a random workout")
    print("Option 2: see list of muscle groups")
    print("Option 3: view exercise difficulty")
    print("Option 4: exit")


armWorkouts = ["Preacher curls", "Tricep extensions", "Wrist curls", "Pinwheel curls", "Tricep pushdown"]
legWorkouts = ["Calf raises", "Lying leg curls", "Horizontal leg press", "Leg Extension", "Rear kick", "Split squats"]
chestWorkouts = ["Crunches", "Bench press", "Side bend", "Chest fly"]

def randomExercise():
    print("Here is a random workout:\n")
    print(random.choice(armWorkouts))

    print(random.choice(chestWorkouts))
    
    print(random.choice(legWorkouts))

    print("Note: these workouts are not saved anywhere.")
    
muscleList = ["Biceps", "Triceps", "Forearms", "Calves", "Hamstrings", "Quadriceps", "Glutes", "Traps", "Lats", "Delts"]

def muscleGroups():
    print("Here are the main muscle groups:")
    print("Arms\nLegs\nShoulders\nBack")
    input


    while(True):
        x = input("Choose a muscle group or type exit to leave: ")
        if x == "exit":
            break
        elif x == "arms":
            print(muscleList[:3])
        elif x == "legs":
            print(muscleList[3:7])
        elif x == "back":
            print(muscleList[7:9])
        elif x == "shoulders":
            print(muscleList[9:])
        else:
            print("Please type a muscle group or exit")


def difficulty():
    while True:
        print("Choose an exercise to view its difficulty or type exit to leave:")
        x = input()
        if x in armWorkouts:
            print("Difficulty: easy")
        elif x in legWorkouts:
            print("Difficulty: medium")
        elif x in chestWorkouts:
            print("Difficulty: hard")
        elif x == "exit":
            break
        elif x == "done":
            break
        else:
            print("please type a valid exercise or exit/done leave")

print("Hello user!")
print("Welcome to LiftAssist\n")
print("Use this to explore exercise and workout information\n")

x = True

while x:
    menu()
    userChoice = input("\nEnter your choice: ")
    if(userChoice == "1"):
        randomExercise()
    elif(userChoice == "2"):
        muscleGroups()
    elif(userChoice == "3"):
        difficulty()
    elif(userChoice == "4"):
        x = False
    else:
        print("Please print a valid input.")

