import time
print(time.time())
print(time.localtime())
x = time.time()
print(f'local time: {time.ctime(x)}')