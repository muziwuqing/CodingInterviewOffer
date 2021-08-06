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


opt=$1
case $opt in
    -h | --help)
        usage
        exit 0
        ;;
    -ip)
        ssh -f -n root@$2 "blkid" >> linzhecont.log
        ;;
esac


~                                        