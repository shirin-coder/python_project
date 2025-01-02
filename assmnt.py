# def result_string():
#     a = input().strip()

#     tmp = ""
#     bal = 0
#     cnt = 0 
#     ans = []
#     for char in a:
#         tmp+=char
#         if char == 'L':
#             bal +=1
#         elif char == 'R':
#             bal -=1

#         if bal == 0:
#             cnt+=1
#             ans.append(tmp)
#             tmp=""

#     print(cnt)
#     for b in ans:
#         print(b)


# result_string()
# n = int(input())
# a = list(map(int,input().split()))
# freq = {}
# for num in a:
#     if num not in freq:
#         freq[num]= 0
#     freq[num]+=1

# sum_removals = 0
# for num in freq:
#     if freq[num] < num:
#         sum_removals += freq[num]  
#     else:
#         sum_removals += freq[num] - num  

# print(sum_removals)


# def display(*args):
#     for x in args:
#         print(x,end=" ")
    
# display("shirin","sharmin","raj")


# def displayName(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")


# displayName(Name = "shirin", hobby = "coding", country = "bangladesh", age = 19)



n =  int(input())
n1 = list(map(int,input().split()))

cnt = 0
while True:
    check_even = True
    for x in n1:
        if x%2!=0:
            check_even = False
            break

    if not check_even:
        break

    
    for i in range(n):
        n1[i]//=2
        
    cnt +=1

print(cnt)