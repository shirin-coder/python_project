# numbers = [2,3,4,5,6,7]
# for i in numbers:
#     print(i)

# num1 = int(input("enter first number "))
# num2 = int(input("enter second number "))
# num3 = int(input("enter third number "))

# if num1>=num2 and num1 >= num3:
#     largest = num1
# elif num2>=num1 and num2>=num3:
#     largest=num2
# else:
#     largest = num3
# print("largest : ",largest)

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# sum = num1+num2+num3
# print(sum)

# num = 39
# while num<=68:
#     if num%2==1:
#         print(num)
#     num=num+1

# num = [2, 22, 3, 10, 5, 12, 25]
# x = 3
# i = 0

# while i < len(num):
#     if num[i] == x:
#         print("Found at index", i)
#         break  # Exit the loop after finding x
#     i += 1


def all_sum(num1,num2,*numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        print(num)
        sum = sum + num
    return sum 
total = all_sum(22,33,44,55,66)
print('all sum ',total)
