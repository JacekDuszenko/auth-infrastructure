# Script to install openssh
# It is one part of configuration to dockerfile,
# Before run script go to root user

#! /bin/bash
apt update &&
apt install build-essential zlib1g-dev -y &&
cd /usr/local/src/ &&
curl -o openssl-1.0.2o.tar.gz https://www.openssl.org/source/openssl-1.0.2o.tar.gz &&
tar -xf openssl-1.0.2o.tar.gz &&
cd openssl-1.0.2o &&
./config --prefix=/usr/local/ssl --openssldir=/usr/local/ssl shared zlib &&
make &&
make install &&
cd /etc/ld.so.conf.d/ &&
echo "/usr/local/ssl/lib" >> openssl-1.0.2o.conf &&
ldconfig -v &&
mv /usr/bin/c_rehash /usr/bin/c_rehash.BEKUP &&
mv /usr/bin/openssl /usr/bin/openssl.BEKUP &&
echo 'PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/local/ssl/bin"' >> /etc/environment &&
source /etc/environment
