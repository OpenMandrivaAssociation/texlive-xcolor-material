%global tl_name xcolor-material
%global tl_revision 42289

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Defines the 256 colors from Google Material Color Palette
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xcolor-material
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xcolor-material.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xcolor-material.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xcolor-material.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is built on top of the great xcolor package. It provides a
useful definition of the beautiful Google Material Color Palette,
available at Google Material design, for its use in document writing
with LaTeX and Friends.

