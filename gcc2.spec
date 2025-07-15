%define		rname		gcc
%define 	rver		2.95.3
%define		snap		20010823
%define		STDC_VERSION	2.10.0
%define		STDC_RELEASE	5
Summary:	GNU Compiler Collection
Summary(pl.UTF-8):	Kolekcja kompilatorów GNU
Name:		%{rname}2
Version:	2.95.4
Release:	0.%{snap}.6
License:	GPL
Group:		Development/Languages
Source0:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{rver}/%{rname}-%{rver}.tar.bz2
# Source0-md5:	87ee083a830683e2aaa57463940a0c3c
Patch0:		%{name}-info.patch
Patch1:		%{name}-pld-linux.patch
Patch2:		%{name}-libstdc++.patch
Patch3:		%{name}-bootstrap.patch
Patch4:		%{name}-cpp-macro-doc.patch
Patch5:		%{name}-default-arch.patch
Patch6:		%{name}-libstdc++-out-of-mem.patch
Patch7:		%{name}-libstdc++-wstring.patch
Patch8:		%{name}-libstdc++-bastring.patch
Patch9:		%{name}-manpage.patch
Patch10:	%{name}-cpp-dos-newlines.patch
Patch11:	%{name}-gpc.patch
Patch12:	%{name}-m68k-pic.patch
Patch13:	%{name}-sparc32-rfi.patch
Patch14:	%{name}-builtin-apply.patch
Patch15:	%{name}-ppc-ice.patch
Patch16:	%{name}-ppc-descriptions.patch
Patch17:	%{name}-alpha-complex-float.patch
Patch18:	%{name}-gcj-vs-iconv.patch
Patch19:	%{name}-libobjc.patch
#Patch20:	%{name}-pointer-arith.patch
Patch21:	%{name}-suffix.patch
Patch22:	%{name}-athlon-option.patch
Patch50:	gcc-%{rver}-%{snap}.patch.bz2
# Patch50-md5:	83f4163aa5b8492d27cbfc9eb8ea419c
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	texinfo
Requires:	binutils
Requires:	cpp2 = %{version}
%ifarch alpha
Conflicts:	glibc-devel < 2.2.5
%endif
URL:		http://gcc.gnu.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A compiler aimed at integrating all the optimizations and features
necessary for a high-performance and stable development environment.

%description -l pl.UTF-8
Kompilator, posiadający duże możliwości optymalizacyjne niezbędne do
wyprodukowania szybkiego i stabilnego kodu wynikowego.

%package c++
Summary:	C++ support for gcc
Summary(fr.UTF-8):	Support C++ pour le compilateur gcc
Summary(pl.UTF-8):	Wspomaganie C++ dla kompilatora gcc
Summary(tr.UTF-8):	gcc için C++ desteği
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Obsoletes:	egcc-c++
Obsoletes:	egcs-c++

%description c++
This package adds C++ support to the GNU C compiler. It includes
support for most of the current C++ specification, including templates
and exception handling. It does not include a standard C++ library,
which is available separately.

%description c++ -l de.UTF-8
Dieses Paket enthält die C++-Unterstützung für den GNU-C-Compiler. Es
unterstützt die aktuelle C++-Spezifikation, inkl. Templates und
Ausnahmeverarbeitung. Eine C++-Standard-Library ist nicht enthalten -
sie ist getrennt erhältlich.

%description c++ -l fr.UTF-8
Ce package ajoute un support C++ au compilateur c GNU. Il comprend un
support pour la plupart des spécifications actuelles de C++, dont les
modéles et la gestion des exceptions. Il ne comprend pas une
bibliothéque C++ standard, qui est disponible séparément.

%description c++ -l pl.UTF-8
Programy z tego pakietu zapewniają wsparcie dla C++ do gcc. Posiada
wspomaganie dla dużej ilości obecnych specyfikacji C++, nie posiada
natomiast standardowych bibliotek C++, które są w oddzielnym pakiecie.

%description c++ -l tr.UTF-8
Bu paket, GNU C derleyicisine C++ desteği ekler. 'Template'ler ve
aykırı durum işleme gibi çoğu güncel C++ tanımlarına uyar. Standart
C++ kitaplığı bu pakette yer almaz.

%package objc
Summary:	Objective C support for gcc
Summary(de.UTF-8):	Objektive C-Unterstützung für gcc
Summary(fr.UTF-8):	Gestion d'Objective C pour gcc
Summary(pl.UTF-8):	Wspomaganie obiektowego C dla kompilatora gcc
Summary(tr.UTF-8):	gcc için Objective C desteği
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Obsoletes:	egcc-objc
Obsoletes:	egcs-objc

