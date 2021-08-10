#! /bin/bash
usage()
{
    echo "Usage: $0 [-h -dc -ip -kc]"
    echo
    echo "Used for check the system"
    echo
    echo "       -h  | --help         output this help information    "
    echo "       -dc | --diskcheck    check the kolla disk information"
    echo "       -ip | --ip           the ip address that need check  "
    echo "       -kc | --kernelcheck  check the kernel                "
    echo
}

diskcheck() {

#    blkid>systemcheck.log
    FILE=systemcheck.log
    MATCH=KOLLA_CEPH_DATA_BS_
    flag=0
    flagWB=0
    flagWOB=0
    countWB=0
    countWOB=0
    messWB=
    messWOB=

    while read line
    do
        result=`echo $line | grep PARTLABEL=\"$MATCH.*`
        if [[ "$result" != "" ]]
        then
            match=`echo $result | grep PARTLABEL=\"$MATCH._B`
            if [[ "$match" != "" ]]
            then
                ((countWB++))
                if [[ $result == *" UUID"* ]];
                then
                    flag=1;
                    flagWB=1;
                    messWB=$result;
                fi
            else
                ((countWOB++))
                if [[ $result != *" UUID"* ]];
                then
                    flag=2
                    flagWOB=1;
                    messWOB=$result;
                fi
            fi
        fi
    done < $FILE

    arrWB=($messWB)
    arrWOB=($messWOB)
    echo -n 'Check Kolla disk: '
    if [[ $flag == "0" ]];
    then
        echo 'OK';
    else
    if [[ $flagWB == "1" ]];
    then
        echo -n 'ERROR, It is can not mount  The error position is: ';
        echo "$arrWB";
    fi
    if [[ $flagWOB == "1" ]];
    then
        echo -n 'ERROR, It is not mounted  The error position is: ';
        echo "$arrWOB";
    fi
    fi

    sum=$(($countWB+$countWOB))
    echo -n 'Check Kolla disk numbers: '
    if [[ $sum == 4 ]] && [[ $countWB == 2 ]] && [[ $countWOB == 2 ]];
    then
        echo 'OK';
    else
        echo -n 'ERROR, The number of PARTLABEL with B is: '
        echo -n "$countWB"
        echo -n ' '
        echo -n 'The number of PARTLABEL with out B is: '
        echo "$countWOB";
    fi
}

kernelcheck(){
    kc=`uname -r`
    echo -n 'Check Kernel: '
    if [[ $kc == "3.10.0-1160.36.2.e17.x86_64" ]];
    then 
        echo 'OK';
    else
        echo -n 'ERROR, The target kernel is 3.10.0-1160.36.2.e17.x86_64, but the result is: '
        echo $kc;
    fi
}

opt=$1
case $opt in
    -h | --help)
        usage
        exit 0
        ;;
    -ip | --ip)
        ssh -f -n root@$2 "blkid" > systemcheck.log
        echo 'The Check result: '
        diskcheck
        kernelcheck
        exit 0
        ;;
    -dc | --diskcheck)
        blkid>systemcheck.log
        echo 'The Check result: '
        diskcheck   
        exit 0
        ;;
    -kc | --kernelcheck)
        echo 'The Check result: '
        kernelcheck
        exit 0
        ;;
    *)
        exit 1
        ;;
esac
