## [D] Friday Off-Topic Thread

### Post:

Welcome to the Friday Off-Topic Thread! Is there something that you want to talk about with /r/rational, but which isn't rational fiction, or doesn't otherwise belong as a top-level post? This is the place to post it. The idea is that while reddit is a large place, with lots of special little niches, sometimes you just want to talk with a certain group of people about certain sorts of things that aren't related to why you're all here. It's totally understandable that you might want to talk about Japanese game shows with /r/rational instead of going over to /r/japanesegameshows, but it's hopefully also understandable that this isn't really the place for that sort of thing.

So do you want to talk about how your life has been going? Non-rational and/or non-fictional stuff you've been reading? The recent album from your favourite German pop singer? The politics of Southern India? The sexual preferences of the chairman of the Ukrainian soccer league? Different ways to plot meteorological data? The cost of living in Portugal? Corner cases for siteswap notation? All these things and more could possibly be found in the comments below!


### Comments:

- u/acinonys:
  ```
  Is anybody here working i an artistic field? 

  I quit my phd in computer science (machine learning) and moved to a different town to study dance theatre. In general I enjoy my new live as a dancer and performer a lot and I love the community of dancers around me. In many aspects I have much more in common with them than with the computer scientists at my previous university.

  Sometimes it’s a bit strange though. My thoughts on a lot of subjects are very much lesswrongish. But I am surrounded by people, who take homeopathic medicine, believe in souls or some kind of afterlife, are into Chinese medicine…. Even concepts, which are very common in STEM communities like a certain trust in scientific progress as a positive thing and a reductionist way of thinking are not shared by many of my current friends. Not to mention more weird concepts like effective altruism or transhumanism, I usually don’t even try to talk about these. The few times I did try, it was a very frustrating experience.

  My main interest with this post was not to complain though. I am mostly curious, if there are other people here working in fields, which are far away from “hard science” and what your experiences have been.
  ```

  - u/GlueBoy:
    ```
    At least you'll be making about the same, between academia and dance theatre. :p
    ```

  - u/None:
    ```
    I have a lot of friends that are very into yoga, meditation, alternative medicine, 'wellness', etc. 

    I am a big fan of meditation, and I'm probably more into it than even most of my somewhat hippie friends, but I'm definitely far more skeptical than them. 

    Like, I'm hilariously high in Openness to Experience, I'm into all sorts of 'wooey' spiritual experiences/traditions (meditation, fasting, reading about all kinds of mystical traditions), and on the right day/night I can be persuaded of deism or some vaguely theistic tendencies...but that's tempered by basically reflexive skepticism and materialism. 


    So I share your experience. Out and out skepticism usually ruins the vibe of most conversations so I reserve it for certain friends/situations.
    ```

