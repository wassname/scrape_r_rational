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

- u/electrace:
  ```
  I've been tasked with sorting about 500 papers that are basically in random order. 
  Each paper has an integer on it. Keeping in mind that I am not a computer, what's the best way to sort them? 

  It's essentially impossible to do this to all 500 papers at the same time due to space constraints. So currently, I group them by their integer into groups of 100 (1-100, 101-200, etc). Then I take one sheet of paper at a time and place it into the correct position (relative to the others I've already picked out). The problem is that after I get about 10-15 pages into the correct order, searching through the stack (and holding the stack) gets harder and harder. 

  To address this, I've also tried sorting smaller stacks, and then combining the stacks. By that I mean, I take 50 of the papers, sort them, put that stack aside, do the same for the other 50 papers, and then pick the one with smaller integer from both piles until I've combined the two stacks of 50 papers into 100 sorted papers.

  I'm not particularly confident in the efficiency of either method, and would really like to hear any ideas you all have.
  ```

  - u/ulyssessword:
    ```
    Ooh, sorting algorithms!

    >Then I take one sheet of paper at a time and place it into the correct position (relative to the others I've already picked out). 

    [Insertion Sort](https://en.wikipedia.org/wiki/Insertion_sort)

    >To address this, I've also tried sorting smaller stacks, and then combining the stacks. By that I mean, I take 50 of the papers, sort them, put that stack aside, do the same for the other 50 papers, and then pick the one with smaller integer from both piles until I've combined the two stacks of 50 papers into 100 sorted papers.

    [Merge Sort](https://en.wikipedia.org/wiki/Merge_sort)

    >I'm not particularly confident in the efficiency of either method, and would really like to hear any ideas you all have. 

    [Radix Sort](https://en.wikipedia.org/wiki/Radix_sort):

    Sort into 0-99, 100-199, 200-299, 300-399, 400-499 piles.  Next, sort each pile into X00-X09, X10-X19, X20-X29, etc.  Sort those piles of 10 pages into the proper order, then combine them with the other sorted piles.

    ---

    EDIT: things to keep in mind:

    How fast is determining the content of an item? (a printed number on a corner is faster than written name in the middle)

    How fast is moving an item? (single sheets are easier than stapled, as you don't have to avoid putting an item in the middle of another one)

    How many arbitrary buckets can you hold in your mind at the same time?  How many on your table?

    Can you change from a tabletop to an [accordion folder](https://www.amazon.com/Expanding-Expandable-organizer-Multicolour-Blinyang/dp/B0754K6GHQ/ref=pd_sim_229_3?_encoding=UTF8&pd_rd_i=B0754K6GHQ&pd_rd_r=Q1F98THMN6CZWDQ31XQ2&pd_rd_w=rU8Hs&pd_rd_wg=r7sR0&psc=1&refRID=Q1F98THMN6CZWDQ31XQ2) to get more buckets?

    Do you have more people that can parallelize it with you?  Is the overhead worth it?

    ---

    More things:

    Is two the best number? Almost all algorithms compare *two* numbers at a time, but choosing the best of four takes less than double the time of choosing the best of two for a human.  Similarly, Merge Sort and Quicksort have you split things in *half* and combine *two* things back together, but that seems less than twice as fast as doing the same for four things at once.
    ```

    - u/Izeinwinter:
      ```
      Radix sort is probably the least prone to human error of the methods given, and never requires more than 19 stacks. Which should be doable on any desk.
      ```

  - u/phylogenik:
    ```
    > due to space constraints

    can you find somewhere more spacious to spread the papers out? when I had to alphabetize exams I'd usually just do an insertion sort, but that was with far fewer than 500.

    If the papers are 8.5" x 11", why not separate them into 50 (or 51 lol) piles according to their leading 2 digits and then sort each pile? That would require what, like 7' by 7' or so? Assuming they actually are numbered 001-500. 

    You can also try the methods suggested in these threads:

    https://www.quora.com/What-is-the-best-manual-sorting-algorithm-E-g-if-you-had-a-stack-of-papers-that-you-wanted-to-sort-alphabetically-what-would-be-the-most-efficient-way-to-do-it-What-if-you-were-okay-with-them-being-off-by-one-or-two-from-their-sorted-position

    https://stackoverflow.com/questions/8023939/which-sorting-algorithm-for-sorting-a-lot-of-exam-papers-by-hand

    https://stackoverflow.com/questions/9741231/best-algorithm-to-sort-exams
    ```

  - u/ShiranaiWakaranai:
    ```
    I'm curious why people are suggesting sorting algorithms. We live in a 3-dimensional world, not stuck using computer registers, so we can do something far better than just write/stack operations. Not to mention human read operations are ridiculously fast compared to our write (move) operations, so you really want an algorithm where you can do tons of reads but as little writes (moves) as possible.

    With that in mind, I prefer just having one diagonal "stack": starting with your pile of 500 papers, take whichever one you can take fastest and put it on the floor. Take another, put it next to the one on the floor. Repeatedly take another paper from the pile, and compare its integer to the papers on the floor. This will quickly let you find the right position it should be placed in. Place it such that it is directly on top of the paper with the immediately smaller integer, shifted slightly so both their integers are visible, and directly below the paper with the immediately larger integer, again shifted slightly so that both their integers are visible. The trick here is that since all (or most if you have less space) integers of the currently sorted papers are always visible and clearly ordered, you can read them all very quickly without moving them, saving you lots of time. If the integers are written in a small corner of the paper, which is usually the case for exam papers, this method doesn't even take up that much space.
    ```

    - u/ulyssessword:
      ```
      > I'm curious why people are suggesting sorting algorithms. 

      You're recommending insertion sort, and giving a specific efficient implementation.  Once you start seeing algorithms in the world around you, you can't stop.
      ```

  - u/GaBeRockKing:
    ```
    So from my time playing yugioh, the fastest way to sort large stacks of paper is to exploit the following facts:

    * that it's trivially easy to read paper, and therefore that it's trivially easy to sort very small stacks of paper(<~12 sheets or so)
    * that combining stacks of paper is O(1)
    * holding a stack of paper, taking a page off the top, then assigning it to a sub-stack is also very fast, provided you have small number of  easily recognizable sub-stacks.

    So with 500 pages, you're on the right track with putting them into groups of 100, but you shouldn't be immediately sorting them, because size ~50 stacks are still too much of a pain in the ass. Instead, for each size ~50 group, you repeat the previous step, but for groups of 10, leaving you with 10 groups of 1-10 pages. At 5-10 pages, you can typically glance through the mini-stack and immediately figure out ordering, so you sort each group of ~5 pages in near-optimal time, leaving you with 10 stacks of 1-10 pages Then you can recombine these stacks in order, which will go pretty quickly, leaving you with a sorted size ~50 stack. Then you repeat the process for your other size ~50 stacks, leaving you with 10 size ~50 stacks, and then you repeat the stack recombine operation, leaving you with a sorted 500 pages.

    Now, there might be a space constraint issue, what with you needing to have a maximum of 9+9=18 stacks on the table, plus one in your hands, but luckily for the greater group of 9 stacks you can have them overlapped when your messing with the smaller group, and if you overlap horizontal-vertical-horizontal-vertical you can put 9 stacks in the place of two.
    ```

  - u/ben_oni:
    ```
    I recommend a [quicksort](https://en.wikipedia.org/wiki/Quicksort) algorithm. You'll need a bit of a work area to hold multiple stacks, or be able to use stickies in the stack to serve as bookmarks (dividing different sub-stacks). An accordion folder (as mentioned by u/ulyssessword) would work best.

    1. Take a stack of papers. Quickly guess what number would divide the group in two (greater and lesser). It doesn't matter if your guess is off, but try to get something near the median. Flipping through the stack real quick should give you a good idea what number to use.

    2. Next, separate the stack into two more stacks, greater, and lesser (or equal). Use the smaller stack, and repeat from step 1. This should give you a series of stacks from larger (and high numbered) so smaller (and lower numbered).

    3. Keep going until you have a stack you can quickly sort by hand (maybe 10 pages?). Once done, set this stack upside-down in the "sorted" pile. Move onto the next stack (which should be about twice the size), and repeat from step 1.

    Note that depending on what you are sorting, there are probably more efficient ways to do it. I often find myself sorting things by integer that *also* have secondary attributes that are easier and faster to compare. I use a dictionary sort in these cases (grouping by gross secondary attributes, and then doing a quicksort on each group.)
    ```

