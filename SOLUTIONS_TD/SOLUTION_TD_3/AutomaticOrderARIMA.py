
#===================================================
#Code for identifying the parameters with smallest AIC
#===================================================

from pandas import read_excel
from statsmodels.tsa.arima_model import ARIMA
import warnings
import itertools

series = read_excel('priceData.xlsx', sheet_name='Data')
series = series.dropna()
#define the p, d and q parameters to take any value between 0 and 2
p = d = q = range(0, 3)

#generate all different combinations of p, q and q triplets
pdq = list(itertools.product(p, d, q))

#indentification of best model from different combinations of pdq
warnings.filterwarnings("ignore") # specify to ignore warning messages
best_score, best_param = float("inf"), None
bestResults = None
for param in pdq:
        try:
            mod = ARIMA(series['Y'], param)
            results = mod.fit()
            if results.aic < best_score:
                best_score, best_param = results.aic, param
                bestResults = results
            print('ARIMA{} - AIC:{}'.format(param, results.aic))
        except:
            continue
print('The best model is ARIMA{} - AIC:{}'.format(best_param, best_score))
print(bestResults.summary())
fig = bestResults.plot_predict()
fig.show()