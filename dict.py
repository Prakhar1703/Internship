A = {"Name": "Ram", "Age": 25} 
for x in A.items():        
    print(x)      
print(A["Name"])
#Initialising new dictionary
Dict={}
#adding elements one at a time
Dict[0] = 'Peter'      
Dict[2] = 'Joseph'      
Dict[3] = 'Ricky'  
#length of dictionary
print(len(Dict))
#adding set of values
Dict['Emp_ages'] = 20, 33, 24 
print(Dict)
#deleting element using pop()
Dict.pop(3)
print(Dict)