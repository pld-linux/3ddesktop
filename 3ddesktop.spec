Summary:	An OpenGL virtual desktop switching program
Summary(pl.UTF-8):   Program przełączający wirtualne pulpity wykorzystujący OpenGL
Name:		3ddesktop
Version:	0.2.9
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/desk3d/%{name}-%{version}.tar.gz
# Source0-md5:	da1e8b0d2c210a441676bbf663e694ee
URL:		http://desk3d.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glut-devel
BuildRequires:	gtk+-devel
BuildRequires:	imlib2-devel
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRequires:	libstdc++-devel
BuildRequires:	qt-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
3D-Desktop is a KDE OpenGL program for switching virtual desktops in a
seamless 3-dimensional manner. The current desktop is mapped into a
fullscreen 3D environment where you may choose other screens. Several
different visualization modes are available. The transition from
working desktop to fullscreen 3D environment is seamless. In other
words when the pager activates you see your current desktop appear to
zoom out to a point in space where you can see your other virtual
desktops allowing you to select another. The best way to understand is
to try it out and get the full effect!

%description -l pl.UTF-8
3D-Desktop jest programem KDE wykorzystującym OpenGL, który przełącza
wirtualne pulpity w płynny, trójwymiarowy sposób. Aktualny pulpit jest
mapowany na pełnoekranowe środowisko 3D, gdzie możesz wybrać inne
ekrany. Dostępnych jest kilka różnych sposobów wizualizacji.

%prep
%setup -q

%build
cp -f /usr/share/automake/missing .
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--with-kde-includes="/usr/include" \
	--with-qt-includes="/usr/include/qt"
%{__make} OPT=""

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%{_datadir}/%{name}
%{_mandir}/man1/3ddesk*
