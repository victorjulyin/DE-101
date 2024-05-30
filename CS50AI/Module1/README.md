# Knowledge. Logic

## Propositional Logic
    - Propositional Logic is based on the logic of statements about the world (just separate sentences)
    - These statements are marked as Propositional Symbols - P, Q and R, for example (maybe others, maybe more)

#### Logical Connectives
    - If we want those sentences to be related to each other somehow and to be something more complex than just separate sentences we need to connect them somehow. That's why we need the Logical Connectives:

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module1/logical_connectives1.jpg" width=70% height=70%></p>

    - "not" (¬) connective. It is clear:

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module1/logical_connectives2.jpg" width=70% height=70%></p>

    - "and" (Ʌ) connective. It is clear:

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module1/logical_connectives3.jpg" width=70% height=70%></p>

    - "or" (V) connective. It is clear:

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module1/logical_connectives4.jpg" width=70% height=70%></p>

    - "Implication" (→) connective:

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module1/logical_connectives5.jpg" width=70% height=70%></p>

    - "Biconditional" (⭤) connective:

<p align="center"><img  src="https://github.com/victorjulyin/DE-101/blob/main/CS50AU/Module1/logical_connectives6.jpg" width=70% height=70%></p>

#### Model
    So now we have Propositional Symbols (statements) and Logical Connectives (relationships between statements). And now we need to tell computer which of the statements are true and which ones are false
        - Model - assignment of a truth value to every propositional sentence (creating a "possible world")

    For instance, we have two statements:
        1) P - it is raining
        2) Q - it is a Tuesday

    And after that we need to assign True/False values to them:
        {P: True, Q: False}

#### Knowledge Base

    And to use the Model with the Logical Connectives we need our AI to store this information somewhere. So we'll store it in a Knowledge Base:
        - Knowledge Base - a set of sentences known by a knowledge-based agent. Things that our AI knows about the world.

#### Entailment (logical consequence)
    This is one more thing that we need to have to create this "possible world"

    For example, we have two sentences - α and β. And if we have this α ⊨ β, it means that in every model in which sentence α is True, sentence β is also True.

#### Inference
    The process of deriving new sentences from old ones (making conclusions)

### Solution algorithms

#### Model Checking Algorithm
    We just create all of our "possible worlds" + add some facts that we have about all worlds. After that we need to check all the possible options and get conclusions from them.

    The problem with this approach is that it is not efficient. While we have n variables, we'll have 2^n of possible "worlds" and we need to check them all. It takes a lot of time

#### Inference Rules
    This is a completely different approach. We are not checking all options. Instead of this We only get the conclusions from the information we have.
    We get this information by rules, which are obvious for a human but not for a computer.

    So these are the rules:
##### Modus Ponens:
        Statement:  α → β (α implies β = when α is True then β is True)
        Knowledge: α is True
        Conclusion: β is True

        Example:
            Statement: If it is raining, then Harry is inside.
            Knowledge: It is raining.
            Conclusion: Harry is inside

##### And Elimination
        Knowledge: α Ʌ β is True
        Conclusion: α is True and β is True

        Example:
            Knowledge: Harry is friends with Ron and Hermione.
            Conclusion: Harry is friends with Hermione.

##### Double Negation Elimination
        Knowledge: ¬(¬α) is True (not not α is True)
        Conclusion: α is True

        Example:
            Knowledge: It is not true that Harry did not pass the test.
            Conclusion: Harry passed the test.

##### Implication Elimination
        Statement:  α → β (α implies β = when α is True then β is True)
        Knowledge: ¬α V β

        Example:
            Knowledge: If it is raining, then Harry is inside.
            Conclusion: It is not raining OR Harry is inside.

##### Biconditional Elimination
        Knowledge: α <-> β
        Conclusion: (α -> β) Ʌ (β -> α)

        Example:
            Knowledge: It is raining if and only if Harry is inside.
            Conclusion: If it is raining, then Harry is inside, and if Harry is inside, then it is raining.

##### De Morgan's Law
        Knowledge: ¬(α Ʌ β)
        Conclusion: ¬α V ¬β

        Example:
            Knowledge: It is not true that both Harry and Ron passed the test.
            Conclusion: Harry did not pass the test OR Ron did not pass the test.

##### De Morgan's Law 2
        Knowledge: ¬(α V β)
        Conclusion: ¬α Ʌ ¬β

        Example:
            Knowledge: It is not true that Harry or Ron passed the test.
            Conclusion: Harry did not pass the test AND Ron did not pass the test.

##### Distributive law
        Knowledge: (α Ʌ (β V γ))
        Conclusion: (α Ʌ β) V (α Ʌ γ)

##### Distributive law 2
        Knowledge: (α V (β Ʌ γ))
        Conclusion: (α V β) Ʌ (α V γ)

