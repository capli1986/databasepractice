# -*- coding:utf8 -*-

import copy
def copyDeep():

    #浅拷贝是拷贝引用，下面例子中，l2是l1的浅拷贝，只是l1中的第五个元素是列表，它是可变长度的，下面的浅拷贝只是拷贝了该元素的引用，我们在l1中修改该
    #元素的值，但是该元素的地址并没有改变，所以l2中引用的地址没有改变，导致l2中的值也被修改
    l1= [1,2,3,5,[1,2]]
    l2= copy.copy(l1)
    #l1[4].append(3)  这个操作可以使得l2的第五个变量也跟着改变
    l1.append(6)  ##这个操作不会导致l2的值改变


    print "浅拷贝结果l2",l2

    l3 = [1, 2, 3, 5, [1, 2]]
    l4 = copy.deepcopy(l3)
    #l3[4].append(3)
    l3.append(6)


    print "深拷贝结果l4", l4

copyDeep()