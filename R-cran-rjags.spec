%define		fversion	%(echo %{version} | tr r -)
%define		modulename	rjags
Summary:	Interface to the JAGS MCMC library
Name:		R-cran-%{modulename}
Version:	3r5
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	30609db97b9f93f04fb3aa1ec52783c4
BuildRequires:	mcmc-jags-devel >= 3.2
BuildRequires:	R >= 2.12.0
BuildRequires:	R-cran-coda
Requires:	R-cran-coda
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interface to the JAGS MCMC library.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}
