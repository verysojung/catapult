#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random
class Ground():
    def __init__(self):
        self.ground=[[700,400],[0,400]]
        a=0
        for i in range(0,700,100):
            
            for j in range(0,100,10):
                a+=random.randint(-5,5)
                self.ground.append([i+j,a+250])
        


# In[ ]:




