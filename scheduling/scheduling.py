#python scheduling.py "[1,6,4,3,5,2,8,9,7,10]" "[[7,14,25],[16,19,14],[11,20,24],[18,12,20],[9,20,13],[11,20,23],[14,18,8],[16,19,21],[11,17,20],[13,14,11]]" "[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]" "[[0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0],[0,1,0,1,0,1,0,0,0,0],[0,1,0,1,1,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,0]]" "200" "[[0.22,1.0],[0.21,1.0],[0.29,1.0]]" "[[0.03,0.8,2.9],[0.04,0.8,2.5],[0.07,1.0,2.5]]"
from locale import ERA_D_FMT
import numpy as np
import sys
import random
from datetime import datetime
import ast
import math

def HEFT(EST, EFT, pos, pscheduling, qlist, T, c, E, n, p):
    for idx, i in enumerate(qlist):
        if idx<pos:
            continue
        EST[i-1][0]=0
        EST[i-1][1]=0
        EFT[i-1][0]=0
        EFT[i-1][1]=1000000
        for k in range(p):
            if idx==0:
                tmp = 0
                tmp2 = tmp+T[i-1][k]
                if tmp2<EFT[i-1][1]:
                    EFT[i-1][1]=tmp2
                    EFT[i-1][0]=k
                    EST[i-1][1]=tmp
                    EST[i-1][0]=k
                    pscheduling[k]=tmp2
            else:
                pred = E[i-1]
                tmp = 0
                for idx2, l in enumerate(pred):
                    if l==1:
                        tmp = max(tmp,EFT[idx2][1]+c[idx2][i-1])
                tmp = max(tmp, pscheduling[k])
                tmp2 = tmp+T[i-1][k]
                if tmp2<EFT[i-1][1]:
                    EFT[i-1][1]=tmp2
                    EFT[i-1][0]=k
                    EST[i-1][1]=tmp
                    EST[i-1][0]=k
                    pscheduling[k]=tmp2
    return EFT[qlist[-1]-1][1]


def DUPRS1(EST, EFT, pos, pscheduling, qlist, T, c, E, n, p,latency,frequency,processorinfo,proc_freq,sl):
    EA = 0
    for idx, i in enumerate(qlist):
        ddl = EFT[i-1][1]*latency/sl
        p_energy = math.inf
        proc = EFT[i-1][0]
        proc_min = frequency[proc][0]
        proc_max = frequency[proc][1]
        rng = np.arange(proc_min, proc_max, 0.05)
        for f in rng:
            tmp = EST[i-1][1]+T[i-1][proc]*proc_max/f
            tmp2 = (processorinfo[proc][0]+processorinfo[proc][1]*pow(f,processorinfo[proc][2]))*T[i-1][proc]*proc_max/f
            if tmp<=ddl and tmp2<=p_energy:
                proc_freq[i-1]=f
                p_energy=tmp2
                EFT[i-1][1]=tmp
                pscheduling[proc]= tmp
                break
        if(p_energy==math.inf):
            proc_freq[i-1]=proc_max
            p_energy=(processorinfo[proc][0]+processorinfo[proc][1]*pow(proc_max,processorinfo[proc][2]))*T[i-1][proc]
            pscheduling[proc]= EFT[i-1][1]
        else:
            EA = EA+p_energy
        sl = HEFT(EST,EFT,idx+1,pscheduling,qlist,T,c,E,n,p)
    return EA, sl


if __name__ == "__main__":
    time1 = datetime.now()
    if len(sys.argv) != 8:
        print("Usage: python scheduling.py <qlist> <T> <c> <Edges> <latency> <frequency> <processorinfo>")
        sys.exit(1) 

    qlist = ast.literal_eval(sys.argv[1])
    T = ast.literal_eval(sys.argv[2])
    c = ast.literal_eval(sys.argv[3])
    E = ast.literal_eval(sys.argv[4])
    latency = ast.literal_eval(sys.argv[5])
    frequency = ast.literal_eval(sys.argv[6])
    #Energy = ast.literal_eval(sys.argv[7])
    processorinfo = ast.literal_eval(sys.argv[7])
    n = len(qlist)
    p = len(T[0])
    EFT = [[None]*2 for _ in range(n)]
    EST = [[None]*2 for _ in range(n)]
    pscheduling = [0]*p
    
    sl = HEFT(EST,EFT,0,pscheduling,qlist,T,c,E,n,p)
    
    proc_freq = [0]*n
    pscheduling = [0]*p
    
    EA, sl = DUPRS1(EST,EFT,0,pscheduling,qlist,T,c,E,n,p,latency,frequency,processorinfo,proc_freq,sl)
    print(EA)
    print(sl)
    


    

            

