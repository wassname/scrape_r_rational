## SMBC: Bayesian Immortality

### Post:

[Link to content](http://smbc-comics.com/index.php?id=4127)

### Comments:

- u/wtfbbc:
  ```
  Mouseover text:

  >I'm just realizing the Venn diagram for people who know the reference and people who like the joke is a null set.

  As a huge SMBC fan, I admit this is approximately accurate tbh
  ```

- u/worldsayshi:
  ```
  The Bayesian overloader sounds like the internet.
  ```

- u/captainNematode:
  ```
  Hmm, you can still have both finite and infinite "theories" integrate to some trivial slice of probability (and indeed you always do with continuous parameters, since there are infinitely many values between two points).

  It's also very common and helpful to assign probability = 0 to certain values (e.g., what's your prior that a standard deviation is negative?).
  ```

  - u/blazinghand:
    ```
    Things like this fall prey to a certain mistake. This is in the same category of those "mugging" thought experiments. In these experiments, there is someone saying "I'm actually simulating this universe, give me 5 dollars and you'll get 10^10^10^10 happiness" or something. It is then said that even if it's super unlikely this is true, it's not zero, and the happiness value is really high, and asks us how we could logically turn it down.

    The mistake made by the presenter in the comic, and also by people who think the thought experiments about mugging are interesting, is not having [error bars](https://en.wikipedia.org/wiki/Error_bar). For most things that we evaluate, we need to have error bars. It is categorically imperative not to consider probabilities below a certain amount. It is literally self-defeating to evaluate a potential outcome and try to reason about it, if that potential outcome is sufficiently unlikely: spending time evaluating things that are smaller than your ability to measure accurately actually decreases your ability to make good choices.

    If we say "I think the likelihood of this being true is 0.000004 ± 0.000300" about a particular outcome, then we shouldn't evaluate anything based on that outcome at all: our measurement is not accurate enough to distinguish something this unlikely from something that has zero likelihood of truth. 

    So, it's not quite true that "all probabilities must add to 1 in total" when we're making these judgement calls. Instead, we should say that "all probabilities, accounting for error, must add to 1 in total"--and effectively ignore outcomes that are sufficiently unlikely that we can't distinguish them from impossible. In fact, this is what most people do.
    ```

    - u/khafra:
      ```
      Uncertainty about uncertainty, in Bayesian terms, resolves to plain old first-order uncertainty. If you want meta-uncertainty, you need [DST](https://en.wikipedia.org/wiki/Dempster%E2%80%93Shafer_theory) or something like that.

      Of course, unadorned Bayesian reasoning is only epistemic, it doesn't prescribe actions. Most flavors of Bayesian decision theory do have ways to deal with Pascal's Muggings.
      ```

    - u/None:
      ```
      The point of the Muggings isn't actually the thought-experiment, [it's that certain expectations don't actually converge.](https://arxiv.org/abs/0712.4318)

      [And of course, there are ways to just model things differently.](http://polymer.bu.edu/hes/rp-peters16gellmann.pdf)
      ```

    - u/Gurkenglas:
      ```
      If the probability of the likelihood of this being true is greater than zero (and according to how error bars are usually used, even greater than 50%), we should invest a monotonous amount of effort into the hypothesis.

      (I suspect that Pascal's Mugging is defeated by game-theoretic concerns.)
      ```

  - u/Sailor_Vulcan:
    ```
    In that case, how do you *know* that 1+1=2? Is this hypothesis based on evidence, or is it something you just know somehow? I'm pretty sure my prior here is based on the evidence that whenever I have added one thing to another thing in the past I got two things, and whenever I typed 1+1= into a calculator it would always say 2. In order to convince me that 1+1 does not equal 2, I would at least need a fucking shitton of shittons of evidence. Like if you could demonstrate that I had hallucinated whenever I added 1 thing to another thing, and if every time I add one thing to another thing in the next few decades I don't get two things. But my prior probability is overwhelmingly in favor of the hypothesis that 1+1=2. Even if I did see the evidence mentioned above, it would be *extremely hard* to distinguish between 1+1 not equaling 2 and plain old human error, and human error has a MUCH higher prior.

    My prior that a standard deviation is negative? Well, if you can turn a data distribution inside-out, or loop it somehow, so that getting farther away from the mean actually brings you closer...but that would require that math is inconsistent. So really really really REALLY unimaginably low prior.
    ```

    - u/FeepingCreature:
      ```
      "But surely there can't be a LessWrong post about _everything_!"

      Ahem. [How To Convince Me That 2+2=3 - LessWrong](http://lesswrong.com/lw/jr/how_to_convince_me_that_2_2_3/)
      ```

    - u/captainNematode:
      ```
      Eh, I'd say probability is in the model (or the mind, maybe), not the world. The "true" state of affairs is already determined (well, maybe barring some interpretations of QM, or something). You can pick whatever priors you want (or hyperpriors, or hyperhyperpriors, etc.) and go with them for either your model or your mind, including assigning all the probability density to the value "2" when evaluating 1+1. Otherwise, though, you just arbitrarily designate priors (well, you can use the posteriors from earlier analyses, but eventually the turtles have to stop stacking) -- they're not out there in the world for you to discover (hence why they're priors). As for *knowing*, the epistemologists have been arguing that one for ages (and I think you can get more fundamental than 1+1; think stuff like the laws of thought, *A* = *A*, ¬(A∧¬A), etc.).

      If standard deviations permit disagreement, can I fall back to the classic playground "if there are no absolute truths, what about this statement"? As in, you can assign probabilities to probabilities, and if you say a *p* of 0 is impossible, you've effectively assigned a probability of 0 to 0. Consider, for example, trying to determine the fairness of a coin. You'd use a binomial (or Bernoulli) likelihood, and in a Bayesian framework have to assign a prior to its parameter, *p*. Typically you'd define this on an interval between 0 and 1 using whatever distribution you fancy (uniform, beta, etc.). Values outside this interval would then receive zero probability density. You could use a prior distribution that's defined on all the reals if you wanted (and depending on what it is, it might work out ok in practice; a normal centered on .5 with low sd), but that'd be silly.
      ```

- u/OrzBrain:
  ```
  I believe the point of the joke was someone following their highly flawed model to a logically absurd conclusion resulting in death, without stopping to consider that reality might be different than their model. That is, someone having a psychotic break. Or behaving like masses of humans have throughout history regarding religion and war. And that by using the buzzword "Bayesian" this nutjob got people to listen while he gave a lecture about it and then committed suicide on stage. And that afterwards instead of reacting to a death or life threatening injury, one of the "rational" audience spent time defending a competing buzzword.

  Would there be less salt here if he had used the buzzword "Quantum" rather than "Bayesian"? Would you be able to notice the point if you weren't busy defending your favorite buzzword, rather like the audience member in the comic? If the guy had instead given a lecture about how he had figured out how to get into Muslim heaven and enjoy the virgins by stabbing himself with a special knife, and one of the audience had commented after the suicide, "That's why I'm a Christian," would the point of the comic been any different?
  ```

  - u/TexasJefferson:
    ```
    The pattern-match reading of this comic is anti-bayesian. The pattern-match reading of the XKCD bayesianism comic was pro-bayesian. I didn't particularly enjoy either because neither make sense as a commentary about statistics.

    So, at least for me, I think the joke fails to land because it's not an intellectually rigorous poke at the nominal subject (which I was expecting and hoping to be far funnier), not mere partisanship. The equivalent joke about a Christian who thought God would protect him because he lives in the best of all possible worlds and his continued existence is obviously a part of that would also fail for me. (A quantum immortality version might have been more salvageable with a different punchline; I'd have to think of one though.)
    ```

- u/gbear605:
  ```
  One problem is that he is changing the map and assuming that the territory will change with it.
  ```

  - u/SometimesATroll:
    ```
    More like he's drawing trillions of maps that may or may not be the true map and hoping reality get's confused about it.  I'm pretty sure Mr. Weinersmith is not actually proposing that someone attempt this, though.
    ```

    - u/Iconochasm:
      ```
      Instruction unclear, please send paramedics.
      ```

      - u/failed_novelty:
        ```
        Request unclear.  I'm sorry; your new puncture wound is plugged, though.
        ```

    - u/None:
      ```
      That sounds like an UNSONG plot device
      ```

---

