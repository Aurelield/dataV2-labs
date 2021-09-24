#!/usr/bin/env python
# coding: utf-8

# In[8]:


def division(lst):
    l_len = len(lst)
    if l_len == 0:
        raise ValueError
    elif l_len == 1:
        return lst
    elif l_len == 2:
        if lst[0] <= lst[1]:
            return lst
        elif lst[0] > lst[1]:
            lst[0], lst[1] = lst[1], lst[0]
            return lst
    else:
        l_left = lst[:l_len//2]
        l_right = lst[l_len//2:]
        return division(l_left), division(l_right)

    def compare(lst):
        final_lst = []
        if division(l_left[0]) < division(l_right[0]):
            final_lst.append(l_left[0])
        elif division(l_left[0]) > division(l_right[0]):
            final_lst.append(l_right[0])
        else:
            final_lst.append(l_left[0], l_right[0])
            return compare(l_left,l_right)
        

lst = [11, 222, 3, 899, 24, 5, 46, 67]
lst_trie = division(lst)
print(lst_trie)


# In[ ]:





# In[27]:


# fonction de division 
def division(lst):
    l_len = len(lst)
    if l_len == 0:
        raise ValueError
    elif l_len == 1:
        return lst
    elif l_len == 2:
        if lst[0] <= lst[1]:
            return lst
        elif lst[0] > lst[1]:
            lst[0], lst[1] = lst[1], lst[0]
            return lst
    else:
        l_left = lst[:l_len//2]
        l_right = lst[l_len//2:]
        return division(l_left), division(l_right)      




# In[30]:


def division(lst):
    l_len = len(lst)
    if l_len == 0:
        raise ValueError
    elif l_len == 1:
        return lst
    elif l_len == 2:
        if lst[0] <= lst[1]:
            return lst
        elif lst[0] > lst[1]:
            lst[0], lst[1] = lst[1], lst[0]
            return lst
    else:
        l_left = lst[:l_len//2]
        l_right = lst[l_len//2:]
        return division(l_left), division(l_right)

def fusion(l_left,l_right):
#eles qui vont être incrémentés dans chaque sous-liste
    index_l_left = 0
    index_l_right= 0  
    l_left2 = len(l_left)
    l_right2 = len(l_right)
    list_fusion = []
    while index_l_left<l_left2 and index_l_right<l_right2:
        if l_left[index_l_left] < l_right[index_l_right]:
            list_fusion.append(l_left[index_l_left])
            index_l_left += 1
        else:
            list_fusion.append(l_right[index_l_right])
            index_l_right += 1
   
    if l_left:
        list_fusion.extend(l_left2[index_l_left:])
    if l_right:
        list_fusion.extend(l_right2[index_l_right:])
    return list_fusion


lst = [11, 222, 3, 899, 24, 5, 46, 67]
print(division(lst))


# In[1]:




    def compare(lst):
        final_lst = []
        if division(l_left[0]) < division(l_right[0]):
            final_lst.append(l_left[0])
        elif division(l_left[0]) > division(l_right[0]):
            final_lst.append(l_right[0])
        else:
            final_lst.append(l_left[0], l_right[0])
            return compare(l_left,l_right)
        

lst = [11, 222, 3, 899, 24, 5, 46, 67]
lst_trie = division(lst)
print(lst_trie)


# In[40]:


def division(lst):
    l_len = len(lst)
    if l_len == 0:
        raise ValueError
    elif l_len == 1:
        return lst
    elif l_len == 2:
        if lst[0] <= lst[1]:
            return lst
        elif lst[0] > lst[1]:
            lst[0], lst[1] = lst[1], lst[0]
            return lst
    else:
        l_left = lst[:l_len//2]
        l_right = lst[l_len//2:]
        return division(l_left),division(l_right)
    
#penser la recursivité
#penser à la fusion 
   

    



# In[ ]:




