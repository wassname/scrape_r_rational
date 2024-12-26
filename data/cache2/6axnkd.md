## [RT] [HSF] Programmer at Large, Chapter 11: Does that work?

* Author: u/DRMacIver *
* URL: http://www.drmaciver.com/2017/05/programmer-at-large-does-that-work/
* Score: 31

* Created: 2017-05-13T12:48:27

### Post:

[Link to content](http://www.drmaciver.com/2017/05/programmer-at-large-does-that-work/)

### Comments:

> **u/arenavanera** [+8]  (13 hours later)
> 
> I like this world a lot, and I'm enjoying the small slice-of-life vignettes, but after 11 chapters I'm starting to get a little antsy for conflict.  I'm hoping that either Kimiko's non-centrality or the game theory simulations turn into larger problems soonish.

>> **u/DRMacIver** [+8]  (19 hours later)
>> 
>> We'll explore the problems, but it's mostly going to continue to be low-conflict slice of life, sorry.

> **u/failed_novelty** [+7]  (7 hours later)
> 
> I'm very curious about what their 'modern' programming languages look like.
> 
> Obviously, they've grown and changed as time went on, and they have techniques (and artificial aides) we don't have presently.
> 
> But it really seems like 90% of their job is just thinking, which seems to be a pretty sweet deal if you can get it.

>> **u/DRMacIver** [+7]  (19 hours later)
>> 
>> > I'm very curious about what their 'modern' programming languages look like.
>> 
>> I'm kinda leaving it deliberately underspecified because I don't feel competent to predict the evolution of programming languages accurately beyond the very near term. Roughly the idea in my head (which should be considered more "author headcanon" than canon) is that rather than having a small set of languages, they have a whole "tree" of languages which start from simple cores and compile down to the next level, with an awful lot of formal verification and analysis happening at each translation level, and an awful lot of focus on interoperability standards.
>> 
>> It would be absolutely maddening to work with unassisted, but fortunately they don't ever work with it unassisted.
>> 
>> > But it really seems like 90% of their job is just thinking, which seems to be a pretty sweet deal if you can get it.
>> 
>> This too can be yours for the low low price of 10,000 years of toolchain development. ;-)

>>> **u/selementar** [+2]  (20 hours later)
>>> 
>>> > absolutely maddening to work with unassisted, but fortunately they don't ever work with it unassisted
>>> 
>>> Curious case about the languages available to us:
>>> 
>>> Lots of work is done in C transparently, i.e. one *almost* never has to go to the level it compiles into (machine codes, represented as assembly code). Then there're interpreted languages / VMs, and one almost never has to go to the C/CPP-representation under them. And recently some made translated languages on top of both ([1](http://cython.org/)) ([2](http://coffeescript.org/)), but didn't entirely manage to organize toolsets for the transparency, i.e. if something goes slightly wrong, there is still a need to go into the underlying representation.
>>> 
>>> The lesson is here is not clear, but it slightly suggests that making a translated language is cheap, but making a toolset to avoid dealing with stuff it is translated into is hard and expensive.
>>> 
>>> And then there's the point of actually *spreading the learning* of a language, and of how best to use it; a notable example in scripted languages is perl as compared to python: in a way, perl could be used about as conveniently as python is (with a little less sugar), but it did not nudge toward those practices, and lots of perl code thus became write-only code.

>>>> **u/Jello_Raptor** [+2]  *The Last Tool User* (9 days later)
>>>> 
>>>> The issue here is mostly precision of semantics and correctness of conversion. Many languages, especially older ones, don't have a precise formal semantics that tools can work with, or use system quirks that are incredibly difficult to model. Even then we're seeing some progress with formally verified compilers and the like. 
>>>> 
>>>> If you have correctness, then the problem becomes performance, and things like linear type systems can help with those when they start becoming more prevalent.

> **u/nicholaslaux** [+6]  (3 hours later)
> 
> Why are PTYs a memetics hazard? Just because explaining them take a lot of explanation time for little to no benefit?

>> **u/sparr** [+6]  (5 hours later)
>> 
>> I'm guessing this is related to tvtropes/Wikipedia tab explosion.

