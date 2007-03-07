Summary:	XCB support libraries
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

render-util: Convenience functions for the Render extension. aux:
Convenient access to connection setup and some core requests. atom:
Standard core X atom constants and atom caching. property: Callback X
property-change handling. icccm: Both client and window-manager
helpers for ICCCM. keysyms: Standard X key constants and conversion
to/from keycodes. event: Callback X event handling. image: Port of
Xlib's XImage and XShmImage functions. wm: Framework for window
manager implementation.

%package devel
Summary:	Header files for XCB util libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxcb-devel

%description devel
Header files for XCB util libraries.

%package static
Summary:	Static XCB util libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XCB util libraries.

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
%attr(755,root,root) %{_libdir}/libxcb*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxcb*.so
%{_libdir}/libxcb*.la
%{_includedir}/xcb
%{_pkgconfigdir}/xcb*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxcb*.a
