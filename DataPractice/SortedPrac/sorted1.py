# -*-  coding:utf-8 -*-


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

##选择排序
def  selectSorting(dataList):

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
    resultList = quickSorting(dataList)
    print resultList