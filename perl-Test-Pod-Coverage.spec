%define modname	Test-Pod-Coverage

# Avoid nasty build dependency loop
%define dont_gprintify 1

Summary:	Check for POD coverage in your Perl modules
Name:		perl-%{modname}
Version:	1.10
Release:	10
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Test::Pod::Coverage
Source0:	http://search.cpan.org/CPAN/authors/id/N/NE/NEILB/Test-Pod-Coverage-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Pod::Coverage)
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl-devel

%description
This Perl module checks for POD coverage in files for your distribution.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%make_install
find %{buildroot} -name perllocal.pod -o -name .packlist |xargs rm -f

%files
%doc Changes
%{perl_vendorlib}/Test/Pod/*
%{_mandir}/man3/*

