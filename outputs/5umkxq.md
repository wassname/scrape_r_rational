## [D] Friday Off-Topic Thread

### Post:

Welcome to the Friday Off-Topic Thread! Is there something that you want to talk about with /r/rational, but which isn't rational fiction, or doesn't otherwise belong as a top-level post? This is the place to post it. The idea is that while reddit is a large place, with lots of special little niches, sometimes you just want to talk with a certain group of people about certain sorts of things that aren't related to why you're all here. It's totally understandable that you might want to talk about Japanese game shows with /r/rational instead of going over to /r/japanesegameshows, but it's hopefully also understandable that this isn't really the place for that sort of thing.

So do you want to talk about how your life has been going? Non-rational and/or non-fictional stuff you've been reading? The recent album from your favourite German pop singer? The politics of Southern India? The sexual preferences of the chairman of the Ukrainian soccer league? Different ways to plot meteorological data? The cost of living in Portugal? Corner cases for siteswap notation? All these things and more could possibly be found in the comments below!


### Comments:

- u/Traiden04:
  ```
  Foldscope.com is an amazing thing which I have put money towards supporting as it will help a large number of people everywhere. I would encourage others to take a look at the site and the people behind the project, as they are an amazing group of people dedicated to helping all of humanity. I found out about the existence of this project from youtube. Here is the link.
  https://www.youtube.com/watch?v=Qf-D1Upn-KU
  ```

  - u/lsparrish:
    ```
    That's pretty awesome. I keep thinking there should be an organized effort to make low cost laboratories (and/or factories), following a bootstrap sequence from an inexpensive starting point.

    One rather crazy thing I found is that it is apparently possible to make a [scanning-tunneling microscope](https://dberard.com/home-built-stm/) using an 80-cent piezoelectric speaker disc and a broken piece of tungsten. There are some additional parts involved (damping out vibrations, moving the needle up to the surface, electronics to move it around and sense the voltage changes), but they were able to get it to resolve individual atoms of HOPG.

    If someone were to combine this with a similarly low cost approach to ultrahigh vacuum, it might be possible to have low cost electron beam lithography, and maybe [Zyvex](http://www.zyvex.com/nano/) style nanotech experimentation.
    ```

- u/CouteauBleu:
  ```
  Quick venting: being team leader in a long term school project is hard and frustrating. STOP MAKING ME CHASE YOU AND POLICE YOU AND GROW SOME RESPONSIBILITY ALREADY.
  ```

  - u/ulyssessword:
    ```
    I appointed myself team leader for a semester-long group project last fall, and it went amazingly well.  I think a big part of it was that I got above-average group members and the prof was good at stricturing the class is a way that facilitated teamwork.

    I limited myself to calling meetings (and laying out what should be done beforehand) taking notes during the meetings, and then distributing the notes after the fact.  It worked well, but wouldn't have helped with a lazy group.
    ```

    - u/CouteauBleu:
      ```
      Yeah, we're in a different setting. The school I'm in encourages a very individualistic "do everything yourself at your own pace" mentality, which is pretty good and attractive for aimless students who come from "Sit down all day and note what the teacher says" environments.

      On the other hand, when you start working as a team, this mentality becomes an obstacle, and you basically have to learn professionalism from the ground up (show up to reunions, communicate about what you're doing, etc). I also think that the school's "You do whatever you want, but we're going to examine your results and not your efforts" policy also encourages students to [A] do everything in last-moment rushes (which is kinda terrible for a long term project with many important-but-abstract first steps) and [B] associate authority and responsibility with strict enforcement, which means that your team's productivity will often be proportional to the team leader's willingness to police everyone.

      It's something I'm thinking about *a lot* lately, especially since I re-read "What Developmental Milestones are you missing" and the associated post about stages of psychological development.

      I'd be interested in u/TK17Studios' opinion on the subject, btw, since you did a series on similar themes (responsibility-building) a while ago.
      ```

- u/ketura:
  ```
  Weekly update on the [rational game](https://docs.google.com/document/d/11QAh61C8gsL-5KbdIy5zx3IN6bv_E9UkHjwMLVQ7LHg/edit?usp=sharing) Pokemon Renegade, as well as the associated engine and tools. [Handy discussion links and previous threads here](https://docs.google.com/document/d/1EUSMDHdRdbvQJii5uoSezbjtvJpxdF6Da8zqvuW42bg/edit?usp=sharing).


  ----


  Wellp, it’s official.  Pokemon Renegade was the overwhelming preference, both here on /r/rational and in Discord, and after weighing everything in the balance, I think that’s the name we’ll go with.  I have created /r/PokemonRenegade and staffed it with some familiar faces as modders, tho it’s still a bit rough around the edges.  It is currently private and may well stay that way for the duration of the project, but if you wish for access simply PM me.  I will be mirroring these weekly updates there, but will continue to post in the off topic thread in /r/rational for the foreseeable future.


  ----


  Work on the initiative (turn order) system continues.  I have a simple turn setup that waits for all involved actors to finish their turn before starting a new round, and it’s easy enough to make different turn logic.  With this system, I will quickly build five different turn orders, and a client that allows you to experiment with each of them:

  1.  Alternating: the most naive approach.  Actor A takes their full turn, and then Actor B, etc.  Speed will be used to determine initial turn order.  Most card games follow this approach.


  2.  Hybrid: the canon Pokemon game approach.  Everyone simultaneously has a planning phase, and then an Execution phase where each turn is resolved sequentially, with the order based on the Speed of the individual actors.  Each turn is a single action.


  3.  Nethack: the turn system used by Nethack (duh).  Speed determines how frequently you take your turn: at the extreme end, a Scyther would take its turn 16 times before a sleepy Slowpoke takes one.  Each turn is a single action.


  4.  Simultaneous: the system I want to get working.  All actors have a simultaneous planning phase, and then all actors execute their plans at once.  How long each action takes is based on the actor’s Speed, so a faster actor can cram more actions into their planned round than slower actors.


  5.  Real-time: basically remove the idea of rounds and have each action take a certain number of ticks, and then play it back in extreme slow-mo, giving the player plenty of time to pause as needed and adjust their action choices.  Might not make it into the prototype due to its UI complexity.


  I believe I’m on track to have a simple utility for people to play around with come next week.  It won’t be pretty, but it should work.  And, as it’s in Unity, I should be able to make a build for all you Mac and Linux users, too.


  ----


  Between the discussions in Discord and the votes placed in last week’s off topic thread, we’ve got the second prototype topic narrowed down to the top three choices:


  1.  Voxel engine

  2.  Spawner/breeding system

  3.  Procedural map generation


  In the /r/PokemonRenegade subreddit, I’ve set up a contest-mode thread for voting for these three options, which will decide which fortnight prototype I begin next Friday.  Please request access to the subreddit and vote there, but if you’re *really* opposed to the idea, I will also count comments (not votes on comments!) in this thread as well.


  ----  

  If you would like to help contribute, or if you have a question or idea that isn’t suited to comment or PM, then feel free to join us [on the #pokengineering channel of the /r/rational Discord server](https://discord.gg/sM99CF3)!
  ```

  - u/Brain_Blasted:
    ```
    Oh boy. Nintendo will DMCA you as soon as they hear of this. Anything with the Pokemon name is attacked once it reaches popularity, and game communities don't seem to have much sympathy when it happens.
    ```

    - u/ketura:
      ```
      Yup, we're aware; that was the main reason the other title was even a contender.  I'm gonna get this to a working state, release it to no fanfare, and move on with my life. The entire point was to get experience balancing complex systems using a known system as a starting point, but I have no delusions of grandeur. Once this is under my belt, I'll go on to make my own horribly complex *original* systems.
      ```

      - u/Brain_Blasted:
        ```
        I see. Good luck to you, my friend.
        ```

  - u/Areign:
    ```
    wow this looks awesome, i hope you manage to take this and run with it because it sounds like a lot of fun.
    ```

- u/DaystarEld:
  ```
  Hey everyone, so a little while back I started [designing an AGI development board game](https://www.reddit.com/r/rational/comments/55o2ah/d_monday_general_rationality_thread/d8cethq/) and documenting my progress in these weekly posts. I've stopped posting because I've mostly stopped developing, and I've mostly stopped developing for one simple reason: I don't know enough about the field to do the work justice.

  Mechanically, I can figure things out to make what I think is an engaging game. I still occasionally design new cards and aspects of the game. But when I say I don't know enough, I mean I literally don't know what to call those cards and aspects.

  Just as an example, I've got a list of cards that can be developed for your AI that fall under "User Modeling." They are, in order, Modeling Dangers, Modeling Beliefs,  Modeling Preferences, Modeling Enhanced Knowledge, and Coherent Extrapolated Volition. Each card that you research and develop gives you more bonuses and lowers the risk of your AI ending the world. Coming up with the costs, the extra effects, things like that, I can do. But to get those names and understand those concepts, I had to research. And that goes for every aspect of the game beyond the basics.

  It's research I don't mind doing, and found educational, but it's also research that took a lot of time that was taking away from my other projects, like Pokemon and Rationally Writing.  So I shelved the game for a bit and tried asking around to see if anyone with that knowledge already, and an interest in board games, is willing to basically look over what I'm doing and answer questions to make sure I'm actually basing my game's design and flavor on real concepts, which is sort of important to me.

  So here I am asking here: if anyone has the extensive knowledge of the AGI field and current research going on in it, and is also interested in spending a few minutes every so often answering emails or chat questions about it, let me know, and maybe I can get this project rolling again!
  ```

- u/None:
  ```
  I know some people here read Quests (either on SV, SB or some other place), so I thought I should point you all to [A Destiny of Strife](https://forums.sufficientvelocity.com/threads/a-destiny-of-strife-a-hollows-quest-bleach.29076/). It's a Quest where you play as a Hollow from Bleach, starting off as a basic one in the city and evolving from there. At the moment, the players have finally hit Adjuchas and are gathering an army to conquer the entirety of Hueco Mundo. 

  I really like the quest because Hollows are, for lack of a better term, soul-eating demons. Yet somehow, the GM for the quest was able to straddle the line between edgy grimderp and dumb whiteknighting, writing a compelling and sympathetic group of sociopathic mass murders. Seriously, it's great. Check it out.

  Anyway, the reason I'm saying this is that one of the players' goals is to create a functioning Hollow Society, akin to Soul Society for those who read bleach. We finally hit the point where we can start designing such a society and started a google doc for it (which I won't link due to brigading reasons; you can find it fairly easily by reading through the story).  

  If anyone is interested in reading about or helping to create a society for soul-eating demons, there's always room.
  ```

- u/blazinghand:
  ```
  Exciting news everyone, about the French election. New polls are in, and with them, new terror and horror about Le Pen's chances for victory. Also included are some more detailed things about the second round:

  From http://cdn1-new-parismatch.ladmedia.fr/var/ifop/16-02-2017.pdf here are some important charts:

  * http://i.imgur.com/nD96Cjz.png

  * http://i.imgur.com/obeToIt.png

  * http://i.imgur.com/XslSATw.png

  * http://i.imgur.com/tsDrPht.png

  So, some sad news: Macron has bled off some votes. Just one week ago it was Le Pen at 26%, Macron at 21%, and Fillon at 17.5%. Now we see Fillon rallying and bringing back some people who liked Macron, as well as as some (but not all) of voters who left him for Bayrou. Hamon and Melenchon are still too low to have a real shot at the run-off.

  It's also interesting to see sureness in votes. Of course, your typical Le Pen voter would never consider changing his mind based on new evidence, or he wouldn't be voting Le Pen in the first place. A majority  (~60%) of Fillon and Melenchon voters are the same way, which makes sense given their radical positions. Hamon's voters are still somewhat on the fence, with half of them saying they may still change their minds, and Macron's voters remain uncertain, perhaps because many of them are UMP defectors, perhaps because Macron is already getting ready to service the banks and people are worried about that.

  Looking at the runoff, you see basically that Macron is unattractive to the far left and right. Half of Melenchon voters would abstain in a Macron-Le Pen runoff. 9% (!!!) would vote for *Le Pen!?* Wow, fuckin populists am I right. Hamon's voters would mostly get in line, with 70% voting for Macron and 6% for Le Pen in a runoff. Macron would supposedly lose 4% of his own voters in a runoff, which is probably the margin of error for this poll. Bayrou's voters would mostly get behind Macron, and Fillon's voters, those that remain at least, would vote 45% for Macron, 26% for Le Pen, and 29% stay home.

  I'm astonished that a quarter of PS voters would stay home rather than help Macron win over Le Pen. Melenchon's guys, though, I get it: Macron is in the pocket of the banks, and this really turns people off. It's interesting to see Bayrou's voters included in this poll. I guess nowadays he has enough of them that you see it happening, but I know little about the guy. Also, I'm surprised that The Greens still haven't put their support behind Hamon, who is pretty good on these things. Usually there's some sort of horse-trading and things are worked out.
  ```

  - u/None:
    ```
    > I'm astonished that a quarter of PS voters would stay home rather than help Macron win over Le Pen.

    Call it the Clinton Inevitability Effect: when your second-choice is viewed as the inevitable winner, you feel more comfortable making a Moral Gesture by not actually helping them get that victory, to Send the Message about how they're disappointing their ideological flank.

    >Melenchon's guys, though, I get it: Macron is in the pocket of the banks, and this really turns people off.

    Well, there's also the fact that most of the Western world has had a *decade* now of bank-dominated austerity politics.  While I personally am a radical socialist, I think that Europe made a *godawful* move by not allowing for any degree of Keynesianism or deficit social democracy within its mainstream this past decade.  And by "godawful", I mean it's empowering the far-right and the Putin pawns.

    You can't hold people down in this kind of social crisis forever and expect that they won't rebel.  You have to give them a rational, mainstream way back towards a decent life.
    ```

  - u/CouteauBleu:
    ```
    > It's also interesting to see sureness in votes. Of course, your typical Le Pen voter would never consider changing his mind based on new evidence, or he wouldn't be voting Le Pen in the first place.

    That's pretty uncharitable. Another viewpoint would be that some voters are pretty sure they won't meet new compelling evidence at all, and that all candidates will mostly stay the same and keep the same positions, stupid debates about colonialism aside.
    ```

    - u/None:
      ```
      >That's pretty uncharitable.

      It's not *that* uncharitable.  Le Pen has been running on the same platform for *years*, while events around her have shifted and changed.  You're either convinced that she's been right all along, or you're not.

      >stupid debates about colonialism aside.

      Wait what?  Is the Left trying to commit suicide again?
      ```

      - u/blazinghand:
        ```
        Not the Left: Macron. He said [(link)](http://www.lemonde.fr/election-presidentielle-2017/article/2017/02/15/macron-qualifie-la-colonisation-de-crime-contre-l-humanite-tolle-a-droite-et-au-front-national_5080331_4854003.html) that the French colonization of Algeria was a "crime against humanity" and that it was "barbaric" in an interview. He went on: "colonization is part of French history. It's a part of the past that we must not shirk away from. We must confront this by apologizing for it to those to whom we did it." roughly translated. 

        The UMP/LR Candidate, Fillon, responded by saying such was "unworthy of a candidate for President of the Republic" and "Not long ago, Mr. Macron found colonization had positive aspects. These statements show us that Emmanuel Macron doesn't have any spine. He simply says that which his listeners want to hear"
        ```

        - u/None:
          ```
          So... there are apologists for colonialism in modern French politics?  And they think they get to tell the center to do like them?
          ```

- u/ToaKraka:
  ```
  *Very* irksomely, the motherboard of my new computer (the only one I've built so far) has died. See [all these one-star reviews](https://www.newegg.com/Product/Product.aspx?Item=N82E16813128651)?

  In addition to ordering a new (non-Gigabyte) motherboard, I also bought copies of the two books that I attempted to discuss [here](http://np.reddit.com/r/rational/comments/2ki3ey). I'll make a detailed post about them after they arrive and I get a chance to re-read them for the first time in *several* years.
  ```

  - u/Magodo:
    ```
    As someone whose graphics card just died, I feel your pain.
    ```

- u/cellsminions:
  ```
  Just moved into a new apartment with my friend, and we want to get either a cat or a small dog, but we have to pick which one and agree on it. I've never owned a pet before, he has. 

  There's a dog park right across from our apartment, and I would assume that dogs are much more loving/fun/active, plus a dog would be a great reason to go on walks since I don't get a great amount of exercise. I'd worry about the dog barking, as the walls are pretty thin.

  An indoor cat seems like it would be a better fit for our small apartment, and I expect they're less work, but every cat I've interacted with seems like a little furry alien with impossible to understand motives.

  We're leaning towards getting a cat once we're all settled in. Anyone have an opinion, or have advice to offer to a first-time pet owner? I've done very little research into what pet ownership involves.
  ```

  - u/zarraha:
    ```
    Get a cat, but make sure it has a good personality.  I grew up with a furry alien cat who didn't let people touch her except in certain circumstances (usually when she wanted food)  She was kind of fun to play with and would attack peoples' feet when they weren't expecting it, but I would have liked to have a cat that I could pet without having to be vigilant so I could dodge when she decided she'd had enough and it was biting time.

    There was a stray cat that sometimes came to our yard who loved being petted.  She was the fluffiest nicest cat around and was so into pets that if you were standing she would get up onto her hind legs in order to rub her head against your hand.  She was also content to just sit in your lap and purr for however long you were willing to sit for.

    For the most part, cats will let you go about doing your own thing and they go about doing their thing.  I would estimate that having a cat is like 30% as much work as having a dog, and 60% as rewarding in what you get out of it in terms of playing together and enjoying its existence.  So definitely the more optimal choice in terms of efficiency, but that's mostly my opinion and not any actual rigorous study.
    ```

    - u/callmebrotherg:
      ```
      > Cats: the Efficient Pet

      I'm never been one for "Dog/Cat owner archetypes" but that is *such* a cat owner thing to say (and I say this as someone who prefers cats over dogs).
      ```

  - u/DRMacIver:
    ```
    How small is your flat and how high is your tolerance for mess? I think it's easy to underestimate how much impact cats actually have on a space, especially if you have to have a litter box for them. (Dogs too I imagine, but I'm more of a cat person and have never owned a dog).

    Also if you do get a pet, consider getting an adult pet from a shelter. Kittens and puppies are adorable, but they're also less predictable in how they grow up than a pet that's already grown and you might e.g. find out that this adorable little kitten you've got grows up to be an adorable big cat with a bladder problem who likes peeing everywhere (source: That wasn't much fun)
    ```

    - u/SvalbardCaretaker:
      ```
      Cats are very low impact mess-wise. All those pics of dogs who destroyed a sofa/pillow/garden? Cats dont do that. You might get a life (or dead) mouse once in a while.
      ```

      - u/DRMacIver:
        ```
        Things cats I have lived with have done, in no particular order:

        * Decided that my sweaters would make a great nest and dragged them all off under a bed
        * Decided that my sweaters were delish and chewd great big holes in them
        * Pissed over all the furniture
        * Pissed on me
        * Vomited all over the carpet
        * Spread their cat litter everywhere
        * Spread their food everywhere
        * Completely destroyed door frames because they make a great scratching post
        * Completely destroyed sofas because they make a great scratching post
        * Knocked over water glasses all over the room (resulting in both water and broken glass) because the foolish human whose glass it was was looking the other way
        * Probably many other things I'm temporarily forgetting

        Cats are low mess if you have a lot of space and they are indoor/outdoor cats (though some of the above comes from indoor/outdoor cats I've lived with too). When you're cooped up in a small flat with a cat that can't get out, they're really not *that* low impact.

        ETA: Just discovered that our cats (who are indoor/outdoor) have vomited all over the dining room table. Thanks cats.
        ```

        - u/SvalbardCaretaker:
          ```
          ...  Well I'll be! I concede the point.
          ```

  - u/GaBeRockKing:
    ```
    Even small dogs will need wildly varying levels of activity depending on breed-- make sure you take that into account.
    ```

  - u/ketura:
    ```
    Cats are much easier, assuming you get one with a good temperament. Self-cleaning, easier to house train, not going to bark their heads off at every random passerby. Disadvantages are the clawing of furniture, more aloof personality, and their ability to get into anything they want.
    ```

- u/CouteauBleu:
  ```
  So I've been thinking a lot about self-awareness and ideas and epistemology and stuff, and through a SSC post I stumbled upon that article: https://vividness.live/2015/10/12/developing-ethical-social-and-cognitive-competence/

  This feels like a big piece of the puzzle. Like, I already knew/suspected/felt some of it, but I've never thought about it as a coherent theory before. And it's like... I feel that if I understood these concepts, it would probably increase my understanding of social situations, philosophy and myself by several orders of magnitude. Anyone here has ever had that impression?

  Also, what do you think of the article itself? Some parts of it sound pretty shaky, but again, I don't remotely understand this enough to tell. It seems to assume, for instance, that people consistently go through each phase one by one, and that a variety of psychological traits (self awareness, relationships, work ethics) can be strongly predicted by what phase they're at.
  ```

  - u/vakusdrake:
    ```
    Yeah a lot of parts seem pretty questionable. There seems to be a common feature in certain kinds of psychological models where the latter "stages" are often highly questionable and more reflections of the authors own opinions on the matter than fundamental facts about the human mind.                              
    I'm also not sure that stage 3 necessarily has to come between stage 2 and 4. It really doesn't seem like that sort of social groupthink has to come between selfish shortsightedness and systematic thinking.

    I think you shouldn't buy to much into the idea that this sort of model will grant you any sort of massive insight. It's just a psychological model and it's the sort that kind of fits the data not the sort that makes testable predictions. Stage 5 is also somewhat vaguely defined and doesn't seem like you could reliably determine someone in that stage with a test.

    Even more established models like Maslow's hierarchy of needs mostly just fit the data and frequently fail to apply to real life (for instance people will often neglect lower levels in pursuit of high level needs).
    ```

    - u/CouteauBleu:
      ```
      > There seems to be a common feature in certain kinds of psychological models where the latter "stages" are often highly questionable and more reflections of the authors own opinions on the matter than fundamental facts about the human mind.

      Oh yeah, I definitely noticed that. There are a few places in the article where the author goes "And this type of thinking is a way people consistently disagree with me and are wrong".

      > I think you shouldn't buy to much into the idea that this sort of model will grant you any sort of massive insight

      Aw man.

      Seriously though, it does feel like a model to explore. There are a lot of ideas (n+1 being mistaken for n-1, the monism-dualism dichotomy) there that resonate with me as patterns I've observed before without putting a name on them, in way Maslow's hierarchy never did (although I guess observing Maslow's hierarchy "in action" is harder than observing patterns in everyday relationships), and I do feel I could make predictions because these patterns are pretty consistent.

      But yeah, stage 5 seems mostly defined as "like 4, except better and without those pesky postmodernist ideas" in the article, and the whole thing seems ironically inflexible, "this is the way things are"; if I'm using the article's language, it's systematic and not fluid, even though the contents of the article explain fluidity is the best thing ever.

      I dunno. Maybe I could find someone who has already refined these ideas, or just take them with a grain of salt ("Trying Too Hard to Fit the Data Into my Model" is a thing).
      ```

- u/narfanator:
  ```
  Holographic 3D printing:
  https://news.ycombinator.com/item?id=13673291

  A real thing that is really occurring. Software-defined hologram printing a paperclip in a single pass.
  ```

---

