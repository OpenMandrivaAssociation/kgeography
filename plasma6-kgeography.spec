Name:		plasma6-kgeography
Summary:	A geography learning program
Version:	24.01.95
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2 GFDL
URL:		http://edu.kde.org/kgeography
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kgeography-%{version}.tar.xz
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

%description
KGeography is a geography learning program.

%files -f kgeography.lang
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

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n kgeography-%{?git:master}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kgeography --with-html
