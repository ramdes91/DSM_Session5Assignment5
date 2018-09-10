
# coding: utf-8

# In[17]:


def throws():
    return 5/0

try:
    throws()
except ZeroDivisionError:
    print ("division by zero!")
except Exceptionerror:
    print ('Caught an exception')


# In[16]:


subject=["Americans", "Indians"]
verb=["Play", "watch"]
obj=["Baseball","Cricket"]

# Use list comprehension instead of looping over each of the predicates
sentence_list = [(sub+" "+ vb + " " + ob) for sub in subject for vb in verb for ob in obj]
for sentence in sentence_list:
    print (sentence)

