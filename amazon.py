import pandas_datareader.data as web
import matplotlib.pyplot as plt

# collect data for Amazon from 2017-04-22 to 2018-04-22
start = '2017-04-22'
end = '2018-04-22'
symbol='AMZN'
df = web.DataReader('AMZN', 'yahoo', start=start, end=end)
#df.index = df.index.
print(df)
df.to_csv("amazon.csv")

# select only close column
close = df[['Close']]
# rename the column with symbole nameß
close = close.rename(columns={'Close': symbol})
ax = close.plot(title='Amazon')
ax.set_xlabel('date')
ax.set_ylabel('close price')
ax.grid()
#plt.show()
plt.savefig('books_read.png')

