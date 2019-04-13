Name:		kgeography
Summary:	A geography learning program
Version:	 19.04.0
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2 GFDL
URL:		http://edu.kde.org/kgeography
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires: 	cmake(KF5XmlGui)
BuildRequires: 	cmake(KF5WidgetsAddons)
BuildRequires: 	cmake(KF5CoreAddons)
BuildRequires: 	cmake(KF5ConfigWidgets)
BuildRequires: 	cmake(KF5I18n)
BuildRequires: 	cmake(KF5ItemViews)
BuildRequires: 	cmake(KF5IconThemes)
BuildRequires: 	cmake(KF5Service)
BuildRequires: 	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Crash)

%description
KGeography is a geography learning program.

%files -f kgeography.lang
%doc README COPYING COPYING.DOC AUTHORS
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_iconsdir}/*/*/apps/%{name}.*
%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/config.kcfg/%{name}.kcfg
%{_datadir}/kxmlgui5/%{name}/kgeographyui.rc
%{_datadir}/metainfo/org.kde.kgeography.appdata.xml
%lang(fi) %{_datadir}/locale/fi/LC_SCRIPTS/kgeography
%lang(fr) %{_datadir}/locale/fr/LC_SCRIPTS/kgeography
%lang(ja) %{_datadir}/locale/ja/LC_SCRIPTS/kgeography
%lang(pl) %{_datadir}/locale/pl/LC_SCRIPTS/kgeography
%lang(uk) %{_datadir}/locale/uk/LC_SCRIPTS/kgeography

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kgeography --with-html
