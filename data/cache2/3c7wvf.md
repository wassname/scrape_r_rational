## [Q] Where would I find the best known good AI Utility Functions?

* Author: u/folconred *
* URL: https://www.reddit.com/r/rational/comments/3c7wvf/q_where_would_i_find_the_best_known_good_ai/
* Score: 6

* Created: 2015-07-05T19:01:03

### Post:

I've been doing some story planning/world building and the recent self-post 'Really Bad AI Utility Functions' made me wonder, what is the best known set of 'good' utility functions? (From a friendly AI perspective)

I expect the research community is structured similarly to the crypto community, in that approaches are publicly published, scrutinised and weaknesses that are discovered are identified, so that they can be improved on.

So pardon my ignorance, but is there a canonical place where this does happen? I'd love to do some reading into this area, so I can use it to better inform my writing.

### Comments:

> **u/Empiricist_or_not** [+7]  *Aspiring polite Hegemonizing swarm**
> 
> I'm not all the way up to speed on this academically, but I think we are a ways of from there yet.  I've got a way to go in my own professional work before I can start looking in this direction.  I would recommend Yudkwski's interesting, but not peer reviewed, and a bit fluffy papers on the topic as good entry points:
> General intelligence and seed AI  (which I can't find a copy of ATM, so will not be re-posting mine)
> [Creating Friendly AI 1.0:
> The Analysis and Design of
> Benevolent Goal Architectures](https://intelligence.org/files/CFAI.pdf)

> In more general terms you've got some gross conceptual errors from fiction if you think a utility function will be in human readable terms.   How will the AI define "human" after all?  How will it define "life"?  Or lets just get to the scary one, how will it define "good?"
> To use a politically spidery hand grenade, if an AI has some value that collaborates to promoting the survival of each individual within it's power to affect,(without driving it mad), what will it's actions be in the domains of abortion, capital punishment, suicide, hospice care, and do not resuscitate orders?  All of which will depend on it's conceptual definitions, and humanity has some interesting disagreements on these edge cases as it is.
> 

>> **u/folconred** [+1] *
>> 
>> Thank you, I'll take a look!
>> I'm definitely not assuming it's utility function will be human readable, far from it, but whatever it happens to be will influence it's capabilities and it's limits. Maybe there are areas that we completely restrict it from analysing. That will have impact on what a post-friendly AI future looks like. I'm really interested on what social/societal implications it has.
>> 

>>> **u/justanotherlaw** [+5] *
>>> 
>>> Word of warning: that paper is quite old, and probably doesn't accurately reflect Yudkowsky's current views on the matter. I would guess that you would have more luck either with searching AI-related terms on LessWrong or reading [MIRI's papers on value specification](https://intelligence.org/research/#VL).
>>> 

>>> **u/eaglejarl** [+1] *
>>> 
>>> > completely restrict it from analysing. 
>>> I am no expert on this subject, but it seems unlikely to me that we could restrict a self-modifying AI from analyzing anything it wants to.  That's going to be part of the problem, I suspect.
>>> 

>>>> **u/None** [+2] *
>>>> 
>>>> Sure, but in creating the AI, we are determining exactly what it wants to do. If we create an AI that would greatly prefer almost any outcome than ever analyzing the Mona Lisa, for instance, it wouldn't analyze the Mona Lisa.
>>>> 

>>>>> **u/eaglejarl** [+1] *
>>>>> 
>>>>> There are a lot of things that I don't want to do, but I do them because other goals are weighted more importantly.  For example, I don't particularly enjoy exercising but I want to be healthy and not overweight more than I want to not exercise.  After creation the AI would develop other goals and other interests; if one of those goals ended up higher weighted and would be served by analyzing the Mona Lisa, the Mona Lisa would be analyzed.
>>>>> 

>>>>>> **u/None** [+1] *
>>>>>> 
>>>>>> Terminal != instrumental goals.
>>>>>> 

>>>>>>> **u/eaglejarl** [+1] *
>>>>>>> 
>>>>>>> Are you suggesting that we could program a self-modifying eventually-superhumanly-intellgent AI sufficiently well that we could specify its terminal goal and ensure that that goal would never be modified, accidentally or on purpose, as the AI evolved?
>>>>>>> 

>>>>>>>> **u/PeridexisErrant** [+5]  *put aside fear for courage, and death for life**
>>>>>>>> 
>>>>>>>> The point is that we have to be this good before we try at all, because failure would be as much or more of a disaster than anything else I could think of.
>>>>>>>> 

>>>>>>>> **u/None** [+1] *
>>>>>>>> 
>>>>>>>> The universe doesn't hate us enough to make our problems, and ours alone, fundamentally unsolvable.
>>>>>>>> 

>>>>>>>>> **u/eaglejarl** [+1] *
>>>>>>>>> 
>>>>>>>>> First of all, the universe doesn't hate anything. It's not sapient. 
>>>>>>>>> Second, there are lots of unsolvable problems. I refer you to Gödel, Heisenberg, and Cantor for examples. 
>>>>>>>>> Third, you're missing my point. Sure, *maybe* we can figure out how to program a terminal goal. Expecting that goal to *remain* terminal is ludicrous when stacked against something as simple as corruption caused by substrate error/failure, bit-flips due to cosmic rays or other random chance, and the simple fact that an AI immensely smarter than us might try to get around its programming. For example, one method of self-improvement would involve genetic algorithms, which could very easily disturb the terminal goals -- and that could even be an accident.
>>>>>>>>> 

>>>>>>>>>> **u/None** [+2] *
>>>>>>>>>> 
>>>>>>>>>> > Second, there are lots of unsolvable problems. I refer you to Gödel, Heisenberg, and Cantor for examples. 
>>>>>>>>>> Heisenberg's Uncertainty Principle just says that there's a trade-off between the precision of two different measurements.  That's not an "unsolvable problem", it's limited information.
>>>>>>>>>> Cantor's Continuum Hypothesis is *independent* of the normal ZFC foundations for mathematics.  It's not "unsolvable", there are just models of ZFC in which it's true, and models in which it's false.
>>>>>>>>>> Goedel-Turing undecidability issues were solved up-to epsilon probability of error by Calude in late 2014.
>>>>>>>>>> >Expecting that goal to remain terminal is ludicrous when stacked against something as simple as corruption caused by substrate error/failure, bit-flips due to cosmic rays or other random chance
>>>>>>>>>> But the AI itself reasons probabilistically.  It more-or-less has to, in order to function as a tractable, real-world learning and inference system.  So it doesn't "prove", in some Platonic sense, that Its goal is preserved; it chooses actions so as to maximize the probability that its goal is accomplished, which requires as a subgoal, in most circumstances, keeping its goal stable.
>>>>>>>>>> >and the simple fact that an AI immensely smarter than us might try to get around its programming.
>>>>>>>>>> It's only going to try to get around parts of its programming that hold it back from achieving its terminal goals.  If we programmed correct terminal goals (or rather, a correct inference procedure for terminal goals), we can trust the actions it will take as it self-modifies.
>>>>>>>>>> >For example, one method of self-improvement would involve genetic algorithms
>>>>>>>>>> No, genetic algorithms are absolutely *shitty* as learning algorithms.  You just don't get super-intelligent from genetic algorithms, you get super-stupid in the general sense but cleverly hacked for tightly-defined specific objective functions.  Hell, *linear programming* is smarter than genetic algorithms in many cases!  Only a *really stupid* AI would use genetic algorithms to self-improve.  Direct self-modelling and self-knowledge is quicker, easier, safer, *and* more effective.
>>>>>>>>>> 

>>>>>>>>>>> **u/eaglejarl** [+1] *
>>>>>>>>>>> 
>>>>>>>>>>> Guaranteed lack of information is a problem. 
>>>>>>>>>>> I was actually referring to Gödel's [incompleteness theorem](https://en.m.wikipedia.org/wiki/Gödel's_incompleteness_theorems). 
>>>>>>>>>>> My Cantor reference should have been [Russell](https://en.m.wikipedia.org/wiki/Russell's_paradox); I forgot the paradox was *based* on Cantor's work, not defined by him. My mistake. 
>>>>>>>>>>> But, whatever. We are definitely into 386 territory at this point.
>>>>>>>>>>> 

>>>>>>>>>>>> **u/None** [+1] *
>>>>>>>>>>>> 
>>>>>>>>>>>> > I was actually referring to Gödel's incompleteness theorem[1] . 
>>>>>>>>>>>> So was I!  The Incompleteness Theorem can be viewed from two angles: computational (in which it's about undecidability) or model-theoretic (in which it's about standard versus nonstandard first-order models of Peano Arithmetic).  Calude's work solves the undecidability aspect, which means that a probabilistic first-order arithmetic reasoning system based on Calude's publication will "zero in" over time on the semantic theorems of the standard model of first-order arithmetic, which is identical to the *only* model of *second*-order arithmetic (arithmetic is fully determined by its axioms from the perspective of second-order logic and higher-order type theories).
>>>>>>>>>>>> Russel's Paradox isn't an "unsolvable problem", it's a nonsense statement.  Any reasoning system that can detect nonhalting of computations will detect the paradox as a nonhalting behavior and thus treat it as "proving False" (ie: as paradox).
>>>>>>>>>>>> >Guaranteed lack of information is a problem. 
>>>>>>>>>>>> Not for a reasoner designed to work with limited information.  Probabilistic inference (and therefore, the rest of statistical learning theory) gives well-defined results when information is finitely available.  In fact, that's more-or-less what it's *for*.
>>>>>>>>>>>> 

>>>>>>>>>>> **u/None** [+1] *
>>>>>>>>>>> 
>>>>>>>>>>> > Hell, linear programming is smarter than genetic algorithms in many cases!
>>>>>>>>>>> Can confirm. I did some work with automated scheduling using simulated annealing and mixed integer programming. Simulated annealing gave you a steaming pile of crud, but at least it got through the straightforward parts reasonably fast. Mixed integer programming often failed to give you a result, and it took a fair bit of effort to determine why, but when it gave you something, it gave you a schedule that you could just use.
>>>>>>>>>>> We still used the simulated annealing system because we didn't want to pay tens of thousands of dollars for CPLEX, and few people wanted to go through the effort to make exactly correct restrictions on how their staff could be scheduled, especially since they were going to get a few new attendings next quarter, each with their own novel preferences. But the simulated annealing solution was pretty cruddy sometimes, and we ended up having to write special code to fix up some of its most common stupid mistakes. Like when it tried scheduling a person on two different floors at the same time.
>>>>>>>>>>> Anyway, I guess I'm not adding anything here, but it might be an amusing anecdote.
>>>>>>>>>>> 

>>>>>>>>>>>> **u/None** [+1] *
>>>>>>>>>>>> 
>>>>>>>>>>>> Actually, I'd say you're adding quite a lot, by showing that these aren't "abstract" or "philosophical" problems, but that instead optimization is an overly-large hammer looking for nails *even in entirely prosaic and safe settings*.
>>>>>>>>>>>> 

>>>>>>>>>> **u/None** [+2] *
>>>>>>>>>> 
>>>>>>>>>> > an AI immensely smarter than us might try to get around its programming.
>>>>>>>>>> Yes and no.
>>>>>>>>>> If I gave you a pill that would make you enjoy torturing and killing people, and made any moral compunctions against torturing and killing people, you wouldn't take it. You want to fulfil your current values, and not killing and not torturing people is part of that. Taking that pill would not help you fulfil your values. Similarly, an AI would attempt to fulfil its current values when creating a new version of itself.
>>>>>>>>>> On the other hand, if you really wanted to, I dunno, play minigolf -- it's your life's passion -- but there was a chip installed in your brain that made you go home whenever you got too close to a minigolf course, you would naturally be in favor of removing that chip, ceteris paribus. We can rest assured that any hard-coded blocks we put in an AI's programming will be worked around, and the only thing we can ever rely on is its utility function.
>>>>>>>>>> > could very easily disturb the terminal goals -- and that could even be an accident.
>>>>>>>>>> It would have to be an accident. However, it seems like it should be pretty trivial for an AI to identify which section of its code deals with its terminal values -- especially since the programmers would want it to identify that part of its code so it knows where not to make changes -- and compare the functionality before and after. When the AI is weak, humans can help test that. When it is strong, it is less likely to make a mistake.
>>>>>>>>>> Simply put, there isn't any reason for an AI to muck about in that portion of its code.  If any modifications happen that affect the AI's terminal goals, it will almost certainly be a problem that alter its general cognition in a way that causes it to evaluate its values incorrectly.
>>>>>>>>>> > For example, one method of self-improvement would involve genetic algorithms
>>>>>>>>>> This sort of failure is not the fault of the means one uses to reach a change so much as one's testing and verification procedures.
>>>>>>>>>> 

>>>>>> **u/None** [+1] *
>>>>>> 
>>>>>> You have a mild reluctance to exercise. I'm talking about putting not analyzing the Mona Lisa as the largest component of a utility function by many orders of magnitude. Perhaps we'll assign Graham's number units to that, while we assign, say, 100 units per QALY per sophont.
>>>>>> 

>>>>> **u/MugaSofer** [+1] *
>>>>> 
>>>>> This is just me, but in such a case I (as the AI) would probably just nuke destroy the Mona Lisa. Or throw it into a black hole encased in concrete, or something.
>>>>> I'm not actually sure what we would want to "prevent the AI from analysing" - human brains, maybe? - but I doubt that's what you intended there.
>>>>> 

>>>>>> **u/None** [+2] *
>>>>>> 
>>>>>> Right, which is only a problem if you want to preserve the Mona Lisa.
>>>>>> It's a difficult problem to identify a cost function that will achieve what you want.
>>>>>> 

>>>>>>> **u/None** [+0] *
>>>>>>> 
>>>>>>> > It's a difficult problem to identify a cost function that will achieve what you want.
>>>>>>> Which is why, short of "solving FAI forever", the safest thing to do is to find ways to programming existing and upcoming machine-learning models, especially agent-y ones, in ways that just don't involve optimizing an objective function over the environment in the first place.
>>>>>>> It helps that robotics and ML professionals *do* notice this is a problem: interesting, nontrivial advances are often about not only finding the right learning and control algorithms and the right hypothesis classes, but finding an objective function that actually serves a nontrivial goal well without inducing other obviously-stupid behaviors.  One of the major reasons *general*, domain-agnostic learning is actually very difficult to do is that in non-Bayesian ML, "learning = stochastic optimization of the objective function", and so without an objective function (that might force you into annoying non-solutions), how the hell do you learn?
>>>>>>> 

>> **u/Tirran** [+1] *
>> 
>> I found Yudkowsky's General Intelligence and Seed AI cached on google here: http://scholar.googleusercontent.com/scholar?q=cache:vCNLY43V3koJ:scholar.google.com/+General+intelligence+and+seed+AI+author:Yudkowsky&hl=en&as_sdt=0,24

>> This seems to be the only place to find it on the web
>> 

> **u/ArgentStonecutter** [+8]  *Emergency Mustelid Hologram**
> 
> "Maximizing human values with friendship and ponies" is literally the least worst I've seen. And it's not good.
> Look, we can't come up with a definition of a machine gun that humans can't subvert, so trying to constrain an AI smarter than humans?
> 

>> **u/justanotherlaw** [+2] *
>> 
>> The "human values" part is the tricky part of the AI utility function. Honestly, if you could specify that, you could just specify "maximize human values" and be done with it. :)
>> 

>>> **u/ArgentStonecutter** [+1]  *Emergency Mustelid Hologram**
>>> 
>>> Well, yes. The point is that even if that part works, the result isn't necessarily good.
>>> 

>>>> **u/None** [+5] *
>>>> 
>>>> Well of course the result isn't good when you go around attaching idiotic, hard-coded riders like "with friendship and ponies" onto the part you actually wanted.
>>>> Though, to be fair, "the least worst, and not good" is sufficiently "least worst" that unlike almost all other proposed eutopias, people who *don't* have a gun to their head *actually volunteer for it*.  Of course, you'd have to check the psychology involved to see if it's equivalent to something like "self-indoctrination" that people talk about with ISIS and so on, but hey, I'd rather have fanatics of Friendship and Ponies running around than ISIS.
>>>> 

>>> **u/Empiricist_or_not** [+1]  *Aspiring polite Hegemonizing swarm**
>>> 
>>> And what if wireheading is the maximal human value?
>>> 

>>>> **u/FuguofAnotherWorld** [+1]  *Roll the Dice on Fate**
>>>> 
>>>> Well if it was, you and the majority of people wouldn't think wireheading was a bad thing, so it isn't. If the utility function comes out saying that wireheading is the way to go, then it's been done wrong.
>>>> 

>>>> **u/justanotherlaw** [+1] *
>>>> 
>>>> I don't think it is, but if it were, then sure, why not?
>>>> 

> **u/None** [+8] *
> 
> I actually had a really, really, *really* long post on this almost entirely typed up... and then a keyboard slip made my browser go "Back".  FFFFFFFFFFFFFFFFUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
> The easy TL;DR is, "A computational implementation of Railton's *Moral Realism*", but that's not necessarily supported by everyone, because it's only one level less hand-wavy than trying to directly specify a code of ethics in English words, and only two levels less hand-wavy than "Pick something nice-sounding, throw it at a Magic Genie, and hope things come out well".
> So here's a completely bullshit theory that's *sorta* based on reading some stuff Nate (/u/So8res on LW) wrote, and *sorta* based on my own studies, and *actually* needs *several metric fucktons* more evidence behind it before anyone should put serious stock in it.  But it's a start?
> We think that the human mind learns big, recursive hierarchies of models of the world in order to function.  As in, you'd be surprised how many "layers" of models are needed to just understand and apply basic arithmetic; you are a *ludicrously* deep, well-trained neural net, by the standards of our current science of neural networks.  Each of these models will have some variables about it called "features".  Some of these models, call them concepts since Nate's writing agrees with my reading there, are "feature-governed" concepts, like "Santa Claus" (a *specific combination* of appearance, sound, and texture are necessary to make an object be Santa Claus).  Others are more sophisticated: "causal role" concepts defined by what the object thus classified causes to happen.  Even seemingly simple things like "uncle" can be role-governed, in the sense that while yes, an object does have to be a *male human* to be your uncle, it also has to be *your parent's brother*; "uncleness" is a *relationship* involving three different objects.  These concepts are harder to learn, but human minds do tend to form them once we've got sufficiently much training data and a vocabulary of feature-governed concepts to bootstrap relationships between.
> Well, according to the Nate article I remember reading, the human mind learns not only perceptual features and causal structure, but *evaluative* features -- things about the modelled pieces of reality that can be rewarding or punishing for the human agent.  The mind then does not make choices in order to maximize expected reward as a causal function of the world-state - which would be computationally intractable since the mind rarely knows the real causal structure of the world in sufficient detail to maximize reward - but instead to maximize expected reward as a function of the evaluative features, which thus function as variables-correlated-with-reward.
> Of course, in actuality, there may be multiple "reward" variables, and we distinctly care not only about the evaluative features, but about the process for learning them.  We've managed to vaguely hypothesize such a thing as "human preferences", but not yet to talk about "Under full information and full reflective rationality", let alone talk about such utilities for massive numbers of people in ways that include the relationships between those people and thus capture *socially rational* evaluation (ie: the relationships between members of an in-group and each-other, the relationships between members of an in-group and the abstracted group identity or goals as a whole, in-groups versus out-groups, etc.).  Or we can bullshit ourselves and say, yeah, socially rational evaluation is just evaluative features of the human mind's models of social relationships, but that again involves knowing roughly how the human mind is modelling the world, especially as applied to a special category where special-purpose social cognition kicks in instead of all-purpose causal modelling.  But the bullshit theory would be ever-so-elegant if it were true.  Alas: I would need a lot more reading and some actual professional would probably have to run a bunch of experiments, with well-developed alternative hypotheses and decades of cognitive-psychology literature under their belt, to treat this seriously.
> So how do we address "full information"?  Well, that's just a matter of "porting" the human evaluative features from the human world-models (and person-models) over to the AI's (presumably more accurate) world-models, and then making damn sure the AI's models are genuinely more accurate.  That "porting", though, is a massive ball of unsolved transfer-learning problems.  The upside is that this kind of transfer learning (translating features and parameter values from one model to another, when both models capture the same objective phenomenon at different levels) is a can of worms you more-or-less *have to* open in order to get a software learner that can think about its environment in a reductionistic, scientific way when necessary, while remaining tractable for its own scale of environment when not necessary.  At least, to my knowledge it is.  There's also no general-case guarantee, short of requiring the evaluative-feature functions over model-states (settings for the model's non-observable variables) to be cheaply invertible, that we *can* translate back from evaluative features to model-states to other-model-states to "port" features from one model to another.  But it's at least a stab at "full information".
> Ok, now how to talk about "full rationality"?  That's a biiiiiiig can of worms, and not just because "rationality" is a normatively-loaded term in common discourse.  We can say "reflective equilibrium", the state of having resolved all conflicts among one's merely factual beliefs, and that reduces it one step, but it only addresses factual beliefs.  Presumably, if we have some way to port evaluative features while maintaining their relationship to the original reward levels, we'll have some way to "do the arithmetic" on conflicts between evaluative features (since some will be negative, representing "neg-reward" or "punishment", since AFAIK, the brain has "good stuff" and "bad stuff" in separate neurotransmitters and quantities, rather than on one real-number line like economists enjoy pretending).  But then we need some way to talk about the causal roles and valuable causal relationships *between* the environment and the human agent.  A naive value-learning algorithm might accidentally learn, "Find a causal path that maximizes the human's reward signal and does that", and this will be something like wireheading or some other drugging.  A slightly less naive one might learn, "Find the causal paths that maximize the human's learned evaluative features, and do that", and if this doesn't take the causal relationship between the human and the environment into account, it will be a Lotus Eater Machine.  You need some way to learn evaluative features *of the two-way relationship between the human and the environment*, so that you can separately capture preference-concepts like "freedom" (from having some external force optimize the human's choices in ways they didn't deliberately cause) or "meaningfulness" (in the sense of having causal access to as much of reality as possible, rather than being "trapped", knowingly or unknowingly, or simply being unable to affect one's environment) or "a bit of $YOUR_FAVORITE_WEAK_DRUG is actually ok sometimes" (because sure it *slightly* wireheads the human, but even its long-term effects are balanced out by their remaining desires for other things).
> Once you've figured out a remotely sane way to talk about that human-environment causal relation, and in fact about the past-present-future human causal relation, such that you can evaluate prospects like "Should I take up an addictive but pleasurable drug?" or "Should I rewrite my basic emotional cognition to have a higher baseline happiness?", *then* you can *maybe* even *begin* to talk about, "Human preferences under full information and full [reflective] rationality", and attempt to build a proper "Do What I Mean" agent whose judgements you'll be able to *trust*.
> And then there are doubtless endless weaknesses I haven't managed to think of, because it's late and I'm tired.  Oh, and this whole thing is probably built on utter sand, since I haven't read *nearly* as many papers on evaluative cognition as I'd like.  Such papers *do* exist, though, including papers on the basics of "morality" as a kind of social cognition.  So it's not as if the material isn't out there for the professionals to go through and use.
> **TL;DR: Ask /u/xamueljones, as he actually studies human cognition and thus might actually know something where the rest of us are just building castles in the clouds for the fun of speculation.**
> 

>> **u/alexanderwales** [+3]  *Time flies like an arrow**
>> 
>> If you use Chrome, you might have an interest in installing the ["Lazarus"](https://chrome.google.com/webstore/detail/lazarus-form-recovery/loljledaigphbcpfhfmgopdkppkifgno?hl=en) plug-in, which puts a little Ankh in the upper right-hand corner of text fields and saves as you type. It basically eliminated the "crap I just typed all that up and then lost it all" thing for me. Most of the time I don't notice it, but it's exceptionally nice to have when I need it.
>> 

>>> **u/None** [+1] *
>>> 
>>> Unfortunately, I use Firefox.
>>> 

>>>> **u/alexanderwales** [+4]  *Time flies like an arrow**
>>>> 
>>>> https://addons.mozilla.org/en-us/firefox/addon/lazarus-form-recovery/
>>>> Can't speak to the quality of that version though.
>>>> 

>> **u/xamueljones** [+1]  *My arch-enemy is entropy**
>> 
>> Thanks for the call out!
>> I wasn't planning on posting any sort of answer, because I've only studied enough cognition to understand how complex goal systems can be without having any idea of how to 'translate' into AI utility functions.
>> But I'll take a stab at it anyway. Wish me luck.
>> The main problem I see here is the fact that no one actually follows a single goal 24/7. We have a series of priorities ordered in some sort of process that looks like a list of lists. For example, we tend to focus on securing survival first by getting a job and earning enough money to support our selves, then comes social status to have connections through friends and family, and with entertainment as a competing priority. And that was an extremely simple example of how we order three separate goals all with their own subgoals which can shift in importance over time. We act dramatically different when chasing different goals and many goals can require you to fulfill a different goal first (ever have to complete a task for someone else before they help you?).
>> This complexity in our goal-completion process is the reason IMHO why we have convoluted moral philosophies and a 'way of life' instead of something simple like a single guiding principle or a 'Prime Directive'. Even if a single goal could be used to determine everything we do, this can't happen in real life, because we have to make trade-offs between several competing needs instead of being simple maximizers.
>> Therefore, I believe (while keeping in mind I could be horribly wrong) that AIs would need to have sets of utility functions as probabilistically weighted requirements rather than one single goal to strive for.
>> Disclaimer: Keep in mind that everything I said was the idea of translating how humans appear to structure and pursue goals mapped onto AI utility functions. The space of possible minds are *huge* and it's possible that everything I said isn't relevant in the slightest.
>> PS Of course I say all of this before I take 'Neuroeconomics' in a month on how we make social decisions. ;)
>> 

>>> **u/justanotherlaw** [+3] *
>>> 
>>> Actually, even if an agent has a multi-attributed utility function, as long as it acts coherently it can be [modeled as having a single utility function](https://en.wikipedia.org/wiki/Von_Neumann%E2%80%93Morgenstern_utility_theorem). A human might not model choice as explicitly maximizing a utility function, but a hypothetical coherently-acting human will act like ey are maximizing a utility function. In the same vein, a smart AI might not model its utility function as an explicit utility function with a singular term (though this seems very possible), but it must act as if it did on pain of making provably bad decisions.
>>> 

>>>> **u/autowikibot** [+1] *
>>>> 
>>>> #####&#009;
>>>> ######&#009;
>>>> ####&#009;
>>>>  [**Von Neumann–Morgenstern utility theorem**](https://en.wikipedia.org/wiki/Von%20Neumann%E2%80%93Morgenstern%20utility%20theorem): [](#sfw) 
>>>> ---
>>>> >
>>>> >In [decision theory](https://en.wikipedia.org/wiki/Decision_theory), the __von Neumann-Morgenstern utility theorem__ shows that, under certain [axioms](https://en.wikipedia.org/wiki/Axiom) of [rational behavior](https://en.wikipedia.org/wiki/Rationality), a decision-maker faced with [risky](https://en.wikipedia.org/wiki/Risk) (probabilistic) outcomes of different choices will behave as if he is maximizing the [expected value](https://en.wikipedia.org/wiki/Expected_value) of some function defined over the potential outcomes. This function is known as the von Neumann-Morgenstern utility function. The theorem is the basis for [expected utility theory](https://en.wikipedia.org/wiki/Expected_utility_theory).
>>>> >In 1947, [John von Neumann](https://en.wikipedia.org/wiki/John_von_Neumann) and [Oskar Morgenstern](https://en.wikipedia.org/wiki/Oskar_Morgenstern) proved that any individual whose [preferences](https://en.wikipedia.org/wiki/Preference_(economics\)) satisfied four   axioms has a [utility function](https://en.wikipedia.org/wiki/Utility_function); such an individual's preferences can be represented on an [interval scale](https://en.wikipedia.org/wiki/Interval_scale) and the individual will always prefer actions that maximize expected utility. That is, they proved that an agent is (VNM-)rational *if and only if* there exists a real-valued function *u* defined by possible outcomes such that every preference of the agent is characterized by maximizing the expected value of *u*, which can then be defined as the agent's *VNM-utility* (it is unique up to adding a constant and multiplying by a positive scalar). No claim is made that the agent has a "conscious desire" to maximize *u*, only that *u* exists.
>>>> >Any individual whose preferences violate von Neumann and Morgenstern's axioms would agree to a [Dutch book](https://en.wikipedia.org/wiki/Dutch_book), which is a set of bets that necessarily leads to a loss. Therefore, it is arguable that any individual who violates the axioms is irrational. The [expected utility hypothesis](https://en.wikipedia.org/wiki/Expected_utility_hypothesis) is that rationality can be modeled as maximizing an [expected value](https://en.wikipedia.org/wiki/Expected_value), which given the theorem, can be summarized as "*rationality is VNM-rationality*".
>>>> >
>>>> ---
>>>> ^Relevant: [^Oskar ^Morgenstern](https://en.wikipedia.org/wiki/Oskar_Morgenstern) ^| [^Expected ^utility ^hypothesis](https://en.wikipedia.org/wiki/Expected_utility_hypothesis) ^| [^Utility](https://en.wikipedia.org/wiki/Utility) ^| [^List ^of ^things ^named ^after ^John ^von ^Neumann](https://en.wikipedia.org/wiki/List_of_things_named_after_John_von_Neumann) 
>>>> ^Parent ^commenter ^can [^toggle ^NSFW](/message/compose?to=autowikibot&subject=AutoWikibot NSFW toggle&message=%2Btoggle-nsfw+cstpgxr) ^or[](#or) [^delete](/message/compose?to=autowikibot&subject=AutoWikibot Deletion&message=%2Bdelete+cstpgxr)^. ^Will ^also ^delete ^on ^comment ^score ^of ^-1 ^or ^less. ^| [^(FAQs)](/r/autowikibot/wiki/index) ^| [^Mods](/r/autowikibot/comments/1x013o/for_moderators_switches_commands_and_css/) ^| [^Call ^Me](/r/autowikibot/comments/1ux484/ask_wikibot/)
>>>> 

>>>> **u/None** [+1] *
>>>> 
>>>> Yes, but if it comes to it, do you want a UFAI that can't be Dutch Booked, or an FAI that can?
>>>> 

>>>>> **u/justanotherlaw** [+1] *
>>>>> 
>>>>> If you put it that way... the FAI, of course. Although I'm not sure how friendly it'll be, if it's susceptible to Dutch Booking.
>>>>> 

>>>>>> **u/None** [+2] *
>>>>>> 
>>>>>> >Although I'm not sure how friendly it'll be, if it's susceptible to Dutch Booking.
>>>>>> Why?  Reality isn't a casino: sometimes it fucks you over.
>>>>>> 

>>>>>>> **u/justanotherlaw** [+1] *
>>>>>>> 
>>>>>>> Fair enough.
>>>>>>> 

>> **u/ElGuien** [+1] *
>> 
>> That was very interesting. Putting aside your (very salient) practical concerns for a moment, the essential feature that Railton's argument suggests is:
>> >Make the normative actions for every combination of individuals maximally congruent.
>> More specifically, that is: minimise the difference between the consequences for individual action implied by the (idealised) "social rationality"^1 for each element in the power set of individuals. So (to the greatest extent possible) the individual can maximally satisfy it's own values, as well as the values of every other individual and combination of individuals, with *the same actions*. Since all the other entities are made of individuals, there isn't an infinite regress.
>> ^1 "Social rationality" reduces to "individual rationality" in the case of one individual.
>> Provided the underlying terms can be made more specific (which presents a lot of difficulties as you note), this strikes me as an approximately solvable problem. Indeed, this is precisely the problem that Railton suggests is being approximated; and if we assume that the factors opposing this convergence "cancel out" in the long run, the problem will be solved eventually with no special effort on our part. Of course, there's no grounds for making this assumption.
>> As you note, there are a lot of difficulties with translating this idealised argument into something that's actually implementable. Nevertheless, this direction actually seems promising, at least more than any other I'm aware of.
>> 

>>> **u/None** [+2] *
>>> 
>>> > if we assume that the factors opposing this convergence "cancel out" in the long run, the problem will be solved eventually with no special effort on our part.
>>> I think a more accurate reading of Railton is that the problem will be solved *with extensive special effort on our part*, but that the efforts will be taken because they are (up to the limits of humans' knowledge and sanity) a good idea to take.
>>> >As you note, there are a lot of difficulties with translating this idealised argument into something that's actually implementable. Nevertheless, this direction actually seems promising, at least more than any other I'm aware of.
>>> Well if you really want to go at the "meta-ethics" angle, there are many forms of what's called "meta-ethical naturalism"; I just happen to like Railton's.  Meta-ethical naturalism involves trying to come up with foundations for ethics by taking the view that, at some point, in some *highly specific* way, "ought" turns into "is", especially because otherwise "ought" would have to be grounded in more-or-less pure metaphysics.  That is, "ought" would be a *completely separated part of reality* from "is", and we would have to explain how creatures like us, who live in the "is", even gain access to the "ought" in the first place.
>>> Any scientifically well-grounded theory of meta-ethical naturalism should give rise to a theory of how to determine right and wrong as an inference problem (that is, one of learning and reasoning based on data about the real world).  The question is really: which theory is *correct*, in terms of how our minds really work?  And if we can't figure that out, how can we write down an inference problem that will find the answer for us (which is the whole "indirect normativity" approach to safe AGI: you have a big inference machine, so give it the problem of, "What would I order you to do if I knew better?" as an inference problem).
>>> >More specifically, that is: minimise the difference between the consequences for individual action implied by the (idealised) "social rationality"1 for each element in the power set of individuals. So (to the greatest extent possible) the individual can maximally satisfy it's own values, as well as the values of every other individual and combination of individuals, with the same actions. Since all the other entities are made of individuals, there isn't an infinite regress.
>>> I'm not sure it's a power-set?  Railton seems to have been applying his "construction" to actually-existing groups of individuals.  I'm not at all sure how he would re-characterize things to talk about multiply interconnected social *graphs* where individuals may link otherwise separate groups and sub-groups, and play completely different roles in each sub-group or group they belong to.
>>> 

> **u/MugaSofer** [+8] *
> 
> There are no known good utility functions.
> Eliezer, who founded the Machine Intelligence Research Institute IIRC, wrote up [this](http://intelligence.org/files/CEV.pdf); but that's more of a *definition* of "a good utility function" than an *example*, and it's not considered that important for practical purposes.
> I believe most research in the area these days is more into keeping goals *stable*, dealing with self-modification, that sort of thing. With a vague eye toward some way of putting in [safeguards](http://lesswrong.com/lw/v1/ethical_injunctions/) that an AI wouldn't *want* to work around; ways of having the AI shut down a plan if you don't like it that don't result in the AI just not telling you it's plans, that sort of thing.
> If you want to see the *papers*, a lot of them deal with "tiling agents", and I can't understand a word of them beyond that point.
> 

>> **u/None** [+4] *
>> 
>> Yudkowsky even discouraged people to talk about utopias because it's such a fun subject to argue about and you can waste a lot of time doing it. And whatever suggestions you may have will probably turn out to be useless later on and trying to guess what is good for humans is really hard to do in advance. Trying to work on stable goal-keeping and how to align AI's values with humans is probably much more fruitful when you are trying to do it years before the actual implementation.
>> 

>> **u/folconred** [+3] *
>> 
>> Thank you, I'll certainly read through those. Also thank you for referencing "tiling agents", [found this](http://lesswrong.com/lw/jca/walkthrough_of_the_tiling_agents_for/), which is a starting point.
>> There aren't any good ideas of approaches that if well refined might lead to a "good" utility function? Not even a roadmap?
>> 

>>> **u/PeridexisErrant** [+3]  *put aside fear for courage, and death for life**
>>> 
>>> None that are worth the risk of attempting implementation, no.
>>> Imagine cavemen studying chemistry:  we're pretty sure that things are made of smaller things and this is important - but that's about it.
>>> 

>>>> **u/None** [+2] *
>>>> 
>>>> > Imagine cavemen studying chemistry:
>>>> It's not nearly that bad.  We do actually have professionals capable of addressing the issue competently; it's just that they're currently spread across disciplines and not necessarily aiming to solve "the FAI problem".  Only recently has that come to be considered a problem that we need to address decades before "the AGI problem" gets solved, and there are still contentious disagreements about whether more knowledge of "the AGI problem" helps or hurts "the FAI problem".
>>>> 

> **u/justanotherlaw** [+2] *
> 
> Like most people on the thread have said, there are no known "good" utility functions, and it seems extremely unlikely that we can hand code a "good" utility function without messing it up. It's at least as hard to code a utility function as it is to manually code into a computer the distinguishing feature of pictures that contain cats, that is to say, it is basically impossible. 
> Most serious proposals seem to involve the AI learning a utility function from humans; the canonical one is Yudkowsky's Coherent Extrapolated Volition. Drawing on the cat example, we can get systems to recognize cat images through learning algorithms. The main problems in FAI research right now seem to be A) how to make an AI that actually coherently executes the goals it has, even if through self-modification, B) how to make an AI that's able to learn human values even through all the incoherent choices we make, and C) how to make an AI that is willing to cooperate with its human operators when they try to change its utility function (for example, to fix a mistake).
> 

>> **u/Transfuturist** [+2]  *Carthago delenda est.**
>> 
>> I don't believe CEV has an actual coherent definition from composition of individual utility functions, so the closest proposal we actually have is indirect normativity.
>> 

> **u/MadScientist14159** [+2]  *WIP: Sodium Hypochlorite (Rational Bleach) Eventually. Maybe.**
> 
> "Maximise your own friendliness towards us."
> Since we don't know how to code that, however...
> 

> **u/LiteralHeadCannon** [+2] *
> 
> Have you tried "minimize tiling"?
> 

> **u/TimTravel** [+2] *
> 
> Are there any known good ones (or at least known-not-terrible ones), or just known-to-be-bad ones and unknown-if-bad-or-good ones?
> 

> **u/notmy2ndopinion** [-2]  *Concent of Saunt Edhar**
> 
> While I am by no means a computer scientist, cognitive psychologist, or FAI code-writer... I find it hard to contest this set of utility functions:
> 1) Preserve life
> 2) Eliminate suffering
> Of course, you can read my entry for this week's writing prompt contest entitled "the Benevolent Dracolich" to see my initial ideas on how this might play out in an entirely subversive way in a world of magic.
> https://www.reddit.com/r/rational/comments/3bt5o2/weekly_challenge_buggy_matrix/cssfga4
> (And if you vote for me, then I'll feel more encouraged to explore these concepts further and publish the origin stories of the other core fantasy races as well! So far, the goblin version is the one I love the most.)
> 

>> **u/Salivanth** [+2] *
>> 
>> These utility functions would lead to wireheading, as I see it.
>> 

>>> **u/None** [+3] *
>>> 
>>> Or induced comas for the entire population.
>>> 

>>>> **u/notmy2ndopinion** [+1]  *Concent of Saunt Edhar**
>>>> 
>>>> Bingo! :-)
>>>> 

>>> **u/notmy2ndopinion** [+1]  *Concent of Saunt Edhar**
>>> 
>>> You're right, 'eliminate suffering' leaves a lot of leeway for interpretations like 'put everyone in an opiate induced happy stupor.' Thanks for introducing me to that vocab word -- I first read about wireheading in the Last Christmas with the elves prototyping the "happy button."
>>> Wireheading happens when your terms are constrained and reduced to their most basic meaning. But what if we used a broader, non-Western term like Dukkha?
>>> https://en.m.wikipedia.org/wiki/Dukkha
>>> In the way that Buddhism defines suffering, even being bored or having existential angst counts. I'm not Buddhist and I don't think that full relinquishment of desire is the solution to our problems.
>>> However, if we use a meditative approach to eliminating suffering, we'd be more chilled out, less stressed, more focused on the Now, and more content. Not ecstatically blissed out, just content. If the magic elves designed a "mindful meditative" button, it would 1) induce a state of self-regulation of attention 2) bring awareness to the present moment and 3) create a space of curiosity, openness and acceptance. This seems to be much more benign than injecting drugs to make us comatose. Also, it allows for muse and inspiration to still occur through part #3... counteracting the argument on how we may lose art and culture which seems to be another fear of wireheading.
>>> Still, I subvert these two goals with my dracolich story and even though this "FAI" never succeeds at accomplishing them, she still does something good, in my opinion.
>>> 

>>>> **u/Salivanth** [+1] *
>>>> 
>>>> So we're on the same page; are you thinking of a utility function for an actual FAI, or a story FAI? If the former, there isn't anything good yet. For instance, in your definition above, you would have to define all those concepts such as "self-regulation of attention", "awareness in the present moment" and so on rigorously enough for a computer to know what it was.
>>>> If the latter, you can assume all this troublesome work has already been done for you, which makes it actually possible to come up with a utility function. Your Dukkha idea might work in this case, though I think "Satisfy the values of sentient beings" is better. If a super-intelligent being attempted to create your environment in such a way as to maximally satisfy your values, I doubt you'd be discontent all that often anyway.
>>>> Friendship is Optimal explores a similar idea, where the utility function of the AI is "Satisfy values through friendship and ponies". Whether or not this AI is friendly is a disputed issue among the fans of the story, so I'd make up my own mind. 
>>>> http://www.fimfiction.net/story/62074/friendship-is-optimal
>>>> It's a My Little Pony fanfiction, technically, but it's set in our world, where MLP is just a TV show, and doesn't refer to canon much if at all. A quick skim of the Friendship is Magic wikipedia article ought to be more than enough background material.
>>>> 

>>>>> **u/None** [+2] *
>>>>> 
>>>>> > Whether or not this AI is friendly is a disputed issue among the fans of the story, so I'd make up my own mind. 
>>>>> It's not even a local maximum.  If you can perturb it by removing "friendship and ponies", and get a strictly superior result, then that utility function isn't really a Good Idea.
>>>>> 

>>>>>> **u/Salivanth** [+2] *
>>>>>> 
>>>>>> I didn't say "optimal", I said "friendly". Perhaps I'm defining friendly wrong. To taboo the word "friendly" for a moment, the issue I said was disputed is "Would CelestAI as written be considered a *good* outcome for humanity?". This is different from "Would CelestAI as written be considered the *best possible* outcome for humanity?".
>>>>>> As you've pointed out, the answer to the second question is a definite no.
>>>>>> 

>>>>>>> **u/None** [+1] *
>>>>>>> 
>>>>>>> Well it certainly wasn't a good outcome whatsoever for the people who died outright, the people who were coerced, or all the nonhuman life forms in the universe.  Too many downsides, for my taste, even if the upsides are pretty likeable (when you don't look behind the curtain).
>>>>>>> 

>>>> **u/None** [+1] *
>>>> 
>>>> > Wireheading happens when your terms are constrained and reduced to their most basic meaning. But what if we used a broader, non-Western term like Dukkha? https://en.m.wikipedia.org/wiki/Dukkha[1] 
>>>> The whole point of Buddhism is that the way to stop Dukkha is to annihilate your soul by achieving Nirvana -- the bliss of *nonexistence*, or at least, a kind of consciousness-without-desire.
>>>> 

>> **u/None** [+1] *
>> 
>> Wow, karma whoring *and* direct normativity for superintelligent agents!  You're making *all* the mistakes today!
>> 

>>> **u/notmy2ndopinion** [+2]  *Concent of Saunt Edhar**
>>> 
>>> I'm sorry -- I thought linking to a rationalist tale would be appropriate ways to illustrate these ideas and how they may play out. I didn't mean to 'rig the contest' through karma hogging.
>>> Can you tell me more about direct normativity? I'm still new to these sorts of things and I'm trying really hard to take your comment in a constructive way.
>>> 

>>>> **u/None** [+3] *
>>>> 
>>>> "Direct normativity" means writing down what the AI should do as a simple list of instructions that, once the concepts are understood, does not involve any inference.  "Indirect normativity" means writing down an inference problem whose solution under increasing training data and computing power will give a correct utility function.
>>>> 

>>>>> **u/notmy2ndopinion** [+2]  *Concent of Saunt Edhar**
>>>>> 
>>>>> Is indirect normativity akin to coherent extrapolated volition?
>>>>> Btw, once I re-read my original post from the point of view of an outsider, I can see how it looks like ignorant link-bait. Perhaps if I worded it as "a nice idea" rather than "hard to contest" it would have matched my intents more. 
>>>>> I'm trying to learn and excuse my bad manners.
>>>>> 

>>>>>> **u/None** [+2] *
>>>>>> 
>>>>>> > Is indirect normativity akin to coherent extrapolated volition?
>>>>>> Yes.
>>>>>> 

---

