## [D] Friday Off-Topic Thread

### Post:

Welcome to the Friday Off-Topic Thread! Is there something that you want to talk about with /r/rational, but which isn't rational fiction, or doesn't otherwise belong as a top-level post? This is the place to post it. The idea is that while reddit is a large place, with lots of special little niches, sometimes you just want to talk with a certain group of people about certain sorts of things that aren't related to why you're all here. It's totally understandable that you might want to talk about Japanese game shows with /r/rational instead of going over to /r/japanesegameshows, but it's hopefully also understandable that this isn't really the place for that sort of thing.

So do you want to talk about how your life has been going? Non-rational and/or non-fictional stuff you've been reading? The recent album from your favourite German pop singer? The politics of Southern India? The sexual preferences of the chairman of the Ukrainian soccer league? Different ways to plot meteorological data? The cost of living in Portugal? Corner cases for siteswap notation? All these things and more could possibly be found in the comments below!


### Comments:

- u/DaystarEld:
  ```
  Finally starting my "is Harry a Marty Stu" HPMOR reread. Learn more here, all feedback welcome!

  https://www.reddit.com/r/HPMOR/comments/70bhdn/methodology_to_finally_put_is_harry_a_marty_stu/
  ```

  - u/None:
    ```
    You're doing God's work. I was planning on going through it myself with a critical eye, but this might just save me the trouble.
    ```

  - u/None:
    ```
    You're pretty brave about flamebaiting.
    ```

