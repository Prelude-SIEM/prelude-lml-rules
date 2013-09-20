Name:		prelude-lml-rules
Epoch:		1
Version:	1.0.0
Release:	1%{?dist}
Summary:	Prelude LML community ruleset
Group:		System Environment/Daemons
License:	GPLv2+
URL:		http://www.prelude-ids.org/
Source0:	%{name}/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
Requires:	prelude-lml

%description
Rules for Prelude LML contributed by the community.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sysconfdir}/prelude-lml/ruleset
mkdir -p %{buildroot}/%{_bindir}
cp -R $RPM_BUILD_DIR/%{name}-%{version}/ruleset/* %{buildroot}/%{_sysconfdir}/prelude-lml/ruleset/
cp $RPM_BUILD_DIR/%{name}-%{version}/src/%{name}* %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING NEWS README AUTHORS
%{_sysconfdir}/prelude-lml/ruleset
%attr(775,root,root) %{_bindir}/*


%changelog
* Wed Sep 18 2013 Jean-Charles ROGEZ <jean-charles.rogez@c-s.fr> - 1:1.0.0-1
- Initial package
