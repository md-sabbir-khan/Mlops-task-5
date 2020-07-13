#!/usr/bin/env python
# coding: utf-8

import pandas as pd
dataset = pd.read_csv('/home/Mr_spy/task-5/parsed_log.csv')
dataset


from sklearn.preprocessing import OneHotEncoder, LabelEncoder
X = dataset.iloc[:,:]
x = X.to_numpy()


label = LabelEncoder()


## Now taking only required field that requered for analysis 

IP = label.fit_transform(x[:,0])
D = label.fit_transform(x[:,2])
U = label.fit_transform(x[:,3])


## changing Heading name

df1 = pd.DataFrame(IP, columns=['IPs'])
df2 = pd.DataFrame(D, columns=['DATE'])
df3 = pd.DataFrame(U, columns=['URL'])


frames = [df1, df2, df3]
result = pd.concat(frames, axis=1 )


## For better accuracy of our model we have to scale our data , For scaling we are using StandardScaler function of sklearn.

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()


## In Ip column all the IPs are of string datatype ,and model do not support string , so we have to convert it into int.

data_scaled = sc.fit_transform(result)

from sklearn.cluster import KMeans


""" find the group of IPs with similar attributes, so we will go for clustering , 
and we have to find either the IP is malicious or not so we will take two clusters.
Now we train our model with scaled dataset."""


model = KMeans(n_clusters=2)
model.fit(data_scaled)
pred  = model.fit_predict(data_scaled)
dataset_scaled = pd.DataFrame(data_scaled, columns=['IP', 'Date', 'URL'])


dataset_scaled['log'] = pred


ips = [dataset['Host'], result['IPs']]
ips_result = pd.concat(ips, axis=1)


## This function will calculate frequency of IP

def CountFrequency(my_list, ip_label): 
  
    ## Creating an empty dictionary  

    freq = {} 
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
    max_freq = 0
    max_key = 0
    for key, value in freq.items(): 
        if value > max_freq:
            max_freq = value
            max_key = key
    
    return ip_label[my_list.index(max_key)]

res = CountFrequency(ips_result['IPs'].tolist(), ips_result['Host'].tolist())
print (res)

# Write result in the result.text file

file1 = open("result.txt","w")
file1.write(res)
file1.close()




