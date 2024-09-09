## [RT] [HSF] Programmer at Large, Chapter 11: Does that work?

### Post:

[Link to content](http://www.drmaciver.com/2017/05/programmer-at-large-does-that-work/)

### Comments:

- u/arenavanera:
  ```
  I like this world a lot, and I'm enjoying the small slice-of-life vignettes, but after 11 chapters I'm starting to get a little antsy for conflict.  I'm hoping that either Kimiko's non-centrality or the game theory simulations turn into larger problems soonish.
  ```

  - u/DRMacIver:
    ```
    We'll explore the problems, but it's mostly going to continue to be low-conflict slice of life, sorry.
    ```

- u/failed_novelty:
  ```
  I'm very curious about what their 'modern' programming languages look like.

  Obviously, they've grown and changed as time went on, and they have techniques (and artificial aides) we don't have presently.

  But it really seems like 90% of their job is just thinking, which seems to be a pretty sweet deal if you can get it.
  ```

  - u/DRMacIver:
    ```
    > I'm very curious about what their 'modern' programming languages look like.

    I'm kinda leaving it deliberately underspecified because I don't feel competent to predict the evolution of programming languages accurately beyond the very near term. Roughly the idea in my head (which should be considered more "author headcanon" than canon) is that rather than having a small set of languages, they have a whole "tree" of languages which start from simple cores and compile down to the next level, with an awful lot of formal verification and analysis happening at each translation level, and an awful lot of focus on interoperability standards.

    It would be absolutely maddening to work with unassisted, but fortunately they don't ever work with it unassisted.

    > But it really seems like 90% of their job is just thinking, which seems to be a pretty sweet deal if you can get it.

    This too can be yours for the low low price of 10,000 years of toolchain development. ;-)
    ```

    - u/selementar:
      ```
      > absolutely maddening to work with unassisted, but fortunately they don't ever work with it unassisted

      Curious case about the languages available to us:

      Lots of work is done in C transparently, i.e. one *almost* never has to go to the level it compiles into (machine codes, represented as assembly code). Then there're interpreted languages / VMs, and one almost never has to go to the C/CPP-representation under them. And recently some made translated languages on top of both ([1](http://cython.org/)) ([2](http://coffeescript.org/)), but didn't entirely manage to organize toolsets for the transparency, i.e. if something goes slightly wrong, there is still a need to go into the underlying representation.

      The lesson is here is not clear, but it slightly suggests that making a translated language is cheap, but making a toolset to avoid dealing with stuff it is translated into is hard and expensive.

      And then there's the point of actually *spreading the learning* of a language, and of how best to use it; a notable example in scripted languages is perl as compared to python: in a way, perl could be used about as conveniently as python is (with a little less sugar), but it did not nudge toward those practices, and lots of perl code thus became write-only code.
      ```

      - u/Jello_Raptor:
        ```
        The issue here is mostly precision of semantics and correctness of conversion. Many languages, especially older ones, don't have a precise formal semantics that tools can work with, or use system quirks that are incredibly difficult to model. Even then we're seeing some progress with formally verified compilers and the like. 

        If you have correctness, then the problem becomes performance, and things like linear type systems can help with those when they start becoming more prevalent.
        ```

- u/nicholaslaux:
  ```
  Why are PTYs a memetics hazard? Just because explaining them take a lot of explanation time for little to no benefit?
  ```

  - u/sparr:
    ```
    I'm guessing this is related to tvtropes/Wikipedia tab explosion.
    ```

    - u/gryfft:
      ```
      My guess is this is it, since learning that PTY stands for "pseudoteletype" begs the question "what is a teletype" and you pretty much inevitably wind up learning the history of early time-sharing systems, the rise of glass TTYs, the history of terminal emulation and the properties of PTY devices as they are exposed through and used by POSIX-compliant systems ("What's POSIX?" asks Arthur and the can of worms goes on.)
      It's all interesting history and useful for modern programmers using POSIX systems, but would probably eat up the rest of Arthur's afternoon without getting them closer to solving their problem.
      ```

      - u/PeridexisErrant:
        ```
        > modern programmers using POSIX systems

        The juxtaposition of *modern* and *POSIX* would probably eat the reminder of Arthur's voyage, never mind an afternoon.
        ```

        - u/selementar:
          ```
          Hey, the standards are still useful! For example, there're a few reasons some distros [switched **from** `bash` as the default /bin/sh](https://wiki.ubuntu.com/DashAsBinSh) to an "arbitrary fast *POSIX-compliant shell*".

          ...

          Sorry for the formatting overload.
          ```

          - u/PeridexisErrant:
            ```
            For *me*, yes.  For *Arthur*... maybe not.
            ```

            - u/gryfft:
              ```
              Which is why I stipulated "modern," which I intended to mean the 21st century (that was probably unclear.)
              ```

          - u/sparr:
            ```
            I was *so happy* on so many levels when Ubuntu switched to dash. The number of bashisms causing breakages in packages that needed to be fixed were a BONUS, not a cost.
            ```

    - u/nerdguy1138:
      ```
      It's a really good idea to warn about the possible wiki-walk beforehand!
      ```

- u/Gurkenglas:
  ```
  It's unlikely that a random one of 114 interesting things will be the culprit, so he should look at others before expending political capital on checking this one.
  ```

  - u/over_who:
    ```
    > It's unlikely that a random one of 114 interesting things will be the culprit, so *they* should look at others before expending political capital on checking this one
    ```

- u/MoralRelativity:
  ```
  Looking forward to learning Go#.
  ```

  - u/monkyyy0:
    ```
    Its go with all the bullshit that c# has
    ```

- u/BadGoyWithAGun:
  ```
  Be honest, how much of this series is just self-insert of the main character by having him scoff at programming practices you have an aversion towards?

  "everyone is autistic and a gendersnowflake" != "rational fiction"
  ```

---

