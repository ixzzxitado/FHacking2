from coloral import *
while True:
	blred("NÃO ME RESPONSABILIZO PELO SEU MAU USO!")
	rosep("USE CONTROL + C PARA ENCERRAR A OPERACÃO")
	time.sleep(4)
	c()
	red(
	"    ▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ █             \n"
	"▀▀▀▀▄ █ █ █ █ █ █  █▀█ netIn v2.7.0\n"
	"     ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ▀             \n"
	)
	sec1()
	host = ["127.0.0.1", "localhost"]
	port = ["8080", "443", "4443", "8.8.8.8"]
	print(
	"[ 1 ] WEP/WAP Force Break\n"
	" \n"
	"[ 2 ] WPA2-AES Force Break \n"
	" \n"
	"[ 3 ] Quit\n"
	" \n"
	)
	resp = int(input(">>>>>>  "))
	if(resp == 1):
		respk = input("Host: ")
		input("Port: ")
		if(respk not in host):
				warn()
				blred("Unknow Port/Host")
				sec1()
				print("\033[3;49;95m using default credentials...\033[m")
				sec1()
				sec1()
				print(f"\033[2;49;93m Port: \033[m \033[2;49;96m {port} \033[m")
				print("")
				sec1()
				print(f"\033[2;49;93m Host: \033[m \033[2;49;96m localhost \033[m")
				os.system("python3 inj.py")
				input("")
				continue
		else:
			blred("Loading Attack...")
			sec1()
			os.system("python3 inj.py")
			input("")
			continue
			
	if(resp == 2):
		respo = input("Host: ")
		input("Port: ")
		if(respo not in host):
				warn()
				blred("Unknow Port/Host")
				sec1()
				print("\033[3;49;95m using default credentials...\033[m")
				sec1()
				sec1()
				print(f"\033[2;49;93m Port: \033[m \033[2;49;96m {port} \033[m")
				print("")
				sec1()
				print(f"\033[2;49;93m Host: \033[m \033[2;49;96m localhost \033[m")
				os.system("python3 inj2.py")
				input("")
				continue
		else:
			blred("Loading Attack...")
			os.system("python3 inj2.py")
			input("")
			continue
	if(resp == 3):
		break
	else:
		red("Unknow Request")
		sec1()
		continue
