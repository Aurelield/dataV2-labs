#!/usr/bin/env python
# coding: utf-8

# In[39]:


#count specific digits from a given list of integers
# if i in 
class List:
    def __init__(self):
        pass
    def countSpecDigits_(self, integers_lists, digits_list):
        return [(d, sum(str(i).count(str(d)) for i in integers_lists)) for d in digits_list]
#(d, sum(str(i).count(str(d)) for i in integers_lists))
#str for indexing each value in digits_list to l

       


# In[40]:


l = List()
integers_lists = [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
digits_list = [1, 3]
l.countSpecDigits_(integers_lists, digits_list) == [(1, 3), (3, 2)]


# In[41]:


integers_list = [-18, -31, 81, -19, 111, -888]
digits_list = [1, 8, 4]
l.countSpecDigits_(integers_list, digits_list) == [(1, 7), (8, 5), (4, 0)]


# In[42]:


integers_list = [-77, -65, 56, -79, 6666, 222]
digits_list = [1, 8, 4]
l.countSpecDigits_(integers_list, digits_list) == [(1, 0), (8, 0), (4, 0)]


# In[ ]:


class List:
    def __init__(self):
        pass
    def countSpecDigits_(self, integers_lists, digits_list):
        return [(d, sum(str(i).count(str(d)) for i in integers_lists)) for d in digits_list]
#result=()    
#for d in range(len(digits_list)):
#digits_list[d] = str(digits_list[d])
#for d in range(len(integers_list)):
#integers_list[a] = str(integers_list[d])
#for d in digits_list:
#count = 0
#for i in integers_list:
#count += i.count(d)
#result.append((int(d),count))
#return result

