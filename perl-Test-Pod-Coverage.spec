%define upstream_name	 Test-Pod-Coverage
%define upstream_version 1.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Check for POD coverage in your Perl modules
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl(Pod::Coverage)
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This Perl module checks for POD coverage in files for your distribution.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.80.0-4mdv2012.0
+ Revision: 765740
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.80.0-3
+ Revision: 764251
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.80.0-2
+ Revision: 667355
- mass rebuild

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 1.80.0-1mdv2011.0
+ Revision: 408087
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.08-4mdv2009.0
+ Revision: 224139
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.08-3mdv2008.1
+ Revision: 180602
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Apr 25 2007 Olivier Thauvin <nanardon@mandriva.org> 1.08-2mdv2008.0
+ Revision: 18032
- rebuild


* Thu Jan 26 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.08-1mdk
- 1.08

* Wed Feb 09 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.06-2mdk
- Fix BuildRequires.

* Thu Dec 09 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.06-1mdk
- Initial MDK release.

