import sys, os

global pFile

def setPear(pear):
	global pFile
	pFile = pear
	

def execute(cmd):
	args = cmd.split()
	a = args[0]
	if a=="exit":
		sys.exit(0)
	elif a=="peek":
		peek()
	elif a=="mem":
		if not len(args)==2:
			sys.stdout.write("Invalid syntax. Proper usage: mem [value]\n")
			sys.stdout.flush()
		else:
			mem(args)
	elif a=="memclr":
		memclr()
	else:
		sys.stdout.write("Command not found: " + args[0] + "\n")
		sys.stdout.flush()

def peek():
	tmp = open(pFile, "r")
	for line in tmp.readlines():
		sys.stdout.write(line)
		sys.stdout.flush()
	tmp.close()

def mem(args):
	tmp = open(pFile, "a+")
	os.system("cat " + pFile + " | grep -i \'mem\' > tmp.p")
	tmp2 = open("tmp.p", "r+")
	length = len(tmp2.readlines())
	tmp2.close()
	os.system("rm -f tmp.p")
	try:
		test = int(args[1])
		tmp.write("mem|0x" + str(length) + "->" + args[1] + "\n")
		tmp.close()
	except Exception as e:
		sys.stdout.write(str(e))
		sys.stdout.write("Invalid syntax. Value needs to be numeric.\n")
		sys.stdout.flush()

def memclr():
	tmp = open(pFile, "w")
	
