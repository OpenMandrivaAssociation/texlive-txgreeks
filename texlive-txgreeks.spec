# revision 21839
# category Package
# catalog-ctan /macros/latex/contrib/txgreeks
# catalog-date 2011-03-18 12:27:11 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-txgreeks
Version:	1.0
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package allows LaTeX users who use the TX fonts to select
the shapes (italic or upright) for the Greek lowercase and
uppercase letters. Once the shapes for lowercase and uppercase
have been selected via a package option, the \other prefix
(e.g., \otheralpha) allows using the alternate glyph (as in the
fourier package). The txgreeks package does not constrain the
text font that may be used in the document.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/txgreeks/txgreeks.sty
%doc %{_texmfdistdir}/doc/latex/txgreeks/README
%doc %{_texmfdistdir}/doc/latex/txgreeks/txgreeks.pdf
#- source
%doc %{_texmfdistdir}/source/latex/txgreeks/txgreeks.dtx
%doc %{_texmfdistdir}/source/latex/txgreeks/txgreeks.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
