# 约瑟夫环的问题


# def move(man, step):
#     for i in range(step):
#         item = man.pop(0)
#         print(item)
#         man.append(item)
# man = [11, 12, 13, 14]
# step = 3
# move(man, step)
# print('-----')
# for i in man:
#     print(i)

# 输出：
# 11
# 12
# 13
# -----
# 14
# 11
# 12
# 13
# import io
# import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# def move(man, sep):
#     for i in range(sep):
#         item = man.pop(0)
#         man.append(item)


# def play(man=41, sep=3, rest=2):
#     print('总共%d个人每报数到第%d的人自杀，最后剩余%d个人' % (man, sep, rest))
#     man = [i for i in range(1, man + 1)]
#     print('玩家队列', man)
#     sep = sep - 1
#     while(len(man) > rest):
#         move(man, sep)
#         print('kill ', man.pop(0))
#         print(len(man))
#     return man


# if __name__ == '__main__':
#     survive = play()
#     print('最后活下来的是 ', survive)

def move(man, sep):
    for i in range(sep):
        item = man.pop(0)
        man.append(item)


def play(man=41, sep=3, rest=2):
    man = [i for i in range(1, man + 1)]
    print('总人数为', man)
    print('每报数为3的人去自杀，剩下2个人可以存活')
    sep -= 1
    while(len(man) > rest):
        move(man, sep)
        print('kill ', man.pop(0))
    return man


survive = play()
print(survive)
