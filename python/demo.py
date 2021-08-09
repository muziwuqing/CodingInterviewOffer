def fn():
    print('我是fn函数....')

# 只需要根据现有的函数，来创建一个新的函数
def fn2():
    print('函数开始执行~~~')
    fn()
    print('函数执行结束~~~')

fn2()  


def add(a , b):
    '''
        求任意两个数的和
    '''
    r = a + b
    return r

def new_add(a,b):
    print('计算开始~~~')
    r = add(a,b)
    print('计算结束~~~')
    return r

r = new_add(111,222)    
print(r)
