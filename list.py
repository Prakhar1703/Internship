#basic list functions
a=[1,2,3,4,5,6,10,9,20,14]
for i in range(len(a)):
    print(a[i],end="")
b=[]
for i in a:
    b.append(i)
    a.pop(3)
    print(i)
b.extend(a)
a.sort()
print(a)
# repetition of list  
c = [12, 14, 16, 18, 20]  
# repetition operator *  
d = c * 2  
print(b)  
#concatenation
e = [12,13,26,88,20]  
f = [9, 10, 45, 67, 86]  
# concatenation operator +  
l = e + f 
print(l)  