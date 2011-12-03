%define _disable_ld_no_undefined 1
%define major 0
%define libname	%mklibname gdu %major
%define libgtk	%mklibname gdu-gtk %major
%define develname %mklibname -d gdu

Summary: Disk management daemon
Name: gnome-disk-utility
Version: 3.0.2
Release: 1
License: LGPLv2+
Group: System/Configuration/Other
URL: http://git.gnome.org/cgit/gnome-disk-utility
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
Patch0: gnome-disk-utility-2.30.1-utf8.patch

BuildRequires:	intltool
BuildRequires:	pkgconfig(avahi-ui)
BuildRequires:	pkgconfig(avahi-ui-gtk3)
BuildRequires:	pkgconfig(dbus-glib-1) >= 0.74
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gtk+-3.0) >= 0.74
BuildRequires:	pkgconfig(libatasmart)
BuildRequires:	pkgconfig(libnautilus-extension)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(udisks)
BuildRequires:	pkgconfig(unique-3.0) >= 2.90.1

Requires: polkit-agent
Obsoletes: %{name}-data

%description
This package contains the Gnome Disk Utility daemon. It supports the detection
and creation of disk volumes.

%package -n palimpsest
Summary: Disk management application
Group: System/Configuration/Other
Requires: %{name} = %{version}-%{release}

%description -n palimpsest
This package contains the Palimpsest disk management application.
Palimpsest supports partitioning, file system creation, encryption,
RAID, SMART monitoring, etc.

%package -n %{libname}
Summary: Shared libraries used by Palimpsest
Group: System/Libraries
Requires: udisks

%description -n %{libname}
This package contains libraries that are used by the Palimpsest
disk management application. The libraries in this package do not
contain UI-related code.

%package -n %{libgtk}
Summary: Shared libraries used by Palimpsest
Group: System/Libraries

%description -n %{libgtk}
This package contains libraries that are used by the Palimpsest
disk management application. The libraries in this package contain
disk-related widgets for use in GTK+ applications.

%package -n %{develname}
Summary: Development files for gnome-disk-utility-libs
Group: Development/C
Provides: libgdu-devel = %{version}-%{release}
Requires: %{libname} = %{version}-%{release}
Requires: %{libgtk} = %{version}-%{release}

%description -n %{develname}
This package contains header files and libraries needed to
develop applications with gnome-disk-utility-libs.
%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static

%make

%install
rm -rf %{buildroot} %{name}.lang palimpsest.lang
%makeinstall_std
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print
%find_lang %{name}
%find_lang palimpsest --with-gnome

for omf in %{buildroot}%{_datadir}/omf/*/*-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%{buildroot}!!)" >> palimpsest.lang
done

%files -f %{name}.lang
%doc README AUTHORS NEWS 
%{_libexecdir}/gdu-notification-daemon
%config(noreplace) %{_sysconfdir}/xdg/autostart/gdu-notification-daemon.desktop
%{_libdir}/nautilus/extensions-3.0/*.so
%{_libexecdir}/gdu-format-tool
%{_datadir}/icons/hicolor/*/apps/gdu*.png
%{_datadir}/icons/hicolor/scalable/apps/gdu*.svg
%{_datadir}/icons/hicolor/*/apps/nautilus*.png
%{_datadir}/icons/hicolor/scalable/apps/nautilus*.svg

%files -n palimpsest -f palimpsest.lang
%{_bindir}/palimpsest
%{_datadir}/applications/palimpsest.desktop
%{_datadir}/icons/hicolor/*/apps/palimpsest*.png
%dir %{_datadir}/omf/palimpsest
%{_datadir}/omf/palimpsest/palimpsest-C.omf

%files -n %{libname}
%{_libdir}/libgdu.so.%{major}*

%files -n %{libgtk}
%{_libdir}/libgdu-gtk.so.%{major}*

%files -n %{develname}
%{_libdir}/libgdu.so
%{_libdir}/libgdu-gtk.so
%{_libdir}/pkgconfig/gdu.pc
%{_libdir}/pkgconfig/gdu-gtk.pc
%dir %{_includedir}/gnome-disk-utility
%dir %{_includedir}/gnome-disk-utility/gdu
%{_includedir}/gnome-disk-utility/gdu/*
%dir %{_includedir}/gnome-disk-utility/gdu-gtk
%{_includedir}/gnome-disk-utility/gdu-gtk/*

