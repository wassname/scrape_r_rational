## [D] Friday Open Thread

### Post:

Welcome to the Friday Open Thread! Is there something that you want to talk about with /r/rational, but which isn't rational fiction, or doesn't otherwise belong as a top-level post? This is the place to post it. The idea is that while reddit is a large place, with lots of special little niches, sometimes you just want to talk with a certain group of people about certain sorts of things that aren't related to why you're all here. It's totally understandable that you might want to talk about Japanese game shows with /r/rational instead of going over to /r/japanesegameshows, but it's hopefully also understandable that this isn't really the place for that sort of thing.

So do you want to talk about how your life has been going? Non-rational and/or non-fictional stuff you've been reading? The recent album from your favourite German pop singer? The politics of Southern India? Different ways to plot meteorological data? The cost of living in Portugal? Corner cases for siteswap notation? All these things and more could (possibly) be found in the comments below!

Please note that this thread has been merged with the Monday General Rationality Thread.

### Comments:

- u/Veedrac:
  ```
  If you've not noticed, GPT-3 has made a bit of a splash after people got the opportunity to play with it. [Here's a good list of the things it has done.](https://github.com/elyase/awesome-gpt3) I've grouped them by category and would encourage people to pay extra attention to the [General reasoning](https://github.com/elyase/awesome-gpt3#general-reasoning) section.
  ```

  - u/alexanderwales:
    ```
    I've been playing with it. It's pretty good. It'll get better with a bigger context window, which is a serious limiter right now, but there are always going to be things that it will have problems with, at least until someone comes along and builds a framework that it can fit inside in order to address some of its issues.

    I'm a bit of a GPT-3 skeptic. I think it's marvelous at what it does, but incredibly limited in a few ways, some of which can be addressed, some of which either can't due to how it was made and what it does, or which will take so much work that no one will invest the time and effort. One of the big issues is that within its enormous corpus are things that we don't particularly want, like bunk science, mis-interpretations, biases, poor writing, etc. Some of that you can overcome with sufficient prompting, but I've noticed a real tendency to regress the longer you let it go on without intervention. At best, that means it ends up talking in tropes and memes, at worst, that means hemming and hawing, going off into tangents, moments of (in-text) confusion, etc. And that's when it's actually working.

    There are definitely some use cases for it, but a lot of what people are saying about it is, uh, quite overblown.

    (I tried "centaur writing" with it, treating it like a co-author, and [this was the result](https://www.reddit.com/r/alexanderwales/comments/hvy8nv/cadmus_centuar_writing_with_gpt3_test/). I don't think that I actually saved much labor though, and likely would have gotten a better, faster result without trying to have GPT-3 "help". Edit: [here's another, unfinished](https://www.reddit.com/r/alexanderwales/comments/hxhqqp/isles_centaur_writing_with_gpt3_test_unfinished/?), with some observations on GPT-3 as a writing partner.)
    ```

    - u/Veedrac:
      ```
      I'm largely uninterested in the fine details of exactly where GPT-3 is, since those are mostly irrelevant over even fairly short time periods. GPT-2 was from 2019, the original GPT was from 2018. Naturally one would expect GPT-4, or something like it, in 2021. I expect we'll see a quadrillion parameter model within five years, or maybe like a 10 quadrillion parameter mixture of experts model, contingent on only fairly modest amounts of funding.

      In particular, consistency is almost irrelevant; if it can solve a problem sometimes, a larger, fine-tuned model will solve that problem reliably. We saw this with GPT-2, where people argued that it was super important how much cherry-picking was taking place in the examples (often as high as something like 1-in-25), and I thought the whole debate was missing the point entirely. If that matters so much just wait for the next version! The key point is that it can do the thing that nothing else could do. A few bits of entropy is nothing. Lo and behold, GPT-3 comes out a year later and does exactly that.

      So the key for me is not what specifically GPT-3 can do to or for humanity, it's that GPT-3 is showing that these models can learn things that seemed out of bounds for models of this sort to learn, like multi-step reasoning (see [math questions](https://pbs.twimg.com/media/EdHuMgsWsAEk-29?format=png&name=large)), zero-shot learning ([‘invent a new word and give its meaning’; ‘use the word tana in a sentence’](https://i.imgur.com/KQSwHnn.png)), and text-encoded logical operations ([‘If a question is "normal" the AI answers it. If the question is "nonsense" the AI says "yo be real"’](https://pbs.twimg.com/media/EdHdZT4UMAASHpN?format=png&name=large)). I already knew GPT-2 could do weak world modelling, so [GPT-3's better modelling](https://www.lesswrong.com/posts/L5JSMZQvkBAx9MD5A/to-what-extent-is-gpt-3-capable-of-reasoning) doesn't surprise me too much (though it's still uncomfortable), but it *should* surprise the AI skeptics. Lots of people were holding that up as an important limitation. One by one the arguments fall.

      Getting it to apply these consistently is a matter of scale. Filtering out the unwanted parts of the corpus is a matter of fine-turning. Losing track should be handled with longer contexts, once that algorithmic problem is fixed.

      Note that AI Dungeon probably doesn't send your input directly to GPT-3, so some of the issues might be down to GPT-3 fighting the format.
      ```

      - u/alexanderwales:
        ```
        I don't personally believe that this is true. Some of the problems will be fixed with larger context windows, or with a better corpus, but some of the problems are fundamental to the approach. Part of the reason for looking at where GPT-3 is at is because it will help you predict the deficiencies that GPT-4 will have, some of which are simply a result of the approach used to build it. Especially with being able to compare GPT-2 and GPT-3, we can see areas where it hasn't shown almost any improvement, and which we would expect there to be not much improvement in scaling up.

        The question of cherry-picking is a crucial one and can't be swept away, because if the AI answers a true/false question right only half the time (no better than chance), then cherry-picking can make it seem like it's *far* more capable than it actually is. That's why the first thing I look at when someone posts GPT-3 samples is how much pruning and cherry-picking they've done: it does fundamentally matter, and just because it's able to do it once doesn't mean that this is a feature of the system that will be (or can be) amplified by changes to the model. It only *might*.

        I do think that there are use cases for it, and ways or places that it will save labor. But as an approach, there are deficiencies that won't be solved simply through a better corpus, fine-tuning, or scaling up. Instead, they'll need to be solved by marrying it to a different approach entirely.

        Edit: In [the paper](https://arxiv.org/abs/2005.14165) there's a whole section on limitations, I'm partly basing my thoughts on that, and my own observations about where GPT-3 has not represented a substantial improvement on GPT-2, and where I don't expect GPT-4 to substantially improve either.
        ```

        - u/Veedrac:
          ```
          > The question of cherry-picking is a crucial one and can't be swept away, because if the AI answers a true/false question right only half the time (no better than chance), then cherry-picking can make it seem like it's far more capable than it actually is.

          But if it answers a reasoning question right, where zero knowledge would imply ~zero chance of correctness, one in ten is already proof that it's capable. You do not get answers to “Name three words that start with the letter F” or “What jobs would you say these men have?” or “Suppose it's a cloudy day in New York City. Suddenly, the clouds all turn to solid lead. Write a story describing what happens next.” by cherry picking from a model that hasn't learned to reason.

          It's true the quality of GPT-3 specifically depends on how much cherry picking is involved (the individual authors aren't rerolling much, but no doubt there's some degree of selectivity in what gets shown), but again that's only relevant if people stop building better models.
          ```

          - u/alexanderwales:
            ```
            It really depends on the specifics. GPT-3 is terrible at rhymes, with no improvement over GPT-2, and my prediction is that GPT-4 won't show any improvement if the primary difference is more parameters, a better corpus, or anything like that. You *could* build a framework around the text output, and select the most-probable word that actually *does* rhyme when you want it to, and thus force GPT-3 into doing end rhymes, which is one of the things I mean by creating frameworks. (Gwern's GPT-3 page [has a long section on attempting to get GPT-3 to rhyme](https://www.gwern.net/GPT-3#rhyming), including a lot of tricks that attempt to induce it.)

            However, if you generate twenty, thirty, or a hundred different endings to a line, you *might* happen upon an actual rhyme, and if you cherry-pick those, then you can make it look like GPT-3 can rhyme, which it cannot. It might know that a noun is called for, or even a noun of a specific length, but it's blind rhymes.

            Similarly, there are cases where GPT-3 will provide a completion that falls within certain bounds, but fails to correctly pick from among the short list of candidates. As an example, it might give completions that are (correctly) an emotion, but not be able to select the *correct* emotion (this is just an example, GPT-3 does kind of okay at very basic emotions). Or it might understand that a name should go in that place, but be no better than chance at supplying *which* name. This is a case in which cherry-picking can make it look much more capable than it actually is, and where increasing the parameters, the fine-tuning, etc. might not actually help it.

            Generally speaking, I've noticed it having quite a few issues with applying adjectives that are correct for the noun they're applied to, but wrong in the context of the scene or what's been previously established about that object (places where the whole text is in the context window, so that's not the issue). Similarly, it doesn't handle negations well (e.g. if you say that someone is not greedy, the model latches onto 'greedy' and disregards the 'not', similarly, it will sometimes include its own negations that don't make sense). These are other places where I'm skeptical that increasing the parameters will be very helpful, since they were definitely problems in GPT-2 as well. They're *also* places where cherry-picking can erase the problems.
            ```

            - u/Veedrac:
              ```
              > GPT-3 is terrible at rhymes, with no improvement over GPT-2,

              But this is because the encoding hides letters from GPT, plus it doesn't hear words, so it has no reference point. I couldn't rhyme if I was deaf and used GPT's alphabet and nobody explained the arbitrary mapping. I don't think this says much about the intelligence of this sort of model, just that we've made its job really difficult in this one instance. The fact it can list words starting with *f* is already impressive.

              > This is a case in which cherry-picking can make it look much more capable than it actually is, and where increasing the parameters, the fine-tuning, etc. might not actually help it.

              These (emotions, choosing names) are things that seem analogous to some of the synthetic benchmarks, and there's a fairly clear trend where larger models do much better and fine-tuned models also do much better. GPT-3 does much better than chance; occasional failures in difficult cases don't imply it can't learn.

              I continue to think it's important to remember that the model has a thousandth the parameters of a human brain and is being trained on the entire breadth of human text. It makes sense that it first learns the shape and statistics of all human and computer languages before it figures out theory of mind. In particular, perplexity is going down on a consistent slope, so it's clearly continuing to learn fine, even if it's not prioritizing specifically those tasks that you'd most like it to do. At some point on this line it figures out the things you're asking, almost by definition; all you've argued is that we haven't passed that point yet.

              Isn't this what one would expect success to look like for a model this small tackling such a difficult task? Asking it to be perfect is basically equivalent to asking for the problem to already be solved. A gorilla's cognitive abilities are also extremely primitive in the measures you're looking at, and yet its brain is an evolutionary neighbour of ours. Surely if we made a model that perfectly emulated a gorilla, we'd want to be very concerned that intelligence is potentially almost solved, even if said gorilla can't rhyme. So it seems to me we should be thinking much more about how an architecture is capable of learning and scaling than about specific tasks it hasn't yet learned.
              ```

  - u/MagicWeasel:
    ```
    I saw an exchange on /r/slatestarcodex i think where someone was insisting it doesn't think or feel and so can't write poetry.

    dude, i fucking love the idea of the algorithm writing poetry (and i mean, it has, and it's good). i am ALL ABOUT the death of the author in writing, and this is an author who was never alive in the first place. it gives you complete utter freedom to interpret the text however you see fit, because there are literally no invalid interpretations. i'm so excited about what this means, becuase as much as things like e.g. Animal Farm are clearly and undeniably based on the Russian revolution, I don't like it when people say "that's not what the author meant by X". 

    The primary relationship is between a text and its reader, not its author. Fuck authors. Long live GPT!
    ```

- u/xamueljones:
  ```
  This is a bit of a random question out of the blue, but I'm wondering what people here think about pre-nups?

  I was talking with someone about this the other day, and they wondering if asking for one would be harmful to their relationship because it implied that they didn't trust their partner.

  I argued back saying that it separated love from money and having a pre-nup doesn't mean you don't trust your partner, but rather it allows you to be able to *build* trust without worries about money tainting the relationship.

  Anyway, I'm curious what people here think of it and whether it should be the default with marriages or not?
  ```

  - u/lsparrish:
    ```
    Regardless of having a prenup or not, the act of asking for one should be beneficial. If they say no, that should give valuable information for understanding where your partner's head is at. In my case, asking for one (but not following through, as I wasn't particularly motivated to do so) opened a conversation about fairness, alimony, child support, financial responsibility, and so on that leads me to trust my wife more.

    Avoiding the relationship being tainted by money is a naive way of putting it, I think. Money influences everything, and relationships especially. Marriage is a financial arrangement in addition to everything else it is. Avoiding it being tainted by miscommunications about money is definitely desirable though.
    ```

---

