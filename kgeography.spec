Name:		kgeography
Summary:	A geography learning program
Version:	15.04.3
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2 GFDL
URL:		http://edu.kde.org/kgeography
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)

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
%{_datadir}/kxmlgui5/%{name}/%{name}.rc

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

