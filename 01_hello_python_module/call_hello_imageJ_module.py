import hello_imageJ_module as him
# hello_imageJ_module.py must be saved in `.../Fiji.app/jars/Lib/` folder

# List all possible functions
print dir(him)

# You can run your function like this
print him.helloImageJ("normic")
print him.helloImageJ_upper("normic")

# Alternatively
from hello_imageJ_module import helloImageJ
helloImageJ("normic")


