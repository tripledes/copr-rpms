Name:          minishift
Version:       1.32.0
Release:       1%{?dist}
Summary:       Run OpenShift locally

Group:         Development Tools
URL:           https://github.com/minishift/minishift
License:       ASL 2.0
Source0:       https://github.com/minishift/minishift/releases/download/v%{version}/minishift-%{version}-linux-amd64.tgz
ExclusiveArch: x86_64
Requires:      docker-machine-driver-kvm

%description
Minishift is a tool that helps you run OpenShift locally by running a
single-node OpenShift cluster inside a VM. You can try out OpenShift
or develop with it, day-to-day, on your local host.

%build

%prep
%setup -q -n %{name}-%{version}-linux-amd64

%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
* Tue Mar  5 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.32.0-1
- Bump version 1.32.0

* Sun Feb 10 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.31.0-1
- Bump version 1.31.0

* Mon Jan 21 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.30.0-1
- Bump version 1.30.0

* Sun Jan 13 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.29.0-1
- Bump version 1.29.0

* Tue Dec 11 2018 Sergi Jimenez <tripledes@fedoraproject.org> - 1.28.1-1
- Initial import
