# xroad6 vagrant conf

see Vagrantfile ;)

run
 
```
vargant up

vargrant ssh saltmaster
```

## TODO

set up center and securityserver 

### Notes
```
curl -s -q http://x-road.eu/.test/xroad/xroad_repo.gpg| sudo apt-key add -
echo "deb file:/srv/xroad/debs trusty main" > /etc/apt/sources.list.d/xroad.list
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 00A6F0A3C300EE8C
echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu trusty main" >> /etc/apt/sources.list.d/xroad.list
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EB9B1D8886F44E2A
echo "deb http://ppa.launchpad.net/openjdk-r/ppa/ubuntu trusty main " >> /etc/apt/sources.list.d/xroad.list 
apt-get update
echo "xroad-proxy xroad-common/username string vagrant" | debconf-set-selections
echo "xroad-proxy xroad-common/admin-subject string /CN=xroad-02" | debconf-set-selections
echo "xroad-proxy xroad-common/admin-altsubject string IP:10.1.10.5,DNS:xroad-02" | debconf-set-selections
echo "xroad-proxy xroad-common/service-subject string /CN=xroad-02" | debconf-set-selections 
echo "xroad-proxy xroad-common/service-altsubject string IP:10.1.10.5,DNS:xroad-02" | debconf-set-selections
export DEBIAN_FRONTEND=noninteractive
apt-get -y install xroad-securityserver
```
