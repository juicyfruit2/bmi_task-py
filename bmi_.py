# Create a program that calculates a person's BMI

# ASKING THE USER TO ENTER HIS/HER WEIGHT AND HEIGHT 
weight_kg = float(input("Enter your weight:"))
height_m = float(input("Enter your height"))
print(weight_kg)
print(height_m)

# CALCULATED THE USERS BMI AND ROUNED OFF 2 DECIMAL PALCES 
BMI = (weight_kg) / (height_m * height_m)
print(round(BMI,2))

# USED IF,ELSE,ELIF STATEMENTS
if BMI >= 30:
    print("You are Obese")
elif BMI >= 25:
    print("You are Over Weight")
elif BMI >= 18.5:
    print("You are noraml")
else:
    print("You are Underweight")