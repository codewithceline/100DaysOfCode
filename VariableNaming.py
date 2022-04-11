# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇


# NB: variables are read sequentially. The first input 3 and 5 will be stored in a and b respectively, then 
# I created another variable to store the value to avoid repetition

#a = b
#b = a 
#In the above, a when printed will return a stored value of b that was inputed above (5). 
#In the above, b when printed willw will return ther new value of a in line 13 (5)
# So we have to find an intermediate storage for the original a value inputed in line 2 to be returned (3). See below

aa = a
a = b
b = aa

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)


