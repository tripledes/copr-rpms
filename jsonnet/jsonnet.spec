Name:          jsonnet
Version:       0.16.0
Release:       1%{?dist}
Summary:       Jsonnet CLI

Group:         Development Tools
URL:           https://github.com/google/jsonnet
License:       ASL 2.0
Source0:       https://github.com/google/jsonnet/releases/download/v%{version}/jsonnet-bin-v%{version}-linux.tar.gz
ExclusiveArch: x86_64

%description
Jsonnet is a data templating language for app and tool developers.
This package includes both, jsonnet and jsonnetfmt CLI tools.

%build

%prep
%setup -q -T -c

%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}
%{__install} -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}fmt

%files
%{_bindir}/%{name}
%{_bindir}/%{name}fmt

%changelog
* Wed Sep 22 2020 Sergi Jimenez <tripledes@fedoraproject.org> - 0.16.0-1
- Initial import
