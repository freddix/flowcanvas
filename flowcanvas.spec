Summary:	Gtkmm/Gnomecanvasmm widget
Name:		flowcanvas
Version:	0.7.1
Release:	2
License:	GPL v2
Group:		Libraries
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.bz2
# Source0-md5:	a4908f6385ce9fd2ce97c8caa823f053
BuildRequires:	boost-devel
BuildRequires:	graphviz-devel
BuildRequires:	libgnomecanvasmm-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FlowCanvas is an interactive Gtkmm/Gnomecanvasmm widget
for "boxes and lines" environments (ie modular synths
or interactive finite state automata diagrams).

%package devel
Summary:	Header files for flowcanvas library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for flowcanvas library.

%prep
%setup -q

%build
export CC="%{__cc}"
export CXX="%{__cxx}"
export CCFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcxxflags}"
export LDFLAGS="%{rpmldflags}"
./waf configure \
	--prefix=%{_prefix}	\
	--libdir=%{_libdir}	\
	--nocache
./waf -v build

%install
rm -rf $RPM_BUILD_ROOT

./waf -v install	\
	--destdir=$RPM_BUILD_ROOT

chmod +x $RPM_BUILD_ROOT%{_libdir}/*.so*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %ghost %{_libdir}/libflowcanvas.so.?
%attr(755,root,root) %{_libdir}/libflowcanvas.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libflowcanvas.so
%{_includedir}/flowcanvas
%{_pkgconfigdir}/*.pc

