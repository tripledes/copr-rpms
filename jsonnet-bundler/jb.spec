Name:          jsonnet-bundler
Version:       0.4.0
Release:       1%{?dist}
Summary:       Package manager for Jsonnet

Group:         Development Tools
URL:           https://github.com/google/jsonnet
License:       ASL 2.0
Source0:       https://github.com/jsonnet-bundler/jsonnet-bundler/releases/download/v%{version}/jb-linux-amd64
ExclusiveArch: x86_64

%description
Jsonnet bundler manages dependencies in Jsonnet based projects.

%build

%prep
%setup -q -T -c

%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/jb

%files
%{_bindir}/jb

%changelog
* Wed Sep 23 2020 Sergi Jimenez <tripledes@fedoraproject.org> - 0.4.0-1
- Initial import
