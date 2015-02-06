%define name mbr
%define version 1.1.10
%define release 6

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


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.10-5mdv2011.0
+ Revision: 620306
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.1.10-4mdv2010.0
+ Revision: 430001
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.1.10-3mdv2009.0
+ Revision: 252132
- rebuild

* Sat Mar 01 2008 Olivier Blin <oblin@mandriva.com> 1.1.10-1mdv2008.1
+ Revision: 177422
- remove Werror build hack
- 1.1.10 (and use Debian patch as well)

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag
    - kill re-definition of %%buildroot on Pixel's request

* Mon Apr 23 2007 Olivier Blin <oblin@mandriva.com> 1.1.9-1mdv2008.0
+ Revision: 17242
- buildrequire dev86
- build without Werror (the debian way not to fix strict aliasing errors)
- 1.1.9
- Import mbr



* Thu Jan 12 2006 Olivier Blin <oblin@mandriva.com> 1.1.5-2mdk
- add Exclusivearch %%ix86, vm86.h is not supported on X86-64
  (thanks Iurt, I owe you a beer)

* Tue Dec 27 2005 Olivier Blin <oblin@mandriva.com> 1.1.5-1mdk
- initial release
