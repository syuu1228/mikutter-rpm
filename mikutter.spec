Name:		mikutter
Version:	3.6.5
Release:	1%{?dist}
Summary:	plugin-extensible Twitter client

License:	MIT
URL:		http://mikutter.hachune.net/
Source0:	mikutter.%{version}.tar.gz
Source1:	mikutter.desktop
Source2:	mikutter.sh
Source3:	v1.json
Source4:	v2.json

Requires:	ruby rubygem-gtk2 rubygem-moneta rubygem-nokogiri rubygem-httpclient rubygem-totoridipjp rubygem-unf_ext rubygem-idn libnotify alsa-utils

%global debug_package %{nil}

%description
 Mikutter is a multi-pane Twitter client with several advanced
 features:
  * different tweet views (flat list, threaded list, searches);
  * user profile and activity views;
  * lists of followers and followings (friends);
  * plugin extensibility.

%prep
%setup -q -n mikutter
%{__install} -m644 %{SOURCE1} .
%{__install} -m644 %{SOURCE2} .
%{__install} -m644 %{SOURCE3} .
%{__install} -m644 %{SOURCE4} .

%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datarootdir}/mikutter
mkdir -p $RPM_BUILD_ROOT%{_datarootdir}/mikutter/config
mkdir -p $RPM_BUILD_ROOT%{_datarootdir}/applications
mkdir -p $RPM_BUILD_ROOT%{_bindir}

rm -vrf vendor/idn.* vendor/unf_ext.* vendor/unf_ext
cp -pr core devel plugin tasks vendor data mikutter.rb $RPM_BUILD_ROOT%{_datarootdir}/mikutter
install -m644 mikutter.desktop $RPM_BUILD_ROOT%{_datarootdir}/applications
install -m755 mikutter.sh $RPM_BUILD_ROOT%{_bindir}/mikutter
install -m644 *.json $RPM_BUILD_ROOT%{_datarootdir}/mikutter/config

%files
%{_datarootdir}/mikutter/mikutter.rb
%{_datarootdir}/mikutter/core/*
%{_datarootdir}/mikutter/devel/*
%{_datarootdir}/mikutter/plugin/*
%{_datarootdir}/mikutter/tasks/*
%{_datarootdir}/mikutter/vendor/*
%{_datarootdir}/mikutter/data/*
%{_datarootdir}/mikutter/config/*
%{_datarootdir}/applications/mikutter.desktop
%{_bindir}/mikutter

%license LICENSE
%doc README



%changelog
* Fri Apr 06 2018 Takuya ASADA <syuu@dokukino.com> - 3.6.5-1
- Version up to 3.6.5

* Sun Feb 14 2018 Takuya ASADA <syuu@dokukino.com> - 3.6.3-1
- Version up to 3.6.3

* Sun Jan 28 2018 Takuya ASADA <syuu@dokukino.com> - 3.6.1-1
- Version up to 3.6.1

* Sat Apr 01 2017 Takuya ASADA <syuu@dokukino.com> - 3.5.6-1
- Version up to 3.5.6

* Sat Apr 01 2017 Takuya ASADA <syuu@dokukino.com> - 3.5.5-1
- Initial package
