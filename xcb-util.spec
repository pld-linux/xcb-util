Summary:	XCB support libraries
Summary(pl.UTF-8):	Biblioteki wspomagające XCB
Name:		xcb-util
Version:	0.3.6
Release:	2
License:	MIT
Group:		Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	dd8968b8ee613cb027a8ef1fcbdc8fc9
URL:		http://xcb.freedesktop.org/
BuildRequires:	gperf
BuildRequires:	libxcb-devel >= 1.4
BuildRequires:	m4
BuildRequires:	pkgconfig
BuildRequires:	xorg-proto-xproto-devel >= 7.0.8
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
%doc README
%attr(755,root,root) %{_libdir}/libxcb-atom.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-atom.so.1
%attr(755,root,root) %{_libdir}/libxcb-aux.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-aux.so.0
%attr(755,root,root) %{_libdir}/libxcb-event.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-event.so.1
%attr(755,root,root) %{_libdir}/libxcb-icccm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-icccm.so.1
%attr(755,root,root) %{_libdir}/libxcb-image.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-image.so.0
%attr(755,root,root) %{_libdir}/libxcb-keysyms.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-keysyms.so.1
%attr(755,root,root) %{_libdir}/libxcb-property.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-property.so.1
%attr(755,root,root) %{_libdir}/libxcb-render-util.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-render-util.so.0
%attr(755,root,root) %{_libdir}/libxcb-reply.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-reply.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxcb-atom.so
%attr(755,root,root) %{_libdir}/libxcb-aux.so
%attr(755,root,root) %{_libdir}/libxcb-event.so
%attr(755,root,root) %{_libdir}/libxcb-icccm.so
%attr(755,root,root) %{_libdir}/libxcb-image.so
%attr(755,root,root) %{_libdir}/libxcb-keysyms.so
%attr(755,root,root) %{_libdir}/libxcb-property.so
%attr(755,root,root) %{_libdir}/libxcb-render-util.so
%attr(755,root,root) %{_libdir}/libxcb-reply.so
%{_libdir}/libxcb-atom.la
%{_libdir}/libxcb-aux.la
%{_libdir}/libxcb-event.la
%{_libdir}/libxcb-icccm.la
%{_libdir}/libxcb-image.la
%{_libdir}/libxcb-keysyms.la
%{_libdir}/libxcb-property.la
%{_libdir}/libxcb-render-util.la
%{_libdir}/libxcb-reply.la
%{_includedir}/xcb/xcb_*.h
%{_pkgconfigdir}/xcb-atom.pc
%{_pkgconfigdir}/xcb-aux.pc
%{_pkgconfigdir}/xcb-event.pc
%{_pkgconfigdir}/xcb-icccm.pc
%{_pkgconfigdir}/xcb-image.pc
%{_pkgconfigdir}/xcb-keysyms.pc
%{_pkgconfigdir}/xcb-property.pc
%{_pkgconfigdir}/xcb-renderutil.pc
%{_pkgconfigdir}/xcb-reply.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxcb-atom.a
%{_libdir}/libxcb-aux.a
%{_libdir}/libxcb-event.a
%{_libdir}/libxcb-icccm.a
%{_libdir}/libxcb-image.a
%{_libdir}/libxcb-keysyms.a
%{_libdir}/libxcb-property.a
%{_libdir}/libxcb-render-util.a
%{_libdir}/libxcb-reply.a
