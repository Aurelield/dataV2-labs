#!/usr/bin/env python
# coding: utf-8

# In[52]:


#Define a method/function that removes from a given array of integers all the values contained in a second array.


# In[44]:


class List:
    def __init__(self):
        pass 
#"pass", parce que il n'y pas d'attributs
    def remove_(self, l1, l2):
#def method_(self, lx, ly)
        return [i for i in l1 if i not in l2]


# In[48]:


l= List()
integer_list =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
values_list = [1, 3]
l.remove_(integer_list, values_list) == [2, 2, 4]


# In[50]:


integer_list = [1, 1, 2 ,3 ,1 ,2 ,3 ,4, 4, 3 ,5, 6, 7, 2, 8]
lst = [1, 3, 4, 2]
l.remove_(integer_list, lst) == [5, 6 ,7 ,8]


# In[51]:


integer_list = [8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2 , 3]
lst = [2, 4, 3]
l.remove_(integer_list, lst) == [8, 7, 6, 5, 1]

