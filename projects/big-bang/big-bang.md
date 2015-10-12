---
title: "Big Bang"
permalink: "/projects/big-bang/"
narrow: true
---

Status

: Active.

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

- Zachary Palmer, Scott
  Smith. [Control-Based Program Analysis](/projects/big-bang/papers/control-based-program-analysis.pdf).
  [Implementation](https://github.com/JHU-PL-Lab/odefa-proof-of-concept).
  Draft, October 2015.

  Abstract

  : We explore a novel approach to higher-order program analysis which combines
    lazy data propagation with ideas from optimal lambda-reduction to produce a
    different form of program analysis. This analysis produces _only_ a
    control-flow graph; we derive all other information (e.g. values of
    variables) directly from this graph. The resulting analysis is flow- and
    context-sensitive with a provable polynomial-time bound. The analysis is
    formalized and proved correct and terminating, and an initial implementation
    is described.

- Pottayil Harisanker Menon, Zachary Palmer, Alexander Rozenshteyn, Scott
  Smith. [Types for Flexible Objects](/projects/big-bang/papers/types-for-flexible-objects.pdf),
  Asian Symposium on Programming Languages and Systems. Singapore, November
  2014.

  Abstract

  : Scripting languages are popular in part due to their extremely flexible
    objects. Features such as dynamic extension, mixins, and first-class
    messages improve programmability and lead to concise code. But attempts to
    statically type these features have met with limited success. Here we
    present TinyBang, a small typed language in which flexible object operations
    can be encoded. We illustrate this flexibility by solving an open problem in
    OO literature: we give an encoding where objects can be extended after being
    messaged without compromising the expressiveness of subtyping. TinyBang's
    subtype constraint system ensures that all types are completely inferred;
    there are no data declarations or type annotations. We formalize TinyBang
    and prove the type system is sound and decidable; all examples in the paper
    run in our most recent implementation.

  Previous drafts

  : - [March 2014](/projects/big-bang/papers/types-for-flexible-objects-2014-03-25.pdf).

    - [January 2014](/projects/big-bang/papers/types-for-flexible-objects-2014-01-13.pdf).

    - [May 2013](/projects/big-bang/papers/types-for-flexible-objects-2013-05.pdf).

- Pottayil Harisanker Menon, Zachary Palmer, Alexander Rozenshteyn, Scott
  Smith. [PatBang: Flexible type-safe pattern matching](/projects/big-bang/papers/pat-bang.pdf),
  technical report. Last updated September 2013.

  Abstract

  : Patterns provide an important dimension of expressiveness to functional
    programming languages because they describe a concise syntax for data
    destruction. However, most languages treat patterns as second-class
    citizens: case match expressions cannot be extended, patterns cannot be
    selected dynamically, and patterns cannot be composed or modified by program
    logic. In this paper, we present a rich, full-featured pattern language,
    PatBang, which treats patterns as first-class data, and additionally
    supports highly expressive patterns including recursive and disjunctive
    patterns, yet is still provably type-safe. We additionally show how such an
    expressive pattern language enables new programming patterns, including use
    of patterns for expressing _pytes_ , a form of lightweight static interface
    declaration. Type soundness is proven and an implementation of the type
    inference algorithm and interpreter is provided.

- Pottayil Harisanker Menon, Zachary Palmer, Alexander Rozenshteyn, Scott
  Smith. [A Practical, Typed Variant Object Model](/projects/big-bang/papers/a-pratical-type-variant-object-model.pdf),
  Foundations of Object-Oriented Languages. Tucson, AZ, USA,
  October 2012. [Slides](/projects/big-bang/slides/a-pratical-type-variant-object-model-slides.pdf).

  Abstract

  : Traditionally, typed objects have been encoded as records; the fields and
    methods of an object are stored in the fields of a record and projected when
    needed. While the dual approach of using variants instead of records has
    been explored, it is more challenging to type: the output type of a variant
    case match must depend on the input value; this is a form of dependent
    typing.

    In this paper, we construct a variant-based encoding of objects which is
    statically typeable and which improves on the flexibility of typed object
    models in several dimensions: messages can be represented as simple
    first-class data, object extension is more generally typeable than in
    previous systems and, arguably, a better integration of objects and
    functions is obtained.

    This encoding is possible due to the features of our new core language,
    TinyBang, which incorporates a subtype constraint type inference system with
    several novel extensions. We develop a generalized notion of first-class
    cases -- functions with an inherent pattern match that are composable -- and
    we extend previous notions of conditional constraint types to obtain
    accurate typings. For added flexibility, TinyBang's record-like structure is
    type-indexed, meaning data can be projected based on its type alone. Our
    record structure's concatenation operator is asymmetric by default,
    naturally supporting object extension. Finally, we develop a refined notion
    of parametric polymorphism which aims to achieve a good combi- nation of
    flexibility and efficiency of inference.

- Pottayil Harisanker Menon, Zachary Palmer, Alexander Rozenshteyn, Scott
  Smith. [Big Bang: Designing a Statically-Typed Scripting Language](/projects/big-bang/papers/big-bang.pdf),
  International Workshop on Scripts to Programs. Beijing, China,
  June 2012. [Slides](/projects/big-bang/slides/big-bang-slides.pdf).

Dissertations
-------------

- Zachary
  Palmer. [Building a Typed Scripting Language](/projects/big-bang/dissertations/building-a-typed-scripting-language.pdf).
