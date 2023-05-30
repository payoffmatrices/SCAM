import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
from scipy import stats
from statsmodels.stats.outliers_influence import variance_inflation_factor

df = pd.read_csv('sanctionset.csv')
print(df.head())
print(df.describe())

X = df[['x1', 'x2', 'x3', 'x4']]
vif = pd.DataFrame()
vif["variables"] = X.columns
vif["VIF"] = [variance_inflation_factor(X.values, i) for i in 
range(X.shape[1])]
print(vif)

model3 = smf.ols('y ~ x1 + x2 + x3 + x4', data=df).fit()
print(model3.summary())

dw = sm.stats.stattools.durbin_watson(model3.resid)
print(f'Durbin-Watson statistic: {dw}')

names = ['Lagrange multiplier statistic', 'p-value',
        'f-value', 'f p-value']
bp = sm.stats.diagnostic.het_breuschpagan(model3.resid, model3.model.exog)
print(f'Breusch-Pagan test:\n {list(zip(names, bp))}')

names = ['Jarque-Bera', 'Chi^2 two-tail prob.', 'Skew', 'Kurtosis']
jb = sm.stats.stattools.jarque_bera(model3.resid)
print(f'Jarque-Bera test:\n {list(zip(names, jb))}')

ci = model3.conf_int()
print('Confidence intervals:')
print(ci)

