importpandasaspd

df=pd.read_csv('Datasets/Adult/adult.csv')

df.columns=[

'age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','income'

]

df.head()

us=df[df['native-country']==' United-States']

us.head()

male=df[df['sex']==' Male']

male.head()

white=df[df['race']==' White']

white.head()

female=df[df['sex']==' Female']

female.head()

merged=pd.concat([male,female])

merged.head()

merged.tail()

sorted=df.sort_values(by='age')

sorted.head()

transposed=df.T

transposed.head()

melted=pd.melt(df,id_vars=['native-country'],value_vars=['capital-gain','capital-loss'])

melted.head()

wide=melted.pivot_table(index='native-country',

columns='variable',

values='value',

aggfunc='mean'

)

wide.head()