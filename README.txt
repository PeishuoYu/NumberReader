# Number reader:
# This is a program in which I applied machine learning algorithm to recognize hand-written number
# After being trained with more than 1000 samples, it is relative accurate now
#
# In this folder, there are:
#	numbers\
#		0.txt		sample data with the right prediction at the end (part of training set)
#		..txt		same as 0.txt
#		test.png	the image of number that is used to make prediction
#		test.txt	the 0s and 1s that represent the test.png
#		sample.txt	a single file that has all the data of the training set
#		model.txt	the file that is used to record a pre-established model
#	node.py			the Python file that can train the model and make prediction
#
# Why develping this program:
# Recently I learned a machine learning algorithm in my data mining and predictive analytics
# class. I wanted to implement this algorithm with Python using my knowledge in data structure 
# and algorithm. After I developed a program that can solve the simple problem in textbook, I 
# wanted to apply this algorithm to a more complicated setting, so I selected hand-written 
# number recognation as my topic. To speed up sample generation, I learned how to use PIL 
# package to read and manipulate images. Finally, I made this program.
#
# Instruction:
# open "Paint" application in Windows and draw a number, save it as "test.png" under the number folder
# the PNG should be a square image
# run the makePrediction function, after the prediction is made, enter the right answer
# when you think you have enough samples, you can train the model using the training() function
# sampleResult() will tell you the number of samples of different 'Numbers'' ('0' - '9')

