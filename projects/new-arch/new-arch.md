---
title: "Rethinking Language Architectures in the New Century"
permalink: "/projects/new-arch/"
narrow: true
---


This ongoing project aims to combine several dimensions of programming language
technology into an infrastructure to better support the recent trends in
software development:

- Interactions between different parts of one application are increasingly
  complex, which poses challenges on the design of encapsulated entities, such
  as modules, components and objects, to model these interactions.

- Software is increasingly developed collaboratively, and runs distributedly.

- Software project management has become increasingly complex, with intertwined
  goals and stages spanning from separate compilation, static linking, version
  control and dynamic updating.

- Security is a crucial concern in an environment lacking of universal trust.

- New application domains, such as sensor networks, are not particularly
  well-supported by traditional language models.

A general thread of the _Ab Initio_ project is to design well-encapuslated
programming entities to best facilate their ability to interact in diversified
fashions, such as static linking, dynamic linking and cross-computation
communications. We have designed _Cells_ for component programming,
_Assemblages_ for module systems, and _Classages_ for object-oriented
programming. This project is now a collaboration between JHU and SUNY
Binghamton.

Publications
------------

- Yu David Liu, Scott
  Smith. [Pedigree Types](/projects/new-arch/papers/pedigree-types.pdf). International
  Workshop on Aliasing, Confinement and Ownership in Object-Oriented Programming
  (IWACO). Paphos,
  Cyprus. July 2008. [Slides](/projects/new-arch/slides/pedigree-types-slides.ppt).

  Abstract

  : _Pedigree Types_ are an intuitive ownership type system requiring minimal
    programmer annotations. Reusing the vocabulary of human genealogy, Pedigree
    Types programmers can qualify any object reference with a pedigree -- a
    **child**, **sibling**, **parent**, **grandparent**, etc -- to indicate what
    relationship the object being referred to has with the referant on the
    standard ownership tree, following the owners-as-dominators convention. Such
    a qualifier serves as a heap shape constraint that must hold at run time and
    is enforced statically. Pedigree **child** captures the intention of
    encapsulation, _i.e._ ownership: the modified object reference is ensured
    not to escape the boundary of its parent. Among existing ownership type
    systems, Pedigree Types are closest to _Universe Types_. The former can be
    viewed as extending the latter with a more general form of pedigree
    modifiers, so that the relationship between any pair of objects on the
    aforementioned ownership tree can be named and -- more importantly --
    inferred. We use a constraint-based type system which is proved sound via
    subject reduction. Other technical originalities include a polymorphic
    treatment of pedigrees not explicitly specified by programmers, and use of
    linear diophantine equations in type constraints to enforce the hierarchy.

- Yu David Liu and Scott
  Smith. [A Formal Framework for Component Deployment](/projects/new-arch/papers/a-formal-framework-for-component-deployment.pdf). In
  Proceedings of the 21st Conference on Object-Oriented Programming, Systems,
  Languages and Applications (OOPSLA'06). Portland, Oregon, USA,
  October 2006. [Slides](/projects/new-arch/slides/a-formal-framework-for-component-deployment-slides.pdf).

  Abstract

  : Software deployment is a complex process, and industrial-strength frameworks
    such as .NET, Java, and CORBA all provide explicit support for component
    deployment. However, these frameworks are not built around fundamental
    principles as much as they are engineering efforts closely tied to
    particulars of the respective systems. Here we aim to elucidate the
    fundamental principles of software deployment, in a platform-independent
    manner. Issues that need to be addressed include deployment unit design,
    _when_, _where_ and _how_ to wire components together, versioning, version
    dependencies, and hot-deployment of components. We define the _application
    buildbox_ as the place where software is developed and deployed, and define
    a formal Labelled Transition System (LTS) on the buildbox with transitions
    for deployment operations that include build, install, ship, and update. We
    establish formal properties of the LTS, including the fact that if a
    component is shipped with a certain version dependency, then at run time
    that dependency must be satisfied with a compatible version. Our treatment
    of deployment is both platform- and vendor-independent, and we show how it
    models the core mechanisms of the industrial-strength deployment frameworks.

- Xiaoqi Lu and Scott
  Smith. [A Microkernel Virtual Machine: Building Security with Clear Interfaces](/projects/new-arch/papers/a-microkernel-virtual-machine.pdf). In
  PLAS 2006, Ottawa, Ontario,
  Canada. [Slides](/projects/new-arch/slides/a-microkernel-virtual-machine-slides.ppt).

  Abstract

  : In this paper we propose a novel microkernel-based virtual machine (µKVM), a
    new code-based security framework with a simple and declarative security
    architecture. The main design goals of the µKVM are to put a clear,
    inviolable programming interface between different codebases or security
    components, and to limit the size of the trusted codebase in the spirit of a
    microkernel. Security policies are enforced solely on the interface because
    all data must explicitly pass through the inviolable interface. The
    architecture of the µKVM effectively removes the need for expensive runtime
    stack inspection, and applies the principle of least privilege to both
    library and application code elegantly and efficiently. We have implemented
    a prototype of the proposed µKVM. A series of benchmarks show that the
    prototype preserves the original functionality of Java and compares
    favorably with the J2SDK performance-wise.

- Yu David Liu and Scott Smith. [Interaction-Based Programming with Classages](/projects/new-arch/papers/interaction-based-programming-with-classages.pdf). In
  Proceedings of the 20th Conference on Object-Oriented Programming, Systems,
  Languages and Applications (OOPSLA'05), San Diego, California, USA,
  October 2005. [Slides](/projects/new-arch/slides/interaction-based-programming-with-classages-slides.pdf).

  Abstract

  : This paper presents _Classages_, a novel interaction-centric object-oriented
    language. Classes and objects in _Classages_ are fully encapsulated, with
    explicit interfaces for all interactions they might be involved in. The
    design of _Classages_ touches upon a wide range of language design topics,
    including encapsulation, object relationship representation, and object
    confinement. An encoding of Java's OO model in _Classages_ is provided,
    showing how standard paradigms are supported. A prototype _Classages_
    compiler is described.

- Yu David Liu and Scott
  Smith. [Modules with Interfaces for Dynamic Linking and Communication](/projects/new-arch/papers/modules-with-interfaces-for-dynamic-linking-and-communication.pdf). In
  Proceedings of the 18th European Conference on Object-Oriented Programming
  (ECOOP'04), Oslo, Norway,
  June 2004. [Slides](/projects/new-arch/slides/modules-with-interfaces-for-dynamic-linking-and-communication-slides.pdf).

  Abstract

  : Module systems are well known as a means for giving clear interfaces for the
    static linking of code. This paper shows how adding explicit interfaces to
    modules for 1) dynamic linking and 2) cross-computation communication can
    increase the declarative nature of modules, and build a stronger foundation
    for language-based security and version control. We term these new modules
    _Assemblages_. We additionally develop a sound constraint-based type system
    particularly suited to a module system supporting bounded type
    parametricity, cross-module type recursion, and polymorphic type binding
    during dynamic linking and cross-computation communication.

- Ran Rinat and Scott
  Smith. [Modular Internet Programming with Cells](/projects/new-arch/papers/modular-internet-programming-with-cells.pdf). In
  Proceedings of the 16th European Conference on Object-Oriented Programming
  (ECOOP'02), Málaga, Spain, June 2002. [Slides](/projects/new-arch/slides/modular-internet-programming-with-cells-slides.pdf).

  Abstract

  : The success of Java in recent years is largely due to its targeting as a
    language for the Internet. Many of the network-related features of Java
    however are not part of the core language design. In this paper we focus on
    the design of a more parsimonious Internet programming language, which
    supports network integration smoothly and coherently as part of its core
    specification. The key idea is to center these extensions around the unified
    notion of a _cell_. Cells are deployable containers of objects and code,
    which may import (_plugin_) and export (_plugout_) classes and
    operations. They may be dynamically linked and unlinked, locally or across
    the network. Cells may be dynamically loaded, unloaded, copied, and moved,
    and serve as units of security. At first approximation, cells can be thought
    of as a hybrid between modules and components. Here we concentrate on the
    design of _JCells_, a language which builds cells on top of the fundamental
    Java notions of class, object, and virtual machine.

- Yu David Liu and Scott
  Smith. [A Component Security Infrastructure](/projects/new-arch/papers/a-component-security-infrastructure.pdf). Foundations
  of Computer Security (FCS'02), Copenhagen, Denmark,
  July 2002. [Slides](/projects/new-arch/slides/a-component-security-infrastructure-slides.pdf).

  Abstract

  : This paper defines a security infrastructure for access control at the
    component level of programming language design. Distributed components are
    an ideal place to define and enforce significant security policies, because
    components are large entities that often define the political boundaries of
    computation. Also, rather than building a security infrastructure from
    scratch, we build on a standard one, the SDSI/SPKI security infrastructure.

- Ran Rinat and Scott
  Smith. [The Cell Project: Component Technology for the Internet](/projects/new-arch/papers/the-cell-project-2001-10.pdf). Proceedings
  of the 1st Workshop on Language Mechanisms for Programming Software
  Components, October 2001.

- Ran Rinat and Scott
  Smith. [The Cell Project: Component Technology for the Internet](/projects/new-arch/papers/the-cell-project-2001-06.pdf). Proceedings
  of the 6th Workshop on Component-Oriented Programming, Budapest, Hungary, June
  2001.

Drafts
------

- Yu David Liu and Scott Smith and Andreas
  Terzis. [A High-level Language for Sensor Networks](/projects/new-arch/papers/a-high-level-language-for-sensor-networks.pdf).

  Abstract

  : In this paper we describe _Ensemble_, a proposed language framework for
    sensor network programming. Our goal is to provide a programming framework
    to scientists and engineers that will allow them to directly code sensor
    network applications, without the need for expertise in low-level device
    programming. The key concepts in _Ensemble_ are high-level communication
    protocol _connectors_, and the ability for systems programmers to define new
    communication protocols as _metaprotocol_ extensions.

- Xiaoqi Lu and Scott
  Smith. [A Secure Microkernel Virtual Machine](/projects/new-arch/papers/a-secure-microkernel-virtual-machine.pdf).

  Abstract

  : In this paper, we develop a novel microkernel-based virtual machine, the
    μKVM. It is a microkernel architecture because the size of the trusted
    system codebase is greatly reduced in comparison to VM's such as the Java
    Virtual Machine. The μKVM kernel manages sensitive resources such as I/O,
    and implements a minimal set of low-level system operations. System
    libraries are implemented outside the kernel, and run in user mode. All
    interactions between the kernel and applications are declared on explicit
    interfaces, and security policies are also enforced at these interfaces. We
    test our architecture in a μKVM prototype developed for Java and show how
    the microkernel architecture supports the existing functionality of the
    J2SDK. The prototype is benchmarked, and the results show that our
    implementation compares favorably with the J2SDK and so the architecture
    does not appear to be a burden on running time.

- Yu David Liu and Ran Rinat and Scott
  Smith. [Component Assemblies and Component Runtimes](/projects/new-arch/papers/component-assemblies-and-component-runtimes.pdf).

  Abstract

  : This paper proposes a component programming language that supports an
    integrated notion of both compile-time and run-time component. The
    centerpiece of this paper is the static, compile time notion of _assembly_,
    complementing our previous work on the dynamic, runtime notion of _cell_. An
    assembly is a declarative, stateless piece of code that facilitates code
    combination. It offers explicit typed interfaces to outsiders, called
    _linkers_, which can be used to link smaller assemblies into bigger,
    compound assemblies. Each assembly may in turn be _loaded_ at run-time,
    producing a cell in the runtime environment. A cell is a dynamic, stateful
    component that interacts with other cells via explicit runtime
    interfaces. Thus, the static assemblies and the dynamic cells are fully
    integrated.