%description objc
This package adds Objective C support to the GNU C compiler. Objective
C is a object oriented derivative of the C language, mainly used on
systems running NeXTSTEP. This package does not include the standard
objective C object library.

%description objc -l de.UTF-8
Dieses Paket ergänzt den GNU-C-Compiler durch Objective-C-Support.
Objective C ist ein objektorientiertes Derivat von C, das zur
Hauptsache auf Systemen mit NeXTSTEP zum Einsatz kommt. Die
Standard-Objective-C-Objekt-Library ist nicht Teil des Pakets.

%description objc -l fr.UTF-8
Ce package ajoute un support Objective C au compilateur C GNU.
L'Objective C est un langage orienté objetdérivé du langage C,
principalement utilisé sur les systèmes NeXTSTEP. Ce package n'inclue
pas la bibliothéque Objective C standard.

%description objc -l pl.UTF-8
Ten pakiet jest wsparciem obiektowego C dla kompilatora gcc. W
pakiecie nie ma jeszcze bibliotek C-obj.

%description objc -l tr.UTF-8
Bu paket, GNU C derleyicisine Objective C desteği ekler. Objective C,
C dilinin nesne yönelik bir türevidir ve NeXTSTEP altında çalışan
sistemlerde yaygın olarak kullanılır. Standart Objective C nesne
kitaplığı bu pakette yer almaz.

%package g77
Summary:	Fortran 77 support for gcc
Summary(pl.UTF-8):	Wspomaganie Fortran 77 dla gcc
Group:		Development/Languages
Obsoletes:	egcs-g77

%description g77
This apckage adds support for compiling Fortran 77 programs with the
GNU compiler.

%description g77 -l pl.UTF-8
Ten pakiet jest wsparciem Fortran 77 dla kompilatora gcc. Jest
potrzebny do kompilowania programów pisanych w języku Fortran 77.

%package chill
Summary:	CHILL support for gcc
Summary(pl.UTF-8):	Wspomoganie CHILL dla gcc
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description chill
This package adds support for compiling CHILL programs with the GNU
compiler.

Chill is the "CCITT High-Level Language", where CCITT is the old name
for what is now ITU, the International Telecommunications Union. It is
is language in the Modula2 family, and targets many of the same
applications as Ada (especially large embedded systems). Chill was
never used much in the United States, but is still being used in
Europe, Brazil, Korea, and other places.

%description chill -l pl.UTF-8
Ten pakiet dodaje do gcc możliwość kompilowania programów w języku
CHILL.

%package -n libstdc++2
Summary:	GNU c++ library
Summary(pl.UTF-8):	Biblioteki GNU C++
Version:	%{STDC_VERSION}
Release:	%{STDC_RELEASE}
Group:		Libraries
Obsoletes:	libg++

%description -n libstdc++2
This is the GNU implementation of the standard C++ libraries, along
with additional GNU tools. This package includes the shared libraries
necessary to run C++ applications.

%description -n libstdc++2 -l de.UTF-8
Dies ist die GNU-Implementierung der Standard-C++-Libraries mit
weiteren GNU-Tools. Dieses Paket enthält die zum Ausführen von
C++-Anwendungen erforderlichen gemeinsam genutzten Libraries.

%description -n libstdc++2 -l fr.UTF-8
Ceci est l'implémentation GNU des librairies C++ standard, ainsi que
des outils GNU supplémentaires. Ce package comprend les librairies
partagées nécessaires à l'exécution d'application C++.

%description -n libstdc++2 -l pl.UTF-8
Pakiet ten zawiera biblioteki będące implementacją standardowych
bibliotek C++. Znajdują się w nim biblioteki dynamiczne niezbędne do
uruchomienia aplikacji napisanych w C++.

%description -n libstdc++2 -l tr.UTF-8
Bu paket, standart C++ kitaplıklarının GNU gerçeklemesidir ve C++
uygulamalarının koşturulması için gerekli kitaplıkları içerir.

%package -n libstdc++2-devel
Summary:	Header files and libraries for C++ development
Summary(de.UTF-8):	Header-Dateien und Libraries zur Entwicklung mit C++
Summary(fr.UTF-8):	Fichiers d'en-tête et biblitothèques pour développer en C++
Summary(pl.UTF-8):	Pliki nagłówkowe do programowania z użyciem bibliotek C++
Summary(tr.UTF-8):	C++ ile program geliştirmek için gerekli dosyalar
Version:	%{STDC_VERSION}
Release:	%{STDC_RELEASE}
Group:		Development/Libraries
Requires:	%{name}-c++
Requires:	libstdc++2 = %{STDC_VERSION}
Obsoletes:	libg++-devel

