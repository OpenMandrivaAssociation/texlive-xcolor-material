Name:		texlive-xcolor-material
Version:	42289
Release:	1
Summary:	Defines the 256 colors from Google Material Color Palette
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xcolor-material
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcolor-material.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcolor-material.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcolor-material.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is built on top of the great xcolor package. It
provides a useful definition of the beautiful Google Material
Color Palette, available at Google Material design, for its use
in document writing with LaTeX and Friends.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/xcolor-material
%{_texmfdistdir}/tex/latex/xcolor-material
%doc %{_texmfdistdir}/doc/latex/xcolor-material

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
