# matrix=[[5,6,7,8],
# [13,14,15,16],
# [1,2,3,4],
# [9,10,11,12]]
# n=4
# for i in range(n):
#         matrix[i][i],matrix[i][n-1-i]=matrix[i][n-1-i],matrix[i][i]
# for row in matrix:
#     print(*row)


# matrix=[[5,6,7,8],
# [13,14,15,16],
# ]
# n=2 
# m=4
# result=[[0]*n for _ in range(m)]
# print(result)
# for i in range(n):
#     for j in range(m):
#         result[j][i]=matrix[i][j]
# print(*result)
    
# nums=[1,2,3,1]
# dup=set()
# for num in nums:
#     if num in dup:
#         print(True)
#     else:
#         dup.add(num)
# print(False)

# strs=["eat","tea","tan","ate","nat","bat"]
# patterns={}
# for word in strs:
#     freq=[0]*26
#     for ch in word:
#         freq[ord(ch)-ord("a")]+=1
#     tup=tuple(freq)
#     # print(tup)
#     if tup not in patterns:
#         patterns[tup]=[]
#     patterns[tup].append(word)
#     print(list(patterns.values()))

# nums=[1,1,1,2,2,3]
# k=2
# freq={}
# ans=[]
# for n in nums:
#     freq[n]=freq.get(n,0)+1
# sorted_items=sorted(freq.items(),key=lambda x:x[1],reverse=True)
# print(sorted_items)
# for num,count in sorted_items[:k]:
#     ans.append(num)
# print(ans)

# strs=["eat","tea","tan","ate","nat","bat"]
# visited=[False]*len(strs)
# ans=[]
# for i in range(len(strs)):
#     if visited[i]:
#         continue
#     group=[strs[i]]
#     visited[i]=True
#     for j in range(i+1,len(strs)):
#         if not visited[j]:
#             if sorted(strs[i])==sorted(strs[j]):
#                 group.append(strs[j])
#                 visited[j]=True
#     ans.append(group)

# print(ans)
# groups={}
# for word in strs:
#     freq=[0]*26
#     for ch in word:
#         freq[ord(ch)-ord("a")]+=1
#     key=tuple(freq)
#     if key not in groups:
#         groups[key]=[]
#     groups[key].append(word)
#     print(groups)
# print(list(groups.values()))

# s=["hi","ramsha"]
# encode=[]
# en_st=""
# for word in s:
#         encode.append(str(len(word))+"#"+word)
# for word in encode:
#         en_st+=word  #"2#hi6#ramsha"
# print(en_st)
# decode=[]
# count=""
# i=0
# while  en_st[i].isdigit():
#         count+=en_st[i]

# print(count)
                
        
            
                
# from datetime import datetime
# st="01:00:00"
# et="01:00:25"

# s=datetime.strptime(st,"%H:%M:%S")
# e=datetime.strptime(et,"%H:%M:%S")
# diff=e-s
# print(int(diff.total_seconds()))


        
# nums=[1,2,3,4]
# k=4
# cost=0
# available=k
# op_count=1
# for i in range(len(nums)):
#         while available<nums[i]:
#             available+=k
#             cost+=op_count
#             op_count+=1
#         available-=nums[i]
# print(cost)

# n=4
# count=0
# res=""
# while n>0:
#         res+=str(n%2)
#         n//=2
# res=res[::-1]
# print(res)
# res=res[::-1]
# for i in res:
#        if i==1:
#             count+=1
# print(count)

# n=16
# x=1
# while x<n:
#     x*=2
#     if x==n:
#         print(True)
#         break
#     elif x>n:
#         print(False)
# n=8  
# arr=[1,2,7,9,5,6,3,8]
# xor=0
# for i in range(1,n+2):
#         xor=xor^i
# arr_xor=0
# for i in arr:
#         arr_xor=arr_xor^i
# missing=xor^arr_xor
# print(missing)

# x=4
# y=3
# res=[]
# for _ in range(x):
#     res.append("1")
# for _ in range(y):
#     res.append("0")
# res="".join(res)
# print(int(res,2))

