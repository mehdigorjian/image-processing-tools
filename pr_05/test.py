import numpy as np
# Q1
# n, m = 3, 3
# r = 1.04
# w = np.zeros((n,m))
# sum =0
# for i in range(n):
#     for j in range(m):
#         w[i,j] = np.exp(-1*((i+.5-n/2)*(i+.5-n/2)+(j+.5-m/2)*(j+.5-m/2))/(r*r))
#         sum += w[i,j]
# print(sum)
# print(np.round(w/np.sum(w),decimals=2))
##############################################
# Q2
# n, m = 3, 3
# w = np.array([[14,31,14],\
#               [33,62,31],\
#               [15,32,14]])

# c = np.array([[175,187,159,156,109],\
#              [191,191,188,118,102],\
#              [166,168,139,101,159],\
#              [145,155,160,197,144],\
#              [155,169,176,194,100]])
# # s1 = 0
# # s2 = 0
# ss = []
# sm = []
# for i in range(n):
#     for j in range(m):
#         # s1 += np.power(w[i,j],2) * np.power(c[1+i-(n-1)//2,1+j-(m-1)//2],2)
#         # s2 += np.power(w[i,j],2)
#         e1 = np.power(w[i,j],1) * np.power(c[1+i-(n-1)//2,1+j-(m-1)//2],1)
#         ss.append(e1)
#         e2 = np.power(w[i,j],1)
#         sm.append(e2)
# # print(np.power(s1/s2, 1/2))
# # print(max(ss)/max(sm))
# print(min(ss)/min(sm))
##############################################
# Q3
n, m = 5, 5
ang = 58
w = np.zeros((n,m))
for i in range(n):
    for j in range(m):
        L = -np.sin(ang)*(i+.5-n/2) + np.cos(ang)*(j+.5-m/2)
        w[i,j] = 1 - abs(L)

w[w<0] = 0
print(f'W: \n', w)
print(f'SUM: \n', np.sum(w))
w = w/np.sum(w)
print(f'w: \n',np.round(w, decimals=2))