##### Unit resolution rule
        Knowledge:
            1) P v Q
            2) ¬P
        Conclusion: 
            1) Q
        Example:
            Knowledge:
                1) (Ron is in the Great Hall) V (Hermione is in the library)
                2) Ron is not in the Great Hall
            Conclusion:
                1) Hermione is in the library

##### Distributive law
        Knowledge:
            1) P v Q1 v Q2 ... Qn
            2) ¬P
        Conclusion: 
            1) Q1 v Q2 ... Qn

##### Unit resolution rule 2
        Knowledge:
            1) P v Q
            2) ¬P v R
        Conclusion:
            1) Q v R

        Example:
                1) (Ron is in the Great Hall) V (Hermione is in the library)
                2) (Ron is not in the Great Hall) V (Harry is sleeping)
            Conclusion:
                1) (Hermione is in the library) V (Harry is sleeping)

##### Distributive law 2
        Knowledge:
            1) P v Q1 v Q2 v ... v Qn
            2) ¬P v R1 v R2 v Rm
        Conclusion: 
            1) Q1 v Q2 v ... v Qn v R1 v R2 ... v Rm

##### Basic of inference resolution
        Knowledge:
            1) P
            2) ¬P
        Conclusion: 
            1) () - Empty clause. Or just False
            Because it is impossible that both P and ¬P can exist at one moment

#### Some definitions
    - Disjuntion - something that connected with "V"
    - Conjuntion - something that connected with "Ʌ"
    - Clause - a disjunction of literals (propositional symbols - P, Q, R...). For example: P v Q v R
    - Conjunctive normal form (CNF) - logical sentence that is a conjunction of clauses. E.G. (A v B v C) Ʌ (D v ¬E) Ʌ (F v G)

### Conversion to CNF (how to convert logical sentence to CNF)
    The thing is that we can convert any logical sentence into CNF using inference rules. This is the algorithm:

    1) Eliminate biconditionals
        - turn (A <-> B) into (A -> B) Ʌ (B -> A)
    2) Eliminate implications
        - turn (A -> B) into ¬A v B
    3) Move ¬ inwards using De Morgan's Laws
        - turn ¬(A Ʌ B) into ¬A v ¬B
    4) Use distributive law to distribute 'v' wherever possible


#### Example:
        - Starting with this:
            - (P v Q) -> R
        - Opening the implication:
            ¬(P v Q) v R
        - Use De Morgan's law
            (¬P Ʌ ¬Q) v R
        - Next step:
            (¬P v R) Ʌ (¬Q v R)

### Inference by Resolution
    So we need to determine that KB ⊨ A. How ca we do it?
        - To determine if KB ⊨ A:
            - Check if (KB Ʌ ¬A) is a contradiction?
                - if so, then KB ⊨ A,
                - Otherwise, no entailment

    - To determine that KB ⊨ A:
        - Convert (KB Ʌ ¬A) to Conjuctive Normal Form
        - Keep checking to see if we can use resolution to produce a new clause
            - If ever we produce the empty clause (equivalent to False), we have a contradiction and KB ⊨ A
            - Otherwise, if we can't add new clauses, there is no entailment

#### Example

    1) Does (A v B) Ʌ (¬B v C) Ʌ (¬C) entail A?

    2) First of all we try to assume that A is False:
        - (A v B) Ʌ (¬B v C) Ʌ (¬C) Ʌ (¬A)
    3) From this we can draw a new conclusion: (¬B v C) Ʌ (¬C) = (¬B)
    - So now we have: (A v B) Ʌ (¬B v C) Ʌ (¬C) Ʌ (¬A) Ʌ (¬B)

    4) (A v B) Ʌ (¬B) = A
    - So now we have: (A v B) Ʌ (¬B v C) Ʌ (¬C) Ʌ (¬A) Ʌ (¬B) Ʌ A

    5) And here is the contradiction: (¬A) Ʌ A
    
## First-Order logic

    For example, we need to assign Harry Potter characters to their houses in Hogwarts.
    And we have:
        Constant Symbols (propositional symbols):
            - Minerva
            - Pomona
            - Horace
            - Gilderoy
            - Gryffindor
            - Hufflepuff
            - Ravenclaw
            - Slytherin
        
        Predicate Symbols (classes and functions):
            - Person
            - House
            - BelongsTo

### Universal Quantification

    ∀x. BelongsTo(x, Gryffindor) -> ¬BelongsTo(x, Huffelpuff)

    Which means - For all objects x (∀ means for all), if x belongs to Gryffindor, then x does not belong to Huffelpuff

### Existentional Quantification

    Ǝx. House(x) Ʌ BelongsTo(Minerva, x)

    Which means - There exists (Ǝ means exists) an object x such that x is a house and Minerva belongs to x.
    Simply - Minerva belongs to some house.

    And as a more general rule we can have this:
        ∀x. Person(x) -> (Ǝy. House(y) Ʌ BelongsTo(x, y))
    For all objects x, if x is a person, then there exists an object y such that y is a house and x belongs to y.
    Which means - every person belongs to a house