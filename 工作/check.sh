#! /bin/bash
usage()
{
    echo "Usage: $0 [-h -dc]"
    echo
    echo "Used for check the system"
    echo
    echo "       -h | --help    output this help information"
    echo "       -dc | --diskcheck    check the kolla disk information"
}

diskcheck() {

    blkid>systemcheck.log
    FILE=systemcheck.log
    MATCH=KOLLA_CEPH_DATA_BS_
    sum=0
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
        if [[ $? == "0" ]];
        then
            echo 
            echo 'All is OK'
            echo
        else
            echo 'There are something wrong'
        exit 0
        ;;
    *)
        exit 1
        ;;
esac
