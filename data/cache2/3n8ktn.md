## [D] How to describe magic as a programming language?

* Author: u/alexanderwales  *Time flies like an arrow**
* URL: https://www.reddit.com/r/rational/comments/3n8ktn/d_how_to_describe_magic_as_a_programming_language/
* Score: 29

* Created: 2015-10-02T15:43:40

### Post:

I've been looking at some of my writing projects lately, thinking about actually finishing them, and there are three that have magic systems that work in pretty similar ways; they all have analogs to computer programming (though they're meant to explore different aspects).

My problem is how to get across the computer programming concepts without having to have a chapter of dense exposition, or several chapters of fluffier exposition.

I think "spells as function calls" is easy enough, to the point where I don't think it adds in that much to a story; knowing that "*Abracadabra!*" is actually `Abracadabra()` doesn't actually change the story, not unless you're going to figure out something clever with that knowledge. Same with having a True Name actually be a GUID.

But I don't know how to easily get across more complex concepts, like ... let's say that we have `Abracadabra()`, but there are variants where you can add on certain parameters. That's something that you can actually do something clever with, depending on what those parameters are. If "*Abracadabra!*" is `ThrowFireball()`, then "*Abracadabra-mancychwynhafalsefyllfa defnyddiwracunfilltiriuncyfeiriad!*" could be `ThrowFireball(new Point(User.Position+5280), DirectionEnum.TrueNorth)` which would create the fireball a mile away instead of right next to the caster.

A large part of my difficulty here is that I don't know how much the average person with no knowledge of computer programming would be able to make the connections. It's natural to me to think of specifying a vector on a magic missile. But I don't know how naturally this comes to someone without the background.

Does anyone have some advice for me?

