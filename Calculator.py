print("********************************* CALCULATOR *********************************")

# add two numbers
def add(num1, num2):
	return num1 + num2

# subtract two numbers
def subtract(num1, num2):
	return num1 - num2

# multiply two numbers
def multiply(num1, num2):
	return num1 * num2

# divide two numbers
def divide(num1, num2):
	return num1 / num2

print("Please select operation -\n" \
		"1. Add\n" \
		"2. Subtract\n" \
		"3. Multiply\n" \
		"4. Divide\n")


# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 :"))

num1 = int(input("Enter first number: "))
num2= int(input("Enter second number: "))

if select == 1:
	print(num1, "+", num2, "=",
					add(num1, num2),)

elif select == 2:
	print(num1, "-", num2, "=",
					subtract(num1, num2))

elif select == 3:
	print(num1, "*", num2, "=",
					multiply(num1, num2))

elif select == 4:
	print(num1, "/", num2, "=",
					divide(num1, num2))
else:
	print("Invalid input")
