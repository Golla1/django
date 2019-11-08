# input list 
l = [1, 2, [3, 4, (5, 6)], 7, 8, [9, [10]]] 
  
# output list 
output = [] 
  
# function used for removing nested  
# lists in python.  
def reemovNestings(l): 
    for i in l: 
        if type(i) == list: 
            reemovNestings(i) 
        elif type(i) == tuple:
            reemovNestings(i) 
        else:     
            output.append(i) 
count = 0            
def list_count(l):
    count=0 
    for i in l: 
        if type(i) == list: 
            for num in list[i]:
                count += 1 
        elif type(i) == tuple:
        	for num in tuple:
        		count += 1
        else:     
            count += 1
    return count   
# Driver code 
print ('The original list: ', l) 
reemovNestings(l) 
print ('The list after removing nesting: ', output) 

count=list_count(l) 
print ('The list count is: ', count) 