Summary:	Game update/launch program for INSTEAD
Name:		instead-launcher
Version:	0.6.1
Release:	1%{?dist}.R

URL:		http://instead-launcher.googlecode.com
License:	GPLv2
Group:		Amusements/Games
Source0:	http://instead-launcher.googlecode.com/files/%{name}_%{version}.tar.gz
Patch0:		instead-launcher-0.6.1-desktop.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	qt-devel
BuildRequires:	zlib-devel

Requires:	instead

%description 
Instead-launcher provides GUI for simple installing, updating and launching of
INSTEAD games

%prep
%setup -q
%patch0 -p1 -b .desktop

%build
qmake-qt4 PREFIX=/usr
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/bin/ $RPM_BUILD_ROOT/usr/share/applications/
install -m 755 instead-launcher $RPM_BUILD_ROOT/usr/bin/
install -m 644 -p instead-launcher.desktop $RPM_BUILD_ROOT/usr/share/applications/
strip $RPM_BUILD_ROOT/usr/bin/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc readme.txt
%{_bindir}/*
%{_datadir}/applications/*

%changelog
* Sat Nov  5 2011 Arkady L. Shane <ashejn@russianfedora.ru> - 0.6.1-1.R
- initial build for Fedora
