## I am a web developer - what website/webapp could I build for this community?

### Post:

Hey everyone!

I'm learning web development and getting pretty competent at it, and as one of my projects I would like to build something for this community, because I think it would be cool and fun.

So I'm wondering - is there any website/webapp that you would like to exist? Something that could be useful for rationalist readers or writers? Or maybe you have some problem that could be solvable with an app? If anyone has any cool ideas that you want me to build - please share =)

P.S.

If anyone offers some cool idea that I will end up building - I will pay a lot of attention to your suggestions and build features that you want to be there, so you essentially can get a custom-built, free, open-source app for yourself that does whatever you want =)

### Comments:

- u/alexanderwales:
  ```
  This is sort of pie-in-the-sky, but what I've really been wanting for a long time is an anachronism checker.

  Here's my basic use case:

  1. User enters in a chunk of text (likely a chapter of 5k-10k words)
  2. User enters a year (for example, "1900")
  3. User clicks "Check me!"
  4. Program highlights suspect words, phrases, etc.

  How this would work on the backend is that it would interface with something like [Google n-gram viewer](https://books.google.com/ngrams) or [Microsoft N-gram Service](http://weblm.research.microsoft.com/), run a check against every unigram, bigram, trigram, etc. to find its frequency in that year, then compare that against its frequency in the current year. If a certain threshold is exceeded, the n-gram is highlighted.

  So in our use-case example, the phrase "Albert Einstein" would be highlighted if you selected the year "1900" because Einstein was a complete unknown then.

  As a bonus, it's a very short step from doing *that* to having a webapp that can help highlight Americanisms in works which are set in British worlds.

  (There are a few ways to do things like this - mostly hacking spellcheck libraries - but all of them need setup and manual processes that are a pain in the ass.)
  ```

  - u/callmebrotherg:
    ```
    That would be The Best Thing Ever. 

    Actually, "Best Thing Ever" would be that, plus the program suggests alternatives.
    ```

  - u/ulyssessword:
    ```
    Also, [specific people](http://maryrobinettekowal.com/journal/how-i-beat-pat-rothfuss-at-being-pat-rothfuss/).
    ```

    - u/alexanderwales:
      ```
      Mary Robinette Kowal was actually how I was first introduced to the concept of automated anachronism checking. She [scraped a list of all the words in Austen's novels](http://maryrobinettekowal.com/journal/the-jane-austen-word-list/), then fed that into her text editor as a spellcheck dictionary, which then highlighted [words that Austen didn't use](http://maryrobinettekowal.com/journal/words-i-couldnt-use-in-glamour-in-glass/). But this method is sort of clunky, and not easy to generalize.
      ```

      - u/MaryRobinette:
        ```
        Good lord. If you actually make such a thing, please let me know.
        ```

  - u/brandalizing:
    ```
    This would be phenomenally useful. A huge help and an incredible time saver. Also, accuracy.
    ```

- u/paladinneph:
  ```
  first let me describe a "real life action tracking" system. this system allows the user to create one-time or time-recurring goals, or constantly on habits. when users notice they are doing a habit, or complete a goal, they manually tell the system.

  ok, now take literally any easily-copied free-to-play web game designed to get you addicted to it, then get you needing to pay for premium currency. (candy crush, anyone?)

  now, instead of charging for premium currency, reward or deduct it for actions via the tracking system already described. you just built a powerful self-guided training tool.

  to my knowledge, the only thing that comes close to this is habitrpg, but it has issues which make it less effective than it could be. for example, it's also free-to-play monetized, which lets you pay real money to bypass having to complete goals, which is a bad thing to train into people, and hurts its training effectiveness (do you want your users to be addicted to completing goals, or paying you?)
  ```

- u/callmebrotherg:
  ```
  Hm. If you know who set up the Rational Reads website, perhaps you get add the ability to edit entries after they've been entered. This'd be especially useful for editing tags like "dead fic" or "updating slowly." 

  http://rationalreads.com/#/
  ```

  - u/mns2:
    ```
    The Rational Reads Github [page](https://github.com/Amit-P-Amin/RationalReads), for those looking to add to it or see its progress.
    ```

    - u/callmebrotherg:
      ```
      Ooh! Thank you. 

      I didn't know that this existed. Thank you.
      ```

  - u/None:
    ```
    [deleted]
    ```

- u/traverseda:
  ```
  Out of curiosity, what tools do you use?
  ```

  - u/raymestalez:
    ```
    Django, Node.js, MongoDB, Express.js, Ember,  MongoDB, EaselJS, Bootstrap.

    Digital Ocean for hosting.
    ```

---

