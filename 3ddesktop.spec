Summary:	An OpenGL virtual desktop switching program
Summary(pl):	Program przełączający virtualne desktopy w OpenGL
Name:		3ddesktop
Version:	0.2.0
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.systemtoolbox.com/bard/3ddesktop/dl/%{name}-%{version}.tar.gz
URL:		http://www.systemtoolbox.com/bard/3ddesktop/
BuildRequires:	OpenGL-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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

%prep
%setup -q

%build
aclocal
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
