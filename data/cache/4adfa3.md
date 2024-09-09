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

- u/Shadawn:
  ```
  Some time ago (during preparation to our slowly-ongoing DnD campaign) we had a discussion about Animate Dead. I pointed out that this spell offers cheap manual labor (almost free, if I will be able to cast it with no material component by applying different spell). GM said that this spell is Evil, and my Chaotic Good character shouldn't aim to use it. We discussed what exactly makes the spell evil, and it turned out that it directly affects souls. This is experimentally testable - if you Animate Dead someone's corpse, you can't raise him from death.

  This prevents truly Good charracter from using Animate Dead for manual labor (or tactical advantage), but makes it most convenient resurrect-denier. And that's kinda important. In fact, any self-respecting wizard should have all his slain enemies Animated, and their skeletons lying in Bag of Holding. There could even be organizations offering Animating and keeping watch over resulting undead.
  ```

  - u/Cariyaga:
    ```
    You should consider using Speak With Dead to get your subjects' permission to use animate dead to improve the world.
    ```

  - u/blazinghand:
    ```
    Is animate dead really that great of a spell in terms of cost-effectiveness? 250 silver pieces is enough to hire an untrained hireling for 250 12-hour days of labor. Granted, a Skeleton or something could work all night as well, so after 4 months it would have been cheaper to use Animate Dead than to hire a laborer. 

    There are times when something like a Skeleton could be useful-- for example, working underwater-- but just hiring people do to stuff works well, doesn't require magic, won't piss off any local governments, and isn't Evil (assuming you work with alignment stuff). 

    If your goal is, for example, to build a castle, this kind of task takes 5-10 years. It's hard to make it go much faster due to logistical limitations dealing with medieval-era construction tools.  Assuming it takes 500 workers 5 years (let's say 2,000 work days) to make a castle, we're talking 1,000,000 sp, or 20,000 gp-- the cost of a +3 sword. This isn't counting the cost of having some builders and master builder + carpenter like people in there, but it should be a reasonable estimate.

    If you're a level 9 wizard casting animate dead, you can control up to 36 HD of skeletons, or 36 workers. It would take a *long* time for 36 workers to put in 1,000,000 worker-days of effort. 

    Of course the real moral of the story here is that wizards have a [lot](http://paizo.com/pathfinderRPG/prd/spells/stoneShape.html) of [spells](http://paizo.com/pathfinderRPG/prd/spells/wallOfStone.html) that are the same level as Animate Dead that let you do great things. You can always [convince](http://www.d20pfsrd.com/magic/all-spells/g/geas-quest#lesser) someone powerful to help you out and lend you labor.
    ```

    - u/Vebeltast:
      ```
      The big advantage of using skeletons for labor is that they don't require logistical support. Additionally, depending on the reading of the Rules as Written, "they follow the last order given" may mean that they follow it forever, in which case you can basically ignore the control limitations by issuing an order and then detaching from the skeleton. I've seen this done to build computers - rat skeletons do nothing for boolean zero and raise their tail for boolean one, then each rat skeleton's orders are a boolean function of the other rat tails they can see.
      ```

      - u/blazinghand:
        ```
        That rules abuse is useful for an order like "act like a piece of machinery" which will let you turn skeletons into mechanical computer components or land-based waterwheel drivers. This is definitely a use for skeletons that you couldn't use hirelings for.

        A lot of this depends, by the way, on what will cause everyone involved in this campaign to have fun. In the campaign I'm running, the party is basically bringing 20 level 1-3 NPCs with them everywhere they go. The campaign is mostly focused on organization-building, gathering influence, making allies, and dealing with internal intrigue with these NPCs. This is what people find fun, so it's good. There's nothing rules-wise preventing a player from introducing a bunch of skeletons or abandoning an NPC or something, but as a PC before you take an action you want to make sure it won't ruin other people's fun. A PC having a spat with an NPC apprentice could actually be great RP, done right.
        ```

- u/LeonCross:
  ```
  Not sure if this goes here or the off topic thread but:

  Dat AlphaGo.
  ```

  - u/None:
    ```
    [deleted]
    ```

    - u/Vebeltast:
      ```
      > LoL has around 10^30 possible states after champion select... at the moment when network latency makes the game nondeterministic.

      Except that a lot of that state space has a nice clean gradient and a bunch of the rest can be handled with integer programming. I wouldn't be too surprised if the only really hard parts of LoL to learn would be strategic movement and tactical focus. Ability sequencing can be handled by adapting tree search. Builds and items roughly the same, though the evaluation function would be kind of ugly and you might want to steal some chunking from GAs. There's also the fact that LoL players are *way* further from optimality than Go players. I wouldn't be entirely surprised to find that a well-trained LoL bot could seriously mess up a human player just by being able to catch every single last hit and deny, for example.
      ```

      - u/Shadawn:
        ```
        Well, there are no denying in LoL, but yes, well-optimized bots that can dodge every dodgeable projectile and chain disables perfectly could be very dangerous if they had bare minimum of strategic ability. There are tools that assist human players in such ways (they are called scripts), and they are strongly prohibited in part due to efficiency.
        ```

        - u/ZeroNihilist:
          ```
          On the topic of scripts, there's a cheat for DotA 2 that made the front page recently.

          Essentially, the animation state (walking, attacking, casting ability 1, casting ability 2, etc.) of every character is represented in memory. One such animation state is "performing critical attack", which is a separate state from "performing non-critical attack".

          Note that there is an item which grants a chance to perform critical attacks, but only heroes with a native critical ability have a separate animation state.

          One hero, Phantom Assassin, has a particularly potent critical ability. Her ultimate at max level gives her a 15% chance to deal 450% damage.

          The script guarantees criticals by monitoring the relevant piece of memory and cancelling the attack if it detects the "perform non-critical attack" animation state. This means that it will rapidly cycle the random number generator until a critical occurs.

          For a human this would be impossible to perform in practice. Phantom Assassin's attacks in less than 0.1 seconds with her buff active, even without any items that increase her attack speed, and even the lowest human reaction time is above that threshold.

          But a well-optimised bot could get a massive advantage from taking advantage of this and many similar things.

          DotA also uses pseudo-random generation for many random numbers. Essentially, it biases the random variable according to how many failures precede the test. The values are calculated to have the same mean probability, but become linearly more likely after each failure.

          Again, a bot could take advantage of this behaviour, for example to "pre-charge" a critical by waiting until N consecutive non-criticals have occurred to maximise the expected probability of getting at least one critical in the next K attacks (and likewise for dodges, blocks, bashes, etc.).
          ```

    - u/LeonCross:
      ```
      Apparently they're thinking of tackling star craft next. Which should be interesting.

      I'd actually been wondering if Civ 5 would lend itself well to being the first non-perfect info game before I found out.

      Not actually sure which would be more complicated as only an amateur player of both.
      ```

