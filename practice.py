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

str="Python"
vowels="aeiouAEIOU"
stat=True
count=0
for i in str:
    if count==4:
        stat=False
        break
    if i not in  vowels:
        count+=1
    else:
        count=0
if stat:
    print("Yes")
else:
    print("No")








