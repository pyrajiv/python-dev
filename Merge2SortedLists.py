'''
Created on Dec 23, 2021

Merge two sorted lists

@author: Rajiv
'''

def merge_lists(lst1, lst2):
    # Write your code here
    lst = []
    i = 0
    j = 0
    len1 = len(lst1)
    len2 = len(lst2)
    k = max(len1,len2)
    for index in range(k):
        while (i < len1) & (j < len2):
            if lst1[i]<lst2[j]:
                lst.append(lst1[i])
                i = i + 1
            else:
                lst.append(lst2[j])
                j = j + 1
        
        if i < len1:
            while i < len1:
                lst.append(lst1[i])
                i = i + 1 
        if j < len2:
            while j < len2:
                lst.append(lst2[j])
                j = j + 1 

    return lst


print(merge_lists([1, 3, 4, 5],[2, 6, 7, 8]))

