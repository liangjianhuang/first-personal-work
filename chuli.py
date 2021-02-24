#!/usr/bin/env python
# coding: utf-8

# In[76]:


import jieba
from collections import Counter
import pyecharts.options as opts
from pyecharts.charts import WordCloud


# In[67]:


fr=open('comments.json', 'r', encoding='UTF-8')
words = fr.read()
word1_list = list(jieba.cut(words))
word2_list = jieba.analyse.extract_tags(words,topK=30)
print(word_list)


# In[71]:


result=[]
for i in word1_list:
    if i in word2_list:
        result.append(i)


# In[91]:


words_counter = Counter(result).most_common(30)
words_counter


# In[111]:


result1={}
for item in words_counter:
    result1.update({'name':item[0]})
    result1.update({'value':item[1]})
    print(result1)


# In[ ]:




