# Decal HW3

#Problem 1- Exponents- DONE!!
x = int(input("Input a base number: "))
y = int(input("Input a number as the exponent: "))
product = 1
while y > 0:
          product = product * x
          y -=1
print(product)



#Problem 2- DONE!!
list = []
maxlength = 5
while len(list) < maxlength:
      num = input("Enter a value. ")
      list.append(num)
      print(list)
end_tuple = {min(list), max(list)}
print(end_tuple)


#Problem 3-  Check leap year- DONE!!
year =  input()
if int(year) % 4 !=  0:
    print('false')
else:
        print('true')


#Problem 4- Caluclate BMI- DONE!!
weight = float(input("How much do you weigh (kg)? "))
height = float(input("How tall are you (m)? "))
BMI = weight/height ** 2
print(BMI)



# Problem 5- Rotating Digits
def rotate_digits():
     n = input("Give me a number: ")



# Problem 6- Min and Max but with Loops
numlist = [1, 54, -3, 19, 25]
#find max with for loop
def max_forloop(somelist):
     formax_num = somelist[0]
     for i in somelist:
          if i > formax_num:
               formax_num = i
               return formax_num
print(max_forloop(numlist))


#find min with for loop
def min_forloop(somelist):
     formin_num = somelist[0]
     for i in somelist:
          if i < formin_num:
               formin_num = i
               return formin_num
print(min_forloop(numlist))


#find max with while loop
numlist = [1, 54, -3, 19, 25]
def max_whileloop(somelist):
     i = 0
     whilemax_num = somelist[0]
     while i < len(somelist):
          if whilemax_num < somelist[i+1]:
               whilemax_num = somelist[i]
               return whilemax_num
print(max_whileloop(numlist))

# find min with while loop
def min_whileloop(somelist):
     i = 0
     whilemin_num = somelist[0]
     while i > len(somelist):
          if whilemin_num < somelist[i+1]:
               whilemin_num = somelist[i]
               return whilemin_num
print(min_whileloop(numlist))



# Problem 7- Vowels- DONE!!
word = str(input("Give me a word: "))
vowels = ["a", "e", "i", "o", "u"]
num_vowels = 0
for i in range(len(word)):
    if word[i] in vowels:
        num_vowels +=1
print(num_vowels)



# Problem 8- digital root- DONE!!
digit = input("Give me a number: ")
sum = 0
for num in str(digit):
    sum = sum + int(num)
print(sum)