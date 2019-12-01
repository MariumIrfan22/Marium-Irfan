#!/usr/bin/env python
# coding: utf-8

# # problem 3.1

# In[1]:


fahrenheit = eval(input( 'Enter the temperature in degrees Fahrenheit: ' ))
celsius = (5/9)*(fahrenheit - 32)
print( 'The temperature in degrees Celsius is' , celsius)


# # problem 3.2

# In[24]:


#a
age=eval(input("enter the age:"))
if age>62:
    print('you can get your pension benefits')


# In[20]:


#b
list=['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']
if 'Musial'in list:
    print('one of the top 5 baseball player ever!')


# In[22]:


#c
hits=eval(input("enter the no of hits:"))
sheild=eval(input("enter the sheild:"))
if hits>10 and sheild is 0:
    print('You are dead...')


# In[23]:


#d
bool=['north','south','east','west']
if 'north' in bool:
    print("i can escape")


# # problem 3.3

# In[25]:


year=eval(input("enter the year:"))
if year%4:
    print('could be a leap year')
else:
    print('better luck next time')


# # problem 3.4

# In[27]:


login=str(input("enter the login id:"))
list=['joe', 'sue', 'hani', 'sophie']
if login in list:
    print('you are a valid user')
else:
    print('user unknown')
print('done')


# # problem 3.5

# In[1]:


word_list = eval(input("Enter word list: "))
for word in word_list:
    if len(word) == 4:
        print(word) 


# # problem 3.6

# In[2]:


for i in range(10):
    print(i)


# In[3]:


for i in range(2):
    print(i)


# # problem 3.7

# In[4]:


for i in range(3 ,13):
    print(i)


# In[5]:


for i in range(0, 10, 2):
    print(i)


# In[6]:


for i in range(0 , 24, 3):
    print(i)


# In[7]:


for i in range(3 ,12 , 5):
    print(i)


# # problem 3.8

# In[8]:


import math
def perimeter(r):
    return 2*math.pi * r


# In[9]:


perimeter(1)


# In[10]:


perimeter(2)


# # problem 3.9

# In[11]:


def average(x,y):
    'it will return average of two values'
    return (x+y)/2


# In[12]:


average(1,3)


# In[14]:


average(23,5)


# # problem 3.10

# In[15]:


def noVowel(n):
    'return true if string n contains vowel otherwise return false'
    for c in n:
        if c in "aeiouAEIOU":
            return False
    return True


# In[16]:


noVowel('marium irfan')


# In[17]:


help(noVowel)


# # problem 3.11

# In[18]:


def allEven(list_num):
    for num in list_num:
        if num %2 != 0:
            return False
    return True


# In[19]:


allEven([8, 0 , -2, 4, -6, 10])


# In[20]:


allEven([2,3,4,1,2,-2])


# # problem 3.12

# In[2]:


def negatives(neg_num):
    'this will take negative value in list and return one per line'
    for i in neg_num:
        if i < 0:
            print(i)


# In[3]:


negatives([4,0,-1,-3,6,-9])


# # problem 3.13

# In[5]:


s = input("Enter square or cube: ")
if s == "square":
    def f(x):
        return x**2
else:
    def f(x):
        return x**3


# In[6]:


f(2)


# # problem 3.15

# In[10]:


def swap_teams(list_team):
    list_team[0],list_team[-1] = list_team[-1], list_team[0]
    return list_team
swap_teams(['ava','eleanor', 'clare', "sarah"])


# # problem 3.17

# In[12]:


eval("2*3+1")


# In[15]:


#eval("hello")
#we will get error because no operation like + - is performed here and entered variable is string data type


# In[16]:


eval("'hello' + ' ' + 'world'")


# In[17]:


eval("'ASCII'.count('I')")


# In[18]:


#eval("x = 5")
#first we need to define value of x outside an eval function 
#we cannot define x using eval function.


# # problem 3.18

# In[4]:


a=3
b=4
c=5
if a<b:
    print('ok')
if c<b:
    print('ok')
if a+b==c:
    print('ok')
if a**2+b**2==c**2:
    print('ok')


# # problem 3.19

# In[5]:


a=3
b=4
c=5
if a<b:
    print('ok')
else:
    ('not ok')
if c<b:
    print('ok')
else:
    print('not ok')
if a+b==c:
    print('ok')
else:
    print('not ok')
if a**2+b**2==c**2:
    print('ok')


# # problem 3.20

# In[19]:


lst = ["January", "February", "March"]
for word in lst:
    print(word[:3])


# # problem 3.21

# In[20]:


lst = [2, 3, 4, 5, 6, 7, 8, 9]
for x in lst:
    if x%2 == 0:
        print(x)


# # problem 3.22

# In[21]:


lst = [2, 3, 4, 5, 6, 7, 8, 9]
for x in lst:
    if (x**2)%8 == 0:
        print(x)


