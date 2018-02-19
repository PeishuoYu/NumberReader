# Update 02/19/2018
#	Added dataSet size constraint and tree depth constraint against overfitting
#		You can see how to use them in instructions
#
#	Note: These two features are not for the purpose of number recognition, since no
#	      different numbers are written in the same way, there are always differences.
#	      These two features are more for general machine learning purpose
#
#
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
#	image example\		some image examples, you can see the weight of strokes 
#
#
# Why develping this program:
#
# 	Recently I learned a machine learning algorithm in my data mining and predictive analytics
# 	class. I wanted to implement this algorithm with Python using my knowledge in data structure 
# 	and algorithm. After I developed a program that can solve the simple problem in textbook, I 
# 	wanted to apply this algorithm to a more complicated setting, so I selected hand-written 
# 	number recognation as my topic. To speed up sample generation, I learned how to use PIL 
# 	package to read and manipulate images. Finally, I made this program.
#
#
# Instructions:
#
#	Draw new number and make prediction (and possibly sample generation):
# 		1) open "Paint" application in Windows and draw a number, save it as "test.png" 
#		   under the number folder, the PNG should be a SQUARE image
# 		2) run the makePrediction function, the program will make prediction based on 
#		   image and model
# 		3) after the prediction is made, the program will prompt you to enter the right 
#		   answer, if you enter the answer, this prediction example will be saved in 
#		   training set, if you prefer not to save the prediction example to the training 
#		   set, just press 'enter' and the program will close
# 
#	Training:
# 		1) you can train the model using the training() function, it will automatically 
# 		   train the model based on the sample provided (those saved in numbers folder)
#		2) constraints against overfitting 
#		   eg. training(minnum=20,maxdepth=5)
#		       this tells us each sorted dataSet will has at least 20 pieces of data
#		       and the maximum depth of the trees (attributes) will be 5
# 	
#	Sample Statistics:
#		sampleResult() will tell you the number of samples of different Numbers ('0' - '9')
#
#
# Model example:
#
#	[{'740': '0', '585': '0', '1374': '1', '1174': '0'}, '8', 43, 17, 2.2826030623075226]
#
#		1) position 740, 585, and 490 have to be black, position 1374 has to be white.
#		2) based on the samples that fit the requirements, the model thinks the number is '8'.
#		3) there are 43 pieces of data that fit this requirement, and 17 of them are '8'.
#		4) the entropy of this dataSet it 2.2826, which is far from 0, this means the model
#	   	   is not quite sure about the prediction made.
#	In a model, there are a lot of sets like the one above.
#
#
# Sample example:
#
#	1111111111111111111111111111111111111111
#	1111111111111111111111111111111111111111
#	1111111111111111111111111111111111111111
#	1111111111111111111111111111111111111111
#	1111111111111111111111111111111111111111
#	1111111111111111111111111111111111111111
#	1111111111000000000111111111111111111111
#	1111111110000000000011111111111111111111
#	1111111111000000000001111111111111111111
#	1111111111000000000001111111111111111111
#	1111111111100000000000111111111111111111
#	1111111111111111000000011111111111111111
#	1111111111111111100000011111111111111111
#	1111111111111111100000011111111111111111
#	1111111111111111110000011111111111111111
#	1111111111111111100000011111111111111111
#	1111111111111111100000011111111111111111
#	1111111111111111000000111111111111111111
#	1111111111111110000000111111111111111111
#	1111111111111100000001111111111111111111
#	1111111111111000000001111111111111111111
#	1111111111100000000011111111111111111111
#	1111111111000000000111111111111111111111
#	1111111100000000001111111111111111111111
#	1111111000000000111111111111111111111111
#	1111110000000001111111111111111111111111
#	1111100000000011111111111111111100000011
#	1111100000000000000000000000000000000011
#	1111100000000000000000000000000000000011
#	1111110000000000000000000000000000000011
#	1111110000000000000000000000000000000011
#	1111111111000000000000000000000000000011
#	1111111111111111111111111111111111111111
#	1111111111111111111111111111111111111111
#	1111111111111111111111111111111111111111
#	1111111111111111111111111111111111111111
#	1111111111111111111111111111111111111111
#	1111111111111111111111111111111111111111
#	1111111111111111111111111111111111111111
#	1111111111111111111111111111111111111111
#	2
#
#	40*40 grid, 0s represent black, 1s represent white, right prediction at the end
#