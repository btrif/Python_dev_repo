#!/usr/bin/python                   o(^_^)o
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Investigating Ulam sequences
Problem 167
For two positive integers a and b, the Ulam sequence U(a,b) is defined by
U(a,b)1 = a, U(a,b)2 = b and for k > 2, U(a,b)_k is the smallest integer greater than U(a,b)(k-1)
which can be written in exactly one way as the sum of two distinct previous members of U(a,b).

For example, the sequence U(1,2) begins with
1, 2, 3 = 1 + 2, 4 = 1 + 3, 6 = 2 + 4, 8 = 2 + 6, 11 = 3 + 8;
5 does not belong to it because 5 = 1 + 4 = 2 + 3 has two representations
as the sum of two previous members, likewise 7 = 1 + 6 = 3 + 4.

Find ∑U(2,2n+1)_k for 2 ≤ n ≤10, where k = 10**11.


'''
import time

### 1,2 --> BUT WE DON't NEED THIS ONE      !!!!!!
# 1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, 57, 62, 69, 72, 77, 82, 87, 97, 99, 102, 106, 114, 126, \
# 131, 138, 145, 148, 155, 175, 177, 180, 182, 189, 197, 206, 209, 219, 221, 236, 238, 241, 243, 253, 258, 260, 273, 282



### 2, 5 --> WE NEED ONLY THIS
# 2, 5, 7, 9, 11, 12, 13, 15, 19, 23, 27, 29, 35, 37, 41, 43, 45, 49, 51, 55, 61, 67, 69, 71, 79, 83, 85, 87, 89, 95, 99, 107,
# 109, 119, 131, 133, 135, 137, 139, 141, 145, 149, 153, 155, 161, 163, 167, 169, 171, 175, 177, 181, 187, 193,
# 195, 197, 205, 209, 211, 213, 215, 221, 225, 233, 235, 245


### 2, 7 --> WE NEED ONLY THIS
# 2, 7, 9, 11, 13, 15, 16, 17, 19, 21, 25, 29, 33, 37, 39

### ...................  ###

### 2, 21 --> WE NEED ONLY THIS
# 2, 21, 23,





def Ulam_gen(n, lim) :
    while n < lim :
        if n%2 ==0 :
            n = n//2
            print(n)
        elif n%2==1 :
            n=3*n+1
            print(n)
        if n==1: break

Ulam_gen(155, 10300)



############## not my code
#
# def extend_seq(l,a,N):
#     d = {x for x in l}
#     al = [(x,red(a*x)) for x in l]
#     al.sort(key=lambda x:-x[1])
#     dists = [x[1] for x in al]
#     xs = [x[0] for x in al]
#     sums = {}
#     for rep in range(N):
#         min_sum = 2*l[-1]
#         best_small = 1
#         for i in range(len(xs)):
#             small = xs[i]
#             large_idx = -1
#             top = l[-1]
#             while(small+large > top and small+large < min_sum):
#                 large = l[large_idx]
#                 if(not small+large in candidates):
#                     sums[small+large] = 0
#                 sums[small+large] += 1
#                 large_idx -= 1
#             candidates = [x for x in sums if sums[x] == 1 and x < min_sum]
#             for s in candidates:
#                 j = i+1
#                 ok = True
#                 while(j < len(s)-1 and l[j]+l[j+1] <= s):
#                     if(s-l[j] in d):
#                         sums[s] += 1
#                         ok = False
#                         break
#                 if(ok):
#                     min_sum = s
# def next_seq(l):
#     i = 0
#     j = len(l)-1
#     M = l[-1]
#     ans = {}
#     while(i < j):
#         k = j
#         while(j < len(l)):
#             ans[l[i] + l[j]] = not (l[i] + l[j] in ans)
#             j += 1
#         j = k
#         i += 1
#         #print("A",ans)
#         while(l[i] + l[j-1] > M and i < j-1):
#             j -= 1
#         #print("IJ",i,j,l[i],l[j])
#         m = min([x for x in ans if ans[x] == True])
#         if(i+1 >= len(l) or l[i] + l[i+1] > m):
#             #print("---------------",i,j,m)
#             return m
#         #print(i,j,l[i],ans)
#     return m
#
# def next_seq2(l,d):
#     s = [x+y for x in l for y in l if x < y and x+y > l[-1]]
#     s.sort()
#     i = 0
#     while(i+1 < len(s)):
#         if(s[i] == s[i+1]):
#             val = s[i]
#             while(s[i] == val):
#                 s.pop(i)
#         else:
#             return s[i]
#     return s[0]
#
# def ulam_old(a,b,n):
#     seq = [a,b]
#     m = 2
#     for i in range(n):
#         m = next_seq(seq)
#         seq.append(m)
#     return seq
#
# def ulam(a,b,n,debug=False):
#     c,dq,ans = extend_with_storage_careful([a,b],{a+b},{},n,debug)
#     return ans
#
# def ulam_rep_dumb(l,n):
#     seq = l
#     d = {}
#     for x in l:
#         for y in l:
#             if(x+y in d):
#                 d[x+y]+=1
#             else:
#                 d[x+y]=1
#     for x in l:
#         d[x] = 0
#
#     for i in range(n):
#         m = min(x for x in d if d[x] == 1 and x > seq[-1])
#         seq.append(m)
#         d[m] = 0
#         for x in seq:
#             if(x+m in d):
#                 d[x+m] += 1
#             else:
#                 d[x+m] = 1
#     return seq
#
#
# def ulam_rep_dumb_k(l,n):
#     seq = l
#     d = {}
#     for x in l:
#         for y in l:
#             for z in l:
#                 if(x < y and y < z):
#                     d[x+y+z]=d.get(x+y+z,0)+1
#     for x in l:
#         d[x] = 0
#
#     for i in range(n):
#         m = min(x for x in d if d[x] == 1 and x > seq[-1])
#         seq.append(m)
#         d[m] = 0
#         for x in seq:
#             for y in seq:
#                 if(y < x):
#                     d[x+y+m] = d.get(x+y+m,0)+1
#                 else:
#                     break
#
#         print(i,seq[-1])
#     return seq
#
#
#
# ulam_rep_dumb(1,20)

print()

# https://github.com/daniel3735928559/wip-ulam/blob/master/README.md
# https://github.com/daniel3735928559/wip-ulam
# https://archive.lib.msu.edu/crcmath/math/math/u/u005.htm
# https://books.google.ro/books?id=1lCHYj5eV-EC&pg=PA85&lpg=PA85&dq=Ulam+sequence+algorithm&source=bl&ots=ccdsfVKnlk&sig=tZDbMn0S8LgyDNKnDYDW5tipXQU&hl=en&sa=X&ved=0ahUKEwj0vpXJkpjSAhVHhiwKHUqCBfw4ChDoAQg-MAY#v=onepage&q=Ulam%20sequence%20algorithm&f=false


print('\n--------------------------TESTS------------------------------')
t1  = time.time()






t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()







# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
