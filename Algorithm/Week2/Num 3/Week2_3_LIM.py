#!/usr/bin/env python
# coding: utf-8

# In[22]:


S = input()

pre_s = 'A'
cnt_0 = 0
cnt_1 = 0

for i in S :
    if i != pre_s :
        if i == '0' :
            cnt_0 += 1
            pre_s = i
        elif i == '1' :
            cnt_1 += 1
            pre_s = i

        
if min(cnt_0, cnt_1) == cnt_0 :
    print(cnt_0)
else :
    print(cnt_1)

