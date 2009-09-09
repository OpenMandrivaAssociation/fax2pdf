Summary:	A Fax to PDF converter
Name:		fax2pdf
Version:	0.1.3
Release:	%mkrel 7
License:	GPL
Group:		Communications
URL:		https://sourceforge.net/projects/fax2pdf/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		fax2pdf-patch01
Requires:	hylafax-server
BuildRequires:	tiff-devel
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
This package contains the fax2pdf utility to convert Fax Files
into PDF files.

%prep

%setup -q
%patch0 -p1

%build

make CFLAGS="%{optflags}" fax2pdf

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -m0755 fax2pdf %{buildroot}%{_bindir}/

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog MANIFEST
%{_bindir}/fax2pdf


