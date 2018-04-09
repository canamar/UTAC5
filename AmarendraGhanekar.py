
# coding: utf-8

# In[ ]:


# Examples from the course Website


# In[12]:


import math


# In[7]:


math.sqrt(25)


# In[8]:


math.pi


# In[13]:


import scipy


# In[3]:


from scipy import stats


# In[9]:


import math as mt


# In[10]:


mt.sqrt(25)


# In[34]:


mt.sqrt(16)


# In[33]:


import numpy as np


# In[30]:


from numpy import random


# In[38]:


dataOne = numpy.random.rand(5,5)


# In[46]:


print(dataOne)


# In[47]:


np.mean(dataOne)


# In[48]:


print('Why am I doing this???')


# In[49]:


v1 = 25


# In[51]:


print(v1)


# In[102]:


v1 = 'Why am I doing this???'


# In[103]:


print(v1)


# In[54]:


v1 = 25
type(v1)


# In[55]:


v1=25.000
type(v1)


# In[57]:


v1=25
v2=25.00
v3=v1+v2
print(v3)


# In[61]:


v1=25
v2="Why am I doing this???"
print(v1,v2)


# In[64]:


listOne = [1,2,3,4]
print(listOne[1:3])


# In[65]:


listOne = [1,2,3,4]
print(listOne[0:3])


# In[67]:


tel = {'Bob':1000, 'jack':2000, 'Dan':3000}
tel['jack']


# In[71]:


print('Jacks Tel No. is',tel['jack'])


# In[74]:


Dictionary1 = {1:100, 2:200, 3:300, 4:400, 5:500}
Dictionary1 [3]


# In[88]:


v1 = Dictionary1 [1]


# In[89]:


v2 = v1 + 1000


# In[90]:


print(v2)


# In[85]:


v1 = Dictionary1 [1] + Dictionary1 [2] + Dictionary1 [4]


# In[86]:


print(v1)


# In[97]:


v1 = Dictionary1 [1]
v2 = Dictionary1 [2]
v3 = Dictionary1 [3]
v4 = Dictionary1 [4]
v5 = Dictionary1 [5]


# In[98]:


v = v1*v2


# In[99]:


print(v)


# In[100]:


v = v1+(v2+v3)*v4


# In[101]:


print(v)


# In[2]:


# Examples from the book 
### Chapter4
################
# Working with numbers and logic


# In[1]:


MyVar = 5
print(MyVar)


# In[2]:


MyVar = 5
MyVar += 5
print(MyVar)


# In[3]:


MyVar = 5
MyVar -= 2
print(MyVar)


# In[4]:


MyVar = 5
MyVar *= 2
print(MyVar)


# In[5]:


MyVar = 5
MyVar /= 2
print(MyVar)


# In[6]:


MyVar = 5
MyVar %=2
print(MyVar)


# In[11]:


MyVar = 5
MyVar **=2
print(MyVar)


# In[12]:


1 == 2


# In[13]:


1 != 2


# In[14]:


1 >2


# In[15]:


1 <2


# In[16]:


1 <=2


# In[17]:


1>=2


# In[18]:


True and True


# In[19]:


True and False


# In[20]:


False and False


# In[21]:


False and True


# In[22]:


not True


# In[23]:


not False


# In[24]:


True or False


# In[25]:


False or True


# In[26]:


True or True


# In[27]:


False or False


# In[29]:


"Hello" in "Hello Goodbye"


# In[30]:


"Hello" not in "Hello Goodbye"


# In[34]:


type(2) is int 


# In[35]:


type(2) is not int


# In[36]:


#Functions
def SayHello():
    print('Why am I doing this?!')


# In[37]:


SayHello()


# In[43]:


def DoSum(Value1,Value2):
    return Value1 + Value2


# In[44]:


DoSum(100,300)


# In[45]:


def DisplaySum(Value1, Value2):
    print(str(Value1) + ' + ' + str(Value2) + ' = ' + str(Value1+Value2))


# In[46]:


DisplaySum(25,50)


# In[47]:


def SayHi(Greetings = "No value supplied"):
    print(Greetings)


# In[49]:


SayHi()


# In[50]:


SayHi("Why am I doing this???")


# In[54]:


def DispMulti(ArgCount = 0, *VarArgs):
    print('You passed '+ str(ArgCount) + ' arguments.')


# In[55]:


DispMulti()


# In[56]:


