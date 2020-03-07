#!/usr/bin/env python
# coding: utf-8

# In[29]:
from math import *
import matplotlib.pyplot as plt

def time_series(dt, N):
    return [[cos(dt * i + t), sin(dt * i + t)] for i in range(1, N + 2)]


# In[48]:


N = 100000
dt = 1.2421
t = 0.01
T = time_series(dt, N)


# In[30]:


def make_w(ind, T, m):
    return T[ind : ind + m]


# In[31]:


def distance(x_i, x_j, m):
    sum = 0
    for k in range(m):
        sum += abs(x_i[k][0] - x_j[k][0]) + abs(x_i[k][1] - x_j[k][1])
    return sum/m


# In[32]:


def nearest(x_i, m):
    min_j = N + 1
    min_val = N + 1
    for j in range(i + 1, N - m):
        x_j = make_w(j, T, m)
        if (distance(x_i, x_j, m) < min_val):
            min_j = j
            min_val = distance(x_i, x_j, m)
    return min_j, min_val
    


# In[49]:


m = 1
graph = {}
while m < 20:
    P = 0
    for i in range(N - m - 1):
        x_i = make_w(i, T, m)
        j, delta = nearest(x_i, m)
        x_j = make_w(j, T, m)
        d = distance(x_i, x_j, m)
        x_i_next = make_w(i, T, m + 1)
        x_j_next = make_w(j, T, m + 1)
        D = distance(x_i_next, x_j_next, m + 1)
        if (D/d) > (m/(m + 1))*delta:
            P += 1
    graph[m] = P
    print(graph[m])
    m += 1
    


# In[46]:


L = list(graph.items())
x, y = zip(*L)
plt.plot(x, y)
plt.show()

