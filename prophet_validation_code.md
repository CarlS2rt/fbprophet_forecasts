## Cross-validation code

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

------

## Updated code with SQL connection

```python
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
from prophet import Prophet
from openpyxl.workbook import Workbook
from matplotlib import pyplot as plt
from prophet.plot import plot_plotly, plot_components_plotly
import plotly.express as px
from prophet.diagnostics import cross_validation
from prophet.diagnostics import performance_metrics
from prophet.plot import plot_cross_validation_metric
import cx_Oracle
from config import oracle_wfm_key
import cx_Oracle
import time
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.types import String
import ipynbname
file = ipynbname.name()
output_path=r'\\Tds\Metrocom\Contact Center\Workforce Management\Forecasting Models\Forecast Outputs\\'
```

```python
fig.write_image(f'outputs/{file}.png')
fig.write_image(f'{output_path}/{file}.png')
fig.write_html(f'outputs/{file}.html',include_plotlyjs="cdn")
fig.write_html(f'{output_path}/{file}.html',include_plotlyjs="cdn")
forecast.to_excel(f'outputs/{file}.xlsx')
forecast.to_excel(f'{output_path}/{file}.xlsx')
```

```python
# open database connection

DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'
USERNAME = 'CCO_WFM' #enter your username
PASSWORD = oracle_wfm_key #enter your password
HOST = 'RACPRD06.TDS.LOCAL' #enter the oracle db host url
PORT = 1521 # enter the oracle port number
SERVICE = 'DB070' # enter the oracle db service name
ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE

ODS = create_engine(ENGINE_PATH_WIN_AUTH)
print('Oracle Connected')
```

```python
# add filename as column
parts = file.split('_weekly')
team = parts[len(parts)-2].split('.')[0]
forecast['Team'] = team

# determine last row
last_row = forecast['ds'].max()
end_date = f"'{last_row}'"

# remove duplicate rows before insert
delete = f'''DELETE FROM
                    "CCO_WFM"."Forecasts_Monthly" "A1"
                WHERE
                    "A1"."Team" = '{team}'
                    
                    AND "A1"."DS" <= TO_DATE({end_date},'YYYY-MM-DD HH24:MI:SS')'''

with ODS.begin() as conn:
    conn.execute(delete)
```

```python
# Import forecast to database
rows_imported = 0
start_time = time.time()

cols = forecast.dtypes[forecast.dtypes=='object'].index
type_mapping = {col : String(100) for col in cols }

print(f'importing rows {rows_imported} to {rows_imported + len(forecast)}...', end='')
forecast.to_sql('Forecasts_Monthly',ODS,schema='CCO_WFM',if_exists='append',dtype=type_mapping)
rows_imported += len(df)

end_time = time.time() - start_time
print(f'Done. {end_time} total seconds have elapsed.')
```

