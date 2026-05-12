importpandasaspd

importmatplotlib.pyplotasplt

cols=['age','workclass','fnlwgt','education','education_num',

'marital_status','occupation','relationship','race',

'sex','capital_gain','capital_loss','hours_per_week',

'native_country','income']

df=pd.read_csv("Datasets/Adult/adult.csv",names=cols)

plt.hist(df['age'])

plt.title("Histogram of Age")

plt.xlabel("Age")

plt.ylabel("Frequency")

plt.show()

plt.plot(df['fnlwgt'],'.')

plt.title("Dot Plot")

plt.show()

df['education'].value_counts().plot(kind='bar')

plt.title("Bar Plot")

plt.show()

plt.plot(df['hours_per_week'])

plt.title("Line Chart")

plt.show()

plt.boxplot(df['age'])

plt.title("Box Plot")

plt.show()

plt.hist(df['age'])

plt.title("Histogram")

plt.show()

plt.scatter(df['age'],df['hours_per_week'])

plt.title("Scatter Plot")

plt.show()