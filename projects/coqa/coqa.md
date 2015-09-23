---
title: "Coqa: Concurrent Objects with Quantized Atomicity"
permalink: "/projects/coqa/"
narrow: true
---

Coqa is a new object-oriented language, (for **C**oncurrent **o**bjects with
**q**uantized **a**tomicity), which builds concurrency and atomicity-by-design
deeply into the object model. This ongoing project aims to reconsider of the
"right" concurrency model for tightly-coupled computations that can be easily
deployable on multi-core CPUs. This project is now a joint collaboration between
JHU and SUNY Binghamton.

The design of Coqa follows six principles that we believe are crucial for a
concurrent programming language:

- Good Concurrency Properties Preserved by Default.
- Always _En Guarde_ While Sharing.
- The Importance of Being Ubiquitously Atomic.
- Atomicity is Not Necessarily All or Nothing.
- Optimistic Atomicity is Not Always the Best Policy.
- Put OO-Style Concurrency in OO Languages.

From a programming perspective, Coqa has three desirable properties, from higher- to lower-level as follows:

Quantized atomicity

: Each method is composed of several discrete quanta, and execution of each
  quantum is serializable regardless of the interleaving of the actual
  execution.

Mutual exclusion within tasks

: Our language guarantees state change happens in a predictable way, even across
  different quanta of a task.

Race freedom

: No race conditions ever arise in object field access.

Coqa currently consists of a formal system, _KernelCoqa_ and a prototype
implementation _CoqaJava_.

Publications
------------

- Aditya Kulkarni, Yu David Liu, Scott
  Smith. [Task Types for Pervasive Atomicity](/projects/coqa/papers/task-types-for-pervasive-atomicity.pdf),
  Proceedings of the 25th ACM Conference on Object-Oriented Programming,
  Systems, Languages and Applications (OOPSLA 2010). Reno, Nevada, USA, October
  2010.

  Abstract

  : Atomic regions are an important concept in correct concurrent programming:
    since atomic regions can be viewed as having executed in a single step,
    atomicity greatly reduces the number of possible interleavings the
    programmer needs to consider. This paper describes a method for building
    atomicity into a programming language in an organic fashion. We take the
    view that atomicity holds for whole threads by default, and a division into
    smaller atomic regions occurs only at points where an explicit need for
    sharing is needed and declared. A corollary of this view is every line of
    code is part of some atomic region. We define a polymorphic type system,
    Task Types, to enforce most of the desired atomicity properties
    statically. We show the reasonableness of our type system by proving that
    type soundness, isolation invariance, and atomicity enforcement properties
    hold at run time. We also present initial results of a Task Types
    implementation built on Java.

- Yu David Liu, Xiaoqi Lu, and Scott
  Smith. [Coqa: Concurrent Objects with Quantized Atomicity](/projects/coqa/papers/coqa-concurrent-objects-with-quantized-atomicity.pdf). Compiler
  Construction
  (CC), 2008. [Slides](/projects/coqa/slides/coqa-concurrent-objects-with-quantized-atomicity-slides.ppt).

  Abstract

  : This paper introduces a new language model, Coqa, for deeply embedding
    concurrent programming into objects. Every program written in our language
    has the desirable behaviors of atomicity, mutual exclusion, and race freedom
    automatically built in. A key property of our model is the notion of
    quantized atomicity: every concurrent program execution can be viewed as
    being divided into quantum regions of atomic execution, greatly reducing the
    number of interleavings to consider. So rather than building atomicity
    locally, with small declared zones, we build it globally, down from the
    top. We justify our approach both from a theoretical basis by showing that a
    formal representation, KernelCoqa, has provable quantized atomicity
    properties, and by implementing CoqaJava, a Java extension incorporating all
    of the Coqa features.

Dissertations
-------------

- Xiaoqi
  Lu. [Coqa: a Concurrent Programming Model with Ubiquitous Atomicity](/projects/coqa/dissertations/coqa-a-concurrent-programming-model-with-ubiquitous-atomicity.pdf). PhD
  Thesis, The Johns Hopkins University, November 2007.
