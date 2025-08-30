# modir amel, heat modireh, tahghighat, tolidat

from random import randint as rt
from random import choice as ch
class Scource:
    def impment(self):
        self.mdam = []
        self.hemo = []
        self.tahg = []
        self.toli = []
        self.mdam_= "00000010101"
        self.hemo_= "00000010101"
        self.tahg_= "00000010101"
        self.toli_= "00000010101"
        self.bank = []
        self.plday = {}
        self.sdy = 0
        
    def proxy(self):
        isp = ch(list(self.mdam_))
        if isp == '0':
            catch = rt(100,1000)
            self.mdam.append(catch)
            self.plday[f'{self.sdy}pl'].append(catch)
            self.bank.append(catch)
            
        elif isp == '1':
            catch = rt(100,1000)
            self.mdam.append(catch*-1)
            self.plday[f'{self.sdy}pl'].append(catch*-1)
            self.bank.append(catch*-1)
        
        isp = ch(list(self.hemo_))
        if isp == '0':
            catch = rt(1000,15000)
            self.hemo.append(catch)
            self.plday[f'{self.sdy}pl'].append(catch)
            self.bank.append(catch)
            
        elif isp == '1':
            catch = rt(1000,15000)
            self.hemo.append(catch*-1)
            self.plday[f'{self.sdy}pl'].append(catch*-1)
            self.bank.append(catch*-1)
        
        isp = ch(list(self.tahg_))
        if isp == '0':
            catch = rt(5000,20000)
            self.tahg.append(catch)
            self.plday[f'{self.sdy}pl'].append(catch)
            self.bank.append(catch)
            
        elif isp == '1':
            catch = rt(5000,20000)
            self.tahg.append(catch*-1)
            self.plday[f'{self.sdy}pl'].append(catch*-1)
            self.bank.append(catch*-1)
        
        isp = ch(list(self.toli_))
        if isp == '0':
            catch = rt(10000,100000)
            self.toli.append(catch)
            self.plday[f'{self.sdy}pl'].append(catch)
            self.bank.append(catch)
            
        elif isp == '1':
            catch = rt(10000,100000)
            self.toli.append(catch*-1)
            self.plday[f'{self.sdy}pl'].append(catch*-1)
            self.bank.append(catch*-1)
        
        
    def netm(self):
        self.sdy += 1
        self.plday[f"{self.sdy}pl"] = []
        print(self.plday)
        
        
    def show(self):
        print("Modir Amel:",sum(self.mdam),"$")
        print("Heiat Modireh:",sum(self.hemo),"$")
        print("Tahghighat:",sum(self.tahg),"$")
        print("Tolidat",sum(self.toli),"$")
        print("Bank:",sum(self.bank),"$")
    
    def part(self):
        self.columns = ["CEO","BOD","RED","PRD"]
        self.index = [sum(self.mdam),sum(self.hemo),sum(self.tahg),sum(self.toli)]
        
        
        
    def pldays(self):
        return self.plday
    
            
            
        
        