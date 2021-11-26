#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
sys.version


# In[2]:


a = 7.9
a


# In[3]:


# What is other inbuild datatype available except 14 datatypes-

a = 10
#print('a')       # To find the variable 
#print(a)         # To find the value of variable
type(a) # To find the data type
id(a)            # To find an address of an object


# In[4]:



a = 4809
a


# In[5]:


#2.Binary form(Base 2)
#a = 1111   # value is declared
b = 0b1111 # Now pvm convert value to binary value
b
#a


# In[6]:


#3. Octal form(Base 8)
#a = 111 # Value is declared
b = 0o111 # Now pvm covert value to octal value
b
#a


# In[7]:


# final summary of INTEGRAL DATATYPES 
a = 10
b = 0b10
c = 0o10
c


# In[8]:


A = 78
A


# In[9]:


# float datatypes - 
#b = 4567.89
#print(type(b))
#type(b)

d = 0o4567.89 # This is octal
#e = 0b4567.89 # This is binary
#
d
#e
#b


# In[10]:


b = 67.9
b


# In[11]:


f = 1.2E5 # only 'e' letter is allowed
#g = 2.4a3 # except 'E' you can't execute any programme
#g
f


# In[12]:


e = 5.e4
e


# In[13]:


x = 30+40j #assigned int value in real part & imaginary part
type(x) 


# In[14]:


y = 20.5+2.3j #assigned float value in real part & imaginary part
z = 30.8+20j  #assigned float value in real part & real value in imaginary part
y + z
y*z
y/z


# In[15]:


c = 15+0o111j # Imaginary part cannot be binary,octal
#d = 0b111+15j # Real part can be binary,octal
c


# In[16]:


a1 = 20+30j
b1 = 40+50j
a1+b1
a1-b1
a1*b1
a1/b1


# In[17]:


a = 2+3j
type(a) 


# In[18]:


a = 10
b = 20
c = a<b
c


# In[19]:


True+True
True*True
True-True
True/True
False+False
False+True


# In[20]:


careerera = '''good for datascience'''
#type(careerera)#' single quotes'
careerera


# In[21]:


careerera1 = '''good for 
 datascience'''

careerera1


# In[22]:


a = '''hallo
how 
are 
you'''

a
#type(a) # SINLE & DOUBLE QUOTES ARE EQUAL 


# In[23]:


b = '''hello 
    hi'''


# In[24]:


b = '''('hallo' 
  'how'
    'are you')'''
    
    # ''' ''' ==> triple quotes are used for multiline comments
b
    # is for commenting


# In[25]:


x = 'careera'
y = "god"
print(type(x))
print(type(y))
z = '''  hi welcome to 
        datascience 
    academy'''
s = '''datascience" academy'''
z
print(type(z)) 


# In[26]:


x


# In[27]:


# int(): - you can convert from other type to int type except complex 

int(10.123)  # float to int
#int(10+20j) # cannot convert from complex to int
int(True)     # Bool to int
int(False)   # Boll to int
int('10')    # string to int


# In[28]:


# float(): -- convert from any type to float except complex

float(10)      # int to float
#float(10+20j)  # cannot convert complex to float
float(False)     # boolean to float
float('11')    # string to float


# In[29]:


# complex(): -- covert any other type to complex type
# --- this only for 1 argument ------

complex(10)    # int to complex
complex(10,20) # int to complex
complex(10.5)  # float to complex
complex(True)  # Bool to complex
complex(False) # Bool to complex
complex('10')  # string to complex 

# ----- Now we will check for 2 arguments ------
#complex(10,20)   # int to complex
complex(10,20.5) # float to complex
#complex('10')    # string to complex, you cannot assign 2 argument


# In[30]:


# Bool()  - (0 means false // 1 means non zero)

bool(0)      # int to bool
bool(10)     # int to bool
bool(0.0)    # float to bool
bool(0.01)   # float to bool 
bool(10+20j) # complext to bool
bool(0+0j)   # complex to bool
bool("")      # string to bool(if argument is empty string then false)
bool('abc')# string to bool(if argument is not empty string then true)
bool(' ')    # space is also treated as character so non empty string


# In[31]:


# str(): --- any type is possible in string 

str(10)     # int to string
str(10.50)  # float to string
str(True)   # bool to string
str(10+20j) # complex to string


# In[32]:


x2 = 10
y2 = 10
z2 = 10 
print(id(x2))
print(id(y2))
print(id(z2))


# In[33]:


print(x2 is z2)
print(x2 is y2)
print(y2 is z2)


# In[34]:


x = 10 
y = 10
print(id(x))
print(id(y))


# In[35]:


id(y)


# In[36]:


# is operator
x = 20 # x,y = 20
y = 20
#x is y
y is x


# In[37]:


x = True
y = True
z = True
x is y
y is z
z is x
z is y


# In[38]:


x = 10.0   # Reusable concept is not there in float data type 
y = 10.0
x is y


# In[39]:


x = 10 +20j # complex and floating number this concept is not applicable
y = 10 +20j
x is y


# In[40]:


l = [] 
type(l) 
print(type(l))


# In[41]:


l


# In[42]:


#Now i want to add an object

l.append(10) 
l.append(20)
l.append(30)
l.append(10)


