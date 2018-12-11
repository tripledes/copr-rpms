Name:          docker-machine-driver-kvm
Version:       0.10.0
Release:       1%{?dist}
Summary:       KVM driver for docker-machine

Group:         Development Tools
URL:           https://github.com/dhiltgen/docker-machine-kvm
License:       ASL 2.0
Source0:       https://github.com/dhiltgen/docker-machine-kvm/releases/download/v%{version}/docker-machine-driver-kvm-centos7
ExclusiveArch: x86_64
Requires:      libvirt, qemu-kvm

%description
This driver leverages the new plugin architecture being developed for
Docker Machine.

%build

%prep
%setup -q -T -c

%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Tue Dec 11 2018 Sergi Jimenez <tripledes@fedoraproject.org> - 0.10.0-1
- Initial import
