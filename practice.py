# def prac(**a):
#     print("Hello",a)
# prac(a=1,b=2,c=3)
# def outer():
#     print("outer function")
#     def inner():
#         print("inner function")
#     inner()


# outer()
# import functions
# print(functions.sum(3,5))
# s=open("example.txt",mode="r")
# print(s.read())
# s.close()
# file=open("example.txt",mode="r+")
# print(file.read())
# file.write("my name is madhu")
# file.close()
# file=open("example.txt",mode="a")
# file.write("Somethonding   ")# the previous data what exits in the file will be reased to 
# #to overcome this problem we use append instead of write mode if u want the previoe data
# file.close()
# file=open("example.txt",mode="r+")
# print(file.read())
# file.write("My name is madhu")
# file.close()
# file=open("example.txt",mode="w+")
# file.write("my_name_is_madhu")
# file.seek(2)
# print(file.read())
# file.close()
# a=7
# try:
#     print(a)
# except:
#     print("The b not defined")
# else:
#     print("No exception This is else block")
# finally:
#     print("This is finally block")
# a=45
# try:
#     print(b)
# except NameError :
#     print("The b not defined")
# except TypeError:
#     print(" This is Type error")
# else:
#     print("This is else block")
# finally:
#     print("This is finally block")


# class Madhu:
#     a=5
#     def fun(self):
#         print(self.a)

# obj=Madhu()
# print(obj.a)

# class Student:
#     def id(self):
#         name="madhu"
#         print("madhu")
# obj=Student()
# obj.id()


# class Madhu:
#     a=6
#     def fun(self):
#         pass
#         #print(self.a)
    
# obj=Madhu()
# print(obj.a)

#inheritance
# 1)single inheritance
# 2)multiple
# #)multilevel
# 5)hierachical 
# hybrid
#1) single inheritance

# class parent():
#     def parent_method(self):
#         print("This is parent method")
# class child(parent):
#     def childs_method(self):
#         print("Thois is child method")
        
# obj=child()
# obj.childs_method()
# obj.parent_method()

#2)multilevel
# class Grand_parent():
#     def grand_parent_method(self):
#         print("This is grand parent method")
# class Parent(Grand_parent):
#     def parent_method(self):
#         print("This is parent method")
# class Child(Parent):
#     def child_method(self):
#         print("This is child method")
# obj = Child()
# obj.child_method()
# obj.parent_method()
# obj.grand_parent_method()


# class demo():
#     def __init__ (self,a,b):
#         self.__a=a
#         self._b=b
    
# class demo2(demo):
#     def output(self):
#         print(self._b)
    

# obj=demo2(4,6)
# obj.output()




# class demo():
#     def __init__(self,a,b):
#         self.__a=a
#         self._b=b
# class demo1(demo):
#     def 






# name="MadhU"
# up_count=0
# low_count=0
# for i in range(len(name)):
#     if ord(name[i])>=65 and ord(name[i])<=90:
#         up_count=+1
#     else:
#         low_count+=1
        
# print("Lower case count",low_count)
# print("upper case count",up_count
# str1="polo"
# str2="loop"

# if len(str1)==len(str2):
#     for i in range(len(str1)):
#         print(str[i])








# class Name():

#     def ma(self):
#         _a=8 #protected variable
#         __b=9 #private variable
#         print(_a)
#         print(__b)
    
# obj=Name()
# print(obj.ma())



# class Name():
#     def __init__ (self,a,b):
#         self._a=a
#         self.__b=b
        
# class Name1(Name):
#     def fun(self):
#         print(self._a)
        

# obj=Name1(5,7)
# obj.fun()

# dic={
#     "name":"madhu",
#     "age":23,
#     "place":"banglore"
# }
# a=dic.values()
# print(a)


# name="kjgjhghj"
# Madhukiran adhukirandhukiran"
# Madhukiran dhukiran
# Madhukiran dhukirannmadhukiran name:
# Madhukiran dhukirannmadhukirant+=1
# Madhukiran adhukirant(i)
# Madhukiran adhukiranhe count is",count)







#str1="Python is a programming language that is used to build software"
# True_count=0
# False_count=0
# for i in str1:
#     if i==" " or (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
#         True_count+=1
#     else:
#         False_count+=1
# if False_count==0:
#     print("valid String")
# else:
#     print("invalid String")
    


