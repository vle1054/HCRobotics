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
scaled_file = file_name + ".scale"
model_file = file_name + ".model"
range_file = file_name + ".range"

if len(sys.argv) > 2:
	test_pathname = sys.argv[2]
	file_name = os.path.split(test_pathname)[1]
	assert os.path.exists(test_pathname),"testing file not found"
	scaled_test_file = file_name + ".scale"
	predict_test_file = file_name + ".predict"


rate, param = find_parameters(file_name,"")


y, x = svm_read_problem(file_name)
prob = svm_problem(y, x)


m = svm_train(prob, param)

p_labels, p_acc, p_vals = svm_predict(y, x, m)
