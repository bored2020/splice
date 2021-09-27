import math
import numbers
import numpy as np
import pandas as pd


def screening(self,X,Y,number):
    """
    X 为输入的样本矩阵，n个样本,p个特征(n_samples,p_features)
    Y 为响应变量，可以为数值型连续变量也可以为0，1分类变量(n_samples)
    number 为screening算法截取的个数，按相关系数大小排序，到number参数为止为screening算法筛选出来的的变量
    这里计算的是p个变量的与响应变量的相关系数，应该是一个p维的向量，然后在这个向量中根据number参数值进行排序.
    这里的X与Y都为pandas中的dataframe类型
    """
    p = X.shape[0]
    n = X.shape[1]
    dfx = pd.DataFrame(X)
    dfy = pd.DataFrame(Y)
    if Y.shape[1] != n:
        raise ValueError("相应变量Y的样本个数与输入样本个数不符")
    if pd.isnan(X).any() :
        raise ValueError("输入样本矩阵中有NAN,请检查")
    if pd.isnan(Y).any() :
        raise ValueError("输入相应矩阵中有NAN,请检查")

    dfx['Y'] = dfy

    dfnew = dfx

    dfnew.corr()



    # 这里的思想是将Y插入到X矩阵中计算相关系数再提取出最后一列即为想要的
    
    for i in np.arange(X.shape[1]):
        X.iloc[i]




def splice(X,Y,tau，max_iter,K):
    """
    max_iter: 算法的最大迭代步数
    X 为输入的样本矩阵，n为样本个数,p为特征个数
    Y 为输入的因变量，可以是连续的数值型也可以是0,1型分类
    tau为门限值，如果在迭代中损失函数的减小小于这个迭代值则停止迭代，输出结果
    K为交叉验证折数

    """
    if 