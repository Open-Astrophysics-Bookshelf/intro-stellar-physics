BASE = intro-stellar-physics
COMPILE = xelatex
OPS = --file-line-error --synctex=1
RM = rm -f

CHAPTERS = frontmatter \
	classifying-stars \
	hydrostatic-balance \
	mean-free-path \
    stellar-atmospheres \
	atomic-lines \
    degeneracy \
	convection \
	nuclear-burning \
	main-sequence \
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
	atomic-lines/figs/damped.pdf \
	atomic-lines/figs/beats.pdf \
	atomic-lines/figs/comparison.pdf \
	atomic-lines/figs/damped-driven.pdf \
	atomic-lines/figs/simple-spring.png \
	degeneracy/figs/fermions.pdf \
	degeneracy/figs/scattering-classical.pdf \
	degeneracy/figs/scattering-quantum.pdf \
	convection/figs/convection-1.jpg \
	convection/figs/convection-2.jpg \
	convection/figs/convective.pdf \
	nuclear-burning/figs/tunnel-schematic.pdf \
	nuclear-burning/figs/coulomb_integrand.pdf \
	main-sequence/figs/luminosity.pdf


BIBS = bibs/stellar-astro.bib

default: $(BASE).pdf

$(BASE).pdf: $(BASE).tex $(TEX_SRC) $(FIGURES) $(BIBS)
	git rev-parse --short=8 HEAD > git-info.tex
	$(COMPILE) $(OPS) $(BASE).tex
	bibtex $(BASE).aux
	$(COMPILE) $(OPS) $(BASE).tex
	$(COMPILE) $(OPS) $(BASE).tex

clean:
	-$(RM) *.aux *.log *.dvi  *.bbl *.blg *.toc *.lot *.lof *.loe *.lob *.out *.synctex.gz

realclean: clean
	-$(RM) $(BASE).pdf
