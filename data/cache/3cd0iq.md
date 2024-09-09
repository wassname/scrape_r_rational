## [D] Thread for layman discussion about the AI value alignment problem / AI goal alignment problem (aka MIRI's research)

### Post:

Please help me on what I should think about Machine Intelligence Research Institute and its work.

Let me start by asking a few questions. These are very hard, almost impossible, questions so I'd like you to answer just what kind of thoughts they inspire in your minds:

1. Do you think intelligence can be increased tenfold, thousandfold and so on? What does it mean, exactly, to increase intelligence? Is there a fundamental difference in the brain architecture between high IQ individuals and low IQ individuals?*

2. Currently AI research seems to be a big number of subfields, do you think this will remain so, or will there ever be an all-encompassing theory of intelligence?

3. To what extent can you do useful theoretical research separately from actually building an AI?

Recently there have been a few threads concerning AI's utility functions and it seems you guys could have interesting thoughts about the main problem. It's "the" problem Machine Intelligence Research is working on: how to align a superintelligence with human values, how to make sure that the superintelligence won't spin out of control and tile the universe with smiley-faces or paper clips, how to make sure that it has stable goals even after several cycles of self-modification, so that it remains committed to the original goals it was given to and so on.

It appears to me that there are several individuals here similar to me. I've read Bostrom Superintelligence, and most of the easy material Yudkowsky and others have written about the subject. I've tried to read the more mathy stuff, and it goes above my head, but I'm still trying to make sense of what's happening around these parts. And I think I truly understand the problem and in any case I don't fall into the usual pitfalls media and the general population fall when thinking about this problem. These common pitfalls include: AI suddenly turns evil bypassing all its earlier goals, AI suddenly becomes conscious even though it wasn't programmed this way, or that an AI will magically emerge from the continuation of Moore's law.

