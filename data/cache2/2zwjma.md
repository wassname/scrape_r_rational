## I am a web developer - what website/webapp could I build for this community?

* Author: u/raymestalez *
* URL: https://www.reddit.com/r/rational/comments/2zwjma/i_am_a_web_developer_what_websitewebapp_could_i/
* Score: 17

* Created: 2015-03-22T14:04:31

### Post:

Hey everyone!

I'm learning web development and getting pretty competent at it, and as one of my projects I would like to build something for this community, because I think it would be cool and fun.

So I'm wondering - is there any website/webapp that you would like to exist? Something that could be useful for rationalist readers or writers? Or maybe you have some problem that could be solvable with an app? If anyone has any cool ideas that you want me to build - please share =)

P.S.

If anyone offers some cool idea that I will end up building - I will pay a lot of attention to your suggestions and build features that you want to be there, so you essentially can get a custom-built, free, open-source app for yourself that does whatever you want =)

### Comments:

> **u/alexanderwales** [+26]  *Time flies like an arrow**
> 
> This is sort of pie-in-the-sky, but what I've really been wanting for a long time is an anachronism checker.
> Here's my basic use case:
> 1. User enters in a chunk of text (likely a chapter of 5k-10k words)
> 2. User enters a year (for example, "1900")
> 3. User clicks "Check me!"
> 4. Program highlights suspect words, phrases, etc.
> How this would work on the backend is that it would interface with something like [Google n-gram viewer](https://books.google.com/ngrams) or [Microsoft N-gram Service](http://weblm.research.microsoft.com/), run a check against every unigram, bigram, trigram, etc. to find its frequency in that year, then compare that against its frequency in the current year. If a certain threshold is exceeded, the n-gram is highlighted.
> So in our use-case example, the phrase "Albert Einstein" would be highlighted if you selected the year "1900" because Einstein was a complete unknown then.
> As a bonus, it's a very short step from doing *that* to having a webapp that can help highlight Americanisms in works which are set in British worlds.
> (There are a few ways to do things like this - mostly hacking spellcheck libraries - but all of them need setup and manual processes that are a pain in the ass.)
> 

>> **u/callmebrotherg** [+6]  *now posting as /u/callmesalticidae**
>> 
>> That would be The Best Thing Ever. 
>> Actually, "Best Thing Ever" would be that, plus the program suggests alternatives.
>> 

>> **u/ulyssessword** [+6] *
>> 
>> Also, [specific people](http://maryrobinettekowal.com/journal/how-i-beat-pat-rothfuss-at-being-pat-rothfuss/).
>> 

>>> **u/alexanderwales** [+6]  *Time flies like an arrow**
>>> 
>>> Mary Robinette Kowal was actually how I was first introduced to the concept of automated anachronism checking. She [scraped a list of all the words in Austen's novels](http://maryrobinettekowal.com/journal/the-jane-austen-word-list/), then fed that into her text editor as a spellcheck dictionary, which then highlighted [words that Austen didn't use](http://maryrobinettekowal.com/journal/words-i-couldnt-use-in-glamour-in-glass/). But this method is sort of clunky, and not easy to generalize.
>>> 

>>>> **u/MaryRobinette** [+4] *
>>>> 
>>>> Good lord. If you actually make such a thing, please let me know.
>>>> 

>> **u/brandalizing** [+3]  *Reserve Pigeon Army**
>> 
>> This would be phenomenally useful. A huge help and an incredible time saver. Also, accuracy.
>> 

>> **u/None** [+1] *
>> 
>> [deleted]
>> 

>>> **u/alexanderwales** [+1]  *Time flies like an arrow**
>>> 
>>> If you do, let me know!
>>> 

>>>> **u/None** [+1] *
>>>> 
>>>> [deleted]
>>>> 

>>>>> **u/alexanderwales** [+3]  *Time flies like an arrow**
>>>>> 
>>>>> An n-gram can be a unigram (one word), bigram (two words), trigram (three words), etc.
>>>>> "The" is a unigram. When you see it at 10%, that percent is the occurrence as a percent of *all unigrams*. So if the graph shows "the" at 10% in 1990, that means that if you were to slice every book on record (*edit: for 1990*) into unigrams, and put those unigrams in a hat, your odds of drawing the word "the" from the hat would be 10%. If you added together the percents for *all unigrams*, you would have 100%.
>>>>> Same goes for bigrams. If you divide up the entire corpus into bigrams, how many of those are "Albert Einstein" or "loosey goosey" or "wild card"? (For an example of how this works, the sentence "Albert Einstein was smart" would get divided into three bigrams: "Albert Einstein", "Einstein was", "was smart")
>>>>> This tends to be a bit better than just counting whether an indexed book has that word, because otherwise an entire book about Einstein would be counted the same as a single reference. Given the sheer size of the corpus, mostly you get smoothish lines.
>>>>> [Check out their About page for more information.](https://books.google.com/ngrams/info)
>>>>> 

>>>>>> **u/None** [+1] *
>>>>>> 
>>>>>> [deleted]
>>>>>> 

>> **u/RMcD94** [+0] *
>> 
>> Wouldn't it be easier to use some sort of captcha like service (as the backend); I feel like coding that would be a nightmare since even Albert Einstein was still around then you'd have to start doing percentage or something weird like that.
>> 

>>> **u/alexanderwales** [+3]  *Time flies like an arrow**
>>> 
>>> Google Ngram viewer already outputs that ngram as percent of the corpus. I'm not really clear on what you mean by a captcha-like service, but the actual logic for evaluating ngrams shouldn't be too much more difficult than:
>>>     percentChange = ngramTodayValue / ngramPastValue
>>>     if (percentChange > threshold)
>>>         flag
>>> The hard part is getting those values into the system - the evaluation shouldn't be terribly problematic.
>>> 

> **u/paladinneph** [+11] *
> 
> first let me describe a "real life action tracking" system. this system allows the user to create one-time or time-recurring goals, or constantly on habits. when users notice they are doing a habit, or complete a goal, they manually tell the system.
> ok, now take literally any easily-copied free-to-play web game designed to get you addicted to it, then get you needing to pay for premium currency. (candy crush, anyone?)
> now, instead of charging for premium currency, reward or deduct it for actions via the tracking system already described. you just built a powerful self-guided training tool.
> to my knowledge, the only thing that comes close to this is habitrpg, but it has issues which make it less effective than it could be. for example, it's also free-to-play monetized, which lets you pay real money to bypass having to complete goals, which is a bad thing to train into people, and hurts its training effectiveness (do you want your users to be addicted to completing goals, or paying you?)
> 

> **u/callmebrotherg** [+4]  *now posting as /u/callmesalticidae**
> 
> Hm. If you know who set up the Rational Reads website, perhaps you get add the ability to edit entries after they've been entered. This'd be especially useful for editing tags like "dead fic" or "updating slowly." 
> http://rationalreads.com/#/
> 

>> **u/mns2** [+5] *
>> 
>> The Rational Reads Github [page](https://github.com/Amit-P-Amin/RationalReads), for those looking to add to it or see its progress.
>> 

>>> **u/callmebrotherg** [+3]  *now posting as /u/callmesalticidae**
>>> 
>>> Ooh! Thank you. 
>>> I didn't know that this existed. Thank you.
>>> 

>> **u/None** [+2] *
>> 
>> [deleted]
>> 

>>> **u/callmebrotherg** [+1]  *now posting as /u/callmesalticidae**
>>> 
>>> Ah. Thank you for letting me know that.
>>> 

> **u/traverseda** [+3]  *With dread but cautious optimism**
> 
> Out of curiosity, what tools do you use?
> 

>> **u/raymestalez** [+2] *
>> 
>> Django, Node.js, MongoDB, Express.js, Ember,  MongoDB, EaselJS, Bootstrap.
>> Digital Ocean for hosting.
>> 

>>> **u/traverseda** [+1]  *With dread but cautious optimism**
>>> 
>>> How are you finding node? I'm generally a lot less heavy on the front end JS type stuff, so I'm interested.
>>> 

---

