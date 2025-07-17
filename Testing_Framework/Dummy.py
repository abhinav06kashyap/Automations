import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("-i", "--inventory",default="inventory.xlsx",help="Inventory file. Deafult =inventoty.xlsx")
args = argParser.parse_args()
print(args)

class my_class:
    def __init__(self):
        pass
    def my_fun(self,param1,param2):
        return param1+param2    

    def your_fun(self,param1,param2,param3):
        a=self.my_fun(2,3)
        return param1+param2*param3
     
if my_class.__init__:
    print("helo")     
     
cl = my_class()
a=cl.my_fun(1,2)
b=cl.your_fun(1,2,3)
print(a,b)