- u/None:
  ```
  One thing that I've been really curious about with when it comes to this sub and the assorted mentality is the sort of irrational insensitivity to difference. 

  Which is to say: I think so many "munchkin" plans aren't actually rational cause they don't account for the way the world is. A basic example would be setting up an intercontinental shipping company if you can open portals. Seems pretty standard and sensible right? Right. Except not really, not in this world as it exists. There's just no way you walk into the government building and get permits, for obvious reasons. You're a worldwide celebrity now, not a businessman. 

  I think people almost never factor in how disruptive the things they're munchkining are and how the world would react in the short term. Possibly because it's essentially impossible to tell. Predicting non-fantasy geopolitics is hard enough.

  Does anyone ever get this sense or is it seen as a cost of doing business when you munchkin in thought experiments.
  ```

  - u/zarraha:
    ```
    I think there's an implicit assumption of "this is the best case scenario", that the shipping company or whatever is the optimal method that you would strive to accomplish.  I don't know how opening intercontinental shipping company works, and I also don't want to spend however many dozens or hundreds of hours it would take to learn all of the relevant business and political details before I make my reddit post.

    We sort of abstract away the details and say "this is what I'd like to do" with an unmentioned nod to the idea that if you did get portals you would be willing to invest the time to learn how these things work, and even if there are trials and tribulations and maybe the company doesn't get going until five years later, it would be worth it once it did.
    ```

  - u/tonytwostep:
    ```
    I strongly agree. So many of the suggestions in the munchkinry threads, seem to make some *crazy* assumptions that fall well outside the realm of plausibility.

    For example, [a recent thread](https://www.reddit.com/r/rational/comments/7ar5by/d_saturday_munchkinry_thread/dpclgvs/) posed a question about munchkining [Biochromatic Breath](https://coppermind.net/wiki/BioChromatic_Breath), from Sanderson's *Warbreaker* novel.

    One person's "munchkined" plan was:

    > Step 1) Go to a third-world country or somewhere with lots of poor people. Offer them money to give you breath (without telling them how giving you breath actually affects them).

    > Step 2) Start animating corpses en masse with the order "Behave as if you were alive, but completely loyal to me and willing to obey every command I give."

    > Step 3) Mass clone people, raise the clones in secret facilities until they can speak and manipulate them to hand over their breaths. Then kill them and grow another clone. Use the undead from step 2 to guard your secret facilities.

    It's just...there are *so many* unrealistic assumptions in this munchkining. Even step #1 has a crazy amount of issues attached, as if a foreigner can easily wander around a third world country, offering money to anyone willing to say a phrase, and not attract a lot of attention. It just escalates from there - where the heck can you just get a bunch of corpses? And then we jump straight to "mass clone people in secret facilities"???

    I guess rather than exploring extreme power fantasies, I'm much more interested in *realistic* approaches to "munchkinry". The former is creative storytelling, the latter is an actually interesting logical exercise.
    ```

    - u/None:
      ```
      > Even step #1 has a crazy amount of issues attached, as if a foreigner can easily wander around a third world country, offering money to anyone willing to say a phrase

      To be fair, as someone from a third world country that tries to bring in tourists and cater to them...that's definitely the easiest part :P

      That said...yeah. It's actually hard to explain what to do with superpowers because they're sort of a singularity; everything after them changes imo, especially if they're public. It's why so many stories start a while after they showed up, cause it's hard to predict how things would change in the short term. 

      But that still doesn't excuse some of the more optimistic "rational" munchkins.
      ```

- u/trekie140:
  ```
  Before I got my job, I had seen the [Adam Ruins Everything](https://youtu.be/7xH7eGFuSYI) about how the taboo against discussing salary gives employers an unfair advantage in negotiations, so I had no inhibitions against sharing how much money I make with whoever asked. 

  When my Mom found this out, she chewed me out in one of the few heated arguments we’ve **ever** had. She acted as if I’d violated some sacred social rule and when I rejected her justifications for it as irrational, she continued to insist it was “just a thing you don’t do”, which I’ve never heard from her.

  Today, my boss told me that he knew I had been telling coworkers my salary and politely, yet sternly, stated that I should change the subject whenever someone brings it up so he doesn’t have to explain to them why I get paid more than them even though they’ve worked here longer.

  The reason I’m paid more is because my education makes me eligible for a position I will eventually be trained for, but right now I’m working the assembly line with the other blue collar laborers. I was really nervous during the meeting and now I’m worried about what I should do.
  ```

  - u/Iconochasm:
    ```
    People get upset about this topic because it's an *egalitarian* social more.  For example, my D&D group has in the past had jobs ranging from "part-time cashier" to "high level defense industry IT consultant".  Flat out comparing salaries would have seemed *horribly* douchey.  Now, that's a social group, rather than a collection of employees, but there's a similar dynamic at play.  When you tell the "blue collar laborers" that you make more than them in spite of being less qualified for the actual job you're actually doing, it's going to come off as offensively pretentious and unfair.  What, they have to wipe your ass while you learn the job and you get paid more anyway because you're just magically *superior*?  Even aside from potential discontent with the boss, you're inviting discontent with *you*, which adds an extra burden to the boss, because they're the one that has to deal with the hit to morale.  

    The American refusal to discuss pay may make salary and wage negotiations more favorable to employers, but it also serves to remove salary and wage from workplace social status games.  You've just forced that element back into the game, and implicitly claimed a high status position.

    As for what to do about it... find a new job?  The only real alternative is to *rock the shit* out of your current position such that if/when you do get promoted up to your level of education, the response from the "lowly" blue collar people is "Yeah, alright, that makes sense."  A high level of empathy for your coworkers would help, but you'd need to avoid coming off as pretentious like the plague.
    ```

    - u/trekie140:
      ```
      Well, I don’t treat my salary as a signifier of my status in the workplace and I don’t see why anyone I’m friends with would hold it against me when I don’t decide how much I get paid. I’m autistic and don’t understand social norms, so I tell everyone I meet to be brutally honest with me so misunderstandings can be avoided and mistakes can be rectified. I never told my salary to anyone who didn’t ask me first and they never called me out for being rude.
      ```

      - u/Iconochasm:
        ```
        > I’m autistic and don’t understand social norms, so I tell everyone I meet to be brutally honest with me so misunderstandings can be avoided and mistakes can be rectified.

        I'm *not* autistic, but I am very blunt and literal minded, and in my experience this literally never works.  It flies in the face of a lifetime of conditioning for social/white lies.  I think most people interpret it as some kind of signalling.

        If you're just answering honestly when people ask you, then my concerns in the previous post are greatly lessened.  Much lower chance of a social backlash against you.  In this scenario, you're biggest worry is probably that your boss will decide you're socially retarded in a career-limiting way.  If your eventual position is more technical than leadership, this may not be much of a concern.  In that case I'd advise telling your boss, regarding the request to avoid the topic, something like "Well, I'll try, and I can avoid bringing it up, but I'm not really comfortable lying to people."
        ```

  - u/None:
    ```
    > Today, my boss told me that he knew I had been telling coworkers my salary and politely, yet sternly, stated that I should change the subject whenever someone brings it up so he doesn’t have to explain to them why I get paid more than them even though they’ve worked here longer.

    Well, *yeah*.  Your boss is telling you not to do things that put *him* at a disadvantage.  Such is capitalism, welcome to it, [would you like to hear about the alternatives?](https://www.youtube.com/watch?v=28-fC6_Byu0)

    >The reason I’m paid more is because my education makes me eligible for a position I will eventually be trained for, but right now I’m working the assembly line with the other blue collar laborers. I was really nervous during the meeting and now I’m worried about what I should do.

    Shut the hell up, and then quietly unionize with the other blue-collar laborers.  "Will eventually be trained for" is an excuse: your boss is paying you more right now, which means he probably makes enough profit off you *right now* to be paying the other guys more.  Fight with them.
    ```

    - u/callmesalticidae:
      ```
      I don't really have anything to add, but I feel like I ought to voice my support so that eaturbrainz doesn't possibly come off a lone kook in the wilderness.
      ```

      - u/ben_oni:
        ```
        But he is a lone kook in the wilderness.
        ```

        - u/None:
          ```
          That's my job \^_\^!

          Of course, there are whole subreddits full of people who'll tell you to unionize your workplace, but *around here*, definitely lone kook in the wilderness.
          ```

          - u/ben_oni:
            ```
            The problem is that this is r/rational, where we often focus on finding optimal solutions, so expressing such sentiments really is weird.

            The problem is that unionization is a local optima from which it becomes very difficult to deviate. And in the long run, the outcomes of unionization are very sub-optimal for everyone.
            ```

            - u/None:
              ```
              > And in the long run, the outcomes of unionization are very sub-optimal for everyone.

              How so?
              ```

              - u/ben_oni:
                ```
                Are you familiar with the collapse of the american automobile industry? It's a fascinating story.

                You might also look into the american public school system for further examples.
                ```

                - u/None:
                  ```
                  > Are you familiar with the collapse of the american automobile industry? It's a fascinating story.
                  > 

                  I thought that was caused by a refusal to install technological, engineering, and quality upgrades to compete with the Japanese imports, which then got "taken out" on the unions.

                  I of course agree that unions aren't a global optimum of worker-representation.  Codetermination and cooperative firms work a lot better, but they're harder to create from today's position of extreme class power on behalf of capital and purely confrontational class relations.

                  Today's class relations are an "inadequacy" in Eliezer's sense.
                  ```

                  - u/ben_oni:
                    ```
                    > I thought that was caused by a refusal to install technological, engineering, and quality upgrades to compete with the Japanese imports, which then got "taken out" on the unions.

                    Partially. Another part is the inability of american manufacturers to modernize the factories without violating the agreements with the unions. Consider the fact that a fair bit of car manufacturing is returning to the states, but without the unions, and a larger picture begins to emerge.

                    > extreme class power on behalf of capital and purely confrontational class relations

                    This is socialist language that doesn't relate to reality.
                    ```

                    - u/None:
                      ```
                      > Another part is the inability of american manufacturers to modernize the factories without violating the agreements with the unions.

                      Could you give me some reading to do?

                      >This is socialist language that doesn't relate to reality.

                      At least from our point of view, it certainly draws a map.  If you want to say it's an *inaccurate* map, sure, but at least point out *how* these pens, so to speak, are incapable of drawing an accurate map.
                      ```

                      - u/ben_oni:
                        ```
                        >> This is socialist language that doesn't relate to reality.

                        > At least from our point of view, it certainly draws a map. If you want to say it's an inaccurate map, sure, but at least point out how these pens, so to speak, are incapable of drawing an accurate map.

                        The problem is with *class* and *class distinctions*. We speak of upper-middle-lower classes because it's easy and convenient for the sake of demographics. Without ignoring the fact that people who have more money live differently than those who have little money, we can do away with that language.

                        See, there is no distinction of classes (at least in America; other countries are not so egalitarian, I know). You can't say that a particular thing is true of people who have so much money but not of people who have less (except the amount of money they have). It's an arbitrary division. There is no nobility, or bourgeois (there is, I know; bear with me). The important fact to remember is that heritage is not destiny. "Class mobility" is real, something that blurs and removes class boundaries.

                        Take a look at [this chart](https://www.learnvest.com/wp-content/uploads/2012/07/Screen-shot-2012-07-16-at-11.25.22-AM.png). I'm not sure where the numbers on this one come from, but you can find something similar all over the web. See that bottom quintile? 43% are "stuck" at the bottom? That means 57% got out, meaning they did better than their parents. You see that top quintile, with 40% of children remaining? 60% didn't do so well, meaning they did worse than their parents. To sum that up: It's easier to climb up from the bottom than to stay at the top. I've heard a lot about "the 1%" the last few years. I want to take these people and make them understand that *they* can be the 4%. That's the 4% from the bottom quintile that end up in the highest quintile.

                        Enough about class mobility. Class warfare. This conjures the image of the great economic pie, each section of society trying to claim a portion for themselves, battling for more and more. [Yes, the rich have the most pie.](https://en.wikipedia.org/wiki/Pareto_principle) The 80/20 rule doesn't exist because of class distributions, or class warfare. It's fundamental mathematics, and if it stops being true, things are very wrong in the world. (As an aside, I'll note that it's not always 80/20. I once had the data to check a particular distribution, and found it was 70/30. Upon verifying the math, I found 70/30 was in fact the expected result.)

                        Consider class struggles from someone at the bottom. A minimum wage worker (or, heaven forbid, unemployed) wants a top paying job. If he succeeds, he isn't taking that job from someone else. He gets in *in addition* to everyone else. This may seem counter-intuitive when looking at a job market. You see a good job that matches your qualifications. You submit your resume, interview, and hope to get the position. 99 other people also applied, but only one of you will get the job. So if you get it, that means someone else didn't. But wait, it's more complicated than that. Perhaps you do the job well. Deadlines are met, sales are made, earnings projections are up. More profit means expansion and more positions open up. More of the applicants in the job market get hired. Alternatively, perhaps the company was on the verge of collapse. You try your best, but management screwed up, and sales are tanking, investors are fleeing, and layoffs are coming. You're most junior, so you go first. Nobody from the applicant pool ends up better off than before.

                        Did I say earlier that there's no real distinction between the classes? I lied. The people at the bottom? They are there for a reason. Most of them, anyways. The reason isn't that they are poor, it is the reason they are poor. Confusing the two means mixing up cause and effect. In a very real sense, heritage *is* destiny -- but it is not a heritage of money. The children of the rich do not end up rich because they inherit wealth, but because they inherit the knowledge of how to become wealthy for themselves. That's what makes them the bourgeois.
                        ```

                        - u/None:
                          ```
                          > The problem is with class and class distinctions. We speak of upper-middle-lower classes because it's easy and convenient for the sake of demographics. Without ignoring the fact that people who have more money live differently than those who have little money, we can do away with that language.
                          > 

                          We're definitely using class in very different ways here.  Socialist usage tends to be:

                          * Aristocracy: people who make their living from, well, state-enforced titles of nobility, usually land ownership.  Essentially, you pay taxes so the aristocrats can take them and spend them on themselves.

                          * Rentiers: people who own stuff and charge for its usage, but never actually *sell* it, thus ensuring themselves a permanent income stream.  Usually landowners, sometimes other natural resources.

                          * Bourgeoisie/"owning class": People who own the means of production, eg: machines, land, and natural resources, but whom are *not* paid out of state revenues *nor* can send in armies to just *take* wealth for themselves.  They have to "earn it" through a market, but they're also the best positioned *in* the market, *by default*, without needing any particular merit.

                          * Proletariat/"working class": People who sell their labor to live, while existing within a legally-codified formal economy.  Can contain all kinds of smaller "castes" like professionals, unionized blue-collar workers (the "image" of the working class), and the "precariat" (people who put multiple jobs together to make a living, but still exist in the formal economy).

                          * Lumpenproletariat/"informal working class": People who sell labor or perform illegal acts to live.  Exist largely outside the formal economy.  Drug dealers, thieves, mafia laborers, prostitutes, email scammers, etc.

                          These classes are very real in terms of what assets and what work they use to generate what kind of value within what legal constraints.  Those are their defining features: what do you do, within what laws, for whom, with what.

                          >The important fact to remember is that heritage is not destiny. "Class mobility" is real, something that blurs and removes class boundaries.

                          Well of course.  You can start out professional and wind up bourgeois, like any typical tech startup founder.  Other cases exist, blah blah blah.  For instance, the "magic money tree" of Anglo economies used to be housing wealth: you started out a moderately-paid middle-class prole, you bought a house, its price rose, and over time you became more and more an asset investor or land rentier.

                          (This is why the Bay Area *sucks*, btw.)

                          >Consider class struggles from someone at the bottom. A minimum wage worker (or, heaven forbid, unemployed) wants a top paying job. If he succeeds, he isn't taking that job from someone else. He gets in in addition to everyone else. This may seem counter-intuitive when looking at a job market.

                          Yes, we all understand.  Nobody actually hires you to generate net-negative value.  Not all transactions maximize expected profit, but over time, bankruptcy drives out those which do not at least satisfice on expected profit.  Gains from division of labor are very real.

                          >Did I say earlier that there's no real distinction between the classes? I lied. The people at the bottom? They are there for a reason. Most of them, anyways. The reason isn't that they are poor, it is the reason they are poor. Confusing the two means mixing up cause and effect. In a very real sense, heritage is destiny -- but it is not a heritage of money. The children of the rich do not end up rich because they inherit wealth, but because they inherit the knowledge of how to become wealthy for themselves.

                          This is the part that basically amounts to a romantic apologia for the supposed meritocracy of a deeply unmeritocratic system.

                          The bourgeoisie are defined by what they *own*, not by what they generate.  So for instance, Donald Trump (oh lovely, right?) *is* bourgeois.  Really.  Sure, his business ventures are all massive failures when they're not flagrant money-laundering schemes.  Sure, as far as we know, he's near-constantly in the hole.  Sure, he's a walking example of how to have a rich person's lifestyle while never contributing to society in any but the most minimal ways.

                          *But he still owns the means of production.*  He still pays *other people* to work *for him*, rather than requiring a wage or salary himself.

                          He's a completely incompetent, unmeritorious piece of shit whose very existence defames capitalism -- but he's still bourgeois!

                          Now, if I could only find it, the paper I'd like to link you to had an important finding.  [Oh well, this is similar.](http://www.decisionsciencenews.com/2017/06/19/counterintuitive-problem-everyone-room-keeps-giving-dollars-random-others-youll-never-guess-happens-next/)  You start out however many agents you please with however many dollars each you please, and start flipping coins to determine who profits off randomized transactions (eg: random agents interact).  We can model the "profits" as talking about the financialized expression of differing subjective prices.

                          The result ends up being an increasingly unequal, concentrated, non-competitive "marketplace" -- a degradation into financialized feudalism.  The only known remedies were to re-randomize, forcibly redistribute downward, and/or "break up" the richest parties into much smaller actors.

                          Note that this was just a model of agents stochastically interacting.  The inequality doesn't come from some difference of merit in this model.  It just comes from the sheer *math* of some stochastic systems having rich-get-richer laws.  The big insight gained was: once *any* inequality begins to show up, even by random chance, these systems of transactions would exacerbate it.  The only agents "safe" were those who could mostly get into transactions where no significant fraction of their existing wealth was at stake.

                          I hope you see the point here.  I may be a heterodox socialist, but I am a socialist, because I view economic inequality not only as degrading the standard of living of the masses, not only as undemocratic, not only as morally dystopic, but as something like entropy that needs to be *actively held off*.  There will probably be some form of inequality under socialism, too!  Socialists tend to fall into every trap that a "whuffie"-type mechanism would produce, as do democratic votes.  That is still better than a system in which inequality occurs by stochastic mathematical necessity, and people begin rationalizing it as the relative superiority or inferiority of different people's contributions to society.

                          You don't apologize for the Second Law of Thermodynamics, so don't apologize for this either.
                          ```

    - u/trekie140:
      ```
      That was something I considered, but it looks like the majority of employees here come from a temp agency the company contracts out to so the situation might not be so straightforward. I’m an exception because I got a referral from one of the engineers who happened to be in my graduating class, so my salary was negotiated individually. I did mention this to the coworkers I spoke to, but I still got a lecture from the boss.
      ```

      - u/None:
        ```
        You seriously need to be meeting with the other workers *where the boss doesn't know about it*.  Otherwise you are probably risking your job.

        But wow, a temp agency?  All the more reason to unionize: those things are fucking abusive.
        ```

