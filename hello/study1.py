# import os
# os.path
# os.getcwd()
# #os.getcwdu()
# os.rename(r'd:\py.txt',r'd:\pyf.txt')
#raise NameError('HiThere')
# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise
# def temp_convert(var):
#     try:
#         return int(var)
#     except(ValueError) as Argument:
#         print('arg not incloud digit\n',Argument)
# temp_convert('henry')
class Parent:
    def myMethod(self):
        print('parent constructor method')
class Child(Parent):
    def myMethod(self):
        print('child constructor method')
c = Child()
c.myMethod()
super(Child,c).myMethod()