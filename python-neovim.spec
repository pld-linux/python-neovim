#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		neovim
%define		egg_name	neovim
Summary:	Python client to neovim
Name:		python-%{module}
Version:	0.1.9
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://github.com/neovim/python-client/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a79bca20b8e4876e059a4190e68e881b
URL:		https://github.com/neovim/python-client
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-greenlet
Requires:	python-msgpack
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implements support for Python plugins in nvim

%package -n python3-neovim
Summary:	Python client to neovim
Group:		Libraries/Python
Requires:	python3-greenlet
Requires:	python3-msgpack

%description -n python3-neovim
Implements support for Python plugins in nvim

%prep
%setup -q -n python-client-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-neovim
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
