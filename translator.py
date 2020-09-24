#!/usr/bin/env python3

import re

print("Hello World")
fin = open("termsOfService.txt", "r")
fout = open("output.txt", "w")
fout2 = open("outeput2.txt", "w")
fout3 = open("output3.txt", "w")
Lines = fin.readlines()

firstDegree = " \d+\. "
secondDegree = " \d+\.\d+\. "
thrirdDegree = " \d+\.\d+\.\d+\. " 

secondDegreeHelper = "\"\"\"]"
#secondX = re.search(secondDegree, line)
#thirdX = re.search(thrirdDegree, line)

degree = 0

for line in Lines:
    x = re.search(firstDegree, line)
    if x :
        if degree == 0:
           degree = degree + 1
           line2 = re.sub(firstDegree, "ol[][li[][text \"\"\"", line)
           fout.write(line2)
        else:
           line2 = re.sub(firstDegree, " \"\"\"] \\n    , li[][text \"\"\"", line)
           fout.write(line2)
    else:
        fout.write(line)

fout.write("\"\"\"]]")

fin.close()
fout.close()


fin2 = open("output.txt", "r")
fout2 = open("output2.txt", "w")

degree = 0

Lines2 = fin2.readlines()
for line2 in Lines2:
    secondX = re.search(secondDegree, line2)
    secondX2 = re.search(secondDegreeHelper, line2)
    if secondX :
        if degree == 0:
           degree = degree + 1
           line2 = re.sub(secondDegree, " \"\"\" \\n      , ol[][li[][text \"\"\"", line2)
           fout2.write(line2)

        else:
           line2 = re.sub(secondDegree, " \"\"\"] \\n          , li[][text \"\"\"", line2)
           fout2.write(line2)

    elif secondX2 :
        if degree == 1:
           line2 = re.sub(secondDegreeHelper, " \"\"\"] ] ] ", line2)
           fout2.write(line2)
           degree = degree -1
        else: 
           fout2.write(line2)
    else:
        fout2.write(line2)



fin2.close()
fout2.close()

fin3 = open("output2.txt", "r")
fout3 = open("output3.txt", "w")

degree = 0
thirdDegreeHelper = "\"\"\"] ] ]"

thirdDegreeHelper2 = "\"\"\"]"

thirdDegree = " \d+\.\d+\.\d+\. " 

Lines3 = fin3.readlines()
for line3 in Lines3:
    thirdX = re.search(thirdDegree, line3)
    thirdX2 = re.search(thirdDegreeHelper, line3)
    thirdX21 = re.search(thirdDegreeHelper2, line3)
    if thirdX :
        if degree == 0:
           degree = degree + 1
           line3 = re.sub(thirdDegree, " \"\"\" \\n      , ol[][li[][text \"\"\"", line3)
           fout3.write(line3)

        else:
           line3 = re.sub(thirdDegree, " \"\"\"] \\n          , li[][text \"\"\"", line3)
           fout3.write(line3)

    elif thirdX21:
        if degree == 1:
           line3 = re.sub(thirdDegreeHelper2, " \"\"\"] ] ] ", line3)
           fout3.write(line3)
           degree = degree -1
        else: 
           fout3.write(line3)

    elif thirdX2 :
        if degree == 1:
           line3 = re.sub(thirdDegreeHelper, " \"\"\"] ] ] ] ] ", line3)
           fout3.write(line3)
           degree = degree -1
        else: 
           fout3.write(line3)
    else:
        fout3.write(line3)



fin3.close()
fout3.close()


fin4 = open("output3.txt", "r")
fout4 = open("output4.txt", "w")

degree = 0
forthDegreeHelper = "\"\"\"] ] ]"

forthDegreeHelper2 = "\"\"\"]"

forthDegree = " \d+\.\d+\.\d+\. " 

Lines4 = fin4.readlines()
for line4 in Lines4:
    forthX = re.search(forthDegree, line4)
    forthX2 = re.search(forthDegreeHelper, line4)
    forthX21 = re.search(forthDegreeHelper2, line4)
    if forthX :
        if degree == 0:
           degree = degree + 1
           line4 = re.sub(forthDegree, " \"\"\" \\n      , ol[][li[][text \"\"\"", line4)
           fout4.write(line4)

        else:
           line4 = re.sub(forthdDegree, " \"\"\"] \\n          , li[][text \"\"\"", line4)
           fout4.write(line4)

    elif thirdX21:
        if degree == 1:
           line4 = re.sub(thirdDegreeHelper2, " \"\"\"] ] ] ", line4)
           fout4.write(line4)
           degree = degree -1
        else: 
           fout4.write(line4)

    elif thirdX2 :
        if degree == 1:
           line4 = re.sub(thirdDegreeHelper, " \"\"\"] ] ] ] ] ", line4)
           fout4.write(line4)
           degree = degree -1
        else: 
           fout3.write(line4)
    else:
        fout3.write(line4)



fin3.close()
fout3.close()