# bn=0
# for _ in range(x):
#     bn<<=1
#     bn+=1
# for _ in range(y):
#     bn<<=1
#     bn+=0
# print(bn)

# n=5
# res=[]
# for i in range(n+1):
#     count=0
#     if i==0:
#         res.append(0)
#     else:
#         while i>0:
#             i=i&(i-1)
#             count+=1
#         res.append(count)
# print(res)

# n=15
# d=""
# while n>0:
#     d+=str(n&1)
#     n>>=1
# print(d)

# k=60
# a=[1,20,40,100,80]
# a.sort()
# i=0
# j=len(a)-1
# if i==j:
#     print(False)
# else:
#        while i<j:
#                 if abs(a[i]-a[j])==k:
#                     print(True)
#                     break
#                 elif abs(a[i]-a[j])>k:
#                     i+=1
#                 else:
#                     j-=1
#        else:
#             print(False)

# a=[4,7,2]
# ans=0
# for start in range(len(a)):
#     for end in range(start,len(a)):
#         total=0
#         for k in range(start,end+1):
#          total+=a[k]
#         ans+=total
# print(ans)

# arr=[2,1,5,1,3,2]
# k=3
# n=len(arr)


# total=0

# for x in range(k):
#         total+=arr[x]
# maxi=total
# i=0
# j=k
# while j<n:
#     total=total-arr[i]+arr[j]
#     maxi=max(total,maxi)
#     i+=1
#     j+=1
# print(maxi)

# a=[-2,-4,-2,4,-2]
# n=len(a)
# k=3
# freq={}
# for num in range(k):
#     freq[a[num]]=freq.get(a[num],0)+1
# distinct=len(freq)
# print(distinct,end=" ")
# i=0
# j=k
# while j<n:
#     freq[a[i]]-=1
#     if freq[a[i]]==0:
#         del freq[a[i]]
#     freq[a[j]]=freq.get(a[j],0)+1
    
#     distinct=len(freq)
#     i+=1
#     j+=1
#     print(distinct,end=" ")


# Enter your code here. Read input from STDIN. Print output to STDOUT
# t=int(input())
# for _ in range(t):
#     s=input()
#     seen={}
#     for ch in s:
#         seen[ch]=seen.get(ch,0)+1
#     for k in seen:
#         if seen[k]>1:
#             print(ch)
#             break
#     else:
#         print(".")
           

# t=int(input())
# stack=[]
# def push(x):
#     stack.append(x)
# def pop():
#     if len(stack)==0:
#         return "Empty"
#     return stack.pop()

# for _ in range(t):
#     op=input().split()

#     if op[0]=="push":
#         x=int(op[1])
#         push(x)
#     else:
#         print(pop())

# nums=[1,2,3,4,5]
# n=len(nums)
# i=0
# j=2
# prefix=[0]*n
# prefix[0]=nums[0]
# for i in range(1,n):
#     prefix[i]=prefix[i-1]+nums[i]
# print(prefix)

# if i==0:
#     ans=prefix[j]
# else:
#     ans=prefix[j]-prefix[i-1]
# print(ans)

# nums=[1,7,3,6,5,6]
# pivot=-1
# left_sum=0
# right_sum=0
# for i in range(len(nums)):
#     left_sum=sum(nums[:i])
#     right_sum=sum(nums[i+1:])

#     if left_sum==right_sum:
#         pivot=i
        # break

# print(pivot)

# class Node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
# drinks=Node("drinks")
# hot=Node("hot")
# cold=Node("cold")
# tea=Node("tea")
# coffee=Node("coffee")
# cola=Node("cola")
# fanta=Node("fanta")
# hot.left=tea
# hot.right=coffee
# cold.left=cola
# cold.right=fanta
# drinks.left=hot
# drinks.right=cold

