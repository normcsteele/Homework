

```python
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as dt
import numpy as np
import pandas as pd
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String, Float, Text, Date
import pymysql
pymysql.install_as_MySQLdb()
```


```python
cleaned_df = pd.read_csv("clean.hawaii_measurements.csv")
station_df = pd.read_csv("hawaii_stations.csv")
data = station_df.to_dict(orient='records')
station_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>station</th>
      <th>name</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>elevation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>USC00519397</td>
      <td>WAIKIKI 717.2, HI US</td>
      <td>21.2716</td>
      <td>-157.8168</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>USC00513117</td>
      <td>KANEOHE 838.1, HI US</td>
      <td>21.4234</td>
      <td>-157.8015</td>
      <td>14.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USC00514830</td>
      <td>KUALOA RANCH HEADQUARTERS 886.9, HI US</td>
      <td>21.5213</td>
      <td>-157.8374</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>USC00517948</td>
      <td>PEARL CITY, HI US</td>
      <td>21.3934</td>
      <td>-157.9751</td>
      <td>11.9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>USC00518838</td>
      <td>UPPER WAHIAWA 874.3, HI US</td>
      <td>21.4992</td>
      <td>-158.0111</td>
      <td>306.6</td>
    </tr>
  </tbody>
</table>
</div>




```python
engine = create_engine("sqlite:///hawaii.sqlite", echo=False)
conn = engine.connect()
```


```python
class Station(Base):
    __tablename__ = 'stations'
    
    id = Column(Integer, primary_key=True)
    station = Column(Text)
    name = Column(Text)
    latitude = Column(Float)
    longitude = Column(Float)
    elevation = Column(Float)
    
class Measurement(Base):
    __tablename__ = 'measurements'
    
    id = Column(Integer, primary_key=True)
    station = Column(Text)
    date = Column(Date)
    prcp = Column(Float)
    tobs = Column(Integer)
```

    C:\Users\Norman\Anaconda3\lib\site-packages\sqlalchemy\ext\declarative\clsregistry.py:120: SAWarning: This declarative base already contains a class with the same class name and module name as __main__.Station, and will be replaced in the string-lookup table.
      item.__name__
    


    ---------------------------------------------------------------------------

    InvalidRequestError                       Traceback (most recent call last)

    <ipython-input-30-cec0309096e7> in <module>()
    ----> 1 class Station(Base):
          2     __tablename__ = 'stations'
          3 
          4     id = Column(Integer, primary_key=True)
          5     station = Column(Text)
    

    ~\Anaconda3\lib\site-packages\sqlalchemy\ext\declarative\api.py in __init__(cls, classname, bases, dict_)
         62     def __init__(cls, classname, bases, dict_):
         63         if '_decl_class_registry' not in cls.__dict__:
    ---> 64             _as_declarative(cls, classname, cls.__dict__)
         65         type.__init__(cls, classname, bases, dict_)
         66 
    

    ~\Anaconda3\lib\site-packages\sqlalchemy\ext\declarative\base.py in _as_declarative(cls, classname, dict_)
         86         return
         87 
    ---> 88     _MapperConfig.setup_mapping(cls, classname, dict_)
         89 
         90 
    

    ~\Anaconda3\lib\site-packages\sqlalchemy\ext\declarative\base.py in setup_mapping(cls, cls_, classname, dict_)
        114         else:
        115             cfg_cls = _MapperConfig
    --> 116         cfg_cls(cls_, classname, dict_)
        117 
        118     def __init__(self, cls_, classname, dict_):
    

    ~\Anaconda3\lib\site-packages\sqlalchemy\ext\declarative\base.py in __init__(self, cls_, classname, dict_)
        142         self._extract_declared_columns()
        143 
    --> 144         self._setup_table()
        145 
        146         self._setup_inheritance()
    

    ~\Anaconda3\lib\site-packages\sqlalchemy\ext\declarative\base.py in _setup_table(self)
        435                     tablename, cls.metadata,
        436                     *(tuple(declared_columns) + tuple(args)),
    --> 437                     **table_kw)
        438         else:
        439             table = cls.__table__
    

    ~\Anaconda3\lib\site-packages\sqlalchemy\sql\schema.py in __new__(cls, *args, **kw)
        436                     "to redefine "
        437                     "options and columns on an "
    --> 438                     "existing Table object." % key)
        439             table = metadata.tables[key]
        440             if extend_existing:
    

    InvalidRequestError: Table 'stations' is already defined for this MetaData instance.  Specify 'extend_existing=True' to redefine options and columns on an existing Table object.



```python
Base.metadata.create_all(engine)
```


```python
station_df.to_sql('stations', conn, dtype={'id': Integer(), 'station': Text(), 'name': Text(), 
                                        'latitude': Float(), 'longitude': Float(), 'elevation': Float()})
cleaned_df.to_sql('measurements', conn, dtype={'id': Integer(), 'station': Text(), 'date': Text(), 'prcp': Float(), 
                                                'tobs': Integer()})
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-20-539daa309701> in <module>()
          1 station_df.to_sql('stations', conn, dtype={'id': Integer(), 'station': Text(), 'name': Text(), 
    ----> 2                                         'latitude': Float(), 'longitude': Float(), 'elevation': Float()})
          3 cleaned_df.to_sql('measurements', conn, dtype={'id': Integer(), 'station': Text(), 'date': Text(), 'prcp': Float(), 
          4                                                 'tobs': Integer()})
    

    ~\Anaconda3\lib\site-packages\pandas\core\generic.py in to_sql(self, name, con, flavor, schema, if_exists, index, index_label, chunksize, dtype)
       1532         sql.to_sql(self, name, con, flavor=flavor, schema=schema,
       1533                    if_exists=if_exists, index=index, index_label=index_label,
    -> 1534                    chunksize=chunksize, dtype=dtype)
       1535 
       1536     def to_pickle(self, path, compression='infer',
    

    ~\Anaconda3\lib\site-packages\pandas\io\sql.py in to_sql(frame, name, con, flavor, schema, if_exists, index, index_label, chunksize, dtype)
        471     pandas_sql.to_sql(frame, name, if_exists=if_exists, index=index,
        472                       index_label=index_label, schema=schema,
    --> 473                       chunksize=chunksize, dtype=dtype)
        474 
        475 
    

    ~\Anaconda3\lib\site-packages\pandas\io\sql.py in to_sql(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype)
       1153                          if_exists=if_exists, index_label=index_label,
       1154                          schema=schema, dtype=dtype)
    -> 1155         table.create()
       1156         table.insert(chunksize)
       1157         if (not name.isdigit() and not name.islower()):
    

    ~\Anaconda3\lib\site-packages\pandas\io\sql.py in create(self)
        590         if self.exists():
        591             if self.if_exists == 'fail':
    --> 592                 raise ValueError("Table '%s' already exists." % self.name)
        593             elif self.if_exists == 'replace':
        594                 self.pd_sql.drop_table(self.name, self.schema)
    

    ValueError: Table 'stations' already exists.

