## Fanfiction Recommender using Collaborative Filtering

* Author: u/grinnbearit *
* URL: http://www.sidhantgodiwala.com/blog/2014/12/11/building-a-fanfiction-recommender-ii/
* Score: 14

* Created: 2014-12-11T18:32:51

### Post:

[Link to content](http://www.sidhantgodiwala.com/blog/2014/12/11/building-a-fanfiction-recommender-ii/)

### Comments:

> **u/alexanderwales** [+4]  *Time flies like an arrow* (an hour later)
> 
> I've often wondered why ff.net doesn't do this themselves. They already make the list of favorite stories public for every user, so it doesn't seem like too much work to code something up that would do a better job at recommendation than what's available on the site now (which is basically crap at finding good stuff).
> 
> I'll be interested to see what the author recommender turns up.

>> **u/Empiricist_or_not** [+4]  *Aspiring polite Hegemonizing swarm* (an hour later)
>> 
>> This strikes me as computationally expensive.

>>> **u/alexanderwales** [+3]  *Time flies like an arrow* (an hour later)
>>> 
>>> Netflix and Goodreads both do it. It should be far simpler for ff.net because it's just a simple "favorite" binary instead of seven choices like Netflix, or six like Goodreads (though Goodreads has a multilevel system that's a bit more complex). I closely followed a lot of the discussion that surrounded the Netflix Prize, and it really isn't *that* expensive depending on which methods you use (and there are a ton of ways to get around any expensive parts).

>>>> **u/FaceDeer** [+3]  (9 hours later)
>>>> 
>>>> For that matter, I think I should mention that Goodreads does allow fanfiction to be listed. The only conditions are:
>>>> 
>>>> * Must be complete
>>>> * Should be "book length"
>>>> * Can't use a screenshot from the source material as a cover image
>>>> 
>>>> Those rules are kinda flexible, too, I suspect they're only there so that they can clean up stuff at their discretion. [Methods of Rationality](https://www.goodreads.com/book/show/10016013-harry-potter-and-the-methods-of-rationality) has an extensive entry despite still being in progress, for example.
>>>> 
>>>> I'm actually a Librarian over there, so if anyone has favourite fanfics they'd like to see listed or that have incomplete listings, let me know and I'll do what I can to fill them out nicely. :)

