'''
对数据进行处理，替代人的手工操作。
本次处理数据的例子是牲畜的养殖量的变化。
'''
import csv

f = open('pig_data.csv', 'r', encoding='gbk')
reader = csv.reader(f)
province = f.readline()
province = province.split(',')
print(province)

f2 = open('new_pig.csv', 'w', encoding='gbk', newline='')
writer = csv.writer(f2)
writer.writerow(['name', 'type', 'value', 'date'])

for line in reader:
    for i in range(1, 32):
        if line[i]:
            writer.writerow([province[i], '', line[i], line[0]])
