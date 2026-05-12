importpandasaspd

importnumpyasnp

df=pd.read_csv(

"Datasets/Adult/adult.csv",

header=None

)

columns=[

"age","workclass","fnlwgt","education",

"education_num","marital_status","occupation",

"relationship","race","sex",

"capital_gain","capital_loss",

"hours_per_week","native_country",

"income"

]

df.columns=columns

print(df["income"].value_counts())

print("First 5 Rows:\n")

print(df.head())

df=df.replace("?",np.nan)

df=df.dropna()

print(df["income"].value_counts())

numeric_cols=df.select_dtypes(include=["number"]).columns

forcolinnumeric_cols:

    df=df[df[col]>=0]

print("\nAfter Cleaning:")

print(df.shape)

print(df["income"].value_counts())

forcolinnumeric_cols:

    Q1=df[col].quantile(0.25)

Q3=df[col].quantile(0.75)

IQR=Q3-Q1

lower=Q1-1.5*IQR

upper=Q3+1.5*IQR

df=df[

(df[col]>=lower)&

(df[col]<=upper)

]

print("\nAfter Outlier Removal:")

print(df.shape)

print(df["income"].value_counts())

fromsklearn.preprocessingimportLabelEncoder

fromsklearn.preprocessingimportStandardScaler

le=LabelEncoder()

cat_col=df.select_dtypes(include=["string","object","category"])

forcolincat_col:

    df[col]=le.fit_transform(df[col])

X=df.drop("income",axis=1)

y=df["income"]

scaler=StandardScaler()

X=scaler.fit_transform(X)

print(df["income"].value_counts())

fromsklearn.model_selectionimporttrain_test_split

X_train,X_test,y_train,y_test=train_test_split(

X,

y,

test_size=0.2,

random_state=42

)

fromsklearn.linear_modelimportLogisticRegression

fromsklearn.metricsimportaccuracy_score

lg=LogisticRegression(max_iter=1000)

lg.fit(X_train,y_train)

y_pred_lg=lg.predict(X_test)

print("\nLogistic Regression Accuracy:",

accuracy_score(y_test,y_pred_lg))

fromsklearn.naive_bayesimportGaussianNB

nb=GaussianNB()

nb.fit(X_train,y_train)

y_pred_nb=nb.predict(X_test)

print("Naive Bayes Accuracy:",

accuracy_score(y_test,y_pred_nb))