## [D] Wednesday Worldbuilding and Writing Thread

### Post:

Welcome to the Wednesday thread for worldbuilding and writing discussions!

/r/rational is focussed on rational and rationalist fiction, so we don't usually allow discussion of scenarios or worldbuilding unless there's finished chapters involved (see the sidebar).  It *is* pretty fun to cut loose with a likeminded community though, so this is our regular chance to:

* Plan out a new story
* Discuss how to escape a supervillian lair... or build a perfect prison
* Poke holes in a popular setting (without writing fanfic)
* Test your idea of how to rational-ify *Alice in Wonderland*
* Generally work through the problems of a fictional world.

On the other hand, this is *also* the place to talk about writing, whether you're working on plotting, characters, or just kicking around an idea that feels like it might be a story. Hopefully these two purposes (writing and worldbuilding) will overlap each other to some extent.

^(Non-fiction should probably go in the Friday Off-topic thread, or Monday Recommendation thead)

### Comments:

- u/RedSheepCole:
  ```
  Consider [https://medium.com/@Jernfrost/why-colonize-venus-instead-of-mars-c490d14c0531](https://medium.com/@Jernfrost/why-colonize-venus-instead-of-mars-c490d14c0531)  
  That's just the start of a rabbit hole; it leads to link upon link, full of lots of speculation about Venusian flying habitats.  Basically the idea is that, since ordinary air is significantly less dense than Venus's CO2 atmosphere, human colonists could live in huge bubbles somewhere around 50km up.  The atmosphere contains, in addition to CO2, some nitrogen, with traces of water vapor, sulfur dioxide, and sulfuric acid--enough building blocks that you could skim and break them down to make all sorts of handy sludges.

  Rarer materials would need to be either imported from Earth or somehow procured from the surface.  This is the biggest difficulty I see at present; the surface of Venus is pretty much hell, and destroyed the one probe the Soviets sent in something like an hour.  Supposedly you could have better luck mining the highest mountains, though that would be a substantial investment.

  Energy would be plentiful; Venus receives oodles of solar energy, and one commenter on a thread suggested dipping a power plant on a mile-long tether, to get into the regions where ambient temps are above boiling.  I don't know enough chemistry to say how the sulfuric-acid clouds would be dealt with, but I've read enough knowledgeable-seeming people waving it aside that I don't feel too troubled.  Apparently it's feasible to make organic acid-resistant materials?  Not a chemist.

  These bubbles would be blown around the world by ferocious winds, effectively giving them fifty hours each of darkness and daylight.  It's been suggested (in one of these pages) that the habs would rise during the day and sink during the night, presumably by using ballast tanks and hydrogen gas, to compensate for the shift in insolation.  Venus itself is quicker/easier to get to than Mars.

  Thoughts?
  ```

  - u/MagicWeasel:
    ```
    I read a pdf of a paper from like 1990 about how to terraform venus, which included a 100 year period where all the CO2 would condense in the form of a continual CO2 rainstorm. It seemed scientifically based and was talking about how the colony could be profitable early on. 

    I googled "old paper about terraforming venus" because google is a wizard I'm pretty sure that this is the paper I read, if you're interested: https://www.orionsarm.com/fm_store/TerraformingVenusQuickly.pdf
    ```

    - u/TangoKilo421:
      ```
      Ah, good ol' Orion's Arm! No surprise there 😄
      ```

  - u/Frommerman:
    ```
    Glass and most ceramics are resistant to organic acids. That's why you can safely store most of them in glass vials. Glass would melt on Venus, but we've got tons of ceramics which would probably do the trick.

    I don't know of any flexible acid-resistant materials however. Neoprene is resistant to some acids, but it has a low flash and melting point and bursts into flames upon contact with nitric acid, which may exist in small quantities as well. Though to be fair I don't know if it would do that in a low oxygen environment.

    There are apparently a whole category of thermoplastics, one of which might do fine in an acid environment.
    ```

