## Quests and the Intelligence of Hiveminds

### Post:

In [quests](https://forums.spacebattles.com/threads/quest-mechanics-introduction-discussion.642898/), players often vote on the next course of action, and this shapes a story's outcome according to the desires of its active readerbase. Before I got into quests proper, I expected that the quest hive mind would be substantially more competent than the average member, and perhaps more competent than its most capable members. After all, each player brings a different perspective to the table, different skill sets, broader knowledge base, more computing power, and if appropriate delegation is done, improves the knowledge acquisition capacity of the collective. However, after reading some quests (specifically quests whose mechanics tried to incentivise competence in the hive mind) I no longer hold this belief.

&#x200B;

The choice of action at each point is usually decided by [plurality vote](https://en.m.wikipedia.org/wiki/Plurality_voting). This has the advantage of making the decision process more fair and more democratic (which I think is something that is unduly privileged in Western culture and may be a bit of an [applause light](https://www.lesswrong.com/posts/dLbkrPu5STNCBLRjr/applause-lights), but that's neither here nor there).

A major weakness of this is a phenomenon called [bandwagoning](https://en.wikipedia.org/wiki/Bandwagon_effect), when a proposed course of action gains momentum, pulling ahead and due to inertia (and perhaps other social effects) it creates a positive feedback loop which eventually cements the position of that plan as the frontrunner. Furthermore, people aren't that likely to change their vote (for various reasons, after voting others may not return to the thread before voting ends, making an explicit decision makes the decision more salient and raises the bar of evidence required to change it, etc). Once a bandwagon starts it's often irreversible without QM intervention (which may invoke perceptions of bias, partiality, etc) and due to the nature of the quest, bandwagons are very easy to start (often they're one of the first few plans). Due to bandwagoning, the earlier a plan is posted, then ceteris paribus the more likely it is to be adopted.

That said, I'm not sure bandwagons are an inherent weakness of hive minds. It seems to me that the phenomenon could be mechanically alleviated. In [one of the quests I read](https://forums.sufficientvelocity.com/threads/even-further-beyond.45951/) by veteran questmaster [Rihaku](https://forums.sufficientvelocity.com/members/rihaku.5176/), there was a one hour moratorium on voting (I really think it should be substantially longer) after each update to allow players to discuss amongst themselves. This meant that once the moratorium was lifted and plans were posted, those first few plans were likely to have substantial thought behind them, as it was usually those who participated in the pre voting discussion that suggested plans (sometimes the course of action was decided before voting began). This meant that when the bandwagon effect did happen, it was on substantially better plans.

&#x200B;

However, even in the aforementioned quests, there were some vulnerabilities that I perceived that seem substantially harder to overcome. In short, the hive mind seems to be strategically hindered and weaker at committing to long term plans. I am reminded of how [Garry Kasparov beat the rest of the world at chess](https://en.wikipedia.org/wiki/Kasparov_versus_the_World) (my original beliefs about hive minds would have predicted them crushing Kasparov), and I wonder if the above vulnerability didn't have a part to play. Progress in quests is sequential, and the players must make decisions at each step along the way. There is often a goal the players are striving towards. In that sense, quests can be viewed as sequential decision problems. There are often many plausible strategies, and the players may favour different strategies. An explicit strategy is often not feasible as important information is often revealed at each update, so players often don't have enough to go off on, that said, people may have ideas for broad paths they intend to pursue. However, only one decision can be made, and once that decision has been made, certain paths are permanently closed off, but there's no mechanism for the players to commit to a given path. Players make atomic decisions when they should be deciding upon paths, usually operating at the tactical level instead of the strategic level.

It seems to me that a hive mind made of competent individuals (hive minds largely populated by less competent individuals would have many other problems to deal with, but they're not as interesting as the problems that persist even in the best case scenario) may be profitably approximated by a [greedy algorithm](https://en.wikipedia.org/wiki/Greedy_algorithm). At each point the hive mind makes the best choice of action available to them at said point. The hive mind may be substantially more tactically competent than its average member (assuming the decision process is robust to phenomena like bandwagoning and encourages serious discussion of plans) but it's not necessarily strategically more competent. Unlike individual agents, the hive mind lacks the means to commit to a given plan of action (perhaps not inherently, one could conceive of systems designed to let players commit their votes to given plans, but regardless of any such systems to enable commitment, the hive mind would still have more difficulty in commitment than the median member). In this critical capacity (the ability to commit to long term plans of action), it seems that *hive minds are* *inherently less competent than their median members.* The ability to commit to long term plans is an important facet of strategic competence and enables such basic maneuvers as sacrificing short term benefit to reap long term rewards.

As a result of the aforementioned weakness, I suspect that hive minds are usually less strategically competent than their most competent member(s) (assuming competence is normally distributed). I can't really make a call on whether they would be more competent than the median member. I suspect that would be very dependent on the nature of the task and the competence/skill distribution of individual members (if there's sufficiently non overlapping skill sets/knowledge/competence amongst the members of the hive mind, then I expect the aggregation of their individual abilities the hive mind enables would exceed its median member).

&#x200B;

[Another weakness of hive minds](https://www.reddit.com/r/rational/comments/cdiql5/quests_and_the_intelligence_of_hiveminds/etug545/) was pointed out to me by u/nohat; the hive mind cannot trust itself to reliably follow any given long term plan. As the individual members of the hive would be aware of this vulnerability, it would set up incentives that biases them away from long term strategic plays (because they wouldn't expect the hive mind to be able to follow through on them). The hive mind being unable to commit to long term strategy thus becomes a self fulfilling prophecy and may reinforce the perceptions of the hive mind being unable to commit to long term strategy in a vicious cycle. When players are individually biased against long term strategy it would manifest as a collective bias, and this may explain the greedy algorithm approach of hive minds as pursuing the apparent best choice of action in the given scenario is easier to persuade the hive mind to adopt. This may manifest as hive minds with suitable communication mechanisms (I suspect this is a big ask, in particular it would require that the best ideas gain currency) being more tactically competent than the best members.

I wonder if a reputation mechanism would improve coordination of the hive mind. u/ArgentStoneCutter [suggested something similar](https://www.reddit.com/r/rational/comments/cdiql5/quests_and_the_intelligence_of_hiveminds/etu6nzc/). The mechanism doesn't even need to be explicitly used in decision making. Ideally, by providing members with convenient access to the histories of their votes, the players who were right more often may gain increased social cred and thus louder voices.

&#x200B;

The main objection to the above theory I have is the aforementioned match in which Kasparov faced off against the rest of the world. While Kasparov did win, he admitted that the hive mind gave him his toughest match yet. Perhaps that result was in part a feature of chess (apart from the idiosyncrasies of the game, there was a clear competence hierarchy and folks may have deferred to the judgement of those more competent than them), but I don't know enough to make a call on this?

Edit: The world team had access to computer assistance. [From Wikipedia](https://en.wikipedia.org/wiki/Kasparov_versus_the_World):

>The World Team also benefited from an organization known as "The Computer Chess Team" founded and captained by Gordon Swobe. This team used distributed computing to analyze each possible line and make recommendations to the world.

&#x200B;

I feel like I should withdraw my previous reservations in light of the above, but I would appreciate commentary from those more knowledgeable on chess (and those aware of what that level of computing assistance would have meant in 1999).

&#x200B;

#### Questions

* What do you think of the hypothesis that hive minds which use plurality votes are intrinsically hindered strategically?
* What measures do you think could be taken to raise the strategic competence of hiveminds in quests?
* What measures do you think could be taken to raise the strategic competence of hiveminds in general?
* Do you think plurality vote is the best method for making a decision on the path of the hivemind?
   * Why?
   * If No? What methods would you suggest?

&#x200B;

&#x200B;

My tentative plans for improving strategic competence in quests is to adopt a three part voting system.

* A discussion period in which no votes are cast nor plans proposed that lasts several hours.
* A plan proposal period in which plans are proposed but not voted on (plans can also be discussed and refined further) that also lasts several hours. No plans can be voted on during this period.
* A voting period in which players [rank the plans](https://en.wikipedia.org/wiki/Ranked_voting). Only voting takes place in this period (one could raise the threshold of investment by requiring players to rank all plans, but if a sufficiently large number of plans are proposed this would become cumbersome).

### Comments:

- u/IICVX:
  ```
  There's a YouTube video out there about ["why corporations aren't AIs"](https://www.youtube.com/watch?v=L5pUA3LsEaw) that's relevant to the topic, but I can't find it right now. 

  The basic thesis is that a committee is sort of like an intellectual harness. If you have a bunch of people pulling on a cart, the cart can never go faster than the fastest person. Similarly, a committee can never be smarter than the smartest person in it.

  And that's completely ignoring the fact that there's an efficiency loss in having to coordinate all those people.
  ```

  - u/Palmolive3x90g:
    ```
    [This video](https://www.youtube.com/watch?v=L5pUA3LsEaw) by Robert Miles covers the topic and seams to offer similar points. Is it the same one?
    ```

    - u/IICVX:
      ```
      Yup that's the video I was thinking of
      ```

  - u/MugaSofer:
    ```
    A cart can never go faster than the *slowest* person pulling it.
    ```

  - u/DragonGod2718:
    ```
    > Similarly, a committee can never be smarter than the smartest person in it.

    What about all the extra manpower? More knowledge, greater knowledge acquisition ability, more skills, more perspectives, etc? I think committees aren't strategically more competent than the most competent members (perhaps even the median members), but committes would have access to significantly more resources than the lone decision maker.
    ```

    - u/IICVX:
      ```
      I mean sure, and that's why science is increasingly done by large research groups. Thing is none of that really helps with pushing the cart. At best it reduces the weight of the cart. You might go like 5% faster, but not 50%.
      ```

      - u/Law_Student:
        ```
        I think the cart metaphor might not work very well. Unless you're trying to demonstrate that many people can do work that no one person could alone, I suppose.

        I think the biggest advantage of group decision making is that the ability of the group to spot potential blunders or optimizations is additive and far better than any individual, assuming all the individuals (or most of them) in the group are willing to listen to productive suggestions of that nature and alter course accordingly. That is a very big presumption, but if it's not the case then you do not have a good selection of people for making group decisions.
        ```

        - u/DragonGod2718:
          ```
          >Unless you're trying to demonstrate that many people can do work that no one person could alone, I suppose.

          Perhaps that. But mainly it's that the cart can never move faster than the fastest person pulling it.
          ```

          - u/LeifCarrotson:
            ```
            The cart metaphor doesnt work. 

            It's almost the 50th anniversary of the Apollo moon landings. The decision making and engineering thought behind those massive machines was done by a large group of people in under a decade. There were smart people, sure, but not one of them could have even come close to the cumulative centuries of thought, testing, and analysis that were performed by the thousands of people involved in the project. A solitary individual couldn't even get past the "gather background information" stage. They'd be hard-pressed to read just the executive summaries of the reams of reports that were produced, much less make good decisions on them.
            ```

- u/nohat:
  ```
  I've definitely noticed the 'Greedy Algorithm' tendency, particularly in acquisition of power. It does make sense to grab short term benefit, especially when you can't rely upon your future decisions to follow through on long term plans. It's a downside of democracy that's been apparent in real life. One administration can start a long term project, but quite often it gets cancelled by the next administration before it is finished. 

  I've also noticed it in a game I played a long time ago called CyberNations. The democratic alliances were considered unreliable by other alliances because the people in charge would change regularly. Of course that also helped sometimes -- the new leaders could easily brush off past animosities or conflicts with a "that was the old administration." Nearly all the rest were run by relatively few high effort members who also tended to bring a lot of history with each other (good and bad) to the table.

  I'm not really sure how to counter it. Possibly some sort of a trust vote (ie I temporarily imbue X with my vote). Possibly a pre-planning exercise where people vote on long term plans to pursue.
  ```

  - u/DragonGod2718:
    ```
    That the hive mind can't trust itself to follow a given strategy is an important insight I hadn't considered. It sets up incentives away from longterm strategy as the individual players expect such strategies to be less than successful.
    ```

  - u/JusticeBeak:
    ```
    A running list of goals and how they are valued seems like it would encourage people to also consider the long term. 

    > I'm not really sure how to counter it. Possibly some sort of a trust vote (ie I temporarily imbue X with my vote). Possibly a pre-planning exercise where people vote on long term plans to pursue.

    I can imagine each update of a quest having a short period where people simply vote on which longer term goals and strategies are more important to them, after which there is a short moratorium on voting to come up with a plan with the goals in mind, and then a vote on which plan to follow.
    ```

- u/Roxolan:
  ```
  > I'm not sure bandwagons are an inherent weakness of hiveminds.

  Agreed. In fact,

  > The choice of action at each point is decided by plurality vote. 

  is only sometimes true. Various other voting systems are used. You can't completely get around [Arrow's impossibility theorem](https://en.wikipedia.org/wiki/Arrow%27s_impossibility_theorem), but you can still do a much better job than plurality vote.

  E.g. /r/rational darling *The Erogamer* uses a combination of [ranked voting](https://en.wikipedia.org/wiki/Ranked_voting) and [approval voting](https://en.wikipedia.org/wiki/Approval_voting) - and sometimes combines multiple high-ranked options. Strategic voting is far less rewarded (and, at any rate, requires too much calculation for readers to bother with).

  &nbsp;

  It's worth noting that in many quests, long-term strategising doesn't bring much benefit *to the readers*. 

  Sure, the character has a strong preference for a certain long-term goal (say, taking over the world). But a *reader* might only have very mild long-term preferences, with much stronger preferences for some kinds of scenes (say, banter) over others.

  Why pick the smart long-term world-conquering option when you could have a banter scene right now? The "I have successfully taken over the world" scene would be sweet, but not so sweet as to be worth the sacrifice. Plus the questmaster is clearly aiming for that scene, so it'll probably happen eventually anyway.

  And since opportunities to banter come pretty much at random, there's no point in doing long-term planning to maximise *that* either. You just vote "banter" whenever the option shows up.

  (I once again present *The Erogamer* as an example.)

  &nbsp;

  Sorry for only addressing the specific case of quests rather than your higher-level question. Well, this *is* /r/rational.
  ```

  - u/DragonGod2718:
    ```
    I'm aware that misaligned incentives is a problem with quests. I didn't address it because:

    >(hiveminds largely populated by less competent individuals would have many other problems to deal with, but they're not as interesting as the problems that persist even in the best case scenario)

    It may be cheeky to file away a player base whose incentives aren't perfectly aligned with the goals of the quest as less than competent, but after covering bandwagoning, I realised that there were other problems with quests as practiced that didn't seem to be inherent problems and thus I didn't find them as interesting as the kind of problems that persisted when we had an ideal player base.

    &#x200B;

    That said I would look at other forms of voting. I was wondering that stuff like ranked choice would make the voting process more complex (especially if write in plans are accepted, it may become cumbersome), but perhaps the higher threshold for voting would incentivise more intelligent behaviour. I'm now thinking of a three part voting period.

    * A discussion period in which no votes are cast nor plans proposed that lasts several hours.
    * A plan proposal period in which plans are proposed but not voted on (plans can also be discussed and refined further) that also lasts several hours. No plans can be voted on during this period.
    * A voting period in which players rank the plans. Only voting takes place in this period (one could raise the threshold of investment by requiring players to rank all plans, but if a sufficiently large number of plans are proposed this would become cumbersome).
    ```

- u/Hust91:
  ```
  Some time ago [a company](https://unanimous.ai/) did an AMA on reddit where they showcased an automatic "voting system" that they called the [Unanimous AI](https://www.google.com/search?q=unu+ai&client=firefox-b-m&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjOlbzn-LfjAhXvpYsKHY9ZCRMQ_AUIBigB&biw=360&bih=512#mhpiv=12&spf=1563228741539), a swarm intelligence that basically made Quest-style voting more intuitive and more likely to defer to the people with the most information.

  Hypothetically it could be used for Quests.
  ```

  - u/DragonGod2718:
    ```
    Thanks, I'll check it out.
    ```

- u/ArgentStonecutter:
  ```
  I think you're overoptimistic when you suggest a committee is no smarter than the median member.

  Piet Hein wrote a grook about committees, I don't recall the whole thing but the last two lines are telling:

  > _Intelligence makes a difference_
  > 
  > _But stupidity makes a sum._

  One thing that might help would be to weight people's votes by whether choices taken where they voted with the majority had positive or negative outcomes, kind of like the classic matchbox tic-tac-toe engine.
  ```

  - u/DragonGod2718:
    ```
    Well apart from the difference in strategic acumen, a committee would have access to more manpower (higher research ability, more knowledge, more skills, and a differing perspectives). It may be not be that great a strategist, but it should have access to more information than a lone decision maker.
    ```

    - u/anenymouse:
      ```
      But it's also limited by the fact that votes are voluntarily brought up by people, an expert uncertain of the right thing to do in the situation, is trumped by anyone who puts together any vote at all. It also implies that more manpower is a virtue rather than an impediment, what you're describing sounds more appropriate when speaking of a committee whose members are chosen for their expertise rather than anyone who chooses to do so. There's kind of the larger problem not necessarily of bandwagon-ing but that some people can explain their vote in a more convincing way even if the vote isn't the best one available.
      ```

- u/RMcD94:
  ```
  I don't really even understand how this is applicable to quests.

  Hive mind video games yes. 

  But the vast majority of quests don't have failure states. The authors are having fun and so are the audience. There are rarely "best" choices. Whatever choice you choose something will occur and when does that something mean game over no more content ever? 

  The long term is vastly discounted because the voters don't even know if they'll bother reading future updates. Even if there was only a single individual voting almost everything you say would still apply.

  I can't trust that my future self is going to want to keep reading, I can't trust that the author will keep producing content, etc.

  Why not look into the video game community? Which can and do commit to longterm plans, especially with small numbers of people. As the game progresses interest dies down and similarly minded people continue the process. 

  Look into twitch plays pokemon and all the thousands of clones of that.
  ```

  - u/DragonGod2718:
    ```
    Well my opinions were formed from reading quests. :V
    ```

- u/DragonGod2718:
  ```
  One thing that's come out of this is that I'm now more sceptical of collective intelligences becoming superintelligent. At the least it seems doubtful that they would gain strategic superpowers.
  ```

  - u/GeneralExtension:
    ```
    The OP's comments refer to a collective of humans, organized in a particular way. I'm curious how things would turn out for 1) a group of competent players, 2) who hold an election\*, 3) some other system where votes are weighted, probably by past performance (which requires the group to keep track/spell out their goals, etc.).

    \*This is one way of fixing the commitment problem. The obvious objection in practice would probably be the impacts on fun-ness. Coming up with ways to make a "hivemind"/group more effective while still fun would probably be necessary for the method to actually be adopted. The actual issue might be entirely due to things being not taken seriously though.
    ```

    - u/DragonGod2718:
      ```
      What about measures to track reputation. It doesn't need to be a mechanism that is explicitly used in decision making, merely providing the ability for players to see how the history of the results of the other player's votes may lead to those who'd been right more often gaining more social cred and louder voices.
      ```

- u/None:
  ```
  Quests are often intelligent in highly specific ways but are just as often extremely blind to potential problems and focused on short term gains, especially those which are 'rational' quests.  Quest participants specifically do not form a true hivemind.  They are a group of different people with different motivations and different desires.  They may collectively choose a course of action, but that is not the same thing as being a hivemind.
  ```

  - u/CitrusJ:
    ```
    I feel like your definition assumes an executive that organizes and directs the overall actions. Having a hivemind that doesn't have such an executive (ex: straight democratic) would be the same as what's described for quests no?
    ```

    - u/None:
      ```
      I would say the opposite - a democratic assembly is specifically not a hivemind because it has dissonance and dissent.  To me, it isn't really a hivemind if it is not the case that every component is more or less identical to every other component in terms of goals and motivations and so on.
      ```

- u/azatol:
  ```
  The Forge of Destiny / Threads of Destiny quests have a Math Cabal that meets on Discord, and a lot of times they have determined the best choice ahead of time, and usually their choice wins the vote.

  That quest also has an automatic 2 hour wait before anyone can vote, which also helps foster discussion.
  ```

- u/Boron_the_Moron:
  ```
  It amuses/frustrates me that you think Quests would be "better" if the posters always made the absolute bestest, most smartest, most well-informed decisions. I completely disagree.

  Stories are built on characters being idiots. On making mistakes. On failing to think ahead. On being flawed, and limited, and buffeted by desires they may only be dimly aware of. Frankly, I find characters' weaknesses vastly more interesting than their strengths, because that's where drama lies.

  You are not treating Quests like an exercise in collaborative storytelling. You are treating them like an engineering problem. You are trying to optimise away the drama. As far as I'm concerned, having a Quest protagonist make stupid decisions, despite having the intelligence of a whole crowd of spectators driving them, is the system working as intended.

  Because stories where the protagonist always makes the right choices, and comes out of every conflict on top, *are fucking boring.*
  ```

- u/llllll--llllll:
  ```
  the 80% rule probably applies.
  ```

- u/Law_Student:
  ```
  It can help to create a mandatory discussion period before voting begins. It's not a perfect solution, but it's a step in the right direction.
  ```

  - u/DragonGod2718:
    ```
    I mentioned this.
    ```

---

