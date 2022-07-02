# (1)Write a Python program to print the following string in a specific format 

#  print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star,\n\tHow I wonder what you are!")

# (2)Write a Python program to get the Python version you are using.

# import sys
#print("user current version:-",sys.version)

# print(sys_version)

#3. Write a Python program to display the current date and time.

# import datetime
# n=datetime.datetime.now()
# print(n)

# 4  Write a Python program which accepts the radius of a circle from the user and compute the area.
# n=float(input("enter the value= "))
# a=3.14*(n*n)
# print(a)

# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

# a=("nandan")
# b=("kalia")
# print (b, " ", a)

# 6.. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

# v = input("enter numbers" )
# list = v.split(",")
# tuple = tuple(list)
# print('List :',list)

# 7 Write a Python program to accept a filename from the user and print the extension of that.
# x="my.nb"
# y=x.split(".")
# print(y[-1])

# 8. Write a Python program to display the first and last colors from the following list.

# color_list = ["Red","Green","White" ,"Black"]
# print (color_list[0],color_list[3])

# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date)
# a = (11, 12, 2014)
# print ("date: %i / %i / %i"%a)

# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

# a = int(input("Input an integer : "))
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# print (n1+n2+n3)

# 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# print(abs.__doc__)

# 12. Write a Python program to print the calendar of a given month and year.

# import calendar 
# y = int(input("input the year :"))
# m = int (input("intput the month :"))
# print(calendar.month(y,m))

#13. Write a Python program to print the following 'here document'

# print("""
# a string that you "don't" have to escape 
# this
# is a   ........ multi-line 
# heredoc string ----------> example
# """)

# 14. Write a Python program to calculate number of days between two dates.

# from datetime import date 
# a = date(2022,7,1)
# b= date(2022,7,19)
# c = a - b
# print(c.days)

# 15. Write a Python program to get the volume of a sphere with radius 6.
# from math import pi
# rad = 6
# vol = 4/3*pi* rad*3
# print(vol)

