#!/bin/bash

mkdir -p /usr/share/fuel-distupgrade

PWD=$(dirname $0)
install -m 644 functions /usr/share/fuel-distupgrade
install -m 644 mos8.0-base.whitelist /usr/share/fuel-distupgrade
install -m 755 fuel-distupgrade /usr/sbin

mkdir -p /etc/fuel
for f in *.settings; do
    install -m 644 $f /etc/fuel
done
