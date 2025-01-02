# a = 5
# if(a>7):
#     print('correct ')
# else:
#     print('not')

# num = 3
# while num<=10:
#     print(num)
#     num = num+1

# num = 0
# while num<=10:
#     num = num+1
#     if num%2 == 1:
#         continue
#     print(num)
numbers = [5,10,15,20,25,30]
sum = 0
for num in numbers:
    print(num)
    sum = sum + num
    if sum> 25:
        print("gotcha!!")
print(sum)