>>>>> **u/eaglejarl** [+1]  (10 hours later)
>>>>> 
>>>>> One of my favorite authors over there is [ebfiddler](https://www.fanfiction.net/u/3092366/ebfiddler) who does some really good Firefly fiction.  She has 12 stories which together constitute a "book length" work, but they are 12 different URLs.  The first half-dozen are about 12-20,000 words, then they start getting longer, going from 50k to 80k.
>>>>> 
>>>>> Actually, given that a novel is generally considered anything from 40k - 120k (depending on genre) there is well more than one book here.  Still, the question stands.
>>>>> 
>>>>> How would / could these be listed on GoodReads?

>>>>>> **u/FaceDeer** [+2]  (11 hours later)
>>>>>> 
>>>>>> Personally, I'd say that the stories are "eh, close enough" to book length and just put them all in, and then link them together into a series.
>>>>>> 
>>>>>> I happen to have a system already set up to do this sort of thing quickly, so here you go: [ebfiddler's Firefly series is on Goodreads now](https://www.goodreads.com/series/142514-a-lion-s-mouth) (didn't know what to name the series so I used the first story's name as the series name. Easily edited if you know what it should be called instead). And as a side effect of the process, [here's a zip containing epub versions of them all](http://www.mediafire.com/download/j86q1smweianm9q/ebfiddler's_Firefly_series.zip). I downloaded them all into a Calibre library using the FanfictionDownloader plugin, then exported a CSV file with all the relevant metadata from the library, and then used the iMacros firefox plugin to automate data entry putting them all into Goodreads.

>>> **u/somnicule** [+1]  (9 hours later)
>>> 
>>> It is if naively done, but for item-based collaborative filtering it doesn't matter much if it takes ages to update all the Jaccard indices. A user can still get relevant recommendations based on how much reader overlap there is between their favourite stories and other stories, which updates immediately if they follow more stories.

>> **u/eaglejarl** [+3]  (5 hours later)
>> 
>> As far as I can tell, FFN wrote a system 10ish (?) years ago that satisfied its needs and hasn't really kept up since then.  There are a lot of very obvious features missing -- one simple example is that there is a Document Manager where I upload and possibly edit chapters, and then there is a Manage Stories where I post / update story chapters.  Wouldn't it make sense it, when I edit a document and then save it, the chapter automatically updates to use the new content?  Or, at least, if there were a 'Save and Update' button that would do that.

>>> **u/None** [+2]  (5 hours later)
>>> 
>>> Right?! Man, that site sucks. We're stuck in some dumb coordination game where everyone has to use ffn because everyone uses ffn.
>>> 
>>> WE MUST ALL ACT AS ONE, MEMBERS OF /R/RATIONAL!

>>>> **u/eaglejarl** [+3]  (11 hours later)
>>>> 
>>>> Ok, here is a feature I would like FFN to add:  the ability to link to a specific review.
>>>> 
>>>> And here's a a feature I would **REALLY** like FFN to add:  the ability to block particular users from leaving reviews or PMing me.    (Yes, I realize it wouldn't be a perfect solution as they could leave the reviews anonymously.)
>>>> 
>>>> I've had one guy who didn't pay attention / frequently misunderstood what he was reading, then left foul-mouthed trollish comments telling me all the ways he felt that I'd screwed up.  That was annoying, but manageable.
>>>> 
>>>> I now have a guy posting reviews who, after several exchanges via PM, I honestly believe is out of touch with reality.  He does not curse, but his comments are starting to make me uncomfortable; for example, the one that is currently [first on this page](https://www.fanfiction.net/r/9669819/0/1/) which starts with "So close and yet so far,"   He's commenting on [this chapter](https://www.fanfiction.net/s/9669819/53/The-Two-Year-Emperor) in which the characters are making sacrifices and [the ](#s "alignment of the person making the sacrifice") determines the color of the resulting flames.  The reviewer is proceeding to tell me that I got it wrong and what the colors should mean.  Here's a couple of excerpts:
>>>> 
>>>> > The color of Morality which you mistakenly call Lawful Good is NOT gold, it's goldEN. It's specifically the color of the SUN, not the color of filthy metal.
>>>> 
>>>> >Red is the color of human blood. The blood of life, the blood flowing in your veins, the blood you shed for humanity. NOT the color of purity.
>>>> 
>>>> Personally, I find this creepifying.

>>>>> **u/None** [+1]  (20 hours later)
>>>>> 
>>>>> Yeah...he's going to kill you. Well, if you disappear from the sub for a few weeks we'll have a lead, at least.

>>>>>> **u/eaglejarl** [+2]  (21 hours later)
>>>>>> 
>>>>>> > Yeah...he's going to kill you. 
>>>>>> 
>>>>>> :P
>>>>>> 
>>>>>> I have a very low prior on him killing me.  I still find it creepy.

>>>> **u/Rhamni** [+2]  *Aspiring author* (7 hours later)
>>>> 
>>>> I would, but all I've got on there are shitty Ranma 1/2 fanfics from half a decade ago, and I'll die before I show them to /r/rational.

>>>> **u/None** [+1]  (2 days later)
>>>> 
>>>> >Right?! Man, that site sucks. We're stuck in some dumb coordination game where everyone has to use ffn because everyone uses ffn.
>>>> 
>>>> There is a site with *much* better features: its own editor *and* Google Docs integration, a story manager, various groups with folder arrangements to provide for specific interests, and a Feature Box with autogenerated recommendations based on click/like/vote/favorite trends.  It just turns out that their idea for solving the coordination problem was to say "Friendship is magic" and leave it at that.
>>>> 
>>>> *snrk*

> **u/RMcD94** [+1]  (5 hours later)
> 
> Would be nifty to do this with subreddits too, though I imagine a fair number of people browse but don't subscribe

>> **u/alexanderwales** [+1]  *Time flies like an arrow* (23 hours later)
>> 
>> There's no way to tell which people are subscribed to a subreddit. You can scrape for people who have set their flair, or scrape for people who have ever made a comment or post, but there's no way that I know of to see all the lurkers, who far outnumber the commenters. This sub, for example, has nearly 2,000 subscribers but the highest number of comments we've had on a single post is in the low ~~double~~ triple digits (and most of that is the same handful of people talking with each other).
>> 
>> See [this post](http://www.reddit.com/r/TheoryOfReddit/comments/1uk9uc/tribes_of_reddit_and_a_new_subreddit_recommender/) in /r/TheoryOfReddit about the "Tribes of Reddit" for some analysis along those lines.

>>> **u/xamueljones** [+1]  *My arch-enemy is entropy* (23 hours later)
>>> 
>>> I know what you mean. I was a lurker on this subreddit for a while mostly for the interesting links to other sites and I couldn't care less about the comments.
>>> 
>>> But I kept seeing comments that I wanted to say something in response to, and I just finally got an account and the rest is history.

---

