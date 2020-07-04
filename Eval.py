# -*- coding:utf-8 -* 
import time
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

import load_file
import Malware
import numpy as np
import os

EVAL_INTERVAL_SECS = 10
BATCH_SIZE = 1

def evaluate(X_test,Y_test):
    #f=open("feature","w")
    with tf.Graph().as_default() as g:
        x = tf.placeholder(tf.float32,[
            BATCH_SIZE,        #第一维表示一个batch中样例的个数
            Malware.IMAGE_SIZE,    #第二维和第三维表示图片的尺寸
            Malware.IMAGE_SIZE,
            Malware.NUM_CHANNELS]  #第四维表示图片的深度
            ,name='x-input')
        
        y_ = tf.placeholder(tf.float32,[None,Malware.OUTPUT_NODE], name='y-input')
        y = Malware.inference(x,False,None)
        correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

        variable_averages = tf.train.ExponentialMovingAverage(Malware.MOVING_AVERAGE_DECAY)
        variables_to_restore = variable_averages.variables_to_restore()
        saver = tf.train.Saver(variables_to_restore)

        while True:
            with tf.Session() as sess:
                ckpt = tf.train.get_checkpoint_state(Malware.MODEL_SAVE_PATH)
                if ckpt and ckpt.model_checkpoint_path:
                    saver.restore(sess,ckpt.model_checkpoint_path)
                    global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]

                    for i in range(len(X_test)):
                        xs=X_test[i:i+1]
                        ys=Y_test[i:i+1]
                        reshaped_xs = np.reshape(xs,(  #此处需要添加对xs的调整，重塑xs
                                                   BATCH_SIZE,
                                                   Malware.IMAGE_SIZE,
                                                   Malware.IMAGE_SIZE,
                                                   Malware.NUM_CHANNELS))
                        accuracy_score = sess.run(accuracy,feed_dict = {x: reshaped_xs, y_: ys})
                        if accuracy_score == 0.0: #输出预测失败的文件编号
                            print (i+1)
                        #print ("After %s training step(s),%d validation accuracy = %g"%(global_step,i,accuracy_score)) 
                        
                    '''  
                    xs=X_test
                    ys=Y_test  #测试集较小，一次全测即可
                    reshaped_xs = np.reshape(xs,(  #此处需要添加对xs的调整
                                                   BATCH_SIZE,
                                                   Malware.IMAGE_SIZE,   
                                                   Malware.IMAGE_SIZE,    
                                                   Malware.NUM_CHANNELS))                      
                    accuracy_score = sess.run(accuracy,feed_dict = {x: reshaped_xs, y_: ys})  #获得准确率
                    
                    print ("After %s training step(s), validation accuracy = %g"%(global_step,accuracy_score))
                    '''
                    #np.savetxt("result.txt",fc11)
                    #print fc11
                    #print type(fc11)
                    #f.write(fc11)
                    #f.write("\n")

                else:
                    print ("No checkpoint file found")
                    return

            time.sleep(EVAL_INTERVAL_SECS)

def main(argv=None):
    BASE_DIR = os.getcwd()
    #X_test,Y_test=load_file.LoadDataMatrix(BASE_DIR + "/test/","test_label.csv") #用测试集测试
    X_test,Y_test=load_file.LoadDataMatrix(BASE_DIR + "/train/","train_label.csv") #用训练集测试
    evaluate(X_test,Y_test)

if __name__ == '__main__':
    tf.app.run()
