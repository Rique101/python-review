#Python supports the for and while loops.
#Loops are used to repeat a block of code.

#The for loop is used for sequential traversal.
#It may be used for iterating through Strings, Tuples,
#Lists, or Dictionaries.

#String
iterable = '987654321'
for i in iterable:
    print(i, end= " ")
print("blastoff!")

#Tuple
iterable = (9,8,7,6,5,4,3,2,1)
for i in iterable:
    print(i, end= " ")
print("blastoff!")

#List
iterable = [9,8,7,6,5,4,3,2,1]
for i in iterable:
    print(i, end=" ")
print("blastoff!")

#Dictionary
iterable = dict({'nine': 9,
                'eight': 8,
                'seven' : 7,
                'six' : 6,
                'five' : 5,
                '4' : 4,
                '3' : 3,
                'two' : 2,
                'one' : 1})

for i in iterable:
    print("%d" % (iterable[i]), end=" ")
    print("blastoff!")

#The while loop must be provided must be provided a condition.
#As long as the condition is true, its code
#block will be executed.
i = 9
while (i > 0):
    print(i, sep=" ")
    #There must be a line of code in the code block
    #that forces the condition to become false, else
    #the loop will repeat infinitely.
    i = i - 1
    print("blastoff!")

i = 8
while (i > 0):
    print(i, sep=" ")
    #There must be a line of code in the code block
    #that forces the condition to become false, else
    #the loop will repeat infinitely.
    i = i - 2
    print("blastoff!")

i = 9
while (i > 0):
    if (i % 2 == 0):
        print(i, sep=" ")
    #There must be a line of code in the code block
    #that forces the condition to become false, else
    #the loop will repeat infinitely.
    i = i - 1
    print("blastoff!")

#4. Write a while loop that prints out the odd numbers 
#between 1 and 10
number = 1
while number <= 10:
    if number % 2 != 0:
        print(number)
    number += 1
