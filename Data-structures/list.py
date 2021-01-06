mylist = ['C','C++','Python']

print(mylist) # print whole list

print(mylist[0]) #print 'C'

print(len(mylist)) #to calculate length

mylist.append('Java') #add new element at last
print(mylist)

mylist.insert(1,"HTML") # add new element at index 1
print(mylist)

mylist.remove('C++') # to remove element
print(mylist)

mylist.sort() # to sort elements in inc/asc order
print(mylist)

mylist.sort(reverse=True) # to sort elements in dec/des order
print(mylist)

