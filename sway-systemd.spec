Summary:	Systemd integration for Sway session
Name:		sway-systemd
Version:	0.4.1
Release:	1
License:	MIT
URL:		https://github.com/alebastr/sway-systemd
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	meson
BuildRequires:	pkgconfig(systemd)
BuildRequires:	systemd-macros
Requires:	sway
Requires:	systemd
Recommends:	dbus-tools

%description
%{summary}.

The goal of this project is to provide a minimal set of configuration files
and scripts required for running Sway in a systemd environment.

This includes several areas of integration:
 - Propagate required variables to the systemd user session environment.
 - Define sway-session.target for starting user services.

%prep
%autosetup -p1

%build
%meson \
    -Dautoload-configs=all

%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/sway/config.d/
%{_libexecdir}/sway-systemd/
%{_userunitdir}/sway-session.target
%{_userunitdir}/sway-session-shutdown.target
%{_userunitdir}/sway-xdg-autostart.target

