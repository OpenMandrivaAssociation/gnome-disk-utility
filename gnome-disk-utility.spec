%define Werror_cflags %nil

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	Disk management daemon
Name:		gnome-disk-utility
Version:	3.5.2
Release:	1
License:	LGPLv2+
Group:		System/Configuration/Other
URL:		http://git.gnome.org/cgit/gnome-disk-utility
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gio-unix-2.0) >= 2.31.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.3.0
BuildRequires:	pkgconfig(udisks2) >= 1.90
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(pwquality)
BuildRequires:	pkgconfig(libsystemd-login) >= 186
BuildRequires:	gnome-doc-utils
BuildRequires:	intltool
BuildRequires:	gtk-doc
Requires:	polkit-agent
Requires:	udisks2 >= 1.90
%rename	palimpsest

%description
This package contains the Palimpsest disk management application.
Palimpsest supports partitioning, file system creation, encryption,
RAID, SMART monitoring, etc.

%prep
%setup -q

%build
%configure2_5x \
        --disable-static
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc README AUTHORS NEWS
%{_bindir}/*
%{_datadir}/%{name}
