## SMBC: Bayesian Immortality

* Author: u/None *
* URL: http://smbc-comics.com/index.php?id=4127
* Score: 55

* Created: 2016-05-31T15:12:39

### Post:

[Link to content](http://smbc-comics.com/index.php?id=4127)

### Comments:

> **u/wtfbbc** [+56]  (8 minutes later)
> 
> Mouseover text:
> 
> >I'm just realizing the Venn diagram for people who know the reference and people who like the joke is a null set.
> 
> As a huge SMBC fan, I admit this is approximately accurate tbh

> **u/worldsayshi** [+9]  (17 hours later)
> 
> The Bayesian overloader sounds like the internet.

> **u/captainNematode** [+15]  (an hour later)
> 
> Hmm, you can still have both finite and infinite "theories" integrate to some trivial slice of probability (and indeed you always do with continuous parameters, since there are infinitely many values between two points).
> 
> It's also very common and helpful to assign probability = 0 to certain values (e.g., what's your prior that a standard deviation is negative?).

>> **u/blazinghand** [+25]  *Chaos Undivided* (4 hours later)
>> 
>> Things like this fall prey to a certain mistake. This is in the same category of those "mugging" thought experiments. In these experiments, there is someone saying "I'm actually simulating this universe, give me 5 dollars and you'll get 10^10^10^10 happiness" or something. It is then said that even if it's super unlikely this is true, it's not zero, and the happiness value is really high, and asks us how we could logically turn it down.
>> 
>> The mistake made by the presenter in the comic, and also by people who think the thought experiments about mugging are interesting, is not having [error bars](https://en.wikipedia.org/wiki/Error_bar). For most things that we evaluate, we need to have error bars. It is categorically imperative not to consider probabilities below a certain amount. It is literally self-defeating to evaluate a potential outcome and try to reason about it, if that potential outcome is sufficiently unlikely: spending time evaluating things that are smaller than your ability to measure accurately actually decreases your ability to make good choices.
>> 
>> If we say "I think the likelihood of this being true is 0.000004 ± 0.000300" about a particular outcome, then we shouldn't evaluate anything based on that outcome at all: our measurement is not accurate enough to distinguish something this unlikely from something that has zero likelihood of truth. 
>> 
>> So, it's not quite true that "all probabilities must add to 1 in total" when we're making these judgement calls. Instead, we should say that "all probabilities, accounting for error, must add to 1 in total"--and effectively ignore outcomes that are sufficiently unlikely that we can't distinguish them from impossible. In fact, this is what most people do.

>>> **u/khafra** [+6]  (a day later)
>>> 
>>> Uncertainty about uncertainty, in Bayesian terms, resolves to plain old first-order uncertainty. If you want meta-uncertainty, you need [DST](https://en.wikipedia.org/wiki/Dempster%E2%80%93Shafer_theory) or something like that.
>>> 
>>> Of course, unadorned Bayesian reasoning is only epistemic, it doesn't prescribe actions. Most flavors of Bayesian decision theory do have ways to deal with Pascal's Muggings.

>>>> **u/None** [+1]  (5 days later)
>>>> 
>>>> Uncertainty about the parameters of your uncertainty in Bayesian stats is hierarchical Bayes methods, which are actually more powerful and really useful at the research frontier right now.

>>> **u/None** [+2]  (a day later)
>>> 
>>> The point of the Muggings isn't actually the thought-experiment, [it's that certain expectations don't actually converge.](https://arxiv.org/abs/0712.4318)
>>> 
>>> [And of course, there are ways to just model things differently.](http://polymer.bu.edu/hes/rp-peters16gellmann.pdf)

>>> **u/Gurkenglas** [+2]  (17 hours later)
>>> 
>>> If the probability of the likelihood of this being true is greater than zero (and according to how error bars are usually used, even greater than 50%), we should invest a monotonous amount of effort into the hypothesis.
>>> 
>>> (I suspect that Pascal's Mugging is defeated by game-theoretic concerns.)

>> **u/Sailor_Vulcan** [+3]  *Champion of Justice and Reason* (3 hours later)
>> 
>> In that case, how do you *know* that 1+1=2? Is this hypothesis based on evidence, or is it something you just know somehow? I'm pretty sure my prior here is based on the evidence that whenever I have added one thing to another thing in the past I got two things, and whenever I typed 1+1= into a calculator it would always say 2. In order to convince me that 1+1 does not equal 2, I would at least need a fucking shitton of shittons of evidence. Like if you could demonstrate that I had hallucinated whenever I added 1 thing to another thing, and if every time I add one thing to another thing in the next few decades I don't get two things. But my prior probability is overwhelmingly in favor of the hypothesis that 1+1=2. Even if I did see the evidence mentioned above, it would be *extremely hard* to distinguish between 1+1 not equaling 2 and plain old human error, and human error has a MUCH higher prior.
>> 
>> My prior that a standard deviation is negative? Well, if you can turn a data distribution inside-out, or loop it somehow, so that getting farther away from the mean actually brings you closer...but that would require that math is inconsistent. So really really really REALLY unimaginably low prior.

>>> **u/FeepingCreature** [+15]  *GCV Literally The Entire Culture* (4 hours later)
>>> 
>>> "But surely there can't be a LessWrong post about _everything_!"
>>> 
>>> Ahem. [How To Convince Me That 2+2=3 - LessWrong](http://lesswrong.com/lw/jr/how_to_convince_me_that_2_2_3/)

>>> **u/captainNematode** [+3]  (5 hours later)
>>> 
>>> Eh, I'd say probability is in the model (or the mind, maybe), not the world. The "true" state of affairs is already determined (well, maybe barring some interpretations of QM, or something). You can pick whatever priors you want (or hyperpriors, or hyperhyperpriors, etc.) and go with them for either your model or your mind, including assigning all the probability density to the value "2" when evaluating 1+1. Otherwise, though, you just arbitrarily designate priors (well, you can use the posteriors from earlier analyses, but eventually the turtles have to stop stacking) -- they're not out there in the world for you to discover (hence why they're priors). As for *knowing*, the epistemologists have been arguing that one for ages (and I think you can get more fundamental than 1+1; think stuff like the laws of thought, *A* = *A*, ¬(A∧¬A), etc.).
>>> 
>>> If standard deviations permit disagreement, can I fall back to the classic playground "if there are no absolute truths, what about this statement"? As in, you can assign probabilities to probabilities, and if you say a *p* of 0 is impossible, you've effectively assigned a probability of 0 to 0. Consider, for example, trying to determine the fairness of a coin. You'd use a binomial (or Bernoulli) likelihood, and in a Bayesian framework have to assign a prior to its parameter, *p*. Typically you'd define this on an interval between 0 and 1 using whatever distribution you fancy (uniform, beta, etc.). Values outside this interval would then receive zero probability density. You could use a prior distribution that's defined on all the reals if you wanted (and depending on what it is, it might work out ok in practice; a normal centered on .5 with low sd), but that'd be silly.

> **u/OrzBrain** [+10]  **Fingers* to *dance*, *hands* to *catch*, *arms* to *pull** (a day later)
> 
> I believe the point of the joke was someone following their highly flawed model to a logically absurd conclusion resulting in death, without stopping to consider that reality might be different than their model. That is, someone having a psychotic break. Or behaving like masses of humans have throughout history regarding religion and war. And that by using the buzzword "Bayesian" this nutjob got people to listen while he gave a lecture about it and then committed suicide on stage. And that afterwards instead of reacting to a death or life threatening injury, one of the "rational" audience spent time defending a competing buzzword.
> 
> Would there be less salt here if he had used the buzzword "Quantum" rather than "Bayesian"? Would you be able to notice the point if you weren't busy defending your favorite buzzword, rather like the audience member in the comic? If the guy had instead given a lecture about how he had figured out how to get into Muslim heaven and enjoy the virgins by stabbing himself with a special knife, and one of the audience had commented after the suicide, "That's why I'm a Christian," would the point of the comic been any different?

>> **u/TexasJefferson** [+2]  (2 days later)
>> 
>> The pattern-match reading of this comic is anti-bayesian. The pattern-match reading of the XKCD bayesianism comic was pro-bayesian. I didn't particularly enjoy either because neither make sense as a commentary about statistics.
>> 
>> So, at least for me, I think the joke fails to land because it's not an intellectually rigorous poke at the nominal subject (which I was expecting and hoping to be far funnier), not mere partisanship. The equivalent joke about a Christian who thought God would protect him because he lives in the best of all possible worlds and his continued existence is obviously a part of that would also fail for me. (A quantum immortality version might have been more salvageable with a different punchline; I'd have to think of one though.)

> **u/gbear605** [+16]  *history’s greatest story* (33 minutes later)
> 
> One problem is that he is changing the map and assuming that the territory will change with it.

>> **u/SometimesATroll** [+34]  (2 hours later)
>> 
>> More like he's drawing trillions of maps that may or may not be the true map and hoping reality get's confused about it.  I'm pretty sure Mr. Weinersmith is not actually proposing that someone attempt this, though.

>>> **u/Iconochasm** [+10]  (6 hours later)
>>> 
>>> Instruction unclear, please send paramedics.

>>>> **u/failed_novelty** [+4]  (9 hours later)
>>>> 
>>>> Request unclear.  I'm sorry; your new puncture wound is plugged, though.

>>> **u/None** [+3]  (a day later)
>>> 
>>> That sounds like an UNSONG plot device

>>>> **u/awesomeideas** [+1]  *Dai stiho, cousin.* (a day later)
>>>> 
>>>> Called, fittingly, "The Plot Device."

> **u/pizzahotdoglover** [+1]  (10 hours later)
> 
> Do people believe the assertion in the second panel? So if you could only come up with one theory it must be true?

>> **u/alexanderwales** [+11]  *Time flies like an arrow* (12 hours later)
>> 
>> The sum of all *possibilities* multiplied by their probability should equal 1, but just because you can only come up with one theory doesn't mean that it's the only possibility. For that matter, just because you can only come up with thirty theories doesn't mean there are only thirty possibilities. Unknown unknowns are notoriously hard to correct for though.

>>> **u/pizzahotdoglover** [+2]  (12 hours later)
>>> 
>>> Right, so since coming up with new theories doesn't change the total number of possibilities, then the whole premise of the comic doesn't work, since those possibilities would have already existed before the machine described them.

>>>> **u/ArisKatsaris** [+10]  *Sidebar Contender* (15 hours later)
>>>> 
>>>> > Right, so since coming up with new theories doesn't change the total number of possibilities, then the whole premise of the comic doesn't work,
>>>> 
>>>> Do you always try to figure out if the premise of a joke "works"?  
>>>> - Two numbers walk into a bar...  
>>>> - Wait a minute, numbers aren't corporeal entities, the whole premise of this doesn't work.

>>>>> **u/holomanga** [+2]  (20 hours later)
>>>>> 
>>>>> If the first reaction to a joke isn't "haha", but "wait, that doesn't make sense", there's still room for the joke to be improved.

>>>>>> **u/ArisKatsaris** [+7]  *Sidebar Contender* (22 hours later)
>>>>>> 
>>>>>> Not everyone's "first reaction" to this comic was the same...

>>>>> **u/pizzahotdoglover** [+1]  (22 hours later)
>>>>> 
>>>>> I get your point, but the part of the joke that doesn't make logical sense should be the punchline not the premise.  A joke meant to highlight the absurdity of a position doesn't really work if it gets the position completely wrong. Anyway, I only brought it up because I wanted to find out if that's what Bayesian theories really said.

>>>>>> **u/ArisKatsaris** [+5]  *Sidebar Contender* (23 hours later)
>>>>>> 
>>>>>> > A joke meant to highlight the absurdity of a position
>>>>>> 
>>>>>> Perhaps you're wrong about what the joke meant to do. I don't see it as a mockery of Bayesianism...

>>>>>> **u/FuguofAnotherWorld** [+1]  *Roll the Dice on Fate* (2 days later)
>>>>>> 
>>>>>> It's SMBC, he rarely takes a position seriously and rigorously from the outset, though from what I can tell he does understand them well enough.

>>>>>> **u/noggin-scratcher** [+1]  *I am a happy tree* (9 days later)
>>>>>> 
>>>>>> I'm super-late to the party here, but I had another thought on the matter...
>>>>>> 
>>>>>> > the part of the joke that doesn't make logical sense should be the punchline not the premise
>>>>>> 
>>>>>> If I had to really break the joke down to its essentials I'd separate it out as:
>>>>>> 
>>>>>> Premise: the 'main' character has terribly misunderstood Bayesianism
>>>>>> 
>>>>>> Development: his misunderstanding leads him to commit an entirely stupid form of suicide
>>>>>> 
>>>>>> Punchline: instead of saying "What a terrible misunderstanding and misrepresentation of Bayesianism", the person in the audience says "That's why I'm a frequentist". 
>>>>>> 
>>>>>> The implication being that Bayesianism really does predict immortality, and that the presenter's Bayesianism was therefore "the problem", rather than his fatal misunderstanding of it.
>>>>>> 
>>>>>> So it *is* the punchline that makes no logical sense; the rest of the comic was "played straight" with exactly the normal logical conclusion of stabbing yourself in the gut.

>>>>> **u/pizzahotdoglover** [+1]  (22 hours later)
>>>>> 
>>>>> I meant the premise within the context of the joke. By the premise in your example, numbers can walk, etc.

>>>>>> **u/Rouninscholar** [+3]  (a day later)
>>>>>> 
>>>>>> Honestly it feels almost anti humor to me.
>>>>>> It begins with him making a true statement.
>>>>>> He extrapolates wrongly.
>>>>>> He builds a machine based off of wrongful extrapolation.
>>>>>> He states the outcome of the machine.
>>>>>> now here is where I got tripped up mentally, THIS IS A COMIC. In one comic someone disproved math, lit themselves on fire and became more powerful. I honestly expected his machine to work within the comic.
>>>>>> Then he died. Subverting expectations and entertaining me.

>>>>>> **u/ArisKatsaris** [+1]  *Sidebar Contender* (23 hours later)
>>>>>> 
>>>>>> The premise within the context of the joke is that there's a buffoon who doesn't understand how Bayesianism works...
>>>>>> 
>>>>>> ...I mean it's not even as if his device worked or anything, even within the joke.
>>>>>> 
>>>>>> Though that would have been funny.

>>>> **u/Putnam3145** [+5]  (18 hours later)
>>>> 
>>>> > the whole premise of the comic doesn't work
>>>> 
>>>> The premise of the comic is that this guy's thing doesn't work, though

---

