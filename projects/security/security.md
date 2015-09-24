---
title: "Secure Language Architectures"
permalink: "/projects/security/"
narrow: true
---

Goal

: The development of secure, programming-language-based access control and
  information flow constructs for statically and dynamic enforcement of security
  guarantees.

Some of the most challenging research problems in computer science in the next
twenty years will be centered around security issues. Security problems arise at
many levels, from cryptographic security to secure network architectures to
secure operating systems architectures. Programming language architectures are
another important layer that must also be secured. The Java JDK now includes a
fairly complete Security Architecture which supports code-based access
control. But, this area is really just beginning, and our goal is to make
fundamental contributions to the programming language security architectures
that eventually become widely established.

Our efforts in this area have been centered around the following topics.

Developing type-based models of security

: Type-based systems give static, declarative security guarantees and so are an
  important level at which to place security policies. Additionally, a static
  security policy requires no run-time overhead of explicit security checks. We
  have developed static type systems corresponding to the Java Security
  Architecture

Type-based models for information flow

: We are focusing on making realistic type-based information flow systems, where
  the flow labels can be completely inferred, and a focus on the I/O boundary as
  the (sole) location where information flow levels should be declared.

Dynamic information flow

: Using ideas from static analysis, we are working on developing run-time
  systems for monitoring information flow. This is a challenging problem due to
  the possibility of indirect leakage of information.

Publications
------------

- Paritosh Shroff and Scott
  F. Smith. [Securing Timing Channels at Runtime](/projects/security/papers/securing-timing-channels-at-runtime.pdf),
  Technical Report, July 2008.

  Abstract

  : We propose a general purpose runtime framework to secure timing
    channels. Our technique supports higher-order function invocations and
    computations looping on secret data, features which none of the existing
    approaches fully allow. We provably eliminate external and internal timing
    channels in both sequential and concurrent settings, in presence of
    deterministic as well as nondeterministic schedulers. There is a price to be
    paid, however – the high computation may have to be disrupted; the low
    computation is nevertheless guaranteed to be unaffected. We illustrate how
    our approach can be realized on standard computing platforms.

- Paritosh Shroff, Scott F. Smith, and Mark
  Thober. [Dynamic Dependency Monitoring to Secure Information Flow](/projects/security/papers/dynamic-dependency-monitoring-to-secure-information-flow.pdf). CSF
  2007: 20th IEEE Computer Security Foundations
  Symposium. [Slides](/projects/security/slides/dynamic-dependency-monitoring-to-secure-information-flow-slides.pdf). [Technical Report](/projects/security/papers/dynamic-dependency-monitoring-to-secure-information-flow-technical-report.pdf). (Best
  Paper Award)

  Abstract

  : Although static systems for information flow security are well-studied, few
    works address run-time information flow monitoring. Run-time information
    flow control offers distinct advantages in precision and in the ability to
    support dynamically defined policies. To this end, we here develop a new
    run-time information flow system based on the run-time tracking of indirect
    dependencies between program points. Our system tracks both direct and
    indirect information flows, and noninterference results are proved.

- Scott F. Smith, and Mark
  Thober. [Improving Usability of Information Flow Security in Java](/projects/security/papers/improving-usability-of-information-flow-security-in-java.pdf). ACM
  SIGPLAN Workshop on Programming Languages and Analysis for Security (PLAS
  2007). [Technical Report](/projects/security/papers/improving-usability-of-information-flow-security-in-java-technical-report.pdf).

  Abstract

  : This paper focuses on improving the usability of information flow type
    systems. We present a static information flow type inference system for
    Middleweight Java (MJ) which automatically infers information flow labels,
    thus avoiding the need for a multitude of program annotations. Additionally,
    policies need only be specified on IO channels, the critical flow
    boundary. Our type system includes a high degree of parametric polymorphism,
    necessary to allow classes to be used in multiple security contexts, and to
    properly distinguish the security policies of different IO channels. We
    prove a noninterference property for programs that interactively input and
    output data. We then describe a mechanism that allows users to define
    top-level policies, which automatically inserts the security policies at the
    proper points in the program. This provides the further benefit that
    whomever is defining the policy does not necessarily need intimate knowledge
    of the program source.

