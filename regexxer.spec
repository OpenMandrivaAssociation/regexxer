Summary:	GUI search/replace tool supporting Perl regular expression
Name:		regexxer
Version:	0.10
Release:	1
License:	GPLv2+
Group:		Text tools
URL:		http://regexxer.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/regexxer/%{name}/%{version}/%{name}-%{version}.tar.xz
Patch0:		regexxer-0.10-rosa-includes.patch
Patch1:		regexxer-0.10-rosa-glib_h.patch
Patch2:		regexxer-0.10-rosa-no_schemas_compile.patch
# (Abel) utf-8 support only enabled after 4.3-4mdk
BuildRequires:	pcre-devel >= 4.3-4mdk
BuildRequires:	pkgconfig(gtkmm-3.0) >= 3.0.0
BuildRequires:	pkgconfig(glibmm-2.4) >= 2.27.94
BuildRequires:	pkgconfig(gtksourceviewmm-3.0) >= 2.91.5
BuildRequires:	pkgconfig(libglademm-2.4)
BuildRequires:	gconfmm2.6-devel >= 2.6.1
BuildRequires:	imagemagick
BuildRequires:	intltool
BuildRequires:	gtk+2.0

%description
regexxer is a nifty search/replace tool for the desktop user.  It features
recursive search through directory trees and Perl-style regular expressions
(using libpcre).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
./autogen.sh
%configure2_5x --disable-schemas-compile
%make

%install
%makeinstall_std

#icons
mkdir -p %{buildroot}%{_iconsdir} \
	%{buildroot}%{_miconsdir}
install -D -m 644       ui/regexxer.png %{buildroot}%{_liconsdir}/%{name}.png
convert -geometry 32x32 ui/regexxer.png %{buildroot}%{_iconsdir}/%{name}.png
convert -geometry 16x16 ui/regexxer.png %{buildroot}%{_miconsdir}/%{name}.png

# remove seemingly useless english translation
rm -rf %{buildroot}%{_datadir}/locale/en/

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.regexxer.gschema.xml

%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/hicolor/*/apps/*


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.9-4mdv2010.0
+ Revision: 433091
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.9-3mdv2009.0
+ Revision: 242539
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - use %%post_install_gconf_schemas/%%preun_uninstall_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Funda Wang <fundawang@mandriva.org>
    - Requires(pre) rather than prereq.

* Tue May 15 2007 Funda Wang <fundawang@mandriva.org> 0.9-1mdv2008.0
+ Revision: 26817
- kill debian menu.
  fix file list.
- New upstream version
- Import regexxer



* Tue Jun 29 2004 Abel Cheung <deaddog@deaddog.org> 0.8-0.20040629.1mdk
- CVS snapshot 2004-06-29, fix 0.7 to work with g++ 3.4 is too much work

* Mon May 17 2004 Abel Cheung <deaddog@deaddog.org> 0.7-1mdk
- New release

* Fri Feb 20 2004 David Baudens <baudens@mandrakesoft.com> 0.6-2mdk
- Fix menu

* Fri Dec 12 2003 Abel Cheung <deaddog@deaddog.org> 0.6-1mdk
- New release

* Wed Nov 12 2003 Abel Cheung <deaddog@deaddog.org> 0.5-1mdk
- First Mandrake package