- u/ketura:
  ```
  Weekly update on the [hopefully rational](https://docs.google.com/document/d/11QAh61C8gsL-5KbdIy5zx3IN6bv_E9UkHjwMLVQ7LHg/edit?usp=sharing) roguelike [immersive sim](https://www.youtube.com/watch?v=kbyTOAlhRHk) Pokemon Renegade, as well as the associated engine and tools. [Handy discussion links and previous threads here](https://docs.google.com/document/d/1EUSMDHdRdbvQJii5uoSezbjtvJpxdF6Da8zqvuW42bg/edit?usp=sharing).

  ----

  Aw shit I forgot about the update today lol.  This last week I've had to work late nearly every day to make up for lost time last week, and on Sunday we're deploying a new version of the product again, so it's been a busy time getting that ready.

  ----

  I finally realized this past week one of the major reasons that javascript hasn't clicked with me yet, and that's due to me expecting frameworks to be mostly self-contained ecosystems.  I mean, if I pick Unity or Unreal to build a game with, I have a rigid foundation to build on, full of tools, archives, and asset stores.  I don't have to go outside those resources much once I've picked an engine, and I was expecting the framework decision to be much the same.  Now that I realize that a framework in javascript is basically just a *blueprint* of a foundation, I think I'll start meshing a bit better.  

  On that note, I'm probably going to end up using [Semantic UI](https://semantic-ui.com/) along with Ember, since Semantic has Ember bindings and otherwise seems to be fairly complete.  Besides UI, I don't *think* there's any major library I'll need for Bill's PC, but who knows.

  ----

  I have in the past mentioned Nethack's system of mechanic randomization, whereby the very building-blocks of the game are partially randomized, rather than just dungeon layout and loot tables.  For each ring, wand, and scroll, there are a variety of appearances, and what those appearances are linked to is randomized with each world. 

  Thus, getting a Tin Wand this run might be a Wand of Lightning or a Wand of Wishing or a Wand of Death and you have no idea which it might be, as you only know it's made of Tin.  Much of the early portion of the game thus requires a very scientific approach to loot; even if you've got the wiki memorized you have to experiment to figure out what it is you've stumbled across.  If you cast your wand at the floor, you might receive the message "the bugs on the floor stop moving".  Is it a wand of sleeping?  A wand of death?  A wand of hold monster?  You really don't know, but it narrows it down considerably without straight up giving you the answer.

  There's also secondary considerations: a Tin Wand will be resistant to heat but an Oak Wand will burn up if applied to fire and a Glass Wand will shatter if you fall too hard.  Thus even in cases where you have found all the answers and identified all the wands, you *still* have to play differently; where one run might have a Wand of Death made of iron and safe to bring against a dragon, in another it's made of wood and you might lose it before getting to cast it.

  I say this because this is probably one of the most rational game mechanics in existence, where even knowing what all the possible wands *are* doesn't straight-up let you win right away, and even in cases where you've done your Science and figured it all out, you *still* have to alter your playstyle to react to the Way The World Works (This Time).  

  I've been on the lookout for possible ways of including similar mechanics, and previously I thought it was going to be restricted to, say, pokeball crafting and the randomization of what parts do and what they're made of.  However, I think I've stumbled upon another aspect of the game that could benefit from a selective, experimentation-friendly randomization mechanic.

  When players create their characters, they can choose to be Psychic, Dark, or Aura users, or just plain vanilla baseline human (which is at least a bit psychic, but that's besides the point).  Each separate power path is a bit different: Psychics are a well-known phenomena, and getting teachers to train oneself is common and socially accepted.  They are moderately powerful if slightly uncommon.  Potential Aura users are actually extremely common, but due to the guru-in-the-wilderness style of training are not frequently utilizing their powers, and knowledge about it isn't disseminated very well. Darks are fairly rare; not unheard of, but not so common as to be a unique "protected status" or well-studied.  As far as most people are aware, it's an entirely passive powerset, mostly limited to psychic-immunity, with a side of YOU'RE STEALING MY SOUL accusations.  However, unbeknownst to the general public, if one can figure out how to actually train their Dark powers, then Dark humans are every bit of capable of using Dark moves as Psychics can use Psychic moves.  The trick is getting over that initial hump.

  The question came up of how to handle this.  Dark EVs would go up whenever Dark was utilized, so letting a Psychic attempt to scan you would make that EV go up, but it would lead to fairly unremarkable gameplay to essentially randomly get a message "Congratulations!  You've been passively scanned by your 4,559th Abra and have now unlocked Sucker Punch!"  There ought to be something else that the player can do between "hang out in Saffron a lot" and "Win Agatha's trust and get her to train you."

  (Oh, did I mention that?  Spoilers, I guess.)

  The idea is to have certain otherwise unrelated tasks be applied to training the various powersets.  For instance, perhaps upon earning Agatha's trust she grants you the secret of unlocking your first active Dark powers:  "Alright, I'll tell you...you must HIT a MAREEP at DUSK.   Yes, this is the one ancient Dark legend that turned out to be true! It may seem strange now, but rest assured, it is the beginning of the path I myself walked!"

  An ACTION would be paired with an OBJECT and a particular CONDITION.  These actions would presumably be things that would be beneficial to grind anyway...punching sheep as in the above example would in fact increase your ATK stat and would thus mean that playing as a Dark human this run would *also* lend itself to playing as a bruiser, since you're going to have to punch things anyway until you've got more useful skills to utilize.  

  However, due to the sheer number of combinations (even just 5 actions, objects, and conditions would be 125 different combinations) you're probably not going to stumble upon a winning combination accidentally, and even if you did, it might not be the one out of the three powersets that you chose.

  This is where things are a bit murky.  I kind of want there to be something like journal entries or tombstone engravings or what have you, some sort of information that you can track down to get you one piece of the puzzle.  "This old book says that an ancient Dark warlord's last words were...PIDGEOT EGG.  Huh.  Wonder if he had gone loony."  Suddenly, such information would narrow down the number of combinations to 25 in our example, which is more doable.  

  This does risk being a bit too gamey and random--impossible to guess if you don't have any pieces, incredibly easy if you stumble across one or two early.  I think the formula could be improved by having the information imparted to the player be ways of eliminating answers rather than straight-up confirming: "My grandfather, Dark as he was, was peculiar.  He always insisted we be thoughtful of what TERRAIN we were on.  An odd golduck, that man."  Thus the player learns that the secret dark training regime doesn't have to do with time of day, or apparel, but maybe has to do with standing in a river or glade or cave: narrows it down without giving away the answer.

  Anyway.  The idea will need refining, but I'm excited to see if this information-gathering mechanic can be coaxed into a general-purpose Science mechanic that could be applied to more than just power training.  As usual, any thoughts or comments are more than welcome.

  ----

  If you would like to help contribute, or if you have a question or idea that isn’t suited to comment or PM, then feel free to request access to the /r/PokemonRenegade subreddit.  If you’d prefer real-time interaction, join us [on the #pokengineering channel of the /r/rational Discord server](https://discord.gg/sM99CF3)!
  ```