- Scott Smith and Mark
  Thober. [Refactoring Programs to Secure Information Flows](/projects/security/papers/refactoring-programs-to-secure-information-flows.pdf),
  ACM SIGPLAN Workshop on Programming Languages and Analysis for Security
  (PLAS), 2006.

  Abstract

  : Adding a sound information flow security policy to an existing program is a
    difficult task that requires major analysis of and changes to the
    program. In this paper we show how refactoring programs into distinct
    components of high and low security is a useful methodology to aid in the
    production of programs with sound information flow policies. Our methodology
    proceeds as follows. Given a program with no information flow controls, a
    program slicer is used to identify code that depends on high security
    inputs. High security code so identified is then refactored into a separate
    component, which may be accessed by the low security component via public
    method calls. A security policy that labels input data and checks the output
    points can then enforce the desired end-to-end security property. Controlled
    information releases can occur at explicit declassification points if deemed
    safe. The result is a well-engineered program with explicit interfaces
    between components of different security levels.

- Scott Smith and Mark
  Thober. [Securing Data at Java IO Boundaries](/projects/security/papers/securing-data-at-java-io-boundaries.pdf)
  Draft.

  Abstract

  : We present an information flow type system for Featherweight Java, taking a
    programmer-centered view by requiring minimal program annotations, and
    focusing on IO points, the most critical flow boundary. Our static type
    inference system automatically infers information flow labels, thus
    eliminating the need for explicit program annotations. We prove type
    soundness and a noninterference property using an extensible operational
    approach. On top of this system, we provide an analysis that extracts all
    information flowing in and out of the IO points of a program. Global program
    flows can then be observed, and policies can be set to control these
    flows. We argue that controlling data at input and output points is
    ultimately the only data security borders that matter, and our system allows
    programmers to focus on this dimension.

- François Pottier, Christian Skalka and Scott
  Smith. [A Systematic Approach to Static Access Control](/projects/security/papers/a-systematic-approach-to-static-access-control-to-appear.pdf),
  TOPLAS, to appear.

  Abstract

  : The Java Security Architecture includes a dynamic mechanism for enforcing
    access control checks, the so-called stack inspection process. While the
    architecture has several appealing features, access control checks are all
    implemented via dynamic method calls. This is a highly non-declarative form
    of specification which is hard to read, and which leads to additional
    run-time overhead. This paper develops type systems which can statically
    guarantee the success of these checks. Our systems allow security properties
    of programs to be clearly expressed within the types themselves, which thus
    serve as static declarations of the security policy. We develop these
    systems using a systematic methodology: we show that the security-passing
    style translation, proposed by Wallach, Appel and Felten as a dynamic
    implementation technique, also gives rise to static security-aware type
    systems, by composition with conventional type systems. To define the
    latter, we use the general HM(X) framework, and easily construct several
    constraint- and unification-based type systems.

- Christian Skalka and Scott
  Smith. [History Effects and Verification](/projects/security/papers/history-effects-and-verification.pdf). In
  Asian Programming Languages Symposium, November 2004.

  Abstract

  : Trace effects are statically generated program abstractions, that can be
    model checked for verification of assertions in a temporal program logic. In
    this paper we develop a type and effect analysis for obtaining trace effects
    of Object Oriented programs in Featherweight Java. We observe that the
    analysis is significantly complicated by the interaction of trace behavior
    with inheritance and other Object Oriented features, particularly overridden
    methods, dynamic dispatch, and downcasting. We propose an expressive type
    and effect inference algorithm combining polymorphism and
    subtyping/subeffecting constraints to obtain a flexible trace effect
    analysis in this setting, and show how these techniques are applicable to
    Object Oriented features.

