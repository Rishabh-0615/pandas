importpandasaspd

importnumpyasnp

df=pd.read_csv('Datasets/Iris/Iris.csv')

df.columns=[

"SepalLength",

"SepalWidth",

"PetalLength",

"PetalWidth",

"Species"

]

df.head()

df=df.dropna()

df=df.replace("?",np.nan)

df=df.dropna()

numeric_col=df.select_dtypes(include="number").columns

forcolinnumeric_col:

    df=df[df[col]>=0]

df.head()

forcolinnumeric_col:

    Q1=df[col].quantile(0.25)

Q3=df[col].quantile(0.75)

IQR=Q3-Q1

lower=Q1-1.5*IQR

upper=Q3+1.5*IQR

df=df[df[col]>=lower]

df=df[df[col]<=upper]

df.head()

fromsklearn.preprocessingimportLabelEncoder

fromsklearn.preprocessingimportStandardScaler

le=LabelEncoder()

df["Species"]=le.fit_transform(df["Species"])

df.head()

x=df.drop("Species",axis=1)

y=df["Species"]

scaler=StandardScaler()

x=scaler.fit_transform(x)

fromsklearn.model_selectionimporttrain_test_split

fromsklearn.linear_modelimportLogisticRegression

fromsklearn.naive_bayesimportGaussianNB

fromsklearn.metricsimportaccuracy_score

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

lg=LogisticRegression()

lg.fit(x_train,y_train)

y_pred_lg=lg.predict(x_test)

print("Accuracy of LogisticRegression is: ",accuracy_score(y_test,y_pred_lg))

nb=GaussianNB()

nb.fit(x_train,y_train)

y_pred_nb=nb.predict(x_test)

print("Accuracy of GaussianNB is: ",accuracy_score(y_test,y_pred_nb))