- u/ketura:
  ```
  Weekly update on the [hopefully rational](https://docs.google.com/document/d/11QAh61C8gsL-5KbdIy5zx3IN6bv_E9UkHjwMLVQ7LHg/edit?usp=sharing) roguelike [immersive sim](https://www.youtube.com/watch?v=kbyTOAlhRHk) Pokemon Renegade, as well as the associated engine and tools. [Handy discussion links and previous threads here](https://docs.google.com/document/d/1EUSMDHdRdbvQJii5uoSezbjtvJpxdF6Da8zqvuW42bg/edit?usp=sharing).


  ----


  So you know what I’m sick of rewriting?  Stats.  I think I’m on the fourth iteration; balancing flexibility, usability, and maintainability has turned out to be a huge pain in the ass.  This past weekend I actually found that saving the actual core field as `dynamic` was unnecessary; for the handful of cases where I needed math within the generic type, I could just *cast* to dynamic instead.  This allowed me to cut back on the amount of runtime-only risks quite a bit, but it did require rewriting *again*.


  Still, I think that stats are finally more or less solidified. I’ll probably end up rearranging some of the fields a bit more in the future, but nothing on the scale of going back to the drawing board (I hope).  


  I got a basic serializer working and using it toyed around with the Species and Unit classes a bit.  For those in the dark, a serializer is a means of translating in-memory data into a different form.  In my case it’s transforming it into Json, which is human-readable and will be the primary means of modding: if you want to make all Charizards OP, just open up Charizard.json and crank the stats way up.  Due to the large amount of data this game will use, I imagine that most modding will be in that form, either adding or modifying Pokemon or other items.


  As I got the serializer working, I found that the first true Systems needed to be set up properly.  System (capital S) in XGEF has a special meaning: a System has control over a particular domain, whether it be as far-reaching as a WorldSimulationSystem or as humble as the StatSystem which just keeps track of what kinds of stat exist.  Systems come in two halves, a CoreSystem and a ModdedSystem.  The dual nature of the beast requires that it be built in three parts (how’s that for a plot twist), but ultimately means that part of the System comes pre-made and ready to go, while the rest is fully moddable.


  As of last night I have the StatSystem all set up and divided in this manner, and with it I’ve developed some simple templates and conventions that will make future Systems easier to create.  


  For combat to be a thing, I’ll need at least rudimentary versions of the following Systems:


  * `Stat System` (contains a registry of different stats that can be used by units)

  * `Species System? ` (similar registry for Species)

  * `Unit System` (for now just a factory that knows how to take a given species and spawn a unit of the appropriate type)

  * `World System` (handles the simulation of the world, which for the combat sim comes down to moving units where they say they want to go)

  * `Action System` (units use this to report what it is they want to do, and the ramifications are played out by this system)

  * `Combat System` (acts as a layer between player/unit or AI/unit, restricting the available actions according to the game design.  For instance, you can’t move if you’re dead, and you can’t breathe fire if you’re exhausted, that sort of thing.)


  And no doubt I’ll trip upon a couple other things that I’ll need as I continue to iterate.  


  Anyway, that’s it for this week.  My focus for next week will be split between getting very basic versions of all the systems ready, ensuring it works with the existing mod loader, and attempting to set up unit tests for things like the serializer and mod loader.  


  ----


  If you would like to help contribute, or if you have a question or idea that isn’t suited to comment or PM, then feel free to request access to the /r/PokemonRenegade subreddit.  If you’d prefer real-time interaction, join us [on the #pokengineering channel of the /r/rational Discord server](https://discord.gg/sM99CF3)!
  ```

  - u/None:
    ```
    Man, I've tried the system approach a few times.

    It may be that I'm not organized enough but it ends up being a cluster-system of systematic proportions. 

    Every system ends up dipping in every other system and before I know I've designed myself into a corner. 

    From your own description the world, action and combat systems have such a vague description of their purpose and will need to interact so heavily that they may as well be a single "Logic" system while the rest are just data containers. 

    If you cant' explain to a five year old why system A and B are not the same thing your assignment of responsibilities is too vaguely defined and you'll end up with cross dependencies and duplication on who needs to do what and who needs what data.
    ```

    - u/ketura:
      ```
      So System, as I've designed it, is at least 80% the same as the system in a [entity-component-system paradigm](https://en.m.wikipedia.org/wiki/Entity%E2%80%93component%E2%80%9 system). Systems do two major things: one, they define particular kinds of entity or component (thus the WorldSystem defines a Map, probably a Tile and maybe even a TilePosition component for units to use) and two, they are called each frame and perform actions on their classes of entity and component. Anything outside of those two things is (probably) passed over to another system, as a way of saying "hey, our entities did something that affects your entities, deal with it".

      It helps that the majority of my experience is with Unity, which pretty exclusively uses E-C-S, so I'm used to the separation of concerns that it enforces. It does require a certain amount of discipline, but that's entirely what XGEF is for: to force the developer to build in a particular way. *I'll* have to make sure my habits are good, but the hope is that by so doing any downstream users (myself included) can then lean on my work in the form of XGEF.

      Plus, it's important to have Systems to help structure mods. In that way they're a lot like namespaces, giving clearly marked regions for containing certain kinds of content. Not everyone will follow the signposts, but those that do will find sensible standards waiting for them (or so we hope).

      I'll grant you that my one-sentence summaries are kind of vague. Part of that is the burden of knowledge starting to rear its ugly head (we've iterated on every aspect of the design enough that it's difficult for me to remember the most recent conclusion, usually), and part of it is leaving some things open ended so I don't feel like I've painted myself into a corner with a rigid unfeeling design. But hey, that's why I'm working on it now--get it some concrete foundation and start sorting those vague ambiguities out. [We know *what* we want to include](https://docs.google.com/document/d/1SlYaK6vZ0OmkQsuVOMCIOMb6nPIU9I1vKMTFMEL0Wk8/edit?usp=drivesdk) and we've got it probably about 75% of the way sorted; I'll patch the rest as we go.
      ```

      - u/None:
        ```
        I'm not familiar with XGEF, what is it?

        My own experience with ECS haven't gone that well, Unity does a good job of it but designing a similar system from the ground up is difficult unless you make concessions somewhere. 

        The best usages of ECS I've had so far is where each system is forced to have it's own thread. This enforces a certain amount of separation and consistent API between systems on how they interact with each other. It tends to improve how multi-threaded your architecture is which is a huge win on modern systems. 

        I have very little game development experience, but a whole lot of engine development experience, so my `SoundSystem`, `GraphicsSystem` and `PhysicsSystem` components are solid but it all falls apart once you start adding flexibility, customization and the support for adding new dynamic systems that other systems were not programmed with hardcoded awareness of. 

        There's also a bit of a trade off between API usability, performance and complexity, a good example is how do you tell your graphics system that something needs to be drawn?

        You might say `graphicsSystem->draw(object->graphicsComponent)` but what does that do?

        Drawing an object can be a complex multipass operation, how can you encode all of that complexity into just a `GraphicsComponent` structure?

        How does the graphics system gather everything it needs for some shader pass and then execute it? The optimal approach is something deferred, you don't want to context switch every time the framebuffer, GPU program or model changes.

        Even for something like the typical depth prepass. If something needs to show up with a shadow, the graphicsSystem might need to multiplex a single API call into multiple. Which means it needs to defer, but deferring the depth pass can have a latency (and therefor performance) impact. 

        What about custom graphics effects or shader passes that require the results of another earlier custom shader pass? At this point you need to create a DAG and determine the proper ordering of passes and it's a whole cluster fuck unless you've kept everything very neat.
        ```

        - u/ketura:
          ```
          So it's funny you bring up creating a DAG, as that's actually exactly what I've spent the last two days tinkering with: letting mods announce what order they need to come in in relation to other mods while still resulting in something resembling sanity.  

          If one *were* to be crazy enough to try and apply E-C-S to a graphics system, it would have to be something like a list of Renderers that are passed the screen buffer in a particular order.  Each one would take a look at its own internal list of applicable entities (a particle system, or billboard, or 3D model, or sprite, or shader or whatever, one type per Renderer) and apply them to the buffer when asked.  Systems which have to apply work to the buffer at multiple stages would simply register multiple places in line at different points.

          However, I'm with you: I don't think Graphics or whatnot can be efficiently subdivided like that.  Its performance is very much based around sharing the same data wherever possible, and that's impeded by needing to split it up like that.  At most I could see a GraphicsSystem owning the types of entities I mentioned, and then a single system would be responsible for and know how to draw a ParticleEffect, Model, Sprite, etc (which is how it works).  It certainly wouldn't play very well with additional rendering systems that were unknown at compile time.

          Regardless, I'm more interested in the design pattern as it pertains to a flexible, moddable game design.

          XGEF is short for eXtensible Game Engine Framework, and it's the modding framework that I'm building to power Renegade (and to hopefully be generalized enough to work for other titles once I'm done). Crucially, it's not an engine but designed to work with one; in this case Renegade will likely end up interfacing with Unity or Xenko but since what XGEF does isn't that close to the metal, it shouldn't matter what you build it with. This means that it doesn't need to apply the pattern to bare-metal systems such as Physics, Graphics, or Audio or whatnot, as the game will need to provide the glue that holds XGEF and the engine together.

          It's for that reason that I think E-C-S is a good fit. Mods, in general, are more concerned with the content and/or design of a game, not the nuts and bolts, so this is where the flexibility can go nuts.  At the end of the day a renderer is just eating matrices and shitting pixels, what does it care how many abstract levels of systems or components funneled into the resulting matrix array?

          As part of the design of XGEF, the number and type of Systems are known at compile time.  The game using XGEF determines which Systems exist, and mods can then add or modify the Components, but not change the actual number of Systems in place.  This puts a hard boundary on what the developer is willing to allow to be modded, while at the same time offering ample room within that sandbox to play in.  Ideally, there will even be a small library of Systems that a developer can pick between, permitting fine-tuning of the basic game logic in broad strokes, but that's far down the road.
          ```

