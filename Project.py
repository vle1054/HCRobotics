import os, string, math, copy, random

from datetime import datetime
random.seed(datetime.now()) #set random seed

path = os.getcwd().replace ('\\','/') + '/20_newsgroups/'

#Ask for classification type
print ('If you would like to select your own folders go in to the python code and insert the folder names, otherwise folders will be selected at random.\n') 
number = input('Would you like to use Binary Classification or Tri-class Classification? (Use 2 or 3, up to 20 for multi-class Classification)\n')

folder_list = os.listdir(path)
selected_folders = random.sample(folder_list, number)


#----------------Specify folders here-------------------------------
#select your own folders by uncommenting and changing the following
#selected_folders =['talk.religion.misc','talk.politics.misc']
#selected_folders =['rec.sport.baseball','soc.religion.christian']
#selected_folders =['talk.religion.misc','talk.politics.misc','talk.politics.mideast']

str1 = ' and '.join(selected_folders)
print ("The selected folders/classes are: "+str1+"\n") #Print out selected folders

training_set = input("How many files would you like to use in the training set? (Set count 1000) \n")

#-----------------------Training-------------------------------------

training = {} #Dictionary of Dictionary of Trained data
file_name ={} #Dictionary of file names

print ("Training...")

for folder in selected_folders:
    Trained = {} #Dictionary of Trained data
    folder_ = path + folder #Path to selected folder
    files = os.listdir(folder_)
    trainsample = random.sample(files, training_set) #Random sampling of the files
    for file in trainsample: #Iterate through sampling
        data = open(folder_ + '/'+file,'r').read().lower()#Read fild and normalize to lower case
        words = data.split(' ')
        for word in words:
            if word == ' ' or word == '':
                continue
            value = Trained.get(word, 0)
            if value == 0:
                Trained[word] = 1
            else:
                Trained[word] = value + 1
        files.remove(file) #Remove from file list
    file_name[folder] = files #Save to dictionary
    training[folder] = Trained #Save to dictionary

#------------------------------Testing----------------------------------

print ("Testing...")

folder_list = copy.deepcopy(selected_folders) #Copy selected folders to list
count = 0
success = 0
for folder in folder_list:#iterate through folder list
    folder_name = folder
    if len(file_name[folder_name])== 0: #if file list in folder is empty remove folder
        folder_list.remove(folder_name)
    else:
        for file in file_name[folder_name]: #iterate through files in folder
            file_name[folder_name].remove(file)
            group = folder_name #Actual Group
            data = open(path + folder_name + '/'+ file,'r').read().lower()
            count = count + 1
            if data =='NULL':
                break
            words = data.split(' ')
            if '' in words: #get rid of blank spaces
                words.remove('')
            if ' ' in words:
                words.remove(' ')
            probabilities = []
            for check in selected_folders:#evaluate the probability
                sum_ = sum(training[check].values())
                probability = 0.0
                for w in words:
                    value = training[check].get(w, 0.0) + .00001
                    probability = probability + math.log(float(value)/float(sum_))
                probabilities.append(probability)
            if group == selected_folders[probabilities.index(max(probabilities))]: #If sucessful classification add one
                success = success + 1   
    group = 'NULL'
if ((float(success)/float(count - 1)*100) > 100):
	result = 100
else:
	result = (float(success)/float(count - 1)*100)
print ('The success rate is = %.1f'% result +"%") #Get the percentage of correct guesses

