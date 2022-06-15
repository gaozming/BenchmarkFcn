'''
2019年3月9日
制定一个矩阵生成函数，后期直接导入使用
'''


# 生成空矩阵
def make_matrix(m,n,Fill=0.0):
    mat=[]
    if m==1 and n==1:
        mat=[Fill]
    elif m==1 and n!=1:
        mat=[Fill]*n
    elif m!=1 and n==1:
        mat=[Fill]*m
    else:
        for i in range(m):
            mat.append([Fill]*n)
    return mat