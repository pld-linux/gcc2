%define		rname		gcc
%define 	rver		2.95.3
%define		snap		20010823
%define		STDC_VERSION	2.10.0
%define		STDC_RELEASE	5
Summary:	GNU Compiler Collection
Summary(pl):	Kolekcja kompilator�w GNU
Name:		%{rname}2
Version:	2.95.4
Release:	0.%{snap}.5
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
BuildRequires:	bison
BuildRequires:	texinfo
BuildRequires:	automake
Requires:	binutils >= 2.9.1.0.25
Requires:	cpp2 = %{version}
%ifarch alpha
Conflicts:	glibc-devel < 2.2.5
%endif
URL:		http://gcc.gnu.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A compiler aimed at integrating all the optimizations and features
necessary for a high-performance and stable development environment.

%description -l pl
Kompilator, posiadaj�cy du�e mo�liwo�ci optymalizacyjne niezb�dne do
wyprodukowania szybkiego i stablinego kodu wynikowego.

%package c++
Summary:	C++ support for gcc
Summary(fr):	Support C++ pour le compilateur gcc
Summary(pl):	Wspomaganie C++ dla kompilatora gcc
Summary(tr):	gcc i�in C++ deste�i
Group:		Development/Languages
Obsoletes:	egcc-c++
Obsoletes:	egcs-c++
Requires:	%{name} = %{version}

%description c++
This package adds C++ support to the GNU C compiler. It includes
support for most of the current C++ specification, including templates
and exception handling. It does not include a standard C++ library,
which is available separately.

%description c++ -l de
Dieses Paket enth�lt die C++-Unterst�tzung f�r den GNU-C-Compiler. Es
unterst�tzt die aktuelle C++-Spezifikation, inkl. Templates und
Ausnahmeverarbeitung. Eine C++-Standard-Library ist nicht enthalten -
sie ist getrennt erh�ltlich.

%description c++ -l fr
Ce package ajoute un support C++ au compilateur c GNU. Il comprend un
support pour la plupart des sp�cifications actuelles de C++, dont les
mod�les et la gestion des exceptions. Il ne comprend pas une
biblioth�que C++ standard, qui est disponible s�par�ment.

%description c++ -l pl
Programy z tego pakietu zapewniaj� wsparcie dla C++ do gcc. Posiada
wspomaganie dla du�ej ilo�ci obecnych specyfikacji C++, nie posiada
natomiast standardowych bibliotek C++, kt�re s� w oddzielnym pakiecie.

%description c++ -l tr
Bu paket, GNU C derleyicisine C++ deste�i ekler. 'Template'ler ve
ayk�r� durum i�leme gibi �o�u g�ncel C++ tan�mlar�na uyar. Standart
C++ kitapl��� bu pakette yer almaz.

%package objc
Summary:	Objective C support for gcc
Summary(de):	Objektive C-Unterst�tzung f�r gcc
Summary(fr):	Gestion d'Objective C pour gcc
Summary(pl):	Wspomaganie obiektowego C dla kompilatora gcc
Summary(tr):	gcc i�in Objective C deste�i
Group:		Development/Languages
Obsoletes:	egcc-objc
Obsoletes:	egcs-objc
Requires:	%{name} = %{version}

%description objc
This package adds Objective C support to the GNU C compiler. Objective
C is a object oriented derivative of the C language, mainly used on
systems running NeXTSTEP. This package does not include the standard
objective C object library.

%description objc -l de
Dieses Paket erg�nzt den GNU-C-Compiler durch Objective-C-Support.
Objective C ist ein objektorientiertes Derivat von C, das zur
Hauptsache auf Systemen mit NeXTSTEP zum Einsatz kommt. Die
Standard-Objective-C-Objekt-Library ist nicht Teil des Pakets.

%description objc -l fr
Ce package ajoute un support Objective C au compilateur C GNU.
L'Objective C est un langage orient� objetd�riv� du langage C,
principalement utilis� sur les syst�mes NeXTSTEP. Ce package n'inclue
pas la biblioth�que Objective C standard.

%description objc -l pl
Ten pakiet jest wsparciem obiektowego C dla kompilatora gcc. W
pakiecie nie ma jeszcze bibliotek C-obj.

