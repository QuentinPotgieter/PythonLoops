#cd c://programs
#python 33361908_Practical_8.py

#Question 1
#Loop While less than user input
n = int(input("Enter the number of values to display: "))
#Print i < n
for i in range(0, n):
    i = i + 1
    print(i)
print('')

#Quention 2
#Use for loops to calculate the power of a variable
base = int(input("Enter base value: "))
exponent = int(input("Enter exponent value: "))
def powerInt(base,exponent):
    power = 1
    for i in range(1, exponent + 1):
        power = power * base
    print(str(base) + ' raised to the power of ' + str(exponent) + ' = ' + str(power))
powerInt(base,exponent)

#Quention 3
#Nested for loop
integer = int(input("Enter value for multiplication table: "))
def mathTable(integer):
    for row in range(1,integer+1):
        for col in range(1,13):
            print(row*col, end="\t")
            if (col == 12):
                print('\n')
mathTable(integer)