[There's a place for more advanced discussion about the problem.](http://agentfoundations.org/) However, I'd like discussion on a more casual level because I don't think everything has been said that can be said about the subject on that level. It's impossible to talk about this subject with people who haven't familiarized themselves with the most basic stuff, but I get the feeling there are people here who understand the problem.

----------------------------------------

*[Robin Hanson thinks that this kind of architectural difference doesn't exist](http://www.overcomingbias.com/2011/07/debating-yudkowsky.html), which according to him makes intelligence explosion improbable. [According to Hanson, intelligence is a collection of extreme amount of simple mental tasks,](http://www.overcomingbias.com/2011/06/the-betterness-explosion.html) therefore talking about intelligence as a simple attribute that can be increased is not sensible. To my mind, Hanson sounds more sensible. When you read the [Wikipedia page about artificial intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence), it seems like knowledge of AI is currently just a big collection of small insights and most advances have happened as a result of the increase in computational power, and from being able to process massive amounts of data. Some kind of grand theory of intelligence seems to be far away.

### Comments:

- u/Transfuturist:
  ```
  >Do you think intelligence can be increased tenfold, thousandfold and so on? What does it mean, exactly, to increase intelligence? Is there a fundamental difference in the brain architecture between high IQ individuals and low IQ individuals?

  Increasing general intelligence means decreasing the complexity costs of the algorithms used in a mind, including architectural changes in the mind itself (on the level of hardware as well as software). No one can currently speak to how efficient the process of GI can become, as we only have a lower bound of humanity's most intelligent individuals, and, as you said, we don't have a generalized theory of GI to estimate a higher bound from.

  Differences in brain architecture between high-IQ and low-IQ individuals don't really matter to determining an upper bound of the efficiency of GI, although you will definitely find them. I believe Einstein had an increased number of connections from the temporal lobe? Anyway, it's not really representative of the plausibility of intelligence explosion, since intelligence differences in humans are the results of fairly tiny differences in brain dynamics, and the brain is the stupidest device necessary to build civilization.

  Intelligence can also be made to mean rationality, as in freedom from biases and using the best predictors and evaluators possible to achieve your goals. In this sense, science itself can be said to contribute to intelligence via the efficiency and accuracy of its resultant tools, and an increase in intelligence would be gained by building a device that relies on those tools instead of the hard-to-reverse-engineer and massively suboptimal tools in the brain. Now it just so happens that some of the tools the brain uses are magnitudes better than any tool we have, but these are mostly in the field of perception and the process of GI itself, although things like self-modification and learning are not the best in either the brain or our current knowledge. If you measure intelligence as the effectiveness with which one gets shit done, then yes, I can imagine a thousandfold improvement in intelligence easily.

  >Currently AI research seems to be a big number of subfields, do you think this will remain so, or will there ever be an all-encompassing theory of intelligence?

  General intelligence itself, which would be formalized in an "all-encompassing" theory of intelligence, is not the entirety of the field of AI. Rather, AI is the study of how to get computers to better do the things that humans can do better than computers. General intelligence as in learning, self-direction, and acting well in a variety of domains, particularly the domain of learning to act well in other domains, is one limited, somewhat stymied field of AI. This is due to the fact that learning depends on perception, which isn't too hot right now.

  Your all-encompassing theory of intelligence will not get rid of AI's subfields, because there are subfields of AI that don't care about GI. However, once a sufficiently advanced GI is made, we will eventually no longer be able to do science faster than it can, so in some essence the field of AI will be unified into the AI itself.

  > To what extent can you do useful theoretical research separately from actually building an AI?

  I'm not sure. However, since safety is starting to come into its own as a cross-cutting concern in AI, the theory will probably direct practical research, and vice versa.
  ```

- u/None:
  ```
  I can give a question that clarifies (1), (2), and (3): *what do you mean by the word "intelligence"?*

  My response is going to be premised on answering that clarifying question with, "Something to do with statistical learning theory and other related theories of cognition-as-uncertain-inference."

  We can then begin answering the numbered questions with a single word: [*compression*](https://hips.seas.harvard.edu/blog/2013/03/12/data-compression-and-unsupervised-learning-part-2/).  Learned computational hypotheses which *compress* the data well, which predict the empirical observations using a hypothesis that takes up less space in memory than other hypotheses, are known to learn more efficiently (to predict well after fewer examples) and to be better-protected from overfitting (mistaking noise in the data for a pattern in the real world).

  Can we find hypothesis classes that compress data more efficiently than others?  Yes, especially if we know something about the data-set we need to learn *before* we formulate our hypothesis class.

  What is the upper limit on data compression in learning algorithms?  The Kolmogorov complexity of some data `x` is mathematically defined to be the *shortest possible* computable representation of `x`, the shortest program that prints `x` and stops.  This then leads to Solomonoff induction, AIXI, and the rest of algorithmic information theory.  Algorithmic information theory, and Shannon information theory as well, thus give us a theoretical framework for characterizing the upper limits of intelligent inference, in terms of how much evidence and CPU time are necessary for reasoning.

  Can there be an intelligence explosion?  Yes, but it would take a sigmoid shape: *eventually*, the agent's compressor would get so damn good that it would approach AIXI/Solomonoff induction, and thus run up against the hard limits reality imposes on anything that wants to act agent-y by shifting information around.  At that point, it would need to look for stronger and more resource-efficient optimization processes than its own superintelligent mind if it wished to push the utility-boundaries of reality even further.  Nonetheless, the gaps in knowledge, memory, and processing speed between an "exploded" and "non-exploded" agent could get so wide that it doesn't matter if the "exploded" agent has hit the flattening portion of its sigmoid, it can still easily wipe the "non-exploded" agent out of the universe (if it so chooses).

  Do real-world agents like humans "explode" in "intelligence"?  Well, actually, I'd say this one is arguable!  One of the largest advantages one gets from a *really good* education is a framework of knowledge that compresses most of one's factual knowledge and sensory experiences very well (like scientific naturalism, for instance), as opposed to learned frameworks that compress very badly (like ancient Paganism).  Learning new frameworks that help to compress established knowledge can make an existing human perceptibly and very significantly "smarter" about their behaviors!

  Is there an underlying structure on how knowledge can be put together into frameworks to compress it efficiently?  Probably: logical implication forms a preorder, so it would seem that at least within a probabilistic framework, preorders of theories would form a kind of optimum: you would know every possible link between everything you know.  It's building them that ranges from hard to incomputable!

  In fact, that's my general verdict on AGI right now: computational tractability is the biggest obstacle today to burning through our buffer of theories of cognition, narrowing it down, and building something that would actually work.  There *are* bunches of theoretical obstacles, but additional researcher-years and experimentation will probably deal with them.  Honestly, if the fucking Halting Problem can fall, it's time to stop thinking the universe can stop us.

  >AI suddenly becomes conscious even though it wasn't programmed this way

  This requires us to believe subjective consciousness is simple enough to happen accidentally, rather than because of evolutionary pressures.

  >how to make sure that it has stable goals even after several cycles of self-modification, so that it remains committed to the original goals it was given to and so on.

  Calude defeated the Halting Problem in 2014, at least in the context of probabilistic reasoning systems.  I spent basically a whole afternoon in shock when I found this out, and I'll spend another one in shock if I manage to *understand* algorithmic information theory on a mathematical level and find that Calude's "Anytime Algorithm" is actually tractable in the real world, unlike many other results in AIT (such as Solomonoff Induction).

  TL;DR: Honestly, spend the five minutes on skeptically evaluating a post rather than just going, "Wow, that was long and used big words!  He must be so smart!"
  ```

- u/justanotherlaw:
  ```
  Here's a decent post summarizing another argument against a possible intelligence explosion: [The Brain as a Universal Learning Machine](http://lesswrong.com/lw/md2/the_brain_as_a_universal_learning_machine/).
  ```

- u/avret:
  ```
  It would seem that a reasonably simple theoretical solution would be to have the ai predict its future actions given some change to its utility function and then evaluate those actions in light of its current utility function, with that resultant utility as the expected utility of any given modification.  Would this not work, or is it too difficult to implement, or...?
  ```

  - u/None:
    ```
    [deleted]
    ```

    - u/avret:
      ```
      Thanks--would implementing some kind of hyperbolic discounting fix that problem?
      ```

  - u/Gurkenglas:
    ```
    You just took the method of [gradient descent](https://en.wikipedia.org/wiki/Gradient_descent) on its source code, then restricted its modifications to the one part of itself (its utility function) where the only way you're going to get any changes is when either your predictor of future actions or your evaluator of actions is still flawed enough that *modifying your utility function* makes you *better at implementing your unmodified utility function*.

    The way this would go wrong is that your code would keep looking for slightly modified utility functions until it finds one, U, where all the neighboring utility functions are worse at achieving U than U is.

    Why did you think U would have anything to do with human values?
    ```

---

