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

class pearOS:
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
            if parts[0] == "mmry":
                ptr = parts[1].split("->")
                self.memory[ptr[0]] = ptr[1]
            elif parts[0] == "user":
                unpw = parts[1].split("::")
                self.users[unpw[0]] = unpw[1]
            elif parts[0] == "file":
                info = parts[1].split(">>")
                files[info[0]] = info[1]
        self.signin()
        os.system("clear")
        self.awaitCommand()

    def signin(self):
        signedIn = False
        sys.stdout.write("Username: ")
        sys.stdout.flush()
        un = raw_input()
        if un in self.users.keys():
            a
        sys.stdout.write("Password: ")
        sys.stdout.flush()
        pw = raw_input()
        for u, p in self.users.items():
            sys.stdout.write(un + " " + u + " " + pw + " " + p)
            sys.stdout.flush()
            if self.users[un] == p and self.users[u] == pw:
                self.currUser = un
                signedIn = True
                break
        if not signedIn:
            sys.stdout.write("Sign-in failed. Please try again.\n\n")
            sys.stdout.flush()
            self.signin()

    def loadImage(self):
        sys.stdout.write("Image file: ")
        sys.stdout.flush()
        newImg = raw_input()
        try:
            self.image = open(newImg, "r+")
            self.name = newImg
        except Exception as e:
            self.imgNotFound(newImg)

    def imgNotFound(self, imgFile):
        sys.stdout.write("Image not found: " + imgFile + ". Would you like to (1) perform first time setup or (2) select a different image?")
        sys.stdout.flush()
        choice = raw_input()
        if choice=="1":
            self.initSetup()
            self.loadImage()
        elif choice=="2":
            self.loadImage()
        else:
            while not choice=="1" and not choice=="2":
                sys.stdout.write("Please select 1 or 2. ")
                sys.stdout.flush()
                choice = raw_input()
                if choice=="1":
                    self.initSetup()
                elif choice=="2":
                    self.loadImage()


    def initSetup(self):
        sys.stdout.write("Welcome to PearOS v" + self.osVer + "! Please enter the name of the file you would like to store the image in (excluding .img): ")
        sys.stdout.flush()
        img = raw_input()
        tempImg = open(img + ".img", "w")
        sys.stdout.write("Enter your preferred username: ")
        sys.stdout.flush()
        un = raw_input()
        sys.stdout.write("Enter your preferred password: ")
        sys.stdout.flush()
        pw = raw_input()
        tempImg.write("user|" + un + "::" + pw + "\n")
        sys.stdout.write("User account created and stored.\n")
        sys.stdout.flush()

    def start(self):
        sys.stdout.write("Would you like to (1) create or (2) load an image?")
        sys.stdout.flush()
        choice = raw_input()
        if choice=="1":
            self.initSetup()
            self.loadImage()
        elif choice=="2":
            self.loadImage()
        else:
            while not choice=="1" and not choice=="2":
                sys.stdout.write("Please select 1 or 2.")
                sys.stdout.flush()
                choice = raw_input()
                if choice=="1":
                    self.initSetup()
                    self.loadImage()
                elif choice=="2":
                    self.loadImage()


    def awaitCommand(self):
        sys.stdout.write(bcolors.OKBLUE + self.currUser + bcolors.ENDC + "@" + bcolors.BOLD + self.name + bcolors.ENDC + bcolors.OKGREEN+ " (PearOS_v" + self.osVer + ") " + bcolors.ENDC + "> ")
        sys.stdout.flush()
        cmd = raw_input()
        self.execute(cmd)
        self.awaitCommand()

    def execute(self, cmd):
        sys.stdout.write("Executing command: " + cmd + "\n")
        if cmd=="exit":
            sys.exit(0)
        sys.stdout.flush()

os = pearOS()
