#!/bin/sh

# Steps from: http://meinit.nl/making-rpm-shell-script

VERSION="1.0"
RELEASE="1"
NAME="omega-backup"
TARFILE="$NAME-$VERSION.tar.gz"
SPEC="$NAME.spec"

# Generate RPM name (don't edit)
RPM="/root/rpmbuild/RPMS/noarch/$NAME-$VERSION-$RELEASE.noarch.rpm"

tar -cvzf $TARFILE $NAME-$VERSION
mv $TARFILE /root/rpmbuild/SOURCES/ -f
cp $SPEC /root/rpmbuild/SPECS/ -f
rpmbuild --bb -bl -bs /root/rpmbuild/SPECS/$SPEC
rpm -Uvh $RPM

echo "The RPM is available at:"
echo $RPM
