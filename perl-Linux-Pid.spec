#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Linux
%define	pnam	Pid
Summary:	Linux::Pid - get the native PID and the PPID on Linux
Summary(pl):	Linux::Pid - uzyskiwanie natywnych PID i PPID pod Linuksem
Name:		perl-Linux-Pid
Version:	0.02
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	af1d6dee6ee94cc8c1847172501b468e
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Inline-C
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux::Pid gets the native PID and the PPID on Linux. It's useful with
multithreaded programs. Linux's C library returns different values of
the PID and the PPID from different threads. This module forces Perl
to call the underlying C functions getpid() and getppid().

%description -l pl
Linux::Pid odczytuje natywne PID i PPID pod Linuksem. Jest przydatny w
programach wielow±tkowych. Linuksowa biblioteka C zwraca ró¿ne
warto¶ci PID i PPID dla ró¿nych w±tków. Ten modu³ zmusza Perla do
wywo³ania funkcji C getpid() i getppid().

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/%{pdir}/*.pm
%dir %{perl_vendorarch}/auto/%{pdir}/%{pnam}
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/%{pnam}/*.so
%{_mandir}/man3/*
