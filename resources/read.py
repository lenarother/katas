#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    read.py

    Open articles online. 
    Single tab, no distractions, just focus.

    Usage: python read.py salt
"""    

import sys
from selenium import webdriver

RESOURCES = {
'salt': 'https://docs.saltstack.com/en/latest/topics/tutorials/walkthrough.html',
'salt2': 'https://docs.saltstack.com/en/latest/topics/tutorials/pillar.html',
}

class ResourceManager:

    def __init__(self):
        self.resources = RESOURCES

    def play(self, name):
        """
        Play given playslist.
        When name is not awailable print s all possibilities.
        """
        if not name in self.resources.keys():#self.playlists.has_key(name):
            self.show_available()
        else:
            #import subprocess
            #DETACHED_PROCESS = 0x00000008
            #p = subprocess.Popen(["python", "browser.py"],
            #           stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            #p.communicate()
            browser = webdriver.Firefox()
            browser.get(self.resources[name])
            
    def show_available(self):
        """Prints available articles."""
        for li in self.resources.keys():
            print(li)



def main():
    resources = ResourceManager()
    if len(sys.argv) > 1:
        name = ''.join(sys.argv[1:])
        name = name.lower()
        if name == 'show':
            resources.show_available()
        else:
            resources.play(name)
        
            
if __name__ == '__main__':
    main()
        
