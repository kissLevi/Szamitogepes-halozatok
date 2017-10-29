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
            if (len(m)) > 2:
                if (re.search("CIKLUS",line)):
                    f2.write(m[0].replace("CIKLUS", "for")+":")             
                    for i in range(1,len(m)):
                        n = m[i].split(";;")
                        g = 0
                        for i in range(len(n)):
                            if (re.search("CIKLUS",n[i])):
                                f2.write("\n"+"    "+n[i].replace("CIKLUS", "for")+":")
                            elif (re.search("ELAGAZAS",n[i])):
                                f2.write("\n"+"    "+n[i].replace("ELAGAZAS", "if")+":")
                            elif (g == 0 and re.search("}",n[i])):
                                f2.write("\n"+"        "+n[i].replace("}",""))
                                g = 1
                            elif (g == 1 and re.search("}",n[i])):
                                f2.write("\n"+"    "+n[i].replace("}",""))
                                g = 1
                            else :
                                f2.write("\n"+"    "+n[i])
                elif (re.search("ELAGAZAS",line)):
                    f2.write(m[0].replace("ELAGAZAS", "if")+":")             
                    for i in range(1,len(m)):
                        n = m[i].split(";;")
                        g = 0
                        for i in range(len(n)):
                            if (re.search("CIKLUS",n[i])):
                                f2.write("\n"+"    "+n[i].replace("CIKLUS", "for")+":")
                            elif (re.search("ELAGAZAS",n[i])):
                                f2.write("\n"+"    "+n[i].replace("ELAGAZAS", "if")+":")
                            elif (g == 0 and re.search("}",n[i])):
                                f2.write("\n"+"        "+n[i].replace("}",""))
                                g = 1
                            elif (g == 1 and re.search("}",n[i])):
                                f2.write("    "+n[i].replace("}",""))
                                g = 1
                            else :
                                f2.write("\n"+"    "+n[i])
            elif (len(m)) == 2:
                        if (re.search("CIKLUS",line)):
                            f2.write("\n"+m[0].replace("CIKLUS", "for")+":")
                            n = m[1].split(";;")
                            for i in range(0,len(n)):
                                if (re.search("}",n[i])):
                                    f2.write("    "+n[i].replace("}",""))
                                else :
                                    f2.write("    "+n[i]+"\n")
                        elif (re.search("ELAGAZAS",line)):
                            f2.write("\n"+m[0].replace("ELAGAZAS", "if")+":")
                            n = m[1].split(";;")
                            for i in range(0,len(n)):
                                if (re.search("}",n[i])):
                                    f2.write("\n"+"    "+n[i].replace("}",""))
                                else :
                                    f2.write("\n"+"    "+n[i])      
            elif line[0] != "\n":
                  for i in range(len(m2)) :
                        f2.write(m2[i])
                        f2.write("\n")
       