%description objc -l tr
Bu paket, GNU C derleyicisine Objective C deste�i ekler. Objective C,
C dilinin nesne y�nelik bir t�revidir ve NeXTSTEP alt�nda �al��an
sistemlerde yayg�n olarak kullan�l�r. Standart Objective C nesne
kitapl��� bu pakette yer almaz.

%package g77
Summary:	Fortran 77 support for gcc
Summary(pl):	Wspomaganie Fortran 77 dla gcc
Group:		Development/Languages
Obsoletes:	egcs-g77

%description g77
This apckage adds support for compiling Fortran 77 programs with the
GNU compiler.

%description g77 -l pl
Ten pakiet jest wsparciem Fortran 77 dla kompilatora gcc. Jest
potrzebny do kompilowania program�w pisanych w j�zyku Fortran 77.

%package chill
Summary:	CHILL support for gcc
Summary(pl):	Wspomoganie CHILL dla gcc
Group:		Development/Languages
Requires:	%{name} = %{version}

%description chill
This package adds support for compiling CHILL programs with the GNU
compiler.

Chill is the "CCITT High-Level Language", where CCITT is the old name
for what is now ITU, the International Telecommunications Union. It is
is language in the Modula2 family, and targets many of the same
applications as Ada (especially large embedded systems). Chill was
never used much in the United States, but is still being used in
Europe, Brazil, Korea, and other places.

%description chill -l pl
Ten pakiet dodaje do gcc mo�liwo�� kompilowania program�w w j�zyku
CHILL.

%package java
Summary:	Java support for gcc
Summary(pl):	Wspomoganie Java dla gcc
Group:		Development/Languages
Requires:	%{name} = %{version}
Requires:	libgcj2 >= 2.95.1

%description java
This package adds experimental support for compiling Java(tm) programs
and bytecode into native code. To use this you will also need the
libgcj package.

%description java -l pl
Ten pakiet dodaje do gcc (eksperymentaln�) mo�liwo�� kompilowania
program�w w Javie(tm) i bytecode do kodu procesora. Wymaga pakietu
libgcj.

%package -n libstdc++2
Summary:	GNU c++ library
Summary(pl):	Biblioteki GNU C++
Group:		Libraries
Version:	%{STDC_VERSION}
Release:	%{STDC_RELEASE}
Obsoletes:	libg++

%description -n libstdc++2
This is the GNU implementation of the standard C++ libraries, along
with additional GNU tools. This package includes the shared libraries
necessary to run C++ applications.

%description -n libstdc++2 -l de
Dies ist die GNU-Implementierung der Standard-C++-Libraries mit
weiteren GNU-Tools. Dieses Paket enth�lt die zum Ausf�hren von
C++-Anwendungen erforderlichen gemeinsam genutzten Libraries.

%description -n libstdc++2 -l fr
Ceci est l'impl�mentation GNU des librairies C++ standard, ainsi que
des outils GNU suppl�mentaires. Ce package comprend les librairies
partag�es n�cessaires � l'ex�cution d'application C++.

%description -n libstdc++2 -l pl
Pakiet ten zawiera biblioteki b�d�ce implementacj� standardowych
bibliotek C++. Znajduj� si� w nim biblioteki dynamiczne niezb�dne do
uruchomienia aplikacji napisanych w C++.

%description -n libstdc++2 -l tr
Bu paket, standart C++ kitapl�klar�n�n GNU ger�eklemesidir ve C++
uygulamalar�n�n ko�turulmas� i�in gerekli kitapl�klar� i�erir.

%package -n libstdc++2-devel
Summary:	Header files and libraries for C++ development
Summary(de):	Header-Dateien und Libraries zur Entwicklung mit C++
Summary(fr):	Fichiers d'en-t�te et biblitoth�ques pour d�velopper en C++
Summary(pl):	Pliki nag��wkowe do programowania z u�yciem bibliotek C++
Summary(tr):	C++ ile program geli�tirmek i�in gerekli dosyalar
Group:		Development/Libraries
Version:	%{STDC_VERSION}
Release:	%{STDC_RELEASE}
Requires:	libstdc++2 = %{STDC_VERSION}
Requires:	%{name}-c++
Obsoletes:	libg++-devel

%description -n libstdc++2-devel
This is the GNU implementation of the standard C++ libraries. This
package includes the header files and libraries needed for C++
development.

%description -n libstdc++2-devel -l pl
Pakiet ten zawiera biblioteki b�d�ce implementacj� standardowych
bibliotek C++. Znajduj� si� w nim pliki nag��wkowe wykorzystywane przy
programowaniu w j�zyku C++.

%package -n libstdc++2-static
Summary:	Static c++ standard library
Summary(pl):	Biblioteka statyczna c++
Group:		Development/Libraries
Version:	%{STDC_VERSION}
Release:	%{STDC_RELEASE}
Requires:	libstdc++2-devel = %{STDC_VERSION}

%description -n libstdc++2-static
Static c++ standard library.

%description -n libstdc++2-static -l pl
Biblioteka statyczna C++.

%package -n cpp2
Summary:	The C Pre Processor
Summary(pl):	Preprocesor C
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

%description -n cpp2 -l pl
Preprocesor C jest "makro procesorem" kt�ry jest automatycznie u�ywany
przez kompilator C do obr�bki kompilowanego programu przed w�a�ciw�
kompilacj�. Jest on nazywany makroprocesorem, poniewa� umo�liwia
definiowanie i rozwijanie makr umo�liwiaj�cych skracanie d�ugich
konstrukcji w j�zyku C.

Preprocesor C umo�liwia wykonywanie czterech r�nych typ�w operacji:

- Do��czanie plik�w (np. nag��wkowych). Wstawia pliki w miejscu
  deklaracji polecenia do��czenia innego pliku.
- Rozwijanie makr. Mo�na definiowa� "makra" nadaj�c im identyfikatory,
  kt�rych p�niejsze u�ycie powoduje podczas rozwijania podmienienie
  identyfikatora deklarowan� wcze�niej warto�ci�.
- Kompilacja warunkowa. W zale�no�ci od obecno�ci symboli i dyrektyw w
  �rodowisku preprocesora s� w��czane warunkowo, b�d� nie, pewne
  fragmenty obrabianego strumienia tekst�w.
- Kontrola linii �r�d�a. Niezale�nie od tego jakim przeobra�eniom
  podlega wynikowy strumie� danych w wyniku rozwijania makr i do��czania
  s� zapami�tywane informacje o tym, kt�rej linii pliku �r�d�owego
  odpowiada fragment pliku wynikowego.

%prep
%setup -q -n %{rname}-%{rver}
%patch50 -p1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p0
%patch6 -p0
%patch7 -p0
%patch8 -p0
%patch9 -p0
%patch10 -p0
%patch11 -p1
%ifarch m68k
%patch12 -p0
%endif
%ifarch sparc sparc32
%patch13 -p0
%patch14 -p0
%endif
%ifarch ppc
%patch15 -p0
%patch16 -p0
%endif
%ifarch alpha
%patch17 -p1
%endif
%patch18 -p0
%patch19 -p0
#%patch20 -p0
%patch21 -p1
%patch22 -p1

%build
(cd gcc; autoconf; cp -f /usr/share/automake/config.* .)
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
mv jcf-dump jcf-dump2
mv jv-scan jv-scan2
mv gcjh gcjh2

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post g77
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun g77
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post chill
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun chill
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post -n cpp2
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun -n cpp2
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post   -p /sbin/ldconfig -n libstdc++2
%postun -p /sbin/ldconfig -n libstdc++2

%clean
rm -rf $RPM_BUILD_ROOT

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

%files java
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/gcj2
%attr(755,root,root) %{_bindir}/gcjh2
%attr(755,root,root) %{_bindir}/jcf-dump2
%attr(755,root,root) %{_bindir}/jv-scan2

%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/jc1
%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/jvgenmain

%files -n libstdc++2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libstdc++.so.*.*.*

%files -n libstdc++2-devel
%defattr(644,root,root,755)
%{_includedir}/g++
%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/libstdc++.so

%files -n libstdc++2-static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/libstdc++.a

%files -n cpp2
%defattr(644,root,root,755)
%attr(755,root,root) /lib/cpp2
%attr(755,root,root) %{_bindir}/cpp2
%attr(755,root,root) %{_libdir}/gcc-lib/%{_target_cpu}*/*/cpp0
