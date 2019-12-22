
# coding: utf-8

# In[1]:



import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from scipy.stats.stats import ttest_ind
import warnings

warnings.filterwarnings('ignore')


# In[3]:


postgres_user = 'dsbc_student'
postgres_pw = '7*.8G9QH21'
postgres_host = '142.93.121.174'
postgres_port = '5432'
postgres_db = 'studentsperformance'

engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(
    postgres_user, postgres_pw, postgres_host, postgres_port, postgres_db))

stu_df = pd.read_sql_query('select * from studentsperformance',con=engine)

# no need for an open connection, 
# as we're only doing a single query
engine.dispose()


# In[4]:


stu_df.groupby("gender").mean()[["math score", "reading score", "writing score"]]


# In[8]:


ttest_ind(stu_df[stu_df.gender == "female"][["math score", "reading score", "writing score"]],
          stu_df[stu_df.gender == "male"][["math score", "reading score", "writing score"]])


# In[10]:


stu_df.groupby("race/ethnicity").mean()[["math score", "reading score", "writing score"]]


# 
# 2. Are there any differences between the lunch types with respect to their performances in exams? If there are, how do you explain this?

# In[11]:


stu_df.groupby("lunch").mean()[["math score", "reading score", "writing score"]]


# In[13]:


ttest_ind(stu_df[stu_df.lunch == "free/reduced"][["math score", "reading score", "writing score"]],
          stu_df[stu_df.lunch == "standard"][["math score", "reading score", "writing score"]])


# 3. Does the test preparation course seem to have an effect on the exam performances?

# In[14]:


stu_df.groupby("test preparation course").mean()[["math score", "reading score", "writing score"]]


# In[16]:



ttest_ind(stu_df[stu_df["test preparation course"] == "completed"][["math score", "reading score", "writing score"]],
          stu_df[stu_df["test preparation course"] == "none"][["math score", "reading score", "writing score"]])


# 4. Which two exam scores are correlated the most with each other?

# In[17]:


stu_df[["math score", "reading score", "writing score"]].corr()

