import pandas as pd
import numpy as np

#set your files and location
path = '/Users/Shared/path/'
left = 'file1.csv'
right = 'file2.csv'

#load the files as dataframes in pandas
dfLeft = pd.read_csv(path + left, sep=',', index_col=False)
dfRight = pd.read_csv(path + right, sep=',', index_col=False)

#disaply the top rows if yo uwant to check the data uncomment
#dfLeft.head(n=5)
#dfRight.head(n=5)

#do a join on a common field and output to csv
output = dfLeft.merge(dfRight,how='inner', on='common-field-name',suffixes=('_x','_y'))
output.to_csv('output.csv',index=False)
