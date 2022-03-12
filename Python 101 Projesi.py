# Task 1
a = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
## output: [1,'a','cat',2,3,'dog',4,5]
k = []
def listeKirici(a):
    for i in a: 
        if type(i) != list:
            k.append(i)
        else:
            listeKirici(i)
    return  
listeKirici(a)
print(k)

# Task 2
b = [[1, 2], [3, 4], [5, 6, 7]]
## output: [[[7, 6, 5], [4, 3], [2, 1]]
x = 0
d = []
b = b[::-1]
while x < len(b):
    c = b[x]
    c = c[::-1]
    d.append(c)
    x = x + 1

print(d)




