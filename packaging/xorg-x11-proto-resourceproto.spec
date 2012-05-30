
Name:       xorg-x11-proto-resourceproto
Summary:    X.Org X11 Protocol resourceproto
Version:    1.1.1
Release:    0
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/resourceproto-%{version}.tar.gz
Source1001: packaging/xorg-x11-proto-resourceproto.manifest 
Provides:   resourceproto

BuildRequires:  pkgconfig(xorg-macros)

%description
Description: %{summary}



%prep
%setup -q -n %{name}-%{version}

%build
cp %{SOURCE1001} .

%reconfigure --disable-shared

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}






%files
%manifest xorg-x11-proto-resourceproto.manifest
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/resourceproto.pc
%{_includedir}/X11/extensions/XResproto.h


