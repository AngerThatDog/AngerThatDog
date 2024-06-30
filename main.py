# -- coding: utf-8 --
# !/usr/bin/python3
import keyword
import random


def ls_key1(): # 打印保留字
    print('保留字：', keyword.kwlist)


def number_type(): # 数字类型Number
    a = 1
    b = 1.23
    print('整数：', a, '布尔型：', a == 1, '浮点型：', b, '复数：', '1 + 2j')


def str_dd():   # 字符串操作
    str1 = 'this is a string'
    str2 = 'want to print'
    print('换行输出：\n', 'this is a string \n want to print') # \转义，\n换行
    print('使用r阻止转义：\n', r'this is a string \n want to print') # r反转义，不让转义字符起作用
    print('使用+连接字符串：\n', str1 + ' ' + str2) # 使用+连接字符串
    print('使用*2打印2次：\n', str1*2) # 使用*2打印2次
    print('[0:-1]从第一位到倒数第二位\n', str1[0:-1])    # 索引，从左往右以0开始，从右往左以-1开始
    print('[2:]从第三位到最后一位\n', str1[2:])    # 输出第三个到最后一个字符
    print('[0:-2]从第一位到倒数第三位\n', str1[:-2])  # 輸出第一位到倒数第三位
    # 字符串反转
    # python列表截取可以接收3个参数，[-1::-1]
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    str3 = str1[-1::-1]
    print(str1, '翻转过来是：\n', str3)   # 字符串反转


def user_input():    # 等待用户输入
    input('\n\n按下enter键后退出')


def dog_age():  # if条件判断
    age = int(input('请输入你家狗狗的年龄：'))
    print('') # 输出一个空行
    if age <= 0:
        print('胡说八道！')
    elif age == 1:
        print('狗狗年龄', age, '相当于14岁的人。')
    elif age == 2:
        print('狗狗年龄', age, '相当于22岁的人。')
    elif age > 2:
        human = 22 + (age - 2) * 5
        print('狗狗年龄', age, '相当于', human, '岁的人。')


def no_new_line():    # 输出不换行
    print('换行输出a、b')
    print('a')
    print('b')
    print('不换行输出c、d')
    print('c', end='')
    print('d', end='')


def multiple_variable_assignments():    # 多个变量同时赋值
    a = b = c = 1
    l, m, n = 1, 1, 1
    print('a = l:', a == l)
    print('b = m:', b == m)
    print('c = n:', c == n)


def judge_datatype():    # 判断数据类型
    a = 1
    print('a = 1, a的数据类型是：', type(a))
    print('a = 1, a的数据类型是：', isinstance(a, int))


