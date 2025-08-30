from collections import deque as dq
import copy
class uppts:
    __ciuva__ = []
    def roof(self,item,maxits):
        self.maxits = copy.copy(maxits)
        ditem = dq(self.__ciuva__)
        if self.__ciuva__.__len__() >= maxits:
            ditem.popleft()
            self.__ciuva__ = ditem
        
        self.__ciuva__.append(item)
    
    def part(self):
        return self.__ciuva__   
    
    def cls(self):
        self.__ciuva__.clear()
        
    def maxmin(self):
        mx = max(self.__ciuva__)
        mn = min(self.__ciuva__)
        indx_max = self.__ciuva__.index(mx)
        indx_min = self.__ciuva__.index(mn)
        return (indx_max,mx),(indx_min,mn)
    
    def middle_dt(self):
        y = sum(self.__ciuva__)/self.__ciuva__.__len__()
        knok = []
        for i in self.__ciuva__:
            knok.append(y)
        return knok
