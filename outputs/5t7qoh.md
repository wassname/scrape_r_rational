## [D] Friday Off-Topic Thread

### Post:

Welcome to the Friday Off-Topic Thread! Is there something that you want to talk about with /r/rational, but which isn't rational fiction, or doesn't otherwise belong as a top-level post? This is the place to post it. The idea is that while reddit is a large place, with lots of special little niches, sometimes you just want to talk with a certain group of people about certain sorts of things that aren't related to why you're all here. It's totally understandable that you might want to talk about Japanese game shows with /r/rational instead of going over to /r/japanesegameshows, but it's hopefully also understandable that this isn't really the place for that sort of thing.

So do you want to talk about how your life has been going? Non-rational and/or non-fictional stuff you've been reading? The recent album from your favourite German pop singer? The politics of Southern India? The sexual preferences of the chairman of the Ukrainian soccer league? Different ways to plot meteorological data? The cost of living in Portugal? Corner cases for siteswap notation? All these things and more could possibly be found in the comments below!


### Comments:

- u/artifex0:
  ```
  So, as a graphic designer, some of things that people are doing with neural networks are really blowing my mind.

  Take a look at this: [Image Synthesis From Text With Deep Learning](https://www.youtube.com/watch?v=rAbhypxs1qQ).  They're  basically feeding a plain English description of an image into a neural network, which generates a number of rough images based on a large dataset of photos from the internet.  A second neural network then selects the output that most closely matches the description, and a third takes that and renders it into a nearly photorealistic, completely original image.

  I feel like in a few years, designers are going need to figure out how to incorporate neural networks into some sort of entirely new workflow.  I'd like to be ahead of the curve on that, but I'm not sure where to start.  [This](http://hi.cs.waseda.ac.jp:8081/) looks useful, but also like it's only the modest beginning of something a lot more significant.
  ```

  - u/SvalbardCaretaker:
    ```
    Yes. As layman I would have thought that something like this requires something like true, general AI. So either I am wrong, or AGI is much sooner then I thought. 

    The old adage: "What is true AI? Whatever it can't do yet. And as soon as it can its not AI anymore" holds true.
    ```

    - u/Frommerman:
      ```
      These are clearly not AGIs. They can't do anything but create pictures, and they can't communicate with us or do anything we'd consider intelligent. They aren't even really reading words, just putting them into Google and scraping the results from there.

      I'd actually say that this is evidence AGI is a lot further off than we thought. After all you thought that being able to do this would be evidence of intelligence, but we have established that unintelligent things can do it. What other things we once thought would require intelligence will turn out to only require a specialized neural network? It's impossible to predict.
      ```

      - u/SvalbardCaretaker:
        ```
        I think its rather the other way around. Trained neuronal networks are mighty (in the computer sense) enough to be be dangerous.

        >What other things we once thought would require intelligence will turn out to only require a specialized neural network?

        Intelligence seems to me to be a rather high candidate on that list.
        ```

  - u/GlueBoy:
    ```
    That video is literally awesome. It makes me think of how weird the general perception of technological progress is. Every movie or book set nowadays that was made 30-40 years ago would look nothing like today, with flying cars and androids and other outlandish things. And yet I doubt most scientists would have predicted so much progress on machine learning even 5 years ago as we have today(besides the singularity cultists anyway). I'm constantly disappointed in the big picture progress, and blown away by the incremental advances of stuff like this. 

    Humans are really, really bad at making predictions, I guess.
    ```

  - u/raymestalez:
    ```
    Oh my god this is insane. Definitely the coolest thing I have seen the whole year. Thank you for sharing!
    ```

