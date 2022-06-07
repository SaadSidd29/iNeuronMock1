from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
import sys

def replace(oriFile, textToReplace, replacedText):

    #Create temporay file
    fh, tempFile = mkstemp()
    
    try:
        with fdopen(fh,'w') as new_file:
            with open(oriFile) as old_file:
                for line in old_file:
                    new_file.write(line.replace(textToReplace, replacedText))

        #Copy the file permissions
        copymode(oriFile, tempFile)

        #Remove original file
        remove(oriFile)

        #Move new file
        move(tempFile, oriFile)

        old_file.close()
        new_file.close()

        print("Changes Done")

    except:
        print(sys.exc_info()[0], "occurred.")




replace('example.txt','placement','screening')

