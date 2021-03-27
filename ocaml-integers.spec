#
# Conditional build:
%bcond_without	ocaml_opt	# skip building native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

%if %{without ocaml_opt}
%define		_enable_debug_packages	0
%endif

Summary:	Various signed and unsigned integer types for OCaml
Name:		ocaml-integers
Version:	0.4.0
Release:	1
License:	MIT
Source0:	https://github.com/ocamllabs/ocaml-integers/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c1492352e6525048790508c57aad93c3
URL:		https://github.com/ocamllabs/ocaml-integers
BuildRequires:	ocaml >= 4.02
BuildRequires:	ocaml-dune
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ocaml-integers library provides a number of 8-, 16-, 32- and
64-bit signed and unsigned integer types, together with aliases such
as `long` and `size_t` whose sizes depend on the host platform.

%package        devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}

%description    devel
This package contains libraries and signature files for developing
applications that use %{name}.

%prep
%setup -q

%build
dune build %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
dune install --destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md README.md
%dir %{_libdir}/ocaml/integers
%dir %{_libdir}/ocaml/integers/top
%{_libdir}/ocaml/integers/META
%{_libdir}/ocaml/integers/*.cma
%{_libdir}/ocaml/integers/*.cmi
%{_libdir}/ocaml/integers/top/*.cma
%{_libdir}/ocaml/integers/top/*.cmi
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/integers/*.cmxs
%endif
%{_libdir}/ocaml/stublibs/dllintegers_stubs.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/integers/dune-package
%{_libdir}/ocaml/integers/opam
%{_libdir}/ocaml/integers/*.a
%if %{with ocaml_opt}
%{_libdir}/ocaml/integers/*.cmx
%{_libdir}/ocaml/integers/*.cmxa
%endif
%{_libdir}/ocaml/integers/*.cmt
%{_libdir}/ocaml/integers/*.cmti
%{_libdir}/ocaml/integers/*.h
%{_libdir}/ocaml/integers/*.mli
%{_libdir}/ocaml/integers/top/*.cmt
%{_libdir}/ocaml/integers/top/*.cmti
%{_libdir}/ocaml/integers/top/*.mli
