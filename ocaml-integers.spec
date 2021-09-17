#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

%if %{without ocaml_opt}
%define		_enable_debug_packages	0
%endif

Summary:	Various signed and unsigned integer types for OCaml
Summary(pl.UTF-8):	Różne typy całkowite ze znakiem i bez dla OCamla
Name:		ocaml-integers
Version:	0.5.1
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/ocamllabs/ocaml-integers/releases
Source0:	https://github.com/ocamllabs/ocaml-integers/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	24d629966763b4956edfb7e64d6c5427
URL:		https://github.com/ocamllabs/ocaml-integers
BuildRequires:	ocaml >= 1:4.02
BuildRequires:	ocaml-dune
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ocaml-integers library provides a number of 8-, 16-, 32- and
64-bit signed and unsigned integer types, together with aliases such
as "long" and "size_t" whose sizes depend on the host platform.

%description -l pl.UTF-8
Biblioteka ocaml-integers dostarcza wiele typów całkowitych, 8-, 16-,
32- i 64-bitowych, ze znakiem i bez, oraz aliasy, takie jak "long" czy
"size_t", których rozmiary zależą od platformy.

%package devel
Summary:	Development files for OCaml integers library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki OCamla integers
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
This package contains libraries and signature files for developing
applications that use OCaml integers library.

%description devel -l pl.UTF-8
Ten pakiet zawiera biblioteki i pliki sygnatur do tworzenia aplikacji
wykorzystujących bibliotekę OCamla integers.

%prep
%setup -q

%build
dune build %{?_smp_mflags} --display=verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/integers{,/top}/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/integers

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/integers
%dir %{_libdir}/ocaml/integers/top
%{_libdir}/ocaml/integers/META
%{_libdir}/ocaml/integers/*.cma
%{_libdir}/ocaml/integers/top/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/integers/*.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllintegers_stubs.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/integers/dune-package
%{_libdir}/ocaml/integers/opam
%{_libdir}/ocaml/integers/*.a
%{_libdir}/ocaml/integers/*.cmi
%{_libdir}/ocaml/integers/*.cmt
%{_libdir}/ocaml/integers/*.cmti
%{_libdir}/ocaml/integers/*.h
%{_libdir}/ocaml/integers/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/integers/*.cmx
%{_libdir}/ocaml/integers/*.cmxa
%endif
%{_libdir}/ocaml/integers/top/*.cmi
%{_libdir}/ocaml/integers/top/*.cmt
%{_libdir}/ocaml/integers/top/*.cmti
%{_libdir}/ocaml/integers/top/*.mli
