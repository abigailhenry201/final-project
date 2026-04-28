
import matplotlib.pyplot as plt
import numpy as np
from datetime import date


date = date.today()
today = date.strftime("%A,%m/%d/%Y")
print(today)


activity_level = {"sedentary" : 1.2 , "light activity" : 1.375 , "moderate activity" : 1.55 , "very active" : 1.725 , "extra active": 1.9}

def femaleBMR():
    return ((10 * (data["weight"]/2.205)) + (6.25 * (data["height"]*2.54)) - (5.0 * data["age"])) - 161


def maleBMR():
    return ((10 * (data["weight"]/2.205)) + (6.25 * (data["height"]*2.54)) - (5.0 * data["age"])) + 5


def BMR():
    if data["gender"] == "female":
        return femaleBMR()
    elif data["gender"] == "male":
        return maleBMR()


def TDEE():
    tdee = round(BMR() * activity_level[data["activity"]])
    print("Your estimated caloric intake based on your height and weight is:", tdee)

    if data["goal_weight"] < data["weight"]:
        intake = tdee - 500
        goal = "Deficit"
        print("To be in deficit and reach your goal weight of" , data["goal_weight"], "pounds, stick to", intake , "a day!")
        
    elif data["goal_weight"] > data["weight"]:
        intake = tdee + 500
        goal = "Bulk"
        print("To bulk and reach your goal weight of" , data["goal_weight"], "pounds, stick to", intake, "a day!")
    else:
        intake = tdee
        goal = "Maintenance"
        print("To maintain your current weight of", data["weight"], "pounds, stick to", tdee, "a day!")
        
    return tdee, goal, intake

    
def newFile():
    name = input("Please enter your name:")
    filename = name + ".txt"

    with open(filename, "w") as file:
        file.write("Calorie Tracker for:" + name + "\n\n\n")

        print(filename, "has been created!")


def save_tdee_data(tdee,goal,intake):
    name = input("Please enter your file name:").lower()
    filename = name + ".txt"
    with open(filename, "w") as file:
        file.write(" ~ Personal Information ~ " + "\n")
        file.write("Name: " + name +"\n")
        file.write("Gender: " + (data["gender"])+ "\n")
        file.write("Age: " + str(data["age"]) + "\n")
        file.write("TDEE: " + str(tdee) + "\n")
        file.write("Caloric Intake: " + str(intake) + " - " + goal +"\n")
        file.write("Starting weight: " + str(data["weight"]) +"\n")
        file.write("Goal weight: " + str(data["goal_weight"]) +"\n\n")


def change_weight():
    name = input("Please enter your file name:").lower()
    current = float(input("Please enter your new weight:"))
    filename = name + ".txt"
    with open(filename,"a") as file:
        file.write("Current weight as of "  +  str(today) +  " is: " + str(current) + "\n")
    print("New weight updated!")

    return current 


def weight_plot():
    name = input("Please enter your file name:").lower()
    filename = name + ".txt"
    
    dates = []
    weights = []

    with open(filename, "r") as file:
        for line in file:
           if "Current weight as of" in line:
                parts = line.strip().split("is:")
                
                weight = float(parts[1].strip())
                
                date = parts[0].replace("Current weight as of", "").strip()


                dates.append(date)
                weights.append(weight)

    plt.figure(figsize=(10,6))
    pounds = plt.plot(dates, weights, marker = "o")
    plt.xlabel("Date")
    plt.ylabel("Weight")
    plt.title("Weekly Weight-In")
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation = 35)
    plt.show()


def log_food():
    cal_total_all = 0
    carb_total_all = 0
    pro_total_all = 0
    fat_total_all = 0


    food_logged = [] 
    name = input("Please enter your file name:").lower()
    filename = name + ".txt"
    
    file = open("food.csv", "r")
    next(file)
    lines = file.readlines()

    
    while True:
            
        food_choice = input("Enter food to add to your log:").lower()
        for line in lines:
            line = line.strip()
            col = line.split(",")
            food = col[0]     

            if food_choice == food:
            
                amount = float(input("Enter the food amount in grams:"))
                cal = float(col[1])
                carb = float(col[2])
                pro = float(col[3])
                fat = float(col[4])

                total_cal = round((cal*amount)/100)
                total_carb = round((carb*amount)/100)
                total_pro = round((pro*amount)/100)
                total_fat = round((fat*amount)/100)
            
                print("Calories:" , total_cal)
                print("Carbs:" , total_carb)
                print("Protein:" , total_pro)
                print("Fats:" , total_fat)

                log = input("Would you like to add this to your file?").lower()
                if log == "yes": 
                    cal_total_all = cal_total_all + total_cal
                    carb_total_all = carb_total_all + total_carb
                    pro_total_all = pro_total_all + total_pro
                    fat_total_all = fat_total_all + total_fat

                    food_logged.append((food_choice, total_cal, total_carb, total_pro, total_fat))

                    print("Food added!")
                break

        else:
            print("Food not Found.")

        ask = input("Would you like to enter another item? (Yes or No)").lower()
        if ask != "yes":
            break 
         
    

    for food in food_logged:
        print("Food:", food[0], "| Calories:", food[1] , "| Carbs:", food[2], "| Protein:", food[3], "| Fats:" , food[4])
    print("      Food Overview     ")
    print("Totals for" , today, ":")
    print("Calories: ", cal_total_all)
    print("Carbs: ", carb_total_all)
    print("Protein: ", pro_total_all)
    print("Fats: ", fat_total_all)

    with open(name + ".txt" , "a") as file:
        file.write("\n======================\n")
        file.write("Food list for:" + str(today) + "\n\n")
    
        for food in food_logged:
            file.write(food[0] + " | Calories:" + str(food[1]) + " | Carbs:" + str(food[2]) + " | Protein:" + str(food[3]) + " | Fats:" + str(food[4]) + "\n")
                
        file.write("~ Daily Totals ~ " + "\n")
        file.write("Calories Total:" + str(cal_total_all) + "\n")
        file.write("Carbs Total:" + str(carb_total_all) + "\n")
        file.write("Protein Total:" + str(pro_total_all) + "\n")
        file.write("Fats Total:" + str(fat_total_all) + "\n\n")

