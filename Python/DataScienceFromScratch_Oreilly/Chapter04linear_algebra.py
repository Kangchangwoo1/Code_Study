
# coding: utf-8

# # 4.1 선형대수

# In[1]:


height_weight_age = [70,170,40]
grades = [95,80,75,62]


# In[4]:


def vector_add(v,w):
    return [v_i + w_i for v_i,w_i in zip(v,w)]

def vector_subtract(v,w):
    return [v_i - w_i for v_i,w_i in zip(v,w)]


# In[7]:


def vector_sum(vectors):
    result = vecotrs[0]
    for vector in vectors[1:]:
        result = vector_add(result,vector)
    return result

def vector_sum(vectors):
    return reduce(vector_add,vectors)

vector_sum = partial(reduce,vector_add)
# reduce의 개념
#partial


# In[8]:


def scalar_multiply(c,v):
    return [ c * v_i in v]


# In[9]:


def vector_mean(vectors):
    n= len(vectors)
    return scalar_multiply(1/n,vector_sum(vectors))


# In[10]:


def dot(v,w):
    return sum(v_i * w_i for v_i, w_i in zip(v,w))


# In[11]:


def sum_of_squares(v):
    return dot(v,v)

#내적의 개념?


# In[12]:


import math
def magnitude(v):
    return math.sqrt(sum_of_squares(v))


# In[13]:


def squared_distance(v,w):
    return sum_of_squares(vector_subtract(v,w))

def distance(v,w):
    return math.sqrt(squared_distance(v,w))

def distance(v,w):
    return magnitude(vector_subtract(v,w))


# # 4.2 행렬

# In[14]:


#2개의 행(row)과 3개의 열(column)로 이루어져 있다.
A = [[1,2,3],[4,5,6]]

#3개의 행(row)과 2개의 열(column)로 이루어져 있다.
B = [[1,2],[3,4],[5,6]]


# In[15]:


def shape(A):
    num_rows = len(A)
    num_columns = len(A[0]) if A else 0
    return num_rows, num_columns


# In[18]:


def get_row(A,i):
    return A[i]

def get_column(A,j):
    return [A_i[j] for A_i in A]


# In[26]:


def make_matrix(num_rows,num_cols,entry_fn):
    return [[entry_fn(i,j) for j in range(num_cols)] for i in range(num_rows)]


# In[27]:


def is_diagonal(i,j):
    return 1 if i==j else 0


# In[28]:


identity_matrix = make_matrix(5,5,is_diagonal)


# In[29]:


identity_matrix


# # 4.3 더 공부해 보고 싶다면
# - https://www.math.ucdavis.edu/~linear/
# - http://joshua.smcvt.edu/linearalgebra/
# - http://www.math.brown.edu/~treil/papers/LADW/LADW.html