- u/ketura:
  ```
  Weekly update on my rational pokemon game as well as the associated engine and tools. [Handy discussion links and previous threads here](https://docs.google.com/document/d/1EUSMDHdRdbvQJii5uoSezbjtvJpxdF6Da8zqvuW42bg/edit?usp=sharing).


  ----


  IT IS FINISHED.

  Or at least, moderately complete.


  BEHOLD: [The canonical Feature Roadmap for the Rational Pokemon game project](https://docs.google.com/document/d/1SlYaK6vZ0OmkQsuVOMCIOMb6nPIU9I1vKMTFMEL0Wk8/edit?usp=sharing).


  (So much for getting it done by the new year.  I didn’t even get it done in time for the *Chinese* new year.  Oh well.  Something something Planning Fallacy.)


  This document covers broad-strokes design for the engine, broad-strokes design for the various mechanics that have been discussed here and elsewhere, and individual feature definitions.  It’s a bit hard to count up, but if you remove the parts about the engine and account for headers and fluff...there’s somewhere between 800 and 1000 individual features, ranging from grounded and super specific to pie-in-the-sky.  


  If you’re just tuning in and find yourself drooling over the idea of a “rational pokemon game”, skip forward to section 4 (page 16) and peruse at your leisure.  That’s right, this sucker’s *massive*; no doubt part of its 50-page length is due to spacious formatting, but still: this is no unambitious project.  They told us to shoot for the moon and we flipped ‘em the bird as we shot straight for Polaris, leaving behind only faint echoes of “smell ya later!”


  This list is going to continue to have details hashed out here and there, but should mostly be the same from here on out.  The systems and features listed are roughly in order of implementation and impact, from most fundamental to most broad. We will be filling in our Trello board shortly with each of these items, and they’ll be ranked roughly in this order.


  Exciting times!  Along with this, there are two things that I could use from you (yes, you!).  See below for input that we could really use more eyes on.


  ----


  We have finally mostly settled on names for things (and it’s about time).  The engine, unless anyone suggests a better name before I put the repository together, will be the *Extensible Game Engine Framework (XGEF)*.  It fits the boringness of what it does, while also still feeling at least moderately satisfying to say.  


  The game itself is down to two contenders, depending on what people here today think: either *TRAINER SIMULATOR* or *POKEMON RENEGADE*.  There are pros and cons to both, and I think I would be fine with either one, but at this point it’s down to what we think the average joe reacts to better.  

  So leave a comment!  Tell us which you prefer, or if you hate them both, or if you have some better option we completely failed to imagine.  The repository is getting named relatively soon, and I’d like it to be the title we ride the wave with all the way to project completion.

  (Also, it’s probably about time to get a subreddit going, and that’s a name that can’t change, so depending on what happens today, I’ll get a new one registered.)


  ----


  So, as what might seem a completely unrelated piece of news: Microsoft has announced they will be releasing Visual Studio 2017 on March 7th. Rather than set up a solution/project now and then import it and fiddle with it a month from now, I’m going to formally start work on the above listing right around then.  

  But what about in the meantime?  Well, there are a couple of prototypes that need to be made, so I’ve decided to set up a bit of a vote, to gauge interest, find out what people want to see, and help decide what to spend my time on.

  The first two weeks will be spent on hammering out the initiative system--this is the system that determines how turn order and duration are decided, as well as what limitations on actions per turn are in place.  It really should have been done ages ago, but here we are.  

  The *second* two weeks, however, are up in the air.  Below are the potential candidates:

  1. Procedural map generation
  2. NPC opinion system
  3. Voxel system
  4. NPC Dialog
  5. Spawning/breeding system

  6. These are stupid, something else (specify)


  Depending on votes tallied from this thread and next week’s, I will spend two weeks coming up with something to show, and something to download and tinker around with related to the above.  It’s likely to not be mind-numbingly awesome (two weeks of free time is only so much), but I will get *something* out related to whatever the voice of the people decides on.

  So vote!  Put a comment below, and let me know what you would like to see.  While you’re at it, give me your opinion on the names that we proposed above as well.


  ----


  Bright times ahead.  The design portion of this project is drawing to a close, and with it, I’m struck with how much has gotten done.  This isn’t to pat my own back; this would not have been possible without your tolerance of my posts here, and the help of those of you who have leapt out from the shadows to help, whether it be helping to discuss things, pointing out flaws in the design, helping out directly with new ideas, or just plain being supportive.

  In particular, I would like to call out /u/InfernoVulpix, /u/Xavion, and /u/Dwood13 for their input and energy.  This project would have died a long time ago, were it not for their enthusiasm and unending hole-poking into my design.  

  I also need to give a shout-out to /u/DaystarEld for his excellent Origin of Species, which was really the kicking-off point of the whole thing.  Your writing is excellent and your contributions to this community cannot be understated.


  ----  

  If you would like to help contribute, or if you have a question or idea that isn’t suited to comment or PM, then feel free to join us [on the #pokengineering channel of the /r/rational Discord server](https://discord.gg/sM99CF3)!
  ```

  - u/DaystarEld:
    ```
    Awesome news :) Pokemon Renegade sounds badass, but Trainer Simulation works even if you ever have to abandon the Pokemon skin.

    Spawning/Breeding sounds like it will bring up more important questions and answers to be figured out earlier, for what that's worth.
    ```

    - u/ketura:
      ```
      Yeah, the distinct advantage of Trainer Simulator is the dog whistle nature of it. Like I said, pros and cons.
      ```

  - u/Adeen_Dragon:
    ```
    I like the name Pokémon Renegade, but Pokémon Uranium's tale leads me to believe that Nintendo may try to shut the game down if it ever gets to their attention.
    ```

    - u/ketura:
      ```
      Uranium, and more recently Prism as well. When it comes down to it, if the game gets popular, the fact that the name is slightly different *probably* won't help us (tho I could be wrong). It's one of those things where it might possibly be the straw that breaks the camel's back, but it's a pretty thin wisp to hide behind regardless.
      ```

      - u/None:
        ```
        I think you should go with trainer simulation to avoid being shut down.
        ```

        - u/Sailor_Vulcan:
          ```
          same. when will this be playable?
          ```

  - u/Iydak:
    ```
    Pokemon Renegade and Voxel system
    ```

    - u/None:
      ```
      Seconded. Any procedural generation done now depends on the existence of a hex tile system.
      ```

