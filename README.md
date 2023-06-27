# Introduction to Stellar Astrophysics

Part of the [Open Astrophysics Bookshelf](http://open-astrophysics-bookshelf.github.io/).  A pdf of these notes is available at [https://web.pa.msu.edu/people/ebrown/docs/intro-stellar-physics.pdf](https://web.pa.msu.edu/people/ebrown/docs/intro-stellar-physics.pdf).

These notes were written for the junior/senior undergraduate course on stars at Michigan State University. They are based on my notes from teaching this course in 2012, 2014, and 2016, and were put into manuscript form, with additional figures and exercises, during the spring and summer of 2018. The motivation for assembling the notes was to make a self-contained package that could be inexpensively distributed to students instead of a textbook.

In addition to deriving a basic physical description of how stars work, a secondary goal of the course is to train students to make simple physical models and order-of-magnitude estimates. This is a crucial skill that is not incorporated enough into the typical undergraduate physics courses. In keeping with this goal, many of the exercises ask the students to make estimates or to employ simple models, such as constant density throughout the star, rather than to perform elaborate calculations. There are some exercises in the text that must be solved numerically, and the course does include a group numerical project.

The text layout uses the [`tufte-book`](https://tufte-latex.github.io/tufte-latex/) LaTeX class: the main features are a large outer margin in which the students can take notes and the tight integration of text, figures, and sidenotes. Exercises are embedded throughout the text. The exercises range from comprehension checks to longer, more challenging problems. This layout is meant to encourage students to actively work through the notes. I've also added boxes containing more advanced material that I felt students should be exposed to, but were not essential to the main development of the course. 

If you do use these notes, I'd appreciate hearing about it!  This helps justify my efforts in maintaining them and adding new material.

## License

Except where explicitly noted, this work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license.

## Requirements for installing

0. Either pdfLaTeX or XeLaTeX.
1. [`tufte-book`](https://tufte-latex.github.io/tufte-latex/) LaTeX class
2. The [`starType`](https://github.com/nworbde/starType) macros.  You can install this from the source; alternatively, a shell script `install_local_starType` is provided to automatically fetch the macros into the directory of this package.

## To build

1. For a default installation, simply `make`.  This will build the document using pdfLaTeX.
2. If you wish to use XeLaTeX, change line 2 of the makefile to read `COMPILE=xelatex`. In this case you will need the TeX Gyre Fonts installed. You may also need to modify the latex class file `tufte-common.def` so that  `fontspec` is loaded with the correct options. A patch file, `tufte-patch`, is included. To use, `patch /path/to/tufte-common.def tufte-patch` (you may need to run this using `sudo`).

    1. If you have Chaparral Pro, Source Code Pro, and Raleway Medium fonts available, add the option `profonts` to the `\documentclass` directive in AST208-notes.tex.
    2. If you wish to use the STIX fonts for greek letters, add the option `stix` to the `\documentclass` directive in AST208-notes.tex.
