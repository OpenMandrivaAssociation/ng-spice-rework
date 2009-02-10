%define name 	ng-spice-rework
%define version 18
%define release %mkrel 1

Summary: Ngspice is a mixed-level/mixed-signal circuit simulator
Name: 	 %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: BSD
Group: 	 Sciences/Other
Url: 	 http://ngspice.sourceforge.net/download.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	libxaw-devel

%description
Ngspice is a mixed-level/mixed-signal circuit simulator. Its code is
based on three open source software packages: Spice3f5, Cider1b1 and
Xspice. Ngspice is part of gEDA project, a full GPL'd suite of
Electronic Design Automation tools.

Spice3 does not need any introduction, is the most popular circuit
simulator. In over 30 years of its life Spice3 has become a de-facto
standard for simulating circuits.

Cider couples Spice3f5 circuit level simulator to DSIM device
simulator to provide greater simulation accuracy of critical
devices. DSIM devices are described in terms of their structures and
materials.

Xspice is an extension to Spice3C1 that provides code modeling support
and simulation of digital components through an embedded event driven
algorithm.

Ngspice is, anyway, a little more than the simple sum of the packages
above, as many people contributed to the project with their
experience, their bug fixes and their improvements. If you are
interested, browse the site and discover what ngspice offers and what
needs. If you think you can help, join the development team.

Ngspice is an ongoing project, growing everyday from users
contributions, suggestions and reports. What we will be able to do
depends mostly on user interests, contributions and feedback.

%prep
%setup -q 

%build
autoreconf -fi
%configure
%make
iconv -t utf-8 doc/ngspice.info -o doc/ngspice.info

%install
rm -rf %{buildroot}
%makeinstall_std


%post
%_install_info ngspice.info.lmza
%_install_info ngspice.info-1.lmza
%_install_info ngspice.info-2.lmza

%preun
%_remove_install_info ngspice.info.lmza
%_remove_install_info ngspice.info-1.lmza
%_remove_install_info ngspice.info-2.lmza

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/ngmakeidx
%{_bindir}/ngmultidec
%{_bindir}/ngnutmeg
%{_bindir}/ngproc2mod
%{_bindir}/ngsconvert
%{_bindir}/ngspice
%{_datadir}/%{name}
%{_mandir}/man1/ngspice.1.lzma
%{_mandir}/man1/ngsconvert.1.lzma
%{_mandir}/man1/ngmultidec.1.lzma
%{_mandir}/man1/ngnutmeg.1.lzma
%{_infodir}/ngspice.info*.lzma
