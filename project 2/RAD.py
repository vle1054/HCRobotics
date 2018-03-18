import os, string, math
import numpy as np

path = os.getcwd().replace ('\\','/') + '/dataset/'

def angle_between(a, b, c):
    ba = a - b
    bc = c - b
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    return np.arccos(cosine_angle)

def RAD(folder ="test"):
	temp = np.zeros((6,3))
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
		angle1 = np.zeros((int(len(instance)/20)))
		angle2 = np.zeros((int(len(instance)/20)))
		angle3 = np.zeros((int(len(instance)/20)))
		angle4 = np.zeros((int(len(instance)/20)))
		angle5 = np.zeros((int(len(instance)/20)))
		i = 0
		for frame in instance:
			if frame[1] == 1:
				temp[0] = frame[2:5]
			elif frame[1] == 4:
				temp[1] = frame[2:5]
			elif frame[1] == 7:
				temp[2] = frame[2:5]
			elif frame[1] == 11:
				temp[3] = frame[2:5]
			elif frame[1] == 15:
				temp[4] = frame[2:5]
			elif frame[1] == 19:
				temp[5] = frame[2:5]
			elif frame[1] ==20:
				distance1[i] = distance1[i-1] if math.isnan(np.linalg.norm(temp[1]-temp[0])) else np.linalg.norm(temp[1]-temp[0])
				distance2[i] = distance2[i-1] if math.isnan(np.linalg.norm(temp[2]-temp[0])) else np.linalg.norm(temp[2]-temp[0])
				distance3[i] = distance3[i-1] if math.isnan(np.linalg.norm(temp[3]-temp[0])) else np.linalg.norm(temp[3]-temp[0])
				distance4[i] = distance4[i-1] if math.isnan(np.linalg.norm(temp[4]-temp[0])) else np.linalg.norm(temp[4]-temp[0])
				distance5[i] = distance5[i-1] if math.isnan(np.linalg.norm(temp[5]-temp[0])) else np.linalg.norm(temp[5]-temp[0])
				angle1[i] = angle1[i-1] if math.isnan(angle_between(temp[1],temp[0],temp[3])) else angle_between(temp[1],temp[0],temp[3])
				angle2[i] = angle2[i-1] if math.isnan(angle_between(temp[3],temp[0],temp[5])) else angle_between(temp[3],temp[0],temp[5])
				angle3[i] = angle3[i-1] if math.isnan(angle_between(temp[5],temp[0],temp[4])) else angle_between(temp[5],temp[0],temp[4])
				angle4[i] = angle4[i-1] if math.isnan(angle_between(temp[4],temp[0],temp[2])) else angle_between(temp[4],temp[0],temp[2])
				angle5[i] = angle5[i-1] if math.isnan(angle_between(temp[2],temp[0],temp[1])) else angle_between(temp[2],temp[0],temp[1])
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
		for x in (np.histogram(angle1,bins=nbins))[0]:
			vec.append(x/i)
		for x in (np.histogram(angle2,bins=nbins))[0]:
			vec.append(x/i)
		for x in (np.histogram(angle3,bins=nbins))[0]:
			vec.append(x/i)
		for x in (np.histogram(angle4,bins=nbins))[0]:
			vec.append(x/i)
		for x in (np.histogram(angle5,bins=nbins))[0]:
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

choice = input("Would you like to run RAD on train(1) or test(2)?")

if (int(choice)==1):
	print("Running RAD on the Training Data")
	outfile = open("rad_d1", "w")
	RAD("train")
	outfile.close()
	print("Completed RAD on the Training Data")
elif (int(choice)==2):
	print("Running RAD on the Test Data")
	outfile = open("rad_d1.t", "a+")
	RAD("test")
	outfile.close()
	print("Completed RAD on the Test Data")
elif (int(choice)==3):
	print("Running RAD on the both folders")
	outfile = open("rad_d1", "w")
	RAD("train")
	outfile.close()
	print("Completed RAD on the Training Data")
	outfile = open("rad_d1.t", "a+")
	RAD("test")
	outfile.close()
	print("Completed RAD on the Test Data")
