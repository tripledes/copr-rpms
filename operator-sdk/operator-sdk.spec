Name:          operator-sdk
Version:       0.17.1
Release:       1%{?dist}
Summary:       SDK for building Kubernetes applications. Provides high level APIs, useful abstractions, and project scaffolding.

Group:         Development Tools
URL:           https://github.com/operator-framework/operator-sdk
License:       ASL 2.0
Source0:       https://github.com/operator-framework/operator-sdk/releases/download/v%{version}/%{name}-v%{version}-x86_64-linux-gnu
ExclusiveArch: x86_64

%description
This project is a component of the Operator Framework, an open source toolkit to manage Kubernetes native applications,
called Operators, in an effective, automated, and scalable way. 

%build

%prep
%setup -q -T -c

%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Thu May 28 2020 Sergi Jimenez <tripledes@fedoraproject.org> - 0.17.1-1
- Bump to 0.17.1

* Wed Nov  6 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 0.12.0-1
- Bump to 0.12.0

* Mon May 27 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 0.8.1-2
- Fix dependencies

* Mon May 27 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 0.8.1-1
- Initial import
