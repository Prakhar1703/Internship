import pandas as pd
#read data
data= pd.read_csv("IRIS.csv")
data1=pd.read_csv('IRIS.csv')
print(data)
#selected data
selected_columns=data[['sepal_length','sepal_width','species']]
print(selected_columns)
#filterd data
filtered_data=data[data["sepal_length"]>5]
print(filtered_data)
#grouped data
grouped_data=data.groupby('species')['sepal_length'].sum()
print(grouped_data)
grp_data=data.groupby('sepal_length')['sepal_width'].sum()
print(grp_data)
#merge data
merg_data=pd.merge(data,data1,on='sepal_length')
print(merg_data)
#fill null values
data.fillna(0,inplace=True)
print(data)
#apply logic or operation and save data in new column
def process_value(value):
    #apply custom logic to process each value
    processed_value=value*2
    return processed_value
data1['double_sepal']=data['sepal_length'].apply(process_value)
print(data1)
#pivot table
pivot_table=pd.pivot_table(data,values='sepal_length',index='petal_length',columns='species')
print(pivot_table)