- Christian Skalka, Scott Smith, and David Van
  Horn. [A Type and Effect System for Flexible Abstract Interpretation of Java](/projects/security/papers/a-type-and-effect-system-for-flexible-abstract-interpretation-of-java.pdf). In
  Proceedings of the ACM Workshop on Abstract Interpretation of Object Oriented
  Languages, Electronic Notes in Theoretical Computer Science, January 2005.

  Abstract

  : This paper describes a flexible type and effect inference system for
    Featherweight Java (FJ). The effect terms generated by static type and
    effect inference embody the abstract interpretation of program event
    sequences. Flexibility in the analysis is obtained by post-processing of
    inferred effects, allowing a modular adaptation to extensions of the
    language. Several example transformations are discussed, including how
    inferred effects can be transformed to reflect the impact of exceptions on
    FJ control flow.

- Christian Skalka and Scott
  Smith. [Set Types and Applications](/projects/security/papers/set-types-and-applications.pdf),
  Worskop on Types in Programming (TIP02). Electronic Notes in Theoretical
  Computer Science, 75, 2003.

  Abstract

  : We present pml, a programming language that includes primitive sets and
    associated operations. The language is equipped with a precise type
    discipline that statically captures dynamic properties of sets, allowing
    runtime optimizations. We demonstrate the utility of pmlB by showing how it
    can serve as a practical implementation language for higher-level
    programming language based security systems, and characterize pml by
    comparing the expressiveness of pmlB sets with enumerations.

- Christian Skalka and Scott
  Smith. [Static Use-Based Object Confinement](/projects/security/papers/static-use-based-object-confinement.pdf),
  Workshop on Foundations of Computer Security
  (FCS02). [Full version](/projects/security/papers/static-use-based-object-confinement-full-version.pdf) appearing in Springer
  International Journal of Information Security, 4(1-2), 2005.

  Abstract

  : The confinement of object references is a significant security concern for
    modern programming languages. We define a language that serves as a uniform
    model for a variety of confined object reference systems. A use-based
    approach to confinement is adopted, which we argue is more expressive than
    previous communication-based approaches. We then develop a readable,
    expressive type system for static analysis of the language, along with a
    type safety result demonstrating that run-time checks can be eliminated. The
    language and type system thus serve as a reliable, declarative and efficient
    foundation for secure capability-based programming and object confinement.

- François Pottier, Christian Skalka, and Scott
  Smith. [A Systematic Approach to Static Access Control](/projects/security/papers/a-systematic-approach-to-static-access-control-2001.pdf). European
  Symposium on Programming (ESOP) 2001, April 2001.

  Abstract

  : The Java JDK 1.2 Security Architecture includes a dynamic mechanism for
    enforcing access control checks, so-called stack inspection. This paper
    studies type systems which can statically guarantee the success of these
    checks. We develop these systems using a new, systematic methodology: we
    show that the security-passing style translation, proposed by Wallach and
    Felten as a dynamic implementation technique, also gives rise to static
    security-aware type systems, by composition with conventional type
    systems. To define the latter, we use the general HM(X) framework, and
    easily construct several constraint- and unification-based type
    systems. They offer significant improvements on a previous type system for
    JDK access control, both in terms of expressiveness and in terms of
    readability of inferred type specifications.

- Christian Skalka and Scott
  Smith. [Static Enforcement of Security with Types](/projects/security/papers/static-enforcement-of-security-with-types.pdf),
  2000 International Conference on Functional Programming (ICFP00), September
  2000.

  Abstract

  : A number of security systems for programming languages have recently
    appeared, including systems for enforcing some form of access control. The
    Java JDK 1.2 security architecture is one such system that is widely studied
    and used. While the architecture has many appealing features, access control
    checks are all implemented via dynamic method calls. This is a highly
    non-declarative form of specification which is hard to read, and which leads
    to additional run-time overhead. In this paper, we present a novel security
    type system that enforces the same security guarantees as Java Stack
    Inspection, but via a static type system with no additional run-time
    checks. The system allows security properties of programs to be clearly
    expressed within the types themselves. We also define and prove correct an
    inference algorithm for security types, meaning that the system has the
    potential to be layered on top of the existing Java architecture, without
    requiring new syntax.
