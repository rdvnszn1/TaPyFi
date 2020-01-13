from tapyfi.OHLCObject import OHLCObject
import pandas as pd
from tapyfi.Indicators.RSI import RSI

Data= pd.read_csv('tapyfi/Test/AAPL.csv')

MyObject= OHLCObject(Data.Date,Data.Open,Data.High,Data.Low,Data.Close,Data.Volume)


rdvnboun34