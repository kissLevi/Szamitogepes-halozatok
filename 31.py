#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import stat
filenames = []
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
            if(re.search(".prog",(os.path.join(name)))):
                filenames.append(os.path.join(name).replace(".prog",""))
for i in range(len(filenames)):
        f = open(filenames[i]+".prog", "r")
        f2 = open(filenames[i]+".py", "w")
        for line in f:
                m= line.split("{")
                m2 = line.split(";;")
                if (len(m)) == 2:
                    if (re.search("CIKLUS",line)):
                        f2.write(m[0].replace("CIKLUS", "for")+":"+"\n")
                        n = m[1].split(";;")
                        for i in range(0,len(n)):
                            if (re.search("}",n[i])):
                                f2.write("    "+n[i].replace("}",""))
                            else :
                                f2.write("    "+n[i]+"\n")
                    elif (re.search("ELAGAZAS",line)):
                        f2.write(m[0].replace("ELAGAZAS", "if")+":"+"\n")
                        n = m[1].split(";;")
                        for i in range(0,len(n)):
                            if (re.search("}",n[i])):
                                f2.write("    "+n[i].replace("}",""))
                            else :
                                f2.write("    "+n[i]+"\n")
                elif (len(m2)) == 2:
                    f2.write(m2[0]+"\n")
                    f2.write(m2[1])
                else :
                    f2.write(line)


