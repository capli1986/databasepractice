# -*-  coding:utf-8 -*-
import os

##冒泡排序
def  bubbleSorting(dataList):
    #dataList = [2,6,3,9,1]
    i = 0
    j = len(dataList)
    while (j>=0):
        i=0
        while(i<j-1):
            if  dataList[i]>dataList[i+1]:
                temp = dataList[i]
                dataList[i]=dataList[i+1]
                dataList[i+1]=temp
            i = i+1
        j = j-1

    print dataList

##插入排序
def  insertSorting(dataList):

    #dataList = [2, 6, 3, 10, 3, 9, 1]
    if  dataList != []:
        j = 1
        while( j <= len(dataList)- 1 ):
            i = 0
            while (i <= j):
                if dataList[i] > dataList[j]:
                    temp = dataList[i]
                    dataList[i] = dataList[j]
                    dataList[j] = temp
                i = i+1
            j = j+1
        print dataList

def  simselectSorting(dataList):
    '''简单选择排序Simple Selection Sort,又称为直接选择排序，它的基本操作是：通过n-i次关键字的比较，"
    "从n-i+1个关键字中选取最小的关键字，然后和第i个关键字交换，i=1,2,3,4...n-1"'''
    if  dataList==[] or len(dataList)==1:
        return dataList
    i= 0
    while(i<len(dataList)-2):
        j= i
        curTemp= j
        while(j<len(dataList)-1):
            if dataList[j+1]< dataList[curTemp]:
                curTemp = j + 1
            j = j + 1
        temp = dataList[curTemp]

        dataList[curTemp]=dataList[i]
        dataList[i] = temp

        i = i+1
    return  dataList

##快速排序
def  quickSorting(dataList):
    #dataList = [2, 6, 3, 10, 3, 9, 1]
    if  dataList != []:
        base = dataList[0]
        left = []
        right = []
        for  item  in  dataList[1:]:
            if  item<=base:
                left.append(item)
            else:
                right.append(item)
        return  quickSorting(left)+[base]+quickSorting(right)
    return []

##堆排序
def  heapSorting(dataList):
    '''小根堆排序'''
    dataList = [30,50,57,77,62,78,94,80,84]
    lenth = len(dataList)
    for  i  in  [lenth-1,0]:
        pass
if __name__ == '__main__':
    #print "hello world"
    dataList = [2, 6, 3, 10, 3, 9, 1]
    #BubbleSorting()
    #selectSorting()
    #resultList = quickSorting(dataList)
    #print resultList
    result=simselectSorting(dataList)
    print  result