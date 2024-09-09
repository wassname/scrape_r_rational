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

- u/rineSample:
  ```
  ***Happy Halloween!***

  I just wanted to share this with y'all since I figure y'all would appreciate it. Recently I asked one of my professors this question:

  > My friends and I heard of an interesting game called Odds, a revised version of "truth or dare" that works like this:

  >Some guy dares you to do something. You give a number for how little you want to do something, from 2 to 99. Both people countdown from 3, and the darer (the guy who is daring a challenge) and the dare-ee (the guy being dared and issuing the number) each say numbers smaller than the original number.

  >If the numbers match, the dare-ee has to do whatever they assigned odds to, and if they sum, the darer has to do it.
  So for example if Alice dares Bob to drink some shots or something, Bob gives a number from 2 to 99 (let's say he says 53). Then they countdown from 3.

  >If they both say 22, then Bob has to drink the shots. If both numbers sum to 53 (if Bob says 22 and Alice says 31) then Alice has to do it instead.
  My questions to you are,

  >A) What are the odds that they sum, and

  >B) What are the odds that they match?

  He replied:

  >Of course, the answer to A and B is "It depends on what strategies Alice and Bob use". But what is an optimal strategy?

  >I will assume if Alice performs the task, she receives a penalty Ap (for some Ap < 0) and if Bob does, she receives reward Ar (for some Ar > 0). Similarly, Bob has penalty and reward Bp < 0 and Br > 0. I will further assume that these values are known to both players, and that each player is acting to maximize the expected payout.

  >What happens if the numbers both sum and match? I'm assuming that if the numbers both sum and match, both Alice and Bob perform the task, and receive both the penalty and reward.

  >Suppose Bob has already chosen the first number k. Alice may use some mixed strategy, choosing number 1 with probability a1, 2 with probability a2, and so on, with a1+a2+...+a(k-1) = 1. Similarly, Bob chooses numbers with probability b1, b2, and so on. Alice's expected payout is SUM_x (ax * ((Ap * b(k-x)) + (Ar * bx))). Bob's expected payout is SUM_x (bx * ((Bp * ax) + (Br * a(k-x)))). (That is, sum over all choices of number, the probability that number is chosen, times the expected payout of that choice, which is the penalty times the probability that the opponent chose the corresponding penalty number, plus the reward times the probability that the opponent chose the corresponding reward number.)

  >One obvious Nash equilibrium is for each player to choose each number with probability 1/(k-1). (This is a Nash equilibrium, since no matter what strategy the opponent uses, the expected payouts are the same - SUM_x (ax * ((Ap * (1/(k-1))) + (Ar * (1/(k-1))))) = (Ap+Ar) (1/(k-1)) for Alice (and similar for Bob).

  >There may be other equilibria - Suppose Ar + Ap > 0 and Br + Bp > 0 and k is even. Then there is a Nash equilibrium in which Alice and Bob both choose k/2. Suppose Ar + Ap < 0 and Br + Bp < 0 and k >= 5. Then there is a Nash equilibrium in which Alice chooses 1 with probability 1/2 and (k-1) with probability 1/2. Bob chooses 2 with probability 1/2 and (k-2) with probability 1/2. Each has an expected payout of 0. This is a Nash equilibrium - If Alice chooses 2 or (k-2) with nonzero probability, then the expected penalty will be larger than the expected reward, so the expected payout will be negative. (We can do something similar if k=3, Alice chooses 1 or 3, and Bob always chooses 2.) So in certain situations there is scope for Alice and Bob to coordinate.

  >Which number k should Bob choose? If Br + Bp > 0, he can choose 2 to get a payout of Br + Bp, and if Br + Bp < 0, he can choose 99 to get an expected payout of (Br + Bp)/98 (or perhaps as much as 0, if he can coordinate with Alice as described above). I suspect these choices are optimal.

  >Ok, so which task should Alice choose? If she knows Ap, Ar, Bp, and Br for all the possible tasks she might name, She will want to choose one with Ar + Ap > 0 if she can - worst case, Bob chooses 99 and she gets payout (Ar + Ap)/98. But she may want to choose one in which Br + Bp > 0 as well, to get payout Ar + Ap (after Bob chooses 2). If the positive reward task that maximizes Ar + Ap also has Br + Bp > 0, then great, choose that one. Else, if the task which maximizes Ar + Ap for those tasks in which Br + Bp > 0 is more than 1/98 that for which Br + Bp < 0, then she should choose that one. If all tasks have Ar + Ap < 0, then she should choose one (any one) for which Br + Bp < 0 as well, to get a payout of 0 (after Alice and Bob coordinate to avoid the task entirely). If she can't, then she chooses one which maximizes Ar + Ap to get a payout of Ar + Ap (after Bob chooses 2).

  >With these strategies, I would say:

  >A) They match with probability 0, 1/98, or 1, depending on the specifics of payouts.

  >B) They sum with probability 0, 1/98, or 1, depending of the specifics of payouts.
  ```

  - u/gbear605:
    ```
    I can't comment on the math, but I've heard of a similar game, called the same thing, where person 1 says "Odd are, do [x]" (where x is a thing that person 1 is daring person 2 to do), and person 2 says "1 in [y]", where y is any number, depending on how extreme x is. They then both say a number between 1 and y, and if they say the same number, then player 2 does x. I once saw a 1 in 2,000,000 happen, but that was only because they both guessed 1,000,000.
    ```

  - u/munchkiner:
    ```
    If I were President of the World I would happily sign and approve any proposal that is preceded by a demonstration like that.
    ```

  - u/Zephyr1011:
    ```
    What happens if Bob picks 4 as k and then both pick 2? Unless odds literally means they must pick odd numbers only
    ```

