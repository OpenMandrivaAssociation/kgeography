Name:		kgeography
Summary:	A geography learning program
Version:	4.8.97
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2 GFDL
URL:		http://edu.kde.org/kgeography
Source:		ftp://ftp.kde.org/pub/kde/unstable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel

%description
KGeography is a geography learning program.

%files
%doc README COPYING COPYING.DOC AUTHORS
%doc %{_kde_docdir}/HTML/en/%{name}
%{_kde_appsdir}/%{name}
%{_kde_bindir}/%{name}
%{_kde_iconsdir}/*/*/apps/%{name}.*
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_datadir}/config.kcfg/%{name}.kcfg

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

