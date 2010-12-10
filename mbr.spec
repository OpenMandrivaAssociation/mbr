%define name mbr
%define version 1.1.10
%define release %mkrel 5

Summary: Master Boot Record for IBM-PC compatible computers
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}_%{version}.orig.tar.gz
Patch0: mbr_1.1.10-1.diff.gz
License: GPL
Group: System/Kernel and hardware
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url: http://packages.debian.org/unstable/admin/mbr
BuildRequires: dev86
Exclusivearch: %ix86

%description
This is used in booting Linux from the hard disk. The MBR runs first,
then transfers control to LILO, which transfers control to the Linux
kernel.

%prep
%setup -q
%patch0 -p1

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sbindir}/install-mbr
%{_mandir}/*/install-mbr.8*
