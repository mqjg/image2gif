"""
This script stitches together a directory of pictures into a gif. You should be able to run it from the command line. The flags are as follows:
-r --root This is a path. This is the path to the directory containing pictures to be stitched together.
-o --output This is a filename. This is the filename and extension the gif will be saved as. The gif will be saved one directory up from root. Currently only gif is supported. Eg. test.gif
-t --time This is a floating point number. This is the amount of time each picture will be displayed for. The minimum is 0.02 seconds.
-e -every This is an integer. This is how frequently an image gets added to the gif. Eg. 5 will add every fifth picture.

Example: python image2gif.py -r C:/Users/Desktop/pics -o test.gif -t 0.5 -e 10
This will look on the desktop for a directory named "pics". It will save a file called test.gif to C:/Users/Desktop. Each frame will take 0.5 seconds and every tenth picture will be used.

This script has imageio as a dependancy. You can install it by opening a console and writing: pip install imageio.

It also uses sys, os, and but I beleive they are all standard modules. 
"""

import imageio
import argparse
import sys
import os

def image2gif(dirLoc, savename, framerate, addEvery):
    os.chdir(dirLoc)
    filenames = os.listdir()
    with imageio.get_writer("../"+savename, mode='I', duration = str(framerate)) as writer:
        for i in range(0,len(filenames),addEvery):
            image = imageio.imread(filenames[i])
            writer.append_data(image)

def checkInput(root, output, time, every):
    """
    This function checks the quality of the inputs. Returns true if all is well, false otherwise.
    """
    if not os.path.exists(root):
        print("Invalid path. The given source directory (the -r argument) could not be found.")
        return False
    if os.path.exists(os.path.join(root,"..",output)):
        print("File already exists. The given output filename (the -o flag) already has a file associated with it.")
        return False

    try:
        float(time)
    except ValueError:
        print("Given time (the -t flag) is not a valid floating point number.")
        return False
    if float(time) < 0.02:
        print("Given time (the -t flag) is less than the minimum of 0.02.")

    try:
        float(every)
    except ValueError:
        print("Given every (the -e flag) is not a valid integer.")
        return False

    return True

if __name__ == '__main__': #this means "If called from the command line"
    
    parse=argparse.ArgumentParser()
    parse.add_argument("-r", "--root", dest="root", help="A path. The path to the directory containing pictures.")
    parse.add_argument("-o", "--output", dest="output", help="A filename including the extension. The filename the new gif will be saved as. It needs a .gif extension. Eg. test.gif")
    parse.add_argument("-t", "--time", dest="time", help="A number. The amount of time each picture should be displayed for. This is the inverse of the framerate. The minimum is 0.02 seconds. Also, wierd numbers may just result in the default of 0.1 seconds.")
    parse.add_argument("-e", "--every", dest="every", help="A number. This is the frequency with with which images are added. Eg. 5 will using every fifth image.")
    args = parse.parse_args()

    if checkInput(args.root, args.output, args.time, args.every):
        image2gif(args.root, args.output, args.time, int(args.every))