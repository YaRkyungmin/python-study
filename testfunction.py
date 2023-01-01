'''
This is Docstring
'''
def hello():
    '''
    This is Function Docstring
    '''
    print('test test')
    if __name__ == 'testfunction':
        print('run hello function')
        print('__name__ : testfuction')
    
if __name__ == '__main__': #terminal에서 바로 실행할때 실행
    print('__name__ : __main__')
elif __name__ == 'testfunction':
    print('__name__ : testfuction')