def compare_macros_plot():
    days = []
    calorie = []
    carbs = []
    protein = []
    fat = []

    name = input("Please enter your file name:").lower()
    filename = name + ".txt"

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            

            if "Carbs Total:" in line:
                carbs.append(float(line.split(":")[1].strip()))
            elif "Protein Total:" in line:
                protein.append(float(line.split(":")[1].strip()))
            elif "Fats Total:" in line:
                fat.append(float(line.split(":")[1].strip()))
            elif "Calories Total:" in line:
                calorie.append(float(line.split(":")[1].strip()))
            elif "Food list for:" in line:
                days.append(line.split(":")[1].strip())

    n=min(len(days), len(calorie), len(carbs),len(protein), len(fat))

    days = days[:n]
    calorie = calorie[:n]
    carbs = carbs[:n]
    protein = protein[:n]
    fat = fat[:n]
             
    x = np.arange(n)
    width = 0.15 

    plt.figure(figsize =(10,6))
    bar_calories = plt.bar(x-width,calorie,width,label="Calories", color = "purple")
    bar_carbs = plt.bar(x,carbs,width,label="Carbs", color = "red")
    bar_protein = plt.bar(x+width,protein,width,label="Protein", color = "blue")
    bar_fats = plt.bar(((x+width)+width),fat,width,label="Fats", color = "yellow")
    plt.bar_label(bar_calories)
    plt.bar_label(bar_carbs)
    plt.bar_label(bar_protein)
    plt.bar_label(bar_fats)
    plt.xlabel("Dates")
    plt.ylabel("Amount (in grams for Marcos)")
    plt.title("Weekly Macro Overview")
    plt.xticks(x, days)
    plt.legend()
    plt.grid(True, alpha=0.3, axis="y")
    plt.show()

def return_to_main():
    screen = input("Would you like to return to the main screen?").lower()
    if screen == "yes":
        main()
    else:
        print("See you soon!")

                   
def main():
    print("TDEE and Calorie Tracker")
    print("1: Create a new file") 
    print("2: Calculate TDEE")
    print("3: Log food")
    print("4: Log Weight")
    print("5: View Weekly Weight Chart")
    print("6: View Weekly Calorie Overview")
    print("7: Exit")
    choice = input("Enter your choice")
    if choice == "1":
        newFile()
        return_to_main()
    elif choice == "2":
        get_user_data()
        tdee, goal, intake = TDEE()
        save_tdee_data(tdee, goal, intake)
        print("Information saved to file!")
        return_to_main()
    elif choice == "3":
        log_food()
        return_to_main()
    elif choice == "4":
        change_weight()
        return_to_main()
    elif choice == "5":
        weight_plot()
        return_to_main()
    elif choice =="6":
        compare_macros_plot()
        return_to_main()    
    else:
        return_to_main()

        
   
    
def get_user_data():
    gender = input("Are you male or female?").lower()

    while gender != "male" and gender != "female":
        gender = input("Please enter 'male' or 'female'")

    age = int(input("Enter your age in years!"))

    weight = float(input("Enter your weight in pound!"))

    height = float(input("Enter your height in inches!"))

    goal_weight = int(input("Enter your goal weight in pounds!"))
    print("Activity Levels:")
    for level in activity_level:
        print(level)

    activity = input("Please enter activity level!").lower()
    while activity not in activity_level:
        activity = input("Please enter activity level!").lower()
        
    global data
    data = {"gender": gender, "age": age, "weight": weight, "height": height, "goal_weight": goal_weight, "activity": activity}
main()


    



