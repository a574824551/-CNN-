#-*- coding: utf-8 -*-

import os
import numpy as np
import sys
import struct
def TranAsmToByte(FileName):
    #wordlist=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','G']
    #wordlist=[bytes('0',encoding="utf-8"),bytes('1',encoding="utf-8"),bytes('2',encoding="utf-8"),bytes('3',encoding="utf-8"),
    #          bytes('4',encoding="utf-8"),bytes('5',encoding="utf-8"),bytes('6',encoding="utf-8"),bytes('7',encoding="utf-8"),
    #          bytes('8',encoding="utf-8"),bytes('9',encoding="utf-8"),bytes('A',encoding="utf-8"),bytes('B',encoding="utf-8"),
    #          bytes('C',encoding="utf-8"),bytes('D',encoding="utf-8"),bytes('E',encoding="utf-8"),bytes('G',encoding="utf-8")]
    wordlist=[48,49,50,51,52,53,54,55,56,57,#0-9 的ascii码
              65,66,67,68,69,70]#A-F 的ascii码
    
    #print (wordlist)
    output=[]
    file_object = open(FileName+".asm","rb")#载入文件
    
    line_num = 0#行号
    for line in file_object:#逐行提取数据
        line_num = line_num+1
        X=line.split()#分割数据
        
        for a in X:
            #print (a,a[0],type(a[0]),len(a))
            if(len(a)==2 and (a[0] in wordlist) and (a[1] in wordlist)):#提取机器码
                #print (a,a[0],a[1],type(a[0]),len(a))
                output.append(a)
        elif (len(a)==3 and (a[0] in wordlist) and (a[1] in wordlist) and (a[2]==43)): #针对数据格式为00+等
            output.append(a[:-1])
        print (X)
        
        
        #if line_num==200: #对前200行进行测试
        #    break
    file_object.close()#关闭.asm文件
    
    #print (output)
    
    #二进制写,保存为.txt,不换行
    '''  
    file_save = open(FileName+".txt","wb")#持久化,二进制写
    num = 0
    ch1 = " "#插入空格分隔符
    ch2 = "\n"#插入回车分隔符
    ch1_byte = ch1.encode("ascii")#将分隔符转码为ascii码
    ch2_byte = ch2.encode("ascii")    
    for x in output:
        num = num+1
        #write_buf = x.decode('ascii')
        file_save.write(x+ch1_byte)#存储一个数据加一个空格
        if (num%16==0):
            file_save.write(ch2_byte)#输出回车符
    '''
    #二进制写结束
    
    
    #字符串写,保存为.txt
    file_save = open(FileName+".txt","w")#持久化,直接写
    num = 0
    for x in output:
        num = num+1
        write_buf = x.decode('ascii') #将二进制数据解码，转为字符型str
        #print (write_buf,type(write_buf))
        
        file_save.write(write_buf+" ") #存储一个数据加一个空格
        if (num%16==0):
            file_save.write("\n")#每16个一行输出回车符
    #字符串写结束
    
    file_save.close()#关闭.txt文件
    print ("write finished")
    
def grayImg(filename):
    
    file_object = open(FileName+".txt","r")#载入文件
    # 二进制文件list化
    binList = []
    for line in file_object :
        
        str_temp = line.split()
        
        # 转二进制
        row = []
        for n_hex in str2 :
            row.append( bin(int(n_hex, 16))[2:] )

            binList.append(row)

    # 最后一行是否满16个,不满则补 ‘0’
    maxRow = len(binList)
    length = len(binList[maxRow - 1])

    for i in range(16 - length) :
        binList[maxRow - 1].append('0')

    # 像素矩阵
    pixMat = np.matrix(binList)
    #print pixMat
    # 生成图像
    img = Image.fromarray(np.uint8(pixMat))
    # 像素改为32*32
    img = img.resize((32, 32),Image.ANTIALIAS)
    img.save( fileName + '.png')
    
    
TranAsmToByte("Ig2DB5tSiEy1cJvV0zdw")
