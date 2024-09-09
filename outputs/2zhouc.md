## GEB Discussion #2 - Chapter #1: The MU-Puzzle

### Post:

**Gödel, Escher, Bach: An Eternal Golden Braid**

This is a discussion of the themes and questions concerning the **Chapter 1: The MU-Puzzle**, and its dialogue, **Two-Part Invention**.

**Formal Systems**

Formal Systems are defined as:

1.	A finite set of symbols which can be used for constructing formula. 

2.	A grammar, i.e. a way of constructing well-formed formula out of the symbols, such that it is possible to find a decision procedure for deciding whether a formula is a well-formed formula or not.
 
3.	A set of axioms or axiom schemata: each axiom has to be a well-formed formula.

4.	A set of inference rules. 

5.	A set of theorems. This set includes all the axioms, plus all well-formed formulas which can be derived from previously-derived theorems by means of rules of inference. Unlike the grammar for well-formed formulas, there is no guarantee that there will be a decision procedure for deciding whether a given well-formed formula is a theorem or not.

Are formal systems applicable to real life?

Can you notice occasions in your life when you were in M-Mode, I-Mode, U-Mode, or some combination of the three modes?

Are people always in one of the three modes, or do we spend time in a non-mode state when we aren’t thinking too intensely on anything?

……

**Isomorphisms**

As quoted in *Godel, Escher, Bach*, “The word “isomorphism” applies when two complex structures can be mapped onto each other, in such a way that to each part of one structure there is a corresponding part in the other structure, where “corresponding” means that the two parts play similar roles in their respective structures.”

Examples:

A wooden cube is isomorphic to a glass cube of the same size.

A standard 52-card deck can be used to play numerous card games such as Gin-Rummy, Solitaire, Hearts, Castle, Mao, and many more. Does this mean cards for one game is isomorphic to the same cards of a different game?

When we learn how to solve one problem, we tend to apply what we learned to similar problems. Is this an application of how isomorphisms can be used in real life?

……

**Dialogue**

Here’s a few questions on the dialogue:

a) What can we say the dialogue is isomorphic to? Or rather what is the theme of the dialogue? 

b) How can the Turtle’s ‘logical’ statements be resolved?

