## [D] Monday General Rationality Thread

### Post:

Welcome to the Monday thread on general rationality topics!  Do you really want to talk about something non-fictional, related to the real world?  Have you:

* Seen something interesting on /r/science?
* Found a new way to get your shit even-more together?
* Figured out how to become immortal?
* Constructed artificial general intelligence?
* Read a neat nonfiction book?
* Munchkined your way into total control of your D&D campaign?


### Comments:

- u/Noumero:
  ```
  As [the self-appointed Court Statistician of this subreddit](https://www.reddit.com/r/rational/comments/6cnsm4/d_monday_general_rationality_thread/dhwgugo/), I took it upon myself to analyse the results of [this little experiment](https://www.reddit.com/r/rational/comments/6jqdij/meta_can_the_weekly_discussion_threads_be/). (tl;dr: default comment sorting for Friday Off-Topic threads was set to "new", to test whether this would encourage more discussion.) Ten weeks have passed since it began. 

  First, **raw data: ([.odt](https://www.dropbox.com/s/eubepzi972n8qgk/Weekly%20Thread%20Statistics%20%20UPDATED%2004.09.2017.ods?dl=0), [.xls](https://www.dropbox.com/s/yyga0cnl0cao8gy/Weekly%20Thread%20Statistics%20%20UPDATED%2004.09.2017.xls?dl=0))**. Includes an updated version of the upvotes/comments/top-level comments statistics for all weekly threads.

  As you can see in the bottom part of this table, I calculated the average numbers for upvotes, total comments and top-level comments for the ten last Friday threads, which used the new setting (period: 30.06.17 — 01.09.17), and the same for the ten threads before the switch (21.04.17 — 23.06.17). I then compared the average numbers for the ten last threads to total averages, and to the averages of the ten before-switch threads.

  Results: compared to before-switch, there's a significant (12-14%) increase in the number of comments and top-level comments, and an increase in upvotes (7.6%). Compared to total-average, there's an insignificant increase in top-level comments and upvotes (2-3%), and a significant increase in upvotes (6.7%).

  There's noise, of course: was the new setting responsible for some of it, or is it the natural result of the subreddit's growth?

  In an attempt to get rid of the noise, I compared ten threads from before-switch (21.04.17 — 23.06.17) to ten threads prior to *that* (10.02.17 — 14.04.17). The numbers were lower: no more than 3.5% variance, which suggested that either 10 threads from before-switch were abnormally low on numbers, or that the new setting was in fact helpful. Were the (21.04.17 - 23.06.17) Friday threads abnormally low on numbers compared to the rest of the subreddit? Why yes, they were: -9.82% in Friday comments compared to +6.73% in total comments.

  Does this mean that Friday Off-Topic threads are in a decline, only stopped by the new setting default, or that the before-switch ten are abnormally low?

  Comparing the increase in upvotes in newest vs. total between Friday and Across All Threads, we could also see a rough correlation here. Which means that the upvotes increase was, most likely, unrelated to the new default sorting.

  **Conclusion:** the usefulness of the new default sorting does not seem to be evident, but large amounts of statistical noise prevent me from forming any more certain conclusions. ^((We need a better statistician.)^)

  ___

  That said, let's analyse data for other threads.

  * Across every weekly thread, the decrease from totals could be attributed to branching: old threads such as Monday General Rationality previously included discussions that now were moved to Wednesday Worldbuilding, and so on.

  * Monday General Rationality: significant decrease in comments compared to totals, no change in upvotes. Compared to 10 old threads, slight decrease in comments and upvotes, significant increase in top-level comments.

  * Wednesday Worldbuilding: very significant decrease in comments and top-level comments, both compared to totals (21%, 30%) and 10 old threads (25%, 15%). It does not correlate with Across All numbers for the relevant time periods.

  * Sunday Munchkinery: significant decrease in top-level comments (~16%), both compared to total averages and ten old threads. Slight decrease in comments (3-7%), not correlated with Across All numbers.

  * Across All: mostly positive numbers, with 12.64% increase in upvotes compared to total averages in 70 last threads,  6.71% increase in comments and 3.08% in top-level comments.

  Well, what we worked out? Wednesday Worldbuilding appears to be in a decline, and I don't think it could be attributed to branching.

  **Edit:** Additionally, [here](https://docs.google.com/spreadsheets/d/1Z5LlgZ2y1Yr_u-f8iCK4RMZQBSGaA3uwMJxdQgfs3io/edit?usp=sharing) is an interesting "BigData" statistics gathered using Google's BigQuery service and [this](https://www.reddit.com/r/bigquery/comments/3cej2b/17_billion_reddit_comments_loaded_on_bigquery/ct3za0t/) query. Includes information for all posters on r/rational, ranked by the total number of posts left by them on the subreddit.
  ```

  - u/alexanderwales:
    ```
    Commenters are distributed along a power law, as you [can see here](https://docs.google.com/spreadsheets/d/1EwpYAPX9vzG-TyMDDO3tIYqEO21qsHcGvcVFS2EoA1M/edit?usp=sharing) (though this data is old). I'd be interested to know how much of a change is due to individuals coming and going from within the community, or high-impact individuals having a lull in activity, since that seems likely to be a major driver in the change of numbers, and a very significant source of noise.
    ```

    - u/Noumero:
      ```
      Interesting. How was this data gathered?

      First 100 of users from this list appear to be responsible for 25732 comments and accumulating 71987 upvotes. The list covers 606 days, from January 2014 to September 2015, correct? My table covers 735 days, from September 2015 to September 2017, and lists 5407 upvotes and 19649 comments. Even taking into account the fact that my data only covers weekly threads, the first 100 really do seem responsible for relatively enormous amount of activity. `71987/113158=0.63` and `25732/40069=0.64`... They're responsible for 63% of upvotes and 64% of comments. Huh.

      Sad news: My data and your data are virtually non-overlapping. Yours ends at September 2015, mine starts.

      >I'd be interested to know how much of a change is due to individuals coming and going from within the community

      I suppose this could be done relatively easily by going through the list of weekly threads and checking which of the first 100 users from this list commented there, but my programming skills won't be enough to do this efficiently.

      **Edit:** Wait, no. Yours starts in 2009, but the activity only really begins in December 2013. Doesn't change the above much.
      ```

      - u/alexanderwales:
        ```
        This was gathered from the BigQuery dataset, [see this comment](https://www.reddit.com/r/rational/comments/3kjt60/d_friday_offtopic_thread/cuxyvle/). I don't think that I have the actual query I used for this anymore, otherwise I would rerun it with updated data.

        Edit: nevermind, it's [this query](https://www.reddit.com/r/bigquery/comments/3cej2b/17_billion_reddit_comments_loaded_on_bigquery/ct3za0t/), which I don't have time to get running again, but feel free to have at it.
        ```

