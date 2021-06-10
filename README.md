# imageJ_ScriptParameters
Here are some simple examples on how to use imagej macros and script parameters to simplify imageJ macros

# Hello world
You can write imageJ macros in any of the script languages with parameters to define input and output.

If you save this scirpt in the plugins folder '.../Fiji.app/plugins/' you can call your script using the imageJ GUI or using the  'run' function in your macros

# Make your own python module and import functions from it
1. Make a folder in the '.../Fiji.app/jars/' folder called 'Lib'.
1. save your macro containing your functions there
```python
def helloImageJ(name):
	print "hello", name

def helloImageJ_upper(name):
	print "hello", (name.upper())
```
1. restart imageJ
1. import your module to a new script

```python
import myModule

``` 

* if you only need one function from your script you can import only that
```python
from hello_imageJ_module import helloImageJ
helloImageJ("normic")
```
