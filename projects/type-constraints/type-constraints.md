---
title: "Type Constraints"
permalink: "/projects/type-constraints/"
narrow: true
---

Status

: Inactive.

Set constraint types are a generalization of the standard notion of "type" to
types which are sets of constraints about program behavior. Set constraints can
capture more details about the potential values that can be in a variable than a
traditional type system. For instance, in an object-oriented language such as
Java, a variable declared as "Serializable" by the Java type system can be any
object which conforms to the Serializable interface, but in practice that
variable will only contain the concrete objects which the program in fact
serializes. Knowing the precise classes the program is serializing at that point
is useful both as a programming aid and as a tool to assist compilers in
generating faster code. Recently we have developed and implemented a tool which
statically checks whether Java downcasts are legal using a set-constraint-based
mechanism.

Type constraint systems are a very expressive form of type which can be given to
programs. They are so expressive that they can in fact fully record flow
information about a program, namely this data value could flow to that
operation.

Goal

: The development of rich type constraint systems for object-oriented
  programming languages.

  Our primary goal has been the extension of type constraint system to allow for
  greater expressivity and usefulness in typing more properties of programs.

Uses

: - Fine-grained type systems for flexible object-oriented languages.

  - Fine-grained program analysis for compilers and other static analysis
    consumers.

Publications
------------

- Tiejun Wang and Scott Smith,
  [Precise Constraint-Based Type Inference for Java](/projects/type-constraints/papers/precise-constraint-based-type-inference-for-java.pdf). ECOOP 2001. [Full version](/projects/type-constraints/papers/precise-constraint-based-type-inference-for-java-full-version.pdf).

  Abstract

  : Precise type information is invaluable for analysis and optimization of
    object-oriented programs. Some forms of polymorphism found in
    object-oriented languages pose significant difficulty for type inference, in
    particular _data polymorphism_. Agesen's Cartesian Product Algorithm (CPA)
    can analyze programs with parametric polymorphism in a reasonably precise
    and efficient manner, but CPA loses precision for programs with data
    polymorphism. This paper presents a precise constraint-based type inference
    system for Java. It uses Data Polymorphic CPA, a constraint-based type
    inference algorithm which extends CPA with the ability to accurately and
    efficiently analyze data polymorphic programs. The system is implemented for
    the full Java language, and is used to statically verify the correctness of
    Java downcasts. Benchmark results are given which show the system performs
    very well: it is significantly more accurate and is nearly as efficient as
    CPA. The implementation itself contains a number of novel optimizations
    which proved necessary to achieve scalability.

  [Try Out the Inference Algorithm Here!](http://www.cs.jhu.edu/~wtj/precise/)

- Scott Smith and Tiejun Wang,
  [Polyvariant Flow Analysis With Constrained Types](/projects/type-constraints/papers/polyvariant-flow-analysis-with-constrained-types.pdf). In
  Gert Smolka, editor, Proceedings of the 2000 European Symposium on Programming
  (ESOP'00), volume 1782 of Lecture Notes in Computer Science, pages
  382--396. Springer Verlag, March 2000.

  Abstract

  : The basic idea behind improving the quality of a monovariant control flow
    analysis such as 0CFA is the concept of polyvariant analyses such as
    Agesen's Cartesian Product Algorithm (CPA) and Shivers' <em>n</em>CFA. In
    this paper we develop a novel framework for polyvariant flow analysis based
    on Aiken-Wimmers constrained type theory. We develop instantiations of our
    framework to formalize various polyvariant algorithms, including
    <em>n</em>CFA and CPA. With our CPA formalization, we show the call-graph
    based termination condition for CPA will not always guarantee
    termination. We then develop a novel termination condition and prove it
    indeed leads to a terminating algorithm. Additionally, we show how data
    polymorphism can be modeled in the framework, by defining a simple extension
    to CPA that incorporates data polymorphism.

- V. Trifonov, S.Smith,
  [Subtyping Constrained Types](/projects/type-constraints/papers/subtyping-constrained-types.pdf),
  Static Analysis Symposium (SAS) 1996, Lecture Notes in Computer Science 1145,
  pp. 349-365.

  Abstract

  : Constrained type systems are a natural generalization of Hindley/Milner type
    inference to languages with subtyping. This paper develops several subtyping
    relations on constrained types. We establish a full type abstraction
    property that equates an operational notion of subtyping with a semantic
    notion based on regular trees. The decidability of this notion of subtyping
    is open; we present a decidable approximation. Subtyping constrained types
    has application to functor signature matching.

- J. Palsberg, S. Smith,
  [Constrained Types and their Expressiveness](/projects/type-constraints/papers/constrained-types-and-their-expressiveness.pdf),
  TOPLAS 18 (5), Sept 1996, pp. 519-527.

- Kim B. Bruce, Luca Cardelli, Giuseppe Castagna, The Hopkins Objects Group,
  Gary T. Leavens, and Benjamin Pierce. On Binary Methods, Theory and Practice
  of Object Systems 1 (3), 1995, pp. 217-238. Department of Computer Science,
  Iowa State University,
  [TR95-08](ftp://ftp.cs.iastate.edu/pub/techreports/TR95-08/TR.ps.Z), May 1995.

- J. Eifrig, S. Smith, V. Trifonov,
  [Sound Polymorphic Type Inference for Objects](/projects/type-constraints/papers/sound-polymorphic-type-inference-for-objects.pdf),
  OOPSLA 1995, pp. 169-384.

- J. Eifrig, S. Smith, V. Trifonov,
  [Type Inference for Recursively Constrained Types and its Application to OOP](/projects/type-constraints/papers/type-inference-for-recursively-constrained-types-and-its-application-to-oop.pdf)
  ([longer version](/projects/type-constraints/papers/type-inference-for-recursively-constrained-types-and-its-application-to-oop-longer-version.pdf)),
  Mathematical Foundations of Programming Semantics 1995 (Elsevier
  [Electronic Notes in Theoretical Computer Science](http://www.elsevier.com/locate/entcs/),
  volume 1).

- J. Eifrig, S. Smith, V. Trifonov, A. Zwarico,
  [Application of OOP Type Theory: State, Decidability, Integration](/projects/type-constraints/papers/application-of-oop-type-theory-state-decidability-integration.pdf),
  OOPSLA 1994, pp. 16-30.

- J. Eifrig, S. Smith, V. Trifonov, A. Zwarico,
  [An Interpretation of Typed OOP in a Language with State](/projects/type-constraints/papers/an-interpretation-of-typed-oop-in-a-language-with-state.pdf),
  Lisp and Symbolic Computation 8 (4), 1995, pp. 357-397.

- J. Eifrig, S. Smith, V. Trifonov, A. Zwarico,
  [A Simple Interpretation of OOP in a Language with State](/projects/type-constraints/papers/a-simple-interpretation-of-oop-in-a-language-with-state.pdf),
  Workshop on State in Programming Languages 1993, pp. 1-36.
