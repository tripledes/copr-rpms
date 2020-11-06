%global srcname s-tui

Name:           %{srcname}
Version:        1.0.2
Release:        1%{?dist}
Summary:        Stress-Terminal UI

License:        GPLv2
URL:            https://pypi.org/project/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-psutil
BuildRequires:  python3-urwid
Requires: stress-ng

%description
Stress-Terminal UI, s-tui, monitors CPU temperature, frequency, power and utilization in a graphical way from the terminal.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files
%doc README.md
%{python3_sitelib}/*
%{_bindir}/%{srcname}

%changelog
* Fri Nov  6 2020 Sergi Jimenez <tripledes@fedoraproject.org> - 1.0.2-1
- Bump to 1.0.2

* Thu Jun 25 2020 Sergi Jimenez <tripledes@fedoraproject.org> - 1.0.1-1
- Initial import
