%define name	drakconf-kde4
%define version	2012.1
%define release	3

Summary:	Drakx tools implementaion for KDE4 Control Center
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Base
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

Requires:	kcm-rpmdrake
Requires:	kcm-harddrake
Requires:	kcm-drakguard
#Requires:	kcm-drakinvictus
Requires:	kcm-XFdrake
Requires:	kcm-drakauth
#Requires:	kcm-drakdvb
Requires:	kcm-drakfirewall
Requires:	kcm-rpmdrake-update
Requires:	kcm-userdrake
#Requires:	kcm-update-freq
Requires:	kcm-grub2
Requires:	kcm-rpmdrake-sources
Requires:	kcm-draksec
Requires:	kcm-printer

Requires: mandriva-release
Requires: drakxtools
Requires: harddrake-ui
Requires: popt
Requires: usermode
Requires: perl-Gtk2
Requires: perl-Gnome2-Vte
Requires: gtk+2.0
Requires: perl-MDK-Common
Suggests: system-config-printer
Requires: rpmdrake 
Requires: drakguard
Suggests: mdkonline >= 2.77.19
Requires: userdrake => 1.2
Requires: drakconf-icons
Requires: drakx-net
Requires: drakx-kbd-mouse-x11

Conflicts:	drakconf

%description
This metapackage install needing KCM plugins for run Drakx utilites 
via KDE Control Center. It's install Rpmdrake, XFdrake, Firewall,
Userdrake and other utilites.

%files