# In[43]:


l


# In[44]:


print(l)


# In[45]:


print(l) #  if you check the output insertation order is preserved & duplication are allowed


# In[46]:


#hetrogenrous objects are allowed or not
#java people came and asking null is availabe or not, such type of stories are not available
# list objects are growable & this is just an introduction session & we will see indetails

l.append('amxwam') 
l.append('8.0')
l.append(None)
l


# In[47]:


l.remove('amxwam') #delete the object from list


# In[48]:


l


# In[49]:


l[4]  # n-1 


# In[50]:


l[3]  


# In[51]:


l


# In[53]:


l[-1] 


# In[54]:


l[-2]


# In[55]:


l[:] 


# In[56]:


l[2:7] # n-1 formula


# In[57]:


l[2:6] 


# In[58]:


l[2:5] 


# In[59]:


l


# In[60]:


l[2:4] 


# In[61]:


l


# In[62]:


l[0] 


# In[63]:


l[0] = 1000


# In[64]:


l


# In[65]:


l # list is mutable 


# In[66]:


l[:4] 


# In[67]:


l


# In[68]:


l[0] = 20
l[0]


# In[69]:


l


# In[70]:


l # list is mutable & allow duplicate


# In[71]:


l[2:-2]


# In[72]:


l[:]  


# In[73]:


l


# In[74]:


l[1] # : --> (SLICING OPERATOR) 


# In[75]:


l[:] #display all the value from  2nd index onwards


# In[76]:


l[-1] # output is none hear


# In[77]:


l[-2] 


# In[78]:


l


# In[79]:


l[:] # : --> this will give us total values which we passed in the object


# In[80]:


l[::-1] # reverse order


# In[81]:


l


# In[82]:


l[-2:2]  # n-1 ( 4th ) 


# In[83]:


l.remove(None) 


# In[84]:


l


# In[85]:


l[-1]


# In[86]:


l[-3]


# In[87]:


l


# In[88]:


l[2] 


# In[89]:


l[:-1]  


# In[90]:


l = [10,20,30,40] #list datastructure
t = (10,20,30,40) #tuple datastructure


# In[91]:


l[:] 


# In[92]:


t1 = (10,'amxwam',True, 5.8, 10)
t1


# In[93]:


t1[0] 


# In[94]:


t1[0] = 20 # tuple is immutable


# In[95]:


t1[0] = 20 # tuple immutable ( not changable) e.g - kyc / adhar 


# In[96]:


t1


# In[97]:


t1[0:3]  # [[ IF YOU RIGHT SIDE THE CALCULATION WILL (Nth INDEX-1) (3-1) == UPTO 2ND INDEX ]]


# In[98]:


t1[0:4] 


# In[99]:


t1


# In[100]:


t


# In[101]:


t[0] # Oth index 


# In[102]:


l #difference between list and tuple


# In[103]:


l[0] 


# In[104]:


l[0] = 30 #mutable (change)


# In[105]:


l


# In[106]:


l[:4]


# In[107]:


l[:-2] 


# In[108]:


t


# In[109]:


t[0]


# In[110]:


t[0]= 20 
# cannot change any value once you decleare cuz tuple is immutable 


# In[111]:


t1


# In[112]:


t


# In[113]:


t.remove(30)


# In[114]:


t


# In[115]:


t = t*3
t


# In[116]:


t[0] = 20


# In[117]:


t1


# In[118]:


t2 = t1 * 3 #in this case content has not changed but same t content repeted twice


# In[119]:


t2


# In[120]:


t3 = (10,20,[2,6])   #is this valid one & u can declare list inside the tuple


# In[121]:


t3


# In[122]:


colors = "red", "green", "blue"
colors
rev = colors[::-1]
rev


# In[123]:


rev = colors[::-1] # reversing order is allowed
rev


# In[124]:


# FORM-1: range(10) -- represents values from 0 to 9 (python index start from 0)

r = range(20) 
(type(r)) 
r


# In[125]:


range(10.0, 11.5) # you cannot declare float argument


# In[126]:


r


# In[127]:


# if i need value for 10 values 

for i in r: print(i) 


# In[128]:


r[4] 


# In[129]:


r[0] 


# In[130]:


r[4]


# In[131]:


r[0:3] 


# In[132]:


# i want to generate a sequence of no from 0 to 99

range(100) 


# In[133]:


# i want to represent number from 10 to 29 then we should not use above one

range(10,30) # repreent no. from 10 to 29 but not 100 & we passed 2 arguments


# In[134]:


range(50) 


# In[135]:


range(10,50) # 5 state from 10 to 50 print the output with 5 steps


# In[136]:


range(10,50,5) # 5 state from 10 to 50 print the output with 5 steps


# In[137]:


range(10,50,5,6) 


# In[138]:


range(10,50,5) 


# In[139]:


for i in range(10,60,30):  
    print(i)


# In[140]:


range(10,20,5,6) #you cannot declare 4 aruguments once becusae max you can assign for 3 arguments or 3 parameter


# In[141]:


a = b = c = d = 4
print(id(a))
print(id(b))
print(id(c))
print(id(d))


# In[142]:


print(id(a) is id(b)) 


# In[143]:


c is d


# In[ ]:




