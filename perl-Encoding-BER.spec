#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Encoding
%define		pnam	BER
Summary:	Encoding::BER - Perl module for encoding/decoding data using ASN.1 Basic Encoding Rules (BER)
Name:		perl-Encoding-BER
Version:	1.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://cpan.metacpan.org/authors/id/J/JA/JAW/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e4fd46dee1ea315b67712215f9d73766
URL:		http://search.cpan.org/dist/Encoding-BER/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.636
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unlike many other BER encoder/decoders, this module uses tree
structured data as the interface to/from the encoder/decoder.

The decoder does not require any form of template or description of
the data to be decoded. Given arbitrary BER encoded data, the decoder
produces a tree shaped perl data structure from it.

The encoder takes a perl data structure and produces a BER encoding
from it.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{?with_tests:%{__make} test}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%dir %{perl_vendorlib}/Encoding/BER
%{perl_vendorlib}/Encoding/BER/*.pm
%{perl_vendorlib}/Encoding/BER.pm
%{_mandir}/man3/Encoding::BER*.3pm*