- u/DaystarEld:
  ```
  Finally finished my Success/Failure reread of HPMOR! You can find it and my analysis [here](https://www.reddit.com/r/HPMOR/comments/7do4y7/hjpev_successfailure_reread_chapters_100end/).
  ```

  - u/trekie140:
    ```
    I do agree that arrogance is a valid character flaw, though I can see why people are averse to it since I really don’t like when that arrogance doesn’t seem to significantly hinder them to achieving their goals.
    ```

- u/rationalidurr:
  ```
  Code Geass Season 3 soon! git hype!
  ```

  - u/CouteauBleu:
    ```
    ... But but but eternal peace between the nations?
    ```

- u/holomanga:
  ```
  TOMT: I remember reading a rational fic some time ago, called or subtitled something like Alex in Wonderland, but what I recall of the plot is fuzzy and I can't find it.

  The main character was a significant human, and fell into some kind of human reserve, where I think there was some population engineering going on. They find their way out, by following a multi-legged robot, into a surrounding maintenance area - I recall a scene where the robot walked on top of him, but the pressure was low enough that he was uninjured.

  At some point in the story, possibly through flashbacks, it's revealed that presently there aren't many humans left and that they slowly phased out in favour of robots, the Earth is a biologically uninhabitable robot-world, and that the main character(?) or the robots(?) have memories from earlier versions of themselves in the distant past of being in a lab able to walk independently and looking intimidating, and of being a military robot that was commanded by an inspecting general that it was being pitched to to shoot itself(?).

  I think some of the flashbacks, or the information nature of the world, came to the main character in the form of a dream.
  ```

  - u/FormerlySarsaparilla:
    ```
    http://sifter.org/~simon/AfterLife/chapter_1.html
    ```

- u/GaBeRockKing:
  ```
  Pokemon Ultra Sun and Ultra Moon just got released today. Does anyone else plan to get it?

  Personally, I already own Moon, so I'm buying Ultra Sun. I used Primarina in my previous playthrough, so I'm split between either using one of the other starters, or bringing in a bred pokemon from moon by using a friend's DS as an intermediary.
  ```

