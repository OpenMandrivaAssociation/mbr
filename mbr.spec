%define name mbr
%define version 1.1.5
%define release %mkrel 2

Summary: Master Boot Record for IBM-PC compatible computers
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}_%{version}.orig.tar.bz2
License: GPL
Group: System/Kernel and hardware
Url: http://packages.debian.org/unstable/admin/mbr
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Exclusivearch: %ix86

%description
This is used in booting Linux from the hard disk. The MBR runs first,
then transfers control to LILO, which transfers control to the Linux
kernel.

%prep
%setup -q -n %{name}-%{version}.orig

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sbindir}/install-mbr
%{_mandir}/*/install-mbr.8*
