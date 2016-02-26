Name:      fuel-distupgrade
Version:   1.0
Release:   1%{?dist}~mos1
Summary:   Sripts for upgrade os on fuel master node

Group:     Development/System
License:   Apache
URL:       http://mirantis.com
Source0:   %{name}-%{version}.tar.gz

Requires:  fuel-dockerctl
Requires:  gawk
Requires:  bash
Requires:  e2fsprogs
Requires:  PyYAML
Requires:  createrepo

%description
This package contains a set of helpers for
upgrade os minor version on master node
to current upstream version.
Remember, this script upgrade only _minor_ version.

%prep
%setup -q

%install
%{__mkdir_p} -m 0755 %{buildroot}/%{_datadir}/%{name}/
%{__mkdir_p} -m 0755 %{buildroot}/%{_sbindir}/
%{__mkdir_p} -m 0755 %{buildroot}/%{_defaultdocdir}/%{name}/
%{__mkdir_p} -m 0755 %{buildroot}/%{_sysconfdir}/fuel/

%{__install} -m 0644 -D %{_builddir}/%{name}-%{version}/mos*.whitelist %{buildroot}/%{_datadir}/%{name}/
%{__install} -m 0644 -D %{_builddir}/%{name}-%{version}/functions %{buildroot}/%{_datadir}/%{name}/functions
%{__install} -m 0755 -D %{_builddir}/%{name}-%{version}/fuel-distupgrade %{buildroot}/%{_sbindir}/fuel-distupgrade
%{__install} -m 0644 -D %{_builddir}/%{name}-%{version}/README.md %{buildroot}/%{_defaultdocdir}/%{name}/README.md
%{__install} -m 0644 -D %{_builddir}/%{name}-%{version}/distupgrade.settings %{buildroot}/%{_sysconfdir}/fuel/distupgrade.settings


%files
%{_datadir}/%{name}/functions
%{_datadir}/%{name}/mos*.whitelist
%{_sbindir}/fuel-distupgrade
%{_sysconfdir}/fuel/distupgrade.settings

%doc
%{_defaultdocdir}/%{name}/README.md


%changelog
* Mon Feb 26 2016 Ivan Suzdal <isuzdal@gmail.com> - 1.0-1~mos1
- Initial version
