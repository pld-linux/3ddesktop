Summary:	An OpenGL virtual desktop switching program
Summary(pl):	Program prze��czaj�cy wirtualne pulpity wykorzystuj�cy OpenGL
Name:		3ddesktop
Version:	0.2.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://prdownloads.sourceforge.net/desk3d/%{name}-%{version}.tar.gz
URL:		http://desk3d.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glut-devel
BuildRequires:	gtk+-devel
BuildRequires:	imlib2-devel
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRequires:	libstdc++-devel
BuildRequires:	OpenGL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
3D-Desktop is a GNOME OpenGL program for switching virtual desktops in
a seamless 3-dimensional manner. The current desktop is mapped into a
fullscreen 3D environment where you may choose other screens. Several
different visualization modes are available. The transition from
working desktop to fullscreen 3D environment is seamless. In other
words when the pager activates you see your current desktop appear to
zoom out to a point in space where you can see your other virtual
desktops allowing you to select another. The best way to understand is
to try it out and get the full effect!

%description -l pl
3D-Desktop jest programem GNOME wykorzystuj�cym OpenGL, kt�ry prze��cza
wirtualne pulpity w p�ynny, tr�jwymiarowy spos�b. Aktualny pulpit jest
mapowany na pe�noekranowe �rodowisko 3D, gdzie mo�esz wybra� inne
ekrany. Dost�pnych jest kilka r�nych sposob�w wizualizacji.

%prep
%setup -q

%build
cp -f /usr/share/automake/missing .
%{__aclocal}
%{__autoconf}
CPPFLAGS="-I/usr/X11R6/include" ; export CPPFLAGS
%configure \
	--with-kde-includes="/usr/X11R6/include" \
	--with-qt-includes="/usr/X11R6/include/qt"
%{__make} OPT=""

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not size md5 mtime) %{_sysconfdir}/*
%{_datadir}/%{name}
