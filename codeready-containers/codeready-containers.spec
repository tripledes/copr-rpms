Name:          crc
Version:       1.0.0.rc.0
Release:       1%{?dist}
Summary:       This project is focused on bringing a minimal OpenShift 4.0 or newer cluster to your local laptop or desktop computer.

%define        _version 1.0.0
%define        _status rc.0

Group:         Development Tools
URL:           https://github.com/code-ready/crc
License:       ASL 2.0
Source0:       https://mirror.openshift.com/pub/openshift-v4/clients/%{name}/%{_version}-%{_status}/%{name}-linux-amd64.tar.xz
ExclusiveArch: x86_64
Requires:      libvirt, qemu-kvm

%description
This project is focused on bringing a minimal OpenShift 4.0 or newer cluster to your local laptop or desktop computer.

%build

%prep
%setup -q -n %{name}-%{_version}-%{_status}-linux-amd64

%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Thu Oct 10 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.0.0-rc.0
- Bumped to 1.0.0-rc.0

* Wed Jul 31 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 0.89.0.alpha-1
- Bumped to 0.89.0-alpha

* Tue Jul  9 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 0.88.0-1
- Bumped to 0.88.0

* Mon May 27 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 0.86.0-2
- Handle archive properly

* Mon May 27 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 0.86.0-1
- Initial import
