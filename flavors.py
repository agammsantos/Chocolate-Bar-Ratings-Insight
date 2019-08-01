import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('flavors_of_cacao.csv',header=0)
data.columns=['Company','Bar Origin or Bar Name','REF','Review Date','Cocoa Percentage','Company Location','Rating','Bean Type','Bean Origin']
# print(data[data['Rating'].isnull()==True])
# print(data.head())


'''
SOAL NOMOR 1: BEST COCOA BEANS
'''
bestBeans=data[['Bean Origin','Rating']]
bestBeans['Bean Origin'].fillna('Unknown',inplace=True)
# print(bestBeans[bestBeans['Bean Origin'].isnull()==True])
# print(bestBeans[bestBeans['Bean Origin']==''])

# print(bestBeans.groupby('Bean Origin').describe())
meanBestBeans=pd.concat([bestBeans.groupby('Bean Origin').mean(),bestBeans.groupby('Bean Origin').count()['Rating'],bestBeans.groupby('Bean Origin').max()['Rating']],axis=1)
meanBestBeans.columns=['Rating Avg','Rating Count','Max Rating']
highMeanBestBeans=meanBestBeans[meanBestBeans['Rating Avg']>=3.2]
maxRatingBestBeans=meanBestBeans[meanBestBeans['Max Rating']>=4]
# print(meanBestBeans)
maxRatingBestBeans.rename(index={maxRatingBestBeans.iloc[-1].name:'Unknown'},inplace=True)
# print(maxRatingBestBeans.iloc[-1])

plt.figure('Bar Plot of Bean Rating Mean for Each Origin Place',figsize=(17,7))
plt.title('Bar Plot of Cocoa Bean Rating Mean for Each Origin Place')
sns.barplot(highMeanBestBeans['Rating Avg'],highMeanBestBeans.index)
plt.ylabel('Origin Place')
plt.xlabel('Rating')
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.tight_layout()

plt.figure('Scatter Plot of Bean Rating Mean with Rating Count for Each Origin Place',figsize=(17,7))
plt.title('Scatter Plot of Cocoa Bean Rating Mean with Rating Count for Each Origin Place')
sns.scatterplot(highMeanBestBeans['Rating Avg'],highMeanBestBeans.index,s=[highMeanBestBeans['Rating Count']*17],alpha=.77)
plt.ylabel('Origin Place')
plt.xlabel('Rating')
plt.grid(True)
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.tight_layout()

plt.figure('Bar Plot of Maximum Bean Rating for Each Origin Place',figsize=(17,7))
plt.title('Bar Plot of Maximum Cocoa Bean Rating for Each Origin Place')
sns.barplot(maxRatingBestBeans['Max Rating'],maxRatingBestBeans.index,color='red')
plt.ylabel('Origin Place')
plt.xlabel('Rating')
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.tight_layout()
'''
JAWAB: 
Karena distribusi jumlah data rating yang tidak merata untuk setiap data asal daerah biji coklat, 
maka biji coklat terbaik sulit untuk ditentukan melalui rata-rata ratingnya dan 
dapat ditentukan berdasarkan rating tertinggi yang diperoleh dari seluruh data.
Sehingga biji coklat terbaik, dengan mengabaikan biji coklat dari daerah yang tidak diketahui,
berasal dari negara Venezuela dengan rating 5.
'''


'''
SOAL NOMOR 2: HIGHEST-RATED CHOCOLATE BARS
'''
bestBars=data[['Company Location','Rating']]
# print(bestBars[bestBars['Company Location'].isnull()==True])
# print(bestBars[bestBars['Company Location']==''])

meanBestBars=pd.concat([bestBars.groupby('Company Location').mean(),bestBars.groupby('Company Location').count(),bestBars.groupby('Company Location').max()],axis=1)
meanBestBars.columns=['Rating Avg','Rating Count','Max Rating']
highMeanBestBars=meanBestBars[meanBestBars['Rating Avg']>=3.2]
maxRatingBestBars=meanBestBars[meanBestBars['Max Rating']>=4]
# print(meanBestBars)

