## What Would You Ask an Oracle?

* Author: u/None *
* URL: https://www.reddit.com/r/rational/comments/9ewbtg/what_would_you_ask_an_oracle/
* Score: 26

* Created: 2018-09-11T10:28:28

### Post:

You have access to an Oracle Machine and can present it with any valid decision lproblem (yes or no question with a valid answer) in natural language. The Oracle Machine will invariably give you the correct answer. What question(s) do you ask to maximise your utility? (Once you finish your question(s) the Oracle banishes itself from existence and forbids it (or a similar oracle from ever existing again).    
   
There are a few ways to interpret the premise, so I'll define two axes along which the question can be interpreted:   
  
1. You can only ask the oracle **one** question.    
2. You can ask the Oracle one question every hour (arbitrarily chosen to prevent access to the Oracle from being too broken, while being significantly more powerful than in the first scenario).    
  
a. The Oracle is omniscient and can answer correctly even in questions involving truly random phenomena.    
b. The Oracle is only nigh omniscient and cannot predict truly random phenomena, but can completely predict all deterministic phenomena.   
   
A question like this has been done before, but I thought it was too I'll defined when I read it and with too much potential for abuse (author added several extra patches to prevent certain kinds of munchkinry). I thought of this as a more sensible version but never got around to posting it, before a certain fic I read made me revisit the question.   
&nbsp;    
Answers format should be prefixed by "**Scenario (x,y):**" (where x is from {1,2} and y is from {a,b}).   

Scenario (1,a) is the scenario that I find most interesting.    

### Comments:

> **u/SkeletonRuined** [+15]  (57 minutes later)
> 
> Scenario (1, a): Since it's natural language, maybe try for some linguistic tricks. "Is the following true: I will win the lottery tomorrow if and only if you answer my question with 'yes'?"
> 
> Scenario (2, b): You can probably get pretty far just asking a series of "Is the first bit of the smallest possible computer program to accomplish X a 1?", "Is the second bit of the smallest possible computer program to accomplish X a 1?", etc. This only transfers data to you at 24 bytes per day, but might work depending on how small truly optimal programs are. (We have some reason to suspect they are tiny but unfindable - finding the smallest version of a program is provably uncomputable in general. But the Oracle could know it!)

>> **u/None** [+10]  (an hour later)
>> 
>> (1,a): The oracle wouldn't answer if the question doesn't have a truth value. This isn't a hack but is part of the specification of Oracle machines in general. They can solve every decision problem but not all problems qualify as decision problems. That said, I don't really get the question I guess. Supposing you were going to win the lottery anyway it would answer "yes", and if you were going to lose, the oracle would answer "no"? That sounds too simple a resolution, so I suspect I'm not fully understanding the question.  
>> &nbsp;    
>> (2,b): I made it a 1h limit to prevent this, but it seems I wasn't sceptical enough. Also, what would the program run on? Software that run on modern computers are pretty bloated aren't they? Can a few KB software usefully run on a modern computer? There's also the fact that payoff would most likely be in years. I think I'll update to a question a day if this is still possible.   
>> &nbsp;

>>> **u/VirtueOrderDignity** [+6]  (2 hours later)
>>> 
>>> > Also, what would the program run on? Software that run on modern computers are pretty bloated aren't they?
>>> 
>>> You could make up a virtual machine with arbitrarily small and terse instructions to get around this, then specify an optimal program on said virtual machine. As a first attempt, you might include an algorithmic random number generator that can provably reach a number of arbitrary-length sequences exponential to the length of the seed, then use the oracle to guess the seed of a much longer program.

>>>> **u/None** [+1]  (6 hours later)
>>>> 
>>>> So what particular program would you pick to construct first? An aligned AI is almost certainly out of your reach.

>>>>> **u/VirtueOrderDignity** [+2]  (6 hours later)
>>>>> 
>>>>> A program that would maximize my profit over [period] if I plugged it into my cryptocurrency exchange's API. It seems reasonable to assume that smaller periods would result in simpler programs, especially if the oracle could just make it output a predefined series of buy and sell orders without having to look at the prices or do any calculation.

>>>>>> **u/None** [+2]  (7 hours later)
>>>>>> 
>>>>>> Yeah. Well that's a way to get rich quick, but not the kind of program I was looking for I guess.

>>> **u/Ristridin1** [+2]  (11 hours later)
>>> 
>>> (1,a): The trick is in the "if and only if". Let X be the statement "I will win the lottery tomorrow", and let Y be the statement "you will answer my question with 'yes'". Then X if and only if Y means that if X is true, then Y is true, and conversely, if Y is true, then X is true. In other words, X if and only if Y means that both have to be true, or that both have to be false.
>>> 
>>> Now, if the answer to the question is 'yes', then this answer says that X is true if and only if Y is true. On the other hand, Y is true, and therefore X is true, so you will win the lottery.
>>> 
>>> Conversely, if the answer to the question is 'no', then Y is false. If X were also false, then the answer to the question should be yes (since FALSE <=> FALSE is a TRUE statement), but since it is not, the only remaining case is that X must be true.
>>> 
>>> In either situation, X is true. You basically force the oracle to answer the question in a way that implies you win the lottery.
>>> 
>>> ...
>>> 
>>> Or at least, that's what Scenario (1,a) is intended to do. It actually breaks if the oracle does not assume X is completely determined and always answers 'no' to this question. Namely: If you win the lottery, the oracle answers with no, and if you don't win the lottery, the oracle also answers with no. Then certainly Y will be false regardless of whether or not X is true.
>>> 
>>> I think that issue can be fixed by changing your question: "Is the following true: I will win the lottery tomorrow OR you will answer this question with 'no'" (revised from a comment by Yudkowski in a similar thread). If the answer is 'yes', then the second statement is false, therefore the first has to be true (an OR-statement is true if at least one of the statements is true). The answer 'no' cannot be given, since if 'no' is given, at least one of the statements is true, meaning the answer would have to be 'yes'.

>>>> **u/None** [+1]  (22 hours later)
>>>> 
>>>> Thanks and congratulations, you've won the thread. Your question causes the Oracle to ensure you win the lottery tomorrow (the thought experiment has the Oracle being very powerful in addition (or by virtue) of their (nigh) omniscience)).   
>>>> &nbsp;   
>>>> > revised from a comment by Yudkowski in a similar thread    
>>>> 
>>>> Link please?

>>>>> **u/Ristridin1** [+1]  (a day later)
>>>>> 
>>>>> https://www.reddit.com/r/rational/comments/8t7v1i/an_omniscient_source_offers_to_provide_a_truthful/e15iddx/

>> **u/Linearts** [+5]  (a day later)
>> 
>> 24 bits per day, not bytes.

>> **u/Ozymandias195** [+3]  (7 hours later)
>> 
>> If there’s 26 characters in the English alphabet, plus a space, could you not just use your method to create a program to output a textual answer to a question with a non yes/no answer? Like if you asked  “If I created a program that outputs the name of the substance that can cure cancer, would the first character of the output message be A?” And repeat every hour, you’d get approximately 11-12 characters a day. Depending on how you frame the question you could probably get full sentence answers in a few days. I also don’t understand computers too well so please tell me if this is totally stupid

>>> **u/ddejong42** [+7]  (7 hours later)
>>> 
>>> You could speed this up with a binary search - start with the question of "Is the first character something between A and M inclusive?" and narrow it down that way.

>>>> **u/Ozymandias195** [+3]  (7 hours later)
>>>> 
>>>> That’s smart, there’s probably ways to make it go even quicker by analyzing which letters are more likely to proceed others

>>>>> **u/None** [+3]  (8 hours later)
>>>>> 
>>>>> Yeah, and that sort of analysis shouldn't be too difficult. I think this is a nice, new solution.

>>>>>> **u/Ozymandias195** [+4]  (9 hours later)
>>>>>> 
>>>>>> Also going on, if we ask if FTL travel is possible, and the answer is yes, we could get our program to write a step by step guide on how to achieve it. It could take millennia with this method but we could also ask if humans could possibly achieve FTL autonomously and if so if it would take longer than using the oracle, and if yes the oracle method would be worth it despite taking so long

>>> **u/None** [+2]  (2 days later)
>>> 
>>> The truly optimal approach is to ask the oracle to generate the bits of a piece of compressed text. For example, a very simple form of compression is dictionary compression where the oracle just outputs the offset of the word within a dictionary. In practice we would probably use one of our more sophisticated text compression methods, which can achieve very low bit per word rates.

>>> **u/None** [+1]  (7 hours later)
>>> 
>>> Nah, this sounds like a great answer. The 1 bit per hour is significantly more powerful than a single bit. Curing cancer is a great application.

>>>> **u/Ozymandias195** [+3]  (7 hours later)
>>>> 
>>>> But I was way off about 11-12 characters a day, it would be more like 1-3 a day, which is much slower but definitely useful over time

>>>>> **u/None** [+1]  (8 hours later)
>>>>> 
>>>>> Yup, you could find the cure to cancer, a room temperature superconductor, etc.

>>>>> **u/Solonarv** [+1]  *Chaos Legion* (17 hours later)
>>>>> 
>>>>> Written English actually contains about 1 bit of information per character, so with proper coding you should be able to average 24 bits per day.

>>>>>> **u/None** [+1]  (a day later)
>>>>>> 
>>>>>> Based on my understanding of info theory, this is blatantly false.

>> **u/SkinnyTy** [+2]  (9 hours later)
>> 
>> Make X a precise model of existance. It would be slow, but you might learn a lot about the nature of our universe which may reveal shortcuts to infinite energy or some other important game breaking piece of info.

>> **u/GeneralExtension** [+1]  (3 days later)
>> 
>> >depending on how small truly optimal programs are. 
>> 
>> Who says it's optimal? [https://stackoverflow.com/questions/7717691/why-is-the-minimalist-example-haskell-quicksort-not-a-true-quicksort](https://stackoverflow.com/questions/7717691/why-is-the-minimalist-example-haskell-quicksort-not-a-true-quicksort). You have to include your specifications of 'optimal' in X, or you'll get something that's short, but doesn't necessarily have a great run time. Like [bubble sort](https://en.wikipedia.org/wiki/Bubble_sort): short but slow.
>> 
>> &#x200B;
>> 
>> >provably uncomputable in general.
>> 
>> That's surprising. I'd have thought you could use brute force; Just run "0", then "1", then "10", etc. 
>> 
>> &#x200B;
>> 
>> >"Is the first bit of the smallest possible computer program to accomplish X a 1?"
>> 
>> What happens if you ask this question about a task for which there is no computer program?

> **u/CCC_037** [+12]  (3 hours later)
> 
> (1, a)
> 
> Hmmm. You want maximum beneficial effect from a single bit of information - in effect, a single yes/no answer.
> 
> So, first of all, let's consider how to maximise the effect. The biggest thing that you can do - the thing that will have the most far-reaching effect - is to completely change the direction of your life.
> 
> Therefore, ideally, you need two possible lives. For example, you might consider life as an author, writing inspirational stories that encourage others to action; or you might consider life as a scientist, expanding and exploring the realms of knowledge. There are thousands of potential paths a life can take; so you pick the two options most suited towards your personal talents and abilities.
> 
> Of these two potential life paths, pick one. Doesn't matter too much which one. (Let us say that, for example, I pick 'novelist').
> 
> Then the question is, "Will it be more beneficial for humanity in general, over the long term, if I were to spend the rest of my life as a novelist?"
> 
> If the answer is yes, I become a novelist and attempt to write and publish stories.
> 
> If the answer is no, I become a scientist and work on expanding the bounds of what knowledge is known.
> 
> Since the oracle can predict even random phenomena directly, the oracle can therefore see which of these two options is more beneficial to humanity in the long term and thus allows me to pick the best option; and the potential scope of the consequences is huge...

>> **u/None** [+5]  (6 hours later)
>> 
>> That's a different route than others have suggested, and I like it. Not sure I'd ask that question personally myself.

> **u/hyphenomicon** [+10]  *seer of seers, prognosticator of prognosticators* (49 minutes later)
> 
> Even in scenario 1, preserving indirect access to the Oracle Machine for future questions, perhaps through controlling other people's questions, would be an obvious goal. So let's further specify that the Oracle disappears from existence, and forbids itself or a similar Oracle from ever existing again, after you finish your question.

>> **u/None** [+3]  (an hour later)
>> 
>> Thanks, I will add that.

> **u/ashinator92** [+7]  (5 hours later)
> 
> There was a biweekly prompt that was related to this, i think :). It uses a time machine instead of an oracle, but close:
> 
> [https://www.reddit.com/r/rational/comments/8daskl/biweekly\_challenge\_complexity/](https://www.reddit.com/r/rational/comments/8daskl/biweekly_challenge_complexity/)
> 
> &#x200B;
> 
> &#x200B;
> 
> Shamelessly copying from /u/xamueljones post:
> 
>  [For God-like power, all I need is one bit](https://docs.google.com/document/d/1UiGUYFm3CfO_6Z_dDIZUsU3P4izjY6FAOq6BGLbeIMk/edit#heading=h.b3ly0s8pl1qo) (5405 words)

>> **u/None** [+1]  (6 hours later)
>> 
>> Thanks for the link. I'll read it and get back to you.

>>> **u/None** [+1]  (7 hours later)
>>> 
>>> Really enjoyed it. They had access to more than one not though.

> **u/SimoneNonvelodico** [+4]  *Dai-Gurren Brigade* (3 hours later)
> 
> "Are you really a perfect Oracle?"
> 
> No, seriously. Uhm. Being just a Yes/No question it's kinda hard. You can't crack any serious problems unless you already have a very good hypothesis in version 1), and version 2) still limits you a lot due to the one hour interval. And with a lot of questions ("Is immortality possible?" "Can we travel FTL?") I suspect the answer would be a discouraging and rather bleak "No", which far from being very useful, might in fact be something I'd just rather not know for sure. You can't even use this damned thing to, say, prove Riemann's hypothesis, because it's not like it will give you the demonstration, and no mathematics journal will accept "the Oracle told me" as a viable "Methods" section in a paper.

>> **u/Ozymandias195** [+4]  (6 hours later)
>> 
>> I think as far as benefitting humanity, it would be extremely beneficial to know whether FTL is possible. Why pour massive resources into something when we can definitely prove it doesn’t exist? Similarly for asking whether certain diseases can be cured

>>> **u/SimoneNonvelodico** [+3]  *Dai-Gurren Brigade* (10 hours later)
>>> 
>>> Asking "can cancer be cured" would probably produce a pointless answer. Cancer isn't a single disease, and of course it *can* be cured - we cure it already, it's just not 100% reliable (but then, what is?). Knowing if FTL signalling is possible would certainly be an interesting constraint to any theories in the future, but it suffers from the problem of many other such questions - it's much more useful if the answer is "yes" than "no". Ideally, I think I'd want to ask one question where knowing is *always* useful, either way.

>>>> **u/Ozymandias195** [+2]  (10 hours later)
>>>> 
>>>> Asking if there’s a cure for cancer is a bit too simple, but something like “is there a universal treatment for all cancers with a 90% or higher success rate” might prove useful. And it’s indirectly useful to know whether certain things are impossible, despite not having direct utility like if they are

>>>>> **u/SimoneNonvelodico** [+2]  *Dai-Gurren Brigade* (11 hours later)
>>>>> 
>>>>> I think that might be valuable for the "one question per hour" Oracle. But I wouldn't make it my only question ever. Also because, at a difference with knowing that FTL signalling is possible (which at least implies there is something fundamentally wrong with our knowledge of physics), such a cure isn't intrinsically impossible, so knowing that it exists tells us nothing really interesting or that can help us find it.

>> **u/None** [+1]  (6 hours later)
>> 
>> Surely there's got to be a question to which knowing the answer would be beneficial. I might ask it if many worlds is true I guess, in which case quantum suicide becomes a viable route to munchkining reality.

>>> **u/alan_wade** [+1]  (7 hours later)
>>> 
>>> > in which case quantum suicide becomes a viable route to munchkining reality.
>>> 
>>> Can you explain what that is?

>>>> **u/None** [+2]  (7 hours later)
>>>> 
>>>> Assume Many Worlds is true. Connect a macrospic effect to the output of a quantum RNG. If the quantum RNG output wasn't what was desired kill yourself. Suppose you're trying to crack a password for which there are quadrillions of combinations. All you need is a quantum RNG that you can map to each of the inputs. Try each of the outputs of the quantum RNG for the password. Kill yourself if you get the wrong password. Because of Many Worlds, the world in which you survive would be the world in which you got the right password, and you would only ever observe your survival. This can be used to e.g pick the winning ticket for the lottery, game the stock market, etc.

>>>>> **u/SimoneNonvelodico** [+3]  *Dai-Gurren Brigade* (10 hours later)
>>>>> 
>>>>> I'm very iffy on this interpretation because it also relies on some notions about consciousness: most notably, that consciousness somehow transcends the individual quantum evolution branches. I am actually of the opposite idea, that quantum collapse is an artefact of our consciousness being confined to only one branch.

>>>>>> **u/None** [+1]  (23 hours later)
>>>>>> 
>>>>>> Nah, it doesn't require any special notion of consciousness. What happens is that at the experiment, several copies of you are made. All copies but one died, so the copy that does survive experiences the beneficial outcome. Because the copies were identical before the split, "you" (in this case the copy that survives) would only experience yourself going through the beneficial outcome. Continuity would be unbroken.

>>>>>>> **u/SimoneNonvelodico** [+4]  *Dai-Gurren Brigade* (23 hours later)
>>>>>>> 
>>>>>>> Unless you're one of the many unlucky copies who, y'know, died, end of story.

>>>>>>>> **u/None** [+1]  (23 hours later)
>>>>>>>> 
>>>>>>>> Yeah, but you don't experience it. What is actually experienced is survival and victory.

>>>>>>>>> **u/SimoneNonvelodico** [+3]  *Dai-Gurren Brigade* (23 hours later)
>>>>>>>>> 
>>>>>>>>> And that's the assumption on consciousness we're talking about. You treat individual consciousness as a sort of fluid that's hosted in many containers but that, upon one container breaking, is just poured into the remaining working ones. You don't admit the possibility of consciousness simply *ending*, or rather, you don't admit to the possibility of *your* consciousness ending. 
>>>>>>>>> 
>>>>>>>>> If your idea is right, then everyone's life past 80 years old will get progressively weirder and weirder, because you're basically saying *subjective consciousness can never end, no matter what*.
>>>>>>>>> 
>>>>>>>>> Sure, somewhere in the infinite branchings of the quantum multiverse (and that's just if we accept Many Worlds), there's going to be *one* of you that survives against all odds. It just isn't going to necessarily be *you*.

>>>>>>>>>> **u/None** [+2]  (23 hours later)
>>>>>>>>>> 
>>>>>>>>>> Aah, I consider all copies of "me" to be "me". My notion of consciousness means that any entity who's psyche, mind, experiences and utility function is sufficiently similar to me is me. Also important to that notion is continuity. According to that notion, the copies of me in other worlds (which diverged at the quantum experiment) are all me. I'm a materialist, so I don't have any mystical ideas about consciousness (exactly the same configuration of matter in my brain currently will also be "me" for example.   
>>>>>>>>>> &nbsp;    
>>>>>>>>>> I think subjective consciousness can end, but I choose to treat all copies of me as "me", which is the difference.

>>>>>>>>>>> **u/SimoneNonvelodico** [+3]  *Dai-Gurren Brigade* (a day later)
>>>>>>>>>>> 
>>>>>>>>>>> But how can you be the same "you" as the "you" that underwent a completely different path along the quantum wavefunction? Why wouldn't that "you" actually be an "other" no more and no less than I, or your mother, or your boss are - just an other with very similar memories *up to a certain point*?

>>>>>>>>>>>> **u/None** [+1]  (a day later)
>>>>>>>>>>>> 
>>>>>>>>>>>> That's not how I conceive of consciousness. I think consciousness is like morality in certain regards, and so feel my notion of consciousness is satisfactory. I'm aware others don't think like that and would not try to persuade them to think like I do. I do not expect to be easily persuaded otherwise (e.g discovering that materialism is false may persuade me otherwise). I think a notion of consciousness that doesn't consider yous in other worlds "you", will not consider a you that underwent teleportation "you" or a you that was uploaded.

>>>>>>>>>>>>> **u/SimoneNonvelodico** [+3]  *Dai-Gurren Brigade* (a day later)
>>>>>>>>>>>>> 
>>>>>>>>>>>>> A "you" that was teleported or uploaded is indeed tricky IMHO. I think the only way that would keep our notion of uniqueness and continuity consistent is if in some way the "you-ness" property of "you" was tied to a specific quantum state, which then would make "you" subject to the no-cloning theorem: you can't be teleported or uploaded without *also* being destroyed elsewhere, as a necessary condition. So it's like a spin flip between two particles - you're simply moved around, really, or at least you can be seen as doing that.

>>>>>>>>>>>>>> **u/crivtox** [+2]  *Closed Time Loop Enthusiast* (a day later)
>>>>>>>>>>>>>> 
>>>>>>>>>>>>>> Wouldn't interacting whith anything change your  state?

>>>>>>>>>>>>>>> **u/SimoneNonvelodico** [+1]  *Dai-Gurren Brigade* (a day later)
>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>> Yeah, of course. It would entangle it. I never said it has to be a *static* state. We don't think of ourselves as "dying" just because we change due to external influences. The no-cloning theorem still applies.

>>>>>>>>>>>>>>>> **u/crivtox** [+2]  *Closed Time Loop Enthusiast* (a day later)
>>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>>> Why not just consider that any future instances of your computation are you?

>>>>>>>>>>>>>>>>> **u/SimoneNonvelodico** [+1]  *Dai-Gurren Brigade* (a day later)
>>>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>>>> How does that match my experience? I only experience *one* timeline, not multiple parallel ones. Seems much simpler and closer to what I actually observe to assume that my qualia are tied to a single specific branch.

>>>>>>>>>>>>>>>>>> **u/crivtox** [+1]  *Closed Time Loop Enthusiast* (a day later)
>>>>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>>>>> You only experience only one timeline , I'm just saying that all posible future you are you.
>>>>>>>>>>>>>>>>>> You have aprobability of experiencing being whoever of them.
>>>>>>>>>>>>>>>>>> Like you basically were saying in the many worlds case.
>>>>>>>>>>>>>>>>>> But  instead of relying on "continuity" you just consider anything that is like you to be potentially you.
>>>>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>>>>> If someone copies you to a computer  you have a 50% chance of experiencing being the one on the computer.
>>>>>>>>>>>>>>>>>> Not after they copy you , since you already have diferent memories and thoughts , but on the moment they copy you.
>>>>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>>>>> The diference in the death thing  Is that I divide the subjective probability of being any future self between the ones that keep existing  existing , while you assign a probability to being the one that dies.
>>>>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>>>>> I'm thinking about  some way of dying where you just stop existing , in most other cases there would be versions of you that  experience slowly dying .
>>>>>>>>>>>>>>>>>> At t0 I exist and at t1 I don't.
>>>>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>>>>> Its not that you somehow experience all universes or something like that.
>>>>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>>>>> And if you  destroyed all copies of me and made a computationally equivalent one in 1000 years , I will consider that I will experience waking up in a 1000 years. 
>>>>>>>>>>>>>>>>>> I can experience lying on the floor bleeding and slowly loosing consciousnness
>>>>>>>>>>>>>>>>>> You can even have half dead versions of me that would be basically like being death for most purposes.
>>>>>>>>>>>>>>>>>> but I cannot experience not existing .

>>>>>>>>>>>>>>>>>>> **u/SimoneNonvelodico** [+3]  *Dai-Gurren Brigade* (a day later)
>>>>>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>>>>>> So by that logic, if you tried to crack a hash using quantum suicide, the most likely outcome would be that... you'd be dead. Though sure, in the end, the only you that'd be still around would be the one who can savour triumph.
>>>>>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>>>>>> I mean, ok, you can't really "experience non existing", but you can break the continuity of experience forever. Though in general it's hard to wrap one's head about what exactly does this mean. I'm not saying it's perfectly clear to me either, but as a general rule: a) I wouldn't take evidence for MWI as evidence for quantum immortality, and b) I wouldn't trust myself to be objective about judging scenarios promising immortality, because frankly as all of the history of religions teaches us those are *way* too tempting to think we can easily assess them fairly.

>>>>>>>>>>>>>>>>>>>> **u/crivtox** [+1]  *Closed Time Loop Enthusiast* (a day later)
>>>>>>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>>>>>>> I would't try to hack a hash like that for a lot of reasons of course .But yeah I would consider the most likely outcome that I would end dead , but I would consider savoring the triumph the most likely thing for me to experience .  
>>>>>>>>>>>>>>>>>>>> For the purposes of self preservation I think I care about what I experience (and otherwise lots of thought experiments become really weird).  
>>>>>>>>>>>>>>>>>>>> For other purposes (like thinking about all the people I'm leaving behind and how my death afects them )I do care.
>>>>>>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>>>>>>> Quantum suicide is an horrible idea, but if I was teleported I wouldn't consider it death ,and If I was uploaded destructively I wouldn't care as long as the one that dies does it instantly( or at least faster than neurons fire or whatever change in the brain)
>>>>>>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>>>>>>> A problem in that kind of thing is that personal identity  is not fundamental,just a feature of my utility function , that determines If I care about  certain computations.

>>>>>>>>>>>>>>>>>>>>> **u/SimoneNonvelodico** [+2]  *Dai-Gurren Brigade* (a day later)
>>>>>>>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>>>>>>>> Well, sure, that's why things like that are philosophically very messy. I just don't think the idea behind quantum immortality is sound in the sense that it doesn't really apply to how our qualia *work*. Teleportation and uploading sound like they may work, but perhaps there's actually some yet not discovered principle why they wouldn't. Understanding what is the origin of qualia (imagine if there was a part of the human brain you can zap to turn someone into a perfectly functional P-zombie - ok, no, don't imagine that, that's a *horrifying* thought) would be a prerequisite to understanding how these things work in any meaningful way.

>>>>>>>>>>>>>>>>>>>>>> **u/crivtox** [+1]  *Closed Time Loop Enthusiast* (a day later)
>>>>>>>>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>>>>>>>>> I kind of asume that an upload would be conscious , and a P-zombie doesn't sound like somehting that can really exist .I'm not saying I'm not sure how consciousnes works but  "imagine if there was a part of the human brain you can zap to turn someone into a perfectly functional P-zombie " this really sounds incoherent in some way .Consciousness is whatever makes me say and think I'm conscious , or it would be really suspicious to have something that says its conscious for no reason that just happens to be the same thing that can host this mysterious consciousness thing.
>>>>>>>>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>>>>>>>>> A teleporter clearly doesn't create P-zombies ,so that case Is pretty much only about continuity , and I think computational continuity is the one that makes more sense( since if you start doing though experiments the concept of "original" becomes weird really fast ,and many worlds already forces  you to decide there are more than one entities on the future you can call you).
>>>>>>>>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>>>>>>>>> Btw  in the quantum suicide hash thing now that I think of it there is more than a  50% chance you will find yourself to be the version of you that by chance gets a hash  that contains "do not mess whith time" or somethng like that and decides to stop if you don't take precautions for that.

>>>>>>>>>>>>>>>>>>>>>>> **u/SimoneNonvelodico** [+3]  *Dai-Gurren Brigade* (a day later)
>>>>>>>>>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>>>>>>>>>> I don't really believe in P-zombies either, but can't discard the idea. But yeah, if you asked me, I think Searle's Chinese room argument and all related ideas are nonsense. It's just weird to accept that "systems" can be conscious even when if you look at their individual information-processing parts they don't look conscious at all. If I had to give my interpretation of it I'd say what makes the whole "I think, therefore I am" thing work for me is a boundary between a very highly integrated information processing system (my brain) and a much lower integrated information processing system (the society at large of which I am part and with which I exchange information). Without this sort of distinction I'd have then to speculate on where does it stop - are countries, or humanity as a whole, "conscious" in the sense that they do experience inner life even though we can't communicate with them? That too sounds like nonsense, but it's hard to put my finger on *why* is it that I expect it not to be true. Seems too much of a gut feeling.

>>>>>>>>>>>>>>>>>>>>>>>> **u/crivtox** [+3]  *Closed Time Loop Enthusiast* (a day later)
>>>>>>>>>>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>>>>>>>>>>> btw since this is a rational fiction subredit this conversation remembers me this story that eliezer wrote  [https://www.lesswrong.com/s/FqgKAHZAiZn9JAjDo/p/fsDz6HieZJBu54Yes](https://www.lesswrong.com/s/FqgKAHZAiZn9JAjDo/p/fsDz6HieZJBu54Yes) .

>>>>>>>>>>>>>>>>>>>>>>>>> **u/SimoneNonvelodico** [+2]  *Dai-Gurren Brigade* (a day later)
>>>>>>>>>>>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>>>>>>>>>>>> Twenty lines in, I'm already laughing my ass off XD.

>>>>>>>>>> **u/None** [+2]  (2 days later)
>>>>>>>>>> 
>>>>>>>>>> > If your idea is right, then everyone's life past 80 years old will get progressively weirder and weirder, because you're basically saying subjective consciousness can never end, no matter what.
>>>>>>>>>> 
>>>>>>>>>> Technically, you can't (conservatively, risking little) disprove this is true until you yourself are 80 and can observe if this sort of thing is happening to you or not. It doesn't apply to people who *aren't* you.

>>>>>> **u/crivtox** [+1]  *Closed Time Loop Enthusiast* (a day later)
>>>>>> 
>>>>>> Does that mean that there are philosophical zombies in the other branches?.Why say there is a magical consciousness stuff that behaves differently from everything else  , why do you believe what you believe ?
>>>>>> 
>>>>>> Anyway your idea doesn't work ,  since if I'm not mistaken the   wavefunction is continuous and  talking about branches or universes or whatever is just a way to put it in a easy to understand way  but it doesn't really work like that .

>>>>>>> **u/SimoneNonvelodico** [+3]  *Dai-Gurren Brigade* (a day later)
>>>>>>> 
>>>>>>> The wavefunction may be continuous, but states are discrete. Possibly infinite, but discrete. And no, I don't mean there are philosophical zombies.
>>>>>>> 
>>>>>>> Take it this way: there's your typical Schroedinger cat system, in a superimposed state |alive> + |dead> (I'll omit the normalization factors for convenience). Your brain is still in the |doesn't know> state. You then open the box. Unitary quantum evolution would then have the total wavefunction of the box + your brain to evolve into:
>>>>>>> 
>>>>>>> |alive>|knows it to be alive> + |dead>|knows it to be dead>
>>>>>>> 
>>>>>>> At this point, the Copenhaghen interpretation mumbles "something something abracadabra measurement and collapse" and says we're only left with either  |alive>|knows it to be alive> or  |dead>|knows it to be dead>, and the system keeps evolving from there. This, IMHO, is not very satisfactory. However the way I see it is, this is only puzzling if we assume that our brain in the entangled state should see somehow the cat both alive *and* dead. That is not what the wavefunction describes, though. The wavefunction describes a state where one one side we have a brain *absolutely, positively sure the cat is alive* and on the other one that is *absolutely, positively sure the cat is dead*. Either brain has *only seen one state*, and would have to wonder where did the other even go! And so, how do we decide which brain should feel like "me", and which one shouldn't? The answer is, we can't. They both are "me". They just are "me who saw the cat alive" and "me who saw the cat dead". They both exist, in configuration space. They both are 100% sure they saw a single, classical outcome from the experiment. They both think the wavefunction mysteriously *collapsed* - only, in different ways.
>>>>>>> 
>>>>>>> There's some additional stuff necessary to justify of course "why those two specific states" and "why is the cat's density matrix diagonal in them" but honestly I feel like that's well justified by decoherence theory. Put together, these two things form a complete explanation of quantum weirdness, if a somehow underwhelming one. It's not something I alone came up with, BTW, it's one possible "soft" interpretation of Many Worlds, in which said worlds are subjective. It's mentioned for example in [this paper](https://arxiv.org/abs/quant-ph/0312059) as the "many minds" interpretation.

>>>>>>>> **u/crivtox** [+2]  *Closed Time Loop Enthusiast* (a day later)
>>>>>>>> 
>>>>>>>> Well yeah I agree whith that interpretation(though I was confused about states ) but then I don't understand why you you disagree whith dragon god and said 
>>>>>>>> "Sure, somewhere in the infinite branchings of the quantum multiverse (and that's just if we accept Many Worlds), there's going to be one of you that survives against all odds. It just isn't going to necessarily be you."
>>>>>>>> There is no meaningful concept of youness to be had there.
>>>>>>>> You have to consider all  sets of states that are computationaly equivalent to you as you .

>>>>>>>>> **u/SimoneNonvelodico** [+1]  *Dai-Gurren Brigade* (a day later)
>>>>>>>>> 
>>>>>>>>> There is, because the *you* you, the one that feels like he's writing those words, and reading mine, right here, right now, wouldn't feel like he's hijacked whatever code he's trying to crack with quantum suicide. He would just experience nothingness and stop existing. Continuity of experience wouldn't be guaranteed.

>>>>>>>>>> **u/crivtox** [+2]  *Closed Time Loop Enthusiast* (a day later)
>>>>>>>>>> 
>>>>>>>>>> Lets say we go foward  a unit of time .
>>>>>>>>>> Which copy of me is the me-me, the one that was experiencing those things?
>>>>>>>>>> All my future copies have me as their past , and some of them are dying independently of what I do.
>>>>>>>>>> 
>>>>>>>>>> In some of those configurations I just don't exist at all.
>>>>>>>>>> 
>>>>>>>>>> Not existing is not something I can experience ,so there aren't going to exist versions of me that die ,they just don't get to exist in the first place.

>>>>>>>>>>> **u/SimoneNonvelodico** [+2]  *Dai-Gurren Brigade* (a day later)
>>>>>>>>>>> 
>>>>>>>>>>> Both of them are "you". But at the same time, you have a 50% probability of dying.
>>>>>>>>>>> 
>>>>>>>>>>> Basically, I don't think you would experience immortality any more than you would if a copy of your consciousness was uploaded to a computer, and *then* you were killed.

>>>>>>>>>>>> **u/crivtox** [+3]  *Closed Time Loop Enthusiast* (a day later)
>>>>>>>>>>>> 
>>>>>>>>>>>> Btw I 'm not saying quantum suicide is a good idea, its a terrible one  because you will end up in increasingly weird universes,and nothing prevents your mind to become worse as long as it it keeps existing( if you get Alzheimer you are fucked , the same if you just get hit by a car and your brain is out of oxygen for a while until  quantumness saves you )   
>>>>>>>>>>>> 
>>>>>>>>>>>>  And it  has a lot of negative utility if you care about the universes you leave behind .

>>>>>>>>>>>>> **u/SimoneNonvelodico** [+3]  *Dai-Gurren Brigade* (a day later)
>>>>>>>>>>>>> 
>>>>>>>>>>>>> Eh, I was actually thinking about writing a story about that. It's a pretty nice topic.

>>>>>>>>>>>>>> **u/crivtox** [+3]  *Closed Time Loop Enthusiast* (a day later)
>>>>>>>>>>>>>> 
>>>>>>>>>>>>>> Well I guess one could be careful.
>>>>>>>>>>>>>> 
>>>>>>>>>>>>>> Actually it is really interenting .The main problem to face would be ensuring you don't try something too unlikely or something you don't want .And actually its basically about optimization processes applied over the universe ad what can go wrong whith that , which I'm really interested in that.In fact I was going to write a blog about things like closed time loops where inconsistent timelines are destroyed , and how the more you try to optimize the more dangerous something like that is.Heuristics about when an optimization process in general is dangerous , optimization daemons etc.
>>>>>>>>>>>>>> 
>>>>>>>>>>>>>> But I haven't started yet because of procrastination.  
>>>>>>>>>>>>>>  I did write something about it on an off topic thread last year I think  .
>>>>>>>>>>>>>> 
>>>>>>>>>>>>>> Using it for figuring out hashes is probably fine (maybe) well unless something goes  wrong whith he rng .

>>>>>>>>>>>>>>> **u/SimoneNonvelodico** [+3]  *Dai-Gurren Brigade* (a day later)
>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>> > But I haven't started yet because of procrastination I did write something about it on an off topic thread last year I think .
>>>>>>>>>>>>>>> > 
>>>>>>>>>>>>>>> > 
>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>> I'm sure *one* of you somewhere in the multiverse has actually gotten down to it :D.

>>>>>>>>>>>>>>>> **u/crivtox** [+5]  *Closed Time Loop Enthusiast* (a day later)
>>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>>> And also somewhere it just materialized by chance and photons changing bits on the server :b.

>>>>>>>>>>>>>>>>> **u/None** [+1]  (a day later)
>>>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>>>> :D
>>>>>>>>>>>>>>>>> Thanks for the laugh.

>>>>>>> **u/Izeinwinter** [+1]  (a day later)
>>>>>>> 
>>>>>>> No. But you are being enormously anti-social. From the perspective of most of your friends, you are just committing suicide. From the perspective of one-in-a-million of your friends, you win the lottery.

>>>>>>>> **u/crivtox** [+3]  *Closed Time Loop Enthusiast* (2 days later)
>>>>>>>> 
>>>>>>>> Yeah I already said that in a comment elsewhere.
>>>>>>>> You are optimizing your experiences , not the universe , soif you care about the universe it (its not even about other people , a paperclip maximizer wouln't quantum suicide)
>>>>>>>> There are also other reasons why quantum suicide is an horrible idea, even if yourutility 
>>>>>>>> Like welll the thing I was going to write about a year ago , the fact that optimization proceses like that can be dangerous.
>>>>>>>> maybe I should actually do it now that I'm inspired again.
>>>>>>>> Quantum suicide its a interestinc case that its similar to the tipical time loop thing I like to think about but has other constraints and its optimizing something different (maybe? dependes on the details of the time loop).
>>>>>>>> 
>>>>>>>> Edit:
>>>>>>>> And now I notice that you probably replied ot the wrong post and were saying thins to dragon god who does seem to think quantum suicide is a good idea, sorry

>>>>> **u/alan_wade** [+1]  (7 hours later)
>>>>> 
>>>>> Wow, that's really mindblowing. Almost tempting =)

>>>>>> **u/None** [+1]  (8 hours later)
>>>>>> 
>>>>>> That's only if the answer is "yes", but EY (and other smart people think so to).

>>>>>>> **u/Gurkenglas** [+2]  (14 hours later)
>>>>>>> 
>>>>>>> I don't remember EY saying he believes that works.
>>>>>>> 
>>>>>>> If it worked, wouldn't most of our probability mass end up in whatever timeline didn't end up even trying to abuse quantum immortality?

>>>>>>>> **u/None** [+1]  (22 hours later)
>>>>>>>> 
>>>>>>>> I don't understand your reasoning if quantum suicide worked the very nature of it is such that no one but people aware that a quantum suicide experiment was carried out would know that it worked. E.g (assuming MWI is true) if I do a quantum suicide experiment to say guess the winning lottery ticket, only the people aware of the experiment, and only in the world in which I correctly guessed the winning ticket would evidence be provided for MWI (and strong evidence at that). In all other worlds, I would die, but that would only be extremely weak evidence against many worlds, as everyone except me would expect to observe my death.   
>>>>>>>> &nbsp;   
>>>>>>>> EY believes in MWI, and as far as (my limited understanding) can tell, MWI implies quantum suicide.

>>>>>>>>> **u/Gurkenglas** [+2]  (22 hours later)
>>>>>>>>> 
>>>>>>>>> I don't see how MWI implies quantum suicide. What part of moving from the Copenhagen interpretation ("Superpositions collapse before conscious observation.") to MWI ("There's no reason to believe that.") makes you think that it introduces the rule "I am guranteed to survive."?
>>>>>>>>> 
>>>>>>>>> If "I am guranteed to survive." is implemented by you ending up in a random timeline where you survived, then deciding to abuse quantum immortality retroactively makes all events from your birth to that point less likely along with whatever events after your decision your abuse intends to make unlikely.

>>>>>>>>>> **u/None** [+1]  (23 hours later)
>>>>>>>>>> 
>>>>>>>>>> Quantum suicide isn't "I'm guaranteed to survive". You engineer a situation where you survive if and only if the quantum RNG produces the desired output. In some world(s) the RNG produces the desired output. The utility of this is if the desired output is say "the number that wins the lottery".    
>>>>>>>>>> &nbsp;   
>>>>>>>>>> I don't get how it makes events less likely.

>>>>>>>>>>> **u/Gurkenglas** [+1]  (23 hours later)
>>>>>>>>>>> 
>>>>>>>>>>> If you aren't guranteed to survive, if no events change probability, why would you want to kill yourself if you don't win the lottery?

>>>>>>>>>>>> **u/None** [+1]  (23 hours later)
>>>>>>>>>>>> 
>>>>>>>>>>>> You will survive because in at least one world the quantum RNG outputs the lottery number. The probability of you winning the lottery isn't changed, but you do win the lottery in some world(s) and so you don't kill yourself there. You're not immortal, but you're basically guaranteed to survive quantum suicide in some world.

>>>>>>>>>>>>> **u/Gurkenglas** [+2]  (23 hours later)
>>>>>>>>>>>>> 
>>>>>>>>>>>>> You killed yourself in the worlds where you played the lottery and lost, but you didn't kill yourself in the worlds where you never played the lottery, so almost all of your surviving selves still haven't won the lottery even if half of you played it.

>>>>>>>>>>>>>> **u/None** [+1]  (23 hours later)
>>>>>>>>>>>>>> 
>>>>>>>>>>>>>> The divergence occurs after I decide to play the lottery not before. So I survive in the worlds where I win the lottery (if I understand it correctly).

>>>>>>>>>>>>>>> **u/Gurkenglas** [+2]  (a day later)
>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>> I don't see any way for the math of the universe to notice the point at which you *make a decision*. We can agree that quantum immortality makes sense iff one can arbitrarily stake off branches of time like that. People might believe the latter because they already believe the former. I'm guessing EY doesn't.

>>>>>>>>>>>>>>>> **u/None** [+1]  (a day later)
>>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>>> Aah, I don't know the relevant maths, so I may be wrong. The assumption was that the branching occurs at the RNG experiment which is *after* your decision.

>>>>>>>>>>>>>>>>> **u/crivtox** [+1]  *Closed Time Loop Enthusiast* (2 days later)
>>>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>>>> You are both wrong ,Branching happens always, faster than your neurons fire, but if the decision is in your past you already are in the made the decision to play the lotery branch , so your posible future experiences are on that one and those are the ones that you should consider for the purpose of calculating utility.
>>>>>>>>>>>>>>>>> 
>>>>>>>>>>>>>>>>> Anyway qantum suicide Take into account that you care for somehting more than your experiences, presumably you care for allthe copies of your friends and family and universes in genereal you leave behind.  
>>>>>>>>>>>>>>>>> And there are other problems, that I can elaborate on if you want

> **u/CreationBlues** [+3]  (6 hours later)
> 
> Can the Oracle control the timing of it's response? Ex answer yes at 1 am for 0, answer yest at 1:01 for 1, answer yes at 1:02 for 2, etc.

>> **u/None** [+3]  (7 hours later)
>> 
>> Nope. You're supposed to extract maximum utility from a single bit of information.

>> **u/alan_wade** [+2]  (7 hours later)
>> 
>> Holy fuck that's brilliant.

>> **u/Trekshcool** [+1]  (8 hours later)
>> 
>> Can you elaborate on what this could be used for?

>>> **u/None** [+1]  (8 hours later)
>>> 
>>> You gain more than one bit in the first scenario.

> **u/Caliburn0** [+2]  (5 hours later)
> 
> Scenario 1.a and b
> 
> Well, first off I would consult with a whole bunch of people about what I should ask it. And when enough people have come to a consensus I would ask the question we came up with, but since that is kind of the point here, my question would be:
> 
> *Is the universe (and by universe, I mean all of existence) infinite?*
> 
> Scenario 2.a and b
> 
> I'm a bit of philosophy and physics geek, so I would probably continue asking it questions about the universe in general.
> 
> In order to earn money from it, I would offer people to ask their questions to me so I can ask the oracle.

> **u/meangreenking** [+2]  (21 hours later)
> 
> Senario (1,a): This one is pretty tough. It shouldn't be too hard to use the question to make a bunch of money via a onetime bet on some future event, but that's about the best I could do with it.
> 
> I could use it to satisfy some scientific question, but then the issue is that no one would ever believe me so all it would do is satisfy my curiosity. I could use it to answer some personal question (eg. will I live to be 100) but that would be meaningless given that with a mere 1 bit of information I would be unable to even attempt to change the results in any way.
> 
> So honestly, I would probably just use it for making money. I would take out a bunch of loans and heavily overextend myself to make a bunch of money on sports event.
> 
> Senario (2,a, b): This one is much more interesting, and far easier to exploit.
> 
> The first thing I would do is ask some questions to ensure I don't die in the time leading up to getting my more important questions done. The chance of death over the time it would take for them to be answered to be answered is fairly small but nontrivial, especially when the rewards would eventually end up with me immortal and by far the most powerful person on earth.
> 
> After that I would basically just ask it what the best question for me to ask it would be. Doing so would of course have to be changed a bit for the format of a yes/no oracle, but could fairly easily be done with "What is the [xth] bit of the ideal question set for me to ask you under 100 characters done in this same format for me to ask you translated from english into bits with yes being 1 and no being 0?"
> 
> Since its omniscent it would logically know what the best question set for me to ask it better then I ever could. Getting the result back of the question it would give me to ask it would take a while but the return would be far better then anything I could think up on my own.

>> **u/None** [+2]  (22 hours later)
>> 
>> Well I guess you solved scenario 2. I'm Scenario 1 isn't the best you can do around doubling your money? You'd be able to half your search space in any problem, but that's the best a single bit gives you. To reliably profit on bets that involve more than 2 outcomes you'd need to have pruned your search space already.

>>> **u/meangreenking** [+3]  (a day later)
>>> 
>>> Without loans yes, the best you are functionally do is doubling your money.
>>> 
>>> However if you are willing to take what would otherwise be crippling amounts of debt that would otherwise be utterly impossible to repay you could do quite a bit better.
>>> 
>>> For instance I would take out a mortgage loan for a house that the bank would be barley willing to let me get with my current salary (and that would represent decades worth of my income) and then use it for the bet instead of buying the house. On top of that I would take out tens of thousands of dollars in credit card debt and as many other less reputable loans (payday loans, loansharks) as I could.
>>> 
>>> Finally I would use leverage (which is basically using other people's money to invest in the stock market/bet at a ratio of your own money) to increase my return even further.
>>> 
>>> Honestly as long as you aren't currently in debt and people are willing to lend to you it shouldn't be all that hard to get a 10-20x return on your current annual income even if you had no hard money on hand.
>>> 
>>> Plus thanks to the fact that the oracle can tell the future, you don't even need the money or a job now, all you would need is to get it by the time your answer to the question happens.

>>>> **u/None** [+2]  (a day later)
>>>> 
>>>> Fair enough. If I could partner with someone much richer than me, I could give them a chance to double their money (say even bet of several million dollars), and they would give me a cut (which would still be in the millions). Convincing them of the Oracle's power would be quite difficult though.

>>>> **u/None** [+1]  (a day later)
>>>> 
>>>> Fair enough. If I could partner with someone much richer than me, I could give them a chance to double their money (say even bet of several million dollars), and they would give me a cut (which would still be in the millions). Convincing them of the Oracle's power would be quite difficult though.

> **u/ArgentStonecutter** [+1]  *Emergency Mustelid Hologram* (4 minutes later)
> 
> Munchkinry is kind of the point of the Oracle machine.

>> **u/None** [+3]  (27 minutes later)
>> 
>> Yes. How would you munchkin this set up. Basically, how much utility can you extract out of a yes or no question?

>>> **u/ArgentStonecutter** [+3]  *Emergency Mustelid Hologram* (36 minutes later)
>>> 
>>> Referring to:
>>> 
>>> > author added several extra patches to prevent certain kinds of munchkinry

> **u/None** [+1]  (10 hours later)
> 
> [deleted]

>> **u/causalchain** [+2]  (18 hours later)
>> 
>> I would add a patch: The oracle can only give what the answer to xyz would have been if the oracle did not exist to influence the world. This changes the problem a bit, but it naturally prevents truly random events (eg. gambling) or self-contradictions like you described. I found this patch in one of the biweekly challenge responses.

>> **u/None** [+1]  (23 hours later)
>> 
>> This assumes that you can contradict the Oracle's predictions. By nature of the experiment, if the Oracle says "yes" to "would I live to see ten more years?" you cannot kill yourself, and neither can anything else until those ten years are up.   
>> 
>> Self fulfilling prophecies do not prevent the Oracle from existing.

>>> **u/None** [+1]  (a day later)
>>> 
>>> [deleted]

>>>> **u/Gurkenglas** [+1]  (a day later)
>>>> 
>>>> If the enforcing mechanism is that events that would lead to a contradiction become less likely, we have an outcome pump on our hands.

>>>> **u/None** [+1]  (a day later)
>>>> 
>>>> Several, but that's beside the point. If the Oracle was given to be infallible in their predictions, then those predictions cannot be violated no matter agents' intentions to the contrary.

> **u/Gurkenglas** [+1]  (14 hours later)
> 
> We can actually get a little more than one bit out of the question: Ask something that is true, false or has no truth value. Also there's the obvious exploit if questions with no truth value let you ask an extra question.

>> **u/None** [+1]  (22 hours later)
>> 
>> Well asking invalid questions results in the Oracle wiping out humanity (I'll add it to the OP).

> **u/Cariyaga** [+1]  *Kyubey did nothing wrong* (2 days later)
> 
> I'd come to r/rational and ask people here what they'd do, naturally.

> **u/None** [+1]  (2 days later)
> 
> (1,a): Will my preferences be served overall by attempting to kill myself at the next convenient and reliable opportunity I recognize?

> **u/GopherAtl** [-2]  (an hour later)
> 
> not got a question to do it off the top of my head, but I would probably make it my priority to come up with some question with the best likelihood of breaking the damned thing. Why? See all other answers. Such a device is far more likely to be abused in ways that make the world worse for the majority, not better.

---

