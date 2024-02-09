%define api		0.2
%define major		0
%define libname		%mklibname manette %{api} %{major}
%define girmanettename	%mklibname manette-gir %{api}
%define develname	%mklibname manette -d

Name:           libmanette
Version:	0.2.7
Release:	1
Summary:        A simple GObject game controller library
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://gitlab.gnome.org/aplazas/libmanette/
Source:         https://download.gnome.org/sources/libmanette/0.2/%{name}-%{version}.tar.xz

BuildRequires:  gobject-introspection-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:	pkgconfig(gobject-introspection-1.0)

%description
libmanette allows easy access to game controllers.

%package -n	%{libname}
Summary:        A simple GObject game controller library
Group:          System/Libraries

%description -n	%{libname}
libmanette allows easy access to game controllers.

%package -n	%{girmanettename}
Summary:        GObject introspection bindings for liblibmanette
Group:          System/Libraries

%description -n	%{girmanettename}
libmanette allows easy access to game controllers.
This subpackage contains the gobject bindings for the liblibmanette
shared library.

%package -n	%{develname}
Summary:        Development files for the libmanette library
Group:          Development/Languages/C and C++
Requires:	%{girmanettename} = %{version}-%{release}

%description -n	%{develname}
libmanette allows easy access to game controllers.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files -n %{libname}
%doc README.md NEWS
%license COPYING
%{_libdir}/libmanette-%{api}.so.%{major}{,.*}

%files -n %{girmanettename}
%doc README.md NEWS
%{_libdir}/girepository-1.0/Manette-%{api}.typelib

%files -n %{develname}
%doc README.md NEWS
%{_bindir}/manette-test
%{_includedir}/libmanette/
%{_libdir}/libmanette-%{api}.so
%{_libdir}/pkgconfig/manette-%{api}.pc
%{_datadir}/gir-1.0/Manette-%{api}.gir
%{_datadir}/vala/vapi/manette-%{api}.deps
%{_datadir}/vala/vapi/manette-%{api}.vapi
