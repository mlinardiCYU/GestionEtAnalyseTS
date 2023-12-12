from pandas import read_excel
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.tsatools import detrend
from matplotlib import pyplot

series = read_excel('priceData.xlsx', sheet_name='Data')
series = series.dropna()
# Time, ACF, and PACF plots for original data

detrendY = detrend(series['Y'],order=1, axis=0)

seriesToUse = detrendY

pyplot.plot(seriesToUse)
pyplot.title('Time plot AR1 data')
plot_acf(seriesToUse, title='ACF of series Y (price data)', lags=20)
plot_pacf(seriesToUse, title='PACF of series Y (price data)', lags=20)
pyplot.show()
