import pandas as pd

from os import listdir
from os.path import isfile, join

for i in range(2005, 2017):
    year = str(i)

    file_path = './' + year + '년_음주운전_월별데이터/'
    drink_per_month_data = [f for f in listdir(file_path) if isfile(join(file_path, f))]

    result = pd.DataFrame()
    for i in range(12):
        df_drink = pd.read_excel(file_path+drink_per_month_data[i], header=[0,1,2], index_col=[0,1,2])
        temp = df_drink.xs('합계', level=1, axis=1).xs('사고건수', level=2).sort_index()
        col_name = year + '.%02d' % (i+1)
        temp.columns=[col_name]
        result[col_name] = temp[col_name]

    result = result.fillna(0)
    result = result.astype('int')
    result = result.xs('합계', level=1)
    result.to_excel(year + '_월별_음주운전_사고건수.xls')