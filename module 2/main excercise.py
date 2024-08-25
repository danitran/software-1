#1
print("Hello, Tai!")
#2
user_string = input("Enter a number r: ")
r = float(user_string)
S = float(user_string)
print("S = r*r*3.14")
S = r * r * 3.14

print(S)

#3
user_string = input("Enter a number Length: ")
user_string1 = input("Enter a number Widlth: ")

L = float(user_string)
W = float(user_string1)
P = float
A = float

P = L + L + W + W
print("PERIMETER IS: ")
print(P)

A = L ** W
print("AREA IS: ")
print(A)

#4
Number_1 = int(input("Enter number 1: "))
Number_2 = int(input("Enter number 2: "))
Number_3 = int(input("Enter number 3: "))

print(Number_1 + Number_2 + Number_3)
print( Number_1 * Number_2 * Number_3)
print((Number_1 + Number_2 + Number_3) / 3)

#5
T = float(input("Enter Talent: "))
P = float(input("Enter Pounds: "))
L = float(input("Enter Lots: "))
G = float
K = float

L_to_G = 13.3
P_to_L = 32
T_to_P = 20

G_to_T = T * T_to_P * P_to_L * L_to_G
G_to_P = P * P_to_L * L_to_G
G_to_L = L * L_to_G
Total_Gram = G_to_L + G_to_P + G_to_T

K = int(Total_Gram // 1000)
G = Total_Gram % 1000

print(f"This is ur weight units : {K} Kilograms and {G:.1f} Grams" )

#6
import random

number_3_random = random.randint(0, 999)
number_4_random = random.randint(1000, 1666)

print(number_3_random)
print(number_4_random)



