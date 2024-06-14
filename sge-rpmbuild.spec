# rpmbuild sge package

%define sge_home /opt/sge
%define username sge

%global debug_package %{nil}

Name:    sge
Version: 8.1.10

Release: 1%{?dist}
Summary: SGE

Group:   Applications/System
License: (SISSL and BSD and LGPLv3+ and MIT) and GPLv3+ and GFDL and others
URL:     https://github.com/wajchina/sge
Source0:  sge.tar.gz

Prefix: %{sge_home}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gcc-c++ cmake hwloc-devel libdb-devel libtirpc-devel motif-devel ncurses-devel openssl-devel pam-devel rsync systemd-devel wget rpmdevtools tcsh jemalloc-devel autoconf automake  ant-junit javacc munge-devel rpm-build

%description
Some Grid Engine/Son of Grid Engine/Sun Grid Engine

%prep

%setup -q -n sge

%build
cmake -S . -B build -DCMAKE_INSTALL_PREFIX=$RPM_BUILD_ROOT%{sge_home}
cmake --build build -j

%install 
cmake --install build

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%{_sbindir}/useradd -d / -s /sbin/nologin \
   -M -r -c 'Grid Engine admin' %username 2>/dev/null || :

%post

%files
%{sge_home}

%changelog
