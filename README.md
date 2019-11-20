# image2gif
This script stitches together a directory of pictures into a gif. You should be able to run it from the command line. The flags are as follows:

-r --root This is a path. This is the path to the directory containing pictures to be stitched together.

-o --output This is a filename. This is the filename and extension the gif will be saved as. The gif will be saved one directory up from root. Currently only gif is supported. Eg. test.gif

-t --time This is a floating point number. This is the amount of time each picture will be displayed for. The minimum is 0.02 seconds.

-e -every This is an integer. This is how frequently an image gets added to the gif. Eg. 5 will add every fifth picture.

Example: python image2gif.py -r C:/Users/Desktop/pics -o test.gif -t 0.5 -e 10

This will look on the desktop for a directory named "pics". It will save a file called test.gif to C:/Users/Desktop. Each frame will take 0.5 seconds and every tenth picture will be used.

This script has imageio as a dependancy. You can install it by opening a console and writing: pip install imageio.
It also uses sys, os, and but I beleive they are all standard modules. 

Known issues:
1. The paths to the pictures uses os.listdir(). This means that if non-image files are in the directory specified to the -r flag the program will crash! Also, os.listdir() does not guarantee a specifc order to the file names so the gif might not be in order.
