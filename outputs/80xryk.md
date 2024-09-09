## [WIP][RT] Worth the Candle, ch 80-82 (Pea/God/Tail)

### Post:

[Link to content](http://archiveofourown.org/works/11478249/chapters/31799628)

### Comments:

- u/cthulhuraejepsen:
  ```
  February report, x-posted from [my Patreon](https://www.patreon.com/posts/february-report-17268937), probably not that interesting to anyone:

  I think that word count is a terrible metric of performance for an author, because word count isn't terribly hard to inflate, and really easily comes at the expense of the story construction and/or quality of the prose. That being said, it's not like you can easily quantify a work's other qualities, which is why word count dominates discussion of output. Word counts are reported verbatim as taken from the function in Google Docs, but shouldn't be treated as absolute, since there are lots of ways to count words and those methods are in disagreement with each other.

  The last chapter of January was published on the 26th, so the February period covers all writing done January 27th to February 28th, a period of 32 days. In that time, 10 chapters were posted (not including ch 75, which was a compilation of material), totaling 60,329 words, or an average of 1,885 words per day, and an average chapter length of 6,032 words.

  And some other stuff, mostly to answer the question of what else I'm doing with my time, and in the interests of being at least transparent about where my time is spent (so you can keep an eye on it):

  Words written for Worth the Candle but not actually used in it total roughly 6K words for the month, though some of those are in the form of scenes that might potentially find a home later.

  Words written for other projects:  
  ~12K for A Series of Fights Without Any Meaning [WIP Title]  
  ~4K for untitled fantasy/military novel  
  ~3K for Glimwarden  

  Reddit comments for the month total (very roughly) 12K words, not counting quotes or mod messages.

  Edit: Oh, also! The (hacked-in) thumbnail is courtesy of my sister, who does a lot of watercolor, and [whose site is here](https://annifriesen.com/). It's a crop of a larger banner for TopWebFiction, which I paid her for with homemade fermented honey-garlic and kimchi.
  ```

  - u/derefr:
    ```
    > word count isn't terribly hard to inflate

    Have you considered calculating the Shannon entropy of your writing?

    I've recommended this approach for calculating programming productivity metrics before, but never thought to apply it to prose until now. But I think it might work!

    A proper measure of Shannon entropy for prose would involve, I think, converting your words into word-pairs, and then generating a big table of word-pair frequencies in the English language and using it as a Huffman prefix table. Not the most approachable metric.

    But a pretty easy heuristic to *estimate* Shannon entropy, is just dump your text into a raw plaintext file, compress that file with any random compression algorithm (say, gzip), and then take the size in bytes of the compressed file as your entropy. Since the theoretic "perfect" compression finds the Minimum Message Length of a plaintext—and current generic compression algorithms are about 95% of the way to "perfect" for text—these algorithms serve as a viable estimate of text's informational entropy.

    For the most conservative estimate of productivity, make sure to compress all your earlier chapters together with the newest one, and then measure the marginal difference in compressed byte-size with and without the newest chapter added. That way, you can't cheat by being redundant *between* chapters, either. Flashbacks would compress to nothing!

    I'd be excited to know whether this works for you, if you're willing to give "marginal compressed bytes per day" a try as a metric.
    ```

  - u/t3tsubo:
    ```
    Can you share your recipe for homemade fermented honey-garlic? That sounds delicious.
    ```

    - u/cthulhuraejepsen:
      ```
      It's literally just raw honey and raw garlic. They ferment each other; the honey gets watery and infused with garlic flavor, while the garlic loses most of its moisture and becomes sweet (almost candied). Then add some vinegar if you have to in order to lower the pH, which should be below 4.5 (I try to use as little vinegar as possible, because I don't think it tends to do good things for the taste). After that, you just wait a month with it out of the light and at room temperature and burp it occasionally to let out the gasses. There should be enough honey to cover the garlic and then some. [See this video.](https://www.youtube.com/watch?v=XLVxVQ8O0s4)

      I use it as a sweetener in anything savory; lately it's been part of kimchi stew (kimchi, rice vinegar, sesame oil, fish sauce, honey-garlic, broth, and some seared pork belly or a soft-boiled egg).
      ```

      - u/dac69:
        ```
        Shit, dude.  In addition to being incredibly entertaining, you may have just made my real life better.  Welp, I've been putting off adding you on patreon for too long.  Time to support.
        ```

- u/sparkc:
  ```
  > Amaryllis frowned. “Have you been talking to Fenn, Grak, or both?”
  “About … this?” I asked. “Neither.”
  “Shit,” said Amaryllis.

  I loved this subtle dig at Joon’s social skills.
   ‘If even Juniper can tell it must be *really* fucking obvious’.
  ```

  - u/adgnatum:
    ```
    Maybe that, but perhaps just the fact that she's now received three independent observations in the same direction
    ```

- u/Jokey665:
  ```
  >mary.bak, grak.bak, and fenn.bak

  love it lol
  ```

  - u/Kilbourne:
    ```
    Can you explain the joke here? I'm not familiar with programming.
    ```

    - u/Jokey665:
      ```
      not a programming thing, just a general computer thing. it's relatively common practice when backing up a file to make a copy of it and append .bak as the file extension
      ```

      - u/Kilbourne:
        ```
        Oh I see. My file back-ups are in the original file-form. Is this bad practice?
        ```

        - u/t3tsubo:
          ```
          Not really, the idea is to just make it clear that the file is a backup.

          So "important.dll.bak" versus "(BACKUP)_important.dll" would accomplish the same thing
          ```

          - u/cthulhuraejepsen:
            ```
            Traditionally, the '.bak' naming process is used because that makes the file unreadable to programs, systems, or code that might be trying to access it. This is especially important when you have somewhat unpolished scripts that go into a folder and, for example, upload all the PDFs to a server somewhere, or attempt to read in a text file. It's really helpful to prevent user error as well, because a .bak file can't be naively opened by double-clicking.
            ```

            - u/derefr:
              ```
              It's also more of a DOS-ism, with filenames always being expected to be in that 8.3 format.

              In Linux or macOS, you'll instead see backup files, or temporary files, with names that end in tildes, like `foo~`. These are usually created by programs like text-editors that want to autosave, but are afraid that creating a file with the real name will make magic happen (like a program noticing a change in its config file and so attempting to reload it.) You don't want to be able to break your computer by shutting it off with a text-editor open with unsaved changes to a system configuration file. So, instead, programs will name their temporary auto-saved copy of a file `foo` as `foo~`, and then, when you save, delete `foo` and rename `foo~` to `foo`—or, if you quit without saving, just delete `foo~`.

              These files still work as backups, too; if power gets cut off to the computer, when you start it back up, you'll find the autosaved `foo~` sitting there beside `foo`. The types of programs that make these files are usually smart enough that, if you try to edit `foo` again while `foo~` is still there, they'll notice `foo~` and offer to resume your editing session.
              ```

- u/XxChronOblivionxX:
  ```
  > “No,” said Amaryllis. She closed her eyes and shook her head. “No, Juniper, why, I’m pregnant now, I can’t even drink my sorrows away.”

  Okay, this is one of her best all-time lines. She is too perfect to only exist in this story. 

  I am smelling a locked room murder mystery here, and kept thinking that Juniper was gonna bring that up. I find myself leery of this new potential companion, I like the current group dynamic and make-up and don't know whether I'd like another person added.
  ```

- u/Escapement:
  ```
  Well, this is going in all sorts of interesting directions. June needs to look into the backpack and see what sort of gear he can come up with from Earth. 

  Odds on Frog Princess joining the party?

  > A large, domesticated, flightless bird had been used as a pack animal for centuries, and was suddenly supplanted by the rails.

  [:(](https://www.youtube.com/watch?v=75417gQnauQ)
  ```

  - u/FatFingerHelperBot:
    ```
    It seems that your comment contains 1 or more links that are hard to tap for mobile users. 
    I will extend those so they're easier for our sausage fingers to click!


    [Here is link number 1](https://www.youtube.com/watch?v=75417gQnauQ) - Previous text ":("



    ----
    ^Please ^PM ^/u/eganwall ^with ^issues ^or ^feedback! ^| ^[Delete](https://reddit.com/message/compose/?to=FatFingerHelperBot&subject=delete&message=delete%20duz1m5p)
    ```

  - u/eaglejarl:
    ```
    > Well, this is going in all sorts of interesting directions. June needs to look into the backpack and see what sort of gear he can come up with from Earth.

    I'm really hoping for "something which includes an Internet connection", because that would be hilarious.
    ```

    - u/mp3max:
      ```
      He couldn't take out a laptop though so i'm guessin that's out of the question.
      ```

      - u/eaglejarl:
        ```
        Yeah, wheni wrote that I hadn't noticed that this was a three-chapter drop so I hadn't read the part with the laptop. Not too surprising, but also a pity.
        ```

- u/NotACauldronAgent:
  ```
  >like a mobile Dyson sphere for the soul

  Yep, reading rational fiction. Love it.
  ```

- u/None:
  ```
  [deleted]
  ```

  - u/XxChronOblivionxX:
    ```
    > starting

    Have you not been paying attention? She's been my girl since the end of the prologue.
    ```

    - u/abcd_z:
      ```
      I think I'd be most attracted to Valencia, myself.
      ```

      - u/Noumero:
        ```
        Best girl wars on r/rational. What has the world come to.
        ```

- u/the_terran:
  ```
  >I started with my favorites, Jelly Belly, Reese’s minis, Warheads, Sour Patch Kids, and then moved on to other things

  Being unfamiliar with American candy, for a moment I thought Joon nonchalantly pulled a couple warheads out.
  ```

  - u/sicutumbo:
    ```
    "Laptops are not allowed, for obvious reasons, but I don't see how high powered explosives could really change anything."
    ```

    - u/I_Hump_Rainbowz:
      ```
      nuclear warheads are WAY more common though. I am sure he can pull a few out.
      ```

      - u/PanickedApricott:
        ```
        I think nuclear weapons (at least magic based ones) were excluded. So maybe he could pull one out but it wouldn't work or something. Or maybe it does because because the mechanism isn't magical.
        ```

    - u/derefr:
      ```
      While reading the "fighting a dragon" bit, I pictured Joon, on an airship, trying to dredge up an air-to-air missile from the backpack to chuck at the dragon. He would fail—then internally monologue to the DM that it was really no more OP than Fenn's multi-void-arrow thing, really just different flavor—and then try again and succeed.
      ```

  - u/LordGoldenroot:
    ```
    Those are excluded.
    ```

- u/MaddoScientisto:
  ```
  Theodicy huh, having Unsong flashbacks here, I really can't wait to know more about the DM and his motivations.

  Also the whole chapter felt wholesome, sometime it's good to just lay back and see people get along and be happy, for once.
  ```

  - u/NotACauldronAgent:
    ```
    Next thing you know, AlexanderWales will announce he and ScottAlexander are the same person. They even share most of a name!
    ```

    - u/CannotThinkOfAThing:
      ```
      Yep, and the non-Alexander parts of both names refer to countries of the UK...
      ```

    - u/MaddoScientisto:
      ```
      I didn't even realize that!

      Scott Alexander Wales... but why stop here?

      Scott Alexander Wales Yudkowski, plus Wildblow, ErraticErrata and Nobodywhatevernumber

      Perhaps you too are part of the writer amalgamation!
      ```

      - u/NotACauldronAgent:
        ```
        Still, nobody's figured out The Waves Arisen. The author has started leaving hints as ANs, but they contain information no one should have access to, some of it classified, some of it merely secret.
        ```

        - u/jaghataikhan:
          ```
          Hang on, new info re TWA's author since it was released a few years ago? Didn't somebody do like a statistical linguistic analysis at some point and rule out most of the famous rational authors?
          ```

          - u/NotACauldronAgent:
            ```
            No, I was making a joke.
            ```

- u/cthulhuraejepsen:
  ```
  Typos here, please. (I'm still behind on typos from last chapter, due to a preference for writing instead of typo fixing, hope to catch up tonight or over lunch.)
  ```

  - u/sharikak54:
    ```
    "Discrete knock" in the last chapter should be "discreet".
    ```

- u/nytelios:
  ```
  That first chapter had so much going on and I thought it did an excellent job of capturing a D&D timed skill challenge with the race-against-time rush. Hope there are more of these! 

  Some parts made me laugh inappropriately though. Joon telling Val that she had to "hurt it to save it" like a parent with the tough love mentality - that won't come back to bite him, right? I laugh-groaned when it was finally clear why Mary was chosen as the nickname over Amy or Liss... Virgin Mary giving birth.

  > On Earth -- well, no, in the specific part of Earth that I grew up on, we’re raised to believe that there’s only one singular god, who made everything in the whole world, wrote all the laws of physics, set up all the rules the world works by, is omnipotent, meaning that he’s all powerful, he’s omniscient, which means that he’s all-seeing, and finally, the kicker, he’s omnibenevolent, which means that he’s all-good, as good as good can be.”

  When you phrase it like that, it looks like one of those super obvious "which one doesn't belong?" multiple choice questions.

  I'm wondering how the tuung can live in the Boundless Pit with their strict H2O needs. If it's like the hole in Cyoria, then they might have access to groundwater but that doesn't seem sufficient. Some sustainable source of water constantly pouring off the edge?
  ```

  - u/Mountebank:
    ```
    Ironic that Joon tells Val that she had to "hurt it to save it" and then later went on a whole thing about the Problem of Pain.
    ```

    - u/kaukamieli:
      ```
      Not really as Joon is not all seeing and all powerful who could just have put everyone into heaven alltogether skipping the pain.
      ```

  - u/derefr:
    ```
    > When you phrase it like that, it looks like one of those super obvious "which one doesn't belong?" multiple choice questions.

    Eh, maybe in that specific phrasing. I prefer Euclid's thought process that, basically, God is a Friendly AI, but specifically, God is the *Friendliest AI*—the *best possible* world-optimizer from a human perspective.

    So, to start with, definitionally, God is omnibenevolent—at least in the weak way the philosophers who first conceptualized that term defined it. Today we'd more say the Abrahamic God is taught to be globally optimizing for [something something] *of humanity specifically*, while not really caring so much what happens to other species. Homobenevolent. Anthropobenevolent?

    But, then, given that, of course God is also omniscient and omnipotent—taking control of the universe was an obvious instrumental sub-goal under the goal of becoming the Friendliest AI.

    And of course God exists rather than doesn't, because making Roko's Basilisk-like bargains from outside of time is *also* an instrumental subgoal of becoming the Friendliest AI.
    ```

- u/SoylentRox:
  ```
  I love how in chapter 82 they are literally on a train and appear to be _railroaded_ into a major quest, probably with a companion as a reward.

  Annoyingly, unlike Bethesda games, quests in this world often seem to have a time limit before failure.  The party may not be ready for heavy combat.
  ```

  - u/GeeJo:
    ```
    > The party may not be ready for heavy combat.

    I mean, thus far Joon's completed every quest he's received through the liberal application of combat/murder (Quills, Aumann, Unicorn, Larkspur, Fallatehr). The gang is pretty competent at it, all in all.
    ```

    - u/SoylentRox:
      ```
      Ok sure.  I was just trying to say that in a world with no respawn I would hate to feel forced into a time limited encounter.  I would rather get another companion, better gear, maybe figure out a better form of attack than swords or find a trainer for magic skills - do everything I could to maximize my odds of success. But this questline implies they may have to take on those guards in the next 2 days.
      ```

      - u/mp3max:
        ```
        I'm hoping that this new quest is something that requires more brain than braw for a change. It would fit with the fact that they aren't in good position for combat and give Valencia a time to shine with her demon-devouring powers. Something like a mistery to be solved or something.
        ```

- u/munkeegutz:
  ```
  Come on, Joon!  Copy Feen's scars onto your own body and try your best to patch the mistakes.  Write down the materials you would need for a more complete version of the scar magic so you can passively start collecting them.  Look at Fallatehrs scars and try to combine the knowledge from the two of them to build scar magic on as many companions as you can.
  ```

  - u/None:
    ```
    Opportunity costs. Juniper has very limited time (and even more limited time with his Essentialism boosted) and he decided that studying scar magic was not a high enough priority.

    Also, while it would be interesting to plenty of us, I suspect the author doesn't want to turn this story into nothing but thousands of words about magic systems.
    ```

    - u/munkeegutz:
      ```
      Nah he was able to pull it off with Fenn, so he should have instantly done the same for himself.  He had an hour of boosted essentialism left, and was out of things to do.  It's a tiny investment for being able to jump 30 feet in the air (and proportionate strength)

      Edit:  I agree that the author doesn't want to turn this into a lecture about magic systems, but a one paragraph doodad saying "I copied the scars onto my own body, but they didn't work out" or the such would have been enough.  Or "Surprisingly, the scars that works for Fenn were almost close enough to work on Amaryllis.  I duplicated them (with corrections) onto everybody's bodies, with their blessing."
      ```

      - u/nytelios:
        ```
        It's unlikely that Joon would be able to create a set of tailored scar magic ex novo. The original explanation by Fenn suggests it's neither quick nor easy:

        >You go through the pain of this scarring in very specific patterns, and when you’re done and they’ve healed, you can put your fist through stone or leap up a few stories into the air. The problem with it, aside from the perfection of technique needed to do the scarring right, is that the scars themselves need to be positioned properly upon the skin, and if the skin changes too much, the magic gets lost.

        So Fenn went through the legitimate process but the effect waned with time and bodily change. Reminds me of the blueprint theory analogy. Easier to fix loose shingles than make a new wing of a house.
        ```

- u/valeskas:
  ```
  >unable to project out because it was too weak

  Well, solution to that is pretty simple - Twinned Souls (Six-Eyed Doe), kind of strange that it is not mentioned. Maybe I missed it.
  ```

  - u/nytelios:
    ```
    That's a great idea! Very likely to be one of the potential answers since the Loyalty perks are unique. Challenges are time and difficulty of raising loyalty with the doe. Also the description was "will never lag behind you in relative power" so the rubber band might only tug one way since the locus should be far ahead of Joon as it is several hundred years old (or is a few centuries considered young for a locus?). Symbiosis offering the locus more magic a possibility?
    ```

    - u/derefr:
      ```
      > the locus should be far ahead of Joon as it is several hundred years old (or is a few centuries considered young for a locus?).

      My understanding of what Joon is perceiving when looking at the locus's soul is that it doesn't have *one*, because it isn't one being, but is rather an emergent property of a large number of independent souls making up its local ecosystem. In other words, the locus is essentially a [bryozoa](https://en.wikipedia.org/wiki/Bryozoa): many life-forms with independent DNA, but which function together as one larger organism in the same way the monoclonal cells of a multicellular plant or animal body do.

      This might neatly explain the waning of the locus's power: even if the emergent phenomenon of sentience of the locus has "cultural memory" that is old, if most of its *constituent organisms* are presently of a young age (because many of the older ones were left outside when its domain was sequestered to the bottle, and then the few remaining older ones died off), that might cause it to be less powerful than before.
      ```

- u/AurelianoTampa:
  ```
  Something I'm not understanding; Grak is the end result of a single founder line that has bred solely by parthenogenesis to avoid "drift," and as a result could be seen as a prince/ess. But Grak left Darili Irid because he was going to be forced into sharing a Kiss with a bondmate. 

  Seems odd that a line which prides itself on not drifting would force its heir into a Kiss with someone else... wonder if that's part of the reason Grak left?

  Also, someone refresh my memory, was there a conversation with Fenn and her views on children before? I seem to recall (or at least believe) that she's against the idea because she doesn't want to raise a child who had to face the alienation she herself faced as a half-elf, but I don't know if that was actually written. Or maybe this is some more evidence that Nellan is a child she had before?

  Next, I'm wondering why the two unknown companion connection lines disappeared when Joon came back from the DM discussion. His skill was still over 100, so it's not based on that... did the DM exclude something from him, perhaps?

  Finally, clarification question on chapter 80 when they're discussing the ritual; Joon originally says he could take Solace's druid connection to do the ritual, but she'll come back as a non-druid. Isn't Solace's druidity (fake words are fun!) what would keep the bottle stable? So what would be the point of even proposing that, besides getting Solace alive again. Locus would still die. 

  ... thinking about it, Joon was probably just speaking outloud, huh? Anyway, good chapters, lots of interesting stuff afoot :)
  ```

  - u/Noumero:
    ```
    > Next, I'm wondering why the two unknown companion connection lines disappeared when Joon came back from the DM discussion

    Possibly it was the DM removing some rails: initially, all companions were set in stone, and them joining Juniper was just a matter of time; afterwards, the DM removed connections to them, and decided to give Juniper more freedom as per his comments about narrative. It could mean that Juniper's group now has a pool of potential companions to choose from instead of preset two, or that they're free to dodge new companions.

    Alternatively, the DM just decided that letting Juniper see his future companions is too easy, and made the lines invisible.

    Alternatively, it was one of the "choices" the DM is apparently so fond of: he wanted to see whether Juniper would want to see his future companions or follow the suspicious black line; if he chose one, the other would disappear.
    ```

- u/ForMyWork:
  ```
  Nice, loved some of the interactions in these chapters. Amarillyis had some excellent moments, and their mini therapy session was well done. I'll be interested to see if they can stay uninvolved like they seem to want to, it's a good test of what the DM said to be true. Of course something may happen that will cause them to choose to become involved, something they couldn't ignore or the like. Still not necessarily forcing them (putting them in direct danger or need) but rather enticing them in some form.
  ```

- u/_immute_:
  ```
  I want to learn more about how these exclusions work. How are they enacted? I’m curious why Juniper seems to take for granted that they cannot be reversed.
  ```

- u/therealflinchy:
  ```
  >“Ah,” I said. “Right. Shit, sorry.” Grak waved a hand, dismissing my oversight.

  I don't quite follow this bit

  what oversight was there?

  EDIT:

  all party members technically kinda being royalty was a welcome, hilarious surprise. I mean, you could argue the six-eyed-doe even, would be top brass of all animals (beasts? spirit beasts? idk) currently.
  ```

  - u/AurelianoTampa:
    ```
    Last locus, queen by default? Ruler of druids?
    ```

- u/PanickedApricott:
  ```
  Maybe june can use the backpack to level up his engineering. It's basically a materials/machined part dispenser.
  ```

- u/infomaton:
  ```
  > “I just thought that you should know. We’ll see whether we can get through the next forty-eight hours without getting into trouble.”

  Joon realizes that this was intentional, I hope. I wonder what her motive is in seeking another companion.
  ```

  - u/akaltyn:
    ```
    Its also a way of testing the DMs pledge not to directly interfere by saying such a massive obvious dramatic irony hook.
    ```

- u/elevul:
  ```
  Yay for munchkinry! Nay for glossing over most of it haha. Kind of disappointed he didn't delve much deeper into finding ways to permanently enhancing himself while being at 180 Essentialism.
  ```

- u/Ace_Kuper:
  ```
  Juniper started as relatable, traumatized, but trying to do good guy. He had issues, but it seemed that he learned from them and was doing or aspiring to be better. It all started to go down for me after the narrative started to creep in, soul magic and Chapter 79 with DM was a culmination of his regression in my eyes.

  His part is only numbers for the most part, he could have asked the DM for Loyalty to not affect them, but instead he opted for "Double Tiff, but no Harem tho". Can loyalty even regress, frankly it should have if he told them the DM exchange as it transpired. He says he cares, but his actions speak otherwise.

  "You guys have free will, but I only say when you are around"

  "I don't want a harem, but let me ogle Valencia in my room while we are alone for no reason. Why he decided that being alone with her was a good idea?

  The problem with Narrative is - you don't need character motivation or logic. I thought DM encounter solved that, but it seems we are again on that track.

  There are other"rant" of mine here, I just think this is a summarized version of my problems. So it can be kinda separate.

  Edit: This was often compared to Mother of Learning. That series started with Zorian being distant, cold and not that caring for people or their struggle. As the time wen on he matured and even in the time loop physically and mentally reacted to negative things he had to do, even tho they shouldn't really have any effect on the "real world". Here Junipers thought more about "who is that Glenn in Fenns values" than he thought about killing people. Or he thought to himself that he should treat people of Aerb as real human, but even with Grak calling him out he replaced into only thinking about and not actually doing it.
  ```

  - u/WalterTFD:
    ```
    I don't get your problem sympathizing with with Juniper's motivations.

    Like, dude is generally trying to acquire power in order to become God and save Aerth from its myriad problems.  Like, he wants to fix the 'problem' of theodicy, make 'everything perfect forever'.

    That may not be literally 'what anyone would do' if granted the ability to rapidly acquire infinite power, but it is certainly not a huge leap.  Presumably if you were in Juniper's shoes you wouldn't just let Aerth lie fallow, but would be doing some variation on what he is up to, yeah?  Leveling up and gaining power, in order to 'win' and fix everything.

    As far as your harshness towards his imperfections go, I guess I can see that.  I think you don't make enough allowances for the difficulties of his situation, but if you can only relate to Clark Kent then I imagine if you wait long enough someone will write a story about a character who never makes mistakes.
    ```

    - u/Noumero:
      ```
      > Aerth 

      Fenn, how did you get access to this thread?
      ```

    - u/Ace_Kuper:
      ```
      >Like, dude is generally trying to acquire power in order to become God and save Aerth from its myriad problems. Like, he wants to fix the 'problem' of theodicy, make 'everything perfect forever'.

      Only motive he directly displayed with actions is Arthur. Other motivations are given by quests aka DM. Start was drifting with the flow and figuring out what is happening, that was good premise.

      But after that he isn't actually doing any of that. As soon as Arthur was back and alive somewhere, it all shifted to focus on saving him. He was willing to pretty much let Locus die in a form, i don't know how to help so if it happens it's not my fault and others voted in him to save it. Maybe saving a living being, that was very important to your companion, who died helping Juniper and saved the life of Fenn should have been a good enough motivation.

      With introduction of Narrative it felt like outside motives driving them and not really inner logic or motivation. Looking out for narrative threads was pretty heavy up to Chapter 79 and it seems to be back with the Chapter 82(Princess Boogaloo)
      ```

      - u/WalterTFD:
        ```
        I feel like you might be confused.

        The 'quests' don't actually assert any compulsive force.  They don't make him do anything.  He has chosen to do everything he's done so far.

        And what he has done, very obviously, is not 'rescue Arthur'.  

        The most recent thing he did was strive to rescue the Locus.  He is currently seeking a time chamber to resurrect Solace in order to rescue the Locus.

        You are talking like you think the vote was mind control or whatever.  I don't get it.  You understand that the only reason that the vote was binding is that he decided that it was, right?
        ```

        - u/Ace_Kuper:
          ```
          >The 'quests' don't actually assert any compulsive force. They don't make him do anything. He has chosen to do everything he's done so far.

          We literally had chapter upon chapter of party wondering that if they don't do quests and idle for to long DM would punish them or drop something bad as the response to their negligence. They are  wondering about the new princess in this current chapter, because "it might be a narrative thread". It's very much the compulsive force and the answer at the same time. Without those quests they could move at their leisure, be more aggressive or have a base of operations without fear of it being attacked because the narrative would demand it. Without the information in those quest descriptions Juniper would have been wandering aimlessly or actually had to learn about the world at large. It helps to keep the world disjointed and have blank spaces in it for future use. Quests pretty much set them on a path, they can approach them differently, but it's a path nonetheless.

          > The most recent thing he did was strive to rescue the Locus.

          No he didn't he voted against it. Valencias vote decided that they were going to save Locust right here and right now. He very much wanted to go and find the clues to save Arthur. Of course it not mind control, but his intentions were pretty clear, he even had a one on one talk with Valencia about "why you voted like you did". Locus conveniently didn't get a vote. He did all that was in his power to not save it at that moment and go for Arthur instead.

          >“Kuum Doona,” I said.

          >“Kuum Doona,” said Fenn.

          >“I want to save the locus,” said Val.

          >Fuck.

          Yeah, he seems so eager to help the Locus.
          ```

          - u/WalterTFD:
            ```
            You get that the votes don't control his mind or anything.  They are just people saying words to him.  He still makes the choice to save the locus, indeed, he still prioritizes it over saving Arthur.
            ```

- u/Ace_Kuper:
  ```
  So lat time i went on a pretty long "rant". I slept on it and thought that i was to harsh on Juniper and i should cut hims some slack.

  Cause his actions are good and he helped all those ... Huh

  He did that good deed...

  Well, it can't be at least his party members helped...

  So i discovered why i disliked the direction the story was taking, why i felt Junipers character was regressing, why meta"narrative" layer and soul magic were bothering me and a ton of other problems. All courtesy off me trying to find the good thing Juniper and his party did.

  So what exactly his motivation are in general, what moves him forward, what was his life goal? What is the goal of all of his comrades? What was motivation of his Earth friends?

  The overarching problem with the story is "telling and not showing". I reread previous chapter and Juniper is highly egoistic, hypocritical, asshole (the nicest word for him i can muster), he says something, but he acts completely different.

  The only two people that acted like they care for somebody else and really mean it so far are Tiff and Solace.

  So this are the problems that exist both in world and in writing that culminated in Chapter 79 (meeting the DM) and they are not that easily fixed if they are fixable.

  1) DM is a Deus Ex MAchina that motivates the living Deus Ex Machina of Juniper to function on Aerb. Without them the whole world doesn't exist. What i mean is Juniper is conveniently motivated by outside force that only exist to give him motivation. If Arthur was not existent here he would do nothing, if he could get Arthur right this instant other things would cease to exist.

  2) Juniper is obsessed with Arthur and he would trade anyone who is not Arhur for Arthur. He never learned his lesson of not being shitty to others and is ready to tready anybody for his Athur time. He holds the D&D books that Arthur had to a higher value than the "Deer" that is a living being, that was VERY important to Solace\friend that die helping you and saved the girl you "love".

  3) Souls stats are a problem, cause they put an anchor on the logic of the world that is too easy to check and it created problems when it clearly doesn't make sense. So Fallatehr can change values so that others follow him, it assumes he is at the top of that value list, right?

  Yeah, when at the top of Junipers it's

  1. Making excuses for himself

  2. Arthur (More than Fenn and Tiff combined)

  Power gap

  3.Level up

  This is not the 6th place
  >>And at the end of it, I want Arthur back. That’s the only way that this game is ever going to be worth the candle.

  4) Juniper double questioning and saying"I felt bad", but still doing it doesn't mean anything at this point. Actions speak more than words.

  5) All the philosophy, morality and psychology discussion in the world mean nothing when characters don't follow them with their actions. Frankly it portraits his whole friend group as a collection of shallow hypocrites. More so it does to Juniper,Arthur and Tiff. I was confused why they are having this discussion, but are not adapted to real world. I confused his age all this time, i thought he was in college, yeah, age of 17 only brings more problems from the time\story stand point.

  6) Bringing points or discussion to the story makes people think about them, it kinda makes them relevant. So we had that segment about feminism so. Now we a have a literal princess in the need of a rescue at the start, which would be fine only.

  1. Princess needs rescue in town.

  2. Princess needs rescue from a literal castle, she would be captured if not for Juniper.

  3. Princess needs rescue from the tower, she is captured.

  4. Princess needs rescue by killing a unicorn.

  5. Princess is captured for a second(3rd) time, she frees herself, but it wouldn't work if Juniper didn't kill Fallatehr.

  Great pattern of princess getting captured and being helpless.

  6) This next one requires it's own separate entry, cause even tho it is similar to other ones and is mostly "actions speak more than words", boy is it BAD.
  ```

  - u/munkeegutz:
    ```
    I think that many of the points you make here have merit -- specifically, it's hard to reconcile Joon's actions with the values in his soul (unless there's another way to slice them or there's more to the story than just the ordered value list)

    I especially disagree with your #6:

    1. Princess needs rescue in town.   ---> I suppose Joon helped, but she had void rifles and a soul cycle.  She might have managed on her own.

    2. Princess needs rescue from a literal castle, she would be captured if not for Juniper.  ---> She had the key and was waiting for him.  If not for Joon, she would have just ported out

    3. Princess needs rescue from the tower, she is captured.  ---> yup

    4. Princess needs rescue by killing a unicorn.  ---> I mean, she had a medical condition that made them need to kill a unicorn, but they also went through a ton of effort to revive Solace and fix Joons bones.

    5. Princess is captured for a second(3rd) time, she frees herself, but it wouldn't work if Juniper didn't kill Fallatehr.  ---> She actually took care of this one on her own rather handily.  I think she was fine.


    On the whole, I very much enjoy the story, and even though I disagree with many of your points, I appreciate that you made them in a constructive manner.
    ```

    - u/Ace_Kuper:
      ```
      You are correct on this one and this was one of the weakest ones. But it was more about the pattern for a princess to get into trouble in a somewhat cliche manner. Bandits after her>castle rescue>tower locked>unicorn>controlled against her will.

      1. Is fine on it's own.

      2. She is dead cause at this point she has Ratrot and only Juniper knows it or that they would need a unicorn to heal it.

      4. It lingers from the second point. At this rate she is not surviving without Junipers knowledge or power.

      5. It was more about her getting captured for the 2nd time. She did save herself, but if it wasn't for the convenience of (Soul link that juniper has) she Fallatehr would not let her go from literal mind control.
      ```

  - u/Ace_Kuper:
    ```
    >“Some personal things,” I said. “Things I don’t want to share, and that I don’t think it would be helpful to share. And … keep an eye out for a backpack, I guess. He said that there would be a magical one that could get things from Earth, a gesture of goodwill.”

    Yeah, it would not be. I mean Juniper said this first

    >I want Tiff. Two of her, one for him, one for me -- she’d kill me if she heard me say that -- and I want to unfuck everything somehow, make it so that I didn’t make so many mistakes, so many things I can’t possibly believe she’d get over them.”
    I want Tiff. Two of her, one for him, one for me -- she’d kill me if she heard me say that -- and I want to unfuck everything somehow, make it so that I didn’t make so many mistakes, so many things I can’t possibly believe she’d get over them.”

    “And Fenn?” he asked.

    “Fuck you,” I said. “I want Fenn too, god damn you, you fucking made her just for me, I knew from the start that Amaryllis was too pretty, terrifyingly pretty, I should have seen it with Fenn too, that you were just --” I shook my head. Manipulating me, but doing it with a full person that couldn’t even be blamed for that manipulation, who I loved in spite of the fact that she was designed to be with me. “Fuck you,” I said.

    Followed by this

    >I don't want a harem

    It really shows his ethics and how Fenn and Tiff(especially) are clearly more important when Arthur. Maybe if you don't want a harem stop acting like a horny teenager. Did he ever describe any of the Aerb girls by something besides them being beautiful and made to appeal to his physical taste? At this point when he says "I didn't want to peak at her being naked via soul link" i assume he stared like crazy, but just made an excuse for himself.

    Also, let me get this straight what he asked and question how exactly that was going to work.

    Junipers point of view:

    **I want you to create a copy of a 15-16 year old feminist girl for me and my 40+(500+) pal. Forget about the fact that i didn't speak to her in moths, she might have moved on, she doesn't like the 40+ in question and he doesn't care cause he had multiple wives,lovers and children. Forget that i did the whole speech about Aerb being a hellhole and totally unsuitable for a 15-17 year old girl from Kansas and she probably doesn't want tob e here**

    So at what point does he tell her about the sex clone of her for Arthur? How exactly it would work? Is she 15-16 at the time of her liking Arthur or 17 when after she dated Juniper and doesn't love Arthur? Would he like her sex clone to be reverted to being a virgin?

    Yeah, he is awful.

    Also story contradicts itself at times.

    >We drifted apart by inches until she was sitting somewhere else for lunch and the last text message from her (an unanswered ‘how are you doing?’) was months ago.

    >I’d been trying to mend things with Tiff, and it had almost seemed to be working, so I guess there was that.
    ```

    - u/eaglejarl:
      ```
      I'm not clear on why you're being downvoted, since I think your posts are constructive critique as opposed to criticism.  Having said that, I disagree with your take on the Tiff thing.  I read this as Juniper speaking directly from the id -- he *wants* this, but he recognizes that he *shouldn't* want it.  He knows perfectly well that these aren't reasonable (or perhaps even possible) things -- that's the point, he's telling the DM "I hate this situation so much that there is nothing you can plausibly give me that would make it right."
      ```

      - u/nytelios:
        ```
        I've read all of his previous posts and agreed/upvoted some of them because there were legitimate concerns but now I feel the posts have degenerated into a not-entirely-coherent rant where he's really committed to his own tunnel-vision interpretation and railroading his reading and opinion as fact or ultimatums of how Joon-the-teenager should/shouldn't think. That's very different from saying "I think Joon is acting like a complete asshole and hypocrite at times because of examples X, Y and Z. It makes me really uncomfortable that Joon even thought about requesting Tiff like a commodity for both him and Arthur."

        It's obvious that Ace_Kuper's a very invested reader, which is always valuable to a writer, but you can't blame people for downvoting a harangue.

        /u/Ace_Kuper - I also think Joon is an asshole sometimes. Personally I hope he continues to show his shortcomings, as it makes him more interesting than if he were a paragon of justice or "being of pure, perfect empathy." People are complex and make mistakes.

        I'm happy you mentioned the save-the-princess trope. I've been wondering whether Amaryllis is aware that she's routinely in some position of distress. She probably has one of the least complementary personalities to endure that and it seems to have had an effect on her confidence, so she probably isn't aware of the ever common damsel-in-distress plot. The anxiety will really start once Joon realizes this *and* that his party is now filled with princesses.
        ```

        - u/Ace_Kuper:
          ```
          It is incoherent at times, that's why i'm thankful for people disagreeing with me, that way i can clarify or acknowledged their points. A lot of those complaints flow from one to another and listing them in a good order is kinda hard for me, but it's fully my fault for not being clear\coherent enough.

          > I think Joon is acting like a complete asshole and hypocrite at times because of examples X, Y and Z. It makes me really uncomfortable that Joon even thought about requesting Tiff like a commodity for both him and Arthur.

          If it didn't came out a such that's my fault, but this was explicitly my point. I feel like he acts as an asshole and should put his actions towards his words.

          >I'm happy you mentioned the save-the-princess trope.

          See, this is funny. Cause other people heavily disagreed that this is the case and even i admitted that this was one of the weakest points i made.

          Some clarifications, i hope they are more coherent.

          1. [Response 1](https://www.reddit.com/r/rational/comments/80xryk/wiprt_worth_the_candle_ch_8082_peagodtail/dv025f7/)

          2. [Response 2](https://www.reddit.com/r/rational/comments/80xryk/wiprt_worth_the_candle_ch_8082_peagodtail/dv034yt/)
          ```

      - u/Ace_Kuper:
        ```
        >I read this as Juniper speaking directly from the id -- he wants this, but he recognizes that he shouldn't want it

        I read at as the same thing, mu problem is almost all of the things he does fall into - "I don't like this, but i will do it anyway or i shouldn't do this, but i will."

        That "Tiff moment" was just the last straw for me. Also, Soul magic having a clear number for "values" should not have really shown Arthur as 6th, he was willing to trade Tiff to make good for Arthur. Giving an underage girl to a 40 year old guys is not really a good thing.

        1. When talking about Amaryliss or other girls he constantly brings up how they "were created for me" and it's mostly physical.

        2. Why exactly he chose to take Valencia to his private room to be alone with her. There did this come from "My heart was hammering away in my chest, and I told myself that it was fear and anxiety talking." Like is he going to be like that with every girl.

        3. You can have low empathy, but he still should take responsibility for his actions. It's not the DM creating a harem when Juniper himself falls for the looks of every party member.

        4. Every time it's convenient for him it's either "they were created for me", but "no you are you and you have free will".

        This is what defines his hypocrisy for me. He says that i should change, but doesn't and backpedals with his actions.

        Unrelated to the Tiff, but related to the hypocrisy. "I couldn't feel any connection to the locus. I didn't understand the cultural significance of it". Well, maybe you should save it just on the basis that your party member just died helping you and she saved the life of a girl you liked. Or honoring someones memory only applies to Arthur and his D&D books that are treated with more reverence when a LIVING being. Like his admittance of "i was an asshole to people because of Arthur, i will try better" didn't solve anything, in fact i would say it became worse, cause now Arthur is Number 1 priority above living people that are near Juniper and their desires.
        ```

        - u/sparkc:
          ```
          In regards to Junipers ‘harem’, I don’t think it’s particularly controversial to point out that physical image is crucial to attraction for a lot of males and that you can’t choose what you’re attracted to. I personally would never judge someone on what or who they’re attracted to, only how they choose to act in regards to that attraction.

          Juniper is a teenager boy who has slept with a single girl in life and then been surrounded by a number of very attractive females who, at various points, show interest in him. He has done nothing unethical or been unfaithful at any point. If you ask me *that* fact is less believable than a story where Juniper caves in and sleeps with Valencia, or sneaks looks at Amarylis through the soul link or something similar.
          ```

          - u/Ace_Kuper:
            ```
            All of your points are valid, but the fact is,being attracted to them is on him and not on the harem flag that forces him to sleep with them. My problem is, he isn't admitting that, but rather shifting the blame of his possible actions on someone else. It's a flaw of his character, not a wrighting flaw. It's me disliking him for not taking responsibility for himself.

            There is a difference of liking someone and thinking to yourself "I might be not able to control myself cause she is so beautiful. His compassion for Valencia took a sudden turn to lust, even tho he saw her as a clueless innocent kid a couple of chapters ago.

            >He has done nothing unethical or been unfaithful at any point. If you ask me that fact is less believable than a story where Juniper caves in and sleeps with Valencia, or sneaks looks at Amarylis through the soul link or something similar.

            Not for the lack of trying. There is a segment in bold text that is in my other comment. He did try to do something super scummy and bad.

            [I want Tiff. Two of her, one for him, one for me](https://www.reddit.com/r/rational/comments/80xryk/wiprt_worth_the_candle_ch_8082_peagodtail/duz6dvq/)
            ```

            - u/eaglejarl:
              ```
              You really need to rewrite this.  I literally cannot understand what you're trying to say in that first paragraph.
              ```

              - u/Ace_Kuper:
                ```
                Fixed, that was a mess.
                ```

        - u/eaglejarl:
          ```
          [hypocrisy]
          It doesn't read that way to me, but okay.

          >  Giving an underage girl to a 40 year old guys is not really a good thing.

          Sure, but he's not thinking of Arthur as a 40-year-old.  He's thinking of him as the teenager that Juniper knew back on Earth.  He knows intellectually that Arthur is not older, but he hasn't accepted it emotionally.

          > Well, maybe you should save it just on the basis that your party member just died helping you and she saved the life of a girl you liked.

          ...that's what he's doing?  Like, he just sacrificed a bunch of skills for a cheaty-munchkin ritual so that he would have the ability to attempt to save it?  And now he and all his friends are spending days traveling in order to get to the place where they can take the next step on saving the locus?
          ```

          - u/Ace_Kuper:
            ```
            >..that's what he's doing? Like, he just sacrificed a bunch of skills for a cheaty-munchkin ritual so that he would have the ability to attempt to save it? And now he and all his friends are spending days traveling in order to get to the place where they can take the next step on saving the locus?

            he was going to pretty much abandon Locus, they voted on it, Juniper was going to do something else instead, but Valencia's vote decided that they should help. He specifically had a one on one talk with her about why she decided to vote like that. Also, all of a sudden he found her highly during that exchange.

            >Sure, but he's not thinking of Arthur as a 40-year-old. He's thinking of him as the teenager that Juniper knew back on Earth. He knows intellectually that Arthur is not older, but he hasn't accepted it emotionally.

            Okay, how about making a clone of a girl that loved you for your friend. She clearly stated that girls are not trophies to be won, but juniper wanted to give her as such for himself and Arthur.

            The problem that i have with Juniper is exactly that, he is not thinking about it, but only in cases that it involves other people. When it's about him making a decision he goes into the over thinker mode. My whole problem is he can justify any of his action, but it doesn't make them less bad and when he is calling out someone for the same thing he does, it's hypocritical.

            He specifically had problems having relationship with Fenn, cause she is older than him, he even thought about her as being immature for her age and that being a problem. Yet, he conveniently forgets about Arthurs real age and acts super immature when it suits him.

            Like i don't think he is badly written, but i do think he is an asshole kid who never interacted with the real world or people. He reminiscence about how Arthur had this talks about morality, but Juniper applies zero of it to real life.
            ```

            - u/eaglejarl:
              ```
              > Like i don't think he is badly written, but i do think he is an asshole kid who never interacted with the real world or people. He reminiscence about how Arthur had this talks about morality, but Juniper applies zero of it to real life.

              Okay...?  And?  I mean, sure, he's a teenager with poor social skills.  I'm not sure if your message is simply "I don't like him" or if there's some actual useful feedback here.  You're free to dislike a character, certainly.
              ```

    - u/derefr:
      ```
      I'm not sure if it would help your enjoyment any, but when I read this story, I'm mostly thinking of it as this:

      > Juniper is obsessed with Arthur and he would trade anyone who is not Arhur for Arthur. He never learned his lesson of not being shitty to others and is ready to tready anybody for his Athur time. He holds the D&D books that Arthur had to a higher value than the "Deer" that is a living being, that was VERY important to Solace\friend that die helping you and saved the girl you "love".

      ...being the *conflict* of the story. This is Joon's *character flaw*, introduced in the very first chapter. It's the thing he can't let go of; the thing he needs to get over. Aerb is here as a trial, a spirit-quest for him to go through that will lead to him figuring out how to let go of Arthur and grow as a person from there.†

      And he *has* started to do this, in a few small ways. For example, his relationship with Fenn is a lot healthier than how he was treating Tiff only a few months earlier.

      But, from my viewpoint, the "main arc" of the story hasn't begun yet, because that'll coincide with Joon actually having to let go of Arthur in order to save Aerb (in other words, explicitly choosing to grow rather than to be tied down to the past.) Everything happening right now—this is all a long demonstration of "pre-crisis" Joon.

      And yes, right now, Joon is an asshole. But I think it's promising that even Joon can see that he's an asshole. He hates himself, and is self-destructive (those two things coming together in him killing a version of himself in Ch. 79)—but I think he feels those impulses now more out of a revulsion for the way he was behaving before, on Earth, after Arthur's death. He knows, at least, that he *doesn't* want to be the person he was at that point. He just hasn't resolved who he *does* want to be yet.

      ---

      † And, because the story is "about" this conflict, Aerb basically *doesn't matter*. Only the Earth framing-device storyline matters. Aerb matters *to Joon*, and will eventually (likely) be the cause of his character development, but nothing that happens there will change things *for us*, as readers. This story is no more about Aerb—or Joon's companions on Aerb—than it would be if Aerb was another of the regular RPG sessions that Joon was playing. This story is, essentially, a one-man fever-dream stage-play. This is *A Christmas Carol* for gamers.
      ```

      - u/Ace_Kuper:
        ```
        I almost fully agree with you and it's my view exactly.

        1. My problem is he started on this "let go quest" at chapter one, but relapsed heavily at the point narrative and Arthur quest became a thing.

        2. It doesn't excuse him being an asshole to his current "friends?" and no amount of him thinking "i lashed out in real world, i should not do it again" would convince me he isn't doing the same thing again.

        3. People are heavily disagreeing that he can't let go of Arthur and is in a self\others destructing rush to get to him.

        >This story is no more about Aerb—or Joon's companions on Aerb—than it would be if Aerb was another of the regular RPG sessions that Joon was playing.

        This is the blessing and a curse, cause it makes the world aka Aerb that much disjointed and not real. The strength of this story is in the separated moment to moment happenings, but it breaks the connections between them. The journey is often more important when the ending, but if this whole journey doesn't matter it doesn't work. He should grow as the result of the journey, not because he needs to grow. He needs to let go , because he comes to some sort of understanding, not because it makes this story pointless otherwise.

        P.S. You are the same guy talking to me. Boy is this super disorganized now and hard to follow for anyone else.
        ```

  - u/dalitt:
    ```
    No one is forcing you to read this story — it’s fine if you don’t like it, but why spend so much time tearing it down?
    ```

    - u/eaglejarl:
      ```
      Clear communication powers, activate!

      Speaking as an author who has received lots of negative feedback over the years, I find that it comes in two categories:  "ur story sux!  Juniper bad guy!  I'm not reading anymore!!1!!"[1] and "I used to like this but it's gone off the rails for me because <reasons>"  The former type is easy to ignore.  The latter type is much more nuanced, and I divide it into "critique" and "criticism".  Critique provides useful and thoughtful evaluation of the story and its failings in a way that is actionable for the author (e.g. "Jess doesn't ever have an emotional reaction", one that I got on the first couple chapters of Tinker's Daughter).  Criticism is oriented around tearing the story/author down condescending, or simply offensive, or a whole spectrum of other BS.  

      Critique is gold; it's nice to get "Woohoo!  This is awesome", but it's the constructively critical reviews that help you grow as a writer.  They generally aren't *fun* to read, but they are usually useful.

      I think /u/Ace_Kuper 's posts fall into the "critique" bucket.  He's put significant work into thinking through what it is that bothers him and he's conveyed it in a clear and (IMO) polite manner.  There's no ad hominem[2] or offensive language, just a set of clearly-stated and actionable problems.  You might disagree with him on whether these are problems or not, but I don't think he's just trying to tear down the story.

      ----

      [1]  <tangent class="pet_peeve"> I've never understood why people feel the need to tell me when they're going to stop reading, especially when they don't say anything else...I mean, unless I know them personally, am I really going to care?  It seems awfully self-indulgent.  </tangent>

      [2] I've gotten every sort of personal criticism from "u sux as writer go die" to the far more insulting "Clearly, you aren't as talented or experienced as you think you are.  I suggest taking some classes before you try to publish anything again."  Ah, internet...how we love and hate you.
      ```

      - u/dalitt:
        ```
        I absolutely agree with you that constructive criticism (what you call critique) is useful, when it's well-thought out.  My most charitable reading of Ace_Kuper's posts, however, is that they're ill-thought-out and based on surface reading; I also think there's a fine line between what you call "criticism" and writing 1000s of words (in this thread and the last WtC thread) essentially repeating the same points over and over again.

        Even if you agree with the points made by Ace_Kuper (which I suspect you don't, based on what you've written), I'm also kind of annoyed by the tone, e.g. the sarcastic "Great pattern of princess getting captured and being helpless."
        ```

        - u/Calsem:
          ```
          Think of it like a bug report: a badly-written bug report with no replication steps is still better than no bug report, because at least you know you have a bug.
          ```

          - u/cthulhuraejepsen:
            ```
            ... except sometimes you don't have a bug at all, you have user error, and you spend time trying to track down the bug and replicate only to find that you can't replicate, or the thing the person was talking about as a bug was actually intended behavior.

            In terms of prose, I get the occasional spelling or grammar correction which is, in fact, wrong, which means that I spend time looking up the rule or googling the spelling for no practical reason. I would say that in these cases, having an incorrect error report is much worse than having no error report at all. (Signal to noise ratio is generally good though.)

            In terms of *interpretation* it's a little different, because I can't strictly say that someone's interpretation is *wrong*, and I do think that it's the author's job to create a text that gets interpreted how they wish it to ... but that doesn't mean that there can't be user error. I think that's especially the case when someone doesn't like something and is fumbling around in order to try to figure out why they didn't like it, and stumbles from complaint to complaint, none of which are really the problem that they've run into. All I get out of it is "I don't like this", which isn't anything that I find actionable.
            ```

            - u/dalitt:
              ```
              Yeah, rather than a bug report, this seems like someone complaining about *features* (e.g. that the characters have complex inner lives and are imperfect, or the interesting meta-narrative aspects of the story), along with a lot of weirdly overstated nitpicks (e.g. the timeline, which seems totally reasonable to me).
              ```

            - u/-main:
              ```
              > In terms of interpretation it's a little different, because I can't strictly say that someone's interpretation is wrong, and I do think that it's the author's job to create a text that gets interpreted how they wish it to

              So the fun thing about writing a serial story, and Wildbow has been playing with this in Ward, is that the author is *not* in fact dead. The text is a work in progress, and if there are reader interpretations in the fan community that run counter to your view of the story, you can have the text contradict that interpretation in a future update.
              ```

            - u/i6i:
              ```
              It reminds me of all those news articles that came out after season 1 of GoT saying they should have changed Eddard Starks death because having the lead die clearly doesn't work for a tv series.
              ```

    - u/Ace_Kuper:
      ```
      Because i liked it and there are still great elements in it, but it took a turn for the worse starting with the introduction of the "narrative" and being the lowest at Chapter 79.

      Like recent chapters are fine, but this things are kinda a problem for me. I also would expect to dispute my points or show evidence of me misunderstanding things.

      Like i think people, especially at rational fiction, should describe and talk about why the liked\disliked the thing.
      ```

      - u/dalitt:
        ```
        Well I disagree with your points in general -- I think they're based on a weird conception of what fiction should be.  But my complaint isn't about that; it's about the sarcastic tone and general meanness which I'm getting from what you've written.  If you don't intend your posts that way, my apologies, but please be aware that they can be read as mean-spirited.
        ```

        - u/None:
          ```
          Frankly, even if his posts were not intended to be mean-spirited, they're so poorly written and formatted that you can't be blamed for seeing them that way. It is *very* hard to take critique seriously when simply trying to understand it is a struggle.
          ```

---

