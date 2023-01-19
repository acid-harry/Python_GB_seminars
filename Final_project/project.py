import pandas
data = pandas.read_csv('train.csv', index_col='PassengerId')

#Какое количество мужчин и женщин ехало на корабле? 
print('Какое количество мужчин и женщин ехало на корабле')
print(data.Sex.value_counts())


#Доля выживших пассажиров.
print('Доля выживших пассажиров: ')
onePercentTotal=data.Survived.count()/100
survived=data.Survived.sum()
print(round(survived/onePercentTotal,2))

#Доля пассажиров первого класса 
print('Доля пассажиров первого класса: ')
data['FirstClassCounter']= 0
mask=data.Pclass == 1
data.loc[mask,'FirstClassCounter']=1
    
_firstClassCounter=data.FirstClassCounter.sum()
print(round(_firstClassCounter/onePercentTotal,2))


#Средний возраст пассажиров и медиана возраста.
print('Среднее значение и медиана возраста пассажирова: ')

print(round(data.Age.mean(),2))
print(round(data.Age.median(),2))

data['count']= 1
data.pivot_table('Name', 'Pclass', 'Survived', 'count').plot(kind='bar', stacked=True)

#Корреляция между признаками SibSp и Parch. 
print('Коррелируют ли число братьев/сестер/супругов с числом родителей/детей: ')
df = pandas.DataFrame(data=data,columns=['SibSp', 'Parch'])
print(round(df.corr().loc['SibSp','Parch'],2))

#Самое популярное женское имя на корабле.
print("Самое популярное женское имя на корабле: ")

NameExtract=data.Name.str.extract('^.+?Mrs\..+?\((.+?)\)|^.+?Miss\.\s([\w\s]+)',expand=False)
NameExtract.fillna('',inplace=True)
NameExtract.columns = ['Mrs','Miss']
NameExtract['CombinedName']=NameExtract.apply(lambda x:'%s%s' % (x['Mrs'],x['Miss']),axis=1)
NameExtract.drop(['Mrs','Miss'],axis=1,inplace=True)
femalenames=[]
#обрабатываем список имен
for i in range(NameExtract.CombinedName.count()):
    names=NameExtract.loc[i+1,'CombinedName']
    words=names.split(' ')
    for word in words:
        if len(word)>2 and word.find('"'):
            femalenames.append(word)
    
femalenamesDataFrame=pandas.DataFrame(data=femalenames,columns=['Names'])
femalenamesDataFrame['count']= 1
femalenamesDataFrameGroupBy=femalenamesDataFrame.groupby('Names').sum()
femalenamesDataFrameSorted=femalenamesDataFrameGroupBy.sort_values(['count'], ascending=[False])
print(femalenamesDataFrameSorted.head(2))#показываем часто встечаемое имя