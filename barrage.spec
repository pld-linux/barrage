Summary:	Kill and destroy as many target as possible in 3 minutes
Summary(pl.UTF-8):	Zniszcz jak najwięcej wrogów w przeciągu 3 minut
Name:		barrage
Version:	1.0.7
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	https://downloads.sourceforge.net/lgames/%{name}-%{version}.tar.gz
# Source0-md5:	0bb7a7033e467c95210852029366df4f
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-icondir.patch
URL:		https://lgames.sourceforge.net/Barrage
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Barrage is a rather violent action game with the objective to kill and
destroy as many targets as possible within 3 minutes. The player
controls a gun that may either fire small or large grenades at
soldiers, jeeps and tanks. It is a very simple gameplay though it is
not that easy to get high scores.

%description -l pl.UTF-8
Barrage jest dość brutalną grą akcji, której celem jest zniszczenie
jak największej ilości przeciwników w przeciągu 3 minut. Gracz steruje
bronią, która może wystrzeliwać zarówno małe jak i duże granaty w
kierunku żołnierzy, jeepów i czołgów. Zasady są proste, lecz
osiągnięcie dobrych wyników jest trudnym zadaniem.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--localstatedir=/var/games
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README
%attr(2755,root,games) %{_bindir}/barrage
%{_datadir}/barrage
%attr(664,root,games) /var/games/barrage.hscr
%{_desktopdir}/barrage.desktop
%{_pixmapsdir}/barrage48.png
