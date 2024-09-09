## Writing tool: GPT-2 autocomplete

### Post:

[Link to content](https://transformer.huggingface.co/)

### Comments:

- u/alexanderwales:
  ```
  Tried this on a few upcoming scenes from *Worth the Candle*. Most of it isn't all that useful, as a writer. I think in the current configuration, it would probably mostly help as an unblocker, or maybe a push in some different direction. I didn't find anything that I would keep as an actual next sentence (or sentence fragment), even when testing on descriptive paragraphs, where I would naively think it would be the most useful (e.g. describing the salient features of a room, or helping to set a scene).
  ```

  - u/iftttAcct2:
    ```
    After some thought, I imagine by "unblocker" you meant to help with writer's block. 

    But my first (horrified) thought on reading was that this could be the next phase of Captcha... Completing sentence fragments with internal consistency in order to train this thing's AI.
    ```

  - u/PresentCompanyExcl:
    ```
    Interesting! I wonder if it would be better if it was trained on your style, or modifying a seed text (which may make it stay closer to your style). Perhaps not though.

    Maybe you could up the noise and use it to represent an antimeme (or whatever the correct term is) or a locus in the book . [Some poets used a similar method to make some poetry](https://docs.google.com/document/d/1aX8yafxFtUt3QvLfyaL0VL3YGejGhpNDIeZu_S-oNKk/edit?usp=sharing), and result is interesting. However, I think this applications easier since they were exploring a much less constrained space. In the end, though, it's easy to generate nonsense, and there are many ways to do it.

    Overall it's likely just a fun toy.
    ```

  - u/PresentCompanyExcl:
    ```
    I tried training GPT2 directly on WtC to see how the generated text would look, here's a sample. I used [gpt-2-simple in colab](https://github.com/minimaxir/gpt-2-simple), and the 345Mb model. Let me know if you would like to see more samples or have a play (I can set up a notebook). I'm just a fan of your writing, and curious how writers might use this (if it's useful at all).

    > [200 | 17992.61] loss=2.92 avg=2.63
    >
    > ======== SAMPLE 1 ========
    >
    >     need just be the thing, no grand plan behind it, there doesn’t need to be any.”
    > 
    > “Alright,” said Amaryllis, nodding. “I’ll see if I can find the portal in the game, at which point I will know that it’s not us.”
    > 
    > “If you see the portal,” I said, “You know we’ll take those precautions, that’s more or less what this is.”
    > 
    > “Oh,” said Amaryllis. “You’ll kill our host, and then the hells? That’s not really what the game was supposed to show me, because it wasn’t the thing that the game was supposed to show me: the game was supposed to show me that there were only ten people who could get through the portal. That’s what it shows, but it’s a stupid, stupid thing that we’ll have to fix.”
    > 
    > “The hells,” said Fenn. “I think that’s a good start. It’s going to take two to tango, right?”
    > 
    > “Yeah,” said Amaryllis. I hadn’t seen any of the game text, or a whole lot that Fenn and Amaryllis were talking about, which meant that I couldn’t really know whether they were talking about the fact that they were the same person or the fact that they came from separate species. I had my doubts, but my gut was telling me that they were talking about the same person, with different quirks.
    > 
    > “Yeah, it’s not that hard, not even much harder than going up the stairs together,” said Amaryllis. “It doesn’t always make the world interesting, but you always look different when you’re holding people. And if you can’t hang it together, it’s hard not to want to take off at some point, or at least the moment of unresponsiveness, even if the reason that’s happening is actually the person. The rest of it is up to us, and we should make the most of it if it’s not working out, which it is not at all.”
    > 
    > “You did some weird stuff,” said Fenn. “You are all right.”
    > 
    > “Wasn’t it?” asked Amaryllis, looking back down at the floor.
    > 
    > “It was my fault,” said Fenn. “You guys did not get me for my talents like I might have,” she wiped her brow. “You’re the same people to me, you didn’t.” She looked slightly less concerned. “You have some talents in common with the person.”
    > 
    > “I have some things,” said Amaryllis. “I don’t pretend otherwise.”
    > 
    > “Hey,” said Fenn. “The way she looks down at the floor makes sense, given that you are holding her together, the way she gets a bit mottled. It was a different version of Fenn, but with you, of course.”
    > 
    > “You’re doing a great job,” said Amaryllis. We would have been done with our story, unless we had another five pages, or had a lot of secrets in there, but she had one more chapter to go, which was fine.
    > 
    > “I’ll meet you in the main room,” said Fenn.
    > 
    > “That is not really what the game was supposed to show,” said Amaryllis, frowning. “If we can get down from here, then it’s possible that we can get to the middle of it, but if we don’t, it can only go to the very end.”
    > 
    > “The last step,” said Amaryllis, frowning. This was a conversation that I’d liked to be having. “It might be that I could help you with it, but I’d think that people who’d like that kind of interaction should first know about Fenn’s talents first, and then I’d think back to the game, because I still don’t really understand it.”
    > 
    > Fenn gave me an exasperated look. “It makes sense!”
    > 
    > “Oh,” said Amaryllis. “You’re really not helping yourself to

    Yup that looks like WtC nonsense to me :p


    > **Alexander Wales**] had been the consummate gentleman. I forgot that he was a wizard, and I had to do some extra work on him to get him to say yes to something, but the thing that I liked most about him was that he had a good heart. I had no idea what his status was in the Order of the Phoenix. Maybe it was because I had to keep a close eye on him, but I knew enough of his story to know that it was preposterous.

    > “He’s in great shape,” said Fenn. “I’ve never seen him in pain, not even when I was in the process of casting.”

    > “It’s not that,” said Amaryllis. “It’s the fact that he’s a wizard.”

    > “It’s a problem,” said Fenn. “It’s complicated, and the solution is to get rid of the problem.”

    > “I’ll be very happy to help,” said Amaryllis.

    > and that was that. I didn’t want
    ```

- u/PresentCompanyExcl:
  ```
  This is a writing tool made by hugging face, it autocompletes your writing. Behind the scenes is the OpenAI GPT-2 model that's been in the news recently (the public medium size version). 

  It's a glimpse of some of the writing tools that will be produced by the latest wave of machine learning + text advances, which are quickly exceeding human performance (see the [GLUE/SUPERGLUE leaderboard](https://gluebenchmark.com/leaderboard)).

  Some more features we are likely to see in future are 

  - completions trained on a certain style, e.g. "complete this as JK Rowling". Similar to Gwerns poetry generation.
  - rewriting/editing (see [Levenstein transformers paper](https://arxiv.org/abs/1905.11006)),
  - better grammar checkers (Grammarly have published quite a bit), 
  - and eventually style tansfer is likely (this is a more challanging application thant text generaiton, and it's early days yet but see [grammerly's paper with informal=>formal translation](https://arxiv.org/abs/1803.06535)).

  If you're interested in this kind of thing keep an eye on huggingface, they are making some really great NLP tools using the latest techniques (I'm not affiliated in any way).

  Be aware that the site may not be up forever since it takes them [$24/hour to run on a AWS p3.16xlarge instance](https://twitter.com/julien_c/status/1139208397579051009). It may also suffer from the hug of death since it's not auto-scaling.

  More:

  - [Producthunt page](https://www.producthunt.com/posts/write-with-artificial-intelligence)
  - [Creators twitter thread with slider explanation](https://twitter.com/julien_c/status/1139166340684681216)
  - [subreddit with similar tools /r/MachinesWrite](https://old.reddit.com/r/MachinesWrite)

  Personally, I do machine learning freelancing for companies, and also look at my own startup ideas (currently comment moderation applications). So I'm interested in people's thoughts on this as a writing tool, especially from those amazing people who actually write (unlike me who just consumes other peoples' writing).

  Hopefully writing tools are on-topic for this subreddit, otherwise, I'll move this to a weekly thread.
  ```

---

