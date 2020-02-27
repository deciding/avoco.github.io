apt-get install -y software-properties-common
add-apt-repository ppa:ubuntu-toolchain-r/test
apt update
apt install g++-7 -y

#update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 60 \
#                        --slave /usr/bin/g++ g++ /usr/bin/g++-7 
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 60
update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-7 60
update-alternatives --config gcc
update-alternatives --config g++
gcc --version
g++ --version

## This one if you want the **all** toolchain programs (with the triplet names) to also point to gcc-7. 
## For example, this is needed if building Debian packages.
## If you are already are root (e.g. inside a docker image), remove the "sudo" below.
#ls -la /usr/bin/ | grep -oP "[\S]*(gcc|g\+\+)(-[a-z]+)*[\s]" | xargs sudo bash -c 'for link in ${@:1}; do ln -s -f "/usr/bin/${link}-${0}" "/usr/bin/${link}"; done' 7
