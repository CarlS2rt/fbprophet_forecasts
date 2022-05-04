```python
# create cross-validation df
df_cv = cross_validation(m, initial='104 W', period='4 W', horizon = '52 W')
df_cv.head()
```

```python
# create performance metrics df
df_p = performance_metrics(df_cv)
df_p.head()
```

```python
# plot cross-validation
fig = plot_cross_validation_metric(df_cv, metric='mape')
```

```python
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
from prophet import Prophet
from openpyxl.workbook import Workbook
from matplotlib import pyplot as plt
from prophet.diagnostics import cross_validation
from prophet.diagnostics import performance_metrics
from prophet.plot import plot_cross_validation_metric
```