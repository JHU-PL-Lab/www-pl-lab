---
title: "The Nuggetizer"
permalink: "/projects/nuggetizer/"
narrow: true
---

Status

: Inactive.

Goal
----

Develop a highly precise and powerful program analysis applicable across a wide
range of higher-order programming paradigms, based on the idea of extracting
inductive definitions from programs. Inductive definitions are the _lingua
franca_ of modern theorem provers and compiling a program directly to an
inductive definition puts the program in a language the theorem prover will best
be able to reason about.

Publications
------------



- Paritosh Shroff, Christian Skalka, and Scott
  Smith. [The Nuggetizer: Abstracting Away Higher-Orderness for Program Verification](/projects/nuggetizer/papers/the-nuggetizer-abstracting-away-higher-orderness-for-program-verification.pdf). In
  [APLAS 2007](http://flint.cs.yale.edu/aplas2007/): The Fifth ASIAN Symposium
  on Programming Languagues and Systems.

  Slides

  : - [PPT](/projects/nuggetizer/slides/the-nuggetizer-abstracting-away-higher-orderness-for-program-verification-slides.ppt).
    - [PDF](/projects/nuggetizer/slides/the-nuggetizer-abstracting-away-higher-orderness-for-program-verification-slides.pdf).

  [Technical Report](/projects/nuggetizer/technical-reports/the-nuggetizer-abstracting-away-higher-orderness-for-program-verification-technical-report.pdf).

  Abstract

  : We develop a static analysis which distills first-order computational
    structure from higher-order functional programs. The analysis condenses
    higher-order programs into a first-order rule-based system, a _nugget_, that
    characterizes all value bindings that may arise from program
    execution. Theorem provers are limited in their ability to automatically
    reason about higher-order programs; nuggets address this problem, being
    inductively defined structures that can be simply and directly encoded in a
    theorem prover. The theorem prover can then prove non-trivial program
    properties, such as the range of values assignable to particular variables
    at runtime. Our analysis is flow- and path-sensitive, and incorporates a
    novel prune-rerun analysis technique to approximate higher-order recursive
    computations.

  Keywords

  : - Program Analysis.
    - Higher-Order.
    - 0CFA.
    - Program Verification.
