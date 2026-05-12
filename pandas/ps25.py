importpandasaspd

importnumpyasnp

df=pd.read_csv('Datasets/Hepatitis/hepatitis.csv')

df.columns=[

'class','age','sex','steroid','antivirals','fatigue','malaise','anorexia','liverbig','liverfirm','spleenpalpable','spiders','ascites','varices','bilirubin','alkphosphate','sgot','albumin','protime','histology'

]

df.head()

df['bilirubin']=pd.to_numeric(df['bilirubin'],errors='coerce')

df['albumin']=pd.to_numeric(df['albumin'],errors='coerce')

male=df[df['sex']==1]

female=df[df['sex']==2]

male.head()

female.head()

merged=pd.concat([male,female])

merged.head()

merged.tail()

sorted=df.sort_values(by=['age','sgot','protime'])

sorted.head()

transposed=df.T

transposed.head()

melted=pd.melt(df,id_vars=['sex'],value_vars=['bilirubin','albumin'])

melted.head()

wide_data=melted.pivot_table(index='sex',

columns='variable',

values='value',

aggfunc='mean')

wide_data.head()