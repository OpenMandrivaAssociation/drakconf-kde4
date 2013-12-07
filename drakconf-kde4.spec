Summary:	Drakx tools implementaion for KDE4 Control Center
Name:		drakconf-kde4
Version:	2013.0
Release:	5
License:	GPLv2
Group:		System/Base
BuildArch:	noarch

Requires:	kcm-rpmdrake
Requires:	kcm-harddrake
Requires:	kcm-drakguard
# Requires:	kcm-drakinvictus
Requires:	kcm-XFdrake
Requires:	kcm-drakauth
Requires:	kcm-drakdvb
Requires:	kcm-drakfirewall
Requires:	kcm-rpmdrake-update
Requires:	kcm-userdrake
Requires:	kcm-update-freq
Requires:	kcm-grub2
Requires:	kcm-rpmdrake-sources
Requires:	kcm-draksec
Requires:	drakconf-icons
Requires:	drakguard
Requires:	drakxtools
Requires:	drakx-net
Requires:	drakx-kbd-mouse-x11
Requires:	gtk+2.0
Requires:	harddrake-ui
Requires:	mandriva-release
Requires:	perl-Gtk2
Requires:	perl-Gnome2-Vte
Requires:	perl-MDK-Common
Requires:	rpmdrake 
Requires:	userdrake => 1.2
Requires:	usermode
Suggests:	mdkonline >= 2.77.19
Suggests:	system-config-printer

Conflicts:	drakconf

%description
This metapackage install needing KCM plugins for run Drakx utilites 
via KDE Control Center. It's install Rpmdrake, XFdrake, Firewall,
Userdrake and other utilites.

%files
