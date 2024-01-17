red="\033[5;49;91m"
green="\033[7;49;95m"
echo "${red}NÃO ME RESPONSABILIZO PELO SEU MAU USO!!\033[m"
echo "${green}USE CONTROL + C PARA PARAR A OPERACÃO!\033[m"
sleep 10
gren="\033[1;49;32m"
echo $gren $(seq 0 1 999)
echo $gren "Capturando logs...."
sleep 1
for z in $(seq 0 1 9999999)
	do
	echo "log$z.vbs.wzk CAPTURADA\n"
	echo ""
	echo "log$z.vbs.wzk movida para C:Sistem/Win32/"
	done

read -p "" yn
python3 password.py
