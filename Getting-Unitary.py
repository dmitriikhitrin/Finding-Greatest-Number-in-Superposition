import math
import numpy as np
import itertools

mtrx= np.random.rand(4,4)
mtrx= np.add(mtrx,np.random.rand(4,4)*complex('j'))
mtrx = np.array(mtrx,dtype=complex)
mtrx=mtrx/np.linalg.norm(mtrx)

stepcount = 50000
blr = 0.05
delt = 0.0000001

def calc(mat,v):
    return np.dot(mat,v)

def std(iv,ov):
    mxu=0
    eth = [0,0,0,0]
    for i in range(len(iv)):
        if iv[i] != 0:
            mxu=i
    eth[mxu]= 1
    sqs=0
    for i in range(len(ov)):
        sqs += (abs(ov[i])-eth[i])**2
    if max(ov)!= ov[mxu]:
        sqs+=0.1
    return sqs

def dot(a,b):
    s = 0
    for i in range(len(a)):
        s += a[i]*b[i].conjugate()
    return s

def normality(mat):
    af= 0
    cf =0
    for i in range(4):
        af+=abs(np.sum(np.absolute(mat[i,:])**2)-1)
        af += abs(np.sum(np.absolute(mat[:,i]) ** 2) - 1)
    rpp = itertools.combinations([0, 1, 2, 3], 2)
    for i in rpp:
        cf += abs(dot(mat[:,i[0]],mat[:,i[1]]))
        cf += abs(dot(mat[i[0],:],mat[i[1],:]))
    return af + cf

def normality2(mat):
    b =np.dot(mtrx, np.conj(np.transpose(mtrx)))
    return np.sum(np.absolute(b-np.eye(4))**2)

def loss(mat):
    comb = list(itertools.combinations_with_replacement([0, 1], 4))
    comb.pop(0)
    perm = set()

    for i in comb:
        perm = perm.union(itertools.permutations(i, 4))
    loss=0

    for i in perm:
        if sum(i)!=1:
            i_v = normalize(i)
            loss += std(i_v,calc(mat,i_v))
    loss += normality(mat)
    loss+=normality2(mat)*3
    return loss
def normalize(v):
    v_a = np.array(v,dtype=complex)
    s= 0
    for i in range(4):
        s+= v_a[i]**2
    v_a = v_a/math.sqrt(s)
    return v_a

def pgrad(mat,delt):
    gradm = np.zeros((4,4),dtype=complex)
    for i in range(4):
        for k in range(4):
            bmat =np.copy(mat)
            bmat[k][i] -= delt
            gradm[k][i] = (loss(mat)-loss(bmat))/delt
    for i in range(4):
        for k in range(4):
            bmat =np.copy(mat)
            bmat[k][i] -= delt*complex('j')
            gradm[k][i] += complex('j')*(loss(mat)-loss(bmat))/delt
    return gradm


def main():
    for j in range(1,stepcount+1):
        lr = abs((blr/j**(1/3+1/2*j/stepcount)))
        grd = pgrad(mtrx,delt)
        for i in range(4):
            for k in range(4):
                mtrx[k][i] -= grd[k][i] * lr
        print(j,lr,loss(mtrx), normality(mtrx), normality2(mtrx))
    comb = list(itertools.combinations_with_replacement([0, 1], 4))
    comb.pop(0)
    perm = set()
    print(mtrx)
    for i in comb:
        perm = perm.union(itertools.permutations(i, 4))
    for i in perm:
        print(normalize(i), np.absolute(calc(mtrx,normalize(i))))
    print(np.absolute(np.dot(mtrx,np.conj(np.transpose(mtrx)))-np.eye(4)))
    print(abs(np.linalg.det(mtrx)))
    print(np.linalg.qr(mtrx))


if __name__ =='__main__':
    main() 