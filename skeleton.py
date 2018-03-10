import os, string, math
import numpy as np

path = os.getcwd().replace ('\\','/') + '/dataset/'

def angle_between(a, b, c):
    ba = a - b
    bc = c - b
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    return angle = np.arccos(cosine_angle)

def RAD (folder = "Train"):
    folder_ = path + folder #Path to selected folder
    files = os.listdir(folder_)
    for file in files: #Scan through files
        instance = np.loadtxt(file)
        for frame in instance:
            if frame[1] == 1:
                temp[0] == frame[3:5]
            else if frame[1] == 4:
                temp[1] == frame[3:5]
            else if frame[1] == 7:
                temp[2] == frame[3:5]
            else if frame[1] == 11:
                temp[3] == frame[3:5]
            else if frame[1] == 15:
                temp[4] == frame[3:5]
            else if frame[1] == 19:
                temp[5] == frame[3:5]
            else if frame[1] ==20;
                Distance = (np.linalg.norm(temp[1]-temp[0]),\
                np.linalg.norm(temp[2]-temp[0]),\
                np.linalg.norm(temp[3]-temp[0]),\
                np.linalg.norm(temp[4]-temp[0]),\
                np.linalg.norm(temp[5]-temp[0]))
                Angle = (angle_between(temp[4],temp[1],temp[11]),\
                angle_between(temp[11],temp[1],temp[19]),\
                angle_between(temp[19],temp[1],temp[15]),\
                angle_between(temp[15],temp[1],temp[7],\
                angle_between(temp[7],temp[1],temp[4]))
                Result[frame[0]]= (Distance,Angle)
