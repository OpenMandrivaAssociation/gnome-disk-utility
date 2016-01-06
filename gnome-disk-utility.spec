%define Werror_cflags %nil
%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define _disable_ld_no_undefined 1
%define _disable_rebuild_configure 1

Summary:	Disk management daemon
Name:		gnome-disk-utility
Version:	3.18.3.1
Release:	1
License:	LGPLv2+
Group:		System/Configuration/Other
Url:		http://git.gnome.org/cgit/gnome-disk-utility
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	pkgconfig(gio-unix-2.0) >= 2.31.0
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gnome-settings-daemon)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.3.0
BuildRequires:	pkgconfig(libsecret-1)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(libsystemd-login) >= 186
BuildRequires:	pkgconfig(pwquality)
BuildRequires:	pkgconfig(udisks2) >= 1.90
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(dvdread)
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(libnotify)

Requires:	polkit-agent
Requires:	udisks2 >= 1.90
%rename		palimpsest

%description
This package contains the Palimpsest disk management application.
Palimpsest supports partitioning, file system creation, encryption,
RAID, SMART monitoring, etc.

%prep
%setup -q

%build
%configure

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc README AUTHORS NEWS
%{_bindir}/*
%{_libdir}/gnome-settings-daemon-3.0/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_datadir}/appdata/org.gnome.DiskUtility.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.DiskUtility.service
%{_datadir}/glib-2.0/schemas/org.gnome.Disks.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.gdu-sd.gschema.xml
%{_mandir}/man1/gnome*1.*

