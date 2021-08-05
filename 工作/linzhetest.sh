echo '------------test-----------'

blkid>linzhetest.log

FILE=linzhetest.log
MATCH=KOLLA_CEPH_DATA_BS_

while read line
do
    result=`echo $line | grep PARTLABEL=\"$MATCH.*`
    if [[ "$result" != "" ]]
    then
        match=`echo $result | grep PARTLABEL=\"$MATCH._B`
        if [[ "$match" != "" ]]
        then
            echo '-------------------------------------------------------'
            if [[ $result == *"UUID"* ]];
            then
                echo 'ERROR, It is can not mount';
            else
                echo 'It is OK';
            fi
            echo $result
            echo '--------------------------------------------------------'
        else
            echo '--------------------------------------------------------'
            if [[ $result == *"UUID"* ]];
            then
                echo 'It is OK';
            else
                echo 'It is not mounted';

            fi
            echo $result
            echo '--------------------------------------------------------'
        fi
    fi
done < $FILE

echo '----------end--test--------'
