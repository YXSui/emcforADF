# -*- coding: utf-8 -*-
#parameters
#input the number of CBM/VBM you wanna plot! The CBM numbers are equal to the VBM 
bn = input('band_number = ')
#list of valence and conductence band   
v,c,r = [],[],[]
bnd = [[] for i in range(2*bn)]
#filename = 'output.file'
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
def plot_bandstructure(x):
    for i in range(len(x)-1):
        plt.plot(x[0],x[i+1])#8 lines of bandstructure,4 valence and 4 conductance
        plt.plot(x[0],[0,]*len(x[0]),linestyle='--') #Fermi level
        plt.xlim([x[0][0],x[0][-1]])
    plt.show()
    return x
def openfile(file1='output.file'):
    with open(file1,'r') as f1:
        a=re.compile(r'\s*(\d+)\s*(-?0.\d+)\s*(-?0.\d+)\s*(2.00000)\s*')
        b=re.compile(r'\s*(\d+)\s*(-?0.\d+)\s*(-?0.\d+)\s*(0.00000)\s*')
        for lines in f1.readlines():
            lines = lines.strip()
            if a.match('%s'%(lines)):
                vband = a.match('%s'%(lines))
                if vband.group(4)=='2.00000':
                    v.append(lines)    
                else:
                    raise ValueError('wrong input')
            if b.match('%s'%(lines)):
                cband = b.match('%s'%(lines))
                if cband.group(4)=='0.00000':
                    c.append(lines)
                else:
                    raise ValueError('wrong input')
        f1.close()
################################################################################
# Main
if __name__ == '__main__':
    import re
    import numpy as np
    import csv
    import matplotlib.pyplot as plt
    openfile()
    vb = [vb.split() for vb in v] 
    cb = [cb.split() for cb in c] 
    str2float2d(cb)
    str2float2d(vb)
    vba = np.array(vb)
    cba = np.array(cb)
    bandgap = (cba[0,1]-vba[-1,2])*27.211
    # the next part is about grep the 8 lines and plot band structure
    #grep datas
    z = np.hstack((vba[-bn:,0],cba[:bn,0]))
    z = map(int,z.tolist())
    with open('emass.csv','rb') as f2:
        readers = csv.reader(f2)
        readers.next()
        for lines in readers:
            r.append(lines[2])
            efermi = lines[3]
            for i in range(2*bn):
                bnd[i].append(lines[z[i]+3])
        str2float2d(k=bnd)
        str2float1d(k=r)
        for i in range(len(bnd)):
            for j in range(len(bnd[i])):
                bnd[i][j] = (bnd[i][j]-float(efermi))*27.211
        f2.close()
    bnd.insert(0,r)
    #print ("efermi = %fev"%(float(efermi)*27.211))
    #plot band structure
    plot_bandstructure(bnd)
    #save plotted bandstructure to Origin format, so you can adjust the figure!
    np.savetxt('band.dat',np.array(bnd).T)