BASE = intro-stellar-physics
TEX = xelatex
BIB = bibtex
OPS = --file-line-error --synctex=1
COMPILE = $(TEX) $(OPS)
RM = rm -f

CHAPTERS = frontmatter \
	starlight \
	hydrostatic-balance \
	mean-free-path \
	stellar-atmospheres \
	classifying-stars \
	convection \
	nuclear-burning \
	main-sequence \
	degeneracy \
	post-main-sequence

TEX_SRC = $(foreach chap, $(CHAPTERS), $(wildcard $(chap)/*.tex))

FIGURES = frontmatter/cover-art.png \
	starlight/figs/intensity.pdf \
	starlight/figs/intensity-conserved.pdf \
	starlight/figs/UBVRI.pdf \
	starlight/figs/E-B-free-space.pdf \
	classifying-stars/figs/spectral_types.pdf \
	hydrostatic-balance/figs/fall-to-center.pdf \
	hydrostatic-balance/figs/hydrostatic-equilibrium.pdf \
	mean-free-path/figs/air-hockey-mfp.pdf \
	mean-free-path/figs/mean-free-path.pdf \
	stellar-atmospheres/figs/legendre.pdf \
	degeneracy/figs/fermions.pdf \
	degeneracy/figs/scattering-classical.pdf \
	degeneracy/figs/scattering-quantum.pdf \
	convection/figs/convection-1.jpg \
	convection/figs/convection-2.jpg \
	convection/figs/convective.pdf \
	nuclear-burning/figs/tunnel-schematic.pdf \
	nuclear-burning/figs/coulomb_integrand.pdf \
	main-sequence/figs/luminosity-eqn.pdf


BIBS = bibs/stellar-astro.bib

default: $(BASE).pdf

$(BASE).pdf: $(BASE).tex $(TEX_SRC) $(FIGURES) $(BIBS)
	git rev-parse --short=8 HEAD > git-info.tex
	$(COMPILE) $(BASE).tex
	$(BIB) $(BASE).aux
	$(COMPILE) $(BASE).tex
	$(COMPILE) $(BASE).tex

clean:
	-$(RM) *.aux *.log *.dvi *.bbl *.blg *.toc *.lot *.lof *.loe *.lob *.out *.synctex.gz

realclean: clean
	-$(RM) $(BASE).pdf