- u/ToaKraka:
  ```
  If you weren't aware, [much continues to be made](http://archive.is/bEKbD) of [George Martin's dig at John Tolkien's failure to provide the details of Aragorn's tax policy](http://marginalrevolution.com/marginalrevolution/2014/04/what-was-aragorns-tax-policy.html). I wonder whether jokes in a similar vein could be made toward *Harry Potter* and/or *Methods of Rationality*. A search for `tax` in my *HPMoR* file turns up no details on the Ministry of Magic's revenue stream&nbsp;.&nbsp;.&nbsp;.
  ```

  - u/Wiron:
    ```
    Trade bariers are mentioned in author notes.

    >Although HPMOR doesn’t go into this in much depth, the lack of trade between magical Britain and Muggle Britain implies some further background reason why the Weasleys can’t just go off and make millions of pounds selling simple healing Charms to rich Muggles. Presumably people like Lucius Malfoy have arranged for trade with Muggles to be heavily regulated - for the protection of the poor innocent Muggles, perhaps - so that only people like Lucius Malfoy are allowed to make their family fortunes at it, and nobody else is allowed to try.  (This is also a likely place where Harry’s idea about trading Galleons and Sickles for Muggle gold and silver would run into a barrier - there are a lot of dogs not barking, a lot of Ricardian comparative advantage trades that aren’t happening, not only that one.)

    I wish Harry tried his arbitrage scheme and failed miserably.  *Harry Potter and the Exclusive Institusions.*
    ```

    - u/buckykat:
      ```
      Okay, so where's the thriving black market?
      ```

      - u/blazinghand:
        ```
        Probably not in a place highly permeable to wealthy muggle-raised 11 year olds but what do I know
        ```

      - u/PeridexisErrant:
        ```
        Quietly murdered by someone not traceable to the Malfoys, and the body vanished?

        If anyone who tries it gets disappeared, people will eventually stop trying.
        ```

        - u/buckykat:
          ```
          > this is what authoritarians actually believe.
          ```

          - u/None:
            ```
            "When you cannot declare that the people freely serve the Emperor, declare Exterminatus."
            ```

  - u/SvalbardCaretaker:
    ```
    There is the quip made about "ink monopoly" and "winning shipping wars" as to sources of revenue. 

    >Chapter 81:  Why, indeed, would wizards with enough status and wealth to turn their hands to almost any endeavor, choose to spend their lives fighting over lucrative monopolies on ink importation? 

    Thats of course a personal wealth scheme. 

    If I remember canon correctly, we get a couple of taxed items, eg. certified portkeys, and maybe the breeding of magical creatures?
    ```

    - u/alexanderwales:
      ```
      Mentioned in ch 3 as well:

      > An old and respected journalist, Yermy Wibble, called for increased taxes and conscription. He shouted that it was absurd for the many to cower in fear of the few. His skin, only his skin, had been found nailed to the newsroom wall that next morning, next to the skins of his wife and two daughters. Everyone wished for something more to be done, and no one dared take the lead to propose it. Whoever stood out the most became the next example.
      ```

      - u/None:
        ```
        I noticed at the time, but looking now *wow*, that's how the KKK operated, isn't it?
        ```

        - u/Frommerman:
          ```
          That's how any terrorist group seeking greater power operates.
          ```

          - u/alexanderwales:
            ```
            Terrorist group, government, or corporation. The tallest nail is the one that gets hammered down.
            ```