DispMulti(3, "Hello", 1, True)


# In[57]:


#Conditional and loop statements
# Decision making


# In[58]:


def TestValue(Value):
    if Value == 5:
        print('Value equals 5!')
    elif Value == 6:
        print('Value equals 6!')
    else:
        print('Value is somethng else.')
        print('It equals to ' + str(Value))
        


# In[59]:


TestValue(5)


# In[60]:


TestValue(6)


# In[61]:


TestValue(100)


# In[ ]:


#Choosing between multiple options using nested decision


# In[9]:


def ScreenNumber():
    One = int(input("Type a number between 1 and 10: "))
    Two = int(input("Type a number between 1 and 10: "))
    if (One >= 1) and (One <= 10):
        if (Two >= 1) and (Two <= 10):
          print('Your secret number is : ' + str(One*Two))
        else:
          print("Incorrect Second value")
    else:
        print("Incorrect First value")


# In[15]:


ScreenNumber()


# In[ ]:


# different approach:If first number is not in the range, throw error and dont ask for second number...


# In[1]:


def ScreenNumber():
    One = int(input("Type a number between 1 and 10: "))
    if (One >= 1) and (One <= 10):
        Two = int(input("Type a number between 1 and 10: "))
        if (Two >= 1) and (Two <= 10):
          print('Your secret number is : ' + str(One*Two))
        else:
          print("Incorrect Second value")
    else:
        print("Incorrect First value")


# In[2]:


ScreenNumber()


# ## 

# In[ ]:


# Performing repetitive tasks using for


# In[27]:


def DisplayMulti(*VarArgs):
    for Arg in VarArgs:
        if Arg.upper() == 'CONT':
            continue
            print('Continue Argument :' + Arg)
        elif Arg.upper() == 'BREAK':
            break
            print('Break Argument: ' + Arg)
        print('Good Argument: ' + Arg)


# In[28]:


DisplayMulti('Hello','Goodbye','CONT','First','BREAK', 'Last')


# In[ ]:


#While statement


# In[8]:


def SecretNumber():
    GotIt = False
    while GotIt == False:
        One = int(input("Type a number between 1 and 10: " ))
        Two = int(input("Type a number between 1 and 10: "))
        
        if (One >= 1) and (One <= 10):
            if (Two >= 1) and (Two <= 10):
                print('Your secret number is : ' + str(One*Two))
                GotIt = True
                continue
            else:
                print("Incorrect Second value")
        else:
            print("Incorrect First value")
            print("Please try again...")        


# In[11]:


SecretNumber()


# ## 

# In[ ]:


#Performing Operation on sets


# In[4]:


#from sets import set - this is no more needed. This book is OLD!
setA = set(['Red','Blue','Green','Black'])
setB = set(['Black','Green','Yellow','Orange'])
setX = setA.union(setB)
setY = setA.intersection(setB)
setZ = setA.difference(setB)


# In[7]:


print(setX,setY,setZ)


# In[8]:


#Print on new ine
print('{0}\n{1}\n{2}'.format(setX,setY,setZ))


# In[ ]:


# Working with lists


# In[12]:


listA = [0,1,2,3]
listB = [4,5,6,7]
listA.extend(listB)
listA


# In[13]:


listA.append(-999)
listA


# In[14]:


listA.remove(-999)
listA


# In[15]:


listX = listA + listB
listX


# In[ ]:


# Tuples


# In[18]:


MyTuple = (1,2,3,(4,5,6,(7,8,9)))


# In[19]:


MyTuple


# In[24]:


for Value1 in MyTuple:
    if type(Value1)==int:
        print(Value1)
    else:
        for Value2 in Value1:
            if type(Value2) == int:
                print("\t", Value2)
            else:
                for Value3 in Value2:
                    print("\t\t", Value3)


# In[29]:


MyNeTuple = (MyTuple+(10,11,12,(13,14,15)))


# In[30]:


for Value1 in MyNeTuple:
    if type(Value1)==int:
        print(Value1)
    else:
        for Value2 in Value1:
            if type(Value2) == int:
                print("\t", Value2)
            else:
                for Value3 in Value2:
                    print("\t\t", Value3)


# In[ ]:


# Defining iterators


# In[31]:


listA = ['Orange', 'Yellow', 'Green', 'Brown']
listB = [1,2,3,4]
listA[1]


# In[32]:


listB[1:3]


# In[34]:


for value in listB[1:3]:
    print(value)


# In[79]:


for value1, value2 in zip(listA,listB):
    print(value1, '\t', value2)


# In[ ]:


# Dictionary - indexing data


# In[39]:


MyDictionary = {'Orange':1, 'Blue':2, 'Pink':3}
MyDictionary['Pink']


# In[40]:


MyDictionary.keys()


# In[ ]:


################
#Chapter5
################


# In[ ]:


#Uploading small amount of data


# In[92]:


with open("C:\\Users\\amare\\Documents\\U Texas Austin Data Science\\Course 51\\colours.txt", 'r') as open_file:
        print('Colours.txt content:') 
        print (open_file.read())


# In[93]:


with open("C:\\Users\\amare\\Documents\\U Texas Austin Data Science\\Course 51\\colours.txt", 'r') as open_file:
    for observation in open_file:
        print('Reading Data: '+ observation)


# In[76]:


n = 2
with open("C:\\Users\\amare\\Documents\\U Texas Austin Data Science\\Course 51\\colours.txt", 'r') as open_file:
    for j, observation in enumerate(open_file):
        if j % n ==0:
            print('Reading Line: '+ str(j) + ' Content: ' + observation)
           


# In[70]:


# random sampling
from random import random
sample_size = 0.25
with open("C:\\Users\\amare\\Documents\\U Texas Austin Data Science\\Course 51\\colours.txt", 'r') as open_file:
    for j, observation in enumerate(open_file):
        if random()<=sample_size:
            print('Reading Line: '+ str(j) + ' Content: ' + observation)


# In[91]:


#Reading from text file - pandas
import pandas as pd
colour_table = pd.io.parsers.read_table("C:\\Users\\amare\\Documents\\U Texas Austin Data Science\\Course 51\\colours.txt")
#colour_table.fillna(value=' ')
print(colour_table)


# In[ ]:


# Reading a CSV delimited format


# In[97]:


import pandas as pd
titanic = pd.io.parsers.read_csv("C:\\Users\\amare\\Documents\\U Texas Austin Data Science\\Course 51\\titanic.csv")
x = titanic[['Age']]
print(x)


# In[ ]:


#Reading excel


# In[2]:


import pandas as pd
xls = pd.ExcelFile("C:\\Users\\amare\\Documents\\U Texas Austin Data Science\\Course 51\\Survey.xlsx")
trig_values = xls.parse('Survey', index_col=None,na_values=['NA'])
print(trig_values)


# In[ ]:


# Sending data in unstructured file form


# In[2]:


import scipy
from skimage.io import imread
from skimage.transform import resize
from matplotlib import pyplot as plt
import matplotlib.cm as cm
example_file = ("C:\\Users\\amare\\Documents\\U Texas Austin Data Science\\Course 51\\Dog_face.png")
image = imread(example_file, as_grey=True)
plt.imshow(image, cmap=cm.gray)
plt.show()


# In[3]:


print("data type: %s, shape: %s" % (type(image), image.shape))


# In[4]:


# crop the image
image2 = image[5:70,0:70]
plt.imshow(image2, cmap=cm.gray)
plt.show()


# In[16]:


#Resize
image3=resize(image2,(30,30),mode='symmetric')
plt.imshow(image3, cmap=cm.gray)
print("data type: %s, shape:%s" % (type(image3), image3.shape))


# In[ ]:


#Erros
# Multiple errors occurred - syntax error, packages not installed, nulls in data
# NaN in print output - How to get rid of nulls in sublime? Select all contents. View -> indentation -> indent using spaces
# Error while reading excel files - xlrd was not installed - pip install xlrd
# images - matplotlib not installed - pip install matplotlib
# Errors in syntax - google search. Some code did not work as given in the book. changes for python 3.6.
# file path needs two back slashes ! "C:\\Users\\amare\\...". Solution found using google search of error message.
#
#
#•Was it straightforward to install Python and all of the libraries?
# It was not overly complicated to install Python and all the libraries, but it is not simple and straightforward either. 
#•Was the tutorial useful? Would you recommend it to others?
# This tutorial was certainly useful and I recommend it. 
# Writing all the code and executing it is the only way to get familiar with the programming language, complex environment 
# and tools such as Jupyter Notebook. 
#•What are the main lessons you've learned from this experience?
# The main lesson is Python is powerful and useful languuage for data science.
# Python syntax, environment and tools certainly have a learning curve.

