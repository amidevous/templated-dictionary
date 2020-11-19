%global srcname templated-dictionary

%if 0%{?rhel} == 7
%global python3_pkgversion 36
%endif

Name:       python-%{srcname}
Version:    1.0
Release:    1%{?dist}
Summary:    Dictionary with Jinja2 expansion

License:    GPLv2+
URL:        https://github.com/xsuchy/templated-dictionary

# Source is created by:
# git clone https://github.com/xsuchy/templated-dictionary && cd templated-dictionary
# tito build --tgz --tag %%name-%%version-%%release
Source0:    %name-%version.tar.gz

BuildArch: noarch

BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
Requires:      python%{python3_pkgversion}-jinja2

%global _description\
Dictionary where __getitem__() is run through Jinja2 template.

%description %_description


%package -n python3-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-%{srcname} %_description


%prep
%setup -q


%build
version="%version" %py3_build

%install
version=%version %py3_install


%files -n python3-%{srcname}
%license LICENSE
%{python3_sitelib}/*



%changelog
* Wed Nov 18 2020 Miroslav Suchý <msuchy@redhat.com> 1.0-1
- new package
