import funcs

import os
import sys
import os.path
from os import path

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

class pear:
	osVer = "0.0.1a"
	memory = {}
	users = {}
	currUser = None
	files = {}
	image = None
	name = ""

	def __init__(self):
		os.system("clear")
		self.start()
		for line in self.image.readlines():
			parts = line.split('|')
			if parts[0] == "mem":
				ptr = parts[1].split("->")
				self.memory[eval(ptr[0])] = int(ptr[1])
			elif parts[0] == "usr":
				unpw = parts[1].split("::")
				self.users[unpw[0].strip()] = unpw[1].strip()
			elif parts[0] == "fil":
				info = parts[1].split(">>")
				files[info[0]] = info[1]
		self.signin()
		os.system("clear")
		self.awaitCommand()

	def signin(self):
		signedIn = False
		sys.stdout.write(str(self.users) + "\n")
		sys.stdout.flush()
		sys.stdout.write("Username: ")
		sys.stdout.flush()
		un = input()
		if un in self.users.keys():
			sys.stdout.write("Password: ")
			sys.stdout.flush()
			pw = input()
			for u, p in self.users.items():
				sys.stdout.write(un + " " + u + " " + pw + " " + p)
				sys.stdout.flush()
				if un == u and pw == p:
					self.currUser = un
					signedIn = True
					break
		if not signedIn:
			sys.stdout.write("Sign-in failed. Please try again.\n\n")
			sys.stdout.flush()
			self.signin()

	def loadImage(self):
		sys.stdout.write("List of current directory: ")
		sys.stdout.flush()
		os.system("ls")
		sys.stdout.write("Choose a Pear file: ")
		sys.stdout.flush()
		newImg = input()
		try:
			self.image = open(newImg, "r+")
			self.name = newImg
			funcs.setPear(newImg)
		except Exception as e:
			self.imgNotFound(newImg)

	def imgNotFound(self, imgFile):
		sys.stdout.write("Image not found: " + imgFile + ". Would you like to (1) perform first time setup or (2) select a different image?")
		sys.stdout.flush()
		choice = input()
		if choice=="1":
			self.initSetup()
			self.loadImage()
		elif choice=="2":
			self.loadImage()
		else:
			while not choice=="1" and not choice=="2":
				sys.stdout.write("Please select 1 or 2. ")
				sys.stdout.flush()
				choice = input()
				if choice=="1":
					self.initSetup()
				elif choice=="2":
					self.loadImage()


	def initSetup(self):
		sys.stdout.write("Welcome to Pear v" + self.osVer + "! Please enter the name of the file you would like to store the image in (excluding .pear): ")
		sys.stdout.flush()
		img = input()
		tempImg = open(img + ".pear", "w")
		sys.stdout.write("Enter your preferred username: ")
		sys.stdout.flush()
		un = input()
		sys.stdout.write("Enter your preferred password: ")
		sys.stdout.flush()
		pw = input()
		tempImg.write("usr|" + un + "::" + pw + "\n")
		sys.stdout.write("User account created and stored.\n")
		sys.stdout.flush()

	def start(self):
		sys.stdout.write("Would you like to (1) create or (2) load an image? ")
		sys.stdout.flush()
		choice = input()
		if choice=="1":
			self.initSetup()
			self.loadImage()
		elif choice=="2":
			self.loadImage()
		else:
			while not choice=="1" and not choice=="2":
				sys.stdout.write("Please select 1 or 2. ")
				sys.stdout.flush()
				choice = input()
				if choice=="1":
					self.initSetup()
					self.loadImage()
				elif choice=="2":
					self.loadImage()


	def awaitCommand(self):
		sys.stdout.write(bcolors.OKBLUE + self.currUser + bcolors.ENDC + "@" + bcolors.BOLD + self.name + bcolors.ENDC + bcolors.OKGREEN+ "(PearOS_v" + self.osVer + ")" + bcolors.ENDC + "$ ")
		sys.stdout.flush()
		cmd = input()
		funcs.execute(cmd)
		self.awaitCommand()

pear = pear()
