#! /bin/bash

input_number_check(){
    if [[ $1 =~ ^[0-9]+$ ]]
    then
        return 1

    else

        return 0

    fi

}

printf "Let's get it: "
read -r startInput

printf "\nThat's about it: "
read -r endInput

if input_number_check $startInput;
then
    echo "That's Not It"
    exit 1
fi

for ((i=$startInput;i<=$endInput;i++))
do
    echo "Hey, scan this one 192.168.1.$i..."
    nmap "192.168.1.$i" >> Nmap_is_dope_output
done


