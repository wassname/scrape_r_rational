## [META] Can the weekly discussion threads be automatically sorted by "new" instead of by "best"?

* Author: u/GaBeRockKing  *Horizon Breach: http://archiveofourown.org/works/6785857**
* URL: https://www.reddit.com/r/rational/comments/6jqdij/meta_can_the_weekly_discussion_threads_be/
* Score: 25

* Created: 2017-06-27T04:21:50

### Post:

Normally speaking, if you get to a discussion thread late, there's a disincentive to post top-level replies, since these posts would be sorted to the bottom of the thread. Meanwhile, there's no real need to have a default sort by "best" because the top level posts are typically just the starting points of discussions, instead of being innately useful in and of themselves.

This change would hopefully lead to more top-level replies, and thus to more discussion overall.

The change doesn't need to affect all weekly threads, and instead could be tested out on just one to see if there are any improvements in the quantity of discussion.

Automoderator scripting could be a bottleneck, but unfortunately I don't know enough about the topic.

### Comments:

> **u/alexanderwales** [+1]  *Time flies like an arrow* (10 hours later)
> 
> We can try it. I personally think that loses one of the primary benefits of reddit as opposed to other platforms; you get to see the best stuff first and then stop reading when quality dips. The code for getting Automod to do it, it is as follows (this is mostly for my benefit):
> 
>     author: Automoderator
>     title: ["[D] Friday Off-Topic Thread"]
>     set_suggested_sort: new
> 
>  A better solution might be to turn suggested sort to new at a certain point (e.g. number of comments, time passed), but Automod can't do that because it only looks at every post once.
> 
> **I will manually switch the Friday Off-Topic thread over to suggested sort: new this coming Friday** and we'll see whether it makes any difference in discussion, and how many people complain about it.
> 
> (We don't usually get more than 20 top level comments on any of our weekly threads, usually quite a bit less, so I am skeptical of any change in behavior, but we try things because we get new data.)

>> **u/GaBeRockKing** [+4]  *Horizon Breach: http://archiveofourown.org/works/6785857* (11 hours later)
>> 
>> Thank you!

> **u/gbear605** [+5]  *history’s greatest story* (9 minutes later)
> 
> I think that this sounds like a good change to encourage better commenting. In addition, we should test it as an experiment, if we think there's any chance of it being better.
> 
> Also, I know that there's a "contest" mode that puts them in a random order, so that might be better, though if I remember correctly, that also hides child comments, so that wouldn't be good.

> **u/Noumero** [+4]  *Self-Appointed Court Statistician* (4 hours later)
> 
> I agree, it would be helpful.
> 
> That said, I'm not sure if it's possible. Does reddit allow custom settings for threads out-of-the-box? As far as I could tell, moderators could only enable contest mode for individual threads, or change sorting order of comments for all threads on their subreddit, but not for individual threads.
> 
> Though I wouldn't mind if we switched onto sorting by old/new comments by default.
> 
> (Probably because I already set that as a preference for all of reddit, but nevermind that.)

>> **u/awesomeideas** [+5]  *Dai stiho, cousin.* (10 hours later)
>> 
>> It is possible since that's how the Culture War threads on /r/SlateStarCodex "work." I will leave it as an exercise to the reader to decide  whether or not this is actually helpful.

>>> **u/sneakpeekbot** [+1]  (10 hours later)
>>> 
>>> **Here's a sneak peek of [/r/slatestarcodex](https://np.reddit.com/r/slatestarcodex) using the [top posts](https://np.reddit.com/r/slatestarcodex/top/?sort=top&t=year) of the year!**
>>> 
>>> \#1: [You Are Still Crying Wolf](http://slatestarcodex.com/2016/11/16/you-are-still-crying-wolf/) | [951 comments](https://np.reddit.com/r/slatestarcodex/comments/5ddf5i/you_are_still_crying_wolf/)  
>>> \#2: [Against Murderism](http://slatestarcodex.com/2017/06/21/against-murderism/) | [447 comments](https://np.reddit.com/r/slatestarcodex/comments/6ip8nf/against_murderism/)  
>>> \#3: [A Modern Myth](https://slatestarcodex.com/2017/02/27/a-modern-myth/) | [57 comments](https://np.reddit.com/r/slatestarcodex/comments/5wi2mm/a_modern_myth/)
>>> 
>>> ----
>>> ^^I'm ^^a ^^bot, ^^beep ^^boop ^^| ^^Downvote ^^to ^^remove ^^| [^^Contact ^^me](https://www.reddit.com/message/compose/?to=sneakpeekbot) ^^| [^^Info](https://np.reddit.com/r/sneakpeekbot/) ^^| [^^Opt-out](https://np.reddit.com/r/sneakpeekbot/comments/5lveo6/blacklist/)

>>> **u/cjet79** [+1]  (2 days later)
>>> 
>>> It has certainly increased the volume of comments in those threads.

>> **u/Menolith** [+3]  *Unworthy Opponent* (10 hours later)
>> 
>> [Automod is very versatile in that regard](http://i.imgur.com/5mvQink.png).
>> 
>> In general, I think it would be a good idea. It evens out the highs and lows so the average comment gets more attention. Not sure how impactful the changed sorting would be on slower threads, though, since it's not too hard to read through them entirely regardless of ordering.

> **u/MagicWeasel** [+3]  *Cheela Astronaut* (20 hours later)
> 
> I'd appreciate it too! I often am hesitant about posting on a Monday or Friday thread because they're already so full by the time I wake up. 
> 
> Users are able to override the default sort so if they don't like the "new" setting they can make it "best" instead.

> **u/ketura** [+1]  *Organizer* (9 hours later)
> 
> I support this product and/or service.

---

