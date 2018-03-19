import os, string, math
import numpy as np

path = os.getcwd().replace ('\\','/') + '/dataset/'

def findangles(a, b):	
	if(a[0]==b[0] ):
		xy = 1.5707945
		xz = 1.5707945
	else:
		xy=float(math.atan((b[1]-a[1])/(b[0]-a[0])))
		xz=float(math.atan((b[2]-a[2])/(b[0]-a[0])))
	if(a[1]==b[1] ):
		yz = 1.5707945
	else:
		yz=float(math.atan((b[2]-a[2])/(b[1]-a[1])))
	if(math.isnan(xy)):
		xy = 1.5707945
	if(math.isnan(yz)):
		yz = 1.5707945
	if(math.isnan(xz)):
		xz = 1.5707945
	return xy,yz,xz

def HOD(folder ="test"):
	folder_ = path + folder #Path to selected folder
	files = os.listdir(folder_)
	nbins = 12
	for file in files: #Scan through files
		instance = np.loadtxt(folder_ +"/"+ file)
		joints=[]
		temp1 = []
		temp2 = []
		temp3 = []
		temp4 = []
		temp5 = []
		temp6 = []
		temp7 = []
		temp8 = []
		temp9 = []
		temp10 = []
		temp11 = []
		temp12 = []
		temp13 = []
		temp14 = []
		temp15 = []
		temp16 = []
		temp17 = []
		temp18 = []
		temp19 = []
		temp20 = []
		for frame in instance:			
			if frame[1] == 1:
				temp1.append(frame[2:5])				
			elif frame[1] == 2:
				temp2.append(frame[2:5])
			elif frame[1] == 3:
				temp3.append(frame[2:5])
			elif frame[1] == 4:
				temp4.append(frame[2:5])
			elif frame[1] == 5:
				temp5.append(frame[2:5])
			elif frame[1] == 6:
				temp6.append(frame[2:5])
			elif frame[1] == 7:
				temp7.append(frame[2:5])
			elif frame[1] == 8:
				temp8.append(frame[2:5])
			elif frame[1] == 9:
				temp9.append(frame[2:5])
			elif frame[1] == 10:
				temp10.append(frame[2:5])
			elif frame[1] == 11:
				temp11.append(frame[2:5])
			elif frame[1] == 12:
				temp12.append(frame[2:5])
			elif frame[1] == 13:
				temp13.append(frame[2:5])
			elif frame[1] == 14:
				temp14.append(frame[2:5])
			elif frame[1] == 15:
				temp15.append(frame[2:5])
			elif frame[1] == 16:
				temp16.append(frame[2:5])
			elif frame[1] == 17:
				temp17.append (frame[2:5])
			elif frame[1] == 18:
				temp18.append(frame[2:5])
			elif frame[1] == 19:
				temp19.append(frame[2:5])
			elif frame[1] == 20:
				temp20.append(frame[2:5])
				
		joints.append(temp1)
		joints.append(temp2)
		joints.append(temp3)
		joints.append(temp4)
		joints.append(temp5)
		joints.append(temp6)
		joints.append(temp7)
		joints.append(temp8)
		joints.append(temp9)
		joints.append(temp10)
		joints.append(temp11)
		joints.append(temp12)
		joints.append(temp13)
		joints.append(temp14)
		joints.append(temp15)
		joints.append(temp16)
		joints.append(temp17)
		joints.append(temp18)
		joints.append(temp19)
		joints.append(temp20)
		
		vec=[]
		print(str(len(vec)))
		for jointi in joints:
			xy=[]
			yz=[]
			xz=[]			
			for f in range(0,len(jointi)-1):				
				a1, a2, a3 = findangles(jointi[f],jointi[f+1])
				xy.append(a1)
				yz.append(a2)
				xz.append(a3)			
			for x in (np.histogram(xy,bins=nbins))[0]:
				vec.append(x/len(jointi))			
			for x in (np.histogram(xy[0:(int(len(jointi)/2))],bins=nbins))[0]:
				vec.append(x/(len(jointi)/2))			
			for x in (np.histogram(xy[(int(len(jointi)/2)):(int(len(jointi)))],bins=nbins))[0]:
				vec.append(x/(len(jointi)/2))				
			for x in (np.histogram(yz,bins=nbins))[0]:
				vec.append(x/len(jointi))	
			for x in (np.histogram(yz[0:(int(len(jointi)/2))],bins=nbins))[0]:
				vec.append(x/(len(jointi)/2))	
			for x in (np.histogram(yz[(int(len(jointi)/2)):(int(len(jointi)))],bins=nbins))[0]:
				vec.append(x/(len(jointi)/2))
				
			for x in (np.histogram(xz,bins=nbins))[0]:
				vec.append(x/len(jointi))	
			for x in (np.histogram(xz[0:(int(len(jointi)/2))],bins=nbins))[0]:
				vec.append(x/(len(jointi)/2))	
			for x in (np.histogram(xz[(int(len(jointi)/2)):(int(len(jointi)))],bins=nbins))[0]:
				vec.append(x/(len(jointi)/2))
				
		print(str(len(vec)))
		new_vec=[]
		num=1
		new_vec.append(file[1:3])
		for val in vec:
			new_vec.append(str(num)+":"+str(val))
			num+=1
		print(str(len(new_vec)))
		for val in new_vec:
			outfile.write(" "+val)
		outfile.write("\n")

choice = input("Would you like to run HOD on train(1) or test(2)?")

if (int(choice)==1):
	print("Running HOD on the Training Data")
	outfile = open("hod_d1", "w")
	HOD("train")
	outfile.close()
	print("Completed HOD on the Training Data")
elif (int(choice)==2):
	print("Running HOD on the Test Data")
	outfile = open("hod_d1.t", "a+")
	HOD("test")
	outfile.close()
	print("Completed HOD on the Test Data")
elif (int(choice)==3):
	print("Running HOD on the both folders")
	outfile = open("hod_d1", "w")
	HOD("train")
	outfile.close()
	print("Completed HOD on the Training Data")
	outfile = open("hod_d1.t", "a+")
	HOD("test")
	outfile.close()
	print("Completed HOD on the Test Data")




