Name:          urxvt-font-size
Version:       1.3
Release:       1%{?dist}
Summary:       Perl extension for rxvt-unicode that allows changing the font size on the fly with keyboard shortcuts.
Group:         User Interface/X
URL:           https://github.com/majutsushi/urxvt-font-size
License:       MIT
Source0:       https://github.com/majutsushi/%{name}/archive/v%{version}.tar.gz
BuildArch:     noarch
Requires:      rxvt-unicode

%description
This is a perl extension for rxvt-unicode that allows changing the font size on
the fly with keyboard shortcuts. It has the following features:

* Supports both xft and X11 fonts; X11 fonts work in both full form and as
  aliases.
* Supports all four font settings: font, boldFont, italicFont and
  boldItalicFont and changes them in accordance with the base font (the first
  one from font).
* Can apply the font change globally for the whole server, so that new
  terminals will inherit the same size, and even save it to ~/.Xresources
  to be able to survive a reboot.
* Should work even with complicated font setups like the example
  in the urxvt man-page.

%build

%prep
%setup -q v%{version}

%install
mkdir -p %{buildroot}/%{_libdir}/urxvt/perl
%{__install} -m 644 font-size %{buildroot}/%{_libdir}/urxvt/perl/font-size


%files
%license LICENSE
%doc README.markdown
%{_libdir}/urxvt/perl/font-size

%changelog
* Sun Jan 13 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.3-1
- Initial import
