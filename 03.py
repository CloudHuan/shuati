'''
给定一个只包含正数的数组，要求统计出里面数字出现的字数，返回重复次数最多的前N个数字
重点：sorted也可以排序dict哦
'''


def sortDictByValue(d):
    return sorted(d.items(),key=lambda dd:dd[1],reverse=True)

def countNum(_list,n):
    d = {}
    if n > len(_list):
        return;
    s = set(_list)
    for i in s:
        d[i]=_list.count(i)
    d = sortDictByValue(d)
    print(d)

if __name__ == "__main__":
    countNum([1,1,2,3,1,2,3,5,6,6,6,6,5,4,5],1);