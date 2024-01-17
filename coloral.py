import os
import time
def red(msg):
	print(f"\033[1;49;91m {msg}\033[m")
def green(msg):
	print(f"\033[1;49;92m {msg}\033[m")
def ylw(msg):
	print(f"\033[1;49;93m {msg}\033[m")
def dblue(msg):
	print(f"\033[1;49;94m {msg}\033[m")
def rose(msg):
	print(f"\033[1;49;95m {msg}\033[m")
def blue(msg):
	print(f"\033[1;49;96m {msg}\033[m")
def rosep(msg):
	print(f"\033[7;49;95m {msg}\033[m")
def warn():
	print(f"\033[7;49;91m [ ! ] \033[m \033[1;49;93m Warning! \033[m")
def blred(msg):
	print(f"\033[5;49;91m {msg}\033[m")
def blgre(msg):
	print(f"\033[5;49;92m {msg}\033[m")
def c():
	os.system("clear")
def sec1():
	time.sleep(0.5)
