%define	version	0.9
%define release	%mkrel 1

Summary:	GUI search/replace tool supporting Perl regular expression
Name:		regexxer
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Text tools
URL:		http://regexxer.sourceforge.net/
Source:		http://heanet.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
# (Abel) utf-8 support only enabled after 4.3-4mdk
BuildRequires:	pcre-devel >= 4.3-4mdk
BuildRequires:	gtkmm2.4-devel
BuildRequires:	libglademm2.4-devel
BuildRequires:	gconfmm2.6-devel >= 2.6.1
BuildRequires:	ImageMagick
Requires(post):		GConf2 >= 2.3.3
Requires(preun):	GConf2 >= 2.3.3

%description
regexxer is a nifty search/replace tool for the desktop user.  It features
recursive search through directory trees and Perl-style regular expressions
(using libpcre).

%prep
%setup -q

%build
%configure2_5x --disable-schemas-install
%make

%install
rm -rf %{buildroot}
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

#icons
mkdir -p %{buildroot}%{_iconsdir} \
         %{buildroot}%{_miconsdir}
install -D -m 644       ui/regexxer.png %{buildroot}%{_liconsdir}/%{name}.png
convert -geometry 32x32 ui/regexxer.png %{buildroot}%{_iconsdir}/%{name}.png
convert -geometry 16x16 ui/regexxer.png %{buildroot}%{_miconsdir}/%{name}.png

# remove seemingly useless english translation
rm -rf %{buildroot}%{_datadir}/locale/en/

%find_lang %{name}

%post
%update_menus
%post_install_gconf_schemas regexxer

%preun
%preun_uninstall_gconf_schemas "$1"

%postun
%clean_menus

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/*
%{_datadir}/%{name}

%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
