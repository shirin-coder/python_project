
# N = input().strip()
# reversed_N = N[::-1]
# reversed_int = int(reversed_N)
# print(reversed_int)
# if N == reversed_N:
#     print("YES")
# else:
#     print("NO")

# Read input as strings and convert them to integers
# Read input as a single line, split, and convert to integers
# a, b = input().split()
# a = int(a)
# b = int(b)

# found = False

# # Iterate from a to b
# for i in range(a, b + 1):
#     num = i
#     isLucky = True

#     # Check each digit of the number
#     while num > 0:
#         digit = num % 10
#         if digit != 4 and digit != 7:
#             isLucky = False
#             break  # No need to check further if a non-lucky digit is found
#         num //= 10  # Remove the last digit

#     # If the number is lucky, print it
#     if isLucky:
#         print(i, end=" ")
#         found = True

# # If no lucky number was found, print -1
# if not found:
#     print(-1)

# n = int(input())
# a = []
# for i in range(n):
#     num = int(input())
#     a.append(num)

# min_index = a.index(min(a))
# max_index = a.index(max(a))
# a[min_index], a[max_index] = a[max_index],a[min_index]
# for num in a:
#     print(num,end=" ")
    

# Input: A, B and S
A, B = map(int, input().split())  # Read A and B
S = input().strip()  # Read the string S

# Check if the length of S is A + B + 1
if len(S) != A + B + 1:
    print("No")
else:
    # Check if the character at position A is '-'
    if S[A] != '-':
        print("No")
    else:
        # Check if all other characters are digits
        for i in range(len(S)):
            if i != A and not S[i].isdigit():
                print("No")
                break
        else:
            print("Yes")