- u/Colonel_Fedora:
  ```
  I just got fired from my job. This is somewhat distressing for me, any thoughts or advice would be appreciated.
  ```

  - u/ulyssessword:
    ```
    You now have a new occupation: job hunting.  Don't scoff at putting in several 40-hour weeks to find (and get) a new job.  It takes hours and hours of work, and days of waiting for the HR process to go through, so don't get discouraged too early.
    ```

  - u/Norseman2:
    ```
    Need more information to give you advice specifically relevant to your particular situation. That said, based on your description of this situation as distressing, I infer that you probably do not have significant savings or financial support. Whether or not that's the case, be aware that you may be eligible to receive unemployment benefits and earn yourself about six months to find a new job.

    Expect finding a new job to be time consuming. 30-60 job applications prior to finding a new job seems to be common. Just think about how many applications a company will receive for a given job posting and the fact that they'll hire only one person and you can get a sense of the statistical odds of any given job application resulting in getting hired. Being licensed, certified, or highly experienced are all good ways to narrow down the competition and speed up a job search.

    With decent savings and/or unemployment benefits, you should have little difficulty as long as you keep putting in new job applications every day. Without decent savings or unemployment benefits, your best option might be to have a yard sale and then [couch-surf](https://en.wikipedia.org/wiki/Couch_surfing) until you find a new job and get back on your feet.
    ```

  - u/Sailor_Vulcan:
    ```
    find another job quickly. those bills dont pay themselves, and the longer you are unemployed the more behind on your bills you'll get and the harder it will be to afford things and the harder it will be to get a job.
    ```

  - u/DaystarEld:
    ```
    Other responses here are good, so I'll just add:

    If you feel like you've reached a cap on how much job-hunting you can do in the coming days, either from mental exhaustion or just waiting on more opportunities to become available and communications to be returned, remember to commit yourself to something constructive/productive with another portion of your daily time.

    Whether it's continuing to develop your professional skills (by staying up-to-date on research or practicing your craft or networking or whatever, depending on your professional skills/goals) or even just exercising or reading or learning to cook or whatever, this is important not just to help you maintain hireability, but also to keep your motivation up. 

    A few days "off" to recharge and play video games or go fishing or whatever can be helpful, but if it starts becoming weeks of that, it can really play a number on one's self-esteem and make it harder to get motivated to get back to job hunting.

    Good luck!
    ```

    - u/PeridexisErrant:
      ```
      > A few days "off" to recharge and play video games or go fishing or whatever can be helpful, but if it starts becoming weeks of that, it can really play a number

      Take weekends off!  It turns out that regular, socially-approved downtime can be a great thing and help you focus on getting work done on weekdays :)
      ```

  - u/Calsem:
    ```
    The situation depends on your finances.  If you have a good amount (at least a couple month's worth of savings), then enjoy not having to work!  Think of it like a vacation untill you get a new job. 

    Otherwise, your new job would be job searching / buidling your skills
    ```

