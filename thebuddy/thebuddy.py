
# coding: utf-8

# In[1]:

import pandas as pd
import datetime
import math


# In[2]:

df = pd.read_excel("ExcelFileFiverr (2).xlsx",sheetname = "Sheet1")


# In[3]:

DayL = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
df["WeekDay"]= ""
for row in range(df.shape[0]):
    df["WeekDay"].iat[row] = DayL[datetime.datetime.weekday(df["Date Sold"].iat[row])]
df = df.drop_duplicates("Date Sold") 


# In[4]:

df_g = pd.groupby(df,[df[";Company"],df.WeekDay])


# In[5]:

final_df = df_g.count()
final_df = final_df["Date Sold"]


# In[6]:

final_df_update = pd.DataFrame(final_df)


# In[7]:

new_df = final_df_update.unstack()
import math
total = {}
list_day = ["Fri","Mon","Sat","Sun","Thu","Tue","Wed"]
del_item = ["(",")","[","]"]

def cleaning(x,y):
    c=""
    for letter in x:
        if not letter in y:
            c+= letter
    return c


# In[8]:

output = open("output.csv","w")
output.write("company,Top-Sale,Top-Day,Second-Sale,Second-Day,Third-Sale,Third-Day\n")
for row in range(new_df.shape[0]):
    total[new_df.index[row]]= {}
    for day in range(7):
        if not math.isnan(new_df.irow(row)[day]):
            total[new_df.index[row]][new_df.irow(row)[day]] = list_day[day]
#output.write("company, first_day, first_sale,second_day,second_sale,third_day,third_sale\n")            
for item in total:
    if len(total[item].items()) <= 3:
        x = str(sorted(total[item].items(),reverse=True))
        z = cleaning(x,del_item)
        output.write(str(item).replace(",","")+","+ z +"\n")
    else:
        x = str((sorted(total[item].items(),reverse=True))[:3])
        z = cleaning(x,del_item)
        output.write(str(item).replace(",","")+","+ z +"\n")

        
output.close()


# In[ ]:



