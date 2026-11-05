name   = input("Enter your name: ")
weight = int(input("Enter your weight in pounds: "))
height = int(input("Enter your height in inches: "))


BMI = (weight * 703) / (height * height)
print("---------" + name + "---------" )
print("Your BMI is: " + str(BMI))

if BMI>0:
     if(BMI<18.5):
        print("You are underweight.")
     elif(BMI<= 24.9):
        print("You are normal weight.")
     elif(BMI<=29.9):
         print("You are overweight");
     elif(BMI<=34.9):
         print("You are obese.");
     elif(BMI<39.9):
         print("You are severely obese.");
     else:
         print("You are mobidly obese.")
else:
         print(" Enter Valid input")          