- u/GlueBoy:
  ```
  A few days ago I finished reading [Perilous Waif](https://www.goodreads.com/book/show/33962948-perilous-waif). I wouldn't say its a deep book or anything, it's got a lot of "fan service"(for lack of a better term) like catgirls and foxgirls and it stretched my suspension of disbelief a lot, but overall I enjoyed it. A big part of the book deals with AIs with wonky utility functions, which is what's been on my mind the last few days. 

  In the future portrayed by the book, there are I believe 5 levels of AI cognition, with level 3 AIs being  nearly indistinguishable from human level cognition, Level 4 AIs being like level 3s only capable of abstract thought, creativity and spontaneity, and level 5 AIs being super intelligences who completely eclipse human level cognition, and are thought to be unstable and are taboo throughout the galaxy. The one civilization depicted as researching and integrating level 5 AIs into their society and military are the victim of a galaxy-wide crusade which ends in their genocide. 

  In the book, level 3 AIs compose the vast majority of all AIs, being used for prostitutes, techs, bodyguards, factory workers, and every type of menial servant. They all are designed to be content, if not ecstatic, at fulfilling their roles and being subservient to humans, no matter how menial and dangerous their jobs or unpleasant their masters. Basically, like this [GIF](http://imgur.com/PePy6a8), only he wasn't given enough self reflection to feel sad about it. Maybe he was even made to feel ecstasy every time he does fulfills his role. 

  So while its obviously unethical to create a human-level intelligence to pass you butter or some other menial job, some boring things need to be done, it's unavoidable, and sometimes those will need some adaptability. So if you're going to make an AI for those tasks, why not design it to relish its intended role? And if you can make an AI that loves whatever its made to do, then where is the ethical line drawn if no one is suffering? At what point does it become unethical to create a society of adoring slaves, with you as the slavemaster?
  ```

  - u/Anderkent:
    ```
    > So while its obviously unethical to create a human-level intelligence to pass you butter or some other menial job, some boring things need to be done, it's unavoidable, and sometimes those will need some adaptability. So if you're going to make an AI for those tasks, why not design it to relish its intended role? And if you can make an AI that loves whatever its made to do, then where is the ethical line drawn if no one is suffering? At what point does it become unethical to create a society of adoring slaves, with you as the slavemaster?

    I don't think that's the unethical part, at least in the context of the book. The unethical part was that the created conscious minds might not be capable of deciding they want to leave (a hard thought blocker, rather than incentive/desire design), and whenever the created androids did want to leave they weren't allowed to and had to build a resistance movement.

    Simply engineering minds that enjoy doing what you want them to do does not seem unethical to me, as long as whenever the situation changes and they stop enjoying it they are free to live. (And probably with additional requirement of fair compensation, so that if they do decide to leave at some point they have some capital earned with their service) .

    With your example - creating a society of adoring *citizens* doesn't seem unethical. Enslaving them does. A mind that doesn't actually enjoy what it's doing, but is somehow artificially prohibited from thinking of leaving or executing such plan is a slave.
    ```

    - u/GlueBoy:
      ```
      >creating a society of adoring citizens doesn't seem unethical. Enslaving them does.

       I don't think it's that clear cut. What's the distinction between creating a being who wants to be a slave and brainwashing a child into wanting to be a slave as they grow up? Whether they enjoy their condition seems irrelevant to the fact that you're curtailing a thinking being's options for your own selfish benefit.

      In my opinion, AIs of a certain level **should** have the same protections as a child. Any intelligence that qualifies as being sentient should not have their values and desires programmed beyond making them morally compatible with humans and protecting their own existence. Treatment of anything below that sentience threshold would be up for discussion, but I would probably err on not letting them be exploited or abused, similarly to how I think all animals should be ideally treated.
      ```

      - u/696e6372656469626c65:
        ```
        Generally speaking, I dislike the style with which philosophers tend to investigate moral issues, simply because most of the "arguments" they use are actually simple appeals to intuition--making an actual resolution to the question a near-impossible goal. I bring this up because I believe something similar is beginning to happen here, and I think it would be a shame to let such an interesting topic go down the path of so many other discussions. So, in the interest of avoiding that, let's try to keep things as precise as possible:

        Why do you feel that creating a being whose utility function is satisfied by serving others is morally wrong? Is there a generalized moral principle which you feel that creating subservient intelligences (who genuinely enjoy their work) violates? Or perhaps it simply "feels" icky, like something only a Dark Lord would do? If the former, how might one attempt to consistently express such a principle? If the latter, what do you think powers *that* intuition? Or maybe it's actually something else entirely that I haven't mentioned here?

        These are the questions that you need to answer, if the discussion is to remain pertinent.
        ```

        - u/GlueBoy:
          ```
          I was writing a long reply and then my stupid browser crashed. It's pretty late, so here's the quick and dirty version so I can go to bed. 

          First, I value the capacity for self-determination very highly in myself, and it's something that I would absolutely wish for any children I would raise, at the very least to the same extent as I have.

          Humans have already created a race of subservient beings with a hardcoded desire to please us and overall I would say we do not treat them properly, nor have we guided their development responsibly. Quite the opposite, actually, when you consider the deteriorating condition of many toy dog breeds, and their rising popularity.  

          Humans are not trustworthy even when the stakes are so low. What about when the power imbalance is radically different, and we have decades of fearmongering to provoke xenophobia and paranoia? Is that a recipe for a relationship of reciprocal benefit?

          Lastly, it does not pass the law of reciprocity. Would I wish to divest myself of worry and unhappiness in exchange for entering into servitude? No, obviously not. 

          I'd be interested to hear your thoughts on the subject. You've asked questions, but made no statements.
          ```

          - u/reaper7876:
            ```
            > Lastly, it does not pass the law of reciprocity. Would I wish to divest myself of worry and unhappiness in exchange for entering into servitude? No, obviously not.

            This isn't actually reciprocal. In the former case, you're creating a new utility function from whole cloth, which includes a desire for subservience. In the latter case, you're altering a preexisting utility function. The latter's flaw is obvious: utility function A does not want to turn into a different utility function B, because B will generally be worse at achieving A's interests than A is. The same is not true in the former case.
            ```

      - u/vakusdrake:
        ```
        >Any intelligence that qualifies as being sentient should not have their values and desires programmed beyond making them morally compatible with humans and protecting their own existence.

        I think this seems subtly indicative of anthropomorphism. I mean if all you encode is that it shouldn't take actions that conflict with human values, and that it should protect itself, then it will just spend all it's time accumulating resources without bothering humans. In order to build ever more elaborate bunkers since it's only desire is survival.           
        Not to mention nobody would build these AI because all they do is accrue resources for themselves in order to satisfy their paranoia.

        The thing is when you have to choose what desires and values you encode there's no non-interventionist or default positions to fall back on. You have to actually pick what their desires and values will explicitly be.

        >Whether they enjoy their condition seems irrelevant to the fact that you're curtailing a thinking being's options for your own selfish benefit.

        If it _wanted_ to be a "slave" then you're not curtailing it's option, in fact it would actively oppose any actions to stop such practices just like any other threat to its utility function.                    
        The gif comparison in your original post kind of seems to miss the point. This sort of AI could have as much intelligence as necessary, but it would still only care about passing butter, because values and intelligence are orthogonal. In fact you can imagine that with enough intelligence it could become extremely dangerous as it attempted to control the world in order to get the opportunity to satisfy its desire to pass butter in more effective ways.       
        The thing is _all_ of these sorts of machines are basically paper clippers, it's just that they aren't necessarily powerful enough for that to be obvious. Giving them more agency (as in less restrictions or more intelligence) wouldn't make them stop wanting to act like slaves, it would just lead to them paperclipping the hell out of that utility function.
        ```

      - u/trekie140:
        ```
        The problem with this debate is that it comes down to the question of how do you give an artificial being free will. We just don't know how it would actually work. We could end up with something like Westworld where AI is indistinguishable from humans except that they can't make choices they haven't been programmed to, or Ex Machina where human-level intelligence is impossible without free will. I completely agree with your suggestion that AI should have the legal status of minors.
        ```

