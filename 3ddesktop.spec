Summary:	An OpenGL virtual desktop switching program
Summary(pl):	Program prze³±czaj±cy wirtualne pulpity wykorzystuj±cy OpenGL
Name:		3ddesktop
Version:	0.2.7
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/desk3d/%{name}-%{version}.tar.gz
# Source0-md5:	2b9204195101d17eaca02f0c5286ed15
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
3D-Desktop is a KDE OpenGL program for switching virtual desktops in
a seamless 3-dimensional manner. The current desktop is mapped into a
fullscreen 3D environment where you may choose other screens. Several
different visualization modes are available. The transition from
working desktop to fullscreen 3D environment is seamless. In other
words when the pager activates you see your current desktop appear to
zoom out to a point in space where you can see your other virtual
desktops allowing you to select another. The best way to understand is
to try it out and get the full effect!

%description -l pl
3D-Desktop jest programem KDE wykorzystuj±cym OpenGL, który prze³±cza
wirtualne pulpity w p³ynny, trójwymiarowy sposób. Aktualny pulpit jest
mapowany na pe³noekranowe ¶rodowisko 3D, gdzie mo¿esz wybraæ inne
ekrany. Dostêpnych jest kilka ró¿nych sposobów wizualizacji.

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
%config(noreplace) %verify(not size md5 mtime) %{_sysconfdir}/*
%{_datadir}/%{name}
