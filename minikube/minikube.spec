Name:          minikube
Version:       1.10.1
Release:       1%{?dist}
Summary:       Minikube is a tool that makes it easy to run Kubernetes locally

Group:         Development Tools
URL:           https://github.com/kubernetes/minikube
License:       ASL 2.0
Source0:       https://github.com/kubernetes/minikube/releases/download/v%{version}/%{name}-linux-amd64
ExclusiveArch: x86_64
Requires:      docker-machine-driver-kvm2

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
* Sun May 17 2020 Johan Kok <johan@fedoraproject.org> - 1.10.1-1
- Bump to 1.10.1

* Thu Apr 30 2020 Johan Kok <johan@fedoraproject.org> - 1.9.2-1
- Bump to 1.9.2

* Thu Feb 20 2020 Johan Kok <johan@fedoraproject.org> - 1.7.3-1
- Bump to 1.7.3

* Mon Feb 17 2020 Sergi Jimenez <tripledes@fedoraproject.org> - 1.7.2-1
- Bump to 1.7.2

* Tue Jan 14 2020 Sergi Jimenez <tripledes@fedoraproject.org> - 1.6.2-1
- Bump to 1.6.2

* Fri Dec 13 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.6.1-1
- Bump to 1.6.1

* Wed Nov  6 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.5.2-1
- Bump to 1.5.2

* Tue Jul  2 2019 Edu Minguez <edu@linux.com> - 1.2.0-1
- Bump to 1.2.0

* Tue Jun 11 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.1.1-1
- Bump to 1.1.1

* Mon Jun  3 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.1.0-1
- Bump to 1.1.0

* Fri May  3 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.0.1-1
- Bump to 1.0.1

* Sun Mar 31 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.0.0-1
- Bump to 1.0.0

* Tue Mar 12 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 0.35.0-1
- Bump to 0.35.0

* Tue Mar  5 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 0.34.1-1
- Bump to 0.34.1

* Mon Jan 21 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 0.33.1-1
- Bump to 0.33.1

* Sun Jan 13 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 0.32.0-1
- Bump to 0.32.0

* Wed Dec 12 2018 Sergi Jimenez <tripledes@fedoraproject.org> - 0.31.0-2
- Depend on docker-machine-driver-kvm2, as v1 is being deprecated.

* Wed Dec 12 2018 Sergi Jimenez <tripledes@fedoraproject.org> - 0.31.0-1
- Initial import
