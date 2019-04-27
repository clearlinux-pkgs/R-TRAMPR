#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-TRAMPR
Version  : 1.0.8
Release  : 18
URL      : https://cran.r-project.org/src/contrib/TRAMPR_1.0-8.tar.gz
Source0  : https://cran.r-project.org/src/contrib/TRAMPR_1.0-8.tar.gz
Summary  : 'TRFLP' Analysis and Matching Package for R
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R

%description
polymorphism ('TRFLP') profiles between unknown samples and a
        database of known samples.  TRAMPR facilitates analysis of
        many unknown profiles at once, and provides tools for working
        directly with electrophoresis output through to generating
        summaries suitable for community analyses with R's rich set of
        statistical functions.  TRAMPR also resolves the issues of
        multiple 'TRFLP' profiles within a species, and shared 'TRFLP'
        profiles across species.

%prep
%setup -q -c -n TRAMPR

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552942711

%install
export SOURCE_DATE_EPOCH=1552942711
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library TRAMPR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library TRAMPR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library TRAMPR
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  TRAMPR || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/TRAMPR/CITATION
/usr/lib64/R/library/TRAMPR/DESCRIPTION
/usr/lib64/R/library/TRAMPR/INDEX
/usr/lib64/R/library/TRAMPR/Meta/Rd.rds
/usr/lib64/R/library/TRAMPR/Meta/data.rds
/usr/lib64/R/library/TRAMPR/Meta/features.rds
/usr/lib64/R/library/TRAMPR/Meta/hsearch.rds
/usr/lib64/R/library/TRAMPR/Meta/links.rds
/usr/lib64/R/library/TRAMPR/Meta/nsInfo.rds
/usr/lib64/R/library/TRAMPR/Meta/package.rds
/usr/lib64/R/library/TRAMPR/Meta/vignette.rds
/usr/lib64/R/library/TRAMPR/NAMESPACE
/usr/lib64/R/library/TRAMPR/R/TRAMPR
/usr/lib64/R/library/TRAMPR/R/TRAMPR.rdb
/usr/lib64/R/library/TRAMPR/R/TRAMPR.rdx
/usr/lib64/R/library/TRAMPR/data/demo.knowns.rda
/usr/lib64/R/library/TRAMPR/data/demo.samples.rda
/usr/lib64/R/library/TRAMPR/demo_samples_abi.txt
/usr/lib64/R/library/TRAMPR/demo_samples_abi_info_full.csv
/usr/lib64/R/library/TRAMPR/demo_samples_abi_soilcore.csv
/usr/lib64/R/library/TRAMPR/demo_samples_abi_template_full.csv
/usr/lib64/R/library/TRAMPR/doc/TRAMPRdemo.R
/usr/lib64/R/library/TRAMPR/doc/TRAMPRdemo.Rnw
/usr/lib64/R/library/TRAMPR/doc/TRAMPRdemo.pdf
/usr/lib64/R/library/TRAMPR/doc/index.html
/usr/lib64/R/library/TRAMPR/help/AnIndex
/usr/lib64/R/library/TRAMPR/help/TRAMPR.rdb
/usr/lib64/R/library/TRAMPR/help/TRAMPR.rdx
/usr/lib64/R/library/TRAMPR/help/aliases.rds
/usr/lib64/R/library/TRAMPR/help/paths.rds
/usr/lib64/R/library/TRAMPR/html/00Index.html
/usr/lib64/R/library/TRAMPR/html/R.css