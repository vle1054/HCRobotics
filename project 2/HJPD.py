import os, string, math
import numpy as np
import matplotlib.pyplot as plt

path = os.getcwd().replace ('\\','/') + '/dataset/'

            
def HJPD(folder ="test"):
	temp = np.zeros((20,3))
	folder_ = path + folder #Path to selected folder
	files = os.listdir(folder_)
	nbins = 5
	for file in files: #Scan through files
		instance = np.loadtxt(folder_ +"/"+ file)
		distance1 = np.zeros((int(len(instance)/20)))
		distance2 = np.zeros((int(len(instance)/20)))
		distance3 = np.zeros((int(len(instance)/20)))
		distance4 = np.zeros((int(len(instance)/20)))
		distance5 = np.zeros((int(len(instance)/20)))
		distance6 = np.zeros((int(len(instance)/20)))
		distance7 = np.zeros((int(len(instance)/20)))
		distance8 = np.zeros((int(len(instance)/20)))
		distance9 = np.zeros((int(len(instance)/20)))
		distance10 = np.zeros((int(len(instance)/20)))
		distance11 = np.zeros((int(len(instance)/20)))
		distance12 = np.zeros((int(len(instance)/20)))
		distance13 = np.zeros((int(len(instance)/20)))
		distance14 = np.zeros((int(len(instance)/20)))
		distance15 = np.zeros((int(len(instance)/20)))
		distance16 = np.zeros((int(len(instance)/20)))
		distance17 = np.zeros((int(len(instance)/20)))
		distance18 = np.zeros((int(len(instance)/20)))
		distance19 = np.zeros((int(len(instance)/20)))

		i = 0
		for frame in instance:
			if frame[1] != 20:
				temp[int(frame[1])-1] = frame[2:5]
			elif frame[1] ==20:
				temp[int(frame[1])-1] = frame[2:5]
				distance1[i] = distance1[i-1] if math.isnan(np.linalg.norm(temp[1]-temp[0])) else np.linalg.norm(temp[1]-temp[0])
				distance2[i] = distance2[i-1] if math.isnan(np.linalg.norm(temp[2]-temp[0])) else np.linalg.norm(temp[2]-temp[0])
				distance3[i] = distance3[i-1] if math.isnan(np.linalg.norm(temp[3]-temp[0])) else np.linalg.norm(temp[3]-temp[0])
				distance4[i] = distance4[i-1] if math.isnan(np.linalg.norm(temp[4]-temp[0])) else np.linalg.norm(temp[4]-temp[0])
				distance5[i] = distance5[i-1] if math.isnan(np.linalg.norm(temp[5]-temp[0])) else np.linalg.norm(temp[5]-temp[0])
				distance6[i] = distance6[i-1] if math.isnan(np.linalg.norm(temp[6]-temp[0])) else np.linalg.norm(temp[6]-temp[0])
				distance7[i] = distance7[i-1] if math.isnan(np.linalg.norm(temp[7]-temp[0])) else np.linalg.norm(temp[7]-temp[0])
				distance8[i] = distance8[i-1] if math.isnan(np.linalg.norm(temp[8]-temp[0])) else np.linalg.norm(temp[8]-temp[0])
				distance9[i] = distance9[i-1] if math.isnan(np.linalg.norm(temp[9]-temp[0])) else np.linalg.norm(temp[9]-temp[0])
				distance10[i] = distance10[i-1] if math.isnan(np.linalg.norm(temp[10]-temp[0])) else np.linalg.norm(temp[10]-temp[0])
				distance11[i] = distance11[i-1] if math.isnan(np.linalg.norm(temp[11]-temp[0])) else np.linalg.norm(temp[11]-temp[0])
				distance12[i] = distance12[i-1] if math.isnan(np.linalg.norm(temp[12]-temp[0])) else np.linalg.norm(temp[12]-temp[0])
				distance13[i] = distance13[i-1] if math.isnan(np.linalg.norm(temp[13]-temp[0])) else np.linalg.norm(temp[13]-temp[0])
				distance14[i] = distance14[i-1] if math.isnan(np.linalg.norm(temp[14]-temp[0])) else np.linalg.norm(temp[14]-temp[0])
				distance15[i] = distance15[i-1] if math.isnan(np.linalg.norm(temp[15]-temp[0])) else np.linalg.norm(temp[15]-temp[0])
				distance16[i] = distance16[i-1] if math.isnan(np.linalg.norm(temp[16]-temp[0])) else np.linalg.norm(temp[16]-temp[0])
				distance17[i] = distance17[i-1] if math.isnan(np.linalg.norm(temp[17]-temp[0])) else np.linalg.norm(temp[17]-temp[0])
				distance18[i] = distance18[i-1] if math.isnan(np.linalg.norm(temp[18]-temp[0])) else np.linalg.norm(temp[18]-temp[0])
				distance19[i] = distance19[i-1] if math.isnan(np.linalg.norm(temp[19]-temp[0])) else np.linalg.norm(temp[19]-temp[0])
				i = i + 1
		vec=[]
		for x in (np.histogram(distance1,bins=nbins))[0]:
			vec.append(x/i)
		for x in (np.histogram(distance2,bins=nbins))[0]:
			vec.append(x/i)	
		for x in (np.histogram(distance3,bins=nbins))[0]:
			vec.append(x/i)	
		for x in (np.histogram(distance4,bins=nbins))[0]:
			vec.append(x/i)	
		for x in (np.histogram(distance5,bins=nbins))[0]:
			vec.append(x/i)
		for x in (np.histogram(distance6,bins=nbins))[0]:
			vec.append(x/i)
		for x in (np.histogram(distance7,bins=nbins))[0]:
			vec.append(x/i)	
		for x in (np.histogram(distance8,bins=nbins))[0]:
			vec.append(x/i)	
		for x in (np.histogram(distance9,bins=nbins))[0]:
			vec.append(x/i)	
		for x in (np.histogram(distance10,bins=nbins))[0]:
			vec.append(x/i)	
		for x in (np.histogram(distance11,bins=nbins))[0]:
			vec.append(x/i)
		for x in (np.histogram(distance12,bins=nbins))[0]:
			vec.append(x/i)	
		for x in (np.histogram(distance13,bins=nbins))[0]:
			vec.append(x/i)	
		for x in (np.histogram(distance14,bins=nbins))[0]:
			vec.append(x/i)	
		for x in (np.histogram(distance15,bins=nbins))[0]:
			vec.append(x/i)	
		for x in (np.histogram(distance16,bins=nbins))[0]:
			vec.append(x/i)
		for x in (np.histogram(distance17,bins=nbins))[0]:
			vec.append(x/i)	
		for x in (np.histogram(distance18,bins=nbins))[0]:
			vec.append(x/i)	
		for x in (np.histogram(distance19,bins=nbins))[0]:
			vec.append(x/i)	

		new_vec=[]
		num=1
		new_vec.append(file[1:3])
		for val in vec:
			new_vec.append(str(num)+":"+str(val))
			num+=1

		for val in new_vec:    
			outfile.write(" "+val)
		outfile.write("\n")
            
choice = input("Would you like to run HJPD on train(1) or test(2)?")

if (int(choice)==1):
	print("Running HJPD on the Training Data")
	outfile = open("hjpd_d1", "w")
	HJPD("train")
	outfile.close()
	print("Completed HJPD on the Training Data")
elif (int(choice)==2):
	print("Running HJPD on the Test Data")
	outfile = open("hjpd_d1.t", "a+")
	HJPD("test")
	outfile.close()
	print("Completed HJPD on the Test Data")
