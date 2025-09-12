#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Name:		kgeography
Summary:	A geography learning program
Version:	25.08.1
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2 GFDL
URL:		https://edu.kde.org/kgeography
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%if 0%{?git:1}
Source0:	https://invent.kde.org/education/kgeography/-/archive/%{gitbranch}/kgeography-%{gitbranchd}.tar.bz2#/kgeography-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kgeography-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires: 	cmake(KF6XmlGui)
BuildRequires: 	cmake(KF6WidgetsAddons)
BuildRequires: 	cmake(KF6CoreAddons)
BuildRequires: 	cmake(KF6ConfigWidgets)
BuildRequires: 	cmake(KF6I18n)
BuildRequires: 	cmake(KF6ItemViews)
BuildRequires: 	cmake(KF6IconThemes)
BuildRequires: 	cmake(KF6Service)
BuildRequires: 	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Crash)

%rename plasma6-kgeography

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KGeography is a geography learning program.

%files -f %{name}.lang
%doc README COPYING COPYING.DOC AUTHORS
%{_datadir}/kgeography
%{_bindir}/kgeography
%{_iconsdir}/*/*/apps/kgeography.*
%{_datadir}/applications/org.kde.kgeography.desktop
%{_datadir}/config.kcfg/kgeography.kcfg
%{_datadir}/metainfo/org.kde.kgeography.appdata.xml
%lang(fi) %{_datadir}/locale/fi/LC_SCRIPTS/kgeography
%lang(fr) %{_datadir}/locale/fr/LC_SCRIPTS/kgeography
%lang(ja) %{_datadir}/locale/ja/LC_SCRIPTS/kgeography
%lang(ml) %{_datadir}/locale/ml/LC_SCRIPTS/kgeography
%lang(pl) %{_datadir}/locale/pl/LC_SCRIPTS/kgeography
%lang(uk) %{_datadir}/locale/uk/LC_SCRIPTS/kgeography
