#!/usr/bin/env python
import os, string, math, sys
import numpy as np
from svm import *
from svmutil import *
from subprocess import *
from grid import *

if len(sys.argv) <= 1:
	print('Usage: {0} training_file [testing_file]'.format(sys.argv[0]))
	raise SystemExit

train_pathname = sys.argv[1]
assert os.path.exists(train_pathname),"training file not found"
file_name = os.path.split(train_pathname)[1]
train_file = file_name 

if len(sys.argv) > 2:
	test_pathname = sys.argv[2]
	file_name = os.path.split(test_pathname)[1]
	assert os.path.exists(test_pathname),"testing file not found"
	test_file = file_name 


rate, param = find_parameters(train_file,"")


y, x = svm_read_problem(train_file)
prob = svm_problem(y, x)


parameters = "-c "+ str(param['c']) +" -g " + str(param['g'])

m = svm_train(prob, parameters)

y2, x2 = svm_read_problem(test_file)

p_labels, p_acc, p_vals = svm_predict(y2, x2, m)

tv=[]
pv=[]
fopen = open(str(test_file), "r")

fline = fopen.readlines()


fmat = open(str(test_file)+".cmatrix", "w")

for line in fline:
	tv.append(str(line[1:3]))
	fmat.write(" "+str(line[1:3]))
fmat.write("\n")
for x in p_labels:
	pv.append(x)
	fmat.write(" "+str(x))
fopen.close()
fmat.close()

print(param)
print (rate)

