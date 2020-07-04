#-*- coding: utf-8 -*-

from scipy.misc import imread
import os
import numpy as np
def LoadDataMatrix(filepath,FileName):
    X=[]
    file_object = open(filepath+FileName,"r")#打开文件名表格 格式 （文件名  标签）
    Label= []
    Name = []
    for line in file_object:
        Name.append((line.split(',')[:1])[0]) #Name String型  每一行切割后的第一个元素为Name
        Label.append(int(((line.split(',')[1:])[0].split())[0])) #Label int型  每一行切割后的第二个元素为Name，类型转换为int
        
    for i in range(0,len(Name)):
        #载入数据
        
        #处理像素矩阵
        if (Label[i]==1):
            img = imread(filepath +"1_"+Name[i]+".png") #载入标签为1的图片
            #print (img)
        if (Label[i]==0):
            img = imread(filepath +"0_"+Name[i]+".png") #载入标签为0的图片
            #print (img)
            imga=img.astype('float32') #像素矩阵类型设置为float32
            X.append(imga) #将一个图片的像素矩阵添加进X
        
        #处理标签    
        Label = np.array(Label) #转为array格式
        Y=[]
        for i in range(0,len(Label)):
            #temp = [0,0,0,0,0,0,0,0,0,0]
            temp = [0.0,0.0] 
            temp[Label[i]]=1.0
            temp_np = np.array(temp,dtype = 'float64')
            Y.append(temp_np)
        
        #print (Label.shape)
        #Label = Label.reshape(len(Label),1)
        #print (Label.shape)    
        return X,Y
        
#BASE_DIR = os.getcwd()
#X_train,Y_train=LoadDataMatrix(BASE_DIR + "/train/","train_label.csv")
#print "finish loading train data"
#X_test,Y_test=LoadDataMatrix(BASE_DIR + "/test/","test_label.csv")
#print "finish loading test data"
#print (X_train,Y_train)
#print ("################")
#print (X_test,Y_test)

