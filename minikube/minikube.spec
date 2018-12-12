Name:          minikube
Version:       0.31.0
Release:       1%{?dist}
Summary:       Minikube is a tool that makes it easy to run Kubernetes locally

Group:         Development Tools
URL:           https://github.com/kubernetes/minikube
License:       ASL 2.0
Source0:       https://github.com/kubernetes/minikube/releases/download/v%{version}/%{name}-linux-amd64
ExclusiveArch: x86_64
Requires:      docker-machine-driver-kvm

%description
Minikube is a tool that makes it easy to run Kubernetes locally. Minikube
runs a single-node Kubernetes cluster inside a VM on your laptop for
users looking to try out Kubernetes or develop with it day-to-day.

%build

%prep
%setup -q -T -c

%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Wed Dec 12 2018 Sergi Jimenez <tripledes@fedoraproject.org> - 0.31.1-1
- Initial import
