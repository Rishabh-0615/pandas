importpandasaspd

importnumpyasnp

df=pd.read_csv("Datasets/Hepatitis/hepatitis.csv",header=None)

df.columns=[

"class","age","sex","steroid","antivirals","fatigue","malaise","anorexia","liverbig","liverfirm","spleenpalpable","spiders","ascites","varices","bilirubin","alkphosphate","sgot","albumin","protime","histology"

]

print(df.shape)

df.head()

print(df["class"].value_counts())

df=df.replace("?",np.nan)

df=df.apply(pd.to_numeric)

df=df.dropna()

print(df.shape)

print(df["class"].value_counts())

df.head()

numeric_col=df.select_dtypes(include="number").columns

forcolinnumeric_col:

    df=df[df[col]>=0]

print(df.shape)

print(df["class"].value_counts())

df.head()

print(df.shape)

df.head()

print(df["class"].value_counts())

fromsklearn.preprocessingimportStandardScaler

x=df.drop("class",axis=1)

y=df["class"]

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

print("Accuracy of Logistic Regression is: ",accuracy_score(y_pred_lg,y_test))

nb=GaussianNB()

nb.fit(x_train,y_train)

y_pred_nb=nb.predict(x_test)

print("Accuracy of GaussianNB is: ",accuracy_score(y_pred_nb,y_test))