- u/DataPacRat:
  ```
  Is there a program that can take a rough map as input, and output a plausibly more-detailed version?

  (The particular map I'm looking at is [this](https://commons.wikimedia.org/wiki/File:First_global_geologic_map_of_Titan_\(PIA23174\).jpg) geological one of a moon, particularly the lake southeast of Xanadu.)
  ```

  - u/MagicWeasel:
    ```
    I think I saw a blog post about one of those image AIs that does it with pixelated images, but I'm not sure if it's easily available yet.  

    Here's the blog post in question: https://aiweirdness.com/post/622002033086578688/depixellation-or-hallucination
    ```

  - u/callmesalticidae:
    ```
    If you can't find a program then, depending on your needs, you might be able to cheaply commission the map. 

    I was able to get [this map of Jurassic-era Earth](https://www.alternatehistory.com/forum/threads/a-blank-map-thread.25312/page-294#post-20188626) for very little.
    ```

  - u/jtolmar:
    ```
    What kind of map are you trying to get out of it? If you just want a mostly-reasonable looking heightmap / coastline, most terrain generation programs are just adding up a bunch of octaves of Perlin noise, which you can actually do in Gimp.

    Take the image, cut out the part you want, transform it to mostly get rid of the bending, scale up a bunch, recolor it to a greyscale heightmap (use select by color and paint bucket whole selection), blur it, render simplex noise to a new layer (you may want to do this multiple times and merge them for more detail), set layer to add and lower the opacity, merge (probably do this on copies), posterize back down, maybe recolor back.

    [Here's what that looks like](https://i.imgur.com/xqsbNMy.png). You'll get different results, and tweaking it yourself will let you get more of what you want.

    If I were to spend more time on it, I'd do something about the grid lines (probably painting over them by hand earlier in the process), and try to make more of the land detail limited to the coastlines (starting with using a bigger blur in that step).
    ```

