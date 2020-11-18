import os
import pandas as pd
from matplotlib import pyplot as plt
import multiprocessing


def draw(country):
    for i in country:
        process = multiprocessing.Process(target=draw0, args=(i,))
        process.start()


def draw0(country):
    path = os.path.join('D:/', 'test', '疫情数据分析', 'data', country)
    path.encode('utf-8')
    data0 = pd.read_csv(path, index_col=0)
    x = list(data0.columns)
    index = list(data0.index)
    plt.figure(figsize=(20, 10), dpi=80)
    plt.title(country)
    for i in range(len(index)):
        plt.subplot(2, 2, 1 + i)
        plt.subplots_adjust(wspace=0.1, hspace=0.3, left=0.035, right=0.99, top=0.95, bottom=0.1)
        data1 = pd.Series(data0.loc[index[i], :])
        plt.plot(x, data1.values)
        plt.grid(alpha=0.4)
        plt.xticks(rotation=90)
        plt.xlabel('日期')
        plt.ylabel('人数')
        plt.title(country + index[i])
    plt.show()


def draw1(trend):
    path = os.path.join('D:/', 'test', '疫情数据分析', 'data', trend)
    path.encode('utf-8')
    data0 = pd.read_csv(path, index_col=0)
    x = list(data0.columns)
    index = list(data0.index)
    plt.figure(figsize=(20, 10), dpi=80)
    plt.title(trend)
    for i in range(len(index)):
        data1 = pd.Series(data0.loc[index[i], :])
        plt.plot(x, data1.values)
        plt.grid(alpha=0.4)
        plt.xticks(rotation=90)
        plt.xlabel('日期')
        plt.ylabel('人数')
    plt.legend(index)
    plt.show()


def draw2(state):
    path = os.path.join('D:/', 'test', '疫情数据分析', 'data', state)
    path.encode('utf-8')
    data0 = pd.read_csv(path, index_col=0)
    data0.fillna(value=0, inplace=True)
    data0.plot(kind='bar', figsize=(20, 10))
    plt.show()


def draw3(country):
    database0 = list()
    database1 = list()
    for i in country:
        path = os.path.join('D:/', 'test', '疫情数据分析', 'data', i)
        path.encode('utf-8')
        database0.append(pd.read_csv(path, index_col=0))
    index = list(database0[0].index)
    for i in range(len(country)):
        database0[i].index = [country[i] for j in range(len(index))]
    tmp = list()
    plt.figure(figsize=(20, 10), dpi=80)
    plt.subplots_adjust(wspace=0.1, hspace=0.3, left=0.035, right=0.99, top=0.95, bottom=0.1)
    for i in range(len(index)):
        tmp.clear()
        for j in range(len(database0)):
            tmp.append(database0[j].iloc[i])
        tmp = pd.concat(tmp, axis=1, join='outer', sort=True)
        tmp.fillna(method='ffill', inplace=True)
        index_list = list(map(str, list(tmp.index)))
        index_list.sort(key=lambda a: (int(a[0]), int(a[2:])))
        tmp = tmp.reindex(index_list)
        database1.append(tmp.T)
        tmp = list()
    x = list(database1[0].columns)
    for i in range(len(index)):
        plt.subplot(2, 2, 1 + i)
        for j in range(len(database1[i].index)):
            tmp0 = pd.Series(database1[i].loc[list(database1[i].index)[j], :])
            plt.plot(x, tmp0)
        plt.grid(alpha=0.4)
        plt.xticks(rotation=90)
        plt.xlabel('日期')
        plt.ylabel('人数')
        plt.title(index[i])
        plt.legend(list(database1[i].index))
    plt.show()


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
filename_list0 = set(os.listdir(r'D:\test\疫情数据分析\data'))
filename_list1 = {'allForeignTrend', 'trend'}
filename_list2 = {'北美洲', '大洋洲', '非洲', '南美洲', '亚洲', '欧洲'}
filename_list3 = {'其他', '热门', 'desktop.ini'}
filename_list0 = filename_list0 - filename_list1 - filename_list2 - filename_list3


if __name__ == '__main__':
    name = input()
    if name in filename_list0:
        draw0(name)
    elif name in filename_list1:
        draw1(name)
    elif name in filename_list2:
        draw2(name)
    else:
        draw3(name.split())
