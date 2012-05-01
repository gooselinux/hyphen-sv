Name: hyphen-sv
Summary: Swedish hyphenation rules
Version: 1.00.1
Release: 5%{?dist}
Source: http://extensions.services.openoffice.org/files/1966/4/hyph_sv_SE.oxt
Group: Applications/Text
URL: http://extensions.services.openoffice.org/node/1968
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+ or LGPLv2+
BuildArch: noarch
Requires: hyphen

%description
Swedish hyphenation rules.

%prep
%setup -q -c -n hyphen-sv

%build
chmod -x *
for i in README_sv_SE.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_sv_SE.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen
sv_SE_aliases="sv_FI"
for lang in $sv_SE_aliases; do
        ln -s hyph_sv_SE.dic hyph_$lang.dic
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_sv_SE.txt
%{_datadir}/hyphen/*

%changelog
* Thu Jun 17 2010 Caolán McNamara <caolanm@redhat.com> - 1.00.1-5
- Resolves: rhbz#604010 clarify licence

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.00.1-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 1.00.1-3
- tidy spec

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Caolan McNamara <caolanm@redhat.com> - 1.00.1-1
- latest version

* Fri Nov 23 2007 Caolan McNamara <caolanm@redhat.com> - 0.20030814-1
- initial version
