#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Linux
%define	pnam	Pid
Summary:	Linux::Pid - Get the native PID and the PPID on Linux
Summary(pl):	Linux::Pid - uzyskiwanie natywnych PID i PPID pod Linuksem
Name:		perl-Linux-Pid
Version:	0.02
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Inline-C
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-26
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
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitearch}/%{pdir}/*.pm
%dir %{perl_sitearch}/auto/%{pdir}/%{pnam}
%attr(755,root,root) %{perl_sitearch}/auto/%{pdir}/%{pnam}/*.so
%{_mandir}/man3/*
