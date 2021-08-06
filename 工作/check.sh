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

    blkid>systemcheck.log
    FILE=systemcheck.log
    MATCH=KOLLA_CEPH_DATA_BS_
    flag=0

    while read line
    do
        result=`echo $line | grep PARTLABEL=\"$MATCH.*`
        if [[ "$result" != "" ]]
        then
            match=`echo $result | grep PARTLABEL=\"$MATCH._B`
            if [[ "$match" != "" ]]
            then
                if [[ $result == *" UUID"* ]];
                then
                    flag=1;
                fi
            else
                if [[ $result != *" UUID"* ]];
                then
                    flag=2
                fi
            fi
        fi
    done < $FILE

    return $flag
}

opt=$1
case $opt in
    -h | --help)
        usage
        exit 0
        ;;
    -dc | --diskcheck)
        diskcheck
        fg=$?
        echo
        echo -n 'Check Kolla disk: '
        if [[ $fg == "0" ]];
        then
            echo 'OK';
        elif [[ $fg == "1" ]];
        then 
            echo 'ERROR, It is can not mount';
        elif [[ $fg == "2" ]];
        then
            echo 'ERROR, It is not mounted';
        fi
        exit 0
        ;;
    *)
        exit 1
        ;;
esac
