from ij import IJ

#A test dataset
test_data = ["person 1", "person 2", "person 3", "person 4"]

# make greetings 
g = IJ.run("Hello imageJ py", "name=[person 4]")
print g

#print [n for n in test_data]