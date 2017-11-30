'''
判断列表是否满足回数
比如 1 2 3 4 3 2 1
'''

def check(_list):
    mLength = len(_list)
    for i in range(mLength):
        if not _list[i] == _list[mLength-1-i]:
            return False
    return True

if __name__ == "__main__":
    print(check([1,2,3,5,3,2,1]))