# lis=[10,20,30,40,50]
# if lis[0]==lis[-1]:
#     print("True")
# else:
#     print("False")


# str1="Python is a programming language that is used to build software"

# res=str1.split(" ")
# for i in range(len(res)):
#     for j in range(i+1,len(res),1):
#         if res[i]==res[j]:
#             print(res[i])

# print([8 for _ in range(5)])

# print([5 for _ in range(8)])

# lis=[1,2,3,4,5]
# lis1=[6,7,8,9,10]
# lis[:-1]=lis1
# print(lis)

# def fib(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# print(fib(5))




# def big(a,b):
#     if a>b:
#         return a
#     else:
#         return b

# res1=big(a,b)
# res2=big(res1,c)
# print(res2)



# if a>b:
#     if a>c:
#         print("A is big")
#     else:
#         print("c is big")
# else:
#     if b>c:
        
#         print("B is big")
#     else:
#         print("C is big")


# a,b,c=2,5,104

# if a>b and a>c:
#     print(" A is big")
# else:
#     if b>a and a>c:
#         print("B is big")
#     else:
#         if c>a and c>b:
#             print("C is big")

# str="Python"
# vowels="aeiouAEIOU"
# stat=True
# count=0
# for i in str:
#     if count==4:
#         stat=False
#         break
#     if i not in  vowels:
#         count+=1
#     else:
#         count=0
# if stat:
#     print("Yes")
# else:
#     print("No")





# Types of Errors
# 1. Compile time Error (Syntax Error)
# 2. Runtime Error      
# 3. Logical Error






#Compile time Error (Syntax Error)

# print("Hello World" # Missing parentheses in function call



# #Run time Error
# # This error occurs when you try to divide a number by zero.
# x = 10
# y = 0
# result = x / y  # Division by zero
# print(result)





# #Logical Error
# # This error occurs when the logic of the code is incorrect, leading to unexpected results.
# # For example, if you meant to add two numbers but accidentally used subtraction:
# # num1 = 5
# # num2 = 10
# sum_result = num1 - num2
# print(f"The sum of {num1} and {num2} is: {sum_result}")



# string="Python"
# print(string[ : : ]) #output=> Python

# print(string[0:1]) #output=> P

# print(string[0:2]) #output=> Py

# print(string[0:4:2]) #output=> Pt

# print(string[-1:])  #output=> n

# print(string[0 : : 2]) #output=> Pto
# original = [[1, 2], [3, 4]]

# #Shallow Copy


# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ValueError:
#     print("Please enter a valid number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# else:
#     print("Result:", result)
# finally:
#     print("Execution complete.")

 
# list1=[[1,2,3],[4,5,6],[7,8,9]]
# list2=[]
# for i in range(len(list1)):
#     list2.append(max(list1[i]))
# print(list2)

# list1=[[1,2,3],[4,5,6],[7,8,9]]
# list2=[j for i in list1 for j in i if j==max(i)]
# print(list2)
# a=3
# b=6
# c=9

# big=max(a,b,c)
# n=big
# small=min(a,b,c)


# while True:
#     if big%small==0  and medium%small==0: 
#         print("LCM is",big)
#         break
#     else:
#         big=big+n
        #Python Comprehension

#List Comprehension
# squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
# print(squares)

# #Dictionary Comprehension
# squares_dict = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# print(squares_dict)


# Three numbers


# num1=int(input("Enter the First NO:"))
# num2=int(input("ENter the secound No:"))
# num3=int(input("Enter the third NO:"))
# max_num = max(num1,num2,num3)
# while True:
#     if (max_num%num1==0) and (max_num%num2==0) and (max_num%num3==0):
#         lcm = max_num
#         break
#     max_num += 1

# print("LCM of", num1,num2,num3, "is:", lcm)
# count=0
# num=100
# if num==1:
#     count=0
# else:
#     while True:
#         quo=num//2
#         rem=num-quo
#         num=rem
#         count+=1
#         if num==1:
#             break

    
# print(count)




# str="0010"
# temp=str[0]
# count1=0
# count2=0
# for i in range(len(str)):
#     if str[i]==temp:
#         count1+=1
#     else:
#         count2+=1
#     if count1==count2:
#         print(count1+count2)
#         break
# list1=[1,3,4,5,6,6]
# # list1.extend(9)
# print(list1.count(9))
# print(list1)

# dict={"a":2,"b":6,"c":8}
# dict["a"]=10
# print(dict)

