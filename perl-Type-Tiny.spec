#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Type-Tiny
Version  : 1.016005
Release  : 52
URL      : https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Type-Tiny-1.016005.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Type-Tiny-1.016005.tar.gz
Summary  : 'tiny, yet Moo(se)-compatible type constraint'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Type-Tiny-license = %{version}-%{release}
Requires: perl-Type-Tiny-perl = %{version}-%{release}
Requires: perl(Exporter::Tiny)
Requires: perl(Reply::Plugin)
BuildRequires : buildreq-cpan
BuildRequires : perl(Exporter::Tiny)

%description
NAME
Type::Tiny::Manual - an overview of Type::Tiny
SYNOPSIS
Type::Tiny is a small Perl <http://www.perl.org/> class for writing type
constraints, inspired by Moose's type constraint API and MooseX::Types. It
has only one non-core dependency (and even that is simply a module that
was previously distributed as part of Type::Tiny but has since been spun
off), and can be used with Moose, Mouse, or Moo (or none of the above).

%package dev
Summary: dev components for the perl-Type-Tiny package.
Group: Development
Provides: perl-Type-Tiny-devel = %{version}-%{release}
Requires: perl-Type-Tiny = %{version}-%{release}

%description dev
dev components for the perl-Type-Tiny package.


%package license
Summary: license components for the perl-Type-Tiny package.
Group: Default

%description license
license components for the perl-Type-Tiny package.


%package perl
Summary: perl components for the perl-Type-Tiny package.
Group: Default
Requires: perl-Type-Tiny = %{version}-%{release}

%description perl
perl components for the perl-Type-Tiny package.


%prep
%setup -q -n Type-Tiny-1.016005
cd %{_builddir}/Type-Tiny-1.016005

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Type-Tiny
cp %{_builddir}/Type-Tiny-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Type-Tiny/b288b1bcff3334631a50e17207149b915027c134
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Devel::TypeTiny::Perl56Compat.3
/usr/share/man/man3/Devel::TypeTiny::Perl58Compat.3
/usr/share/man/man3/Error::TypeTiny.3
/usr/share/man/man3/Error::TypeTiny::Assertion.3
/usr/share/man/man3/Error::TypeTiny::Compilation.3
/usr/share/man/man3/Error::TypeTiny::WrongNumberOfParameters.3
/usr/share/man/man3/Eval::TypeTiny.3
/usr/share/man/man3/Eval::TypeTiny::CodeAccumulator.3
/usr/share/man/man3/Reply::Plugin::TypeTiny.3
/usr/share/man/man3/Test::TypeTiny.3
/usr/share/man/man3/Type::Coercion.3
/usr/share/man/man3/Type::Coercion::FromMoose.3
/usr/share/man/man3/Type::Coercion::Union.3
/usr/share/man/man3/Type::Library.3
/usr/share/man/man3/Type::Params.3
/usr/share/man/man3/Type::Parser.3
/usr/share/man/man3/Type::Registry.3
/usr/share/man/man3/Type::Tiny.3
/usr/share/man/man3/Type::Tiny::Class.3
/usr/share/man/man3/Type::Tiny::ConstrainedObject.3
/usr/share/man/man3/Type::Tiny::Duck.3
/usr/share/man/man3/Type::Tiny::Enum.3
/usr/share/man/man3/Type::Tiny::Intersection.3
/usr/share/man/man3/Type::Tiny::Manual.3
/usr/share/man/man3/Type::Tiny::Manual::AllTypes.3
/usr/share/man/man3/Type::Tiny::Manual::Coercions.3
/usr/share/man/man3/Type::Tiny::Manual::Contributing.3
/usr/share/man/man3/Type::Tiny::Manual::Installation.3
/usr/share/man/man3/Type::Tiny::Manual::Libraries.3
/usr/share/man/man3/Type::Tiny::Manual::NonOO.3
/usr/share/man/man3/Type::Tiny::Manual::Optimization.3
/usr/share/man/man3/Type::Tiny::Manual::Params.3
/usr/share/man/man3/Type::Tiny::Manual::Policies.3
/usr/share/man/man3/Type::Tiny::Manual::UsingWithClassTiny.3
/usr/share/man/man3/Type::Tiny::Manual::UsingWithMoo.3
/usr/share/man/man3/Type::Tiny::Manual::UsingWithMoo2.3
/usr/share/man/man3/Type::Tiny::Manual::UsingWithMoo3.3
/usr/share/man/man3/Type::Tiny::Manual::UsingWithMoose.3
/usr/share/man/man3/Type::Tiny::Manual::UsingWithMouse.3
/usr/share/man/man3/Type::Tiny::Manual::UsingWithOther.3
/usr/share/man/man3/Type::Tiny::Manual::UsingWithTestMore.3
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
/usr/share/package-licenses/perl-Type-Tiny/b288b1bcff3334631a50e17207149b915027c134

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