- u/blazinghand:
  ```
  I recently read this interesting article on ancient methods of multiplication of large numbers: [(link)](https://mathwithicecream.tumblr.com/post/167402359658/ancient-egyptian-multiplication). The idea of doubling one side and halving the others, then adding back the remainder at the end when you accidentally generated a remainder with the halving, is pretty clever. This, along with [Polish Hand Math](https://www.scientificamerican.com/article/parents-corner-polish-han/) is the kind of math thing that's pretty interesting to learn. Taking principles of mathematics and using them to generate a tool that operates on those principles and so can be used for calculation, is fun. In a more modern format, we see mechanical analog computers like the [Slide Ruler](https://en.wikipedia.org/wiki/Slide_rule#Basic_concepts). Cool stuff!
  ```

- u/phylogenik:
  ```
  I've had four sets of questions/thoughts this past week that I'm curious to find the answers to. Sorry if they're not appropriate here and would better go int he Friday thread; if that is the case I can delete and repost then:

  ---

  **Temporarily Fireproofing Houses**

  A bunch of homes near-ish to me in N. CA have been devastated by wildfires, and the other day I had a thought: with forewarning is it possible to prevent your house from burning down in some sufficiently slowly encroaching forest fire by covering it in a thick fire-retardant tarp and then maybe soaking the tarp through with water? Stake it down so it doesn’t blow off, even even a little bit -- to prevent gas exchange? Naively it seems like a few thousand dollars could buy something that can be deployed in <1h and provide a layer of protection when you know the fire’s coming. Googling around it looks like things like this *are* available, e.g. [this](http://www.firezat.com/info.html) or [this](https://www.tarpaflex.com/acatalog/avoid-severe-fire-damage-with-flame-retardant-tarps.html) or [this](https://www.popsci.com/scitech/article/2009-06/fireproof-house) (not quite soaked nomex or w/e but far cheaper I reckon). So I wonder why I don’t hear more about this, or see photos of that one house in the neighborhood surrounded by burnt out husks cos it managed to get its fire tarp up. Is it because these systems aren't very reliable? Or fires move too quickly for manual deployment (could an automatic or semi-automatic system work there? press a button and sheets unroll from the roof, or your drone-battalion-with-redundancy takes off, or something)? Or people aren't aware of them, or underestimate their forest-fire risk? I'd like to assess how worthwhile something like this is if I should ever live in an especially fire prone area.

  ---

  **Sexual Consent**

  Given all the recent celebrity sexual misconduct scandals: can we conceptualize sexual consent in an ad-hoc, not-really-rigorous Bayesian decision theoretic framework, where agents could e.g. gradually escalate sexual interaction, obtaining stronger and stronger evidence that their prospective partner is interested/willing (i.e. responses to actions would constitute further evidence)? Gradual escalation would not be “required” in the case of strong initial (“enthusiastic”) consent, enough to overwhelm the prior (which I guess could be specified on an individual-by-individual basis – given your demographic and the demographic you’re interacting with, what is the frequency with which consensual sex occurs or consent is obtained? And maybe wiggled a bit if you’ve e.g. had sex with the person a thousand times already, the most recent of which was yesterday. Also a good place to reemphasize that “uniformative” priors are often pretty bad! Don’t use a discrete uniform prior here! lol). Culture-specific likelihoods could be obtained empirically, e.g. through surveys of the general population – “in instances where you have performed action X, what is the frequency with which you’d have consented to sexual interaction Y”. The input space would be truly vast, though. And another difficulty could be that individual actions are not independent – e.g. there’s temporal autocorrelation w.r.t. smiling, which might be taken as exceptionally weak evidence for sexual consent if smiling is even slightly more probable when consent is present than when it is not. But if someone smiles at you a thousand times over a conversation you don’t get to multiply all those likelihoods – maybe they have a spasmatic facial muscles, or something. Also, interactions between inputs – bundles of behaviors might mean more than the sum of their logs. And between-individual variation in sexual interest-signaling behaviors, too.

  I think the most controversial bit would be the definition of (culture-specific?) loss functions for various actions, as that would require explicit quantification of badness (especially) under action/hypothesis mismatch across a wide range of conditions. Imagine the outrage when someone collapses it to the equivalent of Blackstone’s Ratio for sexual assault! (“better that a thousand consenting adults go sexually unsatisfied than a single dissenting adult be the victim of sexual misconduct” – but of course that’s being done implicitly whenever we make any sort of judgment under uncertainty). Consent could also not be a discrete, binary state, but rather continuously valued, and the likelihood, priors, and loss function would need to accommodate that. It could also be ordinal, thresholded, etc. This seems biologically and socially realistic – someone might suffer more under violation if they’ve mostly consented, or are on the cusp of consenting, rather than in the case where they strongly dissent (e.g. consider the case of kissing your committed partner when they’re really feeling it vs. the case where they’ve got a tummy ache and just want to lie down). 

  And since consent is a two-way street you could also assess the probability with which you yourself give consent, though there you’re privy to much more information re: your internal state. There’s also some question over whether consent is internal or external – e.g. how does the Gettier problem relate to consent status – the nature of legal vs. moral agency, the relation between the parties involved, the intentions of each party, and whether the structure of the loss function can change relating to external circumstance. The loss functions could also be party-neutral – i.e. summing across costs to both parties – but I guess it might be more valid for it to be agent-specific with some tunable “compassion” parameter, since a sizeable fraction of people probably dgaf about hurting prospective partners. Also, consent values aren’t static and presumably change over the course of a series of interactions? – e.g. making out stokes the fires and gets someone randy where they weren’t before. Or do they? How does foreplay fit into the nature of consent? If someone is uninterested in a sexual act at time t but anticipates being interested at t+1, is there an element of coercion at play? e.g. consider “he doesn’t want to have sex with me, but I’m going to *make* him want to”.

  Anyway, some quick googling failed to uncover whether something like this has ever been attempted. But I’m no sexologist and not really familiar with the gender/sexuality studies literature so maybe it’s been tried and failed (also, game/decision theory really isn't my field so I'm probably missing lots of other stuff)? Worm cans aside, would there be any value in such a treatment? Obviously it wouldn’t and shouldn’t see the light of actual application, all models are wrong etc. etc. (and this would be inordinately simple and ad hoc and with a ton of effort *maybe* applicable in an extremely narrow set of circumstances), but it could still serve to build those intuitions and heuristics that get used in real-world decisionmaking.

  ---

  **The Recently Proposed Tax Cuts and Jobs Act**

  A ton of people in my social circles are criticizing this thing in its proposed revocation of tax exempt status to grad school tuition waivers. As a current PhD student it wouldn't affect me too much (I think I fall under 26§117.b/c with a scholarship/fellowship instead of a "tuition reduction", and if not grad student tuition is only ~$14k where I'm at so the marginal burden would be pretty small, especially with the increased standard deduction).

  It looks like PredictIt is giving the following $.3 to the dollar of it passing [the Senate](https://www.predictit.org/Ticker/S.TCJA.2017#data
  ) in 2017, and $.85 to the dollar of it passing [the House](https://www.predictit.org/Ticker/H.TCJA.2017#data
  ). Can't seem to find any more detailed predictions, though, so I'm not sure how these bear on the probabilities of it being passed in 2018, or being amended in some relevant way, but insofar as prediction markets can serve as effective oracles it sounds like it's not quite a done deal yet (the bets aren't conditional, either, but can maybe still give us something of an upper bound). Trumps probably not gonna veto it! lol. How likely is this thing to pass?

  This has also had me wondering -- how much value do people place on the goverment having money/resources? For instance, if by anonymously destroying your own $1 (or material equivalent) you could generate $1X in wealth to give to the gov't, what value would X need to take at the margin for you to happily burn that dollar? (if negative, it would mean paying to destroy gov't wealth). If you're completely indifferent then I guess it can take on any value short of destabilizing the economy (local or global), assuming you'd prefer that not happen.

  I don't think the gov't optimal at allocating and distributing materials in accordance with my own preferences compared to alternatives, but I don't think them antithetical to it. So at the margin my gut says X is somewhere in [10,100].
  ```

  - u/phylogenik:
    ```
    **Veg\*n Cat Food**

    Does anyone know of any good, recent sources for why cats can't be healthy on veg\*n diets? Briefly googling around most of the links I'm seeing are either "I fed my cat GMO-free rainbow farts and organic pixie dust and it lived, laughed, and loved to the ripe age of 45!" or "wildcats eat lots of meat and few veggies. In fact, we know that cats must eat meat because they are *o b l i g a t e* carnivores, which is a *science* word that means they must eat meat. Meet Bob the 2-year-old blind vegan cat who was raised on a diet consisting solely of raw potatoes whose liver is failing and whose muscles are atrophied and whose heart actually just stopped oh shit. Also, nature is metal! Get over it, pussy!". 

    But it seems you can just concoct a high-protein diet with appropriate amounts of bioavailable taurine, arachidonic acid, niacin, retinol, methionine, systine, arginine, lysine, etc. etc. and feed them that. Why haven't there been afaict more longitudinal studies on this? (besides the fact that most consumers dgaf, but you'd think some veterinary researchers would want to pluck a low hanging fruit? "currently there are estimated to be at least XE4 vegan cats in the US whose owners are amenable to feeding them manufactured diets; however, to date no study has systematically investigated the long-term health tradeoffs inherent to commercially sold vegan catfoods. Here, we propose to..."). Googling around it sounds like people really like to cite [this paper](http://sci-hub.bz/10.2460/javma.2004.225.1670), which doesn't really have the right sort of experimental component and, idk, 2 random froofy-sounding vegan catfoods from 2004 seem not-so-exhaustive.

    Most of the recent google scholar hits for vegan + cat are for philosophy papers lol. [This paper](http://www.mdpi.com/2076-2615/6/9/57/htm) from 2016 mentions some RCTs but they're all really old. It does, however, conclude that "Problems with all of these dietary choices have been documented, including nutritional inadequacies and health problems. However, a significant and growing body of population studies and case reports have indicated that cats and dogs maintained on vegetarian diets may be healthy—including those exercising at the highest levels—and, indeed, may experience a range of health benefits. Such diets must be nutritionally complete and reasonably balanced, however, and owners should regularly monitor urinary acidity and should correct urinary alkalinisation through appropriate dietary additives, if necessary." *Animals* seems like a legit journal, though it has a low-ish impact factor.

    Anyway, I've hung out with a lot of small animal vets and it sounds like the consensus among them is that cats should never be fed a veg*n diet, so is that really the case, and if so, is it because there's some strong experimental evidence to suggest that even with all the supplements it's deficient in something important (perhaps even to the extent that their lives are not-worth-living and [euthanasia](http://kittencoalition.org/news-events/statistics/) is the preferable alternative), which is either unknown or prohibitively expensive to produce, or more a belief that the metaphysical origin of a biological substance is important, or what?

    [disclaimer: I don't have a cat and if I did, I'd probably feed it some AAFCO approved Cow-based commercial diet, as I do my roughly cat-sized dog, in the interests of time, cost, and convenience]
    ```

    - u/MagicWeasel:
      ```
      As a regular reader of /r/vegan, the cat food threads there are insane. People act as though it's completely different for a cat to eat meat than for a human to eat meat because ~OBLIGATE CARNIVORES~ like you were saying. I think vegans are so terrified of people thinking they are cat-murderers that they don't think rationally about this. I remember posting in /r/vegan saying "meat is not some magic substance, it is made of atoms like anything else. There's no reason we can't make vegan cat food that meets all their nutrient requirements even if that requires making lab meat". 

      I guess, putting my nutrition student hat on, we probably don't know every single vitamin, amino acid, or fatty acid a cat would need to live a long and comfortable life. So there's a risk that Vegan Cat Soylent is missing some essential item in cat physiology that we don't know about because it's ubiquitous in meat but we don't think to add it to the vegan cat food because we don't know it's essential *for cats* because humans can synthesise it (like we can synthesise taurine but cats can't). But that's just speculation and anecdotally there are cats that do *fine* on a vegan diet, but it could be a long-term deficiency thing, or a "increase cancer risk" thing. Who knows....

      At the end of the day it looks like the main issue with vegan cat food - apart from the lack of long-term studies - is that it seems to alter urine pH and cause urine crystals to form which results in kidney infection. I'm not sure why every brand of vegan cat food doesn't just contain some pH balancer to avoid this, but I'm guessing there's a more in-depth reason. 

      We've got a dog and we feed her a AAFCO approved vegan food. It's much more expensive than cheap dog food but about on par with premium dog food, though I have no illusions that it's probably nutritionally closer to the cheap stuff. 

      The way I look at it personally is a pet eating meat based food would be "responsible" for a few animal deaths (then again, the argument about meat byproducts not contributing much to demand means you could get a cheap mostly-grain-based food?), so even if our dog's diet means that she will die a year earlier than she would have otherwise, from a utilitarian point of view it's better to sacrifice one year of a dog's life than it is to kill a bunch of animals to feed it for 8 years. Plus if you're dealing with rescue dogs, having your dog die sooner (humanely of course) means you can rescue a new dog a year earlier than you would have otherwise. Just to be a bit morbid.
      ```

      - u/callmesalticidae:
        ```
        > I remember posting in /r/vegan saying "meat is not some magic substance, it is made of atoms like anything else. There's no reason we can't make vegan cat food that meets all their nutrient requirements even if that requires making lab meat". 

        Now trending on /r/science: new study suggests that cats literally subsist on murder, and do not, in fact, need to eat meat so long as something dies in their vicinity. 

        (Actually, that's be solvable too, depending on how the death needs to happen. Just take your cat on regular trips to the hospital.)

        >  even if our dog's diet means that she will die a year earlier than she would have otherwise, from a utilitarian point of view it's better to sacrifice one year of a dog's life than it is to kill a bunch of animals to feed it for 8 years. Plus if you're dealing with rescue dogs, having your dog die sooner (humanely of course) means you can rescue a new dog a year earlier than you would have otherwise. Just to be a bit morbid. 

        I love arguments that sound totally off-the-wall and yet...make total sense when you stop to think about them.
        ```

        - u/MagicWeasel:
          ```
          > I love arguments that sound totally off-the-wall and yet...make total sense when you stop to think about them.

          The facebook group "sounds like something brian tomasik would be against but ok" may appeal to you. Well, maybe brian tomasik in general.
          ```

          - u/callmesalticidae:
            ```
            I love Brian Tomasik!
            ```

  - u/ulyssessword:
    ```
    > Temporarily Fireproofing Houses

    Fireproofing usually works something like "This will keep the contents below [temperature that damages them] while in an environment at [likely fire temperature], for [time]".  For example, a safe might be rated to keep paper below 350F for one hour in 1700F surroundings.  I'm eyeballing those safe walls at 2" thick.

    Wildfires are roughly that temperature, and burn for more than one hour, and houses are roughly as flammable as paper.  I don't think that you could get a tarp thick enough to give protection from a wildfire for long enough to matter, while still having it be installable.  They usually stop it kilometers before your house is at risk, or else long after it passes through.
    ```

    - u/phylogenik:
      ```
      Good point! A tarp might stop stray embers from getting through to the underlying house, but if ambient temperatures are hot enough the house may spontaneously without direct exposure to flames or burning materials. The tarp would probably provide only negligible insulation in that case. 

      Is there an intermediate case where it can make a difference, though? The wildfire itself might burn for hours, but do the portions of the wildfire in neighborhoods burn for hours, or do houses surrounding a hypothetical tarped house burn down pretty quickly? If your house is in the middle of a burning forest there's likely nothing that can be done, but ambient temperatures don't seem to have been sufficient to e.g. burn [these houses](https://i.imgur.com/BX7mQRi.png) down. To me it seems intuitive that it was only dint of chance that that right-most intact house survived (e.g. no embers were successfully blown into ignitable material, causing runaway house death), but I don't know anything about fires lol.
      ```

- u/DataPacRat:
  ```
  Good news: As of a couple weeks ago, I have a new CPAP machine, and my blood oxygen isn't dropping to 80% overnight. I have improved mood, drive, and all that mental-functioning stuff.

  My new plan: Take one of my year-old story outline drafts, and use my new drive, and the things I've learned in the past year, to hammer out the unsatisfactory parts, until I have an outline worth turning into actual narrative. The outside view says that, given past experience, I'll manage to write around 90% of a novel before pooping out. My hope is that the CPAP machine will make enough of a difference to get me over that hump.

  Where you come in: If you want to comment on the original outline draft, it's a GDoc that can be found at https://docs.google.com/document/d/1XcgNwELHCU-r7GuYUgDNDDIviThd8Y7Bdto_kMIcmlI/edit . I expect to be doing significant revision, especially to the later, societal sections.

  Wish me luck - even with a fully-oxygenated brain, I'm going to need it. :)
  ```

---

