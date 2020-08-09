#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1=[]

list2=[]

list3=[]

n=int(input("the number of elements you would like to enter in list 1 "))



for i in range(0 , n):
    j=i+1
    elem=int(input("enter the element number {} : ".format(j)))
    list1.append(elem)
    

print("input: list1=",list1)

print("output:")

for i in range(0 , n):

    if (list1[i] >= 0):

        print(list1[i])



m=int(input("the number of elements you would like to enter in list 2 "))



for i in range(0 , m):
    j=i+1
    elem=int(input("enter the element number {} : ".format(j)))
    list2.append(elem)

    

print("input:list2=",list2)

    

for i in range(0 , m):

    if (list2[i] >= 0):

        list3.append(list2[i])

        

print("output:",list3)  
list1.clear()
list2.clear()
list3.clear()


# In[ ]:





# In[ ]:




