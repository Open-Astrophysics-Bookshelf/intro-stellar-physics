BASE = intro-stellar-physics
TEX = xelatex
BIB = bibtex
OPS = --file-line-error --synctex=1
COMPILE = $(TEX) $(OPS)
RM = rm -f

CHAPTERS = frontmatter \
	starlight \
	hydrostatic-balance \
	radiative-transport \
	classifying-stars \
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
	radiative-transport/figs/air-hockey-mfp.pdf \
	radiative-transport/figs/mean-free-path.pdf \
	radiative-transport/figs/diffusive-flux.pdf \
	radiative-transport/figs/radiative-transfer-exercise.pdf \
	radiative-transport/figs/random-walk.pdf \
	radiative-transport/figs/legendre.pdf \
	nuclear-burning/figs/tunnel-schematic.pdf \
	nuclear-burning/figs/coulomb_integrand.pdf \
	main-sequence/figs/convection-1.jpg \
	main-sequence/figs/convection-2.jpg \
	main-sequence/figs/archimedes.png \
	main-sequence/figs/convection_hinode.jpg \
	main-sequence/figs/convective.pdf \
	main-sequence/figs/luminosity-eqn.pdf \
	main-sequence/figs/fermions.pdf \
	main-sequence/figs/scattering-classical.pdf \
	main-sequence/figs/scattering-quantum.pdf \
	main-sequence/figs/etacarinae_hubble_900.jpg


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
