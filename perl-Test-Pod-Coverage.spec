%define module	Test-Pod-Coverage
%define name	perl-%{module}
%define version	1.08
%define	release	%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Check for POD coverage in your Perl modules
License:	GPL or Artistic
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl(Pod::Coverage)
BuildRequires:	perl(Test::Builder::Tester)

%description
This Perl module checks for POD coverage in files for your distribution.

%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Test/Pod/*
%{_mandir}/*/*

