# -*- coding: utf-8 -*-
# lattice constant, input your lattice constant here
lx = input('lattice constant a = ')
ly = input('lattice constant b = ')
#number of points be fitting,you can adjust them accordingly to get better fit
q = input('define fitting steps(recommand 5-10), steps = ')
h = q+2
#number of VBM and CBM, do not change it in effective mass calculation!!!
bn = 1
c,v,r = [],[],[]
################################################################################
# Functions 
def str2float2d(k):
    for i in range(len(k)):
        for j in range(len(k[i])):
            k[i][j]=float(k[i][j])
    return k
def str2float1d(k):
    for i in range(len(k)):
        k[i] = float(k[i])
    return k
def openfile(filename):
    filename = 'output.file'
    with open(filename,'r') as f:
        for lines in f.readlines():
            lines = lines.strip()
            if a.match('%s'%(lines)):
                if  a.match('%s'%(lines)).group(4)=='2.00000':
                    v.append(lines)    
                else:
                    raise ValueError('wrong input')
            if b.match('%s'%(lines)):
                if b.match('%s'%(lines)).group(4)=='0.00000':
                    c.append(lines)
                else:
                    raise ValueError('wrong input')
        f.close() 
def plotfit():
    plt.subplot(2,2,1)
    plt.plot(np.array(xele[0]),np.poly1d(xe)(np.array(xele[0])),linestyle='--')
    plt.plot(np.array(xele[0]),np.array(xele)[1])
    plt.title('polyfitting electrons along x direction')
    #electrons along y 
    plt.subplot(2,2,2)
    plt.plot(np.array(yele[0]),np.poly1d(ye)(np.array(yele[0])),linestyle='--')
    plt.plot(np.array(yele[0]),np.array(yele)[1])
    plt.title('polyfitting electrons along y direction')
    #holes along x 
    plt.subplot(2,2,3)
    plt.plot(np.array(xhole[0]),np.poly1d(xh)(np.array(xhole[0])),linestyle='--')
    plt.plot(np.array(xhole[0]),np.array(xhole)[1])
    plt.title('polyfitting holes along x direction')
    #holes along y
    plt.subplot(2,2,4)
    plt.plot(np.array(yhole[0]),np.poly1d(yh)(np.array(yhole[0])),linestyle='--')
    plt.plot(np.array(yhole[0]),np.array(yhole)[1])
    plt.title('polyfitting holes along y direction')
    plt.show()
################################################################################
# Main
if __name__ == '__main__':
    import re
    import numpy as np
    import csv
    import matplotlib.pyplot as plt
    a=re.compile(r'\s*(\d+)\s*(-?0.\d+)\s*(-?0.\d+)\s*(2.00000)\s*')
    b=re.compile(r'\s*(\d+)\s*(-?0.\d+)\s*(-?0.\d+)\s*(0.00000)\s*')
    openfile('output.file')
    vb = [vb.split() for vb in v] 
    cb = [cb.split() for cb in c] 
    str2float2d(cb)
    str2float2d(vb)
    bandgap = (np.array(cb)[0,1]-np.array(vb)[-1,2])*27.211
    print('bandgap = %fev'%(bandgap))    
    z = map(int,np.hstack((np.array(vb)[-bn:,0],np.array(cb)[:bn,0])).tolist())
    #grep datas
    bnd = [[] for i in range(2*bn)] #y-axis
    with open('emass1.csv','rb') as f:
        readers = csv.reader(f)    
        readers.next()
        for lines in readers:
            r.append(lines[2])
            efermi = lines[3]
            for i in range(2*bn):
                bnd[i].append(lines[z[i]+3])
        str2float2d(bnd)
        str2float1d(r)
        for i in range(len(bnd)):
            for j in range(len(bnd[i])):
                bnd[i][j] = (bnd[i][j]-float(efermi))*27.211
        bnd.insert(0,r)
        f.close()
    print ("efermi = %fev"%(float(efermi)*27.211))
    # effective mass lists
    vbm = bnd[1]
    cbm = bnd[2]
    xhole,xele,yhole,yele = [],[],[],[]
    xhole.append(r[vbm.index(max(vbm))-q:vbm.index(max(vbm))+h]) 
    xhole.append(vbm[vbm.index(max(vbm))-q:vbm.index(max(vbm))+1]+\
    vbm[vbm.index(max(vbm))-q:vbm.index(max(vbm))+1][::-1])
    xele.append(r[cbm.index(min(cbm))-q:cbm.index(min(cbm))+h]) 
    xele.append(cbm[cbm.index(min(cbm))-q:cbm.index(min(cbm))+1]+\
    cbm[cbm.index(min(cbm))-q:cbm.index(min(cbm))+1][::-1])
    yhole.append(r[vbm.index(max(vbm))-q:vbm.index(max(vbm))+h]) 
    yhole.append(vbm[vbm.index(max(vbm))+1:vbm.index(max(vbm))+h][::-1]+\
    vbm[vbm.index(max(vbm))+1:vbm.index(max(vbm))+h])
    yele.append(r[cbm.index(min(cbm))-q:cbm.index(min(cbm))+h]) 
    yele.append(cbm[cbm.index(min(cbm))+1:cbm.index(min(cbm))+h][::-1]+\
    cbm[cbm.index(min(cbm))+1:cbm.index(min(cbm))+h])
    # fitting the parabolic
    xh=np.polyfit(np.array(xhole[0]),np.array(xhole[1]),2)
    yh=np.polyfit(np.array(yhole[0]),np.array(yhole[1]),2)
    xe=np.polyfit(np.array(xele[0]),np.array(xele[1]),2)
    ye=np.polyfit(np.array(yele[0]),np.array(yele[1]),2)       
    # effective mass calculator
    mxh = 150.76881/(lx**2*xh.tolist()[0])
    myh = 150.76881/(ly**2*yh.tolist()[0])
    mxe = 150.76881/(lx**2*xe.tolist()[0])
    mye = 150.76881/(ly**2*ye.tolist()[0])
    print('effective mass of holes along x direction = %f'%(mxh))
    print('effective mass of holes along y direction = %f'%(myh))
    print('effective mass of electrons along x direction = %f'%(mxe))
    print('effective mass of electrons along y direction = %f'%(mye))
    #plot the fitting curves comparison with origin curves
    plotfit()