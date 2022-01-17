'''
This is Docstring
'''
def hello():
    '''
    This is Function Docstring
    '''
    if __name__ == 'testfunction':
        print('__name__ : testfuction')
    
if __name__ == '__main__': #terminal에서 바로 실행할때 실행
    print('__name__ : __main__')
elif __name__ == 'testfunction':
    print('__name__ : testfuction')