# Requirements Engineering

### What is RE?

Cooperative, iterative, and incremental *process* to ensure:
- Specifications exist at the required level of detail
- Agreement is achieved between stakeholders

???
"Requirements engineering is the branch of software engineering concerned with the *real-world goals for functions of and constraints on software systems*. It is also concerned with the relationship of these factors to precise *specifications* of software behavior, and to their *evolution* over time and across software families."
(Pamela Zave: Classification of Research Efforts in Requirements Engineering. ACM Comput. Surv. 29(4): 315-321 (1997))

"Requirements engineering is a *cooperative, iterative, and incremental process* which aims to ensure that: (1) All relevant requirements are explicitly known and understood at the required level of detail; (2) Sufficient agreement about the system requirements is achieved between the stakeholders involved; (3) All requirements are documented and specified in compliance with the relevant documentation/specification formats and rules."
(Klaus Pohl. Requirements Engineering. Springer 2010)

---

Why RE?

- The hardest single part of building a software
system is deciding precisely what to build.
- No other part of the work so cripples
the resulting system if done wrong.
- No other part is more difficult to rectify later.


You cannot build the right product
unless you know precisely:
what the product is intended to do, and
how the product’s success is to be measured.


---

Job of a RE
- Identify the critical stakeholders and their needs:
  – Minimum benefits from using the system
  – Maximum acceptable cost
- Determining a set of software requirements that when satisfied will meet stakeholder’s goals


???
Example of benefits
the technical,
• economic,
• service and
• social

---

Example of requirements:

Show:
the list of students enrolled in a course,
sorted by name,
in less than 1 second,
in an Excel document.
(functionality)
(quality)
(constraint)


project/design/etc. constraints


---

A requirement MUST BE


• Abstract. Implementation independent.
• Unambiguous. Can be interpreted in only
one way.
• Traceable. Its source is known.
• Validatable. There is a means to prove that
the system satisfies the requirement.

---

Pitfalls to avoid, writing requirements

• Design and implementation
• Overspecification
• Overconstrained
• Unbounded
• Assumptions


---

Requirements elicitation is governed by Humphrey's
requirements uncertainty principle:
"For a new software system, the requirements will not
be completely known until after the users have used it."



---


RE Process (Sommerville) 15
• Elicitation
– Obtaining requirements from the information sources
• Analysis
– Understanding the requirements and their dependencies
• Validation
– Checking that requirements are the desired ones
• Negotiation
– Reconciling different points of view
• Documentation
– Writing the requirements in the needed form(s).
• Management
– Controlling the process and the changes



---

NEEDS CHANGE!!

Successfully specifying software requirements in advance is
difficult. But when user- or group-interactive systems are
involved, it proves nearly impossible.
• Users asked to specify requirements generally claim,
“I don’t know how to tell you, but I’ll know it when I see it.”
• Furthermore, users may initially feel that they “know it” when
they see an initial demo or prototype. But their needs and
desires change once they begin operating the system and gain
a deeper understanding of how it could support their mission.


---

Determine Reqs.

Understand
the application domain
Identify
the sources of requirements
Analyze
the stakeholders
Select
the techniques, approaches, and tools to use
Elicit
the requirements


---

Techniques to come up with reqs (with pros and cons. probably good to combine them)

- introspection
- interviews
- questionnaires
- workshops
- observation studies
- brainstorming
- prototyping
- etc.

???

Introspection (based on RE eng beliefs)
+ Quick
+ Non-expensive
{ Biased
{ Poor results
{ Usually insucient

Interviews
+ there are templates available
+ permit a lot of variability
{ can be either too focused or too vague
{ dicult to select the appropriate stakeholders

Questionnaires
+ subjective information promptly
+ low cost
{ biased answers
{ dicult to create

Workshops
+ less formal style =) revealing aspects of the
system-as-is and issues of the system-to-be
+ freedom of thought
+ broad range of ideas
{ composing the group is critical
{ risks associated with group dynamics cannot be ignored:
biased, inadequate or incomplete info
{ lack of focus
{ technical questions are addressed supercially

Observation studies
+ reveal tacit knowledge
{ costly to deploy
{ meaningful conclusions =) long-term observation,
dierent times and dierent workload conditions.
{ weaker at pointing problems and opportunities to be
addressed by the system-to-be

Brainstorming
+ freedom of thought
+ composing the group is \easy"
+ preliminary mission statement
{ key decisions are unlikely to occur
{ too much information produced


Prototyping
+ experimenting
+ user trainer
+ simulation during testing
{ does not cover all aspects
{ performance, cost, reliability, real-time constraints,
interoperability... are kept aside
{ expectation could be higher than desired

Many more...
- Task Analysis
- Domain Analysis
- Repertory Grids
- Card Sorting
- Laddering
- Apprenticing
- Goal Based Approaches


Pitfalls (again!)

Process and Project
Communication and Understanding
Quality of Requirements
Distributed and con
icting knowledge sources
Lack of equipment, expertise and/or experience
(req.engineer)
Not suciently useful or practical techniques
Practice




distributed and conflicting knowledge
time and budget constraints
communication barriers
hidden needs



---

Business use case vs Software use case
- preconditions

A conceptual schema is the general knowledge an
information system needs to know to perform its
functions.

The whole system is to hard to understand as a single unit. Split it into use cases. which include meaningful actors, etc.


Cas d'ús: Treure diners d'un caixer automàtic
Precondicions:
- Funciona la connexió amb el servidor bancari
- El caixer disposa de diners per a lliurar
- L'usuari està autoritzat a fer la transacció.



 Domain property

Exemples de propietats de domini:

Un llibre no pot estar disponible i en prèstec en el mateix moment.

---

# Functional requirements
What the software is able to do

### Process inputs and generate outputs
- Validitation
- Sequence of operations
- Error handling and recovery
- Effect of parameters
- Etc.

???
IEEE Std 830-1998. IEEE Recommended Practice for Software Requirements Specifications
Functional requirements should define the fundamental actions that must take place in the software in accepting and processing the inputs and in processing and generating the outputs. These include
a) Validity checks on the inputs
b) Exact sequence of operations
c) Responses to abnormal situations, including (1) Overflow (2) Communication facilities (3) Error handling and recovery
d) Effect of parameters
e) Relationship of outputs to inputs, including( 1) Input/output sequences, (2) Formulas for input to output conversion

---

# Quality requirements
How well the software performs under specified conditions

### 6 characteristics:
- **Functionality:** provide functions which meet stated needs.
- **Reliability:** maintain a specified level of performance.
- **Usability:** ease of learning, understanding, attractive UI...
- **Efficiency:** appropriate performance, relative to resources used.
- **Maintainability:** modificability (fixes, new features, improvements).
- **Portability:** transferability from one environment to another.

???
ISO/IEC 25030
Software quality is the capability of the software product to satisfy stated and implied needs when used under specified conditions.
ISO/IEC 25010 defines six quality characteristics:


### TODO add constraints ??



---

Goals (not necessaily smart)

Exemples (en una sistema biblioteca):
Objectiu: Els llibres en préstec es retornen a la biblioteca en el termini establert
Requisit: Una setmana abans de vèncer un préstec, s'envia un email recordatori al prestatari.
Expectativa: En el termini d'una setmana després de rebre un recordatori, els prestataris tornen els llibres reclamats a la biblioteca.
Expectativa: Els prestataris llegeixen els llibres que tenen en préstec.
No-objectiu: La biblioteca disposa d'almenys un exemplar de cada llibre que pugui interessar els socis (suposant que no hi hagi agents encarregats de l'adquisició d'exemplars)

---

SMART goals

- **Specific:** well-defined. Clear to anybody who knows the project.
- **Measurable:** to which degree is completed.
- **Agreed:** all stakeholders accept.
- **Realistic:** within constraints (resources/knowledge/etc.)
- **Time-bound:** when the goal must be achieved.

"I believe that this nation should commit itself to achieving the goal, before this decade is out, of landing a man on the moon and returning him safely to the earth" - John F. Kennedy (1961)

Note: many other words may fit the SMART acronym. Also many variants (e.g. SMARTY, SMARTER, etc.)
https://en.wikipedia.org/wiki/SMART_criteria

???
The November 1981 issue of Management Review contained a paper by George T. Doran called There's a S.M.A.R.T. way to write management's goals and objectives.


Business goals categories examples:

• Maintaining growth and continuity of the organization
• Meeting financial objectives
• Meeting personal objectives
• Meeting responsibility to employees
• Meeting responsibility to society
• Meeting responsibility to country
• Meeting responsibility to shareholders
• Managing market position
• Improving business processes
• Managing quality and reputation of products






---

Kano Model (volere model?)
different stakeholders have different goals. Hard to agree with all of them, etc.

There are too many requirements. We must prioritise



volere
satisfaction rating (1 don't care, 5 max)
dissatisfaction rating (1 don't care, 5 max)
Later ratings are weighted against cost


---
Kano Model
Performance on certain requirements produces higher levels of satisfaction than others.



Kano questionnaire

The first question concerns
the reaction of the customer
if the product has that feature
(functional form
of the question)


The second concerns his
reaction if the product does
not have that feature
(dysfunctional form
of the question).

Each question...
Like, must-be, neutral, live with, dislike


---

conceptual schemas exist, even if not formally defined and embedded within the code?



---

"quality (in a project) is never an accident. It is always the result of intelligent effort"
John Ruskin


quality criteria

Completeness
- The requirement must contain all relevant information
(template).
Consistency
- The requirements must be compatible with each other.
Adequacy
- The requirements must address the actual needs of the system.
Unambiguity
- Every requirement must be described in a way that precludes
dierent interpretations.
Comprehensibility
- The requirements must be understandable by the stakeholders.


Importance
- Each requirement must indicate how essential it is for the
success of the project.
Measurability
- The requirement must be formulated at a level of precision
that enables to evaluate its satisfaction.
Necessity
- The requirements must all contribute to the satisfaction of the
project goals.
Viability
- All requirements can be implemented with the available
technology, human resources and budget.
Traceability
- The context in which a requirement was created should be
easy to retrieve.


---


The earlier an error is discovered, the cheaper it is to correct.!!!





---

Conceptual Schemas

A conceptual schema is the general knowledge an information system needs to know to perform its functions.
The principle of necessity of conceptual schemas: To develop an information system it is necessary to define its conceptual schema.

UML, OCL and executable specs (just a brief reference) --->? CSTL? Conceptual Schema Testing Langauge. <- specify methods. With OCL/UML specify test? TDCM?



CS must be valid (correct and relevant) + complete (includes all needed knowledge).


---

TODO: Satisfaction argument?

It must be proved that:
 if the software-to-be satisfies the requirements,
 the expectations are satisfied by the environment,
 and the domain properties and hypothesis hold
 then the goals will be satisfied.


---


Consistencia entre la part estructural i la de comportament
La ultima transpa del PPT


---