- u/Norseman2:
  ```
  I'm world-building a Pathfinder setting (similar to D&D 3.5) and trying to solve one particularly nasty problem: why there hasn't been a vampire apocalypse. Think of your ordinary zombie apocalypse, and now imagine those zombies as vampires. Intelligent, able to turn into a giant bat or a cloud of gas, dominate your mind, heal rapidly, spider climb, and each vampire can create up to two new vampires who are utterly enslaved by it. However, if said vampire dies, those vampires it controlled become free-willed and able to do as they please.

  The only things which can kill them are sunlight or having a wooden stake driven through their hearts followed by severing their heads and anointing them with holy water. If killed by any other means, they turn into a cloud of gas and have two hours to make it back to their coffin where they will be able to regenerate within an hour. Their only other weaknesses are inability to enter a private home or dwelling without permission, and a strong repulsion to mirrors, holy symbols, and garlic.

  I don't see any good reason why a world with even a single free-roaming vampire would not rapidly turn into a vampire apocalypse. Any thoughts?
  ```

  - u/alexanderwales:
    ```
    Though I don't *believe* this is the case in 3.5 D&D, vampires requiring blood is a major impediment to their spread. If a vampire needs 1 pint of blood every day, and a human can safely give 1 pint every month, then the maximum carrying capacity for vampires is 1:30, though probably even more lopsided because you can't safely extract blood from e.g. babies. Maximum extraction of blood from the humanoid population is a vampire dystopia, not an apocalypse; the apocalypse only happens if the incentives for the creation of new vampires result in a tragedy of the commons where the humanoid population is wiped out, resulting in the eventual end of the vampire population as well.

    So basically, your free-roaming vampire has to *want* to create more vampires ad nauseum, which I don't think that he necessarily does, so long as he's constrained by the resource of blood, or maybe not even then. More vampires means more attention, and inevitably means more knowledge of vampire weaknesses, along with organized counter-forces dedicated to operating against vampire-kind. A free-roaming vampire can do as he wishes, with his freedom guaranteed by the difficulty in seeing his patterns; if there are too many vampires, then you have people walking around with mirrors, garlic, holy symbols, etc., never inviting anyone into their home, and adopting other anti-vampire practices.

    It seems to me that it's to the benefit of every vampire, at least in the long-term, to ensure that as few people know about vampires as possible, and to ensure that the vampire population is small and controlled. That is, unless the vampires want to conduct war and make a play for taking over civilization, and that somewhat depends on what the civilization in question looks like.
    ```

    - u/Norseman2:
      ```
      For Pathfinder, vampires do not strictly require blood to survive, though they suffer penalties without it, including compulsions to feed. It would be possible for a vampire apocalypse to end in a world filled with vampires who must feed off of livestock because all of the people have become vampires. However, feeding on sentient victims creates a euphoric sensation for vampires, and is compared in the rules to a drug addict 'satiating her inner demon,' so feeding on livestock would not be the ideal situation for the vampires.

      The way I see it, I suspect that the first vampire would probably start off enjoying more or less free reign to feed its addiction, committing assaults here and there to render victims helpless for feeding. Eventually, people with proper weapons and magic would follow the vampire's tracks and try to kill it. If it survives, it would likely see the need for creating vampires to help protect itself, and the arms race would begin. Eventually, some of its subordinates would be killed while their thralls remain alive, and there would start to be multiple factions of free-willed vampires, leading into a tragedy of the commons scenario and eventual vampire apocalypse.
      ```

      - u/CCC_037:
        ```
        Vampires are often described as being smarter than the average human. Perhaps they can foresee the tragedy of the commons, and will slap each other down to prevent it if any of them starts going too far...
        ```

  - u/Escapement:
    ```
    The reason that this hasn't happened is quite obvious, and spelled out in the rules explicitly. It hasn't happened because the Shadow Apocalypse happened first and wiped out the world even faster and harder - Shadows being CR 3 undead who are all incorporeal and thus basically even more unkillable for your average commoner than a vampire is, and also their spawning from killing people takes 1d4 rounds instead of 1d4 days. So a Shadow Apocalypse should wipe out your given civilization that consists mostly of people without magical weapons at a rate approximately 1,440,000% faster, thus explaining why a Vampire Apocalypse would never wipe the civilization - they're much too slow, the Shadow Apocalypses always run to completion first. They aren't even repelled by threshholds or anything, a single Shadow should be able to kill an entire village and make everything it killed into killers in a single night, they even pass through walls.
    ```

    - u/Norseman2:
      ```
      The Shadow Apocalypse is a very good point and I love the name. It looks like that would spread at nearly 100 miles per day. However, the RAW state that shadows are content to stay in one place, sometimes even just one building in a town, leaving other buildings unscathed.

      As such, to have a Shadow Apocalypse, you'd need a necromancer who created the first shadow and orders it to direct its spawn to wipe out everything. Assuming the world survives the first Shadow Apocalypse, subsequent attempts of that sort should be quite feasible to disrupt. In the event of an impending Shadow Apocalypse people could simply use divination to figure out who was controlling the shadows and kill that person plus the original shadow to stop the spread.

      In contrast, with vampires, taking down the upper echelons of the hierarchy just leaves you with an increasingly free-willed cluster of varying vampire factions. Also, note that vampire mages can teleport, block divination, specifically assassinate mages who try to stop them, etc. And each mage killed by vampires is likely to become a new vampire mage. Once the vampire apocalypse begins, I don't see an easy end to it.
      ```

      - u/Escapement:
        ```
        Another name for the Shadow Apocalypse is the Shadow Over The Sun. If the Necromancer directing this has Mind Blank up, goodbye cruel world - I strongly recommend Mind Blank for the discerning wizard attempting to bring about the end of the world, and that spell by itself is a strong argument to not take Abjuration as a banned school in 3/3.5... though in Pathfinder the penalties are much less burdensome for specializing, of course.

        Anyways, to perhaps be more helpful regarding this sort of thing - there are a few fan-written supplements for D&D 3e/3.5 which you could use in a Pathfinder game with appropriate changes, that address this and similar consistency problems. These are the Tome series were written by Frank Trollman (who also wrote for Shadowrun 4 in e.g. *Street Magic*) and K, and distributed for free online:

        [The Tome of Necromancy](http://www.tgdmb.com/viewtopic.php?t=34248)

        [The Tome of Fiends](http://www.tgdmb.com/viewtopic.php?t=28828)

        [Races of War](http://www.tgdmb.com/viewtopic.php?t=33294) 

        [Dungeonomicon](http://www.tgdmb.com/viewtopic.php?t=28547)

        As well as providing interesting flavour and character options for a lot of popular archetypes that had been ill-served by the official rules, the authors restrict certain problems like the Vampire and Shadow spawning problems to make the established world more plausible by curtailing these paths to power a bit. In these houserules, Vampires created from characters of less than fifth level are only Vampire Spawn (who can't make more vampires), and of course fifth level and higher characters can conceivably defend themselves and in any case are significantly rarer; shadows are restricted in the section on Pools of Deep Shadow, which essentially restricts the area that Shadows can travel around and prevents spawn from eating the entire world. They also address a lot of other rule issues that are more 3/3.5e specific, and I'm unsure how much of these issues are still present in Pathfinder.

        I strongly recommend reading them even just to mine for ideas - the Races of War depiction of the Sahuagin is one of the most hilarious pieces of flavour for the background of a campaign I've read:

        >#Borderlands of the Sahuagin: Sore Winners

        >The first thing to understand about the Sahuagin is that they have already won. Completely. The surface of the world is about 3/4 ocean and they own almost all of it. From the standpoint of the Sahuagin, the only places on the planet that have non-Sahuagin races in them are the stale crusts that they already had the presence of mind to cut off their sandwich. All of the non-Sahuagin races are all ghettoized. Even the other aquatic races have been marginalized to the point where they only get the brackish water (Locathah), the rocky shallows (merfolk), the underground darks (Kuo-Toans), or the muddy salt marshes (Lizardfolk). The real real estate – the ocean and coastline – are pretty much the private playground of the Sahuagin.

        >Individually, Sahuagin will kick your ass, and collectively they will kick the ass of any nation you happen to support. The combined populations of all other sapient races on any planet are less than the population of Sahuagin on that planet. The Sahuagin are also much smarter and better organized than you are so their cities are actually more productive than yours per person in addition to the fact that they have more cities than all the other races and their cities are more populous.

        >The Sahuagin mutate constantly, but are not inclined to Chaos. They just all have different appearances and capabilities. But every one of them is gifted with super intelligence and thick natural armor. The Sahuagin deep seers are some of the most gifted wizards on the planet and honestly have nothing better to do than just scry on crap and tell the armies where there's some cool stuff to go loot. From time to time the Sahuagin will come onto land to beat the living crap out of people and take control of important or valuable items. Then they take the spoils of war and drag it back under water, laughing the whole time.

        >Against this backdrop of crushing inferiority, how do the other races maintain? Most of them are fighting for stakes so small that they haven't even *noticed* that the vast majority of the planet is owned and operated by brutally efficient fish men. But one race that certainly has noticed the power discrepancy is the race of elves most likely to be forgotten: the Sea Elves. They actually live in many of the same areas and have a war going with them.

        >Life is hard for a Sea Elf, because every one of them is born into a post-apocalyptic world where mutants run amok and hunt them for sport. But it's actually even worse than that because in addition to simply being physically and intellectually inferior to the Sahuagin like everyone else is – they are actually stupid and useless *even contrasted with the surface races*. An average Sea Elf is as much the intellectual inferior to a Sahuagin as a Griffin is to a normal human. The Sahuagin consider the Sea Elves to be little more than animals, and they aren't wrong.

        >The Sea Elves keep surviving at all because they see farther than Sahuagin in low-light conditions (and are thus often able to *swim away* from potential encounters with Sahuagin during the morning and twilight hours that Sea Elves leave their hidden nests), and also because every so often a Sahuagin gets born who looks exactly like a Sea Elf. These Sahuagin mutants, called Malenti, are a little bit worse than a normal Sahuagin in that they lack the rending claws. But they're still stronger and smarter than any Sea Elf that ever swam the 7 seas. So when these Malenti realize that they get a crap deal from Sahuagin society, they often as not run off to join the Sea Elves, where they almost immediately rise to positions of leadership. They also gain crap loads of experience very quickly because the odds are so stacked against them. In short, the reason that the Sea Elves still exist is that they actually are a splinter faction of Sahuagin that uses real sea elves as beasts of burden instead of simply hunting them like the more normal Sahuagin groups do.

        >And yet, despite the fact that the Sahuagin have **won** at **everything**, they still continue to fight the other races and take their children and stuff. Partly this is to feed the insatiable demands of their Baatezu masters, and partly this is because on some deep level the Sahuagin are convinced that it actually couldn't possibly be that easy. In addition to looking for bling and candy to take from the weaker races, the Deep Seers are also combing the world for the one thing that the Great Mothers are pretty sure exists somewhere: the hidden army that the other races are putting together to take the world back from the clutches of the Sahuagin Empire. As far as anyone knows, it doesn't exist, but for some reason the Great Mothers keep insisting that the searching continue. Maybe they know something we don't?

        >**Campaign Seed: Free Your World**

        >The Sahuagin have pushed things too far. After the leveling of the city of Kelport, the remaining peoples of the land have at last come to realize the danger that the Sahuagins' unchecked strength poses. The natural alliance of pretty much everyone against the Sahuagin has formed. But how far can you trust your allies? Will the goblins really show up when they said they would? And does everyone together have the strength to topple the coral spires of the Deep Seers?

        >**Campaign Seed: The Price of Hubris**

        >In ages past, the Sahuagin conquered the seas of the Kuo-Toa. They crushed their temples, and slaughtered their children. And noone liked the Kuo-Toa because of all the sacrificing people to the Great Evils they used to do, so noone did anything about it at the time. As massively successful empires are wont to do, the Sahuagin have allowed themselves to become decadent and haven't been crossing their Ts particularly, and now the Great Evils are straining to enter the world. That's... unfortunate... because these ancient and malevolent forces have the power and inclination to destroy everyone on the planet. And to make things worse, while some of the Sahuagin are aware of the problem and contracted our heroes to help solve it, lots of other Sahuagin refuse to acknowledge that any problem could possibly warrant getting help from outsiders and will work against you at every turn.
        ```

  - u/cellsminions:
    ```
    In a previous 3.5 setting I had, Maruts [(d20pfsrd link)](http://www.d20pfsrd.com/bestiary/monster-listings/outsiders/inevitable/inevitable-marut/) tracked down each type of undead, so there'd always be at least one high-level automaton tracking down and slaying vampires on the material plane.

    I've also run a Pathfinder campaign where the world was mostly overrun by undead before the remaining people managed to get a barrier up to protect themselves. Roughly 1/4 of the world sits behind a high magical wall with a terrifying number of undead just barely visible on the other side, waiting for the barrier to come down.

    It's possible some deities see a significant rise in vampire population as one particular god or another trying to seize more power, and in turn, send their own champions to strike down the offending vampires.
    ```

    - u/Norseman2:
      ```
      Maruts are a very good point, particularly for intelligent undead. It would probably take considerably more than one to balance things out, but Maruts could certainly be invaluable for constraining the spread of vampirism.
      ```

  - u/sicutumbo:
    ```
    Not familiar with Pathfinder, so take what I say with a grain of salt.

    If someone wanted to kill a vampire, could they not expose said coffin to sunlight, then kill the vampire through normal means? Basically just wreck their home during the day, and the vampire has no ability to escape. Any vampire set on overrunning a society would have to face quite a bit of push back from people who would otherwise be unwilling to take the risk of attacking them.

    Other options could be that vampires are unwilling to overrun society. Turning everyone into a vampire means that either they run out of humans to feed on, or they have to farm humans for blood. That sounds like quite a bit of work when they currently are an Apex predator surrounded by food.

    Or possibly vampires are limited on the number of vampires they can enslave, and are intensely antisocial towards other free-willed vampires. I'm assuming from your post that the two enslaved vampires can enslave others. If the original vampire can only control, say, two levels down in that hierarchy, and free willed vampires are otherwise in a constant power struggle, you would never have a party of more than 7 vampires acting with any degree of coordination. That's threatening to an individual, or small parties, but not a threat to a society or a decent army.
    ```

    - u/Norseman2:
      ```
      >If someone wanted to kill a vampire, could they not expose said coffin to sunlight, then kill the vampire through normal means? 

      Absolutely, yes. However, to do that, you'd need to delve into whatever cave, dungeon, sewer or basement that the vampire placed has its coffin in and fight the vampire on its own turf. You may need to deal with traps the vampire has laid. It's likely going to be very difficult and there's good odds that many people will die in the process, but it is feasible.

      >Turning everyone into a vampire means that either they run out of humans to feed on, or they have to farm humans for blood.

      I don't expect it would be intentional. I suspect it would happen naturally as a result of free-willed vampires creating a tragedy of the commons kind of situation.

      >I'm assuming from your post that the two enslaved vampires can enslave others.

      Yes, so theoretically you could have a single vampire indirectly controlling millions of vampires. Each vampire only gets direct control of its own spawn, but it can command its spawn to command their spawn to command... etc.
      ```

      - u/sicutumbo:
        ```
        > Absolutely, yes. However, to do that, you'd need to delve into whatever cave, dungeon, sewer or basement that the vampire placed has its coffin in and fight the vampire on its own turf. You may need to deal with traps the vampire has laid. It's likely going to be very difficult and there's good odds that many people will die in the process, but it is feasible.

        Ah, never even considered caves. I was picturing a group of people throwing bombs or fireballs or whatever is appropriate at a house or mansion. Guess that shows my bias from living in a flat area near the coast.

        > I don't expect it would be intentional. I suspect it would happen naturally as a result of free-willed vampires creating a tragedy of the commons kind of situation.

        I'm not sure this applies. I'm postulating that the end state is undesirable, even in a world where there is a single vampire. If a free willed vampire finds that living in a predominantly human world is desirable, and that adding additional vampires gives diminishing returns, and the cost of keeping said vampires fed is linear, the free willed vampire wouldn't have any incentive to enslave more vampires beyond a small number.

        For an example, say 4 vampires inhabit a large forest, with a few towns along the border with a total population of 40,000.  They need to feed on one human a month. The human cost is basically lost in the noise of people dying in the forest. Does having 40 vampires improve the master vampire's quality of life? Does it improve it in proportion to the increased difficulties of feeding 10 times as many vampires?

        > Yes, so theoretically you could have a single vampire indirectly controlling millions of vampires. Each vampire only gets direct control of its own spawn, but it can command its spawn to command their spawn to command... etc.

        That's what I thought. It would be a bit silly for this post to exist if it was firmly established that the slaved vampires can't control other vampires.
        ```

  - u/MugaSofer:
    ```
    Because Pathfinder vampires [suck](http://www.d20pfsrd.com/bestiary/monster-listings/templates/vampire/) (no pun intended).

    >If killed by any other means, they turn into a cloud of gas and have two hours to make it back to their coffin where they will be able to regenerate within an hour.

    Yeah, they flee back to their coffin ... at 4.5 mph, helpfully leading the prospective vampire-slayers back to their lair at a leisurely walking pace. And then they spend an hour orporeal and Helpless.

    In addition, it's "very difficult" (DC 25) and takes at least two rounds for them to approach or attack a person with a holy symbol (or a mirror, or garlic), they can't enter homes, and they suffer grievous damage from water - not holy water, just ordinary running water.

    Sure, they're superhuman ... sort of. But they're not super-angry-human-mob.

    Newborn "vampire spawn" are even weaker, can't reproduce, and AFAICT there's no rule for how long it takes for them to develop into proper vampires.

    Oh, and Pathfinder vampirism can't spread beyond the original species, so in the event that a vampire apocalypse did occur all other sapient species would be fine:

    >A vampire can create spawn out of those it slays with blood drain or energy drain, provided that the slain creature is of the same creature type as the vampire’s base creature type. The victim rises from death as a vampire spawn in 1d4 days.

    So if you really need an excuse for every village to have a *Decanter of Endless Water* for easy Vampire extermination and every villager to wear a holy symbol (which one would assume they would anyway TBH), you could always kill off a minor breed of Elves to vampire plague in the backstory to forewarn them.
    ```

  - u/kraryal:
    ```
    Well, the Two Year Emperor solved this problem via direct divine intervention. Wraiths, IIRC, have the same problem. Anything killed by a wraith can become one. What they did there was drastically reduce the probability that turning would work.

    Terry Pratchett solved this problem culturally, in Lords and Ladies. Vampires that bred too quickly, or stepped too far out of their behavioural expectations were slapped down by everybody around.

    Both of these have a "created already in motion" aspect. If nobody knows the vampires are a problem, you won't get the coordination to work either solution. 

    But where does the first vampire come from? Was it made by a dark god? Perhaps that god doesn't want the world to be boring and peopled entirely by vampires. There's nobody to torture, for instance. So that god might "sit" on vampires, or instill compulsions, or maybe make the vampire maturation process take longer.

    Maybe the first vampire was made by a wizard? Then the god of magic could do similar things, or let all the other gods know. The wizard could be smart, and tell people about the problem, so that anti-vampire crusades are a regular part of the local culture.

    A world with vampires, that still exists, will have all sorts of things built into the culture for dealing with them. You don't go down dark alleys, well, these guys won't either. Everybody will wear holy symbols, public building will be filled with mirrors, garlic oil on the door posts, etc. 

    Finally, why does the first vampire want to spark an apocalypse? Maybe he likes the world the way it is. Better to be a legend that nobody believes is real, then there aren't holy symbols everywhere when he's trying to get lunch. Maybe he tried it, and the gods slapped them down, so now every new vampire is taught to keep things low-key out of self preservation. Then if you get a crazy vampire who doesn't follow along, the others might keep him in line. They know his weaknesses, after all.

    There's a ton of divination magic in Pathfinder. Some vampire causes trouble... scry up his coffin and send some people to burn it while you distract the vampire somewhere else. Now he's as killable as anybody.
    ```

