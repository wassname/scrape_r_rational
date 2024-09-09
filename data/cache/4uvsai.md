## [RT] Romance - Solving the Dating Problem with the SENPAI Protocol

### Post:

[Link to content](http://sigtbd.csail.mit.edu/pubs/veryconference-paper10.pdf)

### Comments:

- u/Chronophilia:
  ```
  Oh hey, this is my field!

  The problem SENPAI is trying to solve is an elaboration on [oblivious transfer](https://en.wikipedia.org/wiki/Oblivious_transfer) - actually, come to think of it, what this paper calls Aaronson's Protocol is the RSA implementation of oblivious transfer.

  This is all a part of secure multi-party computing - cryptographic approaches for doing calculations on inputs that need to stay secret. It's a fairly new field, and there's some interesting results coming out of it. This paper explains how to calculate A AND B - that's a simple logic gate, and if you take the output of one gate as the input of the next, you can do more complicated things like [AES encryption](https://eprint.iacr.org/2009/614.pdf).
  ```

- u/AmeteurOpinions:
  ```
  >**1. Introduction**

  > The Dating Problem is an extremely difficult computational problem that has plagued humanity since time immemorial. The problem concerns two agents Alice and Bob (or Alex and Bob, or Alice and Beatrice), each of whom may or may not have a crush on the other. Each is initially unaware of the other’s feelings, and if they have a crush, they would like to know whether the other does as well; however, each would like to reveal their crush only if the other shares the interest. This problem is of widespread interest and appli- cability; for example, a solution to the Dating Problem is a hitherto unremarked-on prerequisite for the Stable Marriage Algorithm.
  This problem, once thought intractable, can in fact be solved efficiently using cryptographic methods. A protocol providing security against semi-honest adversaries was pre- sented as early as 2008 in a paper by Scott Aaronson. In this paper, Aaronson suggests that zero-knowledge proofs could be used to remove the semi-honesty assumption; however, this poses serious challenges for any practical implementa- tion of the protocol. We have now augmented Aaronson’s protocol with a few extra protections to create the SENPAI
  protocol, which is efficient, easily-implemented, and maxi- mally resistant against covert adversaries.

  The whole paper is pure gold from start to finish. Someone, anyone, write a romance using these, /r/rational *needs* it.

  Further discussion at [Hacker News](https://news.ycombinator.com/item?id=12170183).
  ```

  - u/xamueljones:
    ```
    I *might* give it a try next month (August) since I will have a lot of free time then. And I always wanted to try writing a rational, romance story.

    No promises on actually completing the story or even delivering a good story.
    ```

- u/Charlie___:
  ```
  > If Trent has been compromised, perhaps  by  a  nation-state  adversary

  TvT
  ```

  - u/PeridexisErrant:
    ```
    Also:

    > it is of course possible for Bob
    to cheat if he has access to a quantum computer ... We observe that no stable relationship exists in this scenario, and reiterate our recommendation of polyamory to resolve issues with group SENPAI exchanges

    or in conclusion:

    > the SENPAI protocol is a significant improvement
    on the dating protocols commonly in use today ... We hope to see significant adoption once a few kinks are ironed out
    ```

    - u/gabbalis:
      ```
      > This  could  be  resolved  if  there  were some way of only performing computation for one’s actual crushes;  the  work  of  [2]  on  covert  two-party  computation may offer a solution, but their paper was kind of confusing and we only skimmed it.
      ```

      - u/PeridexisErrant:
        ```
        TBH that was *too* close to home.
        ```

- u/creatureofthewood:
  ```
  The SENPAI protocol falls prey to the Tinder Problem, in which Bob (it's usually Bob, not Alice, who does this) pre-commits to answering YES in all such interactions in order to ascertain all possible romantic options, choosing the most desirable, and rejecting the excess.
  ```

- u/Anderkent:
  ```
  >Ctrl+f notice

  Very disappointed.
  ```

  - u/Pramxnim:
    ```
    It's actually subtly included in the paper when it talks about including a MAYBE answer. The acronym used to describe this variation of the protocol is SENPAI-MTT, which can be read as "Senpai, mitete!" aka the infamous "Senpai, notice me!" line in Japanese.
    ```

- u/xamueljones:
  ```
  Ha! Reminds me of the [marriage problem](https://en.wikipedia.org/wiki/Secretary_problem). [Here's](http://www.npr.org/sections/krulwich/2014/05/15/312537965/how-to-marry-the-right-girl-a-mathematical-solution) a better, less math-heavy explanation.
  ```

- u/Escapement:
  ```
  The conference has some other interesting papers too - http://sigtbd.csail.mit.edu/ is pretty great overall. Just... really top quality papers.
  ```

- u/Linear_Cycle:
  ```
  People considering writing something based on this (if any exist), consider including something from their reference 2, "Covert Two-Party Communication". The idea of that paper is that there can be a protocol which the parties can execute without knowing they're executing it, and find out it occurred only if it returns 'yes'. Lots of interesting things could be done with this; the paper mentions a hypothetical undercover agent in a terrorist cell who suspects another terrorist of being an agent from a friendly agency.
  ```

- u/None:
  ```
  [deleted]
  ```

  - u/CouteauBleu:
    ```
    I think that's more or less how dating sites work. Well, except that you're matched with strangers whose profile you read, not with personal acquaintances.

    That obvious failure mode is that, if you expect to receive far less 'yes' than you send, your incentive is to defect and send as many 'yes' as you can.
    ```

    - u/Xenograteful:
      ```
      >That obvious failure mode is that, if you expect to receive far less 'yes' than you send, your incentive is to defect and send as many 'yes' as you can.

      That is what actually happens on the dating sites. See:

      [How Tinder “Feedback Loop” Forces Men and Women into Extreme Strategies](https://www.technologyreview.com/s/601909/how-tinder-feedback-loop-forces-men-and-women-into-extreme-strategies/)

      >The data analysis reveals some interesting differences between the sexes. For a start, men and women use entirely different strategies to engage a potential mate on Tinder. Men tend to like a large proportion of the women they view but receive only a tiny fraction of matches in return—just 0.6 percent.

      >Women use the opposite strategy. They are far more selective about who they like but have a much higher matching rate of about 10 percent.
      ```

---

