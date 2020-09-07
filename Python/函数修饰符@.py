'''
python函数修饰符@的作用是为现有函数增加额外的功能，常用于插入日志、性能测试、事务处理等等。

创建函数修饰符的规则：
（1）修饰符是一个函数
（2）修饰符取被修饰函数为参数
（3）修饰符返回一个新函数
（4）修饰符维护被维护函数的签名
'''
# def log(func):
#     def wrapper():
#         print('log开始 ...')
#         func()
#         print('log结束 ...')
#     return wrapper
    
# @log
# def test():
#     print('test ..')
# test()
#————————————————————————————
#使用functools模块提供的修改函数属性的方法wraps
def log(func):
    def wrapper():
        print('log开始 ...')
        func()
        print('log结束 ...')
    return wrapper
    
@log
def test1():
    print('test1 ..')

def test2():
    print('test2 ..')

print(test2)
print(test1.__name__)
print(test2.__name__)