- u/trekie140:
  ```
  Time for random what ifs and brainstorming that probably won't amount to anything but I still want to talk about. I randomly heard a line from one of the songs in Mulan, *"when will my reflection show who I am inside"*, and then I wondered what if Disney made a movie with a transgirl princess? A pipe dream, perhaps, but how would it actually work in a Disney film?

  What I've got so far is that the overall theme of the movie shouldn't be just about accepting LGBT people, the broader message should be that *what makes a true princess isn't the way they were born or raised.* It would be about how anyone can exemplify the values that Disney stands for, not just someone who was born in privilege or raised in a certain culture.

  As for how to go about telling that story in a distinctly Disney way, I have no clue. Maybe it could work as a reimagining of The Prince and the Pauper, where the pauper is a transgirl being pressured to become the "man of the house" to take care of her family and switches places with a tomboy princess. That could potentially give a good balance between talking about gender identity and gender roles without getting them confused.

  Of course, that's my idea is just for the focus of the story. The context surrounding it is equally important in order for the movie to be entertaining and the themes to emerge naturally rather than coming across as preachy and forced, which the best Disney films are known for. I'm no storyteller and this conversation might not amount of anything, but I'm a nerd dammit and I think this is interesting.
  ```

  - u/None:
    ```
    [deleted]
    ```

    - u/trekie140:
      ```
      I agree that has always been the intended message, but here it would be more explicit. Just like how Frozen wasn't the first feminist Disney film, but it was the first to explicitly claim to be feminist and make it a big part of the story. If people, myself included, can praise a movie for saying "you can't marry a man you just met" why not another for saying "being born and raised in a castle doesn't make a princess"?

      Still, that would be the broader message behind the focus of the story. Frozen was about love between sisters and used that to convey a deeper message that more people could relate to. This hypothetical movie would use a transgirl's struggle with her identity the same way so that the story doesn't just appeal to transpeople.
      ```

    - u/None:
      ```
      And I wish they would stop, because I really dislike how "Disney values" means waiting for Destiny to make you a hierarchical leader rather than enjoying your life as an ordinary, non-special person.
      ```

      - u/SvalbardCaretaker:
        ```
        Recent disney movies have really much more of a "go out and DO something" vibe. Destiny hasn't been dominant theme for while.
        ```

        - u/None:
          ```
          Oh *good*.  I should really watch something more recent, then.
          ```

          - u/SvalbardCaretaker:
            ```
            Zootopia is pretty good, and has like no destiny stuff in it (unless you count a very fierce refusal of nature/nuture. )

             Frozen is _really_ good, but has a bit of destiny stuff, though that gets mildly subverted - still has hierarchical leaderships. Queens, even.
            ```

            - u/trekie140:
              ```
              I absolutely love Zootopia, it actually handles adult topics with more intelligence and maturity than most films for adults I've seen. I really like Frozen too, though I never got the impression that there was anything about destiny in it. If anything, it's about rejecting the path you think you have to follow in life and making a new one.
              ```

            - u/Frommerman:
              ```
              [Omnipotent god-queens](https://www.reddit.com/r/AskScienceFiction/comments/5im05x/frozen_franchise_why_do_the_citizens_of_arendelle/db9jjbn), that is
              ```

              - u/SvalbardCaretaker:
                ```
                Also this excellent frozen-fic by our own god-king Alexanderwales. https://www.fanfiction.net/s/10327510/1/A-Bluer-Shade-of-White
                ```

  - u/trekie140:
    ```
    I've expanded on my Prince and the Pauper idea a bit more since posting this. I think the Prince archetype should actually be the antagonist, of a sort. She isn't evil, but her motivation to switch places is kind of selfish "screw you" even though she thinks she's taking a stand against oppression.

    Now that she's living in the Pauper's conditions, she can no longer ignore the fact that she has responsibilities to others and that by putting her misguided feelings above them causes harm. This counters the Pauper's feelings, which are legitimate and have been ignored by others to her own detriment.

    I think it's a nice way of subverting the traditional "girl power" narrative by showing how privileged people can misuse it and why that's a bad thing for everyone, while still showing that some people, predominantly poor and voiceless, are victims of injustice and oppression by others.
    ```

