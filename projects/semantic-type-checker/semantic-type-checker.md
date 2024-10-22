---
title: "Semantic-Type-Guided Type Checker"
permalink: "/projects/semantic-type-checker/"
narrow: true
---

Status

: Active.

**Semantic typing** is an approach to typing where, rather than relying on a static type system to define the meaning of types, type inhabitants are determined solely by the behaviors of expressions under an operational or denotational semantics of (untyped) expressions. One fundamental challenge with semantic types is that type membership is undecidable. However, if the focus is on finding **incorrect typings**, only a single **counterexample** is needed.

Publications
------------

Kelvin Qian, Scott Smith, Brandon Stride, Shiwei Weng, Ke Wu, [Semantic-Type-Guided Bug Finding](https://dl.acm.org/doi/10.1145/3689788), Proceedings of the ACM on Programming Languages, Volume 8, Issue OOPSLA2 Article No.: 348, Pages 2183 - 2210.
[Repo](https://github.com/JHU-PL-Lab/jaylang). [Paper](https://dl.acm.org/doi/pdf/10.1145/3689788).

  Abstract

  : In recent years, there has been an increased interest in tools that establish incorrectness rather than correctness of program properties. In this work we build on this approach by developing a novel methodology to prove incorrectness of semantic typing properties of functional programs, extending the incorrectness approach to the model theory of functional program typing. We define a semantic type refuter which refutes semantic typings for a simple functional language. 
  
    We prove our refuter is co-recursively enumerable, and that it is sound and complete with respect to a semantic typing notion. An initial implementation is described which uses symbolic evaluation to efficiently find type errors over a functional language with a rich type system.