%description -n libstdc++2-devel
This is the GNU implementation of the standard C++ libraries. This
package includes the header files and libraries needed for C++
development.

%description -n libstdc++2-devel -l pl.UTF-8
Pakiet ten zawiera biblioteki będące implementacją standardowych
bibliotek C++. Znajdują się w nim pliki nagłówkowe wykorzystywane przy
programowaniu w języku C++.

%package -n libstdc++2-static
Summary:	Static c++ standard library
Summary(pl.UTF-8):	Biblioteka statyczna c++
Version:	%{STDC_VERSION}
Release:	%{STDC_RELEASE}
Group:		Development/Libraries
Requires:	libstdc++2-devel = %{STDC_VERSION}

%description -n libstdc++2-static
Static c++ standard library.

%description -n libstdc++2-static -l pl.UTF-8
Biblioteka statyczna C++.

%package -n cpp2
Summary:	The C Pre Processor
Summary(pl.UTF-8):	Preprocesor C
Group:		Development/Languages
Obsoletes:	egcs-cpp

%description -n cpp2
The C preprocessor is a "macro processor" that is used automatically
by the C compiler to transform your program before actual compilation.
It is called a macro processor because it allows you to define
"macros", which are brief abbreviations for longer constructs.

The C preprocessor provides four separate facilities that you can use
as you see fit:

- Inclusion of header files. These are files of declarations that can
  be substituted into your program.
- Macro expansion. You can define "macros", which are abbreviations
  for arbitrary fragments of C code, and then the C preprocessor will
  replace the macros with their definitions throughout the program.
- Conditional compilation. Using special preprocessing directives, you
  can include or exclude parts of the program according to various
  conditions.
- Line control. If you use a program to combine or rearrange source
  files into an intermediate file which is then compiled, you can use
  line control to inform the compiler of where each source line
  originally came from.

%description -n cpp2 -l pl.UTF-8
Preprocesor C jest "makro procesorem" który jest automatycznie używany
przez kompilator C do obróbki kompilowanego programu przed właściwą
kompilacją. Jest on nazywany makroprocesorem, ponieważ umożliwia
definiowanie i rozwijanie makr umożliwiających skracanie długich
konstrukcji w języku C.

Preprocesor C umożliwia wykonywanie czterech różnych typów operacji:

- Dołączanie plików (np. nagłówkowych). Wstawia pliki w miejscu
  deklaracji polecenia dołączenia innego pliku.
- Rozwijanie makr. Można definiować "makra" nadając im identyfikatory,
  których późniejsze użycie powoduje podczas rozwijania podmienienie
  identyfikatora deklarowaną wcześniej wartością.
- Kompilacja warunkowa. W zależności od obecności symboli i dyrektyw w
  środowisku preprocesora są włączane warunkowo, bądź nie, pewne
  fragmenty obrabianego strumienia tekstów.
- Kontrola linii źródła. Niezależnie od tego jakim przeobrażeniom
  podlega wynikowy strumień danych w wyniku rozwijania makr i dołączania
  są zapamiętywane informacje o tym, której linii pliku źródłowego
  odpowiada fragment pliku wynikowego.

%prep
%setup -q -n %{rname}-%{rver}
%patch -P50 -p1
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p0
%patch -P5 -p0
%patch -P6 -p0
%patch -P7 -p0
%patch -P8 -p0
%patch -P9 -p0
%patch -P10 -p0
%patch -P11 -p1
%ifarch m68k
%patch -P12 -p0
%endif
%ifarch sparc sparc32
%patch -P13 -p0
%patch -P14 -p0
%endif
%ifarch ppc
%patch -P15 -p0
%patch -P16 -p0
%endif
%ifarch alpha
%patch -P17 -p1
%endif
%patch -P18 -p0
%patch -P19 -p0
#%%patch20 -p0
%patch -P21 -p1
%patch -P22 -p1

%build
rm -rf gcc/java
cd gcc
%{__autoconf}
cp -f /usr/share/automake/config.* .
cd ..
cp -f /usr/share/automake/config.* .
rm -rf obj-%{_target_platform}
install -d obj-%{_target_platform} && cd obj-%{_target_platform}

CC="%{__cc}"; export CC
CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcflags}" \
TEXCONFIG=false ../configure \
	--host=%{_target_platform} \
	--build=%{_target_platform} \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--enable-shared \
%ifnarch sparc sparc64
	--enable-threads=posix \
	--enable-haifa \
