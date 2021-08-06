#!/bin/bash
echo '------------test-----------'

blkid>systemcheck.log

FILE=systemcheck.log
MATCH=KOLLA_CEPH_DATA_BS_
sum=0
sumM=0
flag=0


while read line
do
    result=`echo $line | grep PARTLABEL=\"$MATCH.*`
    if [[ "$result" != "" ]]
    then
        ((sum++))
        match=`echo $result | grep PARTLABEL=\"$MATCH._B`
        if [[ "$match" != "" ]]
        then
            if [[ $result == *" UUID"* ]];
            then
                ((sumM++))
                flag=1
                echo 
                echo $result
                echo 'ERROR, It is can not mount';
            fi
        else
            if [[ $result != *" UUID"* ]];
            then
                flag=1
                echo 
                echo $result
                echo 'ERROR, It is not mounted';
            else
                ((sumM++))
            fi
        fi
    fi
done < $FILE

if [[ $flag == "0" ]];
then
    echo 
    echo 'All is OK';
fi



echo 
echo -n 'The total amount of the kolla disk is : '
echo $sum
echo 
echo -n 'The amount of the kolla disk which has been mounted is : '
echo $sumM

echo 
echo '----------end--test--------'
