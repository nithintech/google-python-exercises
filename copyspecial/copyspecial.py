#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):                      #return files like__(\w)__types...and print absolue path of those files
  res=[]
  lis=os.listdir(dir)
  #print lis
  for i in lis:
      m=re.search(r'(\w+)__(\w+)__(.)(\w+)',i)
      if m:
          new=os.path.join(dir,i)
           res.append(os.path.abspath(new))


def copy_to(filelist,newdir):
  if not os.path.exists(newdir):
    os.mkdir(newdir)
  for i in filelist:
    filename=os.path.basename(i)
    shutil.copy(path,os.path.join(newdir,filename))

def zip_to(filelist,zipfile):
  cmd='zip -j' +zipfile+' '+' '.join(filelist)
  print "command is:"+ cmd
  (status,output)=commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write(output)
    sys.exit(1)






def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  filelist=[]
  for k in args:
    filelist.extend(get_special_paths(dir))

  if todir:
    copy_to(filelist,newdir)
  elif tozip:
    zip_to(filelist,zipto)
  else:
    '\n'.join(filelist)


  
  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
