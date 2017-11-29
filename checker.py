#!/usr/bin/env python3
""" Little script that reads from a file packages that are requried for something (whatever) and compare the name to what's installed in the system [Slackware] """

import os
import sys
import subprocess

requiredPath = "./thing"
packagesPath = "/var/log/packages"

def get_file_content(filename):
    if os.path.exists(filename):
        with open(filename,'r') as f:
            return f.read()
    else:
        print("There's been an error with the path to the file containing the requried packages")
        sys.exit(1)

def get_packages(path):
    #pkgs = subprocess.check_output(['ls',packages_path])
    pkgs = subprocess.run(["ls", path],check=True,stdout=subprocess.PIPE)
    pkgs = pkgs.stdout.splitlines()
    return pkgs

#installed = subprocess.run(["ls",packages_path],check=True,stdout=subprocess.PIPE)
#installed = installed.stdout.splitlines()


def start_check(pathToPackages,pathToRequirements):

    if (os.path.exists(pathToPackages)) and (os.path.exists(pathToRequirements)):
        installed = get_packages(pathToPackages)
        required = get_file_content(pathToRequirements).split()

        for i in range(len(required)):
            isit = False
            for j in range(len(installed)):
                if required[i] in installed[j].decode('utf8').strip():
                    isit = True
                    print("{} is installed, {}".format(required[i].ljust(20), installed[j].decode() ))
                    continue
            if not isit:
                print("{} isn't isntalled".format(required[i]))
    else:
        print("Please check on the provided paths")

if __name__ == "__main__":
    start_check(packagesPath,requiredPath)


