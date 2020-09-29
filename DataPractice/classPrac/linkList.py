# - * - coding:utf8 - * -
import  os

class  Node(object):

    def  __init__(self, data, next_=None):

        self.data = data
        self.next = next_

def  reverselinkList(nodeList):

     print  "nodeList",nodeList.data
     if  nodeList==None  or  nodeList.next==None:
         return  nodeList

     pre= None
     next= None
     while(nodeList!=None):

         next=nodeList.next
         nodeList.next= pre
         pre= nodeList
         nodeList= next

     return pre

if   __name__=='__main__':

    head = Node(3)
    head.next=Node(5)
    head.next.next = Node(7)
    print  "head.next.next.next",head.next.next.next

    result= None
    result= reverselinkList(head)

    #temp = result.data
    #print  temp

    while(result!=None):
        print  result.data
        result = result.next