- u/TimTravel:
  ```
  ADHD: what do
  ```

  - u/gabbalis:
    ```
    Meditation helps. So do prescription stimulants, or just coffee, but I assume most people with ADHD already tried that.
    ```

    - u/TimTravel:
      ```
      I do take medication for it, which reminds me: I'd like a quantitative measurement of its effectiveness so I can test myself and find out how long it lasts without just going by intuition. I can't think of a good experimental design though.

      I've tried meditation off and on. I'll try it again.

      Caffeine pills don't work that well for me but they might help for some.
      ```

      - u/gabbalis:
        ```
        There exist apps that test and score your focus supposedly. Might be a good starting point.
        ```

        - u/TimTravel:
          ```
          Yeah. I'm not sure how to statistically separate out the effect of the medication and the effect of practicing the game/app/thing though.
          ```

          - u/Rhamni:
            ```
            One way would be to take the test repeatedly and on several different occasions until retaking it no longer significantly improves your score. And *then* do the comparisons.

            I realize this may be very boring.
            ```

- u/ianyboo:
  ```
  I've read just about all the rational fiction I can get my hands on. Light spoilers since my thoughts here deal with "the end" of these works in general.

  I've read Nearly everything on this list: https://www.reddit.com/r/HPMOR/comments/3f9gly/list_of_stories_similar_to_hpmor/
   I noticed a trend, they end right at the part I most want to see. The characters meet, decide to optimize the world, struggle to overcome all sorts of cool obstacles, figure out a way to defeat the bad guy, or develop a friendly AI, or cure death aaaaaaannnnnnd done. No exploration of what comes next! 

  Don't get me wrong, I love all the stories that detail the lead up to humanity taking that leap into the unknown and presumably utopian future but it would be cool to have a story that takes place ***in that world***. Reading the culture series is the closest I've seen to this kind of setting. Are there others? A bluer shade of white is a great example of coming really close, giving a tease of things to come that sound like a fantastic untold story. 

  Are there just no compelling stories to be told in a utopia? Am I missing the whole point of fiction by wanting to know what happens "after?"

  edit: spelling corrections
  ```

  - u/FuguofAnotherWorld:
    ```
    > Am I missing the whole point of fiction by wanting to know what happens "after?"

    Well the thing is, that once everything is perfect the interesting-ness of the story kinda... dies. Writers are aware of this and tend to avoid the whole shebang, because obviously they want to write compelling stories and perfect worlds are pretty boring. I'm sure there are quite a few stories set in perfect worlds that exist, but most of them are terrible for the aforementioned reasons. If you want to make a story like that work you generally have either be a really, really good writer, (like mister banks) or tell a story at the edges where the utopian society interacts with a non-utopian society. A couple stories you might enjoy:

    [Larger than Worlds:](https://forums.spacebattles.com/threads/larger-than-worlds-a-mass-effect-fanfiction-featuring-transhumanity.369987/) where humanity uploaded themselves and made a Dyson Swarm, then the Mass Effect relays opened. I really love this story by the way, just because it gets so many details *right*.

    [To the Stars:](https://forums.sufficientvelocity.com/threads/to-the-stars-puella-magi-madoka-magica.3927/) by all accounts humanity would have things pretty good in this one as well what with all their massively upgraded bodies and well managed system of AI, if it weren't for the invading space cephalopods. Luckily, they have puella magi on their side.

    [Cruel to be Kind:](https://forums.spacebattles.com/threads/cruel-to-be-kind-si-multicross-thread-iv.310606/) self insert uses dimension hopping power to create multidimensional space empire. Gives populace replicators, universal basic income and 400 year lifespans. Fights wars with various other polities for convincing reasons. Avoids mass uploads and nanobots, but otherwise makes things very nice for the populace.
    ```

    - u/ianyboo:
      ```
      Thank you for the suggestions, I will check out all three. Starting "Larger than Worlds" right now actually :)
      ```

  - u/TennisMaster2:
    ```
    Friendship is Optimal has a coda showing what life is like in the new order, both inside and out; you specifically want a story that only focuses on the new order, and not what it took to get there?

    *The Whims of Creation* by Simon Hawke might fit that criterion if you look at it a certain way.
    ```

---

