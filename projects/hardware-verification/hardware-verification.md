---
title: "Hardware Verification"
permalink: "/projects/hardware-verification/"
narrow: true
---

Status

: Inactive.

In collaboration with Amy Zwarico we defined a formal language for specifying
asynchronous digital circuits that is based on Hoare's CSP, and verified a
translation of these circuit specifications to hardware devices (collections of
gates). The translation was proven correct by defining a formal operational
notion of equivalence, and incrementally translating the specification to the
circuit in small steps that preserve equivalence. Numerous informal arguments of
correctness of similar synthesis methods exist, but this work is the first
complete, rigorous proof of correctness of such a method. Some other features of
this project include the following.

- The translation is defined by a set of rewrite rules, broken into five phases.
- A new notion of "translational equivalence" is defined to state how a
  translation preserves meaning when the language itself is changing.
- Only fair executions considered, for gates are inherently fair. This is some
  of the first work in circuit theory to consider fairness.

Publications
------------

correct-compilation-of-specifications-to-deterministic-asynchronous-circuits

- S. Smith, A. Zwarico,
  [Correct Compilation of Specifications to Deterministic Asynchronous Circuits](/projects/hardware-verification/papers/correct-compilation-of-specifications-to-deterministic-asynchronous-circuits-1995.pdf). Formal
  Methods in System Design volume 7, 1995.

- S. Smith, A. Zwarico,
  [Correct Compilation of Specifications to Deterministic Asynchronous Circuits](/projects/hardware-verification/papers/correct-compilation-of-specifications-to-deterministic-asynchronous-circuits-1993.pdf). Correct
  Hardware Design Methodologies, Arles, France, May 1993, Lecture Notes in
  Computer Science, volume 683.
