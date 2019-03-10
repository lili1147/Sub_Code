    '''
   DataFrame()

   output:
    cols
   a     1
   b     2
   c     3
   d     4
   e     5
      col1  col2  col3
   a     1     2     3
   b     4     5     6
      col1  col2
   0     1     2
   1     3     4
   '''

import pandas as pd
data = pd.DataFrame([1, 2, 3, 4, 5], columns=['cols'], index=['a', 'b', 'c', 'd', 'e'])
print(data)
data.to_csv('data.csv', mode='a', encoding='utf-8_sig')

data2 = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['col1', 'col2', 'col3'], index=['a', 'b'])
print(data2)

# 字典形式
data3 = pd.DataFrame({'col1': [1, 3], 'col2': [2, 4]})
print(data3)
data3.to_csv('data.csv', mode='a', encoding='utf-8_sig')

data4 = pd.DataFrame()
names = ['李黎', '何宇', '谭伟', '刘俊林']
gender = ['m', 'm', 'm', 'm']
data4['name'] = names
data4['gender'] = gender
data4.to_csv('data.csv', mode='a', encoding='utf-8_sig')
