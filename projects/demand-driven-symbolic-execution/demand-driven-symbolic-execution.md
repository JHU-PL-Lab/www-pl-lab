---
title: "Demand-Driven Symbolic Execution"
permalink: "/projects/demand-driven-symbolic-execution/"
narrow: true
---

Status

: Active.

Symbolic execution has been an active area of research for almost 50 years. Symbolic **backwards** execution (SBE) is a useful variation on standard forward symbolic evaluation; it allows a symbolic evaluation to start anywhere in the program and proceed by executing **in reverse** to the program start. SBE brings goal-directed reasoning to symbolic evaluation and has proven effective in e.g. automated test generation for imperative languages.

Publications
------------

- Zachary Palmer, Theodore Park, Scott Smith, Shiwei Weng, [Higher-Order Demand-Driven Symbolic Evaluation](/projects/demand-driven-symbolic-execution/papers/icfp20-ddse-full.pdf), Proceedings of the ACM on Programming Languages, Volume 4, Number ICFP, Article 102 (August 2020), 28 pages. [Full](/projects/demand-driven-symbolic-execution/papers/icfp20-ddse-full.pdf). [Artifact](/projects/demand-driven-symbolic-execution/artifacts/artifact09-source-c19e0730b819707df4251ec7ca248b80.tgz).

  Abstract

  : In this paper we define DDSE: a demand-
  driven symbolic evaluator for higher-order functional languages which also propagates constraints backwards. DDSE is a novel SBE which operates on a **functional** as opposed to imperative language, and furthermore it is defined as a direct abstraction of a backwards-executing interpreter. This reverse propagation is similar in spirit to how Dijkstra weakest-preconditions (**wps**) are propagated, and how classic backward program analyses propagate constraints in reverse. The advantage of SBE is the same as any goal-directed reasoning: by focusing on the goal from the start, there are fewer spurious paths taken.
  
    We establish the soundness of DDSE and define a test generation algorithm for this toy language. We report on an initial reference implementation to confirm the correctness of the principles.