plt.figure('Bar Plot of Bar Rating Mean for Each Producing Country',figsize=(17,7))
plt.title('Bar Plot of Chocolate Bar Rating Mean for Each Producing Country')
sns.barplot(highMeanBestBars['Rating Avg'],highMeanBestBars.index)
plt.ylabel('Producing Country')
plt.xlabel('Rating')
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.tight_layout()

plt.figure('Scatter Plot of Bar Rating Mean with Rating Count for Each Producing Country',figsize=(17,7))
plt.title('Scatter Plot of Chocolate Bar Rating Mean with Rating Count for Each Producing Country')
sns.scatterplot(highMeanBestBars['Rating Avg'],highMeanBestBars.index,s=[highMeanBestBars['Rating Count']*17],alpha=.77)
plt.ylabel('Producing Country')
plt.xlabel('Rating')
plt.grid(True)
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.tight_layout()

plt.figure('Bar Plot of Maximum Bar Rating for Each Producing Country',figsize=(17,7))
plt.title('Bar Plot of Maximum Chocolate Bar Rating for Each Producing Country')
sns.barplot(maxRatingBestBars['Max Rating'],maxRatingBestBars.index,color='red')
plt.ylabel('Producing Country')
plt.xlabel('Rating')
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.tight_layout()
'''
JAWAB: 
Karena distribusi jumlah data rating yang kurang merata untuk setiap data asal negara produk coklat olahan, 
maka produk coklat olahan terbaik sulit untuk ditentukan melalui rata-rata ratingnya dan 
dapat ditentukan berdasarkan rating tertinggi yang diperoleh dari seluruh data.
Sehingga produk coklat olahan terbaik berasal dari negara Italy dengan rating 5.
'''

'''
SOAL NOMOR 3: CORRELATION BETWEEN COCOA SOLIDS PERCENTAGE AND RATING
'''
corrPercentRating=data[['Cocoa Percentage','Rating']]
# print(corrPercentRating[corrPercentRating['Cocoa Percentage'].isnull()==True])
corrPercentRating['Cocoa Percentage']=pd.to_numeric(corrPercentRating['Cocoa Percentage'].str[:-1])
# time consuming process:
# j=0
# for i in corrPercentRating['Cocoa Percentage']:
#     corrPercentRating['Cocoa Percentage'].iloc[j]=float(i.strip('%'))
#     j+=1
# print(corrPercentRating.head())
# print(corrPercentRating.tail())
# print(corrPercentRating.corr())

plt.figure('Relationship Between Cocoa Solids Percentage and Rating on Scatter Plot')
plt.title('Relationship Between Cocoa Solids Percentage and Rating on Scatter Plot')
sns.scatterplot(corrPercentRating['Cocoa Percentage'],corrPercentRating['Rating'])
plt.xlabel('Cocoa Solids Percentage (%)')
plt.ylabel('Rating')
plt.xticks(np.arange(40,101,5))
plt.grid(True)
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.tight_layout()

plt.figure('Relationship Between Cocoa Solids Percentage and Rating on Line Plot')
plt.title('Relationship Between Cocoa Solids Percentage and Rating on Line Plot')
sns.lineplot(corrPercentRating['Cocoa Percentage'],corrPercentRating['Rating'])
plt.xlabel('Cocoa Solids Percentage (%)')
plt.ylabel('Rating')
plt.xticks(np.arange(40,101,5))
plt.grid(True)
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.tight_layout()
'''
JAWAB:
Dapat dilihat bahwa tidak ada korelasi yang signifikan diantara kedua variabel, Cocoa Solids Percentage dan Rating.
Plot menunjukkan bahwa tidak ada perubahan yang berarti dengan bertambahnya atau berkurangnya persentase kokoa terhadap rating yang diperoleh produk,
namun menunjukkan bahwa sebagian besar produk coklat memiliki persentase kokoa 55% hingga 90% dan 
produk dengan rating tertinggi memiliki persentase kokoa 70%.
'''

plt.show()
