importpandasaspd

df=pd.read_csv('Datasets/dataset_Facebook.csv')

df.head()

photo_posts=df[df['Type']=='Photo']

status_posts=df[df['Type']=='Status']

photo_posts.head()

status_posts.head()

merged=pd.concat([photo_posts,status_posts])

merged.head()

sorted=df.sort_values(by='Page total likes')

sorted.head()

transposed=df.T

transposed.head()

melted=pd.melt(df,id_vars=['Type'],value_vars=['like','share'])

melted.head()

wide=melted_data.pivot_table(index='Type',

columns='variable',

values='value',

aggfunc='mean')

wide.head()