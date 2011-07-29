Summary:	Kill and destroy as many target as possible in 3 minutes
Summary(pl.UTF-8):	Zniszcz jak najwięcej wrogów w przeciągu 3 minut
Name:		barrage
Version:	1.0.4
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/lgames/%{name}-%{version}.tar.gz
# Source0-md5:	8c767edc4cf3f84cbfb6dc19e24f5743
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

%description -l pl.UTF-8
Barrage jest dość brutalną grą akcji, której celem jest zniszczenie
jak największej ilości przeciwników w przeciągu 3 minut. Gracz steruje
bronią, która może wystrzeliwać zarówno małe jak i duże granaty w
kierunku żołnierzy, jeepów i czołgów. Zasady są proste, lecz osiągnięcie 
dobrych wyników jest trudnym zadaniem.

%prep
%setup -q
# %patch0 -p1

%build
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
%{_iconsdir}/hicolor/*/apps/%{name}.png
