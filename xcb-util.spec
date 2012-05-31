Summary:	XCB support library
Summary(pl.UTF-8):	Biblioteka wspomagająca XCB
Name:		xcb-util
Version:	0.3.9
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	01dcc7a16d5020530552712710646ea2
URL:		http://xcb.freedesktop.org/XcbUtil/
BuildRequires:	libxcb-devel >= 1.4
BuildRequires:	pkgconfig
BuildRequires:	xcb-proto >= 1.6
BuildRequires:	xorg-proto-xproto-devel >= 7.0.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

XCB util module provides the following library:
- aux: Convenient access to connection setup and some core requests.
- atom: Standard core X atom constants and atom caching.
- event: Callback X event handling.

%description -l pl.UTF-8
xcb-util udostępnia wiele bibliotek opartych powyżej libxcb (głównej
biblioteki protokołu X) oraz trochę bibliotek rozszerzeń. Te
eksperymentalne biblioteki udostępniają wygodne funkcje i interfejsy
czyniące surowy protokół X bardziej używalnym. Niektóre biblioteki
udostępniają także kod kliencki nie będący ściśle częścią protokołu X,
ale tradycyjnie dostarczany przez Xlib.

Moduł XCB util udostępnia następujące biblioteki:
- aux: wygodny dostęp do konfiguracji połączenia i niektórych głównych
  żądań.
- atom: standardowe stałe atomowe X i buforowanie atomowe.
- event: obsługa wywołań zwrotnych dla zdarzeń X.

%package devel
Summary:	Header files for XCB util library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki XCB util
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxcb-devel >= 1.4

%description devel
Header files for XCB util library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki XCB util.

%package static
Summary:	Static XCB util library
Summary(pl.UTF-8):	Statyczna biblioteka XCB util
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XCB util library.

%description static -l pl.UTF-8
Statyczna biblioteka XCB util.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libxcb-util.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-util.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxcb-util.so
%{_libdir}/libxcb-util.la
%{_includedir}/xcb/xcb_atom.h
%{_includedir}/xcb/xcb_aux.h
%{_includedir}/xcb/xcb_event.h
%{_includedir}/xcb/xcb_util.h
%{_pkgconfigdir}/xcb-atom.pc
%{_pkgconfigdir}/xcb-aux.pc
%{_pkgconfigdir}/xcb-event.pc
%{_pkgconfigdir}/xcb-util.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxcb-util.a
