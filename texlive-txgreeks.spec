# revision 21839
# category Package
# catalog-ctan /macros/latex/contrib/txgreeks
# catalog-date 2011-03-18 12:27:11 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-txgreeks
Version:	1.0
Release:	4
Summary:	Shape selection for TX fonts Greek letters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/txgreeks
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/txgreeks.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/txgreeks.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/txgreeks.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 757164
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719823
- texlive-txgreeks
- texlive-txgreeks
- texlive-txgreeks

