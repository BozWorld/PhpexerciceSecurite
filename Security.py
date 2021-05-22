import os
from os import close

with open("result", "a") as r:
    r.write("here is the result of the analysis of php file \n " + "\n")
close

dir = r'D:\projects\repoGithub\PhpexerciceSecurite\plugin_wordpress\wp-mobile-detector'

for file in os.listdir(dir):
    if file.endswith(".php"):
        path = dir + "\\" + file
        phpFile = open(path)
        for line in phpFile:
            if line.find("$_GET") != -1 or line.find("$_PUT") != -1 or line.find("$_POST")!= -1 or line.find("$_REQUEST")!= -1:
                with open("result", "a") as r:
                    r.write("in " + file + " there is this request who can cause security issue: \n" + line + "\n")
                close