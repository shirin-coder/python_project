
# using for loop
x= [2,3,4,5,6,7,8,9]
def make_even(num):
    if num%2==1:
        return num+1
    else:
        return num
y = []
for num in x:
    y.append(make_even(num))
    
print(y)

# without using for loop
y = list(map(make_even,x))
print(y)
