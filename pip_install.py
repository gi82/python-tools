# -*- coding: utf-8 -*-
__author__ = "Ioannis Georgiou"


try:
    from pip import main as pipmain
except:
    from pip._internal import main as pipmain
import os

import sys

class PipInstaller():
    default_package_repository_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "package_repos")
    def __init__(self,package_repos=default_package_repository_path):
        print (package_repos)
        self.package_repos = package_repos
    def install(self,package):
        # Debugging
        # pip.main(["install", "--pre", "--upgrade", "--no-index",
        #         "--find-links=.", package, "--log-file", "log.txt", "-vv"])
        
        pipmain(["install","--upgrade", "--no-index", "--find-links={}".format(self.package_repos), package])
        pass

    def uninstall(self,package):
        response = input("Uninstall '%s'? [y/n]:\n".format(package))
        if "y" in response.lower():
            # Debugging
            # pip.main(["uninstall", package, "-vv"])
            pip.main(["uninstall", package])
        pass

if __name__ == "__main__":    
    print ("Reading from repository '{package_repos}'".format(package_repos=PipInstaller.default_package_repository_path))
    package_name = ["yourpackagename"]

    for package in package_name:    
        PipInstaller().install(package)
    input("Press Enter to Exit...\n")    
