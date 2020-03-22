#!/usr/bin/env python

'''
Strategy:
Buid a class taht may accept 2 type of inputs
Instance an object of this class and use the compare method in both given types
Run test cases
'''

class Detection:
	def verifying(self, a, b):
		# version 1, receiving two strings
		if isinstance(a, str) and isinstance(b, str):
			if a > b:
				return "GT"
			if a < b:
				return "LT"
			if a == b:
				return "EQ"

		else:
			# version 2, receiving two floats
			if isinstance(a, float) and isinstance(b, float):
				if a > b:
					return "GT"
				if a < b:
					return "LT"
				if a == b:
					return "EQ"
			else:

				return "Bad params. Use 2 strings(e.g. \"1\") or 2 floats (e.g. 1.33)"

if __name__ == "__main__":
	detection = Detection()
	# test cases
	print (detection.verifying("", ""))                 # two empty strings -> pass
	print (detection.verifying("pass", "passcode"))     # two word strings -> pass
	print (detection.verifying("a", "b"))               # two alpha strings -> pass
	print (detection.verifying("2", "1"))               # two numeric strings -> pass
	print (detection.verifying("C", "C"))               # two equal strings -> pass
	print (detection.verifying(1.1, 1.3))               # two floats -> pass
	print (detection.verifying(2.1, 1.3))               # two floats -> pass
	print (detection.verifying(1.0, 1.0))               # two floats -> pass
	print (detection.verifying(1, 1.3))                 # one int and one float -> error message
	print (detection.verifying("A", 1.3))               # one string and one float -> error message
	print (detection.verifying("A", 1))                 # one string and one int -> error message
	print (detection.verifying(1.3, 1))                 # one float and one int -> error message
	print (detection.verifying(1.3, "A"))               # one float and one string -> error message
	print (detection.verifying(1, "A"))                 # one int and one string -> error message

'''
--OUTPUT:
EQ
LT
LT
GT
EQ
LT
GT
EQ
Bad params. Use 2 strings(e.g. "1") or 2 floats (e.g. 1.33)
Bad params. Use 2 strings(e.g. "1") or 2 floats (e.g. 1.33)
Bad params. Use 2 strings(e.g. "1") or 2 floats (e.g. 1.33)
Bad params. Use 2 strings(e.g. "1") or 2 floats (e.g. 1.33)
Bad params. Use 2 strings(e.g. "1") or 2 floats (e.g. 1.33)
Bad params. Use 2 strings(e.g. "1") or 2 floats (e.g. 1.33)
'''