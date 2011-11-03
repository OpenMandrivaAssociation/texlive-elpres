# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/elpres
# catalog-date 2007-05-25 16:15:27 +0200
# catalog-license lppl
# catalog-version v0.3
Name:		texlive-elpres
Version:	v0.3
Release:	1
Summary:	A simple class for electronic presentations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/elpres
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elpres.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elpres.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Elpres is a simple class for electronic presentations to be
shown on screen or a beamer. Elpres is derived from article.cls
and may be used with LaTeX or pdfLaTeX.

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
%{_texmfdistdir}/tex/latex/elpres/elpres.cls
%doc %{_texmfdistdir}/doc/latex/elpres/elpres-example.tex
%doc %{_texmfdistdir}/doc/latex/elpres/elpres-manual.pdf
%doc %{_texmfdistdir}/doc/latex/elpres/elpres-manual.tex
%doc %{_texmfdistdir}/doc/latex/elpres/gradient1.png
%doc %{_texmfdistdir}/doc/latex/elpres/gradient2.png
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
