## [RT] [HSF] Programmer at Large, Chapter 10: Can we not?

### Post:

[Link to content](http://www.drmaciver.com/2017/04/programmer-at-large-can-we-not/)

### Comments:

- u/None:
  ```
  [deleted]
  ```

  - u/FeepingCreature:
    ```
    It's _exactly_ about the code. It's just the code is shittily documented and runs in people's heads.

    Basically people have been social-coding to their tests without understanding the reasons, and as a result their society is brittle and unreliable.

    I was not on board with the social stuff last week because I didn't see the relevance. I am 100% on board with it now.
    ```

  - u/DRMacIver:
    ```
    > I both dislike how it isn't about the code anymore

    We'll get back to the code. The plan from the beginning was always to mix the two up.

    > he's 

    they're
    ```

- u/FeepingCreature:
  ```
  Arthur continues to have all my hugs and support.

  Remember last chapter when I was like, "okay so this social code is shit but _at least_ it works for them and it seems they have more experience at this than I do"

  I would like to retract that comment

  > And so on – we have about ninety social unity metrics and this group managed to just avoid alerting on every single one of them.

  THIS IS WHY YOU USE FUZZY LOGIC FOR FUZZY SYSTEMS

  An adversarially-trained neural network [edit: for instance!] would have flagged this in a _heartbeat_.
  ```

  - u/None:
    ```
    I think this is one of those *unspoken* rules. It's a system that's pushing the design tolerances, but there's also an implicit understanding among everyone, including those designing the systems, that *this* particular group is okay. Presumably, the group itself has a hand in it too. So you've got the set of sexually active people, who don't want to get flagged, overlapping somewhat with the social engineers, who don't want to have to deal with flagging them. It's also possible that having a sexually active counterculture is a long-term profitable thing compared to the social losses, especially if that also goes with a more nuanced approach to gender than "what's that?" Ambassadors to grounder cultures with heavy gender biases, for example, or a back-up of sexually active adults to keep a trade ship from dying out in a generation due to the artificial wombs failing, a crash landing, or something similar.
    ```

    - u/FeepingCreature:
      ```
      It's more a question of ... "if it's a good thing, then put it in the model!" The one thing worse than running with no checks, is running with checks that are wrong and have to be bypassed.
      ```

  - u/DRMacIver:
    ```
    I think you're currently:

    * Underestimating the difficulty of the alerting problem for complex systems (you can be as fuzzy as you want, but when noise dwarfs signal you have to be *very* selective in what you flag up to a human).
    * Overestimating the difficulty of fooling neural networks
    * Ignoring that the members of the group have full access to the alerting metrics too
    * Assuming that Arthur is the first person to notice this

    (Some of these things will become clearer in the next chapter or two)
    ```

    - u/FeepingCreature:
      ```
      > Ignoring that the members of the group have full access to the alerting metrics too

      It's not that I'm ignoring this, it's that _whoever designed their system_ was ignoring this. (Or, presumably, the entire thing is just a tool of social oppression, but I'm willing to be charitable enough to not immediately conclude this.)

      With a fuzzy, graded system, possibly discretized with random triggers, it _won't matter_ that people have access to the metrics, because there's no threshold to avoid.

      This whole thing seems like it was designed by very old school programmers, who think in terms of discrete, deterministic events and flags. This _barely_ ¹ works for an unthinking adversary like a ship engine; it fundamentally _does not_ work for a human society for exactly the reason you describe.

      Istm the system you want is not an alert system, but a priority queue of concerns. That solves both the spam issue and the threshold problem.

      ¹If you take action whenever a threshold is crossed, you're gonna end up with systems that barely avoid butting up against the threshold in normal operation. (Because otherwise you'd take action and fix it.) That is not a good place to be _even for machines_.
      ```

      - u/DRMacIver:
        ```
        > It's not that I'm ignoring this, it's that whoever designed their system was ignoring this.

        This is basically true. The system is designed more by way of a form of self-awareness for the ship society - it's there to go "Hey, this is a thing you should be aware of that you might not have noticed". It's not designed to be adversary resistant, because the crew are largely presupposed to be on the same side and social problems are presupposed to not be deliberately created.

        There are also special circumstances here that will be made clear later.

        > Or, presumably, the entire thing is just a tool of social oppression

        I'm not sure it's possible to distinguish a sufficiently heavily designed society from a tool of social oppression.

        > The system you want is not an alert system, but a priority queue of concerns. 

        OK, so, spoiler time because I don't really have a good way of answering this without giving bits of the next chapters away.

        [](#s "Such things absolutely exist and are used. The difference between the soft and hard alerting is that when crossing a threshold someone is forced to take notice and do something about it, if only moving the threshold. If you merely trigger a notice that something is a bit odd and a human is forced to look at it, nobody is *required* to do anything about it, and an unofficial conspiracy of silence can be maintained.")
        ```

        - u/FeepingCreature:
          ```
          I AM NOT LOOKING I CAN WAIT I AM A STRONG ADULT.

          _the spoiler... it tempts!_
          ```

          - u/DRMacIver:
            ```
            FWIW it's not much of a spoiler. \*dangles it in front of you\*
            ```

            - u/FeepingCreature:
              ```
              _You're a mean one, Mister DRMacIver!_
              ```

              - u/DRMacIver:
                ```
                In my defence, the sweet wails of anguish from the readers are one of the greatest delights of authorship.
                ```

          - u/xamueljones:
            ```
            I'm not "A STRONG ADULT" at all and cracked within milliseconds.
            ```

- u/Gurkenglas:
  ```
  His next action shall be to fix people evading social metrics by raising review flags probabilistically based on by how much they evade metrics. This problem is much wider than the one he previously solved, which indicates that other people thought of this before, chose not to implement or mention the solution in order to exploit invisibility to social metrics for their own ends, and will shortly be very angry at him.
  ```

  - u/DRMacIver:
    ```
    > His 

    Their

    > next action shall be to fix people evading social metrics by raising review flags probabilistically based on by how much they evade metrics.

    Not to foreshadow too much, but we *did* establish something about Arthur's likely behaviour in this scenario in a recent chapter.
    ```

- u/HeckDang:
  ```
  Keen to read more.
  ```

- u/TheAtomicOption:
  ```
  As someone who thinks the most common Social Justice rhetoric is frequently wrong, naive, and immoral on multiple levels, many of the social dynamics of this story bother me, and at some points it feels almost like an "The SJWs won" distopia. That said, I can more or less accept genderless pronoun BS and whatever else as part of the world-building cultural norms of having *actually* genderless vat grown people for multiple generations. It's mostly fine so far, but I'm really hoping that this doesn't get preachy later in the story.

  I love the coding though, and I reeeeeeaaally want a HUD to help me keep my life in order now. That's totally the Google Glass killer app. Thanks for writing. Can't wait to see where this goes!
  ```

  - u/DRMacIver:
    ```
    > at some points it feels almost like an "The SJWs won" 

    It's definitely not intended as that.

    (Though I will say our politics differ here and leave it at that)

    > this doesn't get preachy later in the story.

    I've no intention to make it any preachier than it's been to date.

    > Thanks for writing. Can't wait to see where this goes!

    Thanks, glad you're enjoying it.
    ```

  - u/Dragonheart91:
    ```
    It's the author's bias coming through. Arthur is female but doesn't identify as female because they live in the dystopian SJW society you just coined and Arthur was never taught that concepts like female or male exist.

    What I'm really excited about here is that apparently our author is about to give Arthur a rude awakening into gender politics from the anti-SJW rebellion. Although that will probably get quashed because the author is on the side of the SJW society so I'm not sure how things will play out.
    ```

---

