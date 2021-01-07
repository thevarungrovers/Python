myDic = {
    "C" : "Easy",
    "C++" : "Easiest",
    "Java" : "difficult"
}

print(myDic) # print whole

print(len(myDic)) # calculate length

#print paticular value 
print(myDic['Java'])
print(myDic.get('Java'))

# add new element
myDic["Python"] = "Cool and Easy"
print(myDic)

# to remove
del myDic["C"]
print(myDic)

# to edit value
myDic["C++"] = "Beginners"
print(myDic)

# to delete the value of keyword
myDic.pop('Java')
print(myDic)

# to clear the dictionary
myDic.clear()
print(myDic)

# to delete dictionary
del myDic