// A test dataset
test_data = newArray(4);
test_data[0] = "person 1";
test_data[1] = "person 2";
test_data[2] = "person 3";
test_data[3] = "person 4";

// Loop trough test_data list
// Call Hello_ImageJ.ijm for each name
for (i = 0; i < test_data.length; i++) {
	run("Hello imageJ", "name=[" + test_data[i]  + "]");
}