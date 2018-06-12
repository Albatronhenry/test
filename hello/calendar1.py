import time , calendar , hello
# 下面两行代码结果相同 time.time()获取当前时间戳
print(time.ctime())
print(time.ctime(time.time()))
# time.strftime格式化输出当前时间
print(time.strftime('%y-%m-%d %I:%M:%S'))
# print(calendar.calendar(2019,w=2,l=1,c=4))
print(calendar.weekday(2018,6,10))

hello.hello()