# print(drinks.left.val)
# print(drinks.right.val)
# print(drinks.left.left.val)
# print(drinks.left.right.val)
# print(drinks.right.right.val)
# print(drinks.right.left.val)
# def height(self,root):
#         def solve(node):
#                 if node==None:
#                         return 0
#                 left_height=solve(node.left)
#                 right_height=solve(node.right)
#                 return 1+max(left_height,right_height)
#         return solve(root)
# x=2
# k=10
# n=7
# a=[4,1,7,2,2,9,5]
# freq=[0]*(k+1)
# for i in range(n):
#     freq[a[i]]+=1
# prefix=[0]*(k+1)
# prefix[0]=freq[0]
# for i in range(1,len(freq)):
#     prefix[i]=prefix[i-1]+freq[i]
# q=5
# print(prefix[q])
# a=[2,5,5,8,1,9,3]
# n=7
# k=10
# freq=[0]*(k+1)
# for i in range(n):
#     freq[a[i]]+=1
# prefix=[0]*(k+1)
# prefix[0]=freq[0]
# for i in range(1,len(freq)):
#     prefix[i]=prefix[i-1]+freq[i]
# x=0
# if x==0:
#     print(prefix[-1])
# else:
#      count=prefix[-1]-prefix[x-1]
#      print(count)

# arr=[1,1,2,4,4,4,7,9]
# n=8
# k=10
# freq=[0]*(k+1)
# for i in range(n):
#     if freq[arr[i]]==0:
#      freq[arr[i]]+=1
# prefix=[0]*(k+1)
# prefix[0]=freq[0]
# for i in range(1,len(freq)):
#    prefix[i]=prefix[i-1]+freq[i]

# a=1
# b=4
# if a==0:
#    print(prefix[b])
# else:
#    print(prefix[b]-prefix[a-1])
# nums=[1,2,3,2]
# freq=[0]*(max(nums)+1)
# for i in range(len(nums)):
#         freq[nums[i]]+=1
# total=0
# for i in range(len(freq)):
#         if freq[i]==1:
#                 total+=i
# print(freq)
# print(total)

# a="abba"
# b="baab"
# a_sub=[]
# b_sub=[]
# n=len(a)
# m=len(b)
# found=False
# for i in range(n):
#     for j in range(i,n):
#         s1=a[i:j+1]
#         for x in range(m):
#                 for y in range(x,m):
#                       s2=b[x:y+1]
#                       combined=s1+s2
#                       if combined==combined[::-1]:
#                            found=True
#                            break
#                 if found:
#                      break
#         if found:
#              break
#     if found:
#          break
        
# print("Yes"if found else "No")


# found=False      
# for s1 in a_sub:
#     for s2 in b_sub:
#         combined=s1+s2
#         if combined==combined[::-1]:
#              found=True
#              break
#     if found:
#         break
# print("Yes"if found else "No")

# s=""
# st=""
# for ch in s.lower():
#      if ch.isalnum():
#           st+=ch
# if st==st[::-1]:
#      print("yes")
# else:
#      print("no")

# s="madam"
# i=0
# j=len(s)-1
# while i<=j:
#     if s[i]==s[j]:
#         i+=1
#         j-=1
#     else:
#         j-=1

# s="A man, a plan, a canal: Panama"
# i=0
# j=len(s)-1
# found=False
# while i<j:
#     while not s[i].isalnum():
#         i+=1
#     while not s[j].isalnum():
#         j-=1
#     if s[i].lower()!=s[j].lower():
#         print("False")
#         break
#     i+=1
#     j-=1
# print("True")



# l="IceCreAm"
# s=list(l)
# vowels="aeiouAEIOU"
# i=0
# j=len(l)-1
# while i<j:
#     while s[i] not in vowels:
#         i+=1
#     while s[j] not in vowels:
#         j-=1

#     s[i],s[j]=s[j],s[i]
#     i+=1
#     j-=1
# print("".join(s))
    
# nums=[0,0,1,1,1,2,2,3,3,4]
# count=1
# i=0
# j=i+1
# while j<len(nums):
#     if nums[i]==nums[j]:
#         j+=1
#     else:
#         i+=1
#         nums[i]=nums[j]
#         j+=1
#         count+=1
# print(nums,count)

nums=[3,2,2,3]
val=3
i=0
j=1
count=0
while j<len(nums):
    if nums[i]==val and nums[i]!=nums[j]:
        count+=1
        nums[i]=nums[j]
    i+=1
    j+=1
print(nums,count)