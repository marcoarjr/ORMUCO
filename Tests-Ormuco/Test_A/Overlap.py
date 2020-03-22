#!/usr/bin/env python

'''
Strategy:
Read one input from user containing 2 values, store in ons string variable
Read another input from user containing 2 other values
Normalize input data
Build 2 lists, representing a line each one
Check if they overlap
Output the result
'''

if __name__ == "__main__":

	line1 = []
	line2 = []
	overlaps = False

	# read user input
	print("Enter first line  (x1,x2): ")
	user1 = str(input())
	print("enter second line (x3,x4): ")
	user2 = str(input())

	# data pre-processing
	user1 = user1.strip("(")
	user1 = user1.strip(")")
	user2 = user2.strip("(")
	user2 = user2.strip(")")
	values1 = user1.split(",")
	values2 = user2.split(",")

	if len(values1) != 2:
		print ("Bad user input for line 1.")
		exit()
	if len(values2) != 2:
		print ("Bad user input for line 2.")
		exit()

	for element in values1:
		line1.append(int(element.strip(" ")))
	for element in values2:
		line2.append(int(element.strip(" ")))

	if line1[0] > line1[1]:
		temp = line1[0]
		line1[0] = line1[1]
		line1[1] = temp
	if line2[0] > line2[1]:
		temp = line2[0]
		line2[0] = line2[1]
		line2[1] = temp

	# build the lines
	range1 = range(line1[0], line1[1]+1, 1)
	range2 = range(line2[0], line2[1]+1, 1)

	# overlapping detection
	for element in range1:
		if element in range2:
			overlaps = True

	# result output
	if overlaps:
		print("Overlap detected.")
	else:
		print ("No overlap detected.")
