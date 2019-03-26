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
unzip /opt/SwiftInstall/SwiftDeploy/binSwiftDeploy-2.2.13_SLES_x86_64.zip /opt/SwiftInstall/
cd /opt/SwiftInstall/SwiftDeploy/bin
bash /opt/SwiftInstall/SwiftDeploy/bin/start.sh stop
bash /opt/SwiftInstall/SwiftDeploy/bin/start.sh start -ip 0.0.0.0
bash /opt/SwiftInstall/SwiftDeploy/bin/start.sh stop
cp /opt/SwiftInstall/FI_zip/* /opt/SwiftInstall/SwiftDeploy/package/
chown swiftuser:swiftgroup /opt/SwiftInstall/SwiftDeploy/package/*
cp /opt/SwiftInstall/FI_SPC206/* /opt/SwiftInstall/SwiftDeploy/FIPatch/
chown swiftuser:swiftgroup  /opt/SwiftInstall/SwiftDeploy/FIPatch/*
cp /opt/SwiftInstall/SwiftDeploy/etc/templates/FI/*.json /opt/SwiftInstall/SwiftDeploy/etc/datamodel/
chown swiftuser:swiftgroup /opt/SwiftInstall/SwiftDeploy/etc/datamodel/*
vi /opt/SwiftInstall/SwiftDeploy/etc/datamodel/FI_u2000.json
python /opt/SwiftInstall/SwiftDeploy/bin/encrypt_root_key.pyc
vi /opt/SwiftInstall/SwiftDeploy/silentdeploy/deployparameter.json
bash /opt/SwiftInstall/SwiftDeploy/bin/silentdeploy.sh admin *******