- u/Frommerman:
  ```
  I have a strange and recurring problem. Through various means, I make the accquaintence of women who are fundamentally shattered by the events of their lives. They've survived rape, started and quit drugs, had other mental issues exacerbated by their experiences, and never developed into what one might consider a normal adult for a variety of reasons.

  People like this often don't have many in the way of friends, and I am one of the only people who will talk to them. This is a problem, however, because this causes them to become attracted to me because *omg this super nice, empathetic guy notices me!* I am not attracted to them. I have my own mental issues to deal with, and being in a relationship with someone whose issues are worse would destroy me because I would want to reach in and fix their problems. Which I can't. I also feel somewhat obligated to keep talking with them as a harm-reduction method, but I know I really shouldn't because I personally cannot handle interpersonal interaction at all hours of the day, and I know that doing so will just lead them on.

  This has happened twice now. What do?
  ```

  - u/eternal-potato:
    ```
    > I have a strange and recurring problem. 

    > This has happened twice now.

    I'd hardly call two instances _recurring_.
    ```

    - u/Frommerman:
      ```
      It's the fact that it has happened twice which inspired this post. Once is a fluke, twice is a pattern.
      ```

      - u/ketura:
        ```
        Once is happenstance, twice is coincidence, *three times* makes a pattern.
        ```

        - u/blazinghand:
          ```
          From Goldfinger:

          >Once is happenstance. Twice is coincidence. The third time it’s enemy action.

          Clearly this means a conspiracy is afoot! /s
          ```

    - u/None:
      ```
      Once is a point, twice is a line, thrice allows fitting a polynomial and is also enemy action.
      ```

      - u/CthulhuIsTheBestGod:
        ```
        I hate (very slightly) to be pedantic, but lines are polynomials.  In addition, three points allow fitting infinitely many polynomials.
        ```

  - u/ben_oni:
    ```
    > I have a strange and recurring problem.

    I'd hardly call this *strange*. Commonplace is probably a more accurate term.

    Do not engage. There is no victory to be had in these battles. Do not spend significant amounts of one-on-one time with these women. The best thing that can be done is to introduce them to a support network. If you have a church, invite them to attend and engage with the social network there. Other social organizations may be able to fulfill a similar role. Get them to volunteer with a charity organization if possible.
    ```

  - u/MistahTimn:
    ```
    My advice would be to be upfront from the beginning of the interaction. A large part of empathy is that it seems like the person being empathetic has their shit relatively more put together when that might not really be the case. 

    I was in a very similar situation a couple years ago. I started dating a girl, like you described, who had more than her fair share of issues while simultaneously dealing with a diagnosis of depression and anxiety. We started dating primarily because I was the empathetic one in the relationship and was serving as a social crutch for her and she asked me out as a result. An important thing to recognize is that this is not healthy for either party involved. Like you, I found it draining because I'm an introvert who was struggling to live up to being a mental crutch for someone in a not great place. For her, the relationship made it seem like not as much else needed to be done.

    Obviously your situation is not entirely the same, but I think there's a lot of parallels there. It's okay to tell someone that you're not capable of interacting with them sometimes, or that you're not ready to be in a relationship with them because of personal issues. In my experience, that's what I wish I had done because I think it would have turned out better for both of us.
    ```

