
def calculateBMI(weight, height):
    bmi = weight / (height * height)
    return bmi

people = int(input("How many people? "))

bmiHistory = []

for i in range(people):
    print("\n--- Person", i + 1, "---")
    
    name = input("Enter name: ")
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))
    
    bmi = calculateBMI(weight, height)
    
    bmiHistory.append({
        "name": name,
        "bmi": round(bmi, 2)
    })
    
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Severely Overweight"
        
    print(f"BMI for {name}: {round(bmi, 2)} -> Category: {category}")

print("\n=== BMI History ===")
for record in bmiHistory:
    print(f"{record['name']}: {record['bmi']} BMI")