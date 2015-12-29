Name:		kgeography
Summary:	A geography learning program
Version:	15.12.0
Release:	2
Group:		Graphical desktop/KDE
License:	GPLv2 GFDL
URL:		http://edu.kde.org/kgeography
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
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

%description
KGeography is a geography learning program.

%files
%doc README COPYING COPYING.DOC AUTHORS
%doc %{_docdir}/HTML/en/%{name}
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_iconsdir}/*/*/apps/%{name}.*
%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/config.kcfg/%{name}.kcfg
%{_datadir}/kxmlgui5/%{name}/kgeographyui.rc

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

