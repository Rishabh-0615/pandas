importpandasaspd

importmatplotlib.pyplotasplt

cols=['age','workclass','fnlwgt','education','education_num',

'marital_status','occupation','relationship','race',

'sex','capital_gain','capital_loss','hours_per_week',

'native_country','income']

df=pd.read_csv("Datasets/Adult/adult.csv",names=cols)

plt.hist(df['age'])

plt.title("Histogram")

plt.show()

df['income'].value_counts().plot(kind='pie',autopct='%1.1f%%')

plt.title("Pie Chart")

plt.ylabel("")

plt.show()

plt.boxplot(df['age'])

plt.title("Box Plot")

plt.show()

plt.scatter(df['age'],df['hours_per_week'])

plt.title("Scatter Plot")

plt.xlabel("Age")

plt.ylabel("Hours per week")

plt.show()

plt.scatter(df['age'],df['hours_per_week'])

plt.boxplot(df['hours_per_week'])

plt.title("Scatterplot with Boxplot")

plt.show()

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)

plt.scatter(df['age'],df['hours_per_week'])

plt.title("Scatter Plot")

plt.xlabel("Age")

plt.ylabel("Hours")

plt.subplot(1,2,2)

plt.boxplot(df['hours_per_week'])

plt.title("Box Plot")

plt.show()