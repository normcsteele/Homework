

```python
import os
import csv
import pandas as pd
```


```python
measure = "hawaii_measurements.csv"
station = "hawaii_stations.csv"
measure_df = pd.read_csv(measure)
station_df = pd.read_csv(station)
```


```python
measure_df.count()
```




    station    19550
    date       19550
    prcp       18103
    tobs       19550
    dtype: int64




```python
measure_df['prcp'].fillna(value=0, inplace = True)
measure_df.count()
```




    station    19550
    date       19550
    prcp       19550
    tobs       19550
    dtype: int64




```python
measure_df.to_csv("clean.hawaii_measurements.csv", index=False)
```
