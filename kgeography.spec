Name: kgeography
Summary: A geography learning program
Version: 4.8.3
Release: 1
Group: Graphical desktop/KDE
License: GPLv2 GFDL
URL: http://edu.kde.org/kgeography
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.xz
BuildRequires: kdelibs4-devel >= 2:%{version}

%description
KGeography is a geography learning program.

%files
%_kde_appsdir/kgeography
%_kde_bindir/kgeography
%_kde_iconsdir/*/*/apps/kgeography.*
%_kde_datadir/applications/kde4/kgeography.desktop
%_kde_datadir/config.kcfg/kgeography.kcfg
%doc README COPYING COPYING.DOC AUTHORS
%doc %_kde_docdir/HTML/en/kgeography

#----------------------------------------------------------------------

%prep
%setup -q 
%apply_patches

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

