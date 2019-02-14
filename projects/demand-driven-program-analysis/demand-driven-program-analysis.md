---
title: "Demand-Driven Program Analysis"
permalink: "/projects/demand-driven-program-analysis/"
narrow: true
---

Status

: Active.

Demand-Driven Program Analysis (DDPA) is a novel approach to higher-order
program analysis that brings ideas of on-demand lookup from first-order
CFL-reachability program analyses to higher-order programs. The analysis needs
to produce only a control-flow graph; it can derive all other information
including values of variables directly from the graph.

Several challenges have to be overcome, including how to build the control-flow
graph on-the-fly and how to deal with nonlocal variables in functions. The
resulting analysis is flow- and context-sensitive with a provable
polynomial-time bound. Along with the theoretical development, we're also
working on efficient implementations of the variable lookup algorithm.

Publications
------------

- Leandro Facchinetti, Zachary Palmer, Scott Smith, [Higher-Order Demand-Driven Program Analysis](/projects/demand-driven-program-analysis/papers/higher-order-demand-driven-program-analysis-toplas.pdf), ACM Transactions on Programming Languages and Systems (TOPLAS), in progress, 2019.

Abstract

  : Developing accurate and efficient program analyses for languages with higher-order functions is known to be difficult. Here we define a new higher-order program analysis, **Demand-Driven Program Analysis (DDPA)**, which extends well-known demand-driven lookup techniques found in first-order program analyses to higher-order programs.

  This task presents several unique challenges to obtain good accuracy, including the need for a new method for demand-driven lookup of **non-local** variable values. DDPA is **flow-** and **context-sensitive** and **provably polynomial-time**. To efficiently implement DDPA we develop a novel pushdown automaton metaprogramming framework, the **Pushdown Reachability automaton (PDR)**. The analysis is formalized and proved sound, and an implementation is described.


- Leandro Facchinetti, Zachary Palmer, Scott
  Smith. [Relative Store Fragments for Singleton Abstraction](/projects/demand-driven-program-analysis/papers/relative-store-fragments-for-singleton-abstraction.pdf). 24th Static Analysis Symposium, New York, NY, USA, August 2017.

  Abstract

  : A **singleton abstraction** occurs in a program analysis when some results
    of the analysis are known to be exact: an abstract binding corresponds to a
    single concrete binding.  In this paper, we develop a novel approach to
    constructing singleton abstractions via **relative store fragments**.   Each
    store fragment is a **locally** exact store abstraction in that it contains
    only those abstract variable bindings necessary to address a particular
    question at a particular program point; it is **relative** to that program
    point and the point of view may be shifted.  We show how an analysis
    incorporating relative store fragments achieves flow-, context-, path- and
    must-alias sensitivity, and can be used as a basis for environment analysis,
    without any machinery put in place for those specific aims.  We build upon
    recent advances in **demand-driven** higher-order program analysis to
    achieve this construction as it is fundamentally tied to demand-driven
    lookup of variable values.

- Zachary Palmer, Scott
  Smith. [Higher-Order Demand-Driven Program Analysis](/projects/demand-driven-program-analysis/papers/higher-order-demand-driven-program-analysis.pdf),
  European Conference on Object-Oriented Programming (ECOOP) 2016.
  [Implementation](/projects/demand-driven-program-analysis/artifacts/higher-order-demand-driven-program-analysis.tgz).

  Abstract

  : We explore a novel approach to higher-order program analysis that brings
    ideas of on-demand lookup from first-order CFL-reachability program analyses
    to higher-order programs. The analysis needs to produce only a control-flow
    graph; it can derive all other information including values of variables
    directly from the graph. Several challenges had to be overcome, including
    how to build the control-flow graph on-the-fly and how to deal with
    non-local variables in functions. The resulting analysis is flow- and
    context-sensitive with a provable polynomial-time bound. The analysis is
    formalized and proved correct and terminating, and an initial implementation
    is described.
