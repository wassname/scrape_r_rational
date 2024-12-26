## GEB Discussion #2 - Chapter #1: The MU-Puzzle

* Author: u/xamueljones  *My arch-enemy is entropy**
* URL: https://www.reddit.com/r/rational/comments/2zhouc/geb_discussion_2_chapter_1_the_mupuzzle/
* Score: 23

* Created: 2015-03-18T17:54:10

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

> **u/redstonerodent** [+13]  *High Council of Gallifrey* (3 hours later)
> 
> Claim: In the MIU system, no theorem has multiple of 3 'I's.
> 
> Denote the number of steps taken to derive a theorem as the *rank* of the theorem. 
> 
> Proof (induction on rank):
> 
> Base case: rank 0. The only axiom is 'MI' which has not a multiple of 3 'I's.
> 
> Suppose no theorem of rank k has a multiple of 3 'I's. Notice how applying the rules to each of these theorems changes the number if 'I's:
> 
> * Rule I: no change
> * Rule II: double
> * Rule III: decrease by 3
> * Rule IV: no change.
> 
> Doubling or decreasing by 3 any non-multiple of 3 doesn't make a multiple of 3, so no theorem of rank k+1 has a multiple of three 'I's. By induction, no theorem of any rank, and thus no theorem, has a multiple of 3 'I's.
> 
> This means 'MU' isn't a theorem. I'm pretty sure "starting with 'M' and not having a multiple of 3 'I's" is a sufficient and necessary condition on theorems, but I haven't worked through the details of the sufficience proof.
> 
> **Edit:** I proved this; see my response to /u/Hazlzz's comment below.
> 
> In response to (b):
> 
> The Turtle is taken on more and more axioms, without any way to build theorems from them. This is why a formal system needs inference rules; otherwise you have no theorems other than the axioms, and the formal system is trivial.

>> **u/None** [+2]  (6 hours later)
>> 
>> > "starting with 'M' and not having a multiple of 3 'I's" is a sufficient and necessary condition on theorems
>> 
>> Are you saying every string that fits those criteria is a theorem? That's really interesting. I was halfway through arguing that MUII is impossible, but it's not: MI -(R2)-> MII -(R2)-> MIIII -(R2)-> MIIIIIIII -(R3)-> MUIIIII -(R1)-> MUIIIIIU -(R3)-> MUIIUU -(R4)-> MUII.
>> 
>> Rule 1 keeps tripping me up. All the rest go really well together, you can make general statements based on them because they act in very modular-arithmetic ways. But you can just add a U at the end if it ends with I... I find it hard to generalize on that.

>>> **u/redstonerodent** [+2]  *High Council of Gallifrey* (9 hours later)
>>> 
>>> Alright, here's my proof that any string that starts with **M** and has not a multiple of 3 **I**s is a theorem:
>>> 
>>> Let S be a string beginning with **M** that has i **I**s and u **U**s, and i is not a multiple of 3.
>>> 
>>> Clearly 3u+i is not a multiple of 3. Thus there are nonnegative k, a such that 3u+i+3k=2^(a). 
>>> 
>>> The following sequence of rule applications, beginning with **MI** creates S:
>>> 
>>> * Perform Rule 2 a times to form **MI**^2^a (**M** followed by 2^a **I**s). 
>>> * If k is odd, perform Rule 1 to form **MI**^(2^a)**U**
>>> * Perform Rule 3 k times to the last 3k **I**s, forming **MI**^(3u+i)**U**^(k[+1]). The number of **U**s is even.
>>> * Perform Rule 4 k[+1]/2 times to form **MI**^(3u+i)
>>> * Perform Rule 3 u times to create **U**s in the appropriate places, forming S.
>>> 
>>> I proved earlier that no theorem has a multiple of 3 **I**s, and clearly every theorem begins with **M**. I have now shown that any string satisfying these properties is a theorem.
>>> 
>>> Therefore the following python is a decision procedure for the MIU system, assuming the string S only contains **M**, **I**, and **U**:
>>> 
>>>     if S[0] != 'M': return False
>>>     elif S.count('I') % 3 == 0: return False
>>>     elif S.count('M') > 1: return False
>>>     else return True
>>> 
>>> Edit: Added a line as /u/Hazlzz suggested.

