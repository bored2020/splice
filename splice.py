import math
import numbers
import numpy as np
import pandas as pd

# 载入所需要的基础包

#  构造一个示性函数，如果输入值为true则返回1 否则返回0
def shixinghanshu(X):
    if X == True :
        return 1
    else:
        return 0



class Splice(X,Y,max_iter,K_max):
    """
    max_iter: 算法的最大迭代步数
    X 为输入的样本矩阵，n为样本个数,p为特征个数
    Y 为输入的因变量，可以是连续的数值型也可以是0,1型分类
    tau为门限值，如果在迭代中损失函数的减小小于这个迭代值则停止迭代，输出结果
    K_max为最大切片大小
    

    """
    # p为X的列数，即特征数
    # n为X的行数，即样本个数
    p =  X.shape[0]
    n =  X.shape[1]
    # 首先计算出切片大小，即最优子集的个数 s根据论文中的建议，s_max一般为[n/log(p)loglog(n)]

    s_max = int(n/(math.log(p)*math.log(math.log(n))))

    tau_s = (0.01 * s_max * math.log(p) * math.log(math.log(n)) )/ n



    # 首先计算初始的激活集合A^0

    # 这里没有弄好X_j的转置，在python中向量的转置好像有点不同

    for  i in range(p) :
        for j in range(p) ：
            A_index = shixinghanshu(abs((np.multiply(X[:,j],Y)/math.sqrt(math.multiply((X[:,j],X[:,j])) < =  (np.multiply(X[:,i],Y)/math.sqrt(math.multiply((X[:,i],X[:,i]) < = s_max)
            # 这里是根据论文中的算法首先计算出初始的A^0和I^0
A_inital = X[:,A_index]
            # 初始的I是全体变量中除掉初始的A
I_inital = X[:,-A_index]


beta_A_inital =  (A_inital.T @ A_inital).I @ 


        


