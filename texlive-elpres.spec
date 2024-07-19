Name:		texlive-elpres
Version:	71385
Release:	1
Summary:	A simple class for electronic presentations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/elpres
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elpres.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elpres.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Elpres is a simple class for electronic presentations to be
shown on screen or a beamer. Elpres is derived from article.cls
and may be used with LaTeX or pdfLaTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/elpres
%doc %{_texmfdistdir}/doc/latex/elpres

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