- u/VapeKarlMarx:
  ```
  I've been thinking about what kinda economic controlls you would need to keep even a medium magic DnD world from becoming post scarsity without putting a bunch of extra rules on the magic.  

  Everyone I have consulted so far has given me wildly diffrent answers
  ```

  - u/scruiser:
    ```
    Are you trying to stay as close as possible to rules as written?  (As opposed to treating them as an abstraction and adding in various common sense limits). Can anyone level up like a Player Character?  (In an abstract sense, Player Characters are kind of meant to represent unique are or at least rarely skilled individuals.  If you take the rules more literally, you could still interpret it to be that player character levels are rare and hard to get and that XP can’t be safely gained by artificially setting up safe encounters).  If you make character levels rare enough, whether by fiat or a complex in universe explanation about what levels are or by treating them as an abstraction (of fast-learning, lucky, blessed, and/or talented individuals) then you can reduce the economic impact of magic that way.

    One thing that commonly gets ignored or made less annoying by house rules are spell components.  If you went the opposite direction and made spell components rarer or more expensive or needed in greater quantity that could magic less economically impactful.  Likewise for magic item crafting the XP cost rules could be representative of the crafter literally pouring their soul into their work in a process that is costly enough to make magic items economically unviable and not mass produce able.
    ```

  - u/DXStarr:
    ```
    If you want to prevent progress, just have something out there that looks out for progress, and goes after the people who try it. Punishes them -- or eats them.

    Two good options are Industrial Magic is Lethally Patented, or, less comic and more grimdark, Industrial Magic Makes You Tasty To Aliens.

    Industrial Magic is Lethally Patented: there's something very powerful that thinks it "owns" industrial-economy magic, and that thing comes out and punishes societies that use too much magic in ordinary life.

    In *Practical Guide To Evil*, it's the gnomes, who go after anyone who poaches on their monopoly of machinery and automation. In *Worth the Candle*, there's a bit of this with the dragons, who consider the upper atmosphere their property and go after any unlicensed airplanes or flying mages.

    So, pick a powerful distant civilization, and say it's not always distant -- it comes and *visits* if there's too much "commoner magic" and kidnaps or kills the innovators.

    No industrial revolution for you! The gnomes have their monopoly.

    Industrial Magic is Tasty to Aliens: there's something Out There that's drawn to over-rich concentrations of magic in everyday life, and it colonizes or eats those cities, and nobody ever hears of them again.

    No industrial revolution for you! Your customers don't want to attract Cthulhu.

    You can see that both of these aren't about how magic works, but about the *social consequences* for using that magic. So any little thing people do can work just as the rulebooks imply. But the moment it starts to become a system - well, that's when it starts to get the attention of the Patent Enforcers or the Hungry Aliens.

    Is this realistic? I'm afraid we know it is, because it really happened. Imperial colonizers in history did both of these things.

    Lethal Patent Enforcers: the Dutch conquered Indonesia, and then, to get a monopoly on spices, they sent out raiding parties to slaughter everybody raising those spices who wasn't in Dutch territory. Your civilization isn't allowed: the powerful foreigners will kill you if you keep cultivating cloves and peppers.

    Your Civilization Makes You Tasty to Aliens: from all Africa, there's a certain stretch of the west coast where the Europeans took the most slaves from. You know why? Because back then, it was the rich part of sub-Saharan Africa, with the most built-up farms and kingdoms and civilization. And all those people and organized leaders made it the easiest, the most convenient, of all places for the Europeans to go into and demand captives -- to take overseas as slaves.

    The richer your sub-Saharan African kingdom was in 1500, the more likely the Europeans turned you and your whole village into a cargo for overseas slavery by the 1600s or 1700s. Because your economic development makes your people look tasty to the aliens.

    I know, super creepy, but the worst parts of history are.

    But you don't have to be grimdark to get the job done. In *Practical Guide to Evil* the gnomes are a spooky-comic fact rather than a seriously hostile menace. The story makes it possible the gnomes even have "good motives," that they're slowly working on things themselves and don't trust humans not to screw things up -- anti-industrialization as a sort of environmentalism.

    It could even be outright silly: you could have gods that were comically nervous about industrial magic, seeing it as a risk to their authority. Maybe everybody has superstitions about the Forbidden Applications of spells that will draw divine wrath, but also the Loophole Tricks that will let you run your teleportation-smuggling business without getting lightning-bolted by the God of Transport. Why revere the gods' prohibitions when you can, ah, creatively negotiate?

    So the basic principle will work in your world, whether you set it up as a wacky fact or a terrifying one:

    The easiest way to stop progress? Something big and powerful comes after anyone who tries.
    ```

  - u/None:
    ```
    So DnD's economy is wonky because whoever designed it didn't understand the value of gold.  In the rules, fancy magical items cost quite a bit to make.   In 5e a +1 sword is something like 500gp. (Let's use nobles.)  That's 3027 shillings.  (1500 pigs.  320 cows.)  Create food and water feeds 15 people.  By contrast that many medieval cows (yes I looked for medieval milk production) could make about 900 pounds of cheese a day.  This leads to feeding 224 people a day (not counting days when cows weren't milking, but also not counting meat).

    So to answer your question, magic would probably make the economy *less* efficient as arming knights would drastically increase in cost, but their monopoly on force would likely be more complete.  This in turn might actually *decrease* the speed of technological progress, because the price of labor is much lower compared to the price of the raw materials that create the magic.  In some ways technological progress relies on high labor prices.

    There's one exception to the relative cost inefficiency of magical items: bags of holding and teleport.  They would also be 6.6 shillings per pound (weight).  Ships were far cheaper at something like 30 shillings per *ton*.  However, there's speed to consider.  A mage with access to teleportation and a bag of holding could make 900 shillings per day selling spices.  Assuming you need a rare and very rare item to level up + the bag, that's 36,000 shillings or *40 days* to make a profit.  Even then, it's not the massive profit you might think; a 20 ton ship going to India might spend 300 days round trip.  You're still getting 266 shillings per day by this method at the cost of something like 600 shillings for the ship alone.  So mages are like 40x the investment for 3.4x the profit.  A profit that will permanently disappear in a few years once there are permanent teleportation circles between all major trade capitols.

    &#x200B;

    [http://medieval.ucdavis.edu/120D/Money.html](http://medieval.ucdavis.edu/120D/Money.html)

    [http://www.personal.utulsa.edu/\~marc-carlson/history/cattle.html](http://www.personal.utulsa.edu/~marc-carlson/history/cattle.html)

    [https://www.reddit.com/r/AskHistorians/comments/380veq/what\_was\_the\_cost\_of\_a\_ship\_in\_europe\_circa\_ad/](https://www.reddit.com/r/AskHistorians/comments/380veq/what_was_the_cost_of_a_ship_in_europe_circa_ad/)
    ```

---