def data_operation():   # 数据计算
    # 运算
    print('加法：', '10 + 3 =', 10 + 3)
    print('减法：', '10 - 3 =', 10 - 3)
    print('乘法：', '10 * 3 =', 10 * 3)
    print('n次方：', '10 ** 3 =', 10 ** 3)
    print('除法：', '10 / 3 =', 10 / 3)
    print('除法取余：', '10 % 3 =', 10 % 3)
    print('除法取整：', '10 // 3 =', 10 // 3)
    

def list_dd():  # 列表
    longlist = [123, 'abdef', 'runoob', 2.24, [1, 2, 3]]
    tinylist = ['123', 456, 'dhr',]
    print('输出longlist:\n', longlist)    # 输出longlist
    print('输出tinylist:\n', tinylist)    # 输出tinylist
    print('输出tinylist第二个元素:\n', tinylist[1])    # 输出tinylist第二个元素
    print('输出longlist第二个到第三个元素:\n', longlist[1:3])    # 输出longlist第二个到第三个元素
    print('tinylist输出两次\n:', tinylist * 2)    # tinylist输出两次
    print('合并list:\n', tinylist + longlist)    # 合并list
    longlist[0] = 'gas' # list第一个元素改变
    print('改变longlist第一个元素\n', longlist)
    longlist[2:4] = [] # list去掉第三个到第四个元素
    print('去掉longlist第三个到第四个元素\n', longlist)


def tuple_dd(): # 元组
    longtuple = (123, 'abcdef', 'runoob', 2.24, [1, 2, 3])
    tinytuple = ('123', 456, 'mnp')
    print('输出元组longtuple：', longtuple)    # 输出元组longtuple
    print('输出元组tinytuple：', tinytuple)    # 输出元组tinytuple
    print('输出元组longtuple第一个元素: ', longtuple[0])    # 输出元组longtuple第一个元素
    print('输出元组longtuple第二个到第三个元素: ', longtuple[1:3])    # 输出元组longtuple第二个到第三个元素
    print('输出元组longtuple第二个到最后一个元素:', longtuple[1:])    # 输出元组longtuple第二个到最后一个元素
    print('输出两次元组longtuple:', longtuple * 2)    # 输出两次元组longtuple
    print('连接元组：', longtuple + tinytuple)    # 连接元组
    # tinytuple[0] = 1    # 元组的元素不能修改，会报错


def set_dd():   # 集合
    longset = {123, 'abcdef', 'runoob', 2.24, 123, "print"}
    tinyset = {'123', 456, 'mnp', 'runoob'}
    print('输出集合longset：', longset, '\n *重复的会自动去除')    # 输出集合longset，重复的会去除
    if 'rose' in longset:    # 成员测试
        print('rose在集合', longset, '中')
    else:
        print('rose不在集合', longset, '中')

    print('差集：longset - tinyset:\n', longset - tinyset)    # 集合运算
    print('并集：longset | tinyset:\n', longset | tinyset)
    print('交集：longset & tinyset:\n', longset & tinyset)
    print('不同时存在的元素：longset ^ tinyset:\n', longset ^ tinyset)


def dict_dd():  # 字典
    dict1 = {}
    tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.baidu.com'}
    print('输出字典dict:', dict1)
    print('输出字典tinydict:', tinydict)
    print('输出字典tinydict的key:', tinydict.keys())
    print('输出字典tinydict的value:', tinydict.values())


def type_change():  # 数据类型变更
    print('1.3转换为整形是：', int(1.3))    # int(x [,base])：将x转换为一个整数
    print('1转换为浮点型是：', float(1))    # float(x)： 将x转换到一个浮点数
    print('创建一个复数：', complex(1))    # complex(x)：创建一个复数
    print('12转换成字符串：', str(12))    # str(x)：将对象 x 转换为字符串
    print('1+2转换成表达式字符串：', repr(12))    # repr(x)：将对象 x 转换为表达式字符串
    # eval(str)：用来计算在字符串中的有效Python表达式,并返回一个对象
    x = 'this is a to print'
    print('转换成元组：', end=''), print(tuple(x))    # tuple(s)：将序列 s 转换为一个元组
    print('转换成列表：', end=''), print(list(x))    # list(s)：将序列 s 转换为一个列表
    print('转换成集合：', end=''), print(set(x))    # set(s)：转换为可变集合
    # dict(d)：创建一个字典。d 必须是一个 (key, value)元组序列。
    print('转换成不可变集合：', end=''), print(frozenset(x))    # frozenset(s)：转换为不可变集合
    print('整数(13842)转换成字符：', end=''), print(chr(13842))    # chr(x)：将一个整数转换为一个字符
    print('字符(s)转换成整数：', end=''), print(ord('s'))    # ord(x)：将一个字符转换为它的整数
    print('整数(13842)转换成十六进制：', end=''), print(hex(13842))    # hex(x)：将一个整数转换为一个十六进制字符串
    print('整数(13842)转换成八进制：', end=''), print(oct(13842))    # oct(x)：将一个整数转换为一个八进制字符串


list1 = []


def fibonacci():    # 斐波纳契数列
    a = 0
    b = 1
    while b < 100:
        # print(b, end=' ')
        list1.append(b)
        a, b = b, a + b
    return list1


def number_guess(): # 猜数字游戏
    random_number = random.randint(0, 100)
    guess = -1
    print('--猜-数-字-游-戏--')
    print('--目标数字在0-100之间--')
    while guess != random_number:
        guess = int(input('请输入你猜的数字：'))
        if guess == random_number:
            print('恭喜你！猜对了！')
        elif guess < random_number:
            print('猜的数字小了！')
        else:
            print('猜的数字大了！')


def number_plus():  # 计算1-100之和
    a = 0
    i = 1
    while i <= 100:
        a += i
        i += 1
    print('1到100之和为：', a)


def sites():    # for循环
    x = 1
    sit = ['Baidu', 'Google', 'Runoob', 'Taobao']
    for site in sit:
        if site == 'Runoob':
            print('菜鸟教程')
            break
        print('循环数据', end=''), print(x, ':', end=''), print(site)
        x = x + 1
    else:
        print('没有循环数据')
    print('完成循环')


def range1():    # 使用range()遍历数字序列
    for i in range(10):
        print(i, ' ', end='')
    print()
    for j in range(6, 10):
        print(j, ' ', end='')
    print()
    for m in fibonacci():
        print(m, ' ', end='')


# range1()
# ls_key1()
# number_type()
# str_dd()
# user_input()
# no_new_line()
# multiple_variable_assignments()
# judge_datatype()
# data_operation()
# list_dd()
# tuple_dd()
# set_dd()
# dict_dd()
# type_change()
# fibonacci()
# dog_age()
# number_guess()
# number_plus()
# sites()