%endif
	--with-gnu-as \
	--with-gnu-ld \
	--with-gxx-include-dir="\$\{prefix\}/include/g++" \
	--disable-nls \
	--program-suffix="2"

PATH=$PATH:/sbin:%{_sbindir}
touch  ../gcc/c-gperf.h

cd ..
%{__make} -C obj-%{_target_platform} bootstrap \
	LDFLAGS_FOR_TARGET="%{rpmldflags}" \
	mandir=%{_mandir} \
	infodir=%{_infodir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib,%{_datadir}}

cd obj-%{_target_platform}
PATH=$PATH:/sbin:%{_sbindir}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	infodir=$RPM_BUILD_ROOT%{_infodir}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	infodir=$RPM_BUILD_ROOT%{_infodir} -C texinfo

ln -sf gcc2 $RPM_BUILD_ROOT%{_bindir}/cc2

ln -sf g772 $RPM_BUILD_ROOT%{_bindir}/f772

mv $RPM_BUILD_ROOT%{_libdir}/libstdc++.a \
	$RPM_BUILD_ROOT%{_libdir}/gcc-lib/%{_target_cpu}*/*/

ln -sf %{_bindir}/cpp2 $RPM_BUILD_ROOT/lib/cpp2

cd $RPM_BUILD_ROOT%{_bindir}
mv chill chill2
mv %{_target_platform}-gcc %{_target_platform}-gcc2

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post g77	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun g77	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post chill	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun chill	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post -n cpp2	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun -n cpp2	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post   -p /sbin/ldconfig -n libstdc++2
%postun -p /sbin/ldconfig -n libstdc++2

%files
%defattr(644,root,root,755)
%doc READ* ChangeLog

%dir %{_libdir}/gcc-lib
%dir %{_libdir}/gcc-lib/%{_target_cpu}*
%dir %{_libdir}/gcc-lib/%{_target_cpu}*/*
%dir %{_libdir}/gcc-lib/%{_target_cpu}*/*/include

%attr(755,root,root) %{_bindir}/%{_target_cpu}*-gcc2
%attr(755,root,root) %{_bindir}/gcc2
%attr(755,root,root) %{_bindir}/gcov2
%attr(755,root,root) %{_bindir}/protoize2
%attr(755,root,root) %{_bindir}/unprotoize2
%attr(755,root,root) %{_bindir}/cc2

%{_libdir}/gcc-lib/%{_target_cpu}*/*/SYSCALLS.c.X
%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/cc1
%{_libdir}/gcc-lib/%{_target_cpu}*/*/libgcc.a
%{_libdir}/gcc-lib/%{_target_cpu}*/*/lib*.map
%{_libdir}/gcc-lib/%{_target_cpu}*/*/specs

%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/crt*.o
%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/collect2

%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/float.h
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/iso646.h
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/limits.h
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/proto.h
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/stdarg.h
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/stdbool.h
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/stddef.h
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/syslimits.h
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/va-*.h
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/varargs.h

%files c++
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/g++2
%attr(755,root,root) %{_bindir}/c++2
%attr(755,root,root) %{_bindir}/c++filt2
%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/cc1plus

%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/exception
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/new
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/typeinfo
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/new.h

%files objc
%defattr(644,root,root,755)

%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/cc1obj

%{_libdir}/gcc-lib/%{_target_cpu}*/*/libobjc.a
%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/objc

%files g77
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/g772
%attr(755,root,root) %{_bindir}/f772

%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/f771
%{_libdir}/gcc-lib/%{_target_cpu}*/*/libg2c.a

%{_libdir}/gcc-lib/%{_target_cpu}*/*/include/g2c.h

%files chill
%defattr(644,root,root,755)
%doc gcc/ch/chill.brochure

%attr(755,root,root) %{_bindir}/chill2

%{_infodir}/chill*

%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/cc1chill
%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/chill*.o
%{_libdir}/gcc-lib/%{_target_cpu}*/*/libchill.a

%files -n libstdc++2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libstdc++.so.*.*.*

%files -n libstdc++2-devel
%defattr(644,root,root,755)
%{_includedir}/g++
%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/libstdc++.so

%files -n libstdc++2-static
%defattr(644,root,root,755)
%{_libdir}/gcc-lib/%{_target_cpu}*/*/libstdc++.a

%files -n cpp2
%defattr(644,root,root,755)
%attr(755,root,root) /lib/cpp2
%attr(755,root,root) %{_bindir}/cpp2
%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/cpp0
