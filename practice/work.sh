#!/bin/bash
bash /opt/huawei/Bigdata/om-agent/nodeagent/setup/uninstall.sh
bash /opt/huawei/Bigdata/om-server/om/inst/uninstall.sh
rm -rf /srv/BigData/
rm -rf /opt/huawei/Bigdata/
rm -rf /var/log/Bigdata/
userdel omm
userdel ommdba
rm -rf /home/omm
rm -rf /home/oms
rm -rf /home/ommdba
rm -rf /opt/SwiftInstall/SwiftDeploy/
cd /opt/SwiftInstall/
unzip SwiftDeploy-2.2.13_SLES_x86_64.zip
cd /opt/SwiftInstall/SwiftDeploy/bin
bash start.sh stop
bash start.sh start -ip 0.0.0.0
bash start.sh stop
cd /opt/SwiftInstall
cp /opt/SwiftInstall/FI_zip/* /opt/SwiftInstall/SwiftDeploy/package/
chown swiftuser:swiftgroup /opt/SwiftInstall/SwiftDeploy/package/*
cp /opt/SwiftInstall/FI_SPC206/* /opt/SwiftInstall/SwiftDeploy/FIPatch/
chown swiftuser:swiftgroup  /opt/SwiftInstall/SwiftDeploy/FIPatch/*
cp /opt/SwiftInstall/SwiftDeploy/etc/templates/FI/*.json /opt/SwiftInstall/SwiftDeploy/etc/datamodel/
chown swiftuser:swiftgroup /opt/SwiftInstall/SwiftDeploy/etc/datamodel/*
cd /opt/SwiftInstall/SwiftDeploy/etc/datamodel/
vi FI_u2000.json
python /opt/SwiftInstall/SwiftDeploy/bin/encrypt_root_key.pyc
vi /opt/SwiftInstall/SwiftDeploy/silentdeploy/deployparameter.json
bash /opt/SwiftInstall/SwiftDeploy/bin/silentdeploy.sh admin *******
