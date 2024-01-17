red="\033[5;49;91m"
green="\033[7;49;95m"
redy="\033[7;49;91m"
ylw="\033[1;49;93m"
blue="\033[1;49;96m"
echo "${red}NÃO ME RESPONSABILIZO PELO SEU MAU USO!!\033[m"
echo "${green}USE CONTROL + C PARA PARAR A OPERACÃO!\033[m"
sleep 10
gren="\033[1;49;32m"
echo $gren $(ifconfig)
sleep 1
echo $gren $(ifconfig)
sleep 1
echo $gren $(ps)
sleep 1
echo $gren $(ps && ls -i)
sleep 0.5
echo $gren $(ls -a)
echo $gren $(ifconfig)
echo $gren $(ps)
sleep 1
echo $gren $(ps && ls -i)
sleep 0.5
echo $gren $(ls -a)
sleep 1
echo $gren $(ifconfig)
echo $gren $(ps)
sleep 1
echo $gren $(ps && ls -i)
sleep 0.5
echo $gren $(ls -a)
echo $gren $(ifconfig)
sleep 1
echo $gren $(ps)
sleep 1
echo $gren $(ps && ls -i)
sleep 0.5
echo $gren $(ls -a)
for z in $(seq 0 1 150)
	do
	echo "$gren TRYING DO BREAK-FORCE ON WiFi attempts:$z --LockedWithWirelles |Security : WPPA/WSK Wirelless |"
	echo "$redy [ ! ] \033[m $ylw using  > \033[m $blue localhost \033[m $ylw < \033[m"
	sleep 0.2
	echo "$red Loading \033[m"
	sleep 0.2
	echo "$red Loading YOUR \033[m"
	sleep 0.2
	echo "$red Loading YOUR request....\033[m"
	sleep 0.1
	echo "\033[3;49;94m request n° $z\033[m"
	done
echo $red "Ip-Request: 192.168.***.**"
echo $red "response: Fail"
sleep 1
echo $green "403 Forbbiden Error!, Total Requests: 150\033[m"

read -p "" yn
python3 password.py

