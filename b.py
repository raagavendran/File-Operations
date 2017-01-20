import sys

f1 = sys.argv[1]
f2 = sys.argv[2]
z=0
z1=0
with open(f1) as fp1,open(f2) as fp2:
	
	for line in fp1:		
		if line.startswith('tempest'):
			z += 1
	print z
	
	for line in fp2:		
		if line.startswith('tempest'):
			z1 += 1
	print z1