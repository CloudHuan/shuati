'''
输入例子:
I am a    student

输出例子:
student a am I
'''
import re


def mergeWord(word):
    words = re.split('\s+',word)
    words.reverse()
    print(" ".join(words))

if __name__ == "__main__":
    mergeWord('I am a    student')