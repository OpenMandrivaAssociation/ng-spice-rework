%define name 	ng-spice-rework
%define shortname 	ngspice
%define version 21
%define release %mkrel 1

Summary: Ngspice is a mixed-level/mixed-signal circuit simulator
Name: 	 %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch1:	 %{name}-19-build.patch.bz2
License: BSD
Group: 	 Sciences/Other
Url: 	 https://ngspice.sourceforge.net/download.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	xaw-devel
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel
BuildRequires:  gcc-gfortran
BuildRequires:  flex
BuildRequires:  bison

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

%package -n %{name}-examples
Summary:	Examples files for NGSpice
Group:		Sciences/Other
License:	BSD

%description -n %{name}-examples
Examples files for NGSpice

%prep
%setup -q -n %{shortname}-%{version}
%patch1

%build
autoreconf -fi
%configure \
	--with-readline \
	--enable-maintainer-mode \
	--enable-capzerobypass \
	--enable-intnoise \
	--enable-xspice \
	--enable-cider \
	--disable-xgraph \
	--enable-debug \
	--enable-numparam=yes \
	--enable-dot-global \
	--enable-experimental
	
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# Install examples
%__install -d -m755 examples %{buildroot}/%{_datadir}/%{name}

%__mv %{buildroot}/%{_datadir}/%{shortname} %{buildroot}/%{_datadir}/%{name}

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
%{_bindir}/cmpp
%{_libdir}/spice/
%{_datadir}/%{name}
%{_mandir}/man1/ngspice.1.lzma
%{_mandir}/man1/ngsconvert.1.lzma
%{_mandir}/man1/ngmultidec.1.lzma
%{_mandir}/man1/ngnutmeg.1.lzma
%doc AUTHORS BUGS ChangeLog COPYING FAQ INSTALL README

%files -n %{name}-examples
%defattr(-,root,root,0755)
%doc examples