- u/trekie140:
  ```
  I watched The Good Place because a recommendation on this sub led me to find a lot of praise for a show that flew under my radar despite being created by one of the people behind Parks & Rec and Brooklyn 99. Unfortunately, I ended up very disappointed by the series.

  I like Parks & Rec and Brooklyn 99 because they are more than just comedies, they tell stories you can (sometimes) take seriously with characters who undergo development on top of being funny. So I immediately began looking for an underlying theme of The Good Place. 

  From the start, I thought the show was going to be a satire of W.E.I.R.D. culture. We’d see a heaven and hell based on the morality of modern middle class liberals, the target audience of which I’m a member, only to see how such a system can still be discriminatory and somewhat arbitrary.

  Eleanor would be a narcissist who couldn’t learn empathy, Chidi an intellectual who never did anything important with his knowledge, Tahani a pretentious elitist who only helped people for the social status, and Jason a street kid who simply didn’t know any better. I thought it was a brilliant idea.

  Turns out, that was not what the show was about at all. It was just a comedy about characters who are idiots and assholes who get humiliated and actually do deserve exactly what the afterlife gave them because heaven takes context and intention into account, except I don’t think that makes sense.

  Eleanor, Tahani, and Jason’s upbringing made them who they were and the latter seems mentally incapable of understanding the consequences of his actions. Even Chidi is stated to be solely responsible for his own failures even though I think he suffers from an anxiety disorder.

  I get that we’re supposed to root for these characters in spite of their flaws or still consider their fate unjust, but I thought the way the ending recontextualizes the characters within the story  completely undercut the set up. After that, I didn’t care about what happened to them because they didn’t seem to have any control anymore.

  It’s not that I think the show is bad, it just turned out to not be what I wanted it to. I thought it was a subtle social satire that disguised itself as an odd unsubtle comedy, but it turned out to just be a comedy that I never found all that funny in the first place.

  It’s almost exactly the same thing I felt toward The Unbreakable Kimmy Schmidt. A goofy satire that seemed to be really about the determination to survive in the crazy world we live in, only for the plot to go where I didn’t want it to and all that’s left are jokes about people being dumb.

  I can’t just laugh at idiots and assholes because of what they do, there needs to be some wit to the writing or substance to the story to get me to care. SAO Abridged, Faiser, early Brooklyn 99, and Sirens managed to do both and I love them all, but even just one of those would be enough.
  ```

  - u/DaystarEld:
    ```
    To me, it was a relief to see the big reveal because there was just so much wrong with that notion of Heaven that I was constantly distracted by it. I get that things like loving Nickleback being worthy of going to hell is The Joke but it was just too absurd to be taken seriously enough for me to care about the characters. 

    I like your perception of it as social satire, but don't think that was necessarily undone by the reveal. Instead, the core message of the story to me seemed to be that People Can Change, even those consigned to an eternity of torture, and if that's true then there's something even more fundamentally broken with the system.  I haven't seen season 2 so I don't know what direction they take things in, but if the series doesn't end with them causing an utter breakdown of order in the afterlife by proving that people can actually be redeemed if they meet the right people and are put in the right circumstances, I'd be very surprised/disappointed.
    ```

- u/trekie140:
  ```
  I just got introduced to the Polity novels by [this short video](https://youtu.be/EfszijxnVCg) and have never been sold on a book series so fast, it sounds like just the right mixture of hard and soft sci-fi I’d love, but have been unable to find an ebook or audiobook version on Amazon. Does anyone know where I could find one?
  ```

---

