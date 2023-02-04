# function to take a list and return a new one 
# question 4
def uniqueList(lst):
    res = []
    for item in lst:
        if item not in res:
            res.append(item)
    return(res)
    
print("Unique List: ", uniqueList([1,2,3,3,3,3,4,5]))
