#first take the input from user using input() function
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#height and weight variables have string data type.It should be converted float or int type to perform mathematical operations on it
w = float(weight)
h = float(height)

#write the formula for BMI calculation
BMI = (w/(h ** 2))

#then print the value of BMI 
print(BMI)
