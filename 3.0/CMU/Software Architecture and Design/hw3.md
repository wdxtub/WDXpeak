# Week 3 Assignment

In Week 3,

## 3.1 

you will further enhance your architectural diagrams into a collection of view diagrams, to systematically describe the target system from various angles: [60]

+ Functional View -- Show the component diagram, including interfaces and dependencies. [12]
    + What are the main functional components in your system?
    + Consider using simplified UML 2.0 component diagrams to show interfaces of your major components and their dependencies. 
+ Information View -- Show the schema, data models and data flows. Show any state machine diagrams that describe the information model for the system. [12]
    + You may want to use data schema models or simplified UML 2.0 object models to describe information elements, their relationships and cardinality. 
    + Data/information flow diagrams and state diagrams -- describing the information lifecycle -- are also part of well-defined information view. 
+ Deployment View -- Where will software components reside or get deployed for execution? [12]
+ Development View -- What are the main software packages? [12]
+ Concurrency View -- How would concurrent use of our systems form various locations? How do we ensure data consistency in the distributed system? [12]

## 3.2 

Meanwhile, you will refine your Week 2 homework and clearly explain how you apply architectural styles in your design. [40]

For every architectural style you applied, explain:

+ Components
+ Connectors
+ Data elements
+ Behaviors, e.g., describe in wording how your design has applied the architectural style 
+ Cautions: anything you would like to let your development team to pay attention
+ Use some view/diagram to explain

---

+ Traditional, language-influenced styles [10%]
	+ Main program and subroutines
	+ Object-oriented
+ Layered [10%]
	+ Virtual machines
	+ Client-server
	+ MVC
+ Data-flow styles [10%]
	+ Batch sequential
	+ Pipe and filter
+ Shared memory [10%]
	+ Blackboard
	+ Rule based
	+ MapReduce
+ Interpreter [10%]
	+ Interpreter
	+ Mobile code
+ Implicit invocation [10%]
	+ Event-based
	+ Publish-subscribe
+ Peer-to-peer [10%]
+ “Derived” styles [10%]
	+ C2
	+ CORBA
	+ SOA


Submission can be delivered as a set of diagrams together with some written explanations -- possibly including a glossary. Hopefully, you will use some UML 2.0 notation for this submission. Describe the functional, information and deployment views. If you have time or wish to show other views, justify why you think it is important to do so at this point. (You may get extra points but it may also distract you from producing the three main views.)

---

Suggestion: Use Draw.io (a tool resulted from the class vote that can support online collaborative design of UML diagrams).

I will upload a sample Architecture View Report (see the Specific Sections of the document, created from previous students from an EARLIER version of the Sensor Data Service Platform).

Here, we list some other, related tips and tools. For now, feel free to consult them as needed. Browse each reference, when needed, and focusing more on sections that might be useful to the tasks at hand would be a far better strategy for absorbing the material than reading them in their totality from beginning to end. You have been forewarned.

+ UML 2.0 Specification: http://www.omg.org/spec/UML/2.4.1/Superstructure/PDF/
    + Pay more attention to the diagram sections -- for example section 8.4 for functional diagrams. 
+ UML 2.0 activity and action models:
    + http://www.jot.fm/issues/issue_2003_07/column3/
    + http://www.conradbock.org/omg/pm/05-12-05.pdf
+ Advanced information modeling with a focus on practical tools and concepts:
    + http://www.conradbock.org/#UML2.0
+ General views on software architecture as a discipline and its role in software engineering:
    + http://sdm.mit.edu/docs/Software%20Architecture%20Webinar%20v4.pdf
    + Microsoft Architecture Overview: http://msdn.microsoft.com/en-us/library/ms978007.aspx
+ Varying views on architectural views, and more:
    + 4+1 View: http://www.cs.ubc.ca/~gregor/teaching/papers/4+1view-architecture.pdf
    + Also see: http://plg.uwaterloo.ca/~holt/cs/446/08/slides/mazeiar-kruchten-4+1.ppt 
    + Open Group's view on [architectural artifacts](http://pubs.opengroup.org/architecture/togaf9-doc/arch/chap35.html)