The answer to (b) is that Tortoise has led Achilles into the problem of ‘infinite regression’ where he forces Achilles to accept that 1-to-n propositions needs to be accepted to accept the proposition Z. If we treat his logical arguments as isomorphic to a formal system, then we’ll realize that Tortoise seems to be lacking an axiom, since there is no base case for the regression to end at. This is explained more clearly in the Wikipedia article, [What the Tortoise Said to Achilles]( http://en.wikipedia.org/wiki/What_the_Tortoise_Said_to_Achilles), where the axiom of ‘modus ponens’ is missing from the Tortoise's explanation.

Wikia links for these chapters:

* [Chapter 1](http://godel-escher-bach.wikia.com/wiki/Chapter_1)

* [Two-Part Invention](http://godel-escher-bach.wikia.com/wiki/Two-Part_Invention)

Coming up next on March 20th is Chapter 2: Meaning and Form in Mathematics.

The discussion for the previous chapter is posted [here](http://www.reddit.com/r/rational/comments/2z8zm5/geb_discussion_1_introduction_a_musicological/).

The discussion for the next chapter is posted [here](http://www.reddit.com/r/rational/comments/2zpwl4/geb_discussion_3_chapter_2_meaning_and_form_in/).

[Official Schedule](http://www.reddit.com/r/rational/comments/2yys1i/lets_start_the_read_through/).

EDIT: A few people who have previously read GEB have commented on /r/GEB that this schedule is a little aggressively quick and we will be likely to lose many readers as we approach the end of Part 1. I have taken this advice into consideration and adjusted the dates to reflect a switch to two chapters per week starting with **Chapter VII: The Propositional Calculus** on April. The two chapters week will be a Monday and Thursday schedule.

Also someone said:

> Another read through that will probably just drop off into oblivion like all the rest.

Challenge ***accepted***.

### Comments:

- u/redstonerodent:
  ```
  Claim: In the MIU system, no theorem has multiple of 3 'I's.

  Denote the number of steps taken to derive a theorem as the *rank* of the theorem. 

  Proof (induction on rank):

  Base case: rank 0. The only axiom is 'MI' which has not a multiple of 3 'I's.

  Suppose no theorem of rank k has a multiple of 3 'I's. Notice how applying the rules to each of these theorems changes the number if 'I's:

  * Rule I: no change
  * Rule II: double
  * Rule III: decrease by 3
  * Rule IV: no change.

  Doubling or decreasing by 3 any non-multiple of 3 doesn't make a multiple of 3, so no theorem of rank k+1 has a multiple of three 'I's. By induction, no theorem of any rank, and thus no theorem, has a multiple of 3 'I's.

  This means 'MU' isn't a theorem. I'm pretty sure "starting with 'M' and not having a multiple of 3 'I's" is a sufficient and necessary condition on theorems, but I haven't worked through the details of the sufficience proof.

  **Edit:** I proved this; see my response to /u/Hazlzz's comment below.

  In response to (b):

  The Turtle is taken on more and more axioms, without any way to build theorems from them. This is why a formal system needs inference rules; otherwise you have no theorems other than the axioms, and the formal system is trivial.
  ```

  - u/None:
    ```
    > "starting with 'M' and not having a multiple of 3 'I's" is a sufficient and necessary condition on theorems

    Are you saying every string that fits those criteria is a theorem? That's really interesting. I was halfway through arguing that MUII is impossible, but it's not: MI -(R2)-> MII -(R2)-> MIIII -(R2)-> MIIIIIIII -(R3)-> MUIIIII -(R1)-> MUIIIIIU -(R3)-> MUIIUU -(R4)-> MUII.

    Rule 1 keeps tripping me up. All the rest go really well together, you can make general statements based on them because they act in very modular-arithmetic ways. But you can just add a U at the end if it ends with I... I find it hard to generalize on that.
    ```

    - u/redstonerodent:
      ```
      Alright, here's my proof that any string that starts with **M** and has not a multiple of 3 **I**s is a theorem:

      Let S be a string beginning with **M** that has i **I**s and u **U**s, and i is not a multiple of 3.

      Clearly 3u+i is not a multiple of 3. Thus there are nonnegative k, a such that 3u+i+3k=2^(a). 

      The following sequence of rule applications, beginning with **MI** creates S:

      * Perform Rule 2 a times to form **MI**^2^a (**M** followed by 2^a **I**s). 
      * If k is odd, perform Rule 1 to form **MI**^(2^a)**U**
      * Perform Rule 3 k times to the last 3k **I**s, forming **MI**^(3u+i)**U**^(k[+1]). The number of **U**s is even.
      * Perform Rule 4 k[+1]/2 times to form **MI**^(3u+i)
      * Perform Rule 3 u times to create **U**s in the appropriate places, forming S.

      I proved earlier that no theorem has a multiple of 3 **I**s, and clearly every theorem begins with **M**. I have now shown that any string satisfying these properties is a theorem.

      Therefore the following python is a decision procedure for the MIU system, assuming the string S only contains **M**, **I**, and **U**:

          if S[0] != 'M': return False
          elif S.count('I') % 3 == 0: return False
          elif S.count('M') > 1: return False
          else return True

      Edit: Added a line as /u/Hazlzz suggested.
      ```

      - u/Ty-Guy9:
        ```
        I'm loving your proofs, but whoa! You lost me at 3u+i+3k=2^a :
        > Clearly 3u+i is not a multiple of 3. Thus there are nonnegative k, a such that 3u+i+3k=2^a. 

        I guess you skipped the step of showing that for any non-multiple of 3, there always exists a multiple of three that adds with it to a power of 2. Now I'm left to try to figure out a proof for that. [thinks a bit] Okay, this should work, even if it's kind of long:

        1. Powers of 2 are never multiples of three, therefore when divided my three they must have either remainder 1 or remainder 2. (I'll call these classes M1 and M2.)

        2. Numbers in M1 or M2, when doubled, produce numbers in the opposite class. Demonstrations: (3x+1)*2=6x+2=3x'+2. (3x+2)*2=6x+4=3x'+1.

        3. Every number 3u+i, where i is in M1 or M2, will have some additive 3y that brings it to within 1 of the the power of two above it, 2^z. If they are the same class (M1/M2) then choose k=y and a=z, otherwise move up to the next power of two, which will be of the opposite class, and use a=z+1 and the appropriate k. (k=2y+u or k=2y+u+1, if we're looking for M2 or M1, respectively.)

        Well, that was fun, and now I can move on to the rest of your proof! [reads proof] Yes, a very nice proof of the necessary and sufficient properties for the MIU system!
        ```

      - u/None:
        ```
        Beautiful, thank you! I know it's a little redundant to point this out, since it was explicitly stated in the chapter, but for the sake of completion the python should include

             elif S.count('M') > 1: return False
        ```

  - u/None:
    ```
    [deleted]
    ```

- u/None:
  ```
  Had a lot of fun playing around with the MU puzzle. Took me a while to decide the problem was unsolvable, but now I'm confident it is, because: 

  a) you need to end up with no Is in your string  
  b) the only way to remove an I is 3 at a time. To remove all Is you need a number of Is that is divisible by 3.  
  c) the only way to generate an I is by doubling the entire string (except the M). This gives you twice as many Is as before.  
  d) no number that is not divisible by 3 can be doubled and then be divisible by 3. (x % 3 != 0 means 2x % 3 != 0).
  ```

- u/None:
  ```
  [deleted]
  ```

  - u/xamueljones:
    ```
    Oops. Thanks for the catch!

    As a side note, I think of the I-Mode as when we think on a meta-level about the system and it sounds like a mathematical formulation of I-Mode would be first-order, second-order, and other higher orders of logic. Which means that M-Mode for thinking within the system which can be the standard laws of logic, and the first and second order logic systems is I-Mode.

    In simple English, M-Mode is thinking directly about the system and I-Mode is thinking about the system on a meta-level, and on a meta-meta level.

    Before people bring up the obvious extension of a meta-meta-meta-... level. I have only this to say. There is no such thing. We never have any need to do so in real life. There is no need to think in more than three levels about the system (system, meta, and meta-meta). I think it's proven somewhere that third, fourth, fifth, and etc. orders of logic are equally as powerful as second order logic and don't really contribute anything new (maybe restating some theorems in a different way can help, but that's it for their benefits).

    Here's a fun meta joke:

    I'm

    So

    Meta

    Even

    This

    Acronym
    ```

    - u/None:
      ```
      I don't think your claim about repeated levels of meta-reasoning is true.

      For one thing, category theorists, type theorists, and so on, need to allow for an arbitrary number of levels of meta-reasoning, or else some statements become unstateable.

      In category theory, you can't make a claim about "all categories" without encountering [Russell's paradox](http://en.wikipedia.org/wiki/Russell%27s_paradox). You have to create a category of "all small categories", that is, categories that are 'normal' and don't get all meta about category theory. The category of all small categories cannot be a small category, so call it a 2-category.

      If you wanted to make a claim about the category of all 2-categories, you'd need that to be a 3-category. And so on. 3-categories are not the same as 2-categories.

      There might be particular propositional systems where third-order logic is the same as second-order logic -- this is about where I run out of mathematical background -- but I'd want you to at least show me an example of such a system.
      ```

      - u/None:
        ```
        Technically speaking, third-order logic *can* be written down completely inside second-order logic (as /u/xamueljones notes).  However, in [dependent type theory](http://www.cs.ucsb.edu/~benh/290C_W15/papers/Calculus%20of%20Inductive%20Constructions.pdf) we generally find it useful to have an infinite hierarchy of universes available precisely for the sake of making statements that *appear* self-referential, or "impredicative".

        Of course, non-homotopy type theories are mostly constructive, meaning that they simply don't allow us to state undecidable/unprovable propositions as "believed" theorems: once we "go intuitionistic" and require all propositions to be proved in order to be believed (possibly via exhibiting some trivial data object, as with "proving" the "proposition" `Nat` by exhibiting the natural number 1), we can get a well-behaved logic with an infinite hierarchy of universes and no paradoxes.  We just refuse to believe the Law of the Excluded Middle (`forall P. P \/ ~P`) when we can't actually exhibit a finite-time decision-procedure for the proposition `P` in question.
        ```

    - u/Ty-Guy6:
      ```
      Hmm. No added utility from 3rd-order meta? Seems hard to prove or disprove off the cuff, but let me think out loud. Suppose the goal is to get enough carrots to eat:

      * System-level could be picking carrots and eating them.

      * Meta-level could be planting and caring for carrot seeds so that you can eat them later.

      * Meta-meta-level could be forming tools to make carrot-planting more efficient, or perhaps hiring workers and paying them from carrot sales; there are probably a lot of branches we could follow.

      * Meta-meta-meta-level could be ... economics, mechanical/genetic engineering, i.e. fields that directly improve upon your level-2 strategy.

      * Metax4-level could be the scientific system itself, or other systems of thought/action which tend to develop those more directly useful fields of level metax3. It is possible that your religion/worldview could be included here, or otherwise at level metax5.

      Hmm. So far I subscribe to this progression. Would you also accept it as a counterexample, or does it fit into your theory somehow?

      I make no claims of this shedding light on the author's M/U/I thought theory, but at the least it's a fun side-track.
      ```

      - u/xamueljones:
        ```
        Sorry I didn't reply earlier. My computer shut down for a bit.

        I feel like this comment isn't talking about thinking in a more meta sense, but rather categorizing simpler systems like farming within a bigger system like economics.

        Using your example of carrot picking:

        * System-Level - The basic steps to picking a carrot which we can easily automate a robot to do for us. Steps are of the form: check carrot for freshness, then pick or leave alone. This level is the task itself and methods to perform the task.

        * Meta-Level - How well does the robot do it's job? Does it work better on sunny days than rainy days? How quick and efficient is it at its job? What mistakes does it make, or what can it do better? This level is thinking *about* the task and what can be changed about the methods to perform the task.

        * Meta-Meta-Level - How are we examining the robot's effectiveness? How do we come up with new plans for the robot? How were we thinking when we came up with particularly bad plans, or particularly good plans? How do we structure our planning process? This level is thinking about how we are thinking about the task. This is where you examine your thought processes about how you deal with problems, or in other words, how do you structure your planning to solve the problem.

        * Meta-Meta-Meta...-Level - This is where things break down, because the last level was analyzing how you approach problems in the first place and is extremely abstract and is very far removed from the original problem. To go any further would be something like this very discussion where I explained how meta-thinking works. But looking at the problem from a multi-meta viewpoint is still part of the meta-meta level since it examines how you approach the problem in the first place. Therefore this level doesn't seem to offer any further insights to help with solving the problem.

        The flaw you made in your comment is that you confused meta-thinking with thinking more abstractly. But meta-levels should retain the same focus on the same problem/system as the object-level, with the only differences being that you step back from solving the problem to *how* you solve the problem to how you *think* about how you solve the problem.

        A real life example is the HPMOR planning threads:

        The [System-Level/Unified Solutions Thread](http://www.reddit.com/r/HPMOR/comments/2xkbb8/spoilers_113_unified_solutions_thread/) which is about the presented solutions to pass the Final Exam, [Meta-Level/Planning Thread](http://www.reddit.com/r/HPMOR/comments/2xiabn/spoilers_ch_113_planning_thread/) which is about examining the problem and to see how a possible solution would be structured, and [Meta-Meta-Level/Meta Meta Planning Thread](http://www.reddit.com/r/HPMOR/comments/2xhqus/the_meta_meta_planning_thread/) which is about discussing how to discuss the problem and its solutions.

        In fact, /u/alexanderwales stated the purpose of a meta-meta-planning thread as:

        > This is not a place to post solutions.

        > This is not a place to discuss the problem.

        > This is the place to discuss how to discuss the problem and its solutions.

        Furthermore, note that not a single person in a community of thousands even *tried* posting a Meta-Meta-Meta-Level thread, because it just doesn't make sense on a logical* level to do so.

        EDIT: *When I said "on a logical level" I should have said "on a intuitive level", because I'm referring to how humans think about meta-ness and not the theory of logic.
        ```

- u/None:
  ```
  Wikia links for these chapters:

  * [Chapter 1](http://godel-escher-bach.wikia.com/wiki/Chapter_1) - try questions 10 and 10.1 if you consider the MU-puzzle simple.
  * [Two-Part Invention](http://godel-escher-bach.wikia.com/wiki/Two-Part_Invention) - explains the background behind this dialogue, in case you missed it
  ```

- u/None:
  ```
  The chapter was mostly pretty basic but an insightful thing was the "working within the system vs. jumping out of the system" idea. I think you could apply this to the rules of our society: most people work within the system of our society, never making observations of it as a whole.  But some people, like clever salesmen, criminals or lawyers are maybe able to jump out of the system and observe it from a more neutral viewpoint and get an advantage because of it.

  Btw, some people over at /r/GEB complained that the schedule is a bit aggressive and speculated that people would drop out at the beginning of April at the latest. I dunno about that myself, we'll see.
  ```

  - u/None:
    ```
    I'm speculating, specifically, that if you try to cover chapters 7, 8, and 9, as well as their corresponding dialogues, in the same week, it's going to be pretty rough and most people will get left behind.

    ...not that /r/geb should claim any particular expertise on successfully completing readthroughs.
    ```

---

