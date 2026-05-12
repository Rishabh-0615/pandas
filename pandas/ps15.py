importpandasaspd

importnumpyasnp

df=pd.read_csv("Datasets/BreastCancer/BreastCancerWc.csv",header=None)

columns=[

"id","ClumpThickness","UniformityCellSize",

"UniformityCellShape","MarginalAdhesion",

"SingleEpithelialCellSize","BareNuclei",

"BlandChromatin","NormalNucleoli",

"Mitoses","Class"

]

df.columns=columns

print(df.head())

df.replace("?",np.nan,inplace=True)

df=df.apply(pd.to_numeric)

df.dropna(inplace=True)

numeric_cols=df.select_dtypes(include=["number"]).columns

forcolinnumeric_cols:

    df=df[df[col]>=0]

print("\nAfter Cleaning:")

print(df.shape)

print("\nClass Distribution:")

print(df["Class"].value_counts())

fromsklearn.preprocessingimportStandardScaler

X=df.drop("Class",axis=1)

y=df["Class"]

scaler=StandardScaler()

X=scaler.fit_transform(X)

fromsklearn.model_selectionimporttrain_test_split

X_train,X_test,y_train,y_test=train_test_split(

X,y,

test_size=0.2,

random_state=42,

stratify=y

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