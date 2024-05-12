# -*- coding: utf-8 -*-
def loadDict():
    file_dict = open('dict.txt','rb')
    Dict = {}
    for line in file_dict.readlines():
        tmp=[]
        line = str(line.decode('utf-8'))
        lineVec = str(line).strip().split('')
        for content in lineVec[1:-1]:
            tmp.append(content)
        Dict[lineVec[0]] = tmp
    return Dict

def main():
    wholeDict = loadDict()
    wordInput = input("Input an English word: ")
    if wordInput in wholeDict.keys():
        print("English: " + wordInput)
        tmpStr = ''
        for inst in wholeDict[wordInput]:
            
            tmpStr += (inst)
        print("Chinese: " + tmpStr)

if __name__ == '__main__':
    while 1:
        main()