%define major 5
%define apiver 0.5
%define libname %mklibname fo %{apiver} %{major}
%define develname %mklibname fo -d

Summary:	XSL formatter
Name:		xmlroff
Version:	0.5.1
Release:	%mkrel 1
License:	Distributable
Group:		Text tools
URL:		http://xmlroff.org
Source0:	http://xmlroff.org/download/xmlroff-0.5.1.tar.bz2
BuildRequires:	libglib2-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	libcairo-devel
BuildRequires:	freetype6-devel
BuildRequires:	libpango-devel
BuildRequires:	libgdk_pixbuf2.0-devel
Requires:	%{libname} = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Xmlroff is a fast, free, high-quality, multi-platform XSL 
formatter that aims to excel at DocBook formatting and that 
integrates easily with other programs and with scripting languages.

%package -n %{libname}
Summary:	Shared libraries for %{name}
Group:		System/Libraries

%description -n %{libname}
The %{name} XSL formatter library.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Provides:	libfo-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
Development files for %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING NEWS README TODO AUTHORS ChangeLog
%{_bindir}/%{name}
%{_datadir}/xml/libfo-*/
%{_datadir}/gtk-doc/html/%{name}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*%{apiver}.so.%{major}*

%files -n%{develname}
%defattr(-,root,root)
%dir %{_includedir}/libfo-%{apiver}
%dir %{_includedir}/libfo-%{apiver}/area
%dir %{_includedir}/libfo-%{apiver}/datatype
%dir %{_includedir}/libfo-%{apiver}/property
%dir %{_includedir}/libfo-%{apiver}/util
%dir %{_includedir}/libfo-%{apiver}/fo
%{_includedir}/libfo-%{apiver}/*.h
%{_includedir}/libfo-%{apiver}/area/*.h
%{_includedir}/libfo-%{apiver}/datatype/*.h
%{_includedir}/libfo-%{apiver}/property/*.h
%{_includedir}/libfo-%{apiver}/util/*.h
%{_includedir}/libfo-%{apiver}/fo/*.h
%{_libdir}/lib*%{apiver}.a
%{_libdir}/lib*%{apiver}.la
%{_libdir}/lib*%{apiver}.so
%{_libdir}/pkgconfig/*.pc