# # problem 3.23

# In[22]:


for i in range(2):
    print(i, end=" ")
for i in range(1):
    print(i, end=" ")
for i in range(3,7):
    print(i, end= " ")
for i in range(1,2):
    print(i, end=" ")
for i in range(4):
    print(i, end =" ")
for i in range(5, 22, 4):
    print(i, end= " ")


# # problem 3.24

# In[23]:


lst = ['cia', 'secret', 'mi6', 'isi', 'secret']
for word in lst:
    if word != 'secret':
        print(word)


# # problem 3.25

# In[25]:


student_lst = eval(input("Enter list of student names: "))
for word in student_lst:
    if word[0] >= "A" and word[0] <= "M":
        print(word)


# # problem 3.26

# In[26]:


lst_num = eval(input("Enter list of numbers: "))
print("The first num of list is:", lst_num[0])
print("The Last num of list is:", lst_num[-1])


# # problem 3.27

# In[27]:


n = eval(input("Enter number: "))
for i in range(4):
    print(n*i)


# # problem 3.28

# In[32]:


n = eval(input("Enter number: "))
for i in range(n):
    print(i*i)


# # problem 3.29

# In[35]:


n = eval(input("Enter n: " ))
for i in range(1,n+1):
    if(n%i==0):
        print(i)


# # problem 3.30

# In[34]:


n1 = eval(input("Enter first number: " ))
n2 = eval(input("Enter second number: " ))
n3 = eval(input("Enter third number: " ))
n4 = eval(input("Enter last number: " ))
if (n1+n2+n3)/3 == n4:
    print("Equal")


# # problem 3.31

# In[33]:


x = eval(input("Enter x: " ))
y = eval(input("Enter y: " ))
if x**2+y**2 < 8**2:
    print("It is in!")


# # problem 3.32

# In[57]:


n=int(input('enter four integers:'))
x=n%10
y=x-3
for num in range(y,x+1):
    print(num)


# # problem 3.33

# In[38]:


def reverseStr(s):
    'This will take a string and print it in reverse order'
    return s[::-1]


# In[39]:


reverseStr("abc")


# In[40]:


reverseStr("dna")


# # problem 3.34

# In[42]:


def pay(wage,hours):
    payment = 0
    if(hours > 40):
        payment = payment + (hours-40)*wage*1.5
        payment = payment + (40)*wage
    else:
        payment = payment + hours*wage
    return payment


# In[43]:


pay(20,45)


# In[44]:


pay(10,35)


# # problem 3.35

# In[47]:


def prob(n):
    return 2**(-n)


# In[48]:


prob(1)


# In[49]:


prob(2)


# # problem 3.36

# In[51]:


def reverse_int(n):
    x=0
    while(n!=0):
        x*=10
        x+=n%10
        n=n//10
    return x
reverse_int(123)


# # problem 3.37

# In[52]:


import math
def points(x1,y1,x2,y2):
    distance = str(math.sqrt((x1-x2)**2+(y1-y2)**2))
    if(x1==x2):
        slope = "infinity"
    else:
        slope = str((y2-y1)/(x2-x1))
    print("The slope is "+slope+" and the distance is "+distance)
points(0,0,1,1)


# # problem 3.38

# In[54]:


def abbreviation(day):
    if(day == "Monday"):
        return "Mon"
    elif(day == "Tuesday"):
        return "Tues"
    elif(day == "Wednesday"):
        return "Wed"
    elif(day == "Thursday"):
        return "Thrs"
    elif(day == "Friday"):
        return "Fri"
    elif(day == "Saturday"):
        return "Sat"
    elif(day == "Sunday"):
        return "Sun"
abbreviation("Monday")


# # problem 3.39

# In[53]:


def collision(x1,y1,r1,x2,y2,r2):
    if(math.sqrt((x1-x2)**2+(y1-y2)**2) > r1+r2):
        return False
    else:
        return True
collision(0,0,3,0,5,3)


# # problem 3.40

# In[55]:


def partition(list):
    for name in list:
        if name[0] >= "A" and name[0] <= "M":
            print(name)
partition(["Eleanor", "Evelyn", "Sammy", "Owen", "Gavin"])


# # problem 3.41

# In[31]:


def lastF(firstname,lastname):
    return lastname+", "+firstname[0]+"."
lastF("marium","irfan")


# # problem 3.42

# In[30]:


def avg(lists):
    for list in lists:
        print(sum(list)/len(list))
avg([[95,92,86,87],[66,54],[89,72,100],[33,0,0]])


# # problem 3.43

# In[29]:


import math
def hit(x1,y1,r,x2,y2):
    if(math.sqrt((x1-x2)**2+(y1-y2)**2) > r):
        return True
    else:
        return False
hit(0,0,3,3,0)


# # problem 3.44

# In[28]:


def distance(n):
    return n*340.29/1000
distance(3)

