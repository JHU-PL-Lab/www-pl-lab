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

- Zachary Palmer, Scott
  Smith. [Higher-Order Demand-Driven Program Analysis](/projects/demand-driven-program-analysis/papers/higher-order-demand-driven-program-analysis.pdf).
  Draft, March 2016.
  [Implementation](https://github.com/JHU-PL-Lab/odefa-proof-of-concept). ([Draft, November 2015](/projects/demand-driven-program-analysis/papers/control-based-program-analysis.pdf).)

  Abstract

  : We explore a novel approach to higher-order program analysis that brings
    ideas of on-demand lookup from first-order CFL-reachability program analyses
    to higher-order programs. The analysis needs to produce only a control-flow
    graph; it can derive all other information including values of variables
    directly from the graph. Several challenges had to be overcome, including
    how to build the control-flow graph on-the-fly and how to deal with nonlocal
    variables in functions. The resulting analysis is flow- and
    context-sensitive with a provable polynomial-time bound. The analysis is
    formalized and proved correct and terminating, and an initial implementation
    is described.
