%define name      omega-backup
%define version   1.0
%define release   1

Summary:          Backup tool for MySQL.
Name:             %{name}
Version:          %{version}
Release:          %{release}
URL:              http://www.itchyninja.com
License:          GPL-2.0
Group:            Productivity/Databases/Tools
BuildRoot:        %{_tmppath}/%{name}-root
Requires:         mysql
Requires:         bash
Requires:         qpress
Source0:          %{name}-%{version}.tar.gz
BuildArch:        noarch
Provides:         %{name} = %{version}
Obsoletes:        %{name} < %{version}

%description
A bash script that makes MySQL backups using Percona XTRABackup.

%prep
%setup

%build

%pre
echo "Scheduling backup via /etc/cron.d/%{name}"

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/usr/bin
mkdir -p ${RPM_BUILD_ROOT}/etc/cron.d
install -m 755 %{name} ${RPM_BUILD_ROOT}%{_bindir}
install -m 644 %{name}.cron ${RPM_BUILD_ROOT}/etc/cron.d/%{name}
install -m 644 %{name}.conf ${RPM_BUILD_ROOT}/etc/%{name}.conf

%post
echo "Crontab setup completed for %{name}."
echo "You may modify the backup schedule in the /etc/cron.d/%{name} file." 

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/%{name}
%attr(644,root,root) /etc/cron.d/%{name}
%attr(644,root,root) /etc/%{name}.conf

%changelog
* Mon Aug 17 2015 Mike Patrick <mike@itchyninja.com>
- Initial script!
