"""
Generates a file <chapter>-handout.tex that can then be processed to make a 
handout. Adjust the string `frontmatter` to make the fonts to your liking.
"""

import argparse

parser = argparse.ArgumentParser(description="writes out handout for a specified chapter.")
parser.add_argument('chapter_name',type=str,default=None,help="file name for chapter.") 

frontmatter=r'''% !TEX TS-program = xelatex
\documentclass[handout]{astro-bookshelf}
\hypersetup{colorlinks=true,linkcolor=blue,citecolor=black,urlcolor=blue}

\usepackage{aasjournals}

\graphicspath{%
{frontmatter/}{starlight/figs/}{hydrostatic-balance/figs/}{radiative-transport/figs/}{classifying-stars/figs/}{nuclear-burning/figs/}{main-sequence/figs/}{post-main-sequence/figs/}
}

\usepackage{starType}
\input{symbols}
\newcommand{\newterm}[1]{\textsc{#1}}

% for aligning table columns
\usepackage{dcolumn}
\newcolumntype{d}[1]{D{.}{.}{#1}}
\newcommand{\tabhead}[1]{\multicolumn{1}{c}{#1}}
% for coloring rows
\usepackage{colortbl}
\usepackage{aasjournals}

\newcommand*{\maintitle}{To Build a Star}

\author{Edward Brown}
%\publisher{Open Astrophysics Bookshelf}
\date{\today}'''

backmatter=r'''
\bibliographystyle{plainnat}
\bibliography{bibs/stellar-astro}

\end{document}
'''

titles = {
	"starlight":"Starlight",
    "hydrostatic-balance":"Under Pressure",
	"radiative-transport":"Edge of Darkness",
    "classifying-stars":"Rainbow in the Dark",
    "nuclear-burning":"Burn",
    "main-sequence":"Star",
    "post-main-sequence":"End of the Line"
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

