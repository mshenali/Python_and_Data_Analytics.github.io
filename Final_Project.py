# -*- coding: utf-8 -*-
"""Final_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cBuzZWa5je2Wq_jmqi-vNif_xt7W3wbP

### **Reading the data set**

---
***Data Set Description***

Pclass:  Passenger Class : 
                          
                          1-> 1st class
                          2-> 2nd class
                          3-> 3rd class

Survived:  Survival       : 
                           
                           1-> Yes
                           0-> No

Name:    Name of the passenger

Sex:     Gender of the passenger

Age:     Age of the passenger

SibSp:   Number of siblings/spouses aboard

Parch:   Number of parents/children aboard

Ticket:  The ticket number of the passenger

Fare:    Passenger fare (In British Pounds)

Cabin:   Allocated cabin number for the passenger

Embarked: Port of embarkation :
                              
                               C -> Cherbourg
                               Q -> Queenstown
                               S -> Southampton
"""

import pandas as pd
import numpy as np

# Commented out IPython magic to ensure Python compatibility.
#Load the data set into a data frame

# %load_ext google.colab.data_table
Titanic=pd.read_csv('/content/train.csv')
Titanic.head()

# Commented out IPython magic to ensure Python compatibility.
# %unload_ext google.colab.data_table

df=pd.DataFrame(Titanic)
df.head()

#Checking the size of the data frame

df.shape
#df.index

"""


---


***Handling Null values***"""

#Returns total number of missing values in each column of the data frame

df.isnull().sum()

#Drop the column if the total number of missing values is greater than 35% of the total number of rows in the data frame

drop_col=df.isnull().sum()[df.isnull().sum()>(0.35*df.shape[0])]
print(drop_col)

#drop_col.index

df.drop(drop_col.index,axis=1,inplace=True)

#Returns the columns with total missing values being less than 35% of the total number of rows in the data frame

#df.isnull().any()
df.isnull().sum()

df.fillna(df.mean(),inplace=True)

#Returns the columns with missing values to which the statistical operation cannot be applied(For string data type)

df.isnull().sum()

#Checking the value distribution in the column Embarked

df['Embarked'].describe()

#Fill the Embarked column with the mode of the occurrances

df['Embarked'].fillna('S',inplace = True)

#To check whether there are any more columns with missing values

df.isnull().any()

"""---

### **Data Analysis**
"""

#Correlation among the column varaibles

df.corr()

"""> *It can be observed that the passenger class has a considerable correlation with being a survivor; which suggests that higher the passenger class lower the chance of being a survivor(i.e. Inversly proportioned).*



> *i.e. The lower passenger class values (wealthy passengers) might have had been favoured in attempts of saving/survival*



> *A considerable negative correlation can be observed between passenger class and the fare ,which is an obvious case of inversely proportaional relationship.*



> *Though a similar magnitude of negative correlation is shown between age and passenger class;it leads to no useful insights.*



>*The same can be stated regarding the comparatively significant positive correlation between the variables SibSp and Parch.*

---


 ***Survival rate of a passenger boarded alone***
 

 
 Modification: 
 > *Combining the two related variables,no. of siblings and the no. of parents aboard to form a new variable containg the no. of family members aboard*.
"""

#Creating the new variable combining two existing related variables

df['FamSize']=df['SibSp']+df['Parch']

#Removing the two varibales from the data frame

df.drop(['SibSp','Parch'], axis=1,inplace=True)

#Checking the correlation between the variables in the modified data frame

df.corr()

"""Modification:
>*Create a new variable with the column name **Alone** using the column FamSize.*

"""

# Checking whether a person being alone affected the survival rate

df['Alone']=[0 if df['FamSize'][i]>0 else 1 for i in df.index]
df.head()

# Calculate the number of passengers that boarded alone and survived

df.groupby(['Alone'])['Survived'].mean()

#Checking the correlation between a passenger being borded alone and the charged fare

df[['Alone','Fare']].corr()

"""


---

***Survival rate of a female passenger***



Modification:
>*Create a new variable with the column name **Gender** using the column Sex.*"""

#Checking whether the gender being female affected the survival rate

df['Gender'] = [0 if df['Sex'][i]=='male' else 1 for i in df.index]

#Calculate the number of females survived

df.groupby(['Gender'])['Survived'].mean()

"""

---
***Survival rate comparison among passenger classes***


"""

#Checking whether the class had affected the surviva rate

df.groupby(['Pclass'])['Survived'].mean()

"""

---
***Survival rate and port of embarkation***



"""

# Checking whether the port of embarkation affected the survival rate

df.groupby(['Embarked'])['Survived'].mean()

"""---

### **Conclusions**

*    Passengers boarded the ship with their family had survived at a comparatively higher rate. 

*    Female passengers had been prioritized over men.


*    Hierarchy might have played a role in passenger survival rate given that majority of the survivors being from lower passenger classes.

*    Passengers who boarded the ship at Cherbourg have had a comparatively higher chance of survival.
"""