- u/696e6372656469626c65:
  ```
  Question: I often see a lot of rationalists blogging on Tumblr, which based on initial impressions doesn't seem like the best place to write long, involved posts or to have long, involved conversations. Both of these things are so typical for rationalists to engage in that describing them as "typical" borders on *understatement*, and yet for some reason there are a surprising number of rationalists on Tumblr. *I notice that I am confused*; could someone tell me what's going on here?
  ```

  - u/None:
    ```
    It's really nice to be able to write out a bunch of pretentious, semi-academic stuff and not have anyone go all Reviewer 2 on it.  Especially because when you do go *full* academic on it - totally documenting everything, sourcing all the claims, using field-specific precise jargon - it becomes unreadable and nobody engages.

    I'm not sure how to solve this.
    ```

  - u/gbear605:
    ```
    My guess is that sometimes people just want to enjoy making short posts and not needing to be too serious.
    ```

- u/ianstlawrence:
  ```
  Hello!

  I read this recently: http://www.mangareader.net/dr-stone/1 It is not yet done, but I would characterize it as "rational light"? It describes itself as sci-fi survival, but it is very much the aesthetic of a manga.

  Interested in any strong reactions, although I am not sure there will be.
  ```

  - u/tonytwostep:
    ```
    I absolutely love this series, but would certainly not classify it as rational.

    ** **MINOR DR STONE SPOILERS BELOW** **

    * None of the characters besides Senkuu (and maybe Tsukasa) are particularly rational, and many are unrealistically two-dimensional (including Taiju, Yuzuriha, and many of the villagers).
    * The characters are ostensibly "normal"/realistic, but many of the characters have superhuman abilities (e.g. Taiju's strength, Tsukasa's fighting ability)
    * The problems are solved not through science, but through SCIENCE! That is, discoveries/inventions have disproportionately huge impacts, details in the creation process are discussed but glossed over or overly simplified, and rare materials or situations (like the recent lightning storm) often appear at the exact perfect time, deus ex machina style.

    Again, I love Dr. Stone. But I think the series, like a lot of other fiction out there, should be enjoyed in spite of (or often *because* of) it's irrationality; it's simply inaccurate to classify it as rational, or even "rational-lite".
    ```

    - u/ianstlawrence:
      ```
      First I want to say that I think every point you make is pretty valid, but I am curious about the distinction of rational and rational-lite.

      I am going to start with your second bullet-point, as your first is a very general statement, that before tackling it might be beneficial to look at the others first.

      2nd bullet-point - Characters having abnormal abilities doesn't stop something from being rational. Look at HPMOR, they have magic. And it is considered the epitome of rational fiction, or at least the most popular example. 
      I feel like what you maybe are saying is that the rules for human beings are not consistent, and a world without consistent rules has a very hard time being rational?

      3rd bullet-point - This is where I would say this story is rational-lite. The smartest possible decisions are, probably, not being made, and I would agree a lot of the processes are either accelerated or benefit from good luck (although good luck, I would say does not equal non-rational). 
      I, personally, feel like a lot of the rewards take work. Now, it isn't necessarily work that has its own consequences, but it is also true that they've provided working have to happen for any reward. Nothing, so far, has just been given for free, except maybe the lighting storm. But then I have to ask, how long do you have to wait for the lighting storm for it to feel "right" to you? 

      I think a lot of the saving grace, in terms of rational-lite-ness, for this show comes from Senkuu being a level 1 or 2 player to Tsukasa's level 0 or 1, the fact that Senkuu makes the mistake of assuming the North Star is correct without factoring in the possible straying of its path after 3700 years, and that Chrome, despite not being as knowledgeable is treated as a valuable by Senkuu. These are all characteristics I see as pertaining to rational-lite.

      Now, all of this is under the umbrella of the Shounen-ish genre, so it either suffers or benefits (depending on your perspective) from that. I think this is why, as you said, there is disproportionate strength or fighting ability, 2 dimensional characters (although we've seen some of that cleared up, I'd argue. Its just that there is not a ton of character development as the plot moves forward [Also i am not sure that 2 dimensional characters precludes from rational fiction, just probably good fiction])

      Again, the purpose of this post is to enter into discussion, not necessarily to "win" the argument. I am just curious, because my take on Dr. Stone is pretty different than yours, and I also seem to have a pretty different idea of what removes the label of "rational" to a piece of fiction than you do.

      Best,
      ian
      ```

      - u/tonytwostep:
        ```
        You raise some good points as well, and I may need to reexamine my view in light of your arguments.

        However, as my first-thought response, I guess it would be more helpful to take the subreddit's rationalfic criteria, and examine them point by point?

        > Nothing happens solely because 'the plot requires it'. If characters do (or don't do) something, there must be a plausible reason.

        I think this one is borderline for Dr Stone. Like I mentioned, a lot of rather unlikely situations (encountering a villager with a ton of rare and important minerals, a lightning storm occurring right when Senkuu is attempting to recreate electricity, etc.) basically happen just because the plot requires it. On the other hand, the characters do generally act based on plausible (or semi-plausible) motivations.

        > Any factions are defined and driven into conflict by their beliefs and values, not just by being "good" or "evil".

        Dr Stone does a fairly good job of this - even the "evil" Tsukasa has a worldview that's realistic and understandable, even if its not relatable.

        > The characters solve problems through the intelligent application of their knowledge and resources.

        Dr Stone *mostly* does a good job of this (at least, Senkuu does). And like you said, the series even takes it to the next level, where characters fail to take certain scientific details into account (like the shift in North Star trajectory) in a realistic fashion, and later adjust their calculations/decisions based on those realizations.

        > The fictional world has consistent rules, and sticks to them.

        I think this is my biggest contention with a "rational" label, and maybe where you and I disagree the most. I agree that supernatural abilities don't discount a story from being rational, but in this case, Dr Stone is pretty clearly suppose to occur in a future version of our world, with its main characters coming specifically from our world and time. IMO it's inconsistent to be so based in our world from a scientistic perspective, while having characters with unexplained supernatural strength, reflexes, or fighting ability.

        ----------

        All that said, maybe it's a bit pedantic of me to argue whether the series is rational (or rational-lite), when there are clearly enough elements to interest rationalfic fans regardless? I just know that the label generally gets thrown around a lot, which can detract from the meaning of the category.
        ```

- u/None:
  ```
  Excuse my ranting, but [this is a presentation filled with the most magnificently *bad* ideas about how to create general AI and make sure it comes out ok.](https://docs.google.com/presentation/d/119VW6ueBGLQXsw-jGMboGP2-WuOnyMAOYLgd44SL6xM/preview?slide=id.p)  It's literally as if someone was saying, "Here's stuff people proposed in science fiction that's almost guaranteed to turn out omnicidal in real life.  Now let's go give it all a shot!"

  You've got everything from the conventional "ever-bigger neural networks" to "fuck it let's evolve agents in virtual environments" to "oh gosh what if we used MMORPGs to teach them to behave right".

  [Anyone mind if the Inquisition disappears Karpathy and the OpenAI staff for knowingly, deliberately *trying* to create Abominable Intelligence?](https://vignette2.wikia.nocookie.net/warhammer40k/images/d/d7/Imperial_Cardinal_and_retinue.jpg/revision/latest?cb=20130424183351)
  ```

  - u/Noumero:
    ```
    I don't think it's this bad? I mean, the artificial evolution idea is omnicidally suicidal yes, but the rest is tame enough, even if generic. The author also doesn't seem to say that this is how AGI should be done, merely how it *could* theoretically be done. The MMORPG thing is explicitly mentioned as a crazy idea/example of something unexpected.

    I do disagree with the "order of promisingness" as presented, but it's nothing offensive.  Did I miss something? I only skimmed it. I may lack some context regarding this OpenAI company.

    ... Or, wait a moment. Is that an AI research company's official stance on the problem? Iff yes, I retract my objections, and also, we are all going to die.
    ```

    - u/crivtox:
      ```
      Yes the other parts are tame , but the ommicidal idea is the one they seem to be  most interested in, and having the artificial evolution in the presentation makes me suspect that the things that seem tame are actually worse than I initialy though , but I can't say for sure without hearing the actual talk that the presentation was made  for.
      Regarding the context I dont know  how oficial this is .
      And yes I probably was exaggerating a bit , the mmo part is probably just for saying something people are familiar whith and will understand even if they didn't understand the rest of the talk, I dont know who the audience is supposed to be.

      /U/eaturbrainz, where did you found this , is it actually the official stance of open ai , or just some talk by someone related to them that doent necesarily reflect the wiews of the other open ai people?.
      ```

      - u/None:
        ```
        >/U/eaturbrainz, where did you found this , is it actually the official stance of open ai 

        The link was in a machine-learning mailing list I get.  It was presented as serious.  It was a conference presentation.
        ```

        - u/crivtox:
          ```
          Well , you are right , we are fucked , at least the guy that wrote it is apparently now working in self driving cars and not in open ai anymore, but the other people that work there probably thing similarly about safety(meaning they think its only a problem if the ai takes over the world and everything else can be solved by human supervision , which is what I get the presentation).
          ```

  - u/crivtox:
    ```
    Well they seem think  that if they give unfriendly  ai to everyone it wont be a problem.I think this comes from too many people discussing only what happens if one ai takes o ver the  world . 
    So people like the ones in open ai decide that the one entity taking over is the main problem, and that if there are multiple Ai in competition  that's a problem we can deal whith(even if all of them are unfriendly, and often whith similar utility functions) or worse they decide that having a lot of inteligences whith diferent values is  enough like us to  be ok if the ai replace humanity(open ai only makes the first mistake but I 've seen too many people  making the second by antrophomorficig the ai to  not rant about it) .

    At least it seems that open ai now wants to employ ai safety people so , maybe they will notice that value alignment Is important and will stop trying to kill everyone, even Yudkowsky  wanted to make the singularity happen as soon as posible when he started(until he realized that if he had succeeded he would have destroyed the world)so maybe there is still hope for  them(this is before reading the presentation, let's see how horrible it is)
    ```

  - u/ShiranaiWakaranai:
    ```
    Statistically speaking, we're all doomed.

    The incentives for creating an AGI are too high. Fame. Money. Power. Immortality. Security against other unfriendly AGIs. Every moment you wait is another moment someone is dying when they could be saved by an AGI.

    Which means what we have here is a race. A race to see who makes the first AGI. A race where some people, terrified of unfriendly AGIs, will take it slow, carefully checking and rechecking code to make sure their AGIs are safe... and where other people, filled with greed/pride/confidence/altruism(?), will be rushing their code, abandoning safety measures, just doing whatever gets them done fastest. Who do you think will win this race? The odds favor the reckless here, and then in their recklessness, the AGI they unleash will probably be an unfriendly one that kills us all. Or worse, keeps us alive to torture for all eternity.
    ```

    - u/None:
      ```
      Ah, but luckily, the people "racing" to create AGI are scientific incompetents who try bad ideas out of scifi and would prefer to brute-force everything possible.  So they've so far managed to not even measure up to any single principle of real brain function -- though their cheap tricks look impressive if you don't realize how far the toy problems are from real problems.
      ```

- u/traverseda:
  ```
  I have created a probability wrapper object for sympy.

  https://gist.github.com/traverseda/2c3056aede8b01a9d40c11d6b916774f

  You can use it to do things like `p(0.9)+p("1/3")`. Which will produce 0.9333 or `4203359652212463/4503599627370496`, depending on what you're using it for. No floating point errors here. It's a simple little thing, but pretty handy.

  I would love to at some point be able to automatically produce graphs like [this](https://en.wikipedia.org/wiki/Energy_in_the_United_States#/media/File:LLNLUSEnergy2012.png). But that's a long ways off.
  ```

---

