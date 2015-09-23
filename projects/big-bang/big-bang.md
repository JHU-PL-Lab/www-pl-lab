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
  Smith. [Types for Flexible Objects](/projects/big-bang/papers/types-for-flexible-objects.pdf),
  Asian Symposium on Programming Languages and Systems. Singapore, November
  2014.

  Previous drafts:

  - [March 2014](/projects/big-bang/papers/types-for-flexible-objects_2014-03-25.pdf).

  - [January 2014](/projects/big-bang/papers/types-for-flexible-objects_2014-01-13.pdf).

  - [May 2013](/projects/big-bang/papers/types-for-flexible-objects_2013-05.pdf).


- Pottayil Harisanker Menon, Zachary Palmer, Alexander Rozenshteyn, Scott
  Smith. [PatBang: Flexible type-safe pattern matching](/projects/big-bang/papers/pat-bang.pdf),
  technical report. Last updated September 2013.

- Pottayil Harisanker Menon, Zachary Palmer, Alexander Rozenshteyn, Scott
  Smith. [A Practical, Typed Variant Object Model](/projects/big-bang/papers/a-pratical-type-variant-object-model.pdf),
  Foundations of Object-Oriented Languages. Tucson, AZ, USA,
  October 2012. [Slides](/projects/big-bang/slides/a-pratical-type-variant-object-model-slides.pdf).

- Pottayil Harisanker Menon, Zachary Palmer, Alexander Rozenshteyn, Scott
  Smith. [Big Bang: Designing a Statically-Typed Scripting Language](/projects/big-bang/papers/big-bang.pdf),
  International Workshop on Scripts to Programs. Beijing, China,
  June 2012. [Slides](/projects/big-bang/slides/big-bang-slides.pdf).

Dissertations
-------------

- Zachary
  Palmer. [Building a Typed Scripting Language](/projects/big-bang/dissertations/building-a-typed-scripting-language.pdf).