>>> **u/gryfft** [+14]  (6 hours later)
>>> 
>>> My guess is this is it, since learning that PTY stands for "pseudoteletype" begs the question "what is a teletype" and you pretty much inevitably wind up learning the history of early time-sharing systems, the rise of glass TTYs, the history of terminal emulation and the properties of PTY devices as they are exposed through and used by POSIX-compliant systems ("What's POSIX?" asks Arthur and the can of worms goes on.)
>>> It's all interesting history and useful for modern programmers using POSIX systems, but would probably eat up the rest of Arthur's afternoon without getting them closer to solving their problem.

>>>> **u/PeridexisErrant** [+3]  *put aside fear for courage, and death for life* (16 hours later)
>>>> 
>>>> > modern programmers using POSIX systems
>>>> 
>>>> The juxtaposition of *modern* and *POSIX* would probably eat the reminder of Arthur's voyage, never mind an afternoon.

>>>>> **u/selementar** [+3]  (20 hours later)
>>>>> 
>>>>> Hey, the standards are still useful! For example, there're a few reasons some distros [switched **from** `bash` as the default /bin/sh](https://wiki.ubuntu.com/DashAsBinSh) to an "arbitrary fast *POSIX-compliant shell*".
>>>>> 
>>>>> ...
>>>>> 
>>>>> Sorry for the formatting overload.

>>>>>> **u/PeridexisErrant** [+3]  *put aside fear for courage, and death for life* (21 hours later)
>>>>>> 
>>>>>> For *me*, yes.  For *Arthur*... maybe not.

>>>>>>> **u/gryfft** [+3]  (a day later)
>>>>>>> 
>>>>>>> Which is why I stipulated "modern," which I intended to mean the 21st century (that was probably unclear.)

>>>>>> **u/sparr** [+2]  (2 days later)
>>>>>> 
>>>>>> I was *so happy* on so many levels when Ubuntu switched to dash. The number of bashisms causing breakages in packages that needed to be fixed were a BONUS, not a cost.

>>> **u/nerdguy1138** [+3]  *GNU Terry Pratchett* (6 hours later)
>>> 
>>> It's a really good idea to warn about the possible wiki-walk beforehand!

> **u/Gurkenglas** [+7]  (2 hours later)
> 
> It's unlikely that a random one of 114 interesting things will be the culprit, so he should look at others before expending political capital on checking this one.

>> **u/over_who** [+8]  *Aleph you are going to die* (2 hours later)
>> 
>> > It's unlikely that a random one of 114 interesting things will be the culprit, so *they* should look at others before expending political capital on checking this one

> **u/MoralRelativity** [+2]  (18 hours later)
> 
> Looking forward to learning Go#.

>> **u/monkyyy0** [+2]  (3 days later)
>> 
>> Its go with all the bullshit that c# has

> **u/BadGoyWithAGun** [+2]  (10 hours later)
> 
> Be honest, how much of this series is just self-insert of the main character by having him scoff at programming practices you have an aversion towards?
> 
> "everyone is autistic and a gendersnowflake" != "rational fiction"

>> **u/heiligeEzel** [+1]  (3 days later)
>> 
>> Errrr... Only the main character is autistic -- the others are significantly more well-adjusted.
>> 
>> As for the gendersnowflake... it seems like a pretty natural progression of culture that we just collectively stop caring about gender. Once you drop all the biases that people of a certain gender are likely to have certain characteristics, what's the point of keeping the pronouns?

>> **u/sephirothrr** [+1]  (14 hours later)
>> 
>> What, you didn't enjoy the author shilling his own products that apparently will go on to have ~150 years of popularity?

> **u/selementar** [+1]  (20 hours later)
> 
> "Temperature Control Feedback Regulation" ... ^(something)-sharp ... openssh!? Clearly missing a "trash"-like tag. On the other hand, "Fragility: High" is not surprising.
> 
> But a general practice for such code is to rewrite it.

>> **u/GopherAtl** [+1]  (10 days later)
>> 
>> > But a general practice for such code is to rewrite it.
>> 
>> eeh. In a contemporary software *development* shop, yes, absolutely. The protag is not,primarily, a software developer, though; they are more of a software maintenance engineer. 
>> 
>> Even in contemporary reality, programmers who maintain legacy enterprise software systems, systems that major corporations depend on, this "if it ain't broke don't fix it, in fact, don't even look at it funny" rule is often effectively law. And that's just when large amounts of money are at stake - when people's lives are at stake, you don't go tearing down essential bits of code that've worked reliably for decades just because they're ugly.

---

