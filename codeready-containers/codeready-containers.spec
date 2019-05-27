Name:          crc
Version:       0.86.0
Release:       1%{?dist}
Summary:       This project is focused on bringing a minimal OpenShift 4.0 or newer cluster to your local laptop or desktop computer.

Group:         Development Tools
URL:           https://github.com/code-ready/crc
License:       ASL 2.0
Source0:       https://github.com/code-ready/crc/releases/download/%{version}/%{name}-%{version}-linux-amd64.tar.xz
ExclusiveArch: x86_64
Requires:      libvirt, qemu-kvm

%description
This project is focused on bringing a minimal OpenShift 4.0 or newer cluster to your local laptop or desktop computer.

%build

%prep
%setup -q -T -c

%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Mon May 27 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 0.86.0-1
- Initial import
