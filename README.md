Examples of how to use imageJ macros

# imageJ_ScriptParameters
Here are some simple examples on how to use script parameters to simplify input for imageJ macros

[Example script parameters](https://github.com/oodegard/imageJ_ScriptParameters/blob/main/00_hello_ImageJ/Example_script_parameters.ijm)
```java
#@ String (visibility=MESSAGE, value="PERSONAL INFO") msg1
#@ String (label = "Your name")  name
#@ Date (label = "Date of birth") dob
#@ ColorRGB (label = "Favorite color", default = "255,0,204") rgb
#@ String (visibility=MESSAGE, value="PROGRAMMING SKILLS") msg2
#@ Integer(label = "Programming experience", min = 1, max = 10, style = "slider") prog_exp
#@ Boolean (label = "Process subfolders") subfolders
#@ String (visibility=MESSAGE, value="OUTPUT") msg3
#@ File (label="Select a directory", style="directory") myDir
```
# Hello world
You can write imageJ macros in any of the script languages with parameters to define input and output.

[Hello imageJ](https://github.com/oodegard/imageJ_ScriptParameters/blob/main/00_hello_ImageJ/Hello_imageJ_py.py)
```java
#@ String(label = "Your name") name
#@ OUTPUT String greeting

## Hello ImageJ 
greeting = "Hello, " + str(name) + "!"
#print(greeting)
```
If you save this scirpt in the plugins folder `.../Fiji.app/plugins/` you can call your script using the imageJ GUI or using the  `run` function in your macros

[Call Hello ImageJpy](https://github.com/oodegard/imageJ_ScriptParameters/blob/main/00_hello_ImageJ/Call_Hello_ImageJ_py.py)
```python
from ij import IJ

#A test dataset
test_data = ["person 1", "person 2", "person 3", "person 4"]

# make greetings 
for name in test_data:
	print(IJ.run("Hello imageJ py", "name=[" + name + "]"))
```

# Save usefull functions in modules that you can import from other imageJ macros
* Make a folder in the `.../Fiji.app/jars/` folder called `Lib`.
* save your macro containing your functions there
[hello_imageJ_module](https://github.com/oodegard/imageJ_ScriptParameters/blob/main/Lib/hello_imageJ_module.py)
```python
def helloImageJ(name):
	print "hello", name

def helloImageJ_upper(name):
	print "hello", (name.upper())
```
* restart imageJ
* import your module to a new script

[call_hello_imageJ_module](https://github.com/oodegard/imageJ_ScriptParameters/blob/main/01_hello_python_module/call_hello_imageJ_module.py)
```python
import hello_imageJ_module as him
# hello_imageJ_module.py must be saved in `.../Fiji.app/jars/Lib/` folder

# List all possible functions
print dir(him)

# You can run your function like this
him.helloImageJ("normic")
him.helloImageJ_upper("normic")
``` 
if you only need one function from your module you can import only that
```python
from hello_imageJ_module import helloImageJ
helloImageJ("normic")
```
