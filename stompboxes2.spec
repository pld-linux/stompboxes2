#
# TODO:
# - add desktop file.
#
Summary:	Real-time audio effects processor
Summary(pl.UTF-8):	Procesor efektów dźwiękowych czasu rzeczywistego
Name:		stompboxes2
Version:	0.3
Release:	1
License:	GPL v2
Vendor:		Hector Urtubia <urtubia@mrbook.org>
Group:		X11/Applications/Sound
Source0:	http://mrbook.org/stompboxes/%{name}-%{version}.tar.gz
# Source0-md5:	050a90e09952749412f8ac0b07938071
Patch0:		%{name}-Makefile.in.patch
URL:		http://mrbook.org/stompboxes/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Real-time audio effects processor.

%description -l pl.UTF-8
Procesor efektów dźwiękowych czasu rzeczywistego.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/plugins,%{_pixmapsdir}/%{name}}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install plugins/*.so $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins
install pixmaps/*.xpm $RPM_BUILD_ROOT%{_datadir}/%{name}/pixmaps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/QUICKSTART ChangeLog LOG README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%attr(755,root,root) %{_datadir}/%{name}/plugins/*
%{_datadir}/%{name}/pixmaps
