importpandasaspd

df=pd.read_csv('Datasets/Movie/movies_metadata.csv',low_memory=False)

df.head()

en_language=df[df['original_language']=='en']

fr_language=df[df['original_language']=='fr']

en_language.head()

fr_language.head()

merged=pd.concat([en_language,fr_language])

merged.head()

merged.tail()

sorted=df.sort_values(by='vote_average')

sorted.head()

transposed=df.T

transposed.head()

melted=pd.melt(df,id_vars=['title'],value_vars=['vote_average','vote_count'])

melted.head()

wide=melted.pivot_table(index='title',

columns='variable',

values='value',

aggfunc='mean'

)

wide.head()