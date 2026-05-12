importpandasaspd

importmatplotlib.pyplotasplt

cols=['age','sex','cp','trestbps','chol','fbs','restecg',

'thalach','exang','oldpeak','slope','ca','thal','target']

df=pd.read_csv("Datasets/HeartDisease/Cleavland.csv",

names=cols)

plt.hist(df['age'])

plt.title("Histogram of Age")

plt.xlabel("Age")

plt.ylabel("Frequency")

plt.show()

plt.plot(df['chol'],'.')

plt.title("Dot Plot of Cholesterol")

plt.xlabel("Index")

plt.ylabel("Cholesterol")

plt.show()

df['cp'].value_counts().plot(kind='bar')

plt.title("Bar Plot of Chest Pain Type")

plt.xlabel("Chest Pain Type")

plt.ylabel("Count")

plt.show()

plt.plot(df['trestbps'])

plt.title("Line Chart of Resting Blood Pressure")

plt.xlabel("Index")

plt.ylabel("Blood Pressure")

plt.show()

plt.scatter(df['age'],df['chol'])

plt.title("Scatter Plot of Age vs Cholesterol")

plt.xlabel("Age")

plt.ylabel("Cholesterol")

plt.show()

plt.boxplot(df['chol'])

plt.title("Box Plot of Cholesterol")

plt.ylabel("Cholesterol")

plt.show()

plt.hist(df['age'])

plt.title("Histogram of Age")

plt.xlabel("Age")

plt.ylabel("Frequency")

plt.show()