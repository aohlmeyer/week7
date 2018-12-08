#!/usr/bin/env python

#Should prompt user to enter their DNA Sequence upon opening program 

dnaSeq = input ("Enter your DNA Sequence:")

#For calculating the total sequence length.

print ("Total Sequence Length:")
print (len(dnaSeq))

#Each of the following should count the individual bases in the sequence 

print ("Number of As:")
print (dnaSeq.upper().count('A'))

print ("Number of Ts:")
print (dnaSeq.upper().count('T'))

print ("Number of Gs:")
print (dnaSeq.upper().count('G'))

print ("Number of Cs:")
print (dnaSeq.upper().count('C'))

# DB: Good! Although, it doesn't count properly if the sequence is lower case. You can
#     avoid this by adding .upper() to modify your sequence.