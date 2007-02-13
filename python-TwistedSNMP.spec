
%define 	module	TwistedSNMP

Summary:	Set of implementations of SNMP protocol for Twisted networking framework
Summary(pl.UTF-8):	Zbiór implementacji protokołu SNMP dla Twisted
Name:		python-%{module}
Version:	0.2.13
Release:	1
License:	BSD-like
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/twistedsnmp/%{module}-%{version}.tar.gz
# Source0-md5:	b82c7d09f64b68b0cb947b359d849f44
Patch0:		%{name}-build-doc.patch
URL:		http://twistedsnmp.sourceforge.net/
BuildRequires:	pydoc
BuildRequires:	python-devel >= 2.2
Requires:	python-Twisted >= 1.3
Requires:	python-pysnmp => 3.0
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TwistedSNMP is a set of SNMP protocol implementations for Python's
Twisted Matrix networking framework using the PySNMP project.

%description -l pl.UTF-8
TwistedSNMP jest zbiorem implementacji protokołu SNMP dla Twisted,
używającym bibliotek z projektu PySNMP.

%package doc
Summary:	Documentation for TwistedSNMP
Summary(pl.UTF-8):	Dokumentacja do TwistedSNMP
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
Offline documentation for TwistedSNMP.

%description doc -l pl.UTF-8
Dokumentacja offline do TwistedSNMP.

%package examples
Summary:	Example programs for TwistedSNMP
Summary(pl.UTF-8):	Programy przykładowe do TwistedSNMP
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for TwistedSNMP.

%description examples -l pl.UTF-8
Ten pakiet zawiera przykładowe programy dla TwistedSNMP.

%package utils
Summary:	Utility scripts for TwistedSNMP
Summary(pl.UTF-8):	Skrypty narzędziowe do TwistedSNMP
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description utils
This package contains utility scripts for TwistedSNMP.

%description utils -l pl.UTF-8
Ten pakiet zawiera skrypty narzędziowe do TwistedSNMP.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{_datadir}/%{module},%{_examplesdir}/%{name}-%{version}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

# Utilities
cp -a utilities/*.py $RPM_BUILD_ROOT%{_datadir}/%{module}

# Examples
cp -a test/*.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a doc/simpleexample.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# Cleanups
rm -f {$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version},$RPM_BUILD_ROOT%{_datadir}/%{module}}/__init__.py
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/twistedsnmp/{utilities,test}

# Documentation
rm -rf build/lib/twistedsnmp/{utilities,test}
cd doc/pydoc
python builddocs.py
rm -f *.py *.pyc .cvsignore

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc license.txt
%dir %{py_sitescriptdir}/twistedsnmp
%{py_sitescriptdir}/twistedsnmp/*.py[oc]

%files doc
%defattr(644,root,root,755)
%doc doc/index.html doc/style doc/pydoc

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files utils
%defattr(644,root,root,755)
%{_datadir}/%{module}
