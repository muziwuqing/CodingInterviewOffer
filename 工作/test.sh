#! /bin/bash
usage()
{
    echo "Usage: $0 [-h -dc]"
    echo
    echo "Used for check the system"
    echo
    echo "       -h | --help    output this help information"
    echo "       -dc | --diskcheck    check the kolla disk information"
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

ssh -f -n root@172.16.0.2 "blkid">systemcheck.log
echo systemcheck.log

while read rows

do

echo "Line contents are : $rows "

done < systemcheck.log

diskcheck