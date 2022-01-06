#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-entrypoints
Version  : 0.3
Release  : 41
URL      : https://files.pythonhosted.org/packages/b4/ef/063484f1f9ba3081e920ec9972c96664e2edb9fdc3d8669b0e3b8fc0ad7c/entrypoints-0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/b4/ef/063484f1f9ba3081e920ec9972c96664e2edb9fdc3d8669b0e3b8fc0ad7c/entrypoints-0.3.tar.gz
Summary  : Discover and load entry points from installed packages.
Group    : Development/Tools
License  : MIT
Requires: pypi-entrypoints-license = %{version}-%{release}
Requires: pypi-entrypoints-python = %{version}-%{release}
Requires: pypi-entrypoints-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: entrypoints
Provides: entrypoints-python
Provides: entrypoints-python3
BuildRequires : pypi(flit)
BuildRequires : python3-dev

%description
Entry points are a way for Python packages to advertise objects with some
common interface. The most common examples are ``console_scripts`` entry points,
which define shell commands by identifying a Python function to run.

%package license
Summary: license components for the pypi-entrypoints package.
Group: Default

%description license
license components for the pypi-entrypoints package.


%package python
Summary: python components for the pypi-entrypoints package.
Group: Default
Requires: pypi-entrypoints-python3 = %{version}-%{release}

%description python
python components for the pypi-entrypoints package.


%package python3
Summary: python3 components for the pypi-entrypoints package.
Group: Default
Requires: python3-core
Provides: pypi(entrypoints)

%description python3
python3 components for the pypi-entrypoints package.


%prep
%setup -q -n entrypoints-0.3
cd %{_builddir}/entrypoints-0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641434382
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-entrypoints
cp %{_builddir}/entrypoints-0.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-entrypoints/619bfe6da95b23329e5a9c5b4acdab24920c03bd
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-entrypoints/619bfe6da95b23329e5a9c5b4acdab24920c03bd

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
