import glob
import math
import numpy as np
import matplotlib.pyplot as plt
import numpy.ma as ma

list_of_files =  glob.glob('./*.txt')#["a08_s07_e01_skeleton_proj.txt"]# 

de=input("test(1) or train(2)")
if (de==1):
    outfile=open('hod_dl.t.txt','w')
if (de==2):
    outfile=open('hod_dl.txt','w')


def ang_xy(a,b):
	if(a[2]==b[2]):
		return 1.5707945
	else:
		d=float(math.atan((b[3]-a[3])/(b[2]-a[2])))
		return d

def ang_xz(a,b):
	if(a[2]==b[2]):
		return 1.5707945
	else:
		d=float(math.atan((b[4]-a[4])/(b[2]-a[2])))
		return d

def ang_yz(a,b):
	if(a[3]==b[3]):
		return 1.5707945
	else:
		d=float(math.atan((b[4]-a[4])/(b[3]-a[3])))
		return d

n=8   #bins


for fileName in list_of_files:
    infile =open(fileName,"r")
    dic={}
    for i in range(20):
        dic[i+1]=[]
    
    num_array=[]
    count=1
    
	for line in infile: 
		temp=[]
		for x in line.split(" "):
			if (x):
				temp.append(float(x))
			num_array.append(temp)
        
        if(count%20==0):
       	    order=[item[1] for item in num_array]
       	    for n1 in order:
                dic[int(n1)].append(num_array[int(n1)-1])
            num_array=[]
        count+=1
    num=len(dic[1])
    vec=[]
#    print(dic[1])
   
    for i in range(20):
        xy=[]
    	xz=[]
    	yz=[]
        data=[]
        data=dic[i+1]  #(i+1)th joint
        #print(data)
        for j in range(num-1):
            xy.append(ang_xy(data[j],data[j+1]))
            #print(ang_xy(data[j],data[j+1]))
            xz.append(ang_xz(data[j],data[j+1]))
            yz.append(ang_yz(data[j],data[j+1]))
        weights=np.ones_like(xy)/float(len(xy))     #xy lane           
        for x in (np.histogram(xy,weights=weights,bins=n))[0]: 
           
            vec.append(x)
             

        weights=np.ones_like(xz)/float(len(xz))    #xz lane    	     
        for y in np.histogram(xz,weights=weights,bins=n)[0]:
            vec.append(y)

        weights=np.ones_like(yz)/float(len(yz))    #yz lane    	     
        for z in np.histogram(yz,weights=weights,bins=n)[0]:
            vec.append(z)

# transform the data into SVM format
    new_vec=[]
    num=0
    new_vec.append(fileName[3:5])
    for val in vec:
        new_vec.append(str(num)+":"+str(val))
        num+=1
    
   # print(vec)
    
    for val in new_vec:    
        outfile.write(" "+val)
      
    outfile.write("\n")
    
    infile.close()
outfile.close()
           
    
    

    
        
