Summary: PsycologIcal Security System
Summary(es): Sistema psicol�gico de seguridad
Name: piss
Packager: Ismael Olea
%define version 1.0
%define release 0
Version: %{version}
Release: %{release}
Copyright: GPL 
Distribution: Planeta Olea
# Source: http://piss.olea.org/piss-%{version}.tar.gz
Source: piss-%{version}.tar.gz
Group: Applications/System
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-root
Requires(prereq): e2fsprogs fileutils
Prefix: /

%description
The PsychologIcal Security System (P.I.S.S.) is the last barrier and
desperate security system for the lazy trusted system administrator.

It's based on a deep investigation process trying to find the most
generalized psychological system intrusion profile.

The protection scheme is included in English ,  Spanish and Galician.

%description -l es
El sistema de seguridad psicol�gico (siglas PISS en ingl�s) es la
�ltima protecci�n de seguridad para el administrador de redes
confiado y perezoso.

Ha sido dise�ado a partir de una profunda investigaci�n en los
perfiles m�s gen�ricos de intrusi�n en sistemas.

Se incluyen mecanismos de protecci�n tanto en lengua inglesa como
espa�ola y gallega.
 

%prep
%setup
%build
%install
mkdir -p $RPM_BUILD_ROOT/
cp README.src $RPM_BUILD_ROOT/README


%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS  ChangeLog  COPYING  HACKING  INSTALL  NEWS THANKS  TODO readme.html piss.png olea_click.gif
/README

%post 
chmod a-rwx /README
chattr +i /README

%preun 
chattr -i /README


%changelog
* Tue Dec 02 2002 Juan Manuel Sende
- Modificacion de la descripcion, idioma gallego.
* Tue Sep 10 2002 Ismael Olea
- Creaci�n del paquete y liberaci�n inicial.