Edit: If you want to see a first draft of one of the three, [that's here](https://www.reddit.com/r/worldbuilding/comments/186l1y/a_crud_magic_system_v2/). But I'm more concerned with clever ways of giving exposition in-story than how to shape actual mechanics.

### Comments:

> **u/None** [+15] *
> 
> [deleted]
> 

>> **u/alexanderwales** [+2]  *Time flies like an arrow**
>> 
>> One of the things I really love about your fiction is that the story often seems to be saying to the reader, "Hey, you're smart, figure it out". I suppose I'll think more about omitting exposition or making the internals of the magic system relevant.
>> 

>> **u/notmy2ndopinion** [+2]  *Concent of Saunt Edhar**
>> 
>> I don't know very much about programming, but I enjoyed reading the comments and discussion in Ra about how programmers were figuring out the magical syntax.
>> 

> **u/EliezerYudkowsky** [+25]  *Godric Gryffindor**
> 
> I feel like a core problem of magic-as-programming is that it feels impossible to set real limits or make the effects of those laws predictable to the reader.  This is true of any mechanical theory of magic - any attempt to postulate an underlying set of mechanical laws by which magical forces interact.  They all seem to run into the same problem in my mind, namely that it would take an *enormous* amount of work to be at all realistic about what sort of spells could or would be built out of low-level lawful blocks.
> That's why Brian Sanderson has exactly 14(?) kinds of magic you can use in Mistborn, each operating on clearly defined laws and most of them not industrially useful.  Rather than, say, Sanderson giving a set of cellular-automaton rules you can use to craft spells.  In theory, the latter system could be simpler and more lawful.  In practice it's impossible for any of us to imagine what even a small society of magical researchers working for a few decades, would be able to craft using a magical cellular automaton.  All we can do on our own is the first month of one person's research inside that magical system.  So if the author alleges to you that magic has a programming language or any other mechanical set of interactions at the bottom, in literary practice you're left with a batch of spells that the author has just ruled into existence.  There's no license for the reader to assume that anything they can think of doing with the automaton rules will thereby be doable in the story.
> This is why Sam Hughes's Ra never spells out the programming language.  It's why Rick Cook's Wizardry series never spells out the programming language.  One author can't actually go from the low level to the high level - all they can do are tell you, "Here are the final spells."  Does a magical researcher discover a way of combining the features of two spells?  That insight had better not be a critical plot puzzle, because there was no way for the reader to guess that would be allowed.
> Mistborn's magic is more suited to Fair Play Insight puzzles, because we know the characters aren't going to invent a new metal that acts like a combination of Pewter and Iron or whatever.  A smart character can burn both Iron and Pewter at the same time and use a clever combination of effects, but the library of spell effects is strictly limited and packaged into solid blocks, thus presenting a fair puzzle in terms of what you can do by combining those effects.
> One of the fictional setups I'm considering has magical races where each magical species can produce a small set of effects operating according to strict explicit rules.  In this setup, there are no half-breeds.  There are no ways to produce new magical species.  There's a finite list of magical effects, and a human reader can know all of the rules governing them.  We can call this "Mistbornlike magic."  It doesn't require that magic be mechanical or mundane in its effects - some of the magic can revolve around thought and emotion.  What it requires is that the library of magical effects be short enough for humans to read.
> 

>> **u/eaglejarl** [+9] *
>> 
>> I can imagine a series where magic *does* run on a cellular automaton or other formalism, but it's the beginning of the Enlightenment and the scientific method has just been invented. Until now, sorcerors have used magic by sheer trial and error, and now they are actually getting to understand the structure. The main characters would be in the position of doing all that research from the ground up; given a short time frame on the book, this could fit within the author's ability to imagine. 
>> Ideally this would be handled something like the *1632* universe, where Flint set up the rules and then opened it to other authors so that the history would feel real. He keeps control over the broad strokes of things (e.g. there's a master list of uptimers and you're not allowed to make up more), but individual authors can go off in their own direction.
>> 

>> **u/alexanderwales** [+16]  *Time flies like an arrow**
>> 
>> While I generally agree, there are a couple of ways around it.
>> 1. Get a bunch of people on the internet to simulate your small group of researchers.
>> 2. Limit the population of people who can do magic so that there aren't many magical researchers.
>> 3. Set the work of fiction prior to institutionalized research.
>> 4. Set the work of fiction during the era of research.
>> 5. Limit magic so that research is dangerous.
>> 6. Make magic so good that there's not much incentive to expand horizons.
>> 7. Make research difficult enough that progress would naturally be slow.
>> Then when someone thinks, "Oh, logically they would be able to do `x`!", either it's plausible that a small group of people would have missed it, they had other things they were trying, it would be dangerous, or it requires systems of thought that they don't have access to.
>> (Of the three stories I have in draft mode right now, *Robot, Vampire, Wizard* uses 2,4,6, *The Four Methods* uses 2,3,5,6, and *The Gift and the Burden* uses 3,4,7.)
>> 

>>> **u/MugaSofer** [+8] *
>>> 
>>> > Set the work of fiction prior to institutionalized research.
>>> Don't underestimate the power of pre-scientific societies slowly advancing their tech!
>>> I suspect the only reason we're not more impressed with the kind of stuff pre-scientific cultures in our world did with our "basic rules" is that it's all so familiar; and even then, you get stuff like the Pyramids that freak moderns out. The ancient world went through countless iterations of various kinds of arms race to bring you "basic" medieval-style tech, and it'd be odd if they hadn't done the same with magic.
>>> Assuming magic is old, of course.
>>> 

>>> **u/Salaris** [+7]  *Dominion Sorcerer**
>>> 
>>> I use a lot of similar restrictions for my one of my own sort of programmingish magic systems.
>>> 1. Resource scarcity (e.g. spells requiring material components, power sources, etc). If different types of spells require different components this makes the restriction even more significant.
>>> 2. Parameters that restrict the degree to which spells can be customized. (E.g. you can only combine your fireball with two other parameters, only one of which can be a range parameter, etc.)
>>> 3. Cultural values that make specific types of magic taboo or illegal.
>>> 4. Cultural values that discourage the spread of information.
>>> etc.
>>> 

>> **u/Renegade_Scholar** [+1] *
>> 
>> The way I described it is like running several programs on a laptop on battery power. Yeah your spells will be powerful but the battery is going to run out
>> 

> **u/notgreat** [+9] *
> 
> Seems to me that the system you've described is less computer programming and more just stacking metamagic modifiers on top of the base fireball spell. Take fireball and add a new position and velocity. Or apply maximized empowered time-dilated to the fireball.
> 

>> **u/alexanderwales** [+10]  *Time flies like an arrow**
>> 
>> Well, the *other* part of the problem is figuring out which features to include in a hypothetical programming magic system, which I think depends on what sort of story you want. Conditionals? Probably yes. Math operations? Also probably yes. Loops? Maybe, but seems broken if you can do `while(true){ThrowFireball()}` so would need some limits. User defined data types? Interfaces? Global variables?
>> 

>>> **u/ArgentStonecutter** [+8]  *Emergency Mustelid Hologram**
>>> 
>>> Wiz Zumwalt demonstrates the problems with having a while(true){...} in a spell in [Chapter 9](http://wayback.archive.org/web/20100102041439/http://baen.com/library/0671878468/0671878468.htm).
>>> 

>>> **u/gbear605** [+8]  *history’s greatest story**
>>> 
>>> > while(true){ThrowFireball()}
>>> As long as ThrowFireball() takes some kind of mana from the "programmer," there's no problem with this: the person dies.
>>> 

>>>> **u/alexanderwales** [+4]  *Time flies like an arrow**
>>>> 
>>>> Limitations on magic systems are one of those things that you can calibrate in a lot of different ways. Mana is one of the most well-worn. The system I'm using for *The Four Methods* setting (described in a link in the OP) uses something similar; depending on which school of magic you're using, you're getting poisoned, getting weakened, losing memories, or going insane. That's standard "magic has a cost" stuff.
>>>> But you can also add in things like "there's an `x` per minute chance for an IllegalThreadStateException to be thrown, causing a fatal caster error", or something like that.
>>>> 

>>>>> **u/Anderkent** [+6] *
>>>>> 
>>>>> Easily handled! :P
>>>>>     while (true)
>>>>>       try
>>>>>         throwFireball()
>>>>>       catch Throwable
>>>>>         continue
>>>>> 

>>>>> **u/gbear605** [+3]  *history’s greatest story**
>>>>> 
>>>>> I was referring to mana in the broadest sense of something that is taken from the caster, whether that is good health or sanity, or life force, or what not. There are lots of ways to do it.
>>>>> 

>>> **u/rineSample** [+7] *
>>> 
>>> If you found a way to quantify physical pain, it would be *exceedingly* easy to make a "return all damage upon the attacker tenfold" spell.
>>> 

>>> **u/MugaSofer** [+5] *
>>> 
>>> > Loops? Maybe, but seems broken if you can do while(true){ThrowFireball()} so would need some limits.
>>> If spirits become bored easily, that would be a good excuse for memory and run-time limitations on spells. Of course, then you lose the potential for *Sorcerer's Apprentice*-style runaway spell accidents ...
>>> 

>>> **u/Anderkent** [+5] *
>>> 
>>> There's a very great chance that any explicit magic system will be turing complete (see www.gwern.net/Turing-complete for examples of unintended turing-completedness), so even if there's no 'explicit' loop mechanism you can implement your own.
>>> 

>>> **u/FeepingCreature** [+3]  *GCV Literally The Entire Culture**
>>> 
>>> Power limits and efficiency loss makes it usually the right approach to just cast the biggest fireball you can.
>>> Global variables don't work because FTL. What you want is more signal-based, maybe asynchronous programming.
>>> 

>>> **u/AugSphere** [+2]  *Dark Lord of Corruption**
>>> 
>>> Ditch side effects?
>>> 

> **u/ArgentStonecutter** [+10]  *Emergency Mustelid Hologram**
> 
> Following up on my previous post, you could actually make magic a programming language by writing it in Forth. Just make up some gutteral aliases for if while then begin end until else etc...
> badguy locate self locate vector-difference normalize half-power fireball activate
> 

>> **u/alexanderwales** [+4]  *Time flies like an arrow**
>> 
>> I do really like the idea of seemingly-incomprehensible strings of syllables that a diligent reader could decode into a description of what the spell is doing. ("*Abracadabra-mancychwynhafalsefyllfadefnyddiwracunfilltiriuncyfeiriad!*" is just *Abracadabra* with some instructions translated to Welsh and appended to the end.)
>> 

>>> **u/None** [+7] *
>>> 
>>> Point-free style in Haskell would work well for this also.
>>> 

>>>> **u/rhaps0dy4** [+2] *
>>>> 
>>>> I do not see how https://en.wikipedia.org/wiki/Tacit_programming would make this work well. Not defining the function's arguments doesn't really make a better syllable-pronunciation? Since you're only invoking functions anyways.
>>>> I side with ArgentStonecutter, a stack-based low-level language would be rad for that. Alternatively, I'm not sure of the technical merits of Urbit http://urbit.org/preview/~2015.9.25/materials/whitepaper but they do sure have a concise way to pronounce their language.
>>>> 

>>>>> **u/ArgentStonecutter** [+1]  *Emergency Mustelid Hologram**
>>>>> 
>>>>> To write a magical fantasy novel based on Urbit you need to first be Phillip K. Dick.
>>>>> For two completely unrelated reasons.
>>>>> 

>>> **u/KarlitoHomes** [+5] *
>>> 
>>> >I do really like the idea of seemingly-incomprehensible strings of syllables that a diligent reader could decode into a description of what the spell is doing.
>>> [Ra](http://qntm.org/ra) has something similar to this.
>>> 

>>>> **u/Chronophilia** [+2]  *sci-fi ≠ futurology**
>>>> 
>>>> Really? A few of the words have given meanings, but I thought most of the language was gibberish.
>>>> 

>>>>> **u/alexanderwales** [+8]  *Time flies like an arrow**
>>>>> 
>>>>> [See this appendix](http://qntm.org/spells). I think a lot of it can be decoded, but there are surprisingly few examples within the text.
>>>>> 

>>> **u/ArgentStonecutter** [+2]  *Emergency Mustelid Hologram**
>>> 
>>> So prepend it instead. \^\^
>>> 

>>> **u/ArgentStonecutter** [+2]  *Emergency Mustelid Hologram**
>>> 
>>> Third option that came to me re-reading that Forth fragment. Base it on an Linden Scripting Language with extra primitives for effects that Linden Lab would consider dangerous. Don't actually reveal this in the story of course.
>>> Then you can actually test parts of spells out in Second Life. Just have it do llSay(0, llObjectName(spellTarget)+" is turned into a cat") instead of calling llPolymorph(spellTarget, POLYMORPH_TYPE_CAT).
>>> The weird not-quite-list-oriented not-quite JavaScript syntax and semantics, and the 16k limit of classical LSO, are actually good ways to limit spell power.
>>> 

> **u/DCarrier** [+8] *
> 
> I think you should show them actually writing a spell. They might write out something like "ThrowFireball(new Point(User.Position+5280), DirectionEnum.TrueNorth)", then assemble it to "Abracadabra-mancychwynhafalsefyllfa defnyddiwracunfilltiriuncyfeiriad!", and then take that and make a name for it if they want to cast it multiple times.
> 

>> **u/alexanderwales** [+6]  *Time flies like an arrow**
>> 
>> That's a good idea. From a narrative-building perspective, I could do an [Action Prologue](http://tvtropes.org/pmwiki/pmwiki.php/Main/ActionPrologue) with someone having to hastily construct a spell for some specific purpose which coincidentally gives the bare bones of exposition on how the magic works. (Though I've seen better authors than I am have trouble doing this right, so maybe not.)
>> 

> **u/ArgentStonecutter** [+7]  *Emergency Mustelid Hologram**
> 
> Rick Cook did a great job of this in [The Wizardry Compiled](http://www.baenebooks.com/showproduct.aspx?ProductID=1632&SEName=the-wizardry-compiled).
> This is a pretty good read on how a programmer could munchkin the hell out of a magic system. The whole series is worth reading. Each book builds well on the previous ones, the fantasy world has a credible economy and politics, and fucking up the magical economy has real consequences... and not just on the humans.
> 

>> **u/DCarrier** [+3] *
>> 
>> I found links to the first two books on the internet archive ([here](http://wayback.archive.org/web/20100102041439/http://baen.com/library/0671878468/0671878468.htm) and [here](http://wayback.archive.org/web/20100102041341/http://baen.com/library/0671698567/0671698567.htm)), but I don't know how to get the rest of the series. Do I have to buy it or something?
>> The main character didn't start munchkining the magic system until the end of the first book, so I thought most of it was pretty boring.
>> 

>>> **u/ArgentStonecutter** [+2]  *Emergency Mustelid Hologram**
>>> 
>>> Well, he starts hacking it in Chapter 9. Maybe 3/4 of the way in?
>>> http://www.baenebooks.com/p-470-wiz-combo-ii-cursed-and-consulted.aspx
>>> 

> **u/Farmerbob1** [+6]  *Level 1 author**
> 
> You can be very blunt about it and allow computers to be used to draft magic spells, like AutoCAD, complete with simulation software for testing.  Most people who will be interested in either science fiction or fantasy will understand the concept of using computers for design, and you can build from there.
> Speech therapy classes might be a strict requirement for magicians, for pronunciation reasons.  It may even be possible to identify a wizard by the manner of their speech.  If you startle someone and they all of a sudden speak far more clearly with no verbal faults, you might be about to get a magic missile where the sun doesn't shine.
> Going to the dentist would expose them to a great risk.  They would be unable to defend themselves with mushmouth if they accepted painkillers, or have a very strong likelihood of fumbling a verbal component due to swelling or pain if they declined painkillers.
> It would be conceivable for a wizard to learn something completely new by simply mispronouncing something, especially if MagiCAD was merely a tool.  After they clean their shorts post-mistake, the wizard adds the new concept to MagiCAD, and then starts experimenting with the simulator.
> Hrm.  That could lead to an interesting whodunnit mystery, with a murdered researcher plotline.
> 

> **u/LiteralHeadCannon** [+8] *
> 
> What level of language is someone using when they say "Abracadabra!" and a fireball comes out?
> Go a level lower than that.  There's got to be some kind of magical language someone used to program the universe to generate a fireball with a certain momentum when someone says "Abracadabra!" properly.  How does that language work?
> What's the lowest level?  What's the *physical* mechanism for magic, the equivalent of the science that makes computers run?
> 

>> **u/alexanderwales** [+5]  *Time flies like an arrow**
>> 
>> I don't tend to find lowest levels fun. You could do it all in assembly, or you could build the logic into the transistors yourself, but if you don't have to do that why would you want to? Efficiency, I guess?
>> I tend to find lowest levels even *less* fun in magic systems, both because there's hardly ever anything interesting there and because it takes away from the higher levels. A single deeper (but still somewhat abstract) level is my preference.
>> But at the very lowest levels, it's about as irrelevant to spellcasting as atomic physics is to warfare, until someone invents a nuke. And then your story is about nukes, which is fine if you want a story about nukes, but not great if you want it to be about anything else.
>> 

>>> **u/LiteralHeadCannon** [+5] *
>>> 
>>> I don't bring up the lower levels because I think they're inherently interesting.  I bring them up because I think they inherently create a higher understanding of what's actually happening on the higher levels.  If you forget that the lower levels exist, then your mental image of what's going on is pretty much never correct.
>>> 

> **u/MugaSofer** [+5] *
> 
> Several series - serieses? serii? - have magic-as-language; you describe the effect, and Magic obeys your instructions.
> Of course, the philosophy-of-language differs; Earthsea language is prescriptivist "true name" stuff, whereas Eragon magic can have multiple different spells from the word *fire* based on context and intent.
> So I'd do it like this:
> >*Magic is not a human!* Magic - spirits, runes, whatever - understands *only* what is explained to it! It will not understand from context! It will not understand what you *meant*! The great Mages of old have exhaustively defined various words, like "fire", for Magic. Some concepts have *never* been successfully defined!
> >In this class, we'll be creating a simple "fireball" spell. We use Maxwell's system of Co-ordinates to tell magic where to create the fire - a foot to the left and three in front of my heart. We then specify the amount of fire, and it's dimensions, according to the True Names of the numbers; and invoke it all with the Word "*fire*". Finally, we tie the spell to be invoked by a word and a gesture ...
> >Like so: *IFF-gesture1-THEN-create-elementFIRE-spec-input-hlfSbb-radius-qegbq-coord-vrjhjyrsj-atjanzana-ajnnarja-endspec-ENDIF*
> >The spell executes thus:
> >*snaps finger* FOOM
> >As you can see, the candle has been lit. Care must be taken to avoid specifying a flame of ten units rather than one or one-tenth of a unit, or mistakenly invoking the gesture of a spell - FOOM - you see? Now imagine if this were accidentally placed inside my head, or inside my hand ...
> And then just continue the story as normal, perhaps with the protagonists giving vaguely programmer-y partial explanations whenever they prepare their daily spells. I think reader will usually swallow a mentor or teacher giving a quick example, and you really just need a quick example of the spell "code" underlying a simple "program" and a hint that there's deeper "machine code" beneath.
> Oh, also, if I was a wizard I'd make the programming language at least somewhat like English. Even if I had to write a new compiler for it. It's just common sense.
> 

> **u/diraniola** [+4] *
> 
> You could have a way to set sort of 'hot keys' for individual spells, so if you didn't want to spend 2 minutes chanting to get a complex effect, instead you can meditate/study/write out the spell and key it to a shorter phoneme. Make your "Abracadabra-mancychwynhafalsefyllfa defnyddiwracunfilltiriuncyfeiriad!" and map it to "yn hyn llosgi."
> 

> **u/nicholaslaux** [+3] *
> 
> I like the concept of showing meditation or study of a spell or grimoire, and from there, you could show that the "abracadabra" is really just a mnemonic for that spell,  possibly even showing some sort of alias spell for "saving" a new one. 
> If you want to show rather than tell, perhaps an equivalent to shaping exercises from Mother of Learning that shows the underlying spell "language", or to allow the reader to discover on their own, have spells work like some German words, where the spell for fireball is shown at the same time or after showing the spells for start campfire, push object, and protect self from heat.
> 

> **u/None** [+3] *
> 
> [deleted]  
>  ^^^^^^^^^^^^^^^^0.3611 
>  > [What is this?](https://pastebin.com/64GuVi2F/99619)
> 

>> **u/alexanderwales** [+3]  *Time flies like an arrow**
>> 
>> > The thing is, I think the sexiness isn't in the fact that the wizard is using a programming language, but exactly what it means to be using a programming language at all.
>> Yup, this is something that I'm trying to keep in mind. It's the joy of going from a defined program with a bunch of built-in stuff and then cracking it open to change how it works internally. Or it's stitching two libraries together in order to get something novel up and running, like retooling that fireball into a flamethrower or an arc welder.
>> 

> **u/captainNematode** [+3] *
> 
> I haven't played them myself, but there are a few code-magic-spells video games around. For example, [Codespells](http://codespells.org/) just came out a few weeks ago, and [Codemancer](http://codemancergame.com/) is due out in a year. They strive to teach people who've never programmed how to code, so I reckon they'd be pretty broadly accessible. Their implementations might serve as inspiration.
> 

> **u/Transfuturist** [+2]  *Carthago delenda est.**
> 
> The Young Wizards series has both a very nice magic system and a nice way of describing it.
> 

> **u/cartazio** [+2] *
> 
> Look up linear types and other resource models.  Most programming has to manage algorithmic complexity vs usage of various resources that are constrained.  Like time , speed, memory, network speed.  Etc
> 

> **u/None** [+2] *
> 
> I am working on lambda calculus based magic system you can use that
> 

>> **u/TimTravel** [+1] *
>> 
>> Details?
>> 

>>> **u/None** [+1] *
>>> 
>>> I am still thinking it through.
>>> The idea is, there are magical "atoms" (the perfect name would be "monads", but that's already taken in fuctional programming), - those are a basic reality interaction in one space-point
>>> And then you create spells using 2 lambda-calculus operations (application and abstraction) and apply them to atoms to create spell themselves.
>>> Long time ago, you needed to recite the whole source code for the spell to work. Now all spells you create are stored in the repo. 
>>> When you create a spell, the code is stored somewhere and you get a name - convenient to pronounce string, which is a checksum of the code and is used to invoke it. 
>>> Also, there are pretty good standard library and development tools.
>>> To limit destruction potential, ancient mages have created sandbox - world-wide network of spells, which kill all the spells outside the allowed radius, refilling itself with their power.
>>> Yeah, and I thought of it before I read Rick Cook. (But after Yasinsky's "Nick" series with the same premise, Russian, unfortunately)
>>> 

> **u/zachary123212** [+2] *
> 
> Why stop at an imperatively defined magic system? I would love to see a declarative functional magic system implemented in some way. Magical monads for everyone!
> 

>> **u/TimTravel** [+2] *
>> 
>> Monads are pretty magical already... ;)
>> 

> **u/None** [+2] *
> 
> I've developed a magic system where the spell effects are defined by a phrase, which is a sequence of magical characters. Each consonant codes a linear combination of possible spell effects (heat/cold, electric charge, momentum change, psychic effects, etc etc), and each vowel is a scalar value. The end result is the linear combination of the spell effects multiplied by the scalars.
> This effect is loaded into the aether. Where, and how much, is decided by the wizard's pose. Put fingertips together and flap your elbows, and you'll be throwing iceballs or fireballs or whatever. Spread the fingertips and it'll be a blizzard or firestorm instead. 
> So, it's not programming, but it is a general system that builds spells from first principles. If you take careful notes and understand linear algebra, you'll be able to create any arbitrary effect combination, and then it's just a matter of developing a set of useful poses to get those effects to where you want it.
> [Link to MagicBuilding post about the system](https://redd.it/3j38ok).
> 

> **u/sir_pirriplin** [+2] *
> 
> >A large part of my difficulty here is that I don't know how much the average person with no knowledge of computer programming would be able to make the connections.
> Are you familiar with Homestuck?
> The protagonist is a kid who enjoys programming but is not very good at it. He has a magic item that is like a bag of holding that follows the rules of a stack data structure.
> Watching him experiment with his "stack modus captchalogue" allows the reader to understand the rules of that magic item without being burdened with lots of exposition and without having to know a lot about data structures.
> 

> **u/thedarkone47** [+2] *
> 
> see, "The Irregular at Magic High".
> 

> **u/Chronophilia** [+1]  *sci-fi ≠ futurology**
> 
> I thought the interactive fiction game [Suveh Nux](http://ifdb.tads.org/viewgame?id=xkai23ry99qdxce3) did this pretty well, without needing to mention any computer programming concepts (except for binary).
> 

> **u/None** [+1] *
> 
> [deleted]
> 

>> **u/aldonius** [+1] *
>> 
>> You're probably thinking of the [Wizardry series by Rick Cook](https://en.wikipedia.org/wiki/Rick_Cook#Wizardry_series); it's been mentioned elsewhere in the threads...
>> 

> **u/notmy2ndopinion** [+1]  *Concent of Saunt Edhar**
> 
> The easiest way to do this is to make it explicit and just state that the characters are partially aware that they are in a fantasy computer RPG -- so they have a passing familiarity with some programming, the same way that Order of the Stick characters are aware they are in a pen-and-paper RPG and know the rules of the base D&D 3.5 system.
> 

> **u/TimTravel** [+1] *
> 
> Make it mana / node-based. Nodes can transfer mana to other nodes or spend it themselves to have small effects. Individual node size is up to the author based on the setting. Make a small well-defined set of atomic commands nodes can carry out. Add a few basic computation-based commands, finite state per node, and then you've got a Turing machine cooking. You can do while(true) fireball(enemy); but it'll fizzle once the spell runs out of mana.
> Note it takes surprisingly little basic computational power to build a Turing machine, ignoring the difficulty of coming up with an infinite tape. I can give some suggestions / details if you want. I'm pretty good with theoretical compsci.
> 

> **u/Nepene** [+1] *
> 
> The levels of learning of a mage.
> The basic level is mastering the more simple commands- fireball, teleport, invisibility, fly, melt. These are stylistic links to more complicated spells that do something like specify a ball of plasma of a certain size to move from in front of your hand in the direction your index finger is pointing at 100 km/h. In computer terms, running programs. Some programs require greater resources, some less, and this is the level most stop at. When a reception waves her hand and says a few words and a large arrow points you in the right direction, this is an app user.
> The next level is use of variables. Perhaps while flying you want to go faster, or in another direction rather than wherever your index finger is pointing, or you want to fly whenever a fireball shoots at you. So you have to learn variables and types of variables. Many of the standard spells are set to accept certain variables. 
> So, you cast the trigger other spell fireball spell set with the boolean value of 1, then the flying spell and then a number (-400) and then when a fireball flies at you then you'll fly away from your index finger pointing direction at 400km/h.
> The next step is learning to use arrays and for if statements.
> So, your enemy is fleeing from your fireball at a huge speed. You need an array. You earlier cast a spell, located at distance, and melt. This located at distance has a table of different locations enemies can be at. It then detects them with a laser which reflects off them, and uses the array table to decide on what direction to fire the melt spell, a laser heating spell. 
> This spell has a for and an if spell in it. For a certain range of numbers it repeats the spell until a laser gets a result indicating an enemy. If it detects that sort of target it sets a boolean value of 1 in a value, and triggers the if spell and fires a laser to melt the target.
> Suppose you're a target. You need some way of responding. The next level is functions.
> You have a spell. This target is set to wait for a particular input, a laser above a certain amount of energy. If there is no laser the spell is set to loop. If a laser appears, it is set to trigger an invisibility spell. There are different invisibility spells for different wavelengths to defend the person.
> And so on.
> http://lifehacker.com/5744113/learn-to-code-the-full-beginners-guide
> I'd make spells and lessons centered around real beginner program guides.
> 

> **u/clawclawbite** [+1] *
> 
> One thing to hint at that, stylewise, is that you can format spells like code.
> So you actually cast Abracadabra(), or more likely Abracadabra (Ex Nilho) or possibly even
> >Abracadabra(Ex Nilho);
> And call off spells with whitespace, indents, and brackets.
> 

---

