#!/usr/bin/env python

#Should prompt user to enter their DNA Sequence upon opening program 

dnaSeq = input ("Enter your DNA Sequence:")

#For calculating the total sequence length.

print ("Total Sequence Length:")
print (len(dnaSeq))

#Each of the following should count the individual bases in the sequence 

print ("Number of As:")
print (dnaSeq.count('A'))

print ("Number of Ts:")
print (dnaSeq.count('T'))

print ("Number of Gs:")
print (dnaSeq.count('G'))

print ("Number of Cs:")
print (dnaSeq.count('C'))