# list=[2,5,7,8]
# print(max(list))
# for i in range(len(list)):
#     sum=sum+list[i]
# # print(sum)
# list=[2,5,5,7,8,8]
# unq=[]
# for i in range(len(list)):
#     if list[i] not in unq:
#         unq.append(list[i])
# print(unq)

# str="apple banana apple"
# dict={}
# list=str.split(" ")
# dict("apple"(list.count("apple")))



# n=9
# c=True
# for i in range(n,0,-1):
#     if i==5 and c:
#         print(i,end=" ")
#         c=False
#         pass
#     else:
#         print(i,n-(i-1),end=" ")


# n=150
# pri_count=0
# while True:
#     count=0
#     for i in range(2,n,1):
#         if n%i==0:
#             count+=1
#     if count==0:
#         print(n,end=" ")
#         pri_count+=1
#     n=n+1
#     if pri_count==30:
#         break
###############

'''
x = "global"  # Global Scope

def outer():
    x = "enclosing"  # Enclosing Scope
    def inner():
        x = "local"  # Local Scope
        print("Inner:", x)
    inner()
    print("Outer:", x)

outer()
print("Global:", x)
'''
'''import random

print(random.randint(1,10))'''

# import random
# print(random.randint(1,20))

# kilometers=5

# miles=kilometers*0.621
# print(miles)


'''celsius=30
fahrenheat=(celsius*9/5)+32
print(fahrenheat)

celsius=(fahrenheat-32)*5/9
print(celsius)'''
''''import calendar 
print(calendar.month(2003,6))'''

# import calendar

# print(calendar.month(2003,6))

# import math

# a=float(input("Enter coefficient a"))
# b=float(input("Enter coefficient b"))
# c=float(input("Enter coefficient c"))

# disc=b**2-4

#Whiout Zip 

# list1=["a","b","c","d","e","f"]
# list2=[1,2,3,4,5,6]

# new_list=[]
# for i in range(len(list1)):
#     new_list.append((list1[i],list2[i]))

# print(new_list)


#Output => [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6)]
#----------------------------------------------------------------------------
#With Zip

# list1=["a","b","c","d","e","f"]
# list2=[1,2,3,4,5,6]


# res=list(zip(list1,list2))
# print(res)

# # Output => [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6)]

# class Car:
#     # Class variables
#     def __init__(self, brand, model, year): #Constructor
#         # Instance variables
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def display_info(self):                 #Method
#         print(f"Car Brand: {self.brand}",end=",")
#         print(f"Model: {self.model}",end=",")
#         print(f"Year: {self.year}")


# car1 = Car("Toyota", "Camry", 2022)  # Creating object /instances 
# car2 = Car("Hyundai", "Verna", 2023)

# car1.display_info() #Output: Car Brand: Toyota,Model: Camry,Year: 2022
# print("\n")
# car2.display_info() # Output: Car Brand: Hyundai,Model: Verna,Year: 2023
#Single Inheritance

# # Parent class
# class Animal:
#     def sound(self):
#         print("Animals make sounds")

# # Child class
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# # Create object
# d = Dog()
# d.sound()  # Inherited from Animal 
# d.bark()   # Specific to Dog


# for i in range(10):
#     a,b=0,1
#     print(a)
#     a=b
#     b=a+b
    
    
    
# l=[1,2,3,4,5,6,7,8,9,10,"python",True]

# for i in range(len(l)):
#     if isinstance(l[i],bool):
#         pass
#     elif isinstance(l[i], int):
#         l[i] *= 2
   
# print(l)
   

# l=[1,10,20,30,50,60]
# sum=0
# for i in range(len(l)):
#     sum=l[i]
#     sum+=sum
# print(sum)
     

# l="Madhu"
# k="sdf"
# if  str(type(l))=="<class 'str'>":
#     print("This is True") 
    



    


# for i in range(10,20+1,2):
#     print(i)

# for i in range(10,20+1,2):
#     print(i)

# n=10
# while n!=20+1:
#     if n%2==0:
#         print(n)
#     n=n+1

# n=10
# while n!=20+1:
#     if n%2!=0:
#         print(n)
#     n=n+1

# n=10
# while n!=20+1:
#     if n & 1 ==0:
#         print(n)
#     n=n+1

# n=10
# while n!=20:
#     if n & 1 ==1:
#         print(n)
#     n=n+1


