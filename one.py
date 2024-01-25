import time

t = time.localtime(time.time())
local = time.asctime(t)
str = "Today is " + local

print(str)