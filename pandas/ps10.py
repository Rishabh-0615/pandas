importpandasaspd

df=pd.read_csv('Datasets/Iris/Iris.csv')

df.columns=[

'sepalLengths',

'sepalWidths',

'petalLengths',

'petalWidths',

'class'

]

df.head()

setosa=df[df['class']=='Iris-setosa']

versicolor=df[df['class']=='Iris-versicolor']

setosa.head()

versicolor.head()

merged=pd.concat([setosa,versicolor])

merged.head()

merged.tail()

sorted=df.sort_values(by='petalLengths')

sorted.head()

transposed=df.T

transposed.head()

melted=pd.melt(df,id_vars=['class'],value_vars=['sepalLengths','sepalWidths'])

melted.head()

wide=melted.pivot_table(index='class',

columns='variable',

values='value',

aggfunc='mean')

wide.head()