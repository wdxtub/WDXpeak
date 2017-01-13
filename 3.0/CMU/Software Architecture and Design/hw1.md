# Week 1 Assignment

Due: Monday (1/18) midnight PST to submit from blackboard

## Goals

The goals of this homework are three-fold. 

First, this homework will serve as a baseline for your later architectural revision, by designing a software system from a software developer's knowledge. 

Second, this homework will refresh you Object-Oriented Analysis and Design that you have learned from your FSE course. 

Third, this homework will let you refresh how to apply Unified Modeling Language (UML) to document your software design.

## Requirements

Specifically please use Use Case Diagram, Class Diagram, and Sequence Diagram to identify the components and design a software system based on the following requirements. Identify core architectural elements and design their dependencies and connections. Class diagram will be used to outline the software components in your system; sequence diagram will be used to specify the communication protocols (relationships) among components; and use case diagram will be used to define the system functions from a user's perspective.

- Use Cacoo as a free UML tool to design the blueprint you can think of. 
- The diagrams can be hierarchical so break them into several if so desired.

## Grading Criteria

- Submit both Cacoo and PDF versions of the diagrams. [15%]
- Proper OOAD exercise to identify software components in class diagrams [20%]
- Each software component will have a name, attributes, and functions. [20%]
- Use case diagrams [20%]
- Sequence diagrams [25%]

## System Requirements

Each ATM machine will have a magnetic stripe reader for reading an ATM card, a keyboard and display for interaction with customers, a slot for depositing envelopes, a dispenser for cash (in multiples of $20), a printer for printing customer receipts, and a key-operated switch to allow an operator to start or stop the machine. The ATM will communicate with the bank's computer over an appropriate communication link. (The software on the latter is not part of the requirements for this problem.)

One ATM machine will serve one customer at a time. A customer will be required to insert an ATM card and enter a personal identification number (PIN) - both of which will be sent to the bank for validation as part of each transaction. The customer will then be able to perform one or more transactions. The card will be retained in the machine until the customer indicates that she does not desire further transactions, at which point it will be returned - except as noted below.

An ATM machine must be able to provide the following services to customers:

+ A customer must be able to make a cash withdrawal from any suitable account linked to the card, in multiples of $20.00. Approval must be obtained from the bank before cash is dispensed.
+ A customer must be able to make a deposit to any account linked to the card, consisting of cash and/or checks in an envelope. The customer will enter the amount of the deposit into the ATM, subject to manual verification when the envelope is removed from the machine by an operator. Approval must be obtained from the bank before physically accepting the envelope.
+ A customer must be able to make a transfer of money between any two accounts linked to the card.
+ A customer must be able to make a balance inquiry of any account linked to the card.

The ATM will communicate each transaction to the bank and obtain verification that it was allowed by the bank. In the case of a cash withdrawal or deposit, a second message will be sent after the transaction has been physically completed (cash dispensed or envelope accepted).

If the bank determines that the customer's PIN is invalid, the customer will be required to re-enter the PIN before a transaction can proceed. If the customer is unable to successfully enter the PIN after three tries, the card will be permanently retained by the machine, and the customer will have to contact the bank to get it back.

If a transaction fails for any reason other than an invalid PIN, the ATM will display an explanation of the problem, and will then ask the customer whether he/she wants to do another transaction.

An ATM machine will provide the customer with a printed receipt for each successful transaction, showing the date, time, machine location, type of transaction, account(s), amount, and ending and available balance(s) of the affected account ("to" account for transfer).

An ATM machine will have a an operator panel with a key-operated switch (located on the "inside the bank" side) that will allow an operator to start and stop the servicing of customers. When the switch is moved to the "off" position, the machine will shut down, so that the operator may remove deposit envelopes and reload the machine with cash, blank receipts, etc. The operator will be required to verify and enter the total cash on hand before starting the system from this panel.

If an ATM machine does not have sufficient fund for withdrawn, it should recommend some other ATM machines close by with sufficient fund.

An ATM machine typically is associated with some banks. If a user intends to withdraw fund from another bank, some transaction fees may be applied. Such a warning should be conveyed to the customer and obtain her agreement before a transaction is processed.

There is typically a daily cash withdrawn limit associated with an ATM machine.

## Notes

+ Note that this is an open question. Please use your imagination to design the system. Try point out non-functional requirements, raise some questions, think about boundary conditions will be good answers.
+ Below please find some basic requirements to trigger your thoughts and help your practicing the design patterns:
	+ An ATM machine will allow users to deposit money, withdraw money, and check account balance, etc.
	+ The application should provide options for a user to choose from, and then the system enters the selected state.
	+ For designing such a financial system (and for any financial system as a matter of fact) one must requirement is that they should work as expected in all situations.
	+ No matter whether its power outage ATM should maintain correct state (transactions), think about locking, transaction, error condition, boundary condition etc.
	+ If an ATM machine does not have sufficient fund, it should talk to close-by ATM machines and give users suggestions;
	+ ATM machine has to maintain security and privacy for users. After a card is taken out, the previous information should not be revealed to later users.
	+ Each ATM machine will provide 24X7 service.
	+ More banks may join the association with an ATM machine in the future.
	+ Users may choose appropriate account to conduct transactions.
	+ An ATM system may support multiple languages.

## Resources

Here is a good tutorial site for you to review UML: http://www.tutorialspoint.com/uml/index.htm

