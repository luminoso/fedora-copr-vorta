%global srcname vorta

Name:           %{srcname}
Version:        0.7.1
Release:        1%{?dist}
Summary:        A GUI for Borg Backup
License:        GPLv3
URL:            https://vorta.borgbase.com/
#Source0:       %{pypi_source}
Source0:        https://github.com/borgbase/vorta/archive/v%{version}.tar.gz

Summary:        A GUI for Borg Backup
Requires:       python3-appdirs
Requires:       python3-paramiko
Requires:       python3-peewee
Requires:       python3-dateutil
Requires:       python3-qt5
Requires:       python3-APScheduler
Requires:       python3-psutil
Requires:       python3-secretstorage
Requires:       borgbackup
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
#%if 0%{?fedora} || 0%{?rhel} > 7
#Recommends:     python3-pandas-datareader
#Recommends:     python3-xlrd
#Recommends:     python3-xlwt
#%endif

%description
Vorta is a backup client for macOS and Linux desktops. 
It integrates the mighty BorgBackup with your desktop environment 
to protect your data from disk failure, ransomware and theft

%global debug_package %{nil}

%prep
%autosetup -n %{srcname}-%{version}
# Cython is too old in RHEL8.0
%{!?el8:rm -f $(grep -rl '/\* Generated by Cython')}

%build
%py3_build

%install
%py3_install

install -D %{_builddir}/%{srcname}-%{version}/package/icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/com.borgbase.Vorta.svg
install -D %{_builddir}/%{srcname}-%{version}/package/icon-symbolic.svg %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/com.borgbase.Vorta-symbolic.svg
install -D %{_builddir}/%{srcname}-%{version}/src/vorta/assets/metadata/com.borgbase.Vorta.desktop %{buildroot}%{_datadir}/applications/com.borgbase.Vorta.desktop


%files
#%doc RELEASE.md
#%license LICENSE
%{python3_sitelib}/*
%{_bindir}/vorta
%{_datadir}/*

%changelog
* Sat Jan 2 2021 Guilherme Cardoso <gjc@ua.pt> 0.7.1-1
- Initial release




