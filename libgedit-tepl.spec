#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_without	static_libs	# static library
#
Summary:	Tepl - Text editor product line
Summary(pl.UTF-8):	Tepl (Text editor product line) - linia produkcyjna edytorów
Name:		libgedit-tepl
Version:	6.12.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
# also https://github.com/gedit-technology/libgedit-tepl/releases
Source0:	https://download.gnome.org/sources/libgedit-tepl/6.12/%{name}-%{version}.tar.xz
# Source0-md5:	332463dcca18b5035ad936aeb09473b2
URL:		https://gitlab.gnome.org/World/gedit/libgedit-tepl
BuildRequires:	gettext-tools >= 0.19.6
BuildRequires:	glib2-devel >= 1:2.74
BuildRequires:	gobject-introspection-devel >= 1.42.0
BuildRequires:	gsettings-desktop-schemas-devel >= 42
BuildRequires:	gtk+3-devel >= 3.22
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.25}
BuildRequires:	libgedit-amtk-devel >= 5.8
BuildRequires:	libgedit-gfls-devel
BuildRequires:	libgedit-gtksourceview-devel >= 299.3.0
BuildRequires:	libhandy1-devel >= 1.6
BuildRequires:	libicu-devel
BuildRequires:	meson >= 0.64
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= 1:2.74
Requires:	gtk+3 >= 3.22
Requires:	libgedit-gtksourceview >= 299.3.0
Obsoletes:	tepl < 6.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tepl is a library that eases the development of GtkSourceView-based
text editors and IDEs.

Tepl was previously named Gtef (GTK+ text editor framework). The
project has been renamed in June 2017 to have a more beautiful name.

%description -l pl.UTF-8
Tepl to biblioteka ułatawiająca tworzenie edytorów tekstu i IDE
opartych na GtkSourceView.

Tepl wcześniej nazywał się Gtef (GTK+ text editor framework - skielet
edytorów tekstu GTK+); nazwa została zmieniona w czerwcu 2017 na
ładniej brzmiącą.

%package devel
Summary:	Header files for Tepl library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Tepl
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.74
Requires:	gsettings-desktop-schemas-devel >= 42
Requires:	gtk+3-devel >= 3.22
Requires:	libgedit-amtk-devel >= 5.8
Requires:	libgedit-gtksourceview-devel >= 299.3.0
Requires:	libhandy1-devel >= 1.6
Requires:	libicu-devel
Obsoletes:	tepl-devel < 6.10
Obsoletes:	vala-tepl < 2.99.2

%description devel
Header files for Tepl library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Tepl.

%package static
Summary:	Static Tepl library
Summary(pl.UTF-8):	Statyczna biblioteka Tepl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	tepl-static < 6.10

%description static
Static Tepl library.

%description static -l pl.UTF-8
Statyczna biblioteka Tepl.

%package apidocs
Summary:	API documentation for Tepl library
Summary(pl.UTF-8):	Dokumentacja API biblioteki Tepl
Group:		Documentation
Obsoletes:	tepl-apidocs < 6.10
BuildArch:	noarch

%description apidocs
API documentation for Tepl library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki Tepl.

%prep
%setup -q

%build
%meson build \
	%{!?with_static_libs:--default-library=shared} \
	%{!?with_apidocs:-Dgtk_doc=false}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang libgedit-tepl-6

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f libgedit-tepl-6.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_libdir}/libgedit-tepl-6.so.2
%{_libdir}/girepository-1.0/Tepl-6.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgedit-tepl-6.so
%{_includedir}/libgedit-tepl-6
%{_datadir}/gir-1.0/Tepl-6.gir
%{_pkgconfigdir}/libgedit-tepl-6.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgedit-tepl-6.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgedit-tepl-6
%endif
