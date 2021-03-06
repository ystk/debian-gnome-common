Name: gnome-common
Summary: gnome-common contains useful things common to building gnome packages
Version: 2.28.0
Release: 0
License: GPL
Group: Development/Tools
Source: %{name}-%{version}.tar.gz
URL: http://developer.gnome.org/
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Contains files required to bootstrap various Gnome modules when building
from CVS.

%changelog
* Thu May 13 2004 James Henstridge <james@daa.com.au>
- update and simplify
* Mon Mar 26 2000 Robin * Slomkowski <rslomkow@rslomkow.org>
- created this thing, and replaced the generic specfile

%prep
%setup

%build

%configure
make

%install

%makeinstall

%files

%defattr(-, root, root)
%{_bindir}/*
%{_datadir}/aclocal/*
%{_datadir}/gnome-common
