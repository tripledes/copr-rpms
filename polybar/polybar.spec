Name:           polybar
Version:        3.3.1
Release:        3%{?dist}
Summary:        A fast and easy-to-use status bar
License:        MIT
URL:            https://github.com/jaagr/polybar
Source:         https://github.com/jaagr/polybar/releases/download/%{version}/%{name}-%{version}.tar
patch0:         matches-uninitialized-cairo-context.hpp.diff
patch1:         window-gcc9.diff
BuildRequires:  python2
BuildRequires:  clang >= 3.4
BuildRequires:  cmake >= 3.1
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-proto)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-ewmh)
# optional
BuildRequires:  pkgconfig(xcb-xrm)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-sync)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libmpdclient)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  i3-ipc
BuildRequires:  wireless-tools-devel


%description
A fast and easy-to-use status bar for tilling WM

%prep
%setup -q -n %{name}
mkdir build

%patch0 -p1
%patch1 -p1

%build
cd build
%{cmake} ..
%{make_build}

%install
cd build
%{make_install}

%files
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions
%docdir %{_datadir}/doc/%{name}
%{_datadir}/doc/%{name}
%{_bindir}/%{name}
%{_bindir}/%{name}-msg
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/zsh/site-functions/_%{name}_msg

%changelog
* Sat May  4 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 3.3.1-3
- Patches for f30

* Sat Apr 27 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 3.3.1-2
- Spec improvements

* Fri Apr  5 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 3.3.1-1
- Initial import