>>>> **u/Ty-Guy9** [+4]  *Wants to become a "FAI"* (16 hours later)
>>>> 
>>>> I'm loving your proofs, but whoa! You lost me at 3u+i+3k=2^a :
>>>> > Clearly 3u+i is not a multiple of 3. Thus there are nonnegative k, a such that 3u+i+3k=2^a. 
>>>> 
>>>> I guess you skipped the step of showing that for any non-multiple of 3, there always exists a multiple of three that adds with it to a power of 2. Now I'm left to try to figure out a proof for that. [thinks a bit] Okay, this should work, even if it's kind of long:
>>>> 
>>>> 1. Powers of 2 are never multiples of three, therefore when divided my three they must have either remainder 1 or remainder 2. (I'll call these classes M1 and M2.)
>>>> 
>>>> 2. Numbers in M1 or M2, when doubled, produce numbers in the opposite class. Demonstrations: (3x+1)*2=6x+2=3x'+2. (3x+2)*2=6x+4=3x'+1.
>>>> 
>>>> 3. Every number 3u+i, where i is in M1 or M2, will have some additive 3y that brings it to within 1 of the the power of two above it, 2^z. If they are the same class (M1/M2) then choose k=y and a=z, otherwise move up to the next power of two, which will be of the opposite class, and use a=z+1 and the appropriate k. (k=2y+u or k=2y+u+1, if we're looking for M2 or M1, respectively.)
>>>> 
>>>> Well, that was fun, and now I can move on to the rest of your proof! [reads proof] Yes, a very nice proof of the necessary and sufficient properties for the MIU system!

>>>> **u/None** [+2]  (18 hours later)
>>>> 
>>>> Beautiful, thank you! I know it's a little redundant to point this out, since it was explicitly stated in the chapter, but for the sake of completion the python should include
>>>> 
>>>>      elif S.count('M') > 1: return False

>> **u/None** [+2]  (a day later)
>> 
>> [deleted]

>>> **u/redstonerodent** [+1]  *High Council of Gallifrey* (a day later)
>>> 
>>> If your formal system has the rule of inference "If x is a theorem and x->y is a theorem, then y is a theorem", you'll have to add more theorems. Achilles thinks "(x&(x->y))->y" should be a rule of inference, but the Tortoise instead includes each instantiation of it as an axiom. If he were willing to accept modus ponens, having as axioms A and B immediately proves the theorem Z.

>> **u/None** [+1]  (4 hours later)
>> 
>> If (b) were as simple as you make it, Lewis Carroll's dialogue would not have been anything remarkable or startling. For one thing, Achilles keeps adding rules of inference, they're just not sufficient to convince the Tortoise of anything.
>> 
>> Suppose Achilles simply asks the Tortoise to accept the inference rule of modus ponens, and Tortoise agrees as long as Achilles writes it down in his book. Does Achilles win?
>> 
>> (Edit: I forgot that in the dialogue, Achilles is responsible for writing everything that the Tortoise is asked to accept, so I had to reword the above)
>> 
>> I have more to say about this on [the Wikia page for the Two-Part Invention](http://godel-escher-bach.wikia.com/wiki/Two-Part_Invention).

>>> **u/autowikiabot** [+2]  (4 hours later)
>>> 
>>> #####&#009;
>>> 
>>> ######&#009;
>>> 
>>> ####&#009;
>>>  [**Two-Part Invention**](https://godel-escher-bach.wikia.com/wiki/Two-Part%20Invention) (from Godel-Escher-Bach wikia): [](#sfw) 
>>> 
>>> ---
>>> >*Bach also wrote fifteen two part inventions. This two-part Dialogue was written not by me* [Hofstadter]*, but by Lewis Carroll in 1895. Carroll borrowed Achilles and the Tortoise from Zeno, and I in turn borrowed them from Carroll. The topic is the relation between reasoning, reasoning about reasoning, reasoning about reasoning about reasoning, and so on. It parallels, in a way, Zeno’s paradoxes about the impossibility of motion, seeming to show, by using infinite regress, that reasoning is impossible. It is a beautiful paradox, and is referred to several times later in the book.* (p. viii)
>>> >
>>> >^Interesting: [^Three-Part ^Invention](https://godel-escher-bach.wikia.com/wiki/Three-Part Invention) ^| [^Chapter ^1](https://godel-escher-bach.wikia.com/wiki/Chapter 1) ^| [^Introduction](https://godel-escher-bach.wikia.com/wiki/Introduction) 
>>> 
>>> ^Parent ^commenter ^can [^toggle ^NSFW](http://www.np.reddit.com/message/compose?to=autowikiabot&subject=AutoWikibot NSFW toggle&message=%2Btoggle-nsfw+cpjajld) ^or[](#or) [^delete](http://www.np.reddit.com/message/compose?to=autowikiabot&subject=AutoWikibot Deletion&message=%2Bdelete+cpjajld)^. ^Will ^also ^delete ^on ^comment ^score ^of ^-1 ^or ^less. ^| [^(FAQs)](http://www.np.reddit.com/r/autowikiabot/wiki/index) ^|  [^Source](https://github.com/Timidger/autowikiabot-py)
>>>  ^(Please note this bot is in testing. Any help would be greatly appreciated, even if it is just a bug report! Please checkout the) [^source ^code](https://github.com/Timidger/autowikiabot-py) ^(to submit bugs)

>>> **u/redstonerodent** [+1]  *High Council of Gallifrey* (8 hours later)
>>> 
>>> The Tortoise only accepts statements written in the book; I consider those axioms. He refuses to accept statements that Achilles thinks are implied by them. He keeps adding more axioms, but has no way to prove theorems from them-no rules of inference.

>>>> **u/None** [+2]  (13 hours later)
>>>> 
>>>> I suppose that's a reasonable way to put it.
>>>> 
>>>> Tortoise keeps taking the things that Achilles intends to be rules of inference, and turns them into axioms of the system, leaving a system of nothing but axioms with no deductive power.
>>>> 
>>>> The conclusion I come to is that, if you have some axioms and you want to make them useful, it's not enough to add a rule of inference -- at least once, you also have to add a mutual understanding that the rule has a purpose. "This isn't just a proposition to be manipulated like the other axioms. We're going to *use* it. When it implies things, we're going to *believe* them."

> **u/None** [+8]  (an hour later)
> 
> Had a lot of fun playing around with the MU puzzle. Took me a while to decide the problem was unsolvable, but now I'm confident it is, because: 
> 
> a) you need to end up with no Is in your string  
> b) the only way to remove an I is 3 at a time. To remove all Is you need a number of Is that is divisible by 3.  
> c) the only way to generate an I is by doubling the entire string (except the M). This gives you twice as many Is as before.  
> d) no number that is not divisible by 3 can be doubled and then be divisible by 3. (x % 3 != 0 means 2x % 3 != 0).

> **u/None** [+4]  (2 hours later)
> 
> [deleted]

>> **u/xamueljones** [+3]  *My arch-enemy is entropy* (2 hours later)
>> 
>> Oops. Thanks for the catch!
>> 
>> As a side note, I think of the I-Mode as when we think on a meta-level about the system and it sounds like a mathematical formulation of I-Mode would be first-order, second-order, and other higher orders of logic. Which means that M-Mode for thinking within the system which can be the standard laws of logic, and the first and second order logic systems is I-Mode.
>> 
>> In simple English, M-Mode is thinking directly about the system and I-Mode is thinking about the system on a meta-level, and on a meta-meta level.
>> 
>> Before people bring up the obvious extension of a meta-meta-meta-... level. I have only this to say. There is no such thing. We never have any need to do so in real life. There is no need to think in more than three levels about the system (system, meta, and meta-meta). I think it's proven somewhere that third, fourth, fifth, and etc. orders of logic are equally as powerful as second order logic and don't really contribute anything new (maybe restating some theorems in a different way can help, but that's it for their benefits).
>> 
>> Here's a fun meta joke:
>> 
>> I'm
>> 
>> So
>> 
>> Meta
>> 
>> Even
>> 
>> This
>> 
>> Acronym

>>> **u/None** [+5]  (6 hours later)
>>> 
>>> I don't think your claim about repeated levels of meta-reasoning is true.
>>> 
>>> For one thing, category theorists, type theorists, and so on, need to allow for an arbitrary number of levels of meta-reasoning, or else some statements become unstateable.
>>> 
>>> In category theory, you can't make a claim about "all categories" without encountering [Russell's paradox](http://en.wikipedia.org/wiki/Russell%27s_paradox). You have to create a category of "all small categories", that is, categories that are 'normal' and don't get all meta about category theory. The category of all small categories cannot be a small category, so call it a 2-category.
>>> 
>>> If you wanted to make a claim about the category of all 2-categories, you'd need that to be a 3-category. And so on. 3-categories are not the same as 2-categories.
>>> 
>>> There might be particular propositional systems where third-order logic is the same as second-order logic -- this is about where I run out of mathematical background -- but I'd want you to at least show me an example of such a system.

>>>> **u/None** [+2]  (20 hours later)
>>>> 
>>>> Technically speaking, third-order logic *can* be written down completely inside second-order logic (as /u/xamueljones notes).  However, in [dependent type theory](http://www.cs.ucsb.edu/~benh/290C_W15/papers/Calculus%20of%20Inductive%20Constructions.pdf) we generally find it useful to have an infinite hierarchy of universes available precisely for the sake of making statements that *appear* self-referential, or "impredicative".
>>>> 
>>>> Of course, non-homotopy type theories are mostly constructive, meaning that they simply don't allow us to state undecidable/unprovable propositions as "believed" theorems: once we "go intuitionistic" and require all propositions to be proved in order to be believed (possibly via exhibiting some trivial data object, as with "proving" the "proposition" `Nat` by exhibiting the natural number 1), we can get a well-behaved logic with an infinite hierarchy of universes and no paradoxes.  We just refuse to believe the Law of the Excluded Middle (`forall P. P \/ ~P`) when we can't actually exhibit a finite-time decision-procedure for the proposition `P` in question.

>>>> **u/autowikibot** [+1]  (6 hours later)
>>>> 
>>>> #####&#009;
>>>> 
>>>> ######&#009;
>>>> 
>>>> ####&#009;
>>>>  [**Russell's paradox**](https://en.wikipedia.org/wiki/Russell%27s%20paradox): [](#sfw) 
>>>> 
>>>> ---
>>>> 
>>>> >
>>>> 
>>>> >In the [foundations of mathematics](https://en.wikipedia.org/wiki/Foundations_of_mathematics), __Russell's paradox__ (also known as __Russell's antinomy__), discovered by [Bertrand Russell](https://en.wikipedia.org/wiki/Bertrand_Russell) in 1901, showed that some attempted formalizations of the [naive set theory](https://en.wikipedia.org/wiki/Naive_set_theory) created by [Georg Cantor](https://en.wikipedia.org/wiki/Georg_Cantor) led to a contradiction. The same paradox had been discovered a year before by [Ernst Zermelo](https://en.wikipedia.org/wiki/Ernst_Zermelo) but he did not publish the idea, which remained known only to [Hilbert](https://en.wikipedia.org/wiki/David_Hilbert), [Husserl](https://en.wikipedia.org/wiki/Edmund_Husserl) and other members of the [University of Göttingen](https://en.wikipedia.org/wiki/University_of_G%C3%B6ttingen).
>>>> 
>>>> >According to naive set theory, any definable collection is a [set](https://en.wikipedia.org/wiki/Set_(mathematics\)). Let *R* be the set of all sets that are not members of themselves. If *R* is not a member of itself, then its definition dictates that it must contain itself, and if it contains itself, then it contradicts its own definition as the set of all sets that are not members of themselves. This contradiction is Russell's paradox. Symbolically:
>>>> 
>>>> >>
>>>> 
>>>> >In 1908, two ways of avoiding the paradox were proposed, Russell's [type theory](https://en.wikipedia.org/wiki/Type_theory) and the [Zermelo set theory](https://en.wikipedia.org/wiki/Zermelo_set_theory), the first constructed [axiomatic set theory](https://en.wikipedia.org/wiki/Axiomatic_set_theory). Zermelo's axioms went well beyond [Frege](https://en.wikipedia.org/wiki/Frege)'s axioms of [extensionality](https://en.wikipedia.org/wiki/Axiom_of_extensionality) and unlimited [set abstraction](https://en.wikipedia.org/wiki/Set_builder_notation), and evolved into the now-canonical [Zermelo–Fraenkel set theory](https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory) (ZF). 
>>>> 
>>>> >====
>>>> 
>>>> >[**Image**](https://i.imgur.com/fkfalmu.png) [^(i)](https://commons.wikimedia.org/wiki/File:Bertrand_Russell_transparent_bg.png)
>>>> 
>>>> ---
>>>> 
>>>> ^Interesting: [^Universal ^set](https://en.wikipedia.org/wiki/Universal_set) ^| [^Grelling–Nelson ^paradox](https://en.wikipedia.org/wiki/Grelling%E2%80%93Nelson_paradox) ^| [^Paradox](https://en.wikipedia.org/wiki/Paradox) ^| [^Cantor's ^diagonal ^argument](https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument) 
>>>> 
>>>> ^Parent ^commenter ^can [^toggle ^NSFW](/message/compose?to=autowikibot&subject=AutoWikibot NSFW toggle&message=%2Btoggle-nsfw+cpjcq0b) ^or[](#or) [^delete](/message/compose?to=autowikibot&subject=AutoWikibot Deletion&message=%2Bdelete+cpjcq0b)^. ^Will ^also ^delete ^on ^comment ^score ^of ^-1 ^or ^less. ^| [^(FAQs)](http://www.np.reddit.com/r/autowikibot/wiki/index) ^| [^Mods](http://www.np.reddit.com/r/autowikibot/comments/1x013o/for_moderators_switches_commands_and_css/) ^| [^Magic ^Words](http://www.np.reddit.com/r/autowikibot/comments/1ux484/ask_wikibot/)

>>>> **u/xamueljones** [+1]  *My arch-enemy is entropy* (7 hours later)
>>>> 
>>>> I don't really have the mathematics backgrounds to explain too well the bit I learned about higher-order logics, but it was from people, or academic communities, who I do trust to get their maths right.
>>>> 
>>>> First is /u/EliezerYudkowsky's post on LessWrong called the [Second Order Logic: The Controversy](http://lesswrong.com/lw/g7n/secondorder_logic_the_controversy/) with the quote:
>>>> 
>>>> > Once you make the jump to second-order logic, you're *done* - so far as anyone knows (so far as I know) there's *nothing* more powerful than second-order logic in terms of *which models it can characterize*.
>>>> 
>>>> And there was a neat academic textbook somewhere I can't find which also explained this, but I dug up this [PDF download](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0CCUQFjAB&url=https%3A%2F%2Fstaff.science.uva.nl%2Fj.vanbenthem%2Fdocs%2FHOL.pdf&ei=PSMKVZ6nFYOigwTyuIOQCw&usg=AFQjCNHUip3_EkBm9lI6y4dqmOzRhfC7ww&sig2=YQWODgv5hv2St46NQv5TvQ&bvm=bv.88528373,d.eXY) online which makes for some really complex reading and I spent quite a while skimming it to be sure it supported me with what I *think* is a proof for the following quote on page number 30: 
>>>> 
>>>> > The logic and model theory of L[2] exhibit the same phenomena as those of L[omega]: a fluid border line with set theory, and a few systematic results. Indeed, in a sense, **higher-order logic does not offer anything new**.
>>>> 
>>>> Look below to my reply to /u/rspeer's other comment for why meta-meta-meta doesn't work.

>>>>> **u/Ty-Guy9** [+1]  *Wants to become a "FAI"* (17 hours later)
>>>>> 
>>>>> Ah, I see that I have again missed a crucial factor in our discussion, Mr. Jones. I must have missed this post before writing my other replies below, and for that I apologize. I see now that you have made a valiant effort to whittle down some part of what you learned from these complex texts, to make it simple enough for the layman. I cannot follow much of what is said in either of the documents you have linked, but if those quotes are in fact descriptions pertaining to the very thing we are talking about, then I suppose I also feel inclined to trust these 'expert opinions,' even before having my own understanding just yet.
>>>>> 
>>>>> I may have a go at Eliezer's dialogue there. It seems to build on top of a tower of long documents he wrote before, but with a few tricks or given enough time I might sort it out. At least his *seem* like the more accessible writings for those lacking in formal training. Then again, it's probably not worth the time while I have so much else to read, of his and of others, on similarly engaging (and yet only theoretically useful -- sigh) topics.

>>> **u/Ty-Guy6** [+2]  (5 hours later)
>>> 
>>> Hmm. No added utility from 3rd-order meta? Seems hard to prove or disprove off the cuff, but let me think out loud. Suppose the goal is to get enough carrots to eat:
>>> 
>>> * System-level could be picking carrots and eating them.
>>> 
>>> * Meta-level could be planting and caring for carrot seeds so that you can eat them later.
>>> 
>>> * Meta-meta-level could be forming tools to make carrot-planting more efficient, or perhaps hiring workers and paying them from carrot sales; there are probably a lot of branches we could follow.
>>> 
>>> * Meta-meta-meta-level could be ... economics, mechanical/genetic engineering, i.e. fields that directly improve upon your level-2 strategy.
>>> 
>>> * Metax4-level could be the scientific system itself, or other systems of thought/action which tend to develop those more directly useful fields of level metax3. It is possible that your religion/worldview could be included here, or otherwise at level metax5.
>>> 
>>> Hmm. So far I subscribe to this progression. Would you also accept it as a counterexample, or does it fit into your theory somehow?
>>> 
>>> I make no claims of this shedding light on the author's M/U/I thought theory, but at the least it's a fun side-track.

>>>> **u/xamueljones** [+3]  *My arch-enemy is entropy* (7 hours later)
>>>> 
>>>> Sorry I didn't reply earlier. My computer shut down for a bit.
>>>> 
>>>> I feel like this comment isn't talking about thinking in a more meta sense, but rather categorizing simpler systems like farming within a bigger system like economics.
>>>> 
>>>> Using your example of carrot picking:
>>>> 
>>>> * System-Level - The basic steps to picking a carrot which we can easily automate a robot to do for us. Steps are of the form: check carrot for freshness, then pick or leave alone. This level is the task itself and methods to perform the task.
>>>> 
>>>> * Meta-Level - How well does the robot do it's job? Does it work better on sunny days than rainy days? How quick and efficient is it at its job? What mistakes does it make, or what can it do better? This level is thinking *about* the task and what can be changed about the methods to perform the task.
>>>> 
>>>> * Meta-Meta-Level - How are we examining the robot's effectiveness? How do we come up with new plans for the robot? How were we thinking when we came up with particularly bad plans, or particularly good plans? How do we structure our planning process? This level is thinking about how we are thinking about the task. This is where you examine your thought processes about how you deal with problems, or in other words, how do you structure your planning to solve the problem.
>>>> 
>>>> * Meta-Meta-Meta...-Level - This is where things break down, because the last level was analyzing how you approach problems in the first place and is extremely abstract and is very far removed from the original problem. To go any further would be something like this very discussion where I explained how meta-thinking works. But looking at the problem from a multi-meta viewpoint is still part of the meta-meta level since it examines how you approach the problem in the first place. Therefore this level doesn't seem to offer any further insights to help with solving the problem.
>>>> 
>>>> The flaw you made in your comment is that you confused meta-thinking with thinking more abstractly. But meta-levels should retain the same focus on the same problem/system as the object-level, with the only differences being that you step back from solving the problem to *how* you solve the problem to how you *think* about how you solve the problem.
>>>> 
>>>> A real life example is the HPMOR planning threads:
>>>> 
>>>> The [System-Level/Unified Solutions Thread](http://www.reddit.com/r/HPMOR/comments/2xkbb8/spoilers_113_unified_solutions_thread/) which is about the presented solutions to pass the Final Exam, [Meta-Level/Planning Thread](http://www.reddit.com/r/HPMOR/comments/2xiabn/spoilers_ch_113_planning_thread/) which is about examining the problem and to see how a possible solution would be structured, and [Meta-Meta-Level/Meta Meta Planning Thread](http://www.reddit.com/r/HPMOR/comments/2xhqus/the_meta_meta_planning_thread/) which is about discussing how to discuss the problem and its solutions.
>>>> 
>>>> In fact, /u/alexanderwales stated the purpose of a meta-meta-planning thread as:
>>>> 
>>>> > This is not a place to post solutions.
>>>> 
>>>> > This is not a place to discuss the problem.
>>>> 
>>>> > This is the place to discuss how to discuss the problem and its solutions.
>>>> 
>>>> Furthermore, note that not a single person in a community of thousands even *tried* posting a Meta-Meta-Meta-Level thread, because it just doesn't make sense on a logical* level to do so.
>>>> 
>>>> EDIT: *When I said "on a logical level" I should have said "on a intuitive level", because I'm referring to how humans think about meta-ness and not the theory of logic.

>>>>> **u/None** [+1]  (7 hours later)
>>>>> 
>>>>> What do you mean, it doesn't make logical sense? There might not be a lot to say, but that's different from not making logical sense.
>>>>> 
>>>>> Your comment about meta-meta-level threads would fit in perfectly in a meta-meta-meta-level thread.

>>>>>> **u/xamueljones** [+1]  *My arch-enemy is entropy* (7 hours later)
>>>>>> 
>>>>>> I didn't say that there was very little to say, I said (poorly) that anything we can say on a higher level can be rephrased to be defined from a meta-meta level only.
>>>>>> 
>>>>>> Also, I defined the Meta-Meta-Level to be discussing how to think about thinking about the problem.
>>>>>> 
>>>>>> The comment about meta-meta level threads is still on a meta-meta level, because it's still discussing how to think about thinking about the problem. In other words, the first level is about the problem, the second level is about how to approach the problem, and the third level is about approaching all of the possible ways to handle solving the problem. The distinction is really subtle, but one possible way to approach all of the possible approaches to solving the problem is to break it down into levels of meta-ness. Therefore, my comment about the different meta levels stays on the meta-meta-level instead of the "meta-meta-meta-level".
>>>>>> 
>>>>>> To best understand it, I think of it like the idea of recursion. The first level is the base case, the second level is the demonstration of the first inductive/recursive step, and the third level is the actual recursion where it even contains recursive statements about itself.
>>>>>> 
>>>>>> One last point is when I moved from one level to another, I clearly noticed a change in my patterns of thinking about the problem, but I don't experience any similar change when I try thinking about the meta-meta level on another meta-level, but that could be chalked up to me not knowing what such a level of thought would be like if it exists, so it's not a very good reason to support my argument.

>>>>>>> **u/None** [+1]  (8 hours later)
>>>>>>> 
>>>>>>> I think what you're describing is the ease with which the human mind will jump up more meta-levels, once it's already done so once. You just don't notice it, because you're using basically the same thought patterns you used before.
>>>>>>> 
>>>>>>> In a forum, it's clear that meta-meta issues and meta-meta-meta issues could go in the same thread -- humans are not so slavishly devoted to categories that they'd have to distinguish them.
>>>>>>> 
>>>>>>> Math won't usually let you get away with not making the distinction.
>>>>>>> 
>>>>>>> Also, just because you've described a countably infinite number of meta-levels at once, that doesn't mean things are settled, because there are more than a countably infinite number of ordinals. Suppose this message board has gotten very meta indeed, and I wanted to object to the very notion of putting meta^2 issues, meta^3 issues, meta^4 issues, and so on in the same thread. In what thread would I raise my objection?

>>>>>>>> **u/xamueljones** [+1]  *My arch-enemy is entropy* (8 hours later)
>>>>>>>> 
>>>>>>>> But the problem you are describing is that whenever I need to talk about one specific meta-level, I always have to go up another level which leads to recursing until there is an infinitely number of meta levels. Even then, your example of "meta^2 issues, meta^3 issues, meta^4 issues, and so on" requires even *more* meta levels which  gets very confusing and it's hard to say what each level brings to the table in terms of telling us what more we learn about a given problem which started all of this meta-ness in the first place. It's a confusing and paradoxical mess.
>>>>>>>> 
>>>>>>>> If we use the system of three levels I describe, it better matches our intuitive understanding of meta-ness, where discussing the problem goes in the meta-level, and **anything** about the meta-level goes in the meta-meta-level (even about the meta-meta-level). Hence, the answer the thread your objection goes in would be the meta-meta thread.
>>>>>>>> 
>>>>>>>> Finally, the point is that while stating anything with multiple metas can make sense and are valid statements, they are not any more *powerful* in a meaningful sense than simply stating it on the meta-meta level anyway. Everything above the meta-meta-level can be rephrased to be part of the meta-meta level.
>>>>>>>> 
>>>>>>>> I wouldn't apply my reasoning about meta-ness to strict formal logical (or set) theory because I'm not a mathematician and I wouldn't know how to prove something like this. But what I'm arguing is that the system of three levels is how humans most naturally think in a meta sense, and I thought the mathematics supported me (sorta) with the evidence I cited [here](http://www.reddit.com/r/rational/comments/2zhouc/geb_discussion_2_chapter_1_the_mupuzzle/cpjgamo) about all higher order logics being equivalent to second order logic being the same as all higher meta-levels being equivalent to the meta-meta-level.
>>>>>>>> 
>>>>>>>> Sorry I take so long to write my responses. I keep going over them to be sure that I'm clear on what I'm trying to say.

>>>>>>>>> **u/None** [+3]  (10 hours later)
>>>>>>>>> 
>>>>>>>>> I think what you're saying, then, is that the human mind can generalize in ways that logic can't -- that we can jump out of "all the systems" at the same time, even when it's impossible to define what that means.
>>>>>>>>> 
>>>>>>>>> The system you get by jumping out of "all the systems" is just another system that you haven't jumped out of yet, which is contradictory, so you can't really describe what it means to jump out of all the systems.
>>>>>>>>> 
>>>>>>>>> The claim that the human mind can do things that can never be described is a claim that some make, but you should be sure you're making it. Later in GEB you should have to think hard about this.
>>>>>>>>> 
>>>>>>>>> To indicate why it's a problem to talk about "all the levels", I'm going to make a dialogue between a ridiculously mathematically literal version of me, and a puppet version of you whose mouth I'll put words in:
>>>>>>>>> 
>>>>>>>>> * Me: So what if I want to object to having a countably infinite number of meta-levels of discussion in the same thread?
>>>>>>>>> * You: They're all the same meta-level. They go in the meta^2 thread.
>>>>>>>>> * Me: I disagree, because I think it's important to clarify when you're trying to talk about "all the things" in a system from outside of it. So I'm going to have to disagree in a new meta^ω thread.
>>>>>>>>> * You: Meta^ω threads are silly. You should have put that in the meta^2 thread.
>>>>>>>>> * Me: Isn't that a pretty meta^(ω+1) thing to say?
>>>>>>>>> * You: No. It's a meta^2 thing to say. What you call meta^(ω+2) would also be what I call meta^(2).
>>>>>>>>> * Me: I object to that on a meta^(2ω) level.
>>>>>>>>> * You: There *is* no meta^(2ω) level. There's no meta^(3ω) level either, or --
>>>>>>>>> * Me: Apparently there's a meta^(ω^2) level, because you're currently arguing on it.
>>>>>>>>> * You: You're going to keep naming these levels after [ordinal numbers](http://en.wikipedia.org/wiki/Ordinal_number), and I'm going to keep saying that they're just meta^(2).
>>>>>>>>> * Me: Which meta-levels, exactly, can I name that you'd say are just meta^(2)?
>>>>>>>>> * You: ALL OF THEM.
>>>>>>>>> * Me: All of them in what set?
>>>>>>>>> * You: The set of all the meta-levels you can name.
>>>>>>>>> * Me: But my names are all ordinal numbers.
>>>>>>>>> * You: All of those, then.
>>>>>>>>> * Me: There is no set of all ordinal numbers. Any set of ordinal numbers you can pick defines an ordinal number that isn't in that set. You have to say 'class of ordinal numbers', or 'set^(2) of ordinal numbers', to avoid a paradox.
>>>>>>>>> * You: Fine, all of them in the *set^(2)* of ordinal numbers.
>>>>>>>>> * Me: I'm just going to have to make a different set^2 that's isomorphic to the ordinal numbers and start naming meta-levels after those.
>>>>>>>>> * You: I'm not interested in talking about sets^2 of sets of meta-levels anymore.
>>>>>>>>> * Me: Which ones are you not interested in talking about?
>>>>>>>>> * You: ALL OF THEM.
>>>>>>>>> * Me: That's a nice set^3 of sets^2 of sets of meta-levels you've just defined.
>>>>>>>>> * You: I'm also not interested in sets^3 or sets^4 or...
>>>>>>>>> 
>>>>>>>>> Apologies for the puppetry. It'd take a long time to make anything like this conversation happen naturally.
>>>>>>>>> 
>>>>>>>>> How many times could this argument escalate? Could you ever respond to "all the ways" I might escalate the argument to a new meta-level?

>>>>>>>>>> **u/xamueljones** [+2]  *My arch-enemy is entropy* (10 hours later)
>>>>>>>>>> 
>>>>>>>>>> Thanks for that dialogue. I know you aren't trying to make me look silly, but it really does help me understand what you seem to be understanding from my argument and I think I understand how to clarify the difference between our arguments.
>>>>>>>>>> 
>>>>>>>>>> To me, all of the potential levels of meta you could ever name, 1, 2, 3, ω, ω+1, ω^2, ordinal sets, etc, etc... are mainly used to comment on other levels which are meta. However, the critical distinction we seem to be making is that I'm an extremely practical (almost utilitarian) person and when I use meta-thinking, I look at how the different levels relate directly to the system-level problem. I have not ever found anything higher than the meta-meta level which provide useful insights into the system-problem itself which can't also be restated somehow onto the meta-meta level. Hence it seems like how people think about meta-ness can be simplified to the bottom three levels.
>>>>>>>>>> 
>>>>>>>>>> The statement about my argument you said was:
>>>>>>>>>> 
>>>>>>>>>> > the human mind can generalize in ways that logic can't -- that we can jump out of "all the systems" at the same time, even when it's impossible to define what that means.
>>>>>>>>>> 
>>>>>>>>>> I don't...*think* I'm making that claim, but rather the case that the human mind can jump out of multiple systems at a time, for a lot of meta-levels (but I don't mean all of them at once). It's just that for practical purposes to solve the original problem, jumping up to the metax4 level, for example, is equally as helpful as jumping to the metax2 level. Sure, on the metax4 level, you now can make statements about the metax3 and metax2 level, but it's not helpful for solving the problem and any other possible insights can also be found on the metax2 level.
>>>>>>>>>> 
>>>>>>>>>> I just thought I had something really interesting when I found out about the mathematical implications concerning higher order logics which seems to back me up with the statements in how higher-order logics are more expressive than second-order logic, but are only at most as powerful as second-order logic.
>>>>>>>>>> 
>>>>>>>>>> I'm going to go to bed now, so if you have any more responses or counter-arguments, I won't be posting my reply for a while.

>>>>>>>>>>> **u/Transfuturist** [+1]  *Carthago delenda est.* (12 hours later)
>>>>>>>>>>> 
>>>>>>>>>>> > ω+1
>>>>>>>>>>> 
>>>>>>>>>>> To be pedantic, you mean 1+ω. Addition with transfinite ordinals is noncommutative.

>>>>>>>>>> **u/autowikibot** [+1]  (10 hours later)
>>>>>>>>>> 
>>>>>>>>>> #####&#009;
>>>>>>>>>> 
>>>>>>>>>> ######&#009;
>>>>>>>>>> 
>>>>>>>>>> ####&#009;
>>>>>>>>>>  [**Ordinal number**](https://en.wikipedia.org/wiki/Ordinal%20number): [](#sfw) 
>>>>>>>>>> 
>>>>>>>>>> ---
>>>>>>>>>> 
>>>>>>>>>> >
>>>>>>>>>> 
>>>>>>>>>> >In [set theory](https://en.wikipedia.org/wiki/Set_theory), an __ordinal number__, or __ordinal__, is the [order type](https://en.wikipedia.org/wiki/Order_type) of a [well-ordered set](https://en.wikipedia.org/wiki/Well-order). They are usually identified with [hereditarily](https://en.wikipedia.org/wiki/Hereditary_property) [transitive sets](https://en.wikipedia.org/wiki/Transitive_set). Ordinals are an extension of the [natural numbers](https://en.wikipedia.org/wiki/Natural_number) different from [integers](https://en.wikipedia.org/wiki/Integer) and from [cardinals](https://en.wikipedia.org/wiki/Cardinal_number). Like other kinds of numbers, ordinals can be added, multiplied, and exponentiated.
>>>>>>>>>> 
>>>>>>>>>> >Ordinals were introduced by [Georg Cantor](https://en.wikipedia.org/wiki/Georg_Cantor) in 1883  to accommodate [infinite](https://en.wikipedia.org/wiki/Infinite_set) sequences and to classify [derived sets](https://en.wikipedia.org/wiki/Derived_set_(mathematics\)), which he had previously introduced in 1872 while studying the uniqueness of [trigonometric series](https://en.wikipedia.org/wiki/Trigonometric_series). 
>>>>>>>>>> 
>>>>>>>>>> >Two sets *S* and *S'* have the same *cardinality* if there is a [bijection](https://en.wikipedia.org/wiki/Bijection) between them (i.e. there exists a function f that is both [injective](https://en.wikipedia.org/wiki/Injective) and [surjective](https://en.wikipedia.org/wiki/Surjective), that is it maps each element *x* of *S* to a unique element *y* = *f*(*x*) of *S'* and each element *y* of *S'* comes from exactly one such element *x* of *S*).
>>>>>>>>>> 
>>>>>>>>>> >====
>>>>>>>>>> 
>>>>>>>>>> >[**Image**](https://i.imgur.com/qZztSnc.png) [^(i)](https://commons.wikimedia.org/wiki/File:Omega-exp-omega-labeled.svg) - *Representation of the ordinal numbers up to ω^ω. Each turn of the spiral represents one power of ω*
>>>>>>>>>> 
>>>>>>>>>> ---
>>>>>>>>>> 
>>>>>>>>>> ^Interesting: [^Ordinal ^number ^\(linguistics)](https://en.wikipedia.org/wiki/Ordinal_number_\(linguistics\)) ^| [^Successor ^ordinal](https://en.wikipedia.org/wiki/Successor_ordinal) ^| [^List ^of ^military ^corps](https://en.wikipedia.org/wiki/List_of_military_corps) 
>>>>>>>>>> 
>>>>>>>>>> ^Parent ^commenter ^can [^toggle ^NSFW](/message/compose?to=autowikibot&subject=AutoWikibot NSFW toggle&message=%2Btoggle-nsfw+cpjkv0o) ^or[](#or) [^delete](/message/compose?to=autowikibot&subject=AutoWikibot Deletion&message=%2Bdelete+cpjkv0o)^. ^Will ^also ^delete ^on ^comment ^score ^of ^-1 ^or ^less. ^| [^(FAQs)](http://www.np.reddit.com/r/autowikibot/wiki/index) ^| [^Mods](http://www.np.reddit.com/r/autowikibot/comments/1x013o/for_moderators_switches_commands_and_css/) ^| [^Magic ^Words](http://www.np.reddit.com/r/autowikibot/comments/1ux484/ask_wikibot/)

>>>>>>>>>> **u/Ty-Guy6** [+1]  (11 hours later)
>>>>>>>>>> 
>>>>>>>>>> Maybe not to the point, but I have heard similar things before, from reputable sources, as jumping out of "all the systems." Perhaps these systems could be taken to include also the system in which the phrase is offered? In other words, 'I'd like to point you outside of the box, but it's hard because this conversation itself is within it?'
>>>>>>>>>> 
>>>>>>>>>> As for me, I believe the human mind is capable of things outside of all the systems humans have so far defined, which include such things as language, logic, and mathematics. (I don't mean Language, Logic, and Mathematics, the theoretical ideals of that which we now know.) We may also be able to describe those things later using means not readily available now.
>>>>>>>>>> 
>>>>>>>>>> Take this as you will, the thread grows long. ;)

>>>>>>>>> **u/Ty-Guy6** [+1]  (10 hours later)
>>>>>>>>> 
>>>>>>>>> Hmm. After some consideration, I'm not convinced (at least not yet) of the logic of the collapse of metax3 into metax2. When I followed the logic through in my head*, it seemed to cause further collapses, until I eventually questioned why metax2 might not be a part of the system itself. But I decided that it would be rather odd to say that thinking about how we solve the problem (metax1) is the same as solving the problem. While on the other hand, metax3 makes sense as-is: thinking about how we think about how we think about solving the problem is a thing, and should be credited as being separate from the lower levels.
>>>>>>>>> 
>>>>>>>>> *My thought path: I thought of the problem as a series of introductions to a book. It seems to fit the definition of meta-writing. I thought of an author who writes an introduction to his introduction, (metax2) and an introduction to that (metax3). Then I realized that they are all introductions, after all, so they should all fit under metax1. And if introductions, why, they are also all part of the book! Metax0! And this is where I saw my mistake as I realized that introductions are still introductions, not part of the body text.
>>>>>>>>> 
>>>>>>>>> EDIT: But yes, clearly humans think so very rarely on the metax3 level that it is almost exclusively just a thought exercise whenever we refer to it. As examples, intros to intros to intros would be overkill, and I don't even know the symbol (although we probably have one) for what falls next in the pattern of addition-multiplication-powers-...

>>>>>>>>>> **u/xamueljones** [+2]  *My arch-enemy is entropy* (11 hours later)
>>>>>>>>>> 
>>>>>>>>>> After exponents, it's [tetration](http://en.wikipedia.org/wiki/Tetration). The most interesting bit to me is that for addition, multiplication, and exponentiation, you use algebra if there's a variable in the term. But you have to use calculus if there's a variable in tetration. My brain hurt a little when I had to find the limit of x^x^x^x^x^x... as x approaches number like √2 or e for an infinite tower of x's.

>>>>>>>>>>> **u/autowikibot** [+1]  (11 hours later)
>>>>>>>>>>> 
>>>>>>>>>>> #####&#009;
>>>>>>>>>>> 
>>>>>>>>>>> ######&#009;
>>>>>>>>>>> 
>>>>>>>>>>> ####&#009;
>>>>>>>>>>>  [**Tetration**](https://en.wikipedia.org/wiki/Tetration): [](#sfw) 
>>>>>>>>>>> 
>>>>>>>>>>> ---
>>>>>>>>>>> 
>>>>>>>>>>> >
>>>>>>>>>>> 
>>>>>>>>>>> >In [mathematics](https://en.wikipedia.org/wiki/Mathematics), __tetration__ (or __hyper-4__) is the next [hyper operator](https://en.wikipedia.org/wiki/Hyperoperation) after [exponentiation](https://en.wikipedia.org/wiki/Exponentiation), and is defined as iterated exponentiation. The word was coined by [Reuben Louis Goodstein](https://en.wikipedia.org/wiki/Reuben_Louis_Goodstein), from [tetra-](https://en.wikipedia.org/wiki/Tetra-) (four) and [iteration](https://en.wikipedia.org/wiki/Iterated_function). Tetration is used for the [notation of very large numbers](https://en.wikipedia.org/wiki/Large_numbers#Standardized_system_of_writing_very_large_numbers). Shown here are examples of the first four [hyper operators](https://en.wikipedia.org/wiki/Hyper_operator), with tetration as the fourth (and [succession](https://en.wikipedia.org/wiki/Successor_function), the unary operation denoted  taking  and yielding the number after , as the 0th):
>>>>>>>>>>> 
>>>>>>>>>>> >
>>>>>>>>>>> 
>>>>>>>>>>> >* [Addition](https://en.wikipedia.org/wiki/Addition)
>>>>>>>>>>> 
>>>>>>>>>>> >>
>>>>>>>>>>> 
>>>>>>>>>>> >>*n* copies of 1 added to *a*.
>>>>>>>>>>> 
>>>>>>>>>>> >* [Multiplication](https://en.wikipedia.org/wiki/Multiplication)
>>>>>>>>>>> 
>>>>>>>>>>> >>
>>>>>>>>>>> 
>>>>>>>>>>> >>*n* copies of *a* combined by addition.
>>>>>>>>>>> 
>>>>>>>>>>> >* [Exponentiation](https://en.wikipedia.org/wiki/Exponentiation)
>>>>>>>>>>> 
>>>>>>>>>>> >>
>>>>>>>>>>> 
>>>>>>>>>>> >>*n* copies of *a* combined by multiplication.
>>>>>>>>>>> 
>>>>>>>>>>> >* Tetration
>>>>>>>>>>> 
>>>>>>>>>>> >>
>>>>>>>>>>> 
>>>>>>>>>>> >>*n* copies of *a* combined by exponentiation, right-to-left.
>>>>>>>>>>> 
>>>>>>>>>>> >where each operation is defined by iterating the previous one (the next operation in the sequence is [pentation](https://en.wikipedia.org/wiki/Pentation)). Tetration is not an [elementary function](https://en.wikipedia.org/wiki/Elementary_function).
>>>>>>>>>>> 
>>>>>>>>>>> >Tetration is not an [elementary recursive function](https://en.wikipedia.org/wiki/ELEMENTARY). 
>>>>>>>>>>> 
>>>>>>>>>>> >Here, succession () is the most basic operation; addition () is a primary operation, though for natural numbers it can be thought of as a chained succession of *n* successors of *a*; multiplication () is also a primary operation, though for natural numbers it can be thought of as a chained addition involving *n* numbers *a*; and exponentiation () can be thought of as a chained multiplication involving *n* numbers *a*. Analogously, tetration () can be thought of as a chained power involving *n* numbers *a*. The parameter *a* may be called the base-parameter in the following, while the parameter *n* in the following may be called the *height*-parameter (which is integral in the first approach but may be generalized to fractional, real and complex *heights*, see below).
>>>>>>>>>>> 
>>>>>>>>>>> >====
>>>>>>>>>>> 
>>>>>>>>>>> >[**Image**](https://i.imgur.com/Uf78G43.png) [^(i)](https://commons.wikimedia.org/wiki/File:TetrationComplexColor.png) - *Complex plot of holomorphic tetration*
>>>>>>>>>>> 
>>>>>>>>>>> ---
>>>>>>>>>>> 
>>>>>>>>>>> ^Interesting: [^Pentation](https://en.wikipedia.org/wiki/Pentation) ^| [^Super-logarithm](https://en.wikipedia.org/wiki/Super-logarithm) ^| [^PR ^\(complexity)](https://en.wikipedia.org/wiki/PR_\(complexity\)) 
>>>>>>>>>>> 
>>>>>>>>>>> ^Parent ^commenter ^can [^toggle ^NSFW](/message/compose?to=autowikibot&subject=AutoWikibot NSFW toggle&message=%2Btoggle-nsfw+cpjlx3k) ^or[](#or) [^delete](/message/compose?to=autowikibot&subject=AutoWikibot Deletion&message=%2Bdelete+cpjlx3k)^. ^Will ^also ^delete ^on ^comment ^score ^of ^-1 ^or ^less. ^| [^(FAQs)](http://www.np.reddit.com/r/autowikibot/wiki/index) ^| [^Mods](http://www.np.reddit.com/r/autowikibot/comments/1x013o/for_moderators_switches_commands_and_css/) ^| [^Magic ^Words](http://www.np.reddit.com/r/autowikibot/comments/1ux484/ask_wikibot/)

>>>>>>>>>> **u/xamueljones** [+1]  *My arch-enemy is entropy* (10 hours later)
>>>>>>>>>> 
>>>>>>>>>> I still disagree with your idea of there being a metax3, but if you already read all of my earlier arguments on this subject and have remained unconvinced, then there is nothing more I can say. Regardless, it was a very interesting debate and I had fun clarifying what I think of the concept of 'meta' for others and myself.

>>>>> **u/Ty-Guy6** [+1]  (9 hours later)
>>>>> 
>>>>> Whew! Ok, it seems you have solid grounds for supposing that I am conflating meta- with simply thinking more abstractly. The definition of meta- that we seem to be referring to involves both:
>>>>> 
>>>>> * An exiting of the system to a higher level of abstraction
>>>>> 
>>>>> * Reference, from without the system, to the system
>>>>> 
>>>>> On a related note (pgs 45-47): While it's a reasonable jump to make, so far the author has not connected M/U/I thinking with the prefix "meta-". He talks about "jumping out of the system" and "surveying what the system has done" in the same breath, but hasn't firmly affixed the two together under any name that I can see. I'm not sure whether it's meta- he's referring to when he says "I-mode," or just thinking outside of the box.
>>>>> 
>>>>> That's what got my definitions crossed.

>>>>>> **u/xamueljones** [+1]  *My arch-enemy is entropy* (9 hours later)
>>>>>> 
>>>>>> You're right that Hofstadter doesn't mention "meta-", but it means to be self-referential which fits his themes so well, that I can't believe it won't show up at some point.
>>>>>> 
>>>>>> I agree that he doesn't seem to be talking about it directly in the chapter, but since it relates to so many of his themes and I-Mode looks like it is largely thinking about the system in a meta-sense, I wanted to bring up the idea for discussion.

>>>> **u/None** [+1]  (20 hours later)
>>>> 
>>>> You can always "go up" another "meta-level" of reasoning, forming a more-or-less infinite hierarchy.  *However*, real-life reasoning is mostly abductive, and to reason "well" abductively at very high meta-levels of hierarchy, you need increasing amounts of data.  So the higher the meta-level you go, the "wider" your tree of encompassed "object-level" reasoning systems/categories have to get in order to train your nth-level model well.

> **u/None** [+5]  (5 hours later)
> 
> Wikia links for these chapters:
> 
> * [Chapter 1](http://godel-escher-bach.wikia.com/wiki/Chapter_1) - try questions 10 and 10.1 if you consider the MU-puzzle simple.
> * [Two-Part Invention](http://godel-escher-bach.wikia.com/wiki/Two-Part_Invention) - explains the background behind this dialogue, in case you missed it

> **u/None** [+3]  (an hour later)
> 
> The chapter was mostly pretty basic but an insightful thing was the "working within the system vs. jumping out of the system" idea. I think you could apply this to the rules of our society: most people work within the system of our society, never making observations of it as a whole.  But some people, like clever salesmen, criminals or lawyers are maybe able to jump out of the system and observe it from a more neutral viewpoint and get an advantage because of it.
> 
> Btw, some people over at /r/GEB complained that the schedule is a bit aggressive and speculated that people would drop out at the beginning of April at the latest. I dunno about that myself, we'll see.

>> **u/None** [+3]  (4 hours later)
>> 
>> I'm speculating, specifically, that if you try to cover chapters 7, 8, and 9, as well as their corresponding dialogues, in the same week, it's going to be pretty rough and most people will get left behind.
>> 
>> ...not that /r/geb should claim any particular expertise on successfully completing readthroughs.

> **u/TotesMessenger** [+1]  (2 hours later)
> 
> This thread has been linked to from another place on reddit.
> 
> - [/r/GEB] [Chapter #1: The MU-Puzzle Discussion of GEB](http://np.reddit.com/r/GEB/comments/2zi9i0/chapter_1_the_mupuzzle_discussion_of_geb/)
> 
> - [/r/HPMOR] [Discussion #2 of the Godel, Escher, Bach Read Through](http://np.reddit.com/r/HPMOR/comments/2zijr0/discussion_2_of_the_godel_escher_bach_read_through/)
> 
> [](#footer)*^If ^you ^follow ^any ^of ^the ^above ^links, ^respect ^the ^rules ^of ^reddit ^and ^don't ^vote. ^\([Info](/r/TotesMessenger/wiki/) ^/ ^[Contact](/message/compose/?to=\/r\/TotesMessenger))* [](#bot)

> **u/None** [+1]  (4 hours later)
> 
> Well, the MU thing was kinda obvious if you translate it into numbers.

> **u/Newfur** [+1]  *Crazy like a fox. Literally.* (5 days later)
> 
> Formal systems are pretty much the basis of all rigorous inference. I thus find it kinda important for having remotely accurate beliefs about anything. 
> 
> P-sets or reading for information tend to put me in M-mode, playing Magic or working on my own puts me in I-mode, and meditation and occasional flashes of waking delight put me in U-mode. I'd put a mu-state in with the U-mode, for my part.
> 
> ~~~
> 
> Isomorphism is the soul of metaphor, and that's all I need say about that.
> 
> ~~~
> 
> It's the crab canon!
> 
> Why, you need but jump out of the system. Alternately, lie back and wait for Mr. Tortoise to get repeatedly mugged by reality, the smugly clever little shit.

---

