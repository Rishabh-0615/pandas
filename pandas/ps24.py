importpandasaspd

df=pd.read_csv('Datasets/forestfires/forestfires.csv')

df.head()

not_affected=df[df['area']<=1]

partially_affected=df[(df['area']>1)&(df['area']<=50)]

fully_affected=df[df['area']>50]

not_affected.head()

partially_affected.head()

fully_affected.head()

merged=pd.concat([partially_affected,fully_affected])

merged.head()

merged.tail()

sorted=df.sort_values(by=['temp','wind','area'])

sorted.head()

transposed=df.T

transposed.head()

melted=pd.melt(df,id_vars=['month'],value_vars=['wind','rain'])

melted.head()

wide=melted.pivot_table(index='month',

columns='variable',

values='value',

aggfunc='mean'

)

wide.head()