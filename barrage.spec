Summary:	Kill and destroy as many target as possible in 3 minutes
Summary(pl):	Zniszcz jak najwiêcej wrogów w przeci±gu 3 minut
Name:		barrage
Version:	1.0.1
Release:	3
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/lgames/%{name}-%{version}.tar.gz
# Source0-md5:	5b0dd010c9c0be1e5391631c8a2844ee
Source1:	%{name}.png
Patch0:		%{name}-desktop.patch
URL:		http://lgames.sourceforge.net/index.php?project=Barrage
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Barrage is a rather violent action game with the objective to kill and
destroy as many targets as possible within 3 minutes. The player
controls a gun that may either fire small or large grenades at
soldiers, jeeps and tanks. It is a very simple gameplay though it is
not that easy to get high scores.

%description -l pl
Barrage jest do¶æ brutaln± gr± akcji, której celem jest zniszczenie
jak najwiêkszej ilo¶ci przeciwników w przeci±gu 3 minut. Gracz steruje
broni±, która mo¿e wystrzeliwaæ zarówno ma³e jak i du¿e granaty w
kierunku ¿o³nierzy, jeepów i czo³gów. Zasady s± proste, lecz osi±gniêcie 
dobrych wyników jest trudnym zadaniem.

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README AUTHORS
%attr(2755,root,games) %{_bindir}/*
%{_datadir}/games/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