# n=10
# while n!=20:
#     rem=divmod(n,2)
#     if rem==1:
#         print(n)
#     n=n+1







# string="Madhukiran"

# new_str=""
# for i in range(-1,-(len(string)+1),-1):
#     new_str+=string[i]
    
# print(new_str)

# new_str=""

# for i in range(len(string)):
#     if string[i] not in new_str:
#         new_str+=string[i]
        
# print(new_str)

# l=[2,6,9,3,5,7,10,15,1]
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[i]>l[j]:
#             l[i]=l[j]
            
            
            
            
# print(l)
# l=[2,6,9,3,5,7,10,15,1]

# small=l[0]
# for i in range(len(l)):
#     if small>l[i]:
#         small=l[i]
# print(small)
    
    
    
# max=l[0]
# for i in range(len(l)):
#     if max<l[i]:
#         max=l[i]
# print(max)
    

# import keyword  as ky
# print(ky.kwlist)

# for i in range(-10,1,1):
#     if i%2==0:
#         print(i-1)
        # def len_fun(l):
#     count=0
#     for i in l:
#         count+=1
#     return count

# l=[1,2,3,4,5,6,7]
# obj=len_fun(l)
# print(obj)
# def sum_list(l):
#     sum=0
#     for i in l:
#         sum+=i
#     return sum

# l=[1,2,3,4,5,6,7]
# obj=sum_list(l)
# print(obj)
        
        
# st="MadhuKIRAN"

# for i in range(len(st)):
#     if ord(st[i])>=65 and ord(st[i])<=90 :
#         new_str+=chr(ord(st[i])+32)
#     elif ord(st[i])>=97 and ord(st[i])<=122:
#         new_str+=chr(ord(st[i])-32)
# print(new_str)
# st='PythonDeveloper'

# for i in range(-1,-len(st),-1):
#     print(st[i])

# s=""
# for i in st:
#     s=i+s
# print(s)
    
# n=153
# count=0
# temp=n
# temp2=n
# while n!=0:
    # rem=n%10
    # count+=1
    # n=n//10

# sum=0
# while temp!=0:
    # re=temp%10
    # sum+=re**count
    # temp=temp//10
    
# if sum==temp2:
    # print("True")
# else:
    # print("False")


# n=5
# count=0
# while count<5:
    # print("* "*5)
    # count=count+1
    
    
#task-02
#row=5
#for row in range(1,row+1):
    #string=""
    #for col in range(1,row+1):
        #string+=str(row)+" "
    #print(string)

# row=5
# for row in range(1,row+1):
#     string=""
#     for col in range(row):
#         string+=str(col+1)+" "
#     print(string)




# num=7
# if num & 1==0:
#     print("even")
# else:
#     print("odd")    



# n
# d=7569791711
# length=0
# temp=d
# if d == 0:
#     length = 1
# else:   
#     while temp > 0:
#      temp=temp // 10
#      length += 1
# print("length:",length)  



# num=756979111
# string=str(num) 
# for i in range(len(string)-1,-1,-1):
#      print(string[i],end=" ")





# row=5
# for i in range (1,row+1):
#     res1=""
#     for j in range(1,row+1):
#         if i+j==row+1 or i==row or  j==row:
#             res1+="*"+" "
#         else:
#             res1+=" "+" "
#     print(res1)
      
            
# row=5 
# for i in range(1,row+1):
#     res2=""
#     for j in range(1,row+1):
#         if i+j<=row+1:
#             res2+="*"+" "
#         else:
#             res2+=" "+" "
#     print(res2)

# row=5
# for i in range (1,row+1):
#     res1=""
#     for j in range(1,row+1):
#         if i+j>=row+1:
#             res1+="*"+" "
#         else:
#             res1+=" "+" "
#     print(res1)              
# 0 1 1 2 3 5 8 13 21 34 55
# a b
#   a=b  b=

# n=5
# a,b=0,1
# for i in range (1,n+1):
#     b=a+b
#     print(a)
#     a=b
# # use_input=int(input())
    
# *         *
# * *     * *
# *  *  *   *
# *   *     *
# *         *
# *         *

#      *
#     * *   
#    *   *
#   *******
#  *       *
# *         *

# *
# *  *
# *    *
# *      *
# *     *    
# *  *
# * 

# *        *
# *        *
# *        *
# **********
# *        *
# *        *
# *        *

# *           *
#  *         *
#   *       *
#    *     *
#      * *

# for i in range(1,7):
#     for j in range(1,8):
#         if j==1 or j==7:
#             print("*",end=" ")
#         else:
#             print(" "+" ")
#     print("\n")
        
        
        

# n = 7 
# for row in range(n):
#     for col in range(n):
#         if col == 0 or col == n - 1 or (row == col and col <= n // 2) or (row + col == n - 1 and col >= n // 2):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# print() 

# for row in range(n):
#     for col in range(n):
#         if (col == 0 or col == n - 1) and row != 0 or (row == 0 and col > 0 and col < n - 1) or row == n // 2:
#             print("$", end="")
#         else:
#             print(" ", end="")
#     print()
# print()

# for row in range(n):
#     for col in range(n):
#         if col == 0 or (col == n - 1 and row != 0 and row != n - 1) or ((row == 0 or row == n - 1) and col < n - 1):
#             print("#", end="")
#         else:
#             print(" ", end="")
#     print()
# print()

# for row in range(n):
#     for col in range(n):
#         if col == 0 or col == n - 1 or row == n // 2:
#             print("@", end="")
#         else:
#             print(" ", end="")
#     print()
# print()

# for row in range(n):
#     for col in range(n):
#         if (col == 0 or col == n - 1) and row != n - 1 or (row == n - 1 and col > 0 and col < n - 1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()






# n = 7 
# for row in range(n):
#     for col in range(n):
#         if col == 0 or (row == 0 and col < n - 1) or (row == n // 2 and col < n - 1) or (col == n - 1 and row > 0 and row < n // 2):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# print()

# for row in range(n):
#     for col in range(n):
#         if ((col == 0 or col == n - 1) and row != n - 1) or (row == n - 1 and col > 0 and col < n - 1):
#             print("$", end="")
#         else:
#             print(" ", end="")
#     print()
# print()

# for row in range(n):
#     for col in range(n):
#         if col == 0 or col == n - 1 or row == col:
#             print("#", end="")
#         else:
#             print(" ", end="")
#     print()
# print()


# for row in range(n):
#     for col in range(n):
#         if row == 0 or row == n - 1 or col == n // 2:
#             print("@", end="")
#         else:
#             print(" ", end="")
#     print()
# print()

# for row in range(n):
#     for col in range(n):
#         if row == 0 or col == n // 2:
#             print("+", end="")
#         else:
#             print(" ", end="")
#     print()
# print()

# for row in range(n):
#     for col in range(n):
#         if col == 0 or col == n - 1 or row == n // 2:
#             print("&", end="")
#         else:
#             print(" ", end="")
#     print()
# print()

# for row in range(n):
#     for col in range(n):
#         if (col == 0 or col == n - 1) and row != 0 or (row == 0 and col > 0 and col < n - 1) or row == n // 2:
#             print("=", end="")
#         else:
#             print(" ", end="")
#     print()
# print()
  
  
  
  
  
  

# n=9
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print("\n")
# for i in range(n-1,0,-1):
#     for j in range(i,0,-1):
#         print("*",end=" ")
#     print("\n")


# def my_decorator(fun):
#     def madhu():
#         print("Before the function run ")
#         fun()
#         print("after the function call ")
#     return madhu

# def say_hi():
#     print("Hello")
# say_hi = my_decorator(say_hi)
# say_hi()
    




 
#         *
#       * *
#     * * *
#   * * * *
# * * * * *


# rows=5

# for row in range(1,rows+1):
    
#     for col in range(1,rows+1):
#         if row+col>=rows+1:
#             print("+",end=" ") 
#         else:
#             print(" ",end=" ")
#     print()


# import math
# n=5
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         if row==1 or row==5 or col==1 or col==5 or  (row==math.ceil(n/2) and col==math.ceil(n/2)):
#              print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# name="madhu"
# vowels="aeiou"

# res=""

# for char in name:
#     if char in vowels:
#         res+= str(vowels.index(char)+1)
#     else:
#         code=ord(char)
#         res+=chr(code+1)
        
# # print(res)

# cou=5
# for i in range(2,n+1):
#     is_prime=True
#     for j in range(2,i):
#         if i%j==0:
#             is_prime=False
#             break
#     if is_prime :
#         print(i,end=" ")
#         count+=1




# n=10
# co=True
# while co:
#      for i in range()
    
# def decorator_function(func):
#     def wrapper():


# #Diagonal elements of a matrix

# li=[[1,2,3],[4,5,6],[7,8,9]]
# for i in range(len(li)):
#    print(li[i][i],end=" ")
   
# #Output:1 5 9
# #------------------------------

# #Finding the maximum index of a list of lists
# li=[[1,2],[4,5,6],[7,8,9,3]]
# re=max([i for i in range(len(li))])
# print(re)
#Output= 2



# name="ma_dhu_ki_ran"
# new_str=" "
# for i in range(len(name)):
#    if name[i]=="_" and i<=len(name)-2:
#        cap_let=(name[i+1]).upper()
#        new_str+=cap_let
      
#    else:
#        if  name[i] !="_" and chr(ord((name[i]).lower())-32)!= new_str[-1]:
#            new_str+=name[i]
# print(new_str)


# x="ma_dh_u_ki_ran"
# i=0
# for j in range(len(x)):



# str="ma_dhu_ki_ran"
# res=''
# for i in range(len(str)):
#     if str[i]=='_' and i<=len(str)-2:
#         s1=str[i+1]
#         s1=s1.upper()
#         res=res+s1
#     else:
#         if str[i-1]=="_" and (i-1)!=-1:
#             continue
#         else:
#             # if str[i]!="_":
#                 res+=str[i]
# print(res)
    
    
# lis=[1,2,3,4,5,6,7,8,9]

# for i in range(-len(lis),0,1):
#     print(lis[i],end=" ")

# i=0
# while i<len(lis):
#     print(lis[i],end=" ")
#     i+=1
# count=0
# val=0
# for i in range(len(lis)):
#     if lis.count(lis[i])>count:
#         count=lis.count(lis[i])
#         val=lis[i]
# print(val)


# lis2=lis.copy()
# lis[0]=10
# print(lis2)
# print(lis)
# lis.insert(2,2)
# lis[2:2]=[5,6]

# lis[2:1]=[5,6,7]
# lis.insert(2,5,5)
# lis.extend([8,9])


# lis[2:]=[11,12,13]
# print(lis)
# lis[2:0]=[11,12,13]
# print(lis)
# lis[2:1]=[11,12,13]
# print(lis)
# lis[2:2]=[11,12,13]
# print(lis)
# lis[2:3]=[11,12,13]
# print(lis)
# lis[2:4]=[11,12,13]
# print(lis)

# lis=[1,2,3,4]
# new=[11,12,13]
# lis[2:2]=new
# print(lis)


# license






# lis=[1,2,3,4,5,6]
# use=3
# use_list=[6,7,8]

# out=1,2,3,6,7,8,5,6


# j=0
# for i in range(2,len(use_list)+1):
#     lis[i]=use_list[j]
#     j+=1
# print(lis)









# lis=[1,2,3,4,5,6]

# user_index=3
# user_list=[6,7,8]  #1,2,3,6,7,8,4,5,6
# res=[]
# for i in range(0,len(lis)+len(user_li))
# lis=[1,2,3,4]
# use_index=3
# user_lis=[4,5,6]
# lis[use_index:use_index]=user_lis
# # lis.append(1,2,3)
# print(lis)

# user_index=3
# user_list=[6,7,8]  #1,2,3,6,7,8,4,5,6
# res=[]
# j=0
# for i in range(0,(len(lis)+len(user_list))):
#     if i<3:
#         res.append(lis[i])
        
#     elif j<len(user_list):
#         res.append(user_list[j])
#         j+=1
#     else:
#         res.append(i-(len(user_list)-1))
# print(res)


# lis=["flower","flow","flight","flourish"]
# small_str=[]
# c=len(lis[0])
# for i in range(len(lis)):
#     if len(lis[i])<c:
#         c=len(lis[i])
    
    
# lis=[[1,2,3],[4,5,6],[7,8,9]]

# for i in range()  
 
 
 #2**3
# res=1
# for i in range(3):
#     temp=0
#     for j in range(2): 
#         temp+=res
#     res=temp
# print(res)

# n=6
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end=" ") 
#         else:
#             print(" ",end=" ")
            
#     print("")
    
# n=4  
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j==1:
#             print(" "*(n-i),end=" ")
#         print(i,end=" ")
        
#     print("") 


# import requests

