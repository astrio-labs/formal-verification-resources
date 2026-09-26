<p align="center">
  <img src="cover.png" width="100%">
</p>

# Formal Verification Resources

A curated resource list for learning formal verification across software, mathematics, and hardware.

The list first covers verification techniques, from automatic model checking and solvers to interactive proof, and then applies them to mathematics, software systems, and hardware. AI-assisted verification is collected separately under Frontier. Read **Start here** first. After that, use it as a reference.

The core list uses original papers, official specifications and documentation, project repositories, and direct implementation work.

## Contents

- [Start here, the minimum mental model](#start-here-the-minimum-mental-model)
- [1. Specifications and model checking](#1-specifications-and-model-checking)
  - [TLA+ and PlusCal](#tla-and-pluscal)
  - [Alloy](#alloy)
  - [Model checking algorithms](#model-checking-algorithms)
- [2. SAT and SMT](#2-sat-and-smt)
  - [SAT](#sat)
  - [SMT](#smt)
- [3. Program verification](#3-program-verification)
  - [Program logics](#program-logics)
  - [Contracts and invariants](#contracts-and-invariants)
  - [Rust and C](#rust-and-c)
- [4. Proof assistants](#4-proof-assistants)
  - [Lean](#lean)
  - [Rocq](#rocq)
  - [Isabelle](#isabelle)
- [5. Formalized mathematics](#5-formalized-mathematics)
  - [Background](#background)
  - [Libraries](#libraries)
  - [Landmark theorems](#landmark-theorems)
  - [Research mathematics](#research-mathematics)
- [6. Verified systems](#6-verified-systems)
  - [Kernels](#kernels)
  - [Compilers](#compilers)
  - [Distributed systems](#distributed-systems)
- [7. Hardware verification](#7-hardware-verification)
  - [RTL](#rtl)
  - [Instruction sets](#instruction-sets)
- [Frontier](#frontier)
  - [Frontier labs](#frontier-labs)
  - [Other work](#other-work)
- [Source policy](#source-policy)

## Start here, the minimum mental model

Read these in order if you are new to the field.

1. [How Amazon Web Services Uses Formal Methods](https://cdn.amazon.science/67/f9/92733d574c11ba1a11bd08bfb8ae/how-amazon-web-services-uses-formal-methods.pdf) - Specifications and model checking at AWS.
2. [Model Checking: Algorithmic Verification and Debugging](https://dl.acm.org/doi/10.1145/1592761.1592781) - State spaces, temporal properties, counterexamples, and state explosion.
3. [Satisfiability Modulo Theories: An Appetizer](https://leodemoura.github.io/files/sbmf09.pdf) - How SMT solvers decide formulas over theories.
4. [An Axiomatic Basis for Computer Programming](https://dl.acm.org/doi/10.1145/363235.363259) - Hoare triples and proof rules for program correctness.
5. [Dafny: An Automatic Program Verifier for Functional Correctness](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/12/krml203.pdf) - Contracts and invariants checked automatically through SMT.
6. [Propositions as Types](https://homepages.inf.ed.ac.uk/wadler/papers/propositions-as-types/propositions-as-types.pdf) - The correspondence between proofs and programs.
7. [Theorem Proving in Lean 4](https://lean-lang.org/theorem_proving_in_lean4/) - Dependent type theory, inductive types, and tactics in Lean.
8. [seL4: Formal Verification of an OS Kernel](https://sel4.org/Research/pdfs/sel4-formal-verification-os-kernel.pdf) - Kernel correctness from abstract specification to C.

For a practical companion, work through [Functional Programming in Lean](https://lean-lang.org/functional_programming_in_lean/).

## 1. Specifications and model checking

### TLA+ and PlusCal

- [Learn TLA+: Conceptual Overview](https://learntla.com/intro/conceptual-overview.html) - Why specifications and model checking matter.
- [The PlusCal Algorithm Language](https://lamport.azurewebsites.net/pubs/pluscal.pdf) - Pseudocode-like algorithms that translate to TLA+.
- [Model Checking TLA+ Specifications](https://lamport.azurewebsites.net/pubs/yuanyu-model-checking.pdf) - How the TLC model checker explores states.
- [The Temporal Logic of Actions](https://lamport.org/pubs/lamport-actions.pdf) - The logic behind TLA+.
- [TLA+ Examples](https://github.com/tlaplus/Examples) - Specifications of algorithms and distributed protocols.

### Alloy

- [Alloy: A Language and Tool for Exploring Software Designs](https://cacm.acm.org/research/alloy/) - An introduction to Alloy.
- [Practical Alloy: Structural modeling](https://practicalalloy.github.io/chapters/structural-modeling/index.html) - Signatures, fields, constraints, and assertions.
- [Practical Alloy: Behavioral modeling](https://practicalalloy.github.io/chapters/behavioral-modeling/index.html) - Mutable state, actions, and properties over traces.
- [Using Lightweight Modeling To Understand Chord](https://www.pamelazave.com/chord-ccr.pdf) - Alloy shows no published version of Chord is correct.

### Model checking algorithms

- [An Automata-Theoretic Approach to Linear Temporal Logic](https://www.cs.rice.edu/~vardi/papers/banff94rj.pdf) - LTL, and how model checkers check it with automata.
- [The Model Checker SPIN](https://spinroot.com/spin/Doc/ieee97.pdf) - Explicit-state LTL checking with partial-order reduction.
- [Symbolic Model Checking without BDDs](https://fmv.jku.at/papers/BiereCimattiClarkeZhu-TACAS99.pdf) - Bounded model checking with SAT solvers.
- [Understanding IC3](https://theory.stanford.edu/~arbrad/papers/Understanding_IC3.pdf) - How IC3 builds inductive invariants.

## 2. SAT and SMT

### SAT

- [Chaff: Engineering an Efficient SAT Solver](https://www.princeton.edu/~chaff/publication/DAC2001v56.pdf) - Watched literals and VSIDS branching for CDCL solvers.
- [An Extensible SAT-solver](http://minisat.se/downloads/MiniSat.pdf) - MiniSat's clause-learning design and implementation.

### SMT

- [Satisfiability Modulo Theories: A Beginner's Tutorial](https://cvc5.github.io/tutorials/beginners/) - SMT foundations, theories, models, and proofs.
- [Solving SAT and SAT Modulo Theories: from an Abstract Davis-Putnam-Logemann-Loveland Procedure to DPLL(T)](https://homepage.cs.uiowa.edu/~tinelli/papers/NieOT-JACM-06.pdf) - Combining a SAT engine with theory solvers.
- [Programming Z3](https://z3prover.github.io/papers/programmingz3.html) - Z3's APIs, theories, and problem encodings.
- [Efficient E-matching for SMT Solvers](https://leodemoura.github.io/files/ematching.pdf) - Quantifier instantiation through trigger patterns.

## 3. Program verification

### Program logics

- [Hoare Logic, Part I](https://softwarefoundations.cis.upenn.edu/plf-current/Hoare.html) - Hoare triples and proof rules in Rocq.
- [Guarded commands, non-determinacy and formal derivation of programs](https://www.cs.utexas.edu/~EWD/ewd04xx/EWD472.PDF) - Dijkstra's weakest-precondition calculus.
- [Separation Logic: A Logic for Shared Mutable Data Structures](https://www.cs.cmu.edu/~jcr/seplogic.pdf) - Separating conjunction and the frame rule for pointer programs.
- [Separation Logic](https://discovery.ucl.ac.uk/10075346/1/O%27Hearn_AAM_sl-cacm-cameraready.pdf) - Local reasoning, concurrency, and the Infer analyzer.

### Contracts and invariants

- [Getting Started with Dafny: A Guide](https://dafny.org/latest/OnlineTutorial/guide) - Contracts, loop invariants, termination, and framing in Dafny.
- [Interfacing with an SMT solver](https://fstar-lang.org/tutorial/book/part1/part1_prop_assertions.html) - How F* sends propositions and refinement types to SMT.
- [Viper: A Verification Infrastructure for Permission-Based Reasoning](https://pm.inf.ethz.ch/publications/MuellerSchwerhoffSummers16.pdf) - An intermediate verification language with built-in permissions.

### Rust and C

- [Verus: Verifying Rust Programs using Linear Ghost Types (extended version)](https://arxiv.org/abs/2303.05491) - SMT-based verification for Rust.
- [Verus guide: forall and triggers](https://verus-lang.github.io/verus/guide/forall.html) - Choosing triggers for quantifiers in Verus.
- [Kani](https://model-checking.github.io/kani/tutorial-first-steps.html) - Bounded model checking for Rust.
- [CBMC: The C Bounded Model Checker](https://arxiv.org/abs/2302.02384) - Bounded model checking for C.
- [Frama-C](https://frama-c.com/) - Contracts, proofs, and static analysis for C.

## 4. Proof assistants

### Lean

- [Natural Number Game](https://adam.math.hhu.de/#/g/leanprover-community/nng4) - Natural numbers and induction, in a browser game.
- [The Lean 4 Theorem Prover and Programming Language (System Description)](https://lean-lang.org/papers/lean4.pdf) - Lean 4's extensibility, metaprogramming, and implementation.
- [Lean4Lean: Verifying a Typechecker for Lean, in Lean](https://arxiv.org/abs/2403.14064) - An independent Lean kernel, partly verified in Lean.

### Rocq

- [Functional Programming in Rocq](https://softwarefoundations.cis.upenn.edu/lf-current/Basics.html) - Data types, functions, and first proofs in Rocq.
- [The Curry-Howard Correspondence](https://softwarefoundations.cis.upenn.edu/lf-current/ProofObjects.html) - Proofs as programs, and logic as inductive types.

### Isabelle

- [Programming and Proving in Isabelle/HOL](https://isabelle.in.tum.de/doc/prog-prove.pdf) - Higher-order logic, induction, automation, and Isar proofs.
- [Hammering towards QED](https://jfr.unibo.it/article/view/4593) - How hammers like Sledgehammer call external provers.

## 5. Formalized mathematics

### Background

- [The Proof in the Code: How a Truth Machine Is Transforming Math and AI](https://www.quantabooks.org/books/the-proof-in-the-code/) - A paid book on how Lean came to verify mathematics.

### Libraries

- [The Lean mathematical library](https://arxiv.org/abs/1910.09336) - Mathlib's design, structures, automation, and community.
- [Hierarchy Builder: Algebraic hierarchies Made Easy in Coq with Elpi (System Description)](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSCD.2020.34) - Declaring algebraic hierarchies in Coq.
- [Archive of Formal Proofs](https://isa-afp.org/) - Refereed Isabelle proof developments.
- [Lean formalization of Analysis I](https://github.com/teorth/analysis) - Tao's analysis textbook in Lean.

### Landmark theorems

- [Formal Proof—The Four-Color Theorem](https://www.ams.org/notices/200811/tx081101382p.pdf) - The Four Color Theorem, checked in Coq.
- [A formal proof of the Kepler conjecture](https://arxiv.org/abs/1501.02155) - The Kepler conjecture, checked in HOL Light and Isabelle.

### Research mathematics

- [Liquid Tensor Experiment](https://github.com/leanprover-community/lean-liquid) - Scholze's condensed-mathematics challenge, verified in Lean 3.
- [The Polynomial Freiman-Ruzsa Conjecture](https://github.com/teorth/pfr) - The PFR conjecture proof in Lean.
- [The Equational Theories Project: Advancing Collaborative Mathematical Research at Scale](https://arxiv.org/abs/2512.07087) - Implications among magma laws, all checked in Lean.

## 6. Verified systems

### Kernels

- [Comprehensive Formal Verification of an OS Microkernel](https://sel4.systems/Research/pdfs/comprehensive-formal-verification-os-microkernel.pdf) - seL4 proofs for binary code, security, and timing.
- [seL4 proofs](https://sel4.systems/Verification/proofs.html) - What is proved, and for which configurations.
- [Hyperkernel: Push-Button Verification of an OS Kernel](https://unsat.cs.washington.edu/papers/nelson-hyperkernel.pdf) - Push-button kernel verification with Z3.
- [CertiKOS: An Extensible Architecture for Building Certified Concurrent OS Kernels](https://www.usenix.org/system/files/conference/osdi16/osdi16-gu.pdf) - A concurrent kernel verified in Coq.

### Compilers

- [Formal verification of a realistic compiler](https://xavierleroy.org/publi/compcert-CACM.pdf) - CompCert, a C compiler proved correct in Coq.
- [Finding and Understanding Bugs in C Compilers](https://users.cs.utah.edu/~regehr/papers/pldi11-preprint.pdf) - Random compiler testing that spared CompCert's verified core.
- [CakeML: A Verified Implementation of ML](https://cakeml.org/popl14.pdf) - An end-to-end verified ML implementation in HOL4.
- [Alive2: Bounded Translation Validation for LLVM](https://users.cs.utah.edu/~regehr/alive2-pldi21.pdf) - SMT-based translation validation for LLVM optimizations.

### Distributed systems

- [IronFleet: Proving Practical Distributed Systems Correct](https://www.andrew.cmu.edu/user/bparno/papers/ironfleet.pdf) - Verified Paxos and a key-value store in Dafny.
- [Verdi: A Framework for Implementing and Formally Verifying Distributed Systems](https://homes.cs.washington.edu/~ztatlock/pubs/verdi-wilcox-pldi15.pdf) - Distributed systems in Coq, including Raft.
- [Using Lightweight Formal Methods to Validate a Key-Value Storage Node in Amazon S3](https://www.cs.utexas.edu/~bornholt/papers/shardstore-sosp21.pdf) - Reference models, property-based testing, and model checking in production.

## 7. Hardware verification

### RTL

- [SBY / SymbiYosys](https://yosyshq.readthedocs.io/projects/sby/en/latest/quickstart.html) - Hardware assertions, bounded checks, induction, and counterexamples.
- [My first experience with Formal Methods](https://zipcpu.com/blog/2017/10/19/formal-intro.html) - Formal tools finding bugs in a long-used FIFO.
- [OpenTitan assertions](https://opentitan.org/book/hw/formal/index.html) - SystemVerilog assertions in an open-source chip project.

### Instruction sets

- [ISA Semantics for ARMv8-A, RISC-V, and CHERI-MIPS](https://www.cl.cam.ac.uk/users/pes20/sail/sail-popl2019.pdf) - Sail ISA models with emulators and prover definitions.
- [End-to-End Verification of ARM Processors with ISA-Formal](https://alastairreid.github.io/papers/cav2016_isa_formal.pdf) - Arm's bounded model checking of processors against its ISA.
- [riscv-formal](https://github.com/YosysHQ/riscv-formal) - RISC-V instruction checks through the RVFI interface.

## Frontier

This section covers AI-assisted proof generation.

### Frontier labs

- [Olympiad-level formal mathematical reasoning with reinforcement learning](https://www.nature.com/articles/s41586-025-09833-y) - Google DeepMind's AlphaProof.
- [On the Navier–Stokes Millennium Prize Problem](https://openai.com/index/navier-stokes-solution/) - OpenAI's claimed Navier–Stokes proof.
- [Formalizing Fermat's Last Theorem](https://www.anthropic.com/research/formalizing-fermats-last-theorem) - Anthropic's Lean proof of Fermat's Last Theorem.
- [DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition](https://arxiv.org/abs/2504.21801) - DeepSeek's open-weight Lean prover.
- [Leanstral 1.5: Proof Abundance for All](https://mistral.ai/news/leanstral-1-5/) - Mistral's open-weight Lean prover.

### Other work

- [Aristotle: IMO-level Automated Theorem Proving](https://arxiv.org/abs/2510.01346) - Harmonic's Lean prover.
- [Seed-Prover 1.5: Mastering Undergraduate-Level Theorem Proving via Learning from Experience](https://arxiv.org/abs/2512.17260) - ByteDance Seed's Lean prover.
- [Kimina-Prover Preview: Towards Large Formal Reasoning Models with Reinforcement Learning](https://arxiv.org/abs/2504.11354) - Numina and Kimi's Lean prover.
- [A Minimal Agent for Automated Theorem Proving](https://arxiv.org/abs/2602.24273) - A simple baseline prover agent.
- [Prove2Me: An Open Collaborative Platform for Scaling Math Formalization](https://arxiv.org/abs/2608.28433) - AI agents building Lean proofs together.

## Source policy

Core entries are original papers, official specifications or documentation, implementation repositories, or technical accounts by the people who did the work.

Verification claims need the property, checked artifact, assumptions, and proof scope. AI benchmark comparisons also need the toolchain, evaluation protocol, and search budget.

See [CONTRIBUTING.md](CONTRIBUTING.md) for additions and corrections.

Inspired by [Wafer's GPU performance engineering resources](https://github.com/wafer-ai/gpu-perf-engineering-resources).

## License

[MIT](LICENSE)
