"""
Generates a file <chapter>-handout.tex that can then be processed to make a 
handout. Adjust the string `frontmatter` to make the fonts to your liking.  In 
particular, if you don't want to use the stix, raleway, etc. fonts, change
    \documentclass[profonts,stix,handout]{astro-bookshelf}
to
    \documentclass[handout]{astro-bookshelf}
"""

import argparse

parser = argparse.ArgumentParser(description="writes out handout for a specified chapter.")
parser.add_argument('chapter_name',type=str,default=None,help="file name for chapter.") 

frontmatter=r'''% !TEX TS-program = xelatex
\documentclass[profonts,stix,handout]{astro-bookshelf}
\hypersetup{colorlinks=true,linkcolor=blue,citecolor=black,urlcolor=blue}

\usepackage{aasjournals}

\graphicspath{%
{frontmatter/}{starlight/figs/}{hydrostatic-balance/figs/}{radiative-transport/figs/}{classifying-stars/figs/}{nuclear-burning/figs/}{main-sequence/figs/}{post-main-sequence/figs/}
}

\usepackage{starType}
\input{symbols}
% for aligning table columns
\usepackage{dcolumn}
\newcolumntype{d}[1]{D{.}{.}{#1}}
\newcommand{\tabhead}[1]{\multicolumn{1}{c}{#1}}
% for coloring rows
\usepackage{colortbl}

\newcommand*{\maintitle}{Stars}

\author{Edward Brown}
%\publisher{Open Astrophysics Bookshelf}
\date{\today}'''

backmatter=r'''
\bibliographystyle{plainnat}
\bibliography{bibs/stellar-astro}

\end{document}
'''

titles = {
	"classifying-stars":"Stellar classification",
    "hydrostatic-balance":"Hydrostatic balance and basic stellar properties",
	"mean-free-path":"Transport: The mean free path",
    "stellar-atmospheres":"A closer look at the Eddington approximation",
    "atomic-lines":"Atomic Lines",
    "degeneracy":"The Equation of State",
    "convection":"Convection",
    "nuclear-burning":"Non-resonant fusion reactions",
    "main-sequence":"The main sequence",
    "post-main-sequence":"After the main sequence"
}

# execution starts here

args = parser.parse_args()
chapter = args.chapter_name

# check name
if chapter not in titles.keys():
    raise ValueError('invalid name for the chapter')

texfile=chapter.strip()+'-handout.tex'

title = r'\title{{{0}}}'.format(titles[chapter])
chapter = r'\input{{{0}/{0}}}'.format(chapter)
folios = (frontmatter,title,r'\begin{document}',r'\maketitle',chapter,backmatter)

with open(texfile,'w') as f:
    f.write('\n\n'.join(folios))