- u/Sagebrysh:
  ```
  [I've been making rationalist youtube videos](https://www.youtube.com/user/Ztikara/videos). I talk about various rationality concepts and am slowly beginning to work my way through the sequences. Check it out!
  ```

- u/Dwood15:
  ```
  Man, I'm always late to these things. 


  Anyway, about a year ago, I discovered there was a homebrew community for the NES, SNES, Playstation 1, Dreamcast, etc. 

  Remarkably, there is very little information on Nintendo 64 Homebrew. 

  Being a complete nerd, and wanting to rectify that, I went and created a new subreddit, called /r/N64Homebrew, in the same vein as /r/consolehomebrew, and began scouring about the internet for development information on the N64. 

  Surely _someone_ has a C library which builds N64 Roms?

  Turns out? 

  _No recently updated tools build to be able to initialize 3D on the N64._ This means that libdragon can do sprite, audio, controller interface, activate the rumble pak, and so much other stuff. But nope, no 3D. 

  So, what did I do? 

  Kept scouring. 

  The original n64 sdk is still around! It comes with 16-bit compiled GCC built for MS-DOS. Now I was cooking! I had working tools, but I was having problems getting them to install properly... After some major googling, I found the right user referenced on multiple n64 fan sites, contacted them, and they gave me the last keys I needed to get the system running. 

  See [this sticky](https://www.reddit.com/r/N64Homebrew/comments/4d5het/it_works_how_to_build_your_own_rom_using_the/) on installing and getting set up with your own working build.

  Now, we're good to go. But I'm still tied to versions of Windows less than Vista! 

  Nintendo was using GCC, but the SDK _doesn't actually include GCC's full source code_, like the GNU license required. I contacted the original company which produced the toolchain, but they were silent. I checked the version of GCC - "ca 1997, is V. 2.7.2, release 1.2"

  That version of GCC was (iirc) one of the last versions ever built to run on a Windows Machine directly. How hard could it be to get it to build?

  I made a post here: 

  https://www.reddit.com/r/gcc/comments/57vqbc/looking_for_some_help_working_with_legacy_gcc/

  And got some help. 

  Only problem is that the person who helped me get it to compile (and they did get it to work on Windows 10 64 bit...) deleted all of their comments and deleted their account.

  So here I am, with a working copy of GCC from 1997 running on my Win 10 machine, and the person who helped me get it to work, is gone, and all their comments deleted.

  I'm honestly not sure if trying to recreate the person's effort is worth it at this point.
  ```

  - u/CthulhuIsTheBestGod:
    ```
    [This page](http://level42.ca/projects/nintendo-64-development/) linked in your sticky post appears to have moved [here](http://ultra64.ca/resouorces/software/).
    ```

  - u/gbear605:
    ```
    To look at the deleted comments, check out (rot13) uggc://prqqvg.pbz/
    ```

  - u/None:
    ```
    Do you have any of this on github?
    ```

  - u/traverseda:
    ```
    Why not dosbox?
    ```

    - u/Dwood15:
      ```
      The application errors out. Not sure why.
      ```

- u/RMcD94:
  ```
  Anyone read any of the fanfiction on alternate history's new fanfiction section. The quality of writing seems much better than average I assume because of the more rigorous standards required to write alternative history 

  Does anyone have any recommendations
  ```

- u/None:
  ```
  Honestly, the debates about that startup Bodega are mostly making me want a really junky sandwich, but I think I'll hold off.
  ```

