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
            
def HOD(folder ="test"):
    temp = np.zeros((6,3))
    folder_ = path + folder #Path to selected folder
    files = os.listdir(folder_)

    for file in files: #Scan through files
        instance = np.loadtxt(folder_ +"/"+ file)
        distance1 = np.zeros((int(len(instance)/20)),3)
        distance2 = np.zeros((int(len(instance)/20)),3)
        distance3 = np.zeros((int(len(instance)/20)),3)
        distance4 = np.zeros((int(len(instance)/20)),3)
        distance5 = np.zeros((int(len(instance)/20)),3)
        distance6 = np.zeros((int(len(instance)/20)),3)
        distance7 = np.zeros((int(len(instance)/20)),3)
        distance8 = np.zeros((int(len(instance)/20)),3)
        distance9 = np.zeros((int(len(instance)/20)),3)
        distance10 = np.zeros((int(len(instance)/20)),3)
        distance11 = np.zeros((int(len(instance)/20)),3)
        distance12 = np.zeros((int(len(instance)/20)),3)
        distance13 = np.zeros((int(len(instance)/20)),3)
        distance14 = np.zeros((int(len(instance)/20)),3)
        distance15 = np.zeros((int(len(instance)/20)),3)
        distance16 = np.zeros((int(len(instance)/20)),3)
        distance17 = np.zeros((int(len(instance)/20)),3)
        distance18 = np.zeros((int(len(instance)/20)),3)
        distance19 = np.zeros((int(len(instance)/20)),3)
        angle1 = np.zeros((int(len(instance)/20)))
        angle2 = np.zeros((int(len(instance)/20)))
        angle3 = np.zeros((int(len(instance)/20)))
        angle4 = np.zeros((int(len(instance)/20)))
        angle5 = np.zeros((int(len(instance)/20)))
        angle6 = np.zeros((int(len(instance)/20)))
        angle7 = np.zeros((int(len(instance)/20)))
        angle8 = np.zeros((int(len(instance)/20)))
        angle9 = np.zeros((int(len(instance)/20)))
        angle10 = np.zeros((int(len(instance)/20)))
        angle11 = np.zeros((int(len(instance)/20)))
        angle12 = np.zeros((int(len(instance)/20)))
        angle13 = np.zeros((int(len(instance)/20)))
        angle14 = np.zeros((int(len(instance)/20)))
        angle15 = np.zeros((int(len(instance)/20)))
        angle16 = np.zeros((int(len(instance)/20)))
        angle17 = np.zeros((int(len(instance)/20)))
        angle18 = np.zeros((int(len(instance)/20)))
        angle19 = np.zeros((int(len(instance)/20)))
        
        hdata1 = np.zeros((int(len(instance)/20)))
        hdata2 = np.zeros((int(len(instance)/20)))
        hdata3 = np.zeros((int(len(instance)/20)))
        hdata4 = np.zeros((int(len(instance)/20)))
        hdata5 = np.zeros((int(len(instance)/20)))
        hdata6 = np.zeros((int(len(instance)/20)))
        hdata7 = np.zeros((int(len(instance)/20)))
        hdata8 = np.zeros((int(len(instance)/20)))
        hdata9 = np.zeros((int(len(instance)/20)))
        hdata10 = np.zeros((int(len(instance)/20)))
        hdata11 = np.zeros((int(len(instance)/20)))
        hdata12 = np.zeros((int(len(instance)/20)))
        hdata13 = np.zeros((int(len(instance)/20)))
        hdata14 = np.zeros((int(len(instance)/20)))
        hdata15 = np.zeros((int(len(instance)/20)))
        hdata16 = np.zeros((int(len(instance)/20)))
        hdata17 = np.zeros((int(len(instance)/20)))
        hdata18 = np.zeros((int(len(instance)/20)))
        hdata19 = np.zeros((int(len(instance)/20)))
        i = 0
        for frame in instance:
            if frame[1] != 20:
                temp[int(frame[1])-1] = frame[2:5]
            elif frame[1] ==20:
                distance1[i] = distance1[i-1] if math.isnan(np.linalg.norm(temp[1]-temp[0])) else\
                ((math.hypot(temp[1][0]-temp[0][0],temp[1][1]-temp[0][1])), (math.hypot(temp[1][1]-temp[0][1],temp[1][2]-temp[0][2])),(math.hypot(temp[1][0]-temp[0][0],temp[1][2]-temp[0][2])))
                distance2[i] = distance2[i-1] if math.isnan(np.linalg.norm(temp[2]-temp[0])) else\
                ((math.hypot(temp[2][0]-temp[0][0],temp[2][1]-temp[0][1])), (math.hypot(temp[2][1]-temp[0][1],temp[2][2]-temp[0][2])),(math.hypot(temp[2][0]-temp[0][0],temp[2][2]-temp[0][2])))
                distance3[i] = distance3[i-1] if math.isnan(np.linalg.norm(temp[3]-temp[0])) else \
                ((math.hypot(temp[3][0]-temp[0][0],temp[3][1]-temp[0][1])), (math.hypot(temp[3][1]-temp[0][1],temp[3][2]-temp[0][2])),(math.hypot(temp[3][0]-temp[0][0],temp[3][2]-temp[0][2])))
                distance4[i] = distance4[i-1] if math.isnan(np.linalg.norm(temp[4]-temp[0])) else \
                ((math.hypot(temp[4][0]-temp[0][0],temp[4][1]-temp[0][1])), (math.hypot(temp[4][1]-temp[0][1],temp[4][2]-temp[0][2])),(math.hypot(temp[4][0]-temp[0][0],temp[4][2]-temp[0][2])))
                distance5[i] = distance5[i-1] if math.isnan(np.linalg.norm(temp[5]-temp[0])) else \
                ((math.hypot(temp[5][0]-temp[0][0],temp[5][1]-temp[0][1])), (math.hypot(temp[5][1]-temp[0][1],temp[5][2]-temp[0][2])),(math.hypot(temp[5][0]-temp[0][0],temp[5][2]-temp[0][2])))
                distance6[i] = distance6[i-1] if math.isnan(np.linalg.norm(temp[6]-temp[0])) else\
                ((math.hypot(temp[6][0]-temp[0][0],temp[6][1]-temp[0][1])), (math.hypot(temp[6][1]-temp[0][1],temp[6][2]-temp[0][2])),(math.hypot(temp[6][0]-temp[0][0],temp[2][2]-temp[0][2])))
                distance7[i] = distance7[i-1] if math.isnan(np.linalg.norm(temp[7]-temp[0])) else \
                ((math.hypot(temp[7][0]-temp[0][0],temp[7][1]-temp[0][1])), (math.hypot(temp[7][1]-temp[0][1],temp[7][2]-temp[0][2])),(math.hypot(temp[7][0]-temp[0][0],temp[3][2]-temp[0][2])))
                distance8[i] = distance8[i-1] if math.isnan(np.linalg.norm(temp[8]-temp[0])) else \
                ((math.hypot(temp[8][0]-temp[0][0],temp[8][1]-temp[0][1])), (math.hypot(temp[8][1]-temp[0][1],temp[8][2]-temp[0][2])),(math.hypot(temp[8][0]-temp[0][0],temp[4][2]-temp[0][2])))
                distance9[i] = distance9[i-1] if math.isnan(np.linalg.norm(temp[9]-temp[0])) else \
                ((math.hypot(temp[9][0]-temp[0][0],temp[9][1]-temp[0][1])), (math.hypot(temp[9][1]-temp[0][1],temp[9][2]-temp[0][2])),(math.hypot(temp[9][0]-temp[0][0],temp[5][2]-temp[0][2])))
                distance10[i] = distance10[i-1] if math.isnan(np.linalg.norm(temp[10]-temp[0])) else\
                ((math.hypot(temp[10][0]-temp[0][0],temp[10][1]-temp[0][1])), (math.hypot(temp[10][1]-temp[0][1],temp[10][2]-temp[0][2])),(math.hypot(temp[10][0]-temp[0][0],temp[2][2]-temp[0][2])))
                distance11[i] = distance11[i-1] if math.isnan(np.linalg.norm(temp[11]-temp[0])) else \
                ((math.hypot(temp[11][0]-temp[0][0],temp[11][1]-temp[0][1])), (math.hypot(temp[11][1]-temp[0][1],temp[11][2]-temp[0][2])),(math.hypot(temp[11][0]-temp[0][0],temp[3][2]-temp[0][2])))
                distance12[i] = distance12[i-1] if math.isnan(np.linalg.norm(temp[12]-temp[0])) else \
                ((math.hypot(temp[12][0]-temp[0][0],temp[12][1]-temp[0][1])), (math.hypot(temp[12][1]-temp[0][1],temp[12][2]-temp[0][2])),(math.hypot(temp[12][0]-temp[0][0],temp[4][2]-temp[0][2])))
                distance13[i] = distance13[i-1] if math.isnan(np.linalg.norm(temp[13]-temp[0])) else \
                ((math.hypot(temp[13][0]-temp[0][0],temp[13][1]-temp[0][1])), (math.hypot(temp[13][1]-temp[0][1],temp[13][2]-temp[0][2])),(math.hypot(temp[13][0]-temp[0][0],temp[5][2]-temp[0][2])))
                distance14[i] = distance14[i-1] if math.isnan(np.linalg.norm(temp[14]-temp[0])) else\
                ((math.hypot(temp[14][0]-temp[0][0],temp[14][1]-temp[0][1])), (math.hypot(temp[14][1]-temp[0][1],temp[14][2]-temp[0][2])),(math.hypot(temp[14][0]-temp[0][0],temp[2][2]-temp[0][2])))
                distance15[i] = distance15[i-1] if math.isnan(np.linalg.norm(temp[15]-temp[0])) else \
				((math.hypot(temp[15][0]-temp[0][0],temp[15][1]-temp[0][1])), (math.hypot(temp[15][1]-temp[0][1],temp[15][2]-temp[0][2])),(math.hypot(temp[15][0]-temp[0][0],temp[3][2]-temp[0][2])))
				distance16[i] = distance16[i-1] if math.isnan(np.linalg.norm(temp[16]-temp[0])) else \
				((math.hypot(temp[16][0]-temp[0][0],temp[16][1]-temp[0][1])), (math.hypot(temp[16][1]-temp[0][1],temp[16][2]-temp[0][2])),(math.hypot(temp[16][0]-temp[0][0],temp[4][2]-temp[0][2])))
				distance17[i] = distance17[i-1] if math.isnan(np.linalg.norm(temp[17]-temp[0])) else \
				((math.hypot(temp[17][0]-temp[0][0],temp[17][1]-temp[0][1])), (math.hypot(temp[17][1]-temp[0][1],temp[17][2]-temp[0][2])),(math.hypot(temp[17][0]-temp[0][0],temp[5][2]-temp[0][2])))
				distance18[i] = distance18[i-1] if math.isnan(np.linalg.norm(temp[18]-temp[0])) else\
				((math.hypot(temp[18][0]-temp[0][0],temp[18][1]-temp[0][1])), (math.hypot(temp[18][1]-temp[0][1],temp[18][2]-temp[0][2])),(math.hypot(temp[18][0]-temp[0][0],temp[2][2]-temp[0][2])))
				distance19[i] = distance19[i-1] if math.isnan(np.linalg.norm(temp[19]-temp[0])) else \
				((math.hypot(temp[19][0]-temp[0][0],temp[19][1]-temp[0][1])), (math.hypot(temp[19][1]-temp[0][1],temp[19][2]-temp[0][2])),(math.hypot(temp[19][0]-temp[0][0],temp[3][2]-temp[0][2])))
				angle1[i] = angle1[i-1] if math.isnan(np.linalg.norm(temp[1]-temp[0])) else\
				math.atan(temp[1][1]-temp[0][1]/temp[1][0]-temp[0][0])
				angle2[i] = angle2[i-1] if math.isnan(np.linalg.norm(temp[2]-temp[0])) else\
				math.atan(temp[2][1]-temp[0][1]/temp[2][0]-temp[0][0])
				angle3[i] = angle3[i-1] if math.isnan(np.linalg.norm(temp[3]-temp[0])) else \
				math.atan(temp[3][1]-temp[0][1]/temp[3][0]-temp[0][0])
				angle4[i] = angle4[i-1] if math.isnan(np.linalg.norm(temp[4]-temp[0])) else \
				math.atan(temp[4][1]-temp[0][1]/temp[4][0]-temp[0][0])
				angle5[i] = angle5[i-1] if math.isnan(np.linalg.norm(temp[5]-temp[0])) else \
				math.atan(temp[5][1]-temp[0][1]/temp[5][0]-temp[0][0])
				angle6[i] = angle6[i-1] if math.isnan(np.linalg.norm(temp[6]-temp[0])) else\
				math.atan(temp[6][1]-temp[0][1]/temp[6][0]-temp[0][0])
				angle7[i] = angle7[i-1] if math.isnan(np.linalg.norm(temp[7]-temp[0])) else \
				math.atan(temp[7][1]-temp[0][1]/temp[7][0]-temp[0][0])
				angle8[i] = angle8[i-1] if math.isnan(np.linalg.norm(temp[8]-temp[0])) else \
				math.atan(temp[8][1]-temp[0][1]/temp[8][0]-temp[0][0])
				angle9[i] = angle9[i-1] if math.isnan(np.linalg.norm(temp[9]-temp[0])) else \
				math.atan(temp[9][1]-temp[0][1]/temp[9][0]-temp[0][0])
				angle10[i] = angle10[i-1] if math.isnan(np.linalg.norm(temp[10]-temp[0])) else\
				math.atan(temp[10][1]-temp[0][1]/temp[10][0]-temp[0][0])
				angle11[i] = angle11[i-1] if math.isnan(np.linalg.norm(temp[11]-temp[0])) else \
				math.atan(temp[11][1]-temp[0][1]/temp[11][0]-temp[0][0])
				angle12[i] = angle12[i-1] if math.isnan(np.linalg.norm(temp[12]-temp[0])) else \
				math.atan(temp[12][1]-temp[0][1]/temp[12][0]-temp[0][0])
				angle13[i] = angle13[i-1] if math.isnan(np.linalg.norm(temp[13]-temp[0])) else \
				math.atan(temp[13][1]-temp[0][1]/temp[13][0]-temp[0][0])
				angle14[i] = angle14[i-1] if math.isnan(np.linalg.norm(temp[14]-temp[0])) else\
				math.atan(temp[14][1]-temp[0][1]/temp[14][0]-temp[0][0])
				angle15[i] = angle15[i-1] if math.isnan(np.linalg.norm(temp[15]-temp[0])) else \
				math.atan(temp[15][1]-temp[0][1]/temp[15][0]-temp[0][0])
				angle16[i] = angle16[i-1] if math.isnan(np.linalg.norm(temp[16]-temp[0])) else \
				math.atan(temp[16][1]-temp[0][1]/temp[16][0]-temp[0][0])
				angle17[i] = angle17[i-1] if math.isnan(np.linalg.norm(temp[17]-temp[0])) else \
				math.atan(temp[17][1]-temp[0][1]/temp[17][0]-temp[0][0])
				angle18[i] = angle18[i-1] if math.isnan(np.linalg.norm(temp[18]-temp[0])) else\
				math.atan(temp[18][1]-temp[0][1]/temp[18][0]-temp[0][0])
				angle19[i] = angle19[i-1] if math.isnan(np.linalg.norm(temp[19]-temp[0])) else \
                math.atan(temp[19][1]-temp[0][1]/temp[19][0]-temp[0][0])
                
                hdata1[i] = angle1[i]*distance1[i][0]/360
                hdata2[i] = angle2[i]*distance2[i][0]/360
                hdata3[i] = angle3[i]*distance3[i][0]/360
                hdata4[i] = angle4[i]*distance4[i][0]/360
                hdata5[i] = angle5[i]*distance5[i][0]/360
                hdata6[i] = angle6[i]*distance6[i][0]/360
                hdata7[i] = angle7[i]*distance7[i][0]/360
                hdata8[i] = angle8[i]*distance8[i][0]/360
                hdata9[i] = angle9[i]*distance9[i][0]/360
                hdata10[i] = angle10[i]*distance10[i][0]/360
                hdata11[i] = angle11[i]*distance11[i][0]/360
                hdata12[i] = angle12[i]*distance12[i][0]/360
                hdata13[i] = angle13[i]*distance13[i][0]/360
                hdata14[i] = angle14[i]*distance14[i][0]/360
                hdata15[i] = angle15[i]*distance15[i][0]/360
                hdata16[i] = angle16[i]*distance16[i][0]/360
                hdata17[i] = angle17[i]*distance17[i][0]/360
                hdata18[i] = angle18[i]*distance18[i][0]/360
                hdata19[i] = angle19[i]*distance19[i][0]/360
                i = i + 1
                 
        hdata1, hdata1bin, hdata1patch = plt.hist(hdata1, bins=8) 
        hdata1[:] = [x / i for x in hdata1]
        hdata2, hdata1bin, hdata1patch = plt.hist(hdata2, bins=8) 
        hdata2[:] = [x / i for x in hdata2]
        hdata3, hdata1bin, hdata1patch = plt.hist(hdata3, bins=8) 
        hdata3[:] = [x / i for x in hdata3]
        hdata4, hdata1bin, hdata1patch = plt.hist(hdata4, bins=8) 
        hdata4[:] = [x / i for x in hdata4]
        hdata5, hdata1bin, hdata1patch = plt.hist(hdata5, bins=8) 
        hdata5[:] = [x / i for x in hdata5]
        hdata6, hdata1bin, hdata1patch = plt.hist(hdata6, bins=8) 
        hdata6[:] = [x / i for x in hdata6]
        hdata7, hdata1bin, hdata1patch = plt.hist(hdata7, bins=8) 
        hdata7[:] = [x / i for x in hdata7]
        hdata8, hdata1bin, hdata1patch = plt.hist(hdata8, bins=8) 
        hdata8[:] = [x / i for x in hdata8]
        hdata9, hdata1bin, hdata1patch = plt.hist(hdata9, bins=8) 
        hdata9[:] = [x / i for x in hdata9]
        hdata10, hdata1bin, hdata1patch = plt.hist(hdata10, bins=8) 
        hdata10[:] = [x / i for x in hdata10]
        hdata11, hdata1bin, hdata1patch = plt.hist(hdata11, bins=8) 
        hdata11[:] = [x / i for x in hdata11]
        hdata12, hdata1bin, hdata1patch = plt.hist(hdata12, bins=8) 
        hdata12[:] = [x / i for x in hdata12]
        hdata13, hdata1bin, hdata1patch = plt.hist(hdata13, bins=8) 
        hdata13[:] = [x / i for x in hdata13]
        hdata14, hdata1bin, hdata1patch = plt.hist(hdata14, bins=8) 
        hdata14[:] = [x / i for x in hdata14]
        hdata15, hdata1bin, hdata1patch = plt.hist(hdata15, bins=8) 
        hdata15[:] = [x / i for x in hdata15]
        hdata16, hdata1bin, hdata1patch = plt.hist(hdata16, bins=8) 
        hdata16[:] = [x / i for x in hdata16]
        hdata17, hdata1bin, hdata1patch = plt.hist(hdata17, bins=8) 
        hdata17[:] = [x / i for x in hdata17]
        hdata18, hdata1bin, hdata1patch = plt.hist(hdata18, bins=8) 
        hdata18[:] = [x / i for x in hdata18]
        hdata19, hdata1bin, hdata1patch = plt.hist(hdata19, bins=8) 
        hdata19[:] = [x / i for x in hdata19]

		if folder == "train":
			fh = open("hod_d1", "a+")
			myString = " ".join(str(hdata1)) +" ".join(str(hdata2))+" ".join(str(hdata3))+" ".join(str(hdata4))+\
			" ".join(str(hdata5)) +" ".join(str(hdata6)) +" ".join(str(hdata7))+" ".join(str(hdata8))+\
			" ".join(str(hdata9))+" ".join(str(hdata10))+" ".join(str(hdata11)) +" ".join(str(hdata12))+\
			" ".join(str(hdata13))+" ".join(str(hdata14))+" ".join(str(hdata15))+" ".join(str(hdata16)) +\
			" ".join(str(hdata17))+" ".join(str(hdata18))+" ".join(str(hdata19))
			fh.write(myString + "\n")
			fh.close
		elif folder == "test":
			fh = open("hod_d1.t", "a+")
			myString = " ".join(str(hdata1)) +" ".join(str(hdata2))+" ".join(str(hdata3))+" ".join(str(hdata4))+\
			" ".join(str(hdata5)) +" ".join(str(hdata6)) +" ".join(str(hdata7))+" ".join(str(hdata8))+\
			" ".join(str(hdata9))+" ".join(str(hdata10))+" ".join(str(hdata11)) +" ".join(str(hdata12))+\
			" ".join(str(hdata13))+" ".join(str(hdata14))+" ".join(str(hdata15))+" ".join(str(hdata16)) +\
			" ".join(str(hdata17))+" ".join(str(hdata18))+" ".join(str(hdata19))
			fh.write(myString + "\n")
			fh.close
      
            
        
RAD("test")
#RAD("train")
#HJPD("test")
#HJPD("train")
#HOD("test")
#HOD("train")