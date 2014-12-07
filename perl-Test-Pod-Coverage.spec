%define modname	Test-Pod-Coverage
%define modver	1.08

Summary:	Check for POD coverage in your Perl modules
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	14
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl(Pod::Coverage)
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl-devel

%description
This Perl module checks for POD coverage in files for your distribution.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Test/Pod/*
%{_mandir}/man3/*

