%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	Disk management daemon
Name:		gnome-disk-utility
Version:	44.0
Release:	2
License:	LGPLv2+
Group:		System/Configuration/Other
Url:		http://git.gnome.org/cgit/gnome-disk-utility
Source0:	https://download.gnome.org/sources/gnome-disk-utility/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	cmake
BuildRequires:	gtk4
BuildRequires:	gtk-update-icon-cache
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	pkgconfig(gio-unix-2.0) >= 2.31.0
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gnome-settings-daemon)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.3.0
BuildRequires:	pkgconfig(libsecret-1)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(pwquality)
BuildRequires:	pkgconfig(udisks2) >= 1.90
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(libhandy-1)
BuildRequires:	pkgconfig(dvdread)
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel
BuildRequires:	gnome-common
BuildRequires:	meson
BuildRequires:	locales

Requires:	polkit-agent
Requires:	udisks2 >= 1.90
%rename		palimpsest

%description
This package contains the Palimpsest disk management application.
Palimpsest supports partitioning, file system creation, encryption,
RAID, SMART monitoring, etc.

%prep
%autosetup -p1
%meson

%build
%meson_build

%install
export LANG=UTF-8
%meson_install

#fix desktop files
desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications \
		%{buildroot}%{_datadir}/applications/*.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc README.md AUTHORS NEWS
%{_bindir}/*
#{_libdir}/gnome-settings-daemon-3.0/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*
#{_datadir}/appdata/org.gnome.DiskUtility.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.DiskUtility.service
%{_datadir}/glib-2.0/schemas/org.gnome.Disks.gschema.xml
#{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.gdu-sd.gschema.xml
%{_mandir}/man1/gnome*1.*
%{_datadir}/metainfo/org.gnome.DiskUtility.appdata.xml
%{_libexecdir}/gsd-disk-utility-notify
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.DiskUtilityNotify.desktop
