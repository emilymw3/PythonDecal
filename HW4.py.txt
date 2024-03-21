import numpy as np

#2.1 Part 1
nums = []
max = 51
# had to change max to 51 since while statement asks when i is less than 50, not equal to
i = 0
while i < max:
    number = i
    nums.append(number)
    i +=1
print(nums)


#2.2 Part 2
lis = [2, 3, 4]
print(lis)
print(len(lis))
def square(randlist):
    length = len(randlist)
    i = 0
    #At first, I did not have the i=0 and the code was reporting error. 
    #So, I set i to 0 to give it an initial value and starting point so it would take the indexes
    #from randlist (or lis) from 0-3.
    while i < length:
        new_value = randlist[i]**2
        randlist[i] = new_value
        i +=1 
    print(randlist)
square(lis)


#2.3 Part 3
listA = []
startA = 0
while startA < 11:
    numberA = startA
    listA.append(numberA)
    startA +=1
print(listA)

listB = []
startB = 20
while startB < 31:
    numberB = startB
    listB.append(numberB)
    startB +=1
print(listB)

listC = listA + listB
print(listC)

listC = []

def remove_evennums(list1, list2, list3):
    list3 = list1 + list2
    # originally was writing for list3[i] in list3:, but realized that i iterates through each value of list3 so such is not necessary
    for i in list3:
        if i % 2 == 0:
        #was originally thinking of moving all values to a new list and setting the parameter as if i % 2 !=0
        # decided against this since it seemed much more complicated to continuously add to a new list
        # creating a list with all of the values combined, then removing the even values seemed simpler and more concise
            list3.remove(i)
    return(list3)

print(remove_evennums(listA, listB, listC))