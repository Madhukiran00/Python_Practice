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


for i in range(10):
    a,b=0,1
    print(a)
    a=a+b
    
    