# def send_otp_via_fast2sms(phone_number, otp):
#     url = "https://www.fast2sms.com/dev/bulkV2"
#     headers = {
#         "authorization": "YOUR_API_KEY_HERE",
#     }
#     payload = {
#         "variables_values": otp,
#         "route": "otp",
#         "numbers": phone_number
#     }
#     response = requests.post(url, headers=headers, data=payload)
#     return response.text

# otp = generate_otp()
# print("Generated OTP:", otp)
# response = send_otp_via_fast2sms("9876543210", otp)
# print("API Response:", response)             
     
     
# import math as m
# #SQUARE ROOT
# print("SQUARE ROOT:",m.sqrt(64))
# #FACTORIAL
# print("FACTORIAL:",m.factorial(5))
# #LCM
# print("LCM:",m.lcm(12,8))
# #GCD
# print("GCD:",m.gcd(12,8))
# #CEIL
# print("CEIL:",m.ceil(2.4))
# #FLOOR
# print("FLOOR:",m.floor(2.4))
# # Euler's Number
# print("Euler's Number:",m.e)
# #PI VALUE
# print("PI VALUE:",m.pi)
# #ABSOLUTE VALUE
# print("ABSOLUTE VALUE:",m.fabs(-10))
# #POWER
# print("POWER:",m.pow(2,3))

        


# def max_num(lis):
#     return max(lis)

# lis=[3,6,8,4,8,9,4,6]
# print(max_num(lis))


# def max_num(lis):
#     sort_lis=lis.sort()
#     a=sort_lis[-1]
    
#     return a
# lis=[3,6,8,4,8,9,4,6]
# max_num(lis)
    



# lis=[3,6,8,4,8,9,4,6]


# lis.sort()
# b=-1
# for i in range(len(lis)):
#     if lis[b]!=lis[b]:
#         print(lis[-2])
#     else:
      
# b="a[3]b[2]c[1]"  
# res=""

# c=""
# for i in range(len(b)):
#     if b[i]=="[":
#         c+=b[i+
    
#     elif b[i].isalpha:
#         res+=b[i]
#     elif b[i].isdigit:
        


# s="a[3]b[2]c[1]" 
# res=""
# d=""
# a=""
# for i in range(len(s)):
#     if s[i].isalpha():
#         a+=s[i]
    
#     elif s[i]=="[":
#         pass
#     elif s[i]=="]":
#         res+=(a)*int(d)
#         d=""
#         a=""
    
#     elif s[i].isdigit():
#         d+=s[i]
        
# print(res)
        
# s="aaabbcc"

# res=""
# count=1
# for i in range(1,len(s)):
#     if s[i]==s[i-1]:
#         count+=1
#     elif s[i]!=s[i-1]:
#         res+=s[i-1]+str(count)
#         count=1
# res+=s[i]+str(count)
# print(res)
    
# a=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]   

# b=[[7,8,9],   #[8,10,12]
#    [4,5,6],   #[8,10,12]
#    [1,2,3]]   #[8,10,12]
        
# res=[]
# for i in range(len(a)):
#     l=[]
#     for j in range(len(a)):
#         l.append((a[i][j])+(b[i][j]))
#     res.append(l)
    
# print(res)



# a=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]   

# b=[[7,8,9],   
#    [4,5,6],  
#    [1,2,3]]  


# res=[]
# for i in range(len(a)):
#     l=[]
#     for j in range(len(a)):
#         l.append((a[i][j])*(b[j][i]))
#     res.append(l)
        
# print(res)


# s="ma_dhu_kir_an"

# ne=""
# for i in range(len(s)):
#     if s[i]=="_":
        

# num=2518 #5182
# list=["1534","2518","86","2001"]
# new_list=[]

# res=""
# for j in range(len(list)):
#     new_num=list[j]
#     for i in range(len(new_num)):
#         if int(new_num[i]) % 2 != 0:
#             new_list.append( new_num[i:] + new_num[:i])
#             break
#         elif (len(new_num)-1)==i:
#             new_list.append(new_num)
            
            
# print(new_list)




# s="abcde"
# sub="ec"
# k=0
# for i in range(len(s)):
#     if sub[k]==s[i]:
#         k=k+1
        
# if k==len(sub):
#     print("yes")
# else:
#     print("no")
  

n = "21582950"
res = ""


for i in range(len(n)):
    if int(n[i]) % 2 != 0:
        res = n[i:]
        break


while int(res)%2==0:
    res=str(int(res)//10)
    
print(res)
    
    
    
    
    
    



