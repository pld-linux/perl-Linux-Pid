#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Linux
%define		pnam	Pid
Summary:	Linux::Pid - get the native PID and the PPID on Linux
Summary(pl.UTF-8):	Linux::Pid - uzyskiwanie natywnych PID i PPID pod Linuksem
Name:		perl-Linux-Pid
Version:	0.04
Release:	14
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Linux/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	130c4d299f827abf1f2285fddf03fccb
URL:		http://search.cpan.org/dist/Linux-Pid/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Inline-C
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux::Pid gets the native PID and the PPID on Linux. It's useful with
multithreaded programs. Linux's C library returns different values of
the PID and the PPID from different threads. This module forces Perl
to call the underlying C functions getpid() and getppid().

%description -l pl.UTF-8
Linux::Pid odczytuje natywne PID i PPID pod Linuksem. Jest przydatny w
programach wielowątkowych. Linuksowa biblioteka C zwraca różne
wartości PID i PPID dla różnych wątków. Ten moduł zmusza Perla do
wywołania funkcji C getpid() i getppid().

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
