import pandas as pd

df = pd.read_csv('gdp.csv')

print('----- 2007 亞洲(Asia) 平均壽命(lifeExp) -----')
s1 = (df['year'] == 2007) & (df['continent'] == 'Asia')
df1 = df[s1].sort_values(by=['lifeExp'],ascending=False)
print(df1[['country','lifeExp']])
print()

print('----- 2000~2007 臺灣(Taiwan) 人均國內生產總值(gdpPercap) -----')
s2 = (df['country'] == 'Taiwan') & (df['year'] >= 2000)
df2 = df[s2]
print(df2[['country','year','gdpPercap']])
