import os, string, math
import numpy as np
import matplotlib.pyplot as plt

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
        dhist1, dhist1bin, dhist1patch = plt.hist(distance1, bins=5) 
        dhist1[:] = [x / i for x in dhist1]
        dhist2, dhist2bin, dhist2patch = plt.hist(distance2, bins=5) 
        dhist2[:] = [x / i for x in dhist2]
        dhist3, dhist3bin, dhist3patch = plt.hist(distance3, bins=5) 
        dhist3[:] = [x / i for x in dhist3]
        dhist4, dhist4bin, dhist4patch = plt.hist(distance4, bins=5) 
        dhist4[:] = [x / i for x in dhist4]
        dhist5, dhist5bin, dhist5patch = plt.hist(distance5, bins=5) 
        dhist5[:] = [x / i for x in dhist5]

        ahist1, ahist1bin, ahist1patch = plt.hist(angle1, bins=5) 
        ahist1[:] = [x / i for x in ahist1]
        ahist2, ahist2bin, ahist2patch = plt.hist(angle2, bins=5) 
        ahist2[:] = [x / i for x in ahist2]
        ahist3, ahist3bin, ahist3patch = plt.hist(angle3, bins=5) 
        ahist3[:] = [x / i for x in ahist3]
        ahist4, ahist4bin, ahist4patch = plt.hist(angle4, bins=5) 
        ahist4[:] = [x / i for x in ahist4]
        ahist5, ahist5bin, ahist5patch = plt.hist(angle5, bins=5) 
        ahist5[:] = [x / i for x in ahist5]

        if folder == "train":
            fh = open("rad_d1", "a+")
            myString = " ".join(str(dhist1)) +" ".join(str(dhist2))+" ".join(str(dhist3))+" ".join(str(dhist4))+" ".join(str(dhist5))\
                        +" ".join(str(ahist1))+" ".join(str(ahist2))+" ".join(str(ahist3))+" ".join(str(ahist4))+" ".join(str(ahist5))
            fh.write(myString + "\n")
            fh.close
        elif folder == "test":
            fh = open("rad_d1.t", "a+")
            myString = " ".join(str(dhist1)) +" ".join(str(dhist2))+" ".join(str(dhist3))+" ".join(str(dhist4))+" ".join(str(dhist5))\
                        +" ".join(str(ahist1))+" ".join(str(ahist2))+" ".join(str(ahist3))+" ".join(str(ahist4))+" ".join(str(ahist5))
            fh.write(myString + "\n")
            fh.close
            
def HJPD(folder ="test"):
    temp = np.zeros((20,3))
    folder_ = path + folder #Path to selected folder
    files = os.listdir(folder_)

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
        dhist1, dhist1bin, dhist1patch = plt.hist(distance1, bins=5) 
        dhist1[:] = [x / i for x in dhist1]
        dhist2, dhist2bin, dhist2patch = plt.hist(distance2, bins=5) 
        dhist2[:] = [x / i for x in dhist2]
        dhist3, dhist3bin, dhist3patch = plt.hist(distance3, bins=5) 
        dhist3[:] = [x / i for x in dhist3]
        dhist4, dhist4bin, dhist4patch = plt.hist(distance4, bins=5) 
        dhist4[:] = [x / i for x in dhist4]
        dhist5, dhist5bin, dhist5patch = plt.hist(distance5, bins=5) 
        dhist5[:] = [x / i for x in dhist5]        
        dhist6, dhist6bin, dhist6patch = plt.hist(distance6, bins=5) 
        dhist6[:] = [x / i for x in dhist6]
        dhist7, dhist7bin, dhist7patch = plt.hist(distance7, bins=5) 
        dhist7[:] = [x / i for x in dhist7]
        dhist8, dhist8bin, dhist8patch = plt.hist(distance8, bins=5) 
        dhist8[:] = [x / i for x in dhist8]
        dhist9, dhist9bin, dhist9patch = plt.hist(distance9, bins=5) 
        dhist9[:] = [x / i for x in dhist9]
        dhist10, dhist10bin, dhist10patch = plt.hist(distance10, bins=5) 
        dhist10[:] = [x / i for x in dhist10]
        dhist11, dhist11bin, dhist11patch = plt.hist(distance11, bins=5) 
        dhist11[:] = [x / i for x in dhist11]
        dhist12, dhist12bin, dhist12patch = plt.hist(distance12, bins=5) 
        dhist12[:] = [x / i for x in dhist12]
        dhist13, dhist13bin, dhist13patch = plt.hist(distance13, bins=5) 
        dhist13[:] = [x / i for x in dhist13]
        dhist14, dhist14bin, dhist14patch = plt.hist(distance14, bins=5) 
        dhist14[:] = [x / i for x in dhist14]
        dhist15, dhist15bin, dhist15patch = plt.hist(distance15, bins=5) 
        dhist15[:] = [x / i for x in dhist15]
        dhist16, dhist16bin, dhist16patch = plt.hist(distance16, bins=5) 
        dhist16[:] = [x / i for x in dhist16]
        dhist17, dhist17bin, dhist17patch = plt.hist(distance17, bins=5) 
        dhist17[:] = [x / i for x in dhist17]
        dhist18, dhist18bin, dhist18patch = plt.hist(distance18, bins=5) 
        dhist18[:] = [x / i for x in dhist18]
        dhist19, dhist19bin, dhist19patch = plt.hist(distance19, bins=5) 
        dhist19[:] = [x / i for x in dhist19]
       
        if folder == "train":
            fh = open("hjpd_d1", "a+")
            myString = " ".join(str(dhist1)) +" ".join(str(dhist2))+" ".join(str(dhist3))+" ".join(str(dhist4))+\
            " ".join(str(dhist5)) +" ".join(str(dhist6)) +" ".join(str(dhist7))+" ".join(str(dhist8))+\
            " ".join(str(dhist9))+" ".join(str(dhist10))+" ".join(str(dhist11)) +" ".join(str(dhist12))+\
            " ".join(str(dhist13))+" ".join(str(dhist14))+" ".join(str(dhist15))+" ".join(str(dhist16)) +\
            " ".join(str(dhist17))+" ".join(str(dhist18))+" ".join(str(dhist19))
            fh.write(myString + "\n")
            fh.close
        elif folder == "test":
            fh = open("hjpd_d1.t", "a+")
            myString = " ".join(str(dhist1)) +" ".join(str(dhist2))+" ".join(str(dhist3))+" ".join(str(dhist4))+\
            " ".join(str(dhist5)) +" ".join(str(dhist6)) +" ".join(str(dhist7))+" ".join(str(dhist8))+\
            " ".join(str(dhist9))+" ".join(str(dhist10))+" ".join(str(dhist11)) +" ".join(str(dhist12))+\
            " ".join(str(dhist13))+" ".join(str(dhist14))+" ".join(str(dhist15))+" ".join(str(dhist16)) +\
            " ".join(str(dhist17))+" ".join(str(dhist18))+" ".join(str(dhist19))
            fh.write(myString + "\n")
            fh.close
            
    
        
RAD("test")
#RAD("train")
#HJPD("test")
#HJPD("train")
#HOD("test")
#HOD("train")