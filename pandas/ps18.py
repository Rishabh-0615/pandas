importpandasaspd

importmatplotlib.pyplotasplt

cols=['age','sex','cp','trestbps','chol','fbs','restecg',

'thalach','exang','oldpeak','slope','ca','thal','target']

df=pd.read_csv("Datasets/HeartDisease/Cleavland.csv",

names=cols)

plt.hist(df['age'])

plt.title("Histogram of Age")

plt.show()

df['target'].value_counts().plot(kind='pie',autopct='%1.1f%%')

plt.title("Pie Chart")

plt.ylabel("")

plt.show()

plt.boxplot(df['chol'])

plt.title("Box Plot")

plt.show()

plt.scatter(df['age'],df['chol'])

plt.title("Scatter Plot")

plt.xlabel("Age")

plt.ylabel("Cholesterol")

plt.show()

plt.scatter(df['age'],df['chol'])

plt.boxplot(df['chol'])

plt.title("Scatter Plot with Box Plot")

plt.show()