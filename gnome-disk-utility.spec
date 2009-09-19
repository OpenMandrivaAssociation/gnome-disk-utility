%define dbus_glib_version	  0.76
%define glib2_version             2.16
%define gtk2_version              2.17.2
%define gnome_doc_utils_version   0.3.2
%define gnome_keyring_version     2.22
%define devicekit_disks_version   007
%define unique_version            1.0.4
%define libnotify_version         0.4.5
%define nautilus_version          2.26

%define major 0
%define libname %mklibname gdu %major
%define libnamegtk %mklibname gdu-gtk %major
%define develname %mklibname -d gdu

Summary: Disk management application
Name: gnome-disk-utility
Version: 2.28.0
Release: %mkrel 1
License: LGPLv2+
Group: System/Configuration/Other
URL: http://git.gnome.org/cgit/gnome-disk-utility
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: dbus-glib-devel >= %{dbus_glib_version}
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: gnome-doc-utils >= %{gnome_doc_utils_version}
BuildRequires: desktop-file-utils
BuildRequires: gnome-keyring-devel >= %{gnome_keyring_version}
BuildRequires: devicekit-disks-devel >= %{devicekit_disks_version}
BuildRequires: unique-devel >= %{unique_version}
BuildRequires: libnotify-devel >= %{libnotify_version}
BuildRequires: nautilus-devel >= %{nautilus_version}
BuildRequires: libatasmart-devel
BuildRequires: intltool
BuildRequires: gtk-doc
Requires: %{libnamegtk} >= %{version}-%{release}
Requires: polkit-agent

%description
This package contains the Palimpsest disk management application.
Palimpsest supports partitioning, file system creation, encryption,
RAID, SMART monitoring, etc.

%package data
Summary: Translations and icons used by Palimpsest
Group: System/Libraries

%description data
This package contains the Palimpsest disk management application.
Palimpsest supports partitioning, file system creation, encryption,
RAID, SMART monitoring, etc.

%package -n %libname
Summary: Shared libraries used by Palimpsest
Group: System/Libraries
Requires: devicekit-disks >= %{devicekit_disks_version}
Requires: %name-data >= %version

%description -n %libname
This package contains libraries that are used by the Palimpsest
disk management application. The libraries in this package do not
contain UI-related code.

%package -n %libnamegtk
Summary: Shared libraries used by Palimpsest
Group: System/Libraries
Requires: %{libname} = %{version}-%{release}

%description -n %libnamegtk
This package contains libraries that are used by the Palimpsest
disk management application. The libraries in this package contain
disk-related widgets for use in GTK+ applications.

%package -n %develname
Summary: Development files for gnome-disk-utility-libs
Group: Development/C
Requires: %{libnamegtk} = %{version}-%{release}

%description -n %develname
This package contains header files and libraries needed to
develop applications with gnome-disk-utility-libs.
%prep
%setup -q

%build
%define _disable_ld_no_undefined 1
%configure2_5x
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# TODO: upstream doesn't ship a HACKING file yet
#echo " " > HACKING

rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0/*.a


%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root,-)
%doc README AUTHORS NEWS doc/TODO
#HACKING
%{_libexecdir}/gdu-notification-daemon
%config(noreplace) %{_sysconfdir}/xdg/autostart/gdu-notification-daemon.desktop
%{_libdir}/nautilus/extensions-2.0/*.so
%{_libexecdir}/gdu-format-tool

%{_bindir}/palimpsest
%{_datadir}/applications/palimpsest.desktop

%dir %{_datadir}/gnome/help/palimpsest
%{_datadir}/gnome/help/palimpsest/*

%dir %{_datadir}/omf/palimpsest
%{_datadir}/omf/palimpsest/*

%files data  -f %{name}.lang
%defattr(-,root,root,-)
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg


%files -n %libname
%defattr(-,root,root,-)
%{_libdir}/libgdu.so.%{major}*


%files -n %libnamegtk
%defattr(-,root,root,-)
%{_libdir}/libgdu-gtk.so.%{major}*

%files -n %develname
%defattr(-,root,root,-)
%{_libdir}/libgdu.so
%{_libdir}/libgdu.la
%{_libdir}/libgdu-gtk.so
%{_libdir}/libgdu-gtk.la
%{_libdir}/pkgconfig/gdu.pc
%{_libdir}/pkgconfig/gdu-gtk.pc

%dir %{_includedir}/gnome-disk-utility
%dir %{_includedir}/gnome-disk-utility/gdu
%{_includedir}/gnome-disk-utility/gdu/*
%dir %{_includedir}/gnome-disk-utility/gdu-gtk
%{_includedir}/gnome-disk-utility/gdu-gtk/*
%dir %{_datadir}/gtk-doc/html/gnome-disk-utility
%{_datadir}/gtk-doc/html/gnome-disk-utility/*


