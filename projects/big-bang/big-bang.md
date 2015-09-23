---
title: "Big Bang"
permalink: "/projects/big-bang/"
narrow: true
---

The Big Bang project aims to create a typed programming language with the feel
and convenience of modern scripting languages. Projects such as DRuby and Typed
Racket retrofit type systems onto existing scripting languages; unfortunately,
these projects are burdened by backwards compatibility, as dynamic scripting
languages are developed without regard to the static typeability of the features
they include. Big Bang re-examines the design of scripting-style languages from
a static typing perspective. In particular, we prioritize:

No explicit typing

: One primary appeal of scripting languages is that programmers need not
  explicitly specify types, even at module or function boundaries.

Global type inference

: The type system should not be brittle to refactorings such as method
  extraction.

Performance

: Using static type information, we contend that it will be possible to compile
  Big Bang scripts to much more efficient programs than with scripting languages
  such as Python or Ruby.

Path sensitivity

: Scripting programmers often use path-sensitive reasoning when confirming that
  a program is sound; the Big Bang type system does as well.

No arbitrary cutoffs

: Polymorphism in Big Bang does not rely on fixed cutoffs or scoping limitations;
  this ensures that the programmer will not be surprised by arbitrary compiler
  decisions.


The Big Bang project is still in a fledgling state. For questions or comments,
please contact <big-bang@jhu.edu>.

Publications
------------

- Pottayil Harisanker Menon, Zachary Palmer, Alexander Rozenshteyn, Scott
  Smith. Types for Flexible Objects, Asian Symposium on Programming Languages
  and Systems. Singapore, November 2014. Previous drafts: (May 2013) (January
  2014) (March 2014).

- Pottayil Harisanker Menon, Zachary Palmer, Alexander Rozenshteyn, Scott
  Smith. PatBang: Flexible type-safe pattern matching, technical report. Last
  updated September 2013.

- Pottayil Harisanker Menon, Zachary Palmer, Alexander Rozenshteyn, Scott
  Smith. A Practical, Typed Variant Object Model, Foundations of Object-Oriented
  Languages. Tucson, AZ, USA, October 2012. Slides.

- Pottayil Harisanker Menon, Zachary Palmer, Alexander Rozenshteyn, Scott
  Smith. Big Bang: Designing a Statically-Typed Scripting Language,
  International Workshop on Scripts to Programs. Beijing, China,
  June 2012. Slides.

Dissertations
-------------

- Zachary Palmer. Building a Typed Scripting Language.
