Name:		kgeography
Summary:	A geography learning program
Version:	15.04.3
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2 GFDL
URL:		http://edu.kde.org/kgeography
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)

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
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

