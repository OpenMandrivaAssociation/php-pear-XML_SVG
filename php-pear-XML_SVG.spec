%define	_class	XML
%define	_subclass	SVG
%define	modname	%{_class}_%{_subclass}

Summary:	XML_SVG API
Name:		php-pear-%{modname}
Version:	1.1.0
Release:	5
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/XML_SVG/
Source0:	http://download.pear.php.net/package/XML_SVG-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
This package provides and object-oriented way of building SVG
documents.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{_datadir}/pear/data/%{modname}
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{modname}.xml

