Summary:	GUI search/replace tool supporting Perl regular expression
Name:		regexxer
Version:	0.10
Release:	3
License:	GPLv2+
Group:		Text tools
Url:		http://regexxer.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/regexxer/%{name}/%{version}/%{name}-%{version}.tar.xz
Patch0:		regexxer-0.10-rosa-includes.patch
Patch1:		regexxer-0.10-rosa-glib_h.patch
Patch2:		regexxer-0.10-rosa-no_schemas_compile.patch
BuildRequires:	gtk+2.0
BuildRequires:	imagemagick
BuildRequires:	intltool
BuildRequires:	pkgconfig(gconfmm-2.6)
BuildRequires:	pkgconfig(gtkmm-3.0)
BuildRequires:	pkgconfig(glibmm-2.4)
BuildRequires:	pkgconfig(gtksourceviewmm-3.0)
BuildRequires:	pkgconfig(libglademm-2.4)
BuildRequires:	pkgconfig(libpcre)

%description
regexxer is a nifty search/replace tool for the desktop user.  It features
recursive search through directory trees and Perl-style regular expressions
(using libpcre).

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

#----------------------------------------------------------------------------

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

