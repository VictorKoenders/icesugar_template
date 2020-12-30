#!/bin/bash
set -ex

mkdir -p tools
cd tools

if [ ! -d "icestorm" ] 
then
    git clone https://github.com/YosysHQ/icestorm.git icestorm
    cd icestorm
    make -j$(nproc)
    sudo make install
    cd ..
fi


if [ ! -d "nextpnr" ] 
then
    git clone https://github.com/YosysHQ/nextpnr nextpnr
    cd nextpnr
    cmake -DARCH=ice40 -DCMAKE_INSTALL_PREFIX=/usr/local .
    make -j$(nproc)
    sudo make install
    cd ..
fi


if [ ! -d "yosys" ] 
then
    git clone https://github.com/YosysHQ/yosys.git yosys
    cd yosys
    make -j$(nproc)
    sudo make install
    cd ..
fi


if [ ! -d "nmigen" ] 
then
    git clone https://github.com/nmigen/nmigen
    cd nmigen
    pip3 install --editable .[builtin-yosys]
    cd ..
fi


if [ ! -d "nmigen-boards" ] 
then
    git clone https://github.com/nmigen/nmigen-boards
    cd nmigen-boards
    cp ../../setup/icesugar.py nmigen_boards/
    pip3 install --editable .[builtin-yosys]
    cd ..
fi

echo "Done installing. You can delete the \`tools\` directory safely."
