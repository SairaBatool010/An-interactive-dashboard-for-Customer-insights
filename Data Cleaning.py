#!/usr/bin/env python
# coding: utf-8

# In[17]:


# Import necessary libraries
import pandas as pd
import missingno as msno
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import numpy as np 
import matplotlib.pyplot as plt
from scipy import stats
df = pd.read_csv('C:\\Users\\SKD\\Downloads\\Marketing_customer.csv')


# In[2]:


df.head()


# In[3]:


df.isnull().sum()


# In[4]:


duplicate_rows = df.duplicated()
print("\nDuplicate rows:")
print(duplicate_rows.sum())


# In[5]:


# Check for consistency in data types
data_types = df.dtypes
print("\nData types:")
print(data_types)


# In[6]:


# Get only categorical columns
categorical_columns = df.select_dtypes(include=['object']).columns

# Iterate over each categorical column
for column in categorical_columns:
    # Print the column name and its distinct values
    print(f"Distinct values of {column}:")
    print(df[column].unique())
    print()


# In[7]:


# Calculate max, min, and average values of numerical columns
max_values = df.select_dtypes(include='number').max()
min_values = df.select_dtypes(include='number').min()
average_values = df.select_dtypes(include='number').mean()

# Print the results
print("Maximum values:")
print(max_values)
print("\nMinimum values:")
print(min_values)
print("\nAverage values:")
print(average_values)


# In[8]:


# Calculate max, min, and average values of numerical columns
max_values = df.select_dtypes(include='number').max()
min_values = df.select_dtypes(include='number').min()
average_values = df.select_dtypes(include='number').mean()

# Print the results
print("Maximum values:")
print(max_values)
print("\nMinimum values:")
print(min_values)
print("\nAverage values:")
print(average_values)


# In[51]:


# Calculate max, min, and average values of numerical columns
max_values = df.select_dtypes(include='number').max()
min_values = df.select_dtypes(include='number').min()
average_values = df.select_dtypes(include='number').mean()

# Define numerical column names
numerical_columns = max_values.index

# Plotting
plt.figure(figsize=(12, 6))
plt.bar(numerical_columns, max_values, color='red', alpha=0.5, label='Max')
plt.bar(numerical_columns, min_values, color='blue', alpha=0.5, label='Min')
plt.bar(numerical_columns, average_values, color='green', alpha=0.5, label='Average')
plt.xlabel('Numerical Columns')
plt.ylabel('Values')
plt.title('Maximum, Minimum, and Average Values of Numerical Columns')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


# In[13]:


# Check for duplicate rows in the entire DataFrame
duplicate_rows = df[df.duplicated()]

if duplicate_rows.empty:
    print("No duplicate rows found.")
else:
    print("Duplicate rows found:")
    print(duplicate_rows)


# In[14]:


# Calculate summary statistics for numerical columns
summary_statistics = df.describe()

# Print summary statistics
print(summary_statistics)


# In[ ]:





# In[ ]:




