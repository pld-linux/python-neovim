#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		neovim
%define		egg_name	pynvim
Summary:	Python client to neovim
Name:		python-%{module}
Version:	0.4.3
Release:	6
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://github.com/neovim/python-client/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b7370a5b3d2177d2b97ca48695ba1ae3
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
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implements support for Python plugins in nvim

%package -n python3-neovim
Summary:	Python client to neovim
Group:		Libraries/Python

%description -n python3-neovim
Implements support for Python plugins in nvim

%prep
%setup -q -n pynvim-%{version}

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

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/pynvim
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-neovim
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/pynvim
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
