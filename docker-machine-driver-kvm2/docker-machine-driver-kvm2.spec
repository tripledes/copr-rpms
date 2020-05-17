Name:          docker-machine-driver-kvm2
Version:       1.10.1
Release:       1%{?dist}
Summary:       docker-machine KVM driver v2 for minikube

Group:         Development Tools
URL:           https://github.com/kubernetes/minikube
License:       ASL 2.0
Source0:       https://github.com/kubernetes/minikube/releases/download/v%{version}/%{name}
ExclusiveArch: x86_64
Requires:      libvirt, qemu-kvm

%description
This driver leverages the new plugin architecture being developed for
Docker Machine. Maintained specifically for minikube.

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

* Thu Feb 20 2020 Sergi Jimenez <tripledes@fedoraproject.org> - 1.7.3-1
- Bump to 1.7.3

* Mon Feb 17 2020 Sergi Jimenez <tripledes@fedoraproject.org> - 1.7.2-1
- Bump to 1.7.2

* Tue Jan 14 2020 Sergi Jimenez <tripledes@fedoraproject.org> - 1.6.2-1
- Bump to 1.6.2

* Fri Dec 13 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.6.1-1
- Bump to 1.6.1

* Wed Nov  6 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.5.2-2
- Fix changelog

* Wed Nov  6 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.5.2-1
- Bump to 1.5.2

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

* Wed Dec 12 2018 Sergi Jimenez <tripledes@fedoraproject.org> - 0.31.0-1
- Initial import
