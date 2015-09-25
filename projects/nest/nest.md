---
title: "NesT: Staged Programming For Sensor Networks"
permalink: "/projects/nest/"
narrow: true
---

Status

: Inactive.

Our new NesT project ("improved NesC/TinyOS", _not_ a refreshing cold beverage)
aims to simultaneously improve the efficiency (in terms of power consumption and
memory usage) as well as programmability of sensor network applications, or in
general any program requiring an incredibly small footprint to run in. At this
point we have developed the theoretical ideas in a small ML-like staged
programming language, \<ML\>. This project is a joint collaboration with
University of Vermont and SUNY Binghamton.

Publications
------------

- Yu David Liu, Christian Skalka, and Scott
  Smith. [Type-Specialized Staged Programming with Process Separation](/projects/nest/papers/type-specialized-staged-programming-with-process-separation.pdf). Workshop
  on Generic Programming, Edinburgh, Scotland, 2009. [Slides](/projects/nest/slides/type-specialized-staged-programming-with-process-separation-slides.pptx).

  Abstract

  : Staging is a powerful language construct that allows a program at one stage
    to manipulate and specialize a program at the next. We propose <ML> as a new
    staged calculus designed with novel features for staged programming in
    modern computing platforms such as embedded systems. A distinguishing
    feature of <ML> is a model of process separation, whereby different stages
    of computation are executed in different process spaces. Our language also
    supports dynamic type specialization, via type abstraction, dynamic type
    construction, and a limited form of type dependence. <ML> is endowed with a
    largely standard metatheory, including type preservation and type safety
    results. We discuss the utility of our language via code examples from the
    domain of wireless sensor network programming.
