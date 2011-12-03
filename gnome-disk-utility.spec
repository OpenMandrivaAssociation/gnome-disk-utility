%define major 0
%define libname	%mklibname gdu %major
%define libgtk	%mklibname gdu-gtk %major
%define develname %mklibname -d gdu

Summary: Disk management daemon
Name: gnome-disk-utility
Version: 2.32.1
Release: 4
License: LGPLv2+
Group: System/Configuration/Other
URL: http://git.gnome.org/cgit/gnome-disk-utility
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0: gnome-disk-utility-2.30.1-utf8.patch
Patch1: gnome-disk-utility-2.32.1-fix-underlinking.patch

BuildRequires: dbus-glib-devel >= 0.76
BuildRequires: glib2-devel >= 2.16
BuildRequires: gtk2-devel >= 2.17.2
BuildRequires: gnome-doc-utils >= 0.3.2
BuildRequires: desktop-file-utils
BuildRequires: libgnome-keyring-devel >= 2.22
BuildRequires: unique-devel >= 1.0.4
BuildRequires: udisks-devel
BuildRequires: libnotify-devel >= 0.4.5
BuildRequires: nautilus-devel >= 2.26
BuildRequires: libatasmart-devel
BuildRequires: libavahi-ui-devel
BuildRequires: intltool
BuildRequires: gtk-doc
Requires: polkit-agent
#gw fix upgrade from 2010.0:
#https://qa.mandriva.com/show_bug.cgi?id=58371
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
automake -f

%build
%configure2_5x \
	--disable-static \
	--enable-gtk-doc

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
%{_libdir}/nautilus/extensions-2.0/*.so
%{_libexecdir}/gdu-format-tool
%{_datadir}/icons/hicolor/*/apps/gdu*.png
%{_datadir}/icons/hicolor/scalable/apps/gdu*.svg
%{_datadir}/icons/hicolor/*/apps/nautilus*.png
%{_datadir}/icons/hicolor/scalable/apps/nautilus*.svg

%files -n palimpsest -f palimpsest.lang
%{_bindir}/palimpsest
%{_datadir}/applications/palimpsest.desktop
%{_datadir}/icons/hicolor/*/apps/palimpsest*.png
%{_datadir}/icons/hicolor/scalable/apps/palimpsest*.svg
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
#%dir %{_datadir}/gtk-doc/html/gnome-disk-utility
#%{_datadir}/gtk-doc/html/gnome-disk-utility/*

