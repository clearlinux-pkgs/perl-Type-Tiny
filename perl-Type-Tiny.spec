#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Type-Tiny
Version  : 1.004002
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Type-Tiny-1.004002.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Type-Tiny-1.004002.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtype-tiny-perl/libtype-tiny-perl_1.002001-1.debian.tar.xz
Summary  : 'tiny, yet Moo(se)-compatible type constraint'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Type-Tiny-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Exporter::Tiny)

%description
NAME
Type::Tiny::Manual - an overview of Type::Tiny
SYNOPSIS
Type::Tiny is a small class for writing type constraints, inspired by
Moose's type constraint API. It has only one non-core dependency (and even
that is simply a module that was previously distributed as part of
Type::Tiny but has since been spun off), and can be used with Moose, Mouse
and Moo (or none of the above).

%package dev
Summary: dev components for the perl-Type-Tiny package.
Group: Development
Provides: perl-Type-Tiny-devel = %{version}-%{release}

%description dev
dev components for the perl-Type-Tiny package.


%package license
Summary: license components for the perl-Type-Tiny package.
Group: Default

%description license
license components for the perl-Type-Tiny package.


%prep
%setup -q -n Type-Tiny-1.004002
cd ..
%setup -q -T -D -n Type-Tiny-1.004002 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Type-Tiny-1.004002/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Type-Tiny
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Type-Tiny/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Type-Tiny/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/Devel/TypeTiny/Perl56Compat.pm
/usr/lib/perl5/vendor_perl/5.26.1/Devel/TypeTiny/Perl58Compat.pm
/usr/lib/perl5/vendor_perl/5.26.1/Error/TypeTiny.pm
/usr/lib/perl5/vendor_perl/5.26.1/Error/TypeTiny/Assertion.pm
/usr/lib/perl5/vendor_perl/5.26.1/Error/TypeTiny/Compilation.pm
/usr/lib/perl5/vendor_perl/5.26.1/Error/TypeTiny/WrongNumberOfParameters.pm
/usr/lib/perl5/vendor_perl/5.26.1/Eval/TypeTiny.pm
/usr/lib/perl5/vendor_perl/5.26.1/Reply/Plugin/TypeTiny.pm
/usr/lib/perl5/vendor_perl/5.26.1/Test/TypeTiny.pm
/usr/lib/perl5/vendor_perl/5.26.1/Type/CONTRIBUTING.pod
/usr/lib/perl5/vendor_perl/5.26.1/Type/Coercion.pm
/usr/lib/perl5/vendor_perl/5.26.1/Type/Coercion/FromMoose.pm
/usr/lib/perl5/vendor_perl/5.26.1/Type/Coercion/Union.pm
/usr/lib/perl5/vendor_perl/5.26.1/Type/Library.pm
/usr/lib/perl5/vendor_perl/5.26.1/Type/Params.pm
/usr/lib/perl5/vendor_perl/5.26.1/Type/Parser.pm
/usr/lib/perl5/vendor_perl/5.26.1/Type/Registry.pm
/usr/lib/perl5/vendor_perl/5.26.1/Type/Tiny.pm
/usr/lib/perl5/vendor_perl/5.26.1/Type/Tiny/Class.pm
/usr/lib/perl5/vendor_perl/5.26.1/Type/Tiny/Duck.pm
/usr/lib/perl5/vendor_perl/5.26.1/Type/Tiny/Enum.pm
/usr/lib/perl5/vendor_perl/5.26.1/Type/Tiny/Intersection.pm
/usr/lib/perl5/vendor_perl/5.26.1/Type/Tiny/Manual.pod
/usr/lib/perl5/vendor_perl/5.26.1/Type/Tiny/Manual/Coercions.pod
/usr/lib/perl5/vendor_perl/5.26.1/Type/Tiny/Manual/Libraries.pod
/usr/lib/perl5/vendor_perl/5.26.1/Type/Tiny/Manual/Optimization.pod
/usr/lib/perl5/vendor_perl/5.26.1/Type/Tiny/Manual/Params.pod
/usr/lib/perl5/vendor_perl/5.26.1/Type/Tiny/Manual/Policies.pod
/usr/lib/perl5/vendor_perl/5.26.1/Type/Tiny/Manual/UsingWithMoo.pod
/usr/lib/perl5/vendor_perl/5.26.1/Type/Tiny/Manual/UsingWithMoose.pod
/usr/lib/perl5/vendor_perl/5.26.1/Type/Tiny/Manual/UsingWithMouse.pod
/usr/lib/perl5/vendor_perl/5.26.1/Type/Tiny/Manual/UsingWithOther.pod
/usr/lib/perl5/vendor_perl/5.26.1/Type/Tiny/Role.pm
/usr/lib/perl5/vendor_perl/5.26.1/Type/Tiny/Union.pm
/usr/lib/perl5/vendor_perl/5.26.1/Type/Tiny/_HalfOp.pm
/usr/lib/perl5/vendor_perl/5.26.1/Type/Utils.pm
/usr/lib/perl5/vendor_perl/5.26.1/Types/Common/Numeric.pm
/usr/lib/perl5/vendor_perl/5.26.1/Types/Common/String.pm
/usr/lib/perl5/vendor_perl/5.26.1/Types/Standard.pm
/usr/lib/perl5/vendor_perl/5.26.1/Types/Standard/ArrayRef.pm
/usr/lib/perl5/vendor_perl/5.26.1/Types/Standard/CycleTuple.pm
/usr/lib/perl5/vendor_perl/5.26.1/Types/Standard/Dict.pm
/usr/lib/perl5/vendor_perl/5.26.1/Types/Standard/HashRef.pm
/usr/lib/perl5/vendor_perl/5.26.1/Types/Standard/Map.pm
/usr/lib/perl5/vendor_perl/5.26.1/Types/Standard/ScalarRef.pm
/usr/lib/perl5/vendor_perl/5.26.1/Types/Standard/StrMatch.pm
/usr/lib/perl5/vendor_perl/5.26.1/Types/Standard/Tied.pm
/usr/lib/perl5/vendor_perl/5.26.1/Types/Standard/Tuple.pm
/usr/lib/perl5/vendor_perl/5.26.1/Types/TypeTiny.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Devel::TypeTiny::Perl56Compat.3
/usr/share/man/man3/Devel::TypeTiny::Perl58Compat.3
/usr/share/man/man3/Error::TypeTiny.3
/usr/share/man/man3/Error::TypeTiny::Assertion.3
/usr/share/man/man3/Error::TypeTiny::Compilation.3
/usr/share/man/man3/Error::TypeTiny::WrongNumberOfParameters.3
/usr/share/man/man3/Eval::TypeTiny.3
/usr/share/man/man3/Reply::Plugin::TypeTiny.3
/usr/share/man/man3/Test::TypeTiny.3
/usr/share/man/man3/Type::CONTRIBUTING.3
/usr/share/man/man3/Type::Coercion.3
/usr/share/man/man3/Type::Coercion::FromMoose.3
/usr/share/man/man3/Type::Coercion::Union.3
/usr/share/man/man3/Type::Library.3
/usr/share/man/man3/Type::Params.3
/usr/share/man/man3/Type::Parser.3
/usr/share/man/man3/Type::Registry.3
/usr/share/man/man3/Type::Tiny.3
/usr/share/man/man3/Type::Tiny::Class.3
/usr/share/man/man3/Type::Tiny::Duck.3
/usr/share/man/man3/Type::Tiny::Enum.3
/usr/share/man/man3/Type::Tiny::Intersection.3
/usr/share/man/man3/Type::Tiny::Manual.3
/usr/share/man/man3/Type::Tiny::Manual::Coercions.3
/usr/share/man/man3/Type::Tiny::Manual::Libraries.3
/usr/share/man/man3/Type::Tiny::Manual::Optimization.3
/usr/share/man/man3/Type::Tiny::Manual::Params.3
/usr/share/man/man3/Type::Tiny::Manual::Policies.3
/usr/share/man/man3/Type::Tiny::Manual::UsingWithMoo.3
/usr/share/man/man3/Type::Tiny::Manual::UsingWithMoose.3
/usr/share/man/man3/Type::Tiny::Manual::UsingWithMouse.3
/usr/share/man/man3/Type::Tiny::Manual::UsingWithOther.3
/usr/share/man/man3/Type::Tiny::Role.3
/usr/share/man/man3/Type::Tiny::Union.3
/usr/share/man/man3/Type::Tiny::_HalfOp.3
/usr/share/man/man3/Type::Utils.3
/usr/share/man/man3/Types::Common::Numeric.3
/usr/share/man/man3/Types::Common::String.3
/usr/share/man/man3/Types::Standard.3
/usr/share/man/man3/Types::Standard::ArrayRef.3
/usr/share/man/man3/Types::Standard::CycleTuple.3
/usr/share/man/man3/Types::Standard::Dict.3
/usr/share/man/man3/Types::Standard::HashRef.3
/usr/share/man/man3/Types::Standard::Map.3
/usr/share/man/man3/Types::Standard::ScalarRef.3
/usr/share/man/man3/Types::Standard::StrMatch.3
/usr/share/man/man3/Types::Standard::Tied.3
/usr/share/man/man3/Types::Standard::Tuple.3
/usr/share/man/man3/Types::TypeTiny.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Type-Tiny/LICENSE
/usr/share/package-licenses/perl-Type-Tiny/deblicense_copyright