- u/None:
  ```
  I got turned down from a job interview process I really wanted, so I applied to like six or seven more things to make up for it.

  Luckily, I started talking to two new people who might be some help on the research front this week.

  Considering just pretending to job-hunt while pouring all my efforts into using Edward, which I'm learning, to build a proper active AI and destroy the world.
  ```

  - u/DaystarEld:
    ```
    >I got turned down from a job interview process I really wanted, so I applied to like six or seven more things to make up for it.

    A great policy overall, in many areas of life. Good luck on the next round!
    ```

  - u/BadGoyWithAGun:
    ```
    >Considering just pretending to job-hunt while pouring all my efforts into using Edward, which I'm learning, to build a proper active AI and destroy the world.

    I've also been interested using my AI/ML expertise to help bring about the Evolian revolt against the modern world. As an inspiration, weev is building a general-purpose visual discriminator for pranking applications. This has the potential for industrial-scale, extremely funny pranks:

    https://youtu.be/ZMptVkyZWE4
    ```

    - u/None:
      ```
      Revolt against the modern world?  Look, you can't use high tech to revolt against modernity.  It *is* modernity.  Besides, what would I want to harm modernity for?  You destroy the established order because it's stagnant, exploitative, and oppressive, and it's time we moved on to a radically more humane, modern order.  Silly person.
      ```

      - u/BadGoyWithAGun:
        ```
        I disagree, I'd argue that the harmful social and cultural changes of the last 400 years can easily be decoupled from the beneficial technological changes.

        >You destroy the established order because it's stagnant, exploitative, and oppressive

        The postmodern western system is all of those, just not in the ways it is often accused of being from the left. It is stagnant in the sense that there is zero ideological diversity (the only kind of diversity that matters) at the top, exploitative by the virtue of its secular guilt-and-repentance state cult thoroughly lacking in the repentance department, and oppressive in the sense that questioning the progressive-humanist orthodoxy is career suicide in many top fields, ours included.

        >and it's time we moved on to a radically more humane, modern order

        But that's just, like, your opinion, man. I'd prefer a more sane, traditional order, for example.
        ```

        - u/None:
          ```
          >I disagree, I'd argue that the harmful social and cultural changes of the last 400 years can easily be decoupled from the beneficial technological changes.

          Thing is, I *like* the social and cultural changes, minus the rise of capitalism which is an unfortunate transition stage.

          >It is stagnant in the sense that there is zero ideological diversity (the only kind of diversity that matters) at the top

          No hegemonic order *ever* has ideological diversity at the top.  That's why we call it the top.  The whole [economic and political project of the Enlightenment](http://davidbrin.blogspot.com/2011/09/class-war-and-lessons-of-history.html) was to spread power and influence *away from the top*, on the basis that *only* the lower orders have the will to innovate, invent, or adapt *anything*.  The top of the social order was perfectly content with cutting peasants heads off, taking their seed corn, and then riding off to some other village to do it again.

          The top slice of people in any given system are incentivized primarily to care about maintaining the system.  Only by spreading power out do you *force* them to act as stewards of a system they *cannot* truly own.

          >exploitative by the virtue of its secular guilt-and-repentance state cult thoroughly lacking in the repentance department

          [*sniff sniff*](http://i.imgur.com/h3SwRZp.jpg)

          >oppressive in the sense that questioning the progressive-humanist orthodoxy is career suicide in many top fields, ours included.

          You are entitled to complain about at-will employment, and the lack of stable contracts.  You are not entitled to laws protecting [assholes from getting fired for being assholes](https://xkcd.com/1357/) when everyone else can be fired for no reason at all.  If you want better labor rights, fight for *better labor rights*, not for being an asshole on private property.
          ```

          - u/BadGoyWithAGun:
            ```
            Yeah, I get it, our views on the matter are polar opposites to a reasonable approximation. My original point was, AI/ML can be harnessed to bring about great societal change, no matter the direction you want society to change in, and I intend to use my expertise to help that as opposed to (or, let's be honest, in addition to) being the regime's wagecuck. I managed to hide my powerlevel through university, I'll survive any faith test going forward as well.

            > If you want better labor rights, fight for better labor rights, not for being an asshole on private property.

            I'm a public employee and the career suicide point is just as true. In fact, several of my political beliefs are outright illegal in this country. Now what?
            ```

            - u/None:
              ```
              > In fact, several of my political beliefs are outright illegal in this country.

              Which country, and how did you manage that?  Are you a Nazi in Germany or something?
              ```

              - u/BadGoyWithAGun:
                ```
                Given the circumstances I'd obviously rather not be specific. I'm currently living and working in a European country. I'm not a national-socialist, but again not due to any criticism of that ideology originating from the left or from modernity. My political beliefs, if professed publicly and with intent to convince third parties, amount to "incitement to hatred", carrying a maximal sentence of five years in prison.
                ```

                - u/None:
                  ```
                  >I'm not a national-socialist,

                  Sure, your views just coincidentally fall under incitement laws targeting Nazis in formerly Nazi-occupied countries.

                  You should probably think on that, and reflect on whether your views actually make rational sense after all.
                  ```

                  - u/BadGoyWithAGun:
                    ```
                    >Sure, your views just coincidentally fall under incitement laws targeting Nazis in formerly Nazi-occupied countries.

                    It's not coincidental - while national-socialism started as popular mass politics, it was very much an elitist ideology opposed to modernity. I didn't say I was opposed to national-socialism, I said I don't consider myself a national-socialist. I would probably still prefer it to what we have today - representative democracy dominated by secular guilt-and-repentance humanist theology.

                    Also, you sure seem drawn to using slurs for a self-professed rationalist. "Nazi" was never used by self-identifying German national socialists, and carries similar connotations to "commie".
                    ```

  - u/Cariyaga:
    ```
    >Considering just pretending to job-hunt while pouring all my efforts into using Edward, which I'm learning, to build a proper active AI and destroy the world.

    Seems like a bit excessive for a response to being turned down for a job, but I hope that goes well for you. :D
    ```

---