- u/Kishoto:
  ```
  Another question about consent. But this time, information consent!

  Basically, I had a discussion with my friend and she told me that she believes consent is important in all respects, even information. As in, information should not be forced on someone who does not want/ask for it. 

  This was interesting to me because I personally feel that people need to be educated on certain things regardless of their beliefs/consent as I feel that there are certain beliefs that are honestly negative, such as racism or the belief in the earth being flat being used to justify a fundamentalist's view. So I don't personally think I would respect a flat earther's desire to not be educated. 

  How do you guys feel about consent, specifically towards information we take in? Specifically factual information with verifiable (or as good as) evidence.
  ```

  - u/Salivanth:
    ```
    People should have the ability to choose what information to listen to, and it's up to them not to abuse this privilege. I mean, think about it the other way. A flat-earther comes up to you and says "Hey man, I have PROOF that the earth is flat. You're wrong. All you need to do is listen to this ninety-minute video."

    You're well within your rights to say "No, I don't want to." at which point the flat-earther accuses you of refusing to be educated. Should you be allowed to refuse to take in this information, even if it's arguments for the position that you've never heard before?

    As for specifically factual information with verifiable evidence, I could make a similar argument. Someone asks you to read over a boring, obscure three-hundred page technical manual. Every word in it is factual and verifiable. Should you be allowed to refuse?
    ```

    - u/Kishoto:
      ```
      That's a very fair way to look at it. My instinctual reply to that was "But then what do we do if someone's obstinate and refuses to accept the opportunity to challenge their worldviews?'

      And then I reailized that happens literally all of the time. And so we do what we always do. 

      ~~Try and take over the world without their consent~~ Accept that some people are obstinate and pray the damage they inflict is minimal.
      ```

- u/Roseuno3:
  ```
  Why couldn't you just remove the part of the brains of humans and other intelligent creatures that finds suffering important?
  ```

  - u/eternal-potato:
    ```
    What do you expect to achieve with that?
    ```

    - u/ulyssessword:
      ```
      Win at Preference-Utilitarianism by making agents whose preferences are easy to satisfy?
      ```

    - u/ben_oni:
      ```
      Obviously we'd be archiving brain tissue. Probably to do an extensive analysis at a later date. Maybe put them all back together into one bigger brain that only cares about suffering.

      EDIT: Aah, eternal-potato, you fixed your typo! Now my reply doesn't make any sense at all. :(
      ```

  - u/CouteauBleu:
    ```
    "I don't like spinach, and I'm glad I don't, because if I liked it I'd eat it, and I just hate it."
    ```

  - u/None:
    ```
    Because brains aren't really modular like that.  It's an old bit of pop-neuroscience and doesn't really have a lot of weight in real life anymore.
    ```

  - u/ShiranaiWakaranai:
    ```
    I'm not sure you can do that without removing sentience along with it. I mean, you could probably disable all their pain nerves, but that's not the same as making suffering unimportant since there's other types of suffering like grief and melancholy and boredom and helplessness and anger, so you would have to delete all those too...
    ```

  - u/buckykat:
    ```
    Because that's a lobotomy?
    ```

- u/None:
  ```
  Anyone here play Zachtronics' games? I've played quite a bit of TIS-100 (though I got stuck and haven't played it in a while); I've been playing Infinifactory and Shenzhen I/O recently, too.
  ```

- u/SvalbardCaretaker:
  ```
  In an unexpected turn of "small world" events, Robin Hanson over on overcomingbias has linked in [this Post](http://www.overcomingbias.com/2017/09/too-much-of-a-good-thing.html) to the minor NSFW reddit celebrity /u/aellagirl on her twitter account.
  ```

  - u/AellaGirl:
    ```
    I'm balls deep in the rationalist community somehow

    **edit** shit i didnt mean that to have sexual implications, I just meant I go to like, their meetups, nothing else
    ```

    - u/Frommerman:
      ```
      We all believe you.
      ```

    - u/None:
      ```
      > edit shit i didnt mean that to have sexual implications, I just meant I go to like, their meetups, nothing else

      Lots of people go to meetups, and would not describe themselves/ourselves as "balls deep".  Yeeks, I didn't even know you *could* fuck an incorporeal community-concept.  Though there's almost definitely porn of it somewhere.
      ```

      - u/SvalbardCaretaker:
        ```
        Thatsthejoke.jpg 

        Note the missing edit star.
        ```

        - u/None:
          ```
          Shiiiiit.  I've been got good.
          ```

---

