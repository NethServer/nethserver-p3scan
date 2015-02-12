Name:		nethserver-p3scan
Version:        1.0.0
Release:        1
Summary:	NethServer p3scan
Group:		Networking/Daemons
License:	GPLv2
URL:		http://www.nethesis.it
Source0:	%{name}-%{version}.tar.gz
BuildArch: 	noarch

BuildRequires:	nethserver-devtools
Requires:	nethserver-firewall-base
Requires:	spamassassin
Requires:	nethserver-antivirus
Requires:	p3scan

%description
p3scan (pop3 proxy) add-on for NethServer

%prep
%setup

%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -not -name '*.orig' -print  | cpio -dump $RPM_BUILD_ROOT)
%{genfilelist} $RPM_BUILD_ROOT > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%pre

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)

%changelog
* Fri Oct 03 2014 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1.ns6
- First release - Feature #2865

