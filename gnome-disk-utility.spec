%define Werror_cflags %nil

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	Disk management daemon
Name:		gnome-disk-utility
Version:	3.4.1
Release:	%mkrel 1
License:	LGPLv2+
Group:		System/Configuration/Other
URL:		http://git.gnome.org/cgit/gnome-disk-utility
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gio-unix-2.0) >= 2.31.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.3.0
BuildRequires:	pkgconfig(udisks2) >= 1.90
BuildRequires:	gnome-doc-utils
BuildRequires:	intltool
BuildRequires:	gtk-doc
Requires:	polkit-agent
Requires:	udisks2 >= 1.90
Obsoletes:	palimpsest < 3.0.0

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
%{_datadir}/applications/palimpsest.desktop
%{_datadir}/icons/hicolor/*/apps/palimpsest.*
