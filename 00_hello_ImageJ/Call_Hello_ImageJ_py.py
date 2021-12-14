from ij import IJ

#A test dataset
test_data = ["person 1", "person 2", "person 3", "person 4"]

# make greetings 
for name in test_data:
	IJ.run("Hello imageJ py", "name=[" + name + "]")

