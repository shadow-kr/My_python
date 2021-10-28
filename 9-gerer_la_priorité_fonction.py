def func1():
    print ('1-hi')

def func2():
    print ('2-slt')

func1()
func2()

print('===============new way=============')

from threading import Thread

def func1():
    print('1-ello')

def func2():
    print("2-yahallo")

if __name__ == '__main__':
    Thread(target = func2).start()
    Thread(target = func1).start()