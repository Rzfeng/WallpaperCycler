import time
from appscript import app, mactypes
print "What photo do you want to set?"
photoLocation = raw_input("Please enter the directory\n")
app('Finder').desktop_picture.set(mactypes.File(photoLocation))
print "What time do you want to set?"
time = raw_input("Use the form: 08:20\n")
print "What date do you want to set?"
date = raw_input("Use the form: mm/dd/yyyy\n")
