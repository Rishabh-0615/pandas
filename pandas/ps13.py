importpandasaspd

importnumpyasnp

df=pd.read_csv('Datasets/HeartDisease/Cleavland.csv')

df.columns=[

"age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal","num"

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

fromsklearn.preprocessingimportStandardScaler

x=df.drop("num",axis=1)

y=df["num"]

scaler=StandardScaler()

x=scaler.fit_transform(x)

fromsklearn.model_selectionimporttrain_test_split

fromsklearn.neighborsimportKNeighborsClassifier

fromsklearn.linear_modelimportLogisticRegression

fromsklearn.metricsimportaccuracy_score

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

lg=LogisticRegression(max_iter=1000)

lg.fit(x_train,y_train)

y_pred_lg=lg.predict(x_test)

print("Accuracy of LogisticRegression is: ",accuracy_score(y_pred_lg,y_test))

knn=KNeighborsClassifier(n_neighbors=2)

knn.fit(x_train,y_train)

y_pred_knn=knn.predict(x_test)

print("Accuracy of KNN is: ",accuracy_score(y_pred_knn,y_test))