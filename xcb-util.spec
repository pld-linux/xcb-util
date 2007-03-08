Summary:	XCB support libraries
Summary(pl.UTF-8):	Biblioteki wspomagające XCB
Name:		xcb-util
Version:	0.2
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	b09bdebad50638709de22d8eb2dc3bf5
URL:		http://xcb.freedesktop.org/
BuildRequires:	gperf
BuildRequires:	libxcb-devel >= 1.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

These libraries are currently included, roughly ordered by maturity:

render-util: Convenience functions for the Render extension.

aux: Convenient access to connection setup and some core requests.

atom: Standard core X atom constants and atom caching.

property: Callback X property-change handling.

icccm: Both client and window-manager helpers for ICCCM.

keysyms: Standard X key constants and conversion to/from keycodes.

event: Callback X event handling.

image: Port of Xlib's XImage and XShmImage functions.

wm: Framework for window manager implementation.

%description -l pl.UTF-8
xcb-util udostępnia wiele bibliotek opartych powyżej libxcb (głównej
biblioteki protokołu X) oraz trochę bibliotek rozszerzeń. Te
eksperymentalne biblioteki udostępniają wygodne funkcje i interfejsy
czyniące surowy protokół X bardziej używalnym. Niektóre biblioteki
udostępniają także kod kliencki nie będący ściśle częścią protokołu X,
ale tradycyjnie dostarczany przez Xlib.

Załączone biblioteki w kolejności dojrzałości to:

render-util: wygodne funkcje do rozszerzenia Render.

aux: wygodny dostęp do konfiguracji połączenia i niektórych głównych
żądań.

atom: standardowe stałe atomowe X i buforowanie atomowe.

property: obsługa wywołań zwrotnych przy zmianie własności X.

icccm: funkcje pomocnicze dla klientów i zarządców okien do ICCCM.

keysyms: standardowe stałe i konwersje klawiszy X z/do kodów klawiszy.

event: obsługa wywołań zwrotnych dla zdarzeń X.

image: port funkcji XImage i XShmImage z Xlib.

wm: szkielet dla implementacji zarządców okien.

%package devel
Summary:	Header files for XCB util libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek XCB util
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxcb-devel >= 1.0

%description devel
Header files for XCB util libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek XCB util.

%package static
Summary:	Static XCB util libraries
Summary(pl.UTF-8):	Statyczne biblioteki XCB util
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XCB util libraries.

%description static -l pl.UTF-8
Statyczne biblioteki XCB util.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/libxcb

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/libxcb-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxcb-*.so
%{_libdir}/libxcb-*.la
%{_includedir}/xcb/xcb_*.h
%{_pkgconfigdir}/xcb-*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxcb-*.a
