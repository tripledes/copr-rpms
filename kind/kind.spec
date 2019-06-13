Name:          kind
Version:       0.3.0
Release:       2%{?dist}
Summary:       kind is a tool for running local Kubernetes clusters using Docker container "nodes".

Group:         Development Tools
URL:           https://github.com/kubernetes-sigs/kind
License:       ASL 2.0
Source0:       https://github.com/kubernetes-sigs/kind/releases/download/v%{version}/kind-linux-amd64
ExclusiveArch: x86_64
Requires:      docker

%description
kind is a tool for running local Kubernetes clusters using Docker container “nodes”.

%build

%prep
%setup -q -T -c

%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Thu Jun 13 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 0.3.0-1
- Initial import
