Summary:	Game update/launch program for INSTEAD
Name:		instead-launcher
Version:	0.6.1
Release:	2%{?dist}

URL:		http://instead-launcher.googlecode.com
License:	GPLv2
Group:		Amusements/Games
Source0:	http://instead-launcher.googlecode.com/files/%{name}_%{version}.tar.gz

BuildRequires:	qt-devel
BuildRequires:	zlib-devel
BuildRequires:	desktop-file-utils

Requires:	instead

%description 
Instead-launcher provides GUI for simple installing, updating and launching of
INSTEAD games

%prep
%setup -q

%build
%qmake_qt4 PREFIX=/usr
make %{?_smp_mflags}

%install
%make_install INSTALL_ROOT=%{buildroot}
desktop-file-install                       \
--delete-original                          \
--set-icon=sdl_instead                     \
--remove-key=Encoding                      \
--remove-key=Version                       \
--dir=%{buildroot}%{_datadir}/applications \
%{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%doc readme.txt
%{_bindir}/*
%{_datadir}/applications/*

%changelog
* Wed Mar 26 2014 Ivan Epifanov <isage.dna@gmail.com> - 0.6.1-2.R
- Fix debug package and release version

* Sat Nov  5 2011 Arkady L. Shane <ashejn@russianfedora.ru> - 0.6.1-1.R
- initial build for Fedora
