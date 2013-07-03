Name: fbset
Version: 2.1
Release: 1
Summary: Framebuffer setting utility
Group: System/Base
License: GPL
URL: http://users.telenet.be/geertu/Linux/fbdev/
Source0: %{name}-%{version}.tar.gz
BuildRequires: bison, flex
Patch0: build.patch

%description
%{summary}.

%files
%defattr(-,root,root,-)
%{_sbindir}/fbset

%package doc
Summary: Documentation for %{name}

%description doc
%{summary}.

%files doc
%defattr(-,root,root,-)
%{_mandir}/man5/*
%{_mandir}/man8/*

%prep
%setup -q -n %{name}-%{version}/%{name}
%patch0 -p1


%build
make fbset


%install
make fbset DESTDIR=%{buildroot} install
