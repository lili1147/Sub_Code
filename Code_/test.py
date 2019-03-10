# 随机数据生成器
# from random import randrange, choice
# # generateor
# from string import ascii_lowercase as lc
# from time import ctime

# tlds = ['edu', 'com', 'net', 'cn']
# for i in range(5, 11):
#     maxint = randrange(2**32)
#     time_str = ctime(maxint)
#     name_len = randrange(4, 8)
#     name_str = ''.join(choice(lc) for j in range(name_len))
#     web_str = ''.join(choice(tlds))
#     print('%s::%s@%s' % (time_str, name_str, web_str))


# 2019/3/7

a = [1, 2, 3]
b = [3, 2, 1]
c = a
a = b
b = c
print(a)
