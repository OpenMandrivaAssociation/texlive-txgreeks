Name:		texlive-txgreeks
Version:	21839
Release:	2
Summary:	Shape selection for TX fonts Greek letters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/txgreeks
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/txgreeks.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/txgreeks.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/txgreeks.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows LaTeX users who use the TX fonts to select
the shapes (italic or upright) for the Greek lowercase and
uppercase letters. Once the shapes for lowercase and uppercase
have been selected via a package option, the \other prefix
(e.g., \otheralpha) allows using the alternate glyph (as in the
fourier package). The txgreeks package does not constrain the
text font that may be used in the document.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/txgreeks/txgreeks.sty
%doc %{_texmfdistdir}/doc/latex/txgreeks/README
%doc %{_texmfdistdir}/doc/latex/txgreeks/txgreeks.pdf
#- source
%doc %{_texmfdistdir}/source/latex/txgreeks/txgreeks.dtx
%doc %{_texmfdistdir}/source/latex/txgreeks/txgreeks.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
