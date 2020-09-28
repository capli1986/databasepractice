#   -*-   coding:utf-8   -*-

def findTarget(srcList, target):
    lenth = len(srcList)
    print  lenth
    print  "srcList",srcList
    if srcList == []:
        return False
    else:
        curLenth = lenth / 2
        print  "curLenth",curLenth,"target",target,"srcList[curLenth]",srcList[curLenth]
        if target == srcList[curLenth]:
            print  "hello"
            return True
        elif target < srcList[lenth / 2]:
            return findTarget(srcList[0:curLenth], target)
        else:
            return findTarget(srcList[(curLenth + 1):], target)

result = findTarget([1, 2, 3], 3)
print  "result",result

#class  stack():
 #   def  __int__(self):
  #      self.dataList=[]
   #     self.dataNum = 0

    #def  pop(self):
     #   if  self.dataList != []:
      #      return  self.dataList[-1]
       # else:
        #    return -1

    #def  add(self,newData):
     #   self.dataList.append(newData)