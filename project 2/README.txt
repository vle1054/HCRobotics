A README that provides sufficient instructions needed
to compile and execute your code. Your README also
needs to document your implementation information,
for example, including which joints are used in the RAD
representation, and how the histograms are computed
and how many bins are used in your HJPD and HOD
representations.


The code is written in Python3, to run the code place the skeleton.py file into a folder containing
the reduced dataset. To change the function and output access the skeleton.py file and change the 
function call at the end. The functions are RAD, HJPD, and HOD. The parameters for the functions
are "train" and "test".
So to run the RAD for the test folder change the command to RAD("test").


For RAD Joint 1 is the center and Joints 4 ,7 ,11 ,15 ,19 was chosen as extremities

For the HJPD histograms are computed using the distance between the center joint 
and the other joints the numpy.linalg.norm function was used to determine the distance, there
are 5 bins

For the HOD histograms are computed using angle(xy)*distance(xy)/360 there are 8 bins
There are indent errors in the HOD section

