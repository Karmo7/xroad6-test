#!/bin/bash
IP=$(ifconfig eth1 2>/dev/null|grep 'inet addr'|cut -f2 -d':'|cut -f1 -d' ')
NAME=$(hostname -f)
USER='vagrant'
echo $IP $NAME $USER
echo "xroad-proxy xroad-common/username string $USER" | debconf-set-selections
echo "xroad-proxy xroad-common/admin-subject string /CN=$NAME" | debconf-set-selections
echo "xroad-proxy xroad-common/admin-altsubject string IP:$IP,DNS:$NAME" | debconf-set-selections
echo "xroad-proxy xroad-common/service-subject string /CN=$NAME" | debconf-set-selections
echo "xroad-proxy xroad-common/service-altsubject string IP:$IP,DNS:$NAME" | debconf-set-selections
debconf-get-selections | grep xroad
DEBIAN_FRONTEND=noninteractive apt-get -q -y install xroad-securityserver