- u/Sailor_Vulcan:
  ```
  Somebody made a dating website for rationalists and I can't figure out how to use it! The instructions don't match what's actually showing up in the window, and I'm getting kind of frustrated with it. I tried using google chrome as well as Microsoft Edge (Internet Explorer). Had the same problem both times.

  Has somebody else been able to get it to work? It doesn't say anything about browser compatibility on the site.

  Thanks!

  https://www.reciprocity.io/
  ```

- u/Dwood15:
  ```
  If anyone reads this, I'd like to know so I can gauge the worth of making posts a day late.

  There was some moderate drama last week on /r/n64 when someone made a post attempting to show that Ocarina of Time was a terrible game. Their opinion was extremely dramatized, and received a lot of attention. Additionally, there was another post that attempted to say that they were being "objective", and their post was also clearly opinion (much more level-headed than the original, but still not 100% correct) it got me thinking anyway.

  How would you go about attempting to prove objectively, the qualities of a game? I know that with knowledge of basic proofs and discrete math, one can determine the truth or validity of most people's claims. I'm going to mull this over for a day or so and post developed thoughts on Friday, I think.

  For the interested, here are the posts:

  [OOT is terrible](https://www.reddit.com/r/n64/comments/59nb36/i_hate_to_say_it_but_honestly_ocarina_of_time_is/)

  [Response: "Objectively" prove it is not terrible](https://www.reddit.com/r/n64/comments/5aif9k/in_response_to_the_ocarina_of_time_is_terrible/)
  ```

  - u/alexanderwales:
    ```
    Opinions are subjective. They cannot be wrong.

    However, with that said:

    * It's possible to have inconsistent opinions. For example, if I say that books with a prime number of pages are the greatest works of literature, then go on to say that *Catcher in the Rye* (with 214 pages) is the greatest work of literature, clearly my opinions are inconsistent (or incompletely expressed).
    * It's possible to disagree with popular and/or critical consensus. For example, the Star Trek: Voyager episode "Threshold" might be my favorite episode of the series.
    * It's possible to misrepresent the views of others, or lie about them entirely. For example, I might say that *everyone* loved "Threshold" -- but this isn't actually an opinion, it's a statement of fact (one which is incorrect).
    * It's possible to be wrong about factual matters, but hopefully we already knew this. Saying a game runs at 60 fps when it really runs at 30 fps is wrong. But it's not actually an opinion.

    You can list factual qualities of a creative work, like number of distinct colors used in a painting, Flesch-Kincaid reading level of a novel, frames per second of a videogame, etc. ... but while these qualities *might* be predictors of whether the average person would find something good or bad, that's more a measure of subjective evaluation than a measure of objective goodness. In which case you might as well just look at the aggregate of customer reviews on Amazon/Metacritic/Steam, etc..
    ```

  - u/ketura:
    ```
    Objectivity for something like games seems to be to be a pipe dream.  The existence of [different player archetypes](https://en.wikipedia.org/wiki/Bartle_taxonomy_of_player_types) means that you're not going to have a game that is everything to everybody, at all.  

    Honestly, hours played is about the only objective metric off the top of my head that will matter, in the long run.  So many other factors are just too nebulous to be able to compare them within social groups, let alone across the Internet. 

    And you can't talk about critiquing OoT without including [egoraptor's Sequelitis on the subject.](https://www.youtube.com/watch?v=XOC3vixnj_0)
    ```

---

