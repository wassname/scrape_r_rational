## [D] Friday Off-Topic Thread

* Author: u/AutoModerator *
* URL: https://www.reddit.com/r/rational/comments/51xulz/d_friday_offtopic_thread/
* Score: 23

* Created: 2016-09-09T15:04:42

### Post:

Welcome to the Friday Off-Topic Thread! Is there something that you want to talk about with /r/rational, but which isn't rational fiction, or doesn't otherwise belong as a top-level post? This is the place to post it. The idea is that while reddit is a large place, with lots of special little niches, sometimes you just want to talk with a certain group of people about certain sorts of things that aren't related to why you're all here. It's totally understandable that you might want to talk about Japanese game shows with /r/rational instead of going over to /r/japanesegameshows, but it's hopefully also understandable that this isn't really the place for that sort of thing.

So do you want to talk about how your life has been going? Non-rational and/or non-fictional stuff you've been reading? The recent album from your favourite German pop singer? The politics of Southern India? The sexual preferences of the chairman of the Ukrainian soccer league? Different ways to plot meteorological data? The cost of living in Portugal? Corner cases for siteswap notation? All these things and more could possibly be found in the comments below!


### Comments:

> **u/ketura** [+11]  *Organizer* (2 hours later)
> 
> So a while back I mentioned [I might try taking a stab at a rational pokemon game](https://www.reddit.com/r/rational/comments/4snm5i/d_wednesday_worldbuilding_thread/d5ayvuo), and I've been sort of hacking away at the problem ever since. Not on the game itself, but on the tools that would be required for such a thing. Such a data-heavy game would need to be able to *very easily* create dozens or hundreds of pokemon. Anyone interested can take a look at [my progress so far here](https://dl.dropboxusercontent.com/u/6516469/Bills%20PC/Bills_PC_Release_2016-09-09.zip) ([basic documentation here](https://docs.google.com/document/d/1Co3cS6p_5h6HGs3tzjbJRRbUFd-vI2njVGjYyz8jwE4/edit?usp=drive_web)).
> 
> I'm currently working on a good way to show the difference between pokemon stats, so of course I put in a chart, which led me to think about stat growth curves and such. Canon uses a very simple 2x linear growth, so you can expect to have BaseAttack attack by level 50 and 2 * BaseAttack attack by 100, ignoring EVs and IVs.  
> 
> This is boring, so I thought of some different ways that stats might grow, [which I plotted here](http://fooplot.com/#W3sidHlwZSI6MCwiZXEiOiJtaW4oKDUwKjAuOCkvNTUqeCwoNTAqMC44KSouOCkrKCgzMDArKDUwKjAuOCkpLygxK2VeKC0wLjA1NSooeC01MCkpKSkiLCJjb2xvciI6IiMwMDAwMDAifSx7InR5cGUiOjAsImVxIjoibWluKDUwLzkuMCp4LDUwKSsoMip4KSsyMCIsImNvbG9yIjoiIzg3OUUwNiJ9LHsidHlwZSI6MCwiZXEiOiJtaW4oNTAvNDAuMCp4LDUwKSsoeC81LjApXjIiLCJjb2xvciI6IiNGRjAwMDAifSx7InR5cGUiOjAsImVxIjoic2luKHgvMy44KzQpKm1pbih4KjEuNSw1MCkrKCgoMzIwKyg1MCowLjgpKS8oMStlXigtMC4wNTUqKHgtNDUpKSkpKSIsImNvbG9yIjoiIzAwNkRGQyJ9LHsidHlwZSI6MTAwMCwid2luZG93IjpbIi01IiwiMTAxIiwiLTIwIiwiNTUwIl0sInNpemUiOlsxMDAwLDYwMF19XQ--). Black is the standard curve, a logistical function that eases in and out in what I feel to be a very natural way. Green is bug, peaking early and then leveling to linear growth that is shortly outclassed. Red is Dragon, or any other long-lived dominant apex creature. And blue is, well, erratic and might not make sense at all to use, but was fun to plot.
> 
> Currently I'm stuck trying to figure out how to handle different base stats using this model. All the curves are different, so throwing "base stat" in as a variable to the curve itself results in wonky results, such as bug dominating at strange times, or Dragon sucking and then completely destroying. 
> 
> Simply adding the base stat could work, if "base stat" was redefined to mean "power level as a juvenile", but it would mean hardly any difference between the curves at high stat ranges...right now, an assumed base stat 0 under this model results in a difference of about 100 at level 60 between Bug and Erratic, which makes the differen e between curves negligible if the bottom of the curve *starts* at 400.
> 
> Anyhow. Let me know if you have thoughts or critique.
> 
> EDIT: oh, *duh*. I'll just treat this like I've named it, as a *growth* curve and not directly translating level to stat. The point on this curve will be *how much stat was gained* that level, which will eliminate wonky stat loss and other wierdnesses.

>> **u/Anakiri** [+10]  (10 hours later)
>> 
>> The games already do what you are trying to do. You're just not looking in the right place.
>> 
>> Canon uses linear stat growth with level, but *level* growth is not linear with experience. Additionally, when the game actually uses those stats, it multiplies the attack stat by level *again*. Holding everything else equal, damage goes by level squared. The level growth rate is therefore very important.
>> 
>> Check out [the graphs for that](http://bulbapedia.bulbagarden.net/wiki/Experience). Most Bug Pokémon are Erratic and most Dragons are Slow. When they both have 600,000 experience, the Bug will peak at level 100 while the Dragon is back at level 78. Now, an average Bug has a base attack of 90 and an average Dragon has a base attack of 118, so when they're at the same level, the Dragon is stronger. But since Bugs level faster and level counts double, it can overpower Dragons of equal experience until it peaks while the Dragon still has room to grow.
>> 
>> (Also, while some RPGs give you less EXP the higher your level, Pokémon does not. Two Pokémon going through the same battles will gain identical EXP, even if their levels are different. Except in Generation V. But that change didn't stick.)
>> 
>> In practice, a Slow average Dragon will level faster than an Erratic average Bug up to level 37 because the official curves are terrible, then the Bug will get to level 38 with 549 fewer total EXP. Even after that, the Bug's stats will never be higher than the Dragon's with the same amount of experience, even with its higher level. But, since level gets counted twice, the Bug will start doing more damage than the Dragon around 250,000 EXP, when the Bug is level 67 and the Dragon is level 58, in the late game. The Dragon will finally overtake it at level 88 with 851,840 EXP, while the Bug has been stuck at level 100 since 600,000 EXP.
>> 
>> Since canon has these really weird crossover points that most people won't ever see in casual play, it certainly makes sense to tweak the curves. But I think you're not giving the original design enough credit. I discovered all of this the last time I tried to mess with the formulas to make something more sensible and diverse, only to find out it was already done.

>>> **u/ketura** [+3]  *Organizer* (11 hours later)
>>> 
>>> Hmm! I knew about the level xp rates, but I struggled to find an analysis that explained the *ramifications* of the system like you just did here. Bulbapedia is utterly fantastic for collating data and explaining mechanics, but it leaves something to be desired when putting it all together.
>>> 
>>> Your explanation definitely makes me rethink the importance of levels in a system like this. I had considered stretching the levels out to scale up to 500, or be limitless, or take them out entirely and scale based on EXP amount, but you're right, I wasn't giving the old system enough credit. I was still planning on also including EXP curves, I just thought I would also throw it in for stat growth as well, which I think will be more immediately intuitive, since as you mention the current system is more obtuse.  FWIW levelling will be slower in this game, whether it be through less frequent successful battles or higher EXP requirements or whatnot, so early/mid/late game will be more of a thing, with timing peaks being more important. There's a lot of influence from how Dota works in that regard. Also if team death is a thing, well...then it will be even more pronounced.

>>>> **u/DaystarEld** [+1]  *Pokémon Professor* (17 hours later)
>>>> 
>>>> Agree with /u/Anakiri mostly, though alternatively my preference would be to simplify them based off Base Stat Totals, assuming you're using those as a guide of any kind for the strength of pokemon in your game:
>>>> 
>>>> Fast: 200-450 Final Evolution BST
>>>> 
>>>> Medium: 451-525
>>>> 
>>>> Slow: 526-599
>>>> 
>>>> Legendary: 600+
>>>> 
>>>> The last's name might be a misnomer since it includes the pseudo-legendaries like Dragonite, and excludes some legendaries like the storm birds, but I think tweaking the stats of legendaries makes sense anyway, and even certain non-legendary like onix. Alternatively just make the last one 580+, since there's no pokemon that are between 580-600 that aren't legendaries (besides mega evolutions).
>>>> 
>>>> This way the pokemon aren't arbitrarily jumping around on the power level, or becoming more rapidly powerful for no discernable reason.  Evolutions already serve as a good shifting point by which to measure jumps in power, and having some pokemon gain more stats faster between certain level ranges, but not others, is just adding more complication without any real value.
>>>> 
>>>> Random additional points:
>>>> 
>>>> * Evolutions should probably take longer, especially if you're extending the level cap or doing away with it altogether. 
>>>> 
>>>> * Stones should be a held item on a pokemon for awhile before they evolve. I'd also add a level requirement to pokemon that normally only evolve by stones or trading, if level is meant to be at least somewhat correlated with age. (Alternatively, just include age as a factor too, and have pokemon age faster through battle.)
>>>> 
>>>> * Related, experience should be slowly gained passively while pokemon are outside their pokeballs, if there's the ability to travel in the overworld and have a pokemon out with you.
>>>> 
>>>> * Pokemon should gain EV stats through training at a fairly significant rate, maybe only through training, in order to differentiate getting physically stronger through combat (which comes from EXP) and becoming a better fighter through discipline.
>>>> 
>>>> * Are pokemon in your world sapient? Not sure how much you're basing it off my story, but in either case, I headcanon Intelligence as an extra stat that affects things like training speed, amount of moves a pokemon can learn, and unruliness.  If it's not too much effort, might be an interesting stat to add.
>>>> 
>>>> * Environment should matter for which pokemon are able to be used. No fish pokemon on land. Only aquatic pokemon while underwater, if diving is in the game. Maybe some exceptions. 
>>>> 
>>>> * Size of pokemon. You can't summon a wailord for an indoor battle. You can summon a wailord in a big enough space and just have it be stationary during the battle, but all moves against it should automatically have 100% accuracy.

>>>>> **u/ketura** [+2]  *Organizer* (a day later)
>>>>> 
>>>>> I'm definitely planning on adding BST as one of the graphs that one can look at while making a pokemon, but I like the idea of straight-up defining the BST, possibly even instead of the EXP curve.
>>>>> 
>>>>> >Evolutions should probably take longer, especially if you're extending the level cap or doing away with it altogether.
>>>>> 
>>>>> Agreed.  I actually have this idea in my head of treating evolutions the way that Fire Emblem treats class upgrades, so when a pokemon evolves it returns to level 1, but retains all the stats it had before it evolved as the new baseline.  In Fire Emblem you could start upgrading at level 10, but you could instead wait until the cap at 20, and your characters that waited would of course have 10 level's worth of stats over the more impatient characters.
>>>>> 
>>>>> This would result in a *de facto* delay of most evolutions rather than an enforced one, but I kind of like using incentives rather than invisible walls.  It may not be feasible, but either way evolutions will need to be more important of a milestone.
>>>>> 
>>>>> >Stones should be a held item on a pokemon for awhile before they evolve. 
>>>>> 
>>>>> My idea was actually dosages, so it requires X stones to get a Raichu but only Y for Jolteon, or something.  If they're difficult to get, it could even be made more common of a method than canon, requiring the player to decide between evolving the one powerhouse that requires 20, or evolving several less powerful pokemon instead.
>>>>> 
>>>>> >I'd also add a level requirement to pokemon that normally only evolve by stones or trading, if level is meant to be at least somewhat correlated with age. 
>>>>> 
>>>>> Yes, trading evolutions will be done away with, and minimum level requirements only makes sense, regardless of the evolution method used.  The tool currently just has the canon evolution types because I needed to put something in the box, but that will get revamped when the design's been hammered out some more.
>>>>> 
>>>>> >(Alternatively, just include age as a factor too, and have pokemon age faster through battle.)
>>>>> 
>>>>> /u/UltraRedSpectrum mentioned having Metapod/Kakuna evolve through time and not leveling, and age is honestly probably the way to abstract that.  I love the idea--having bug pokemon hit the "age" cap faster was my initial brainstorm concept, but the only problem I have with it is I abhor grinding, and this seems like the sort of thing that leads to that.  Do I leave my game running so everyone ages?  Is it based on steps instead?  
>>>>> 
>>>>> I think you're right in that leveling needs to somehow correlate with age, but I'm not sure what the answer is yet.
>>>>> 
>>>>> >Related, experience should be slowly gained passively while pokemon are outside their pokeballs, if there's the ability to travel in the overworld and have a pokemon out with you.
>>>>> 
>>>>> Excellent idea. 
>>>>> 
>>>>> >Pokemon should gain EV stats through training at a fairly significant rate, maybe only through training, in order to differentiate getting physically stronger through combat (which comes from EXP) and becoming a better fighter through discipline.
>>>>> 
>>>>> This is the basic idea.  In my head EVs are even the source of the majority of a pokemon's strength, dwarfing base stats and rivalling EXP gain.  This is one of those things that I'll just have to fiddle with it as I go, as there's only so much a spreadsheet can help in designing this until I have a working prototype in my hands.
>>>>> 
>>>>> >Are pokemon in your world sapient? Not sure how much you're basing it off my story, but in either case, I headcanon Intelligence as an extra stat that affects things like training speed, amount of moves a pokemon can learn, and unruliness. If it's not too much effort, might be an interesting stat to add.
>>>>> 
>>>>> Aha!  I was trying to identify how I would differentiate the max number of moves between pokemon, and this is probably the way to go.  I have an Experience stat already that is more of an IV than a base stat, but adding Intelligence (or perhaps Skill or something) as a stat isn't hard at all.
>>>>> 
>>>>> Your fic is pretty much the template I'm going after for the world, with a generous helping of Game of Champions.  Who knows how much of it will be ever implemented or brought up, but it's the underlying current.
>>>>> 
>>>>> >Environment should matter for which pokemon are able to be used. No fish pokemon on land. Only aquatic pokemon while underwater, if diving is in the game. Maybe some exceptions.
>>>>> 
>>>>> http://i.imgur.com/ljXQ4Cc.jpg
>>>>> 
>>>>> Actually, pretty much *every* realism issue brought up in this album will be addressed in some way : http://imgur.com/a/KvwYY
>>>>> 
>>>>> >Size of pokemon. You can't summon a wailord for an indoor battle. You can summon a wailord in a big enough space and just have it be stationary during the battle, but all moves against it should automatically have 100% accuracy.
>>>>> 
>>>>> Hell, I'm not even sure I'll ever implement Wailord just for the sheer amount of problems something that large brings to the table.  But size will be something that is tracked and enforced; your pokemon will take up X number of hexes depending on its size, and if there's not enough hexes in an area to support your pokemon, your pokeball errors out and refuses to open.  
>>>>> 
>>>>> Thanks for the feedback and idea dump!

>>>>>> **u/UltraRedSpectrum** [+1]  (a day later)
>>>>>> 
>>>>>> >/u/UltraRedSpectrum mentioned having Metapod/Kakuna evolve through time and not leveling, and age is honestly probably the way to abstract that. I love the idea--having bug pokemon hit the "age" cap faster was my initial brainstorm concept, but the only problem I have with it is I abhor grinding, and this seems like the sort of thing that leads to that. Do I leave my game running so everyone ages? Is it based on steps instead?
>>>>>> >I think you're right in that leveling needs to somehow correlate with age, but I'm not sure what the answer is yet.
>>>>>> 
>>>>>> Avoiding grinding is definitely a tricky issue, and while there are a few ways around it, none of them are foolproof. Two ideas come to mind:
>>>>>> 
>>>>>> 1) Take careful measure of how many units of time (either minutes or steps, I'd go with steps) it takes until you want the player to have a Butterfree, and at what time they're likely to catch a Caterpie, and plan the evolution accordingly. For example, since we're only doing the first gym, we might test how long it takes a normal player to get to Pewter, and try to make it so that, if a player catches the first Caterpie they run into, it'll evolve into a Butterfree by the time they're facing the gym. In an alternate universe in which we were doing two gyms, we might have it evolve into Metapod by Pewter and Butterfree some time before Cerulean, since Butterfree are pretty bad against Rock-types anyway. Obviously you'd want to create a bunch of different options and test, test, test to see which one felt best.
>>>>>> 
>>>>>> 2) Treat time as a resource in your game design. This requires a huge departure from the original Pokemon games and is therefore very impractical, but I feel it's in line with the pie-in-the-sky "Witchermon" you said you weren't going to do, so I figured I might as well bring it up as a theoretical exercise. In this case, you make the game very difficult and put the player under a great deal of pressure. Any Ice Pick Lodge game is a good example of this. The idea is that the player will feel as though, by having the Caterpie in their party, they aren't grinding steps so much as multitasking as part of a grand strategy. You'd also combine it with some of what I described in 1). There's obviously a lot more to it than that, but this post is getting a bit long as-is.
>>>>>> 
>>>>>> The issue with both is that the whole thing gets more effective the more immersive the game is, and immersion really isn't in the cards at the moment. I'd say that if you implement aging, you should implement age-based evolution, but otherwise just stick with levels. As always, I'm in favor of launching 1.0 ASAP so you can test everything, and saving any extra bells and whistles for 1.1+.

>>>>>> **u/DaystarEld** [+1]  *Pokémon Professor* (2 days later)
>>>>>> 
>>>>>> >This would result in a de facto delay of most evolutions rather than an enforced one, but I kind of like using incentives rather than invisible walls. It may not be feasible, but either way evolutions will need to be more important of a milestone.
>>>>>> 
>>>>>> Rationally I feel like delaying evolution should only be possible with exposure to an Everstone, which is probably going to be a pretty rare item, or at least not a widely available one. In my world I see it as a luxury item for people who own pokemon as pets, to ensure that the cute and cuddly mon they have doesn't turn into a destructive giant ten years down the line.  I think most trainers would be fine with just letting their pokemon evolve when they naturally can, so there's no real reason to incentive lack of evolution imo.
>>>>>> 
>>>>>> >My idea was actually dosages, so it requires X stones to get a Raichu but only Y for Jolteon, or something. If they're difficult to get, it could even be made more common of a method than canon, requiring the player to decide between evolving the one powerhouse that requires 20, or evolving several less powerful pokemon instead.
>>>>>> 
>>>>>> Kind of like Candy in Pokemon GO? It's an interesting alternative, though it mostly works in GO because you can have hundreds of pokemon "with you" at any given time and putting pokemon in Gyms limits your fighting ability, so having six strong Vaporeon is better than having one super strong vaporeon in many cases.
>>>>>> 
>>>>>> Even without a pokemon limit of 6 in your game, having so many repeats wouldn't be all that advantageous. Though if pokemon die realistically often, that might be a good justification not to put all your stones into one pokemon.
>>>>>> 
>>>>>> >/u/UltraRedSpectrum mentioned having Metapod/Kakuna evolve through time and not leveling, and age is honestly probably the way to abstract that... Do I leave my game running so everyone ages? Is it based on steps instead?
>>>>>> 
>>>>>> Easiest way I can think to do this is to make there be real life money constraints. If time passes in day-night and weekly cycles, just have your trainer incur living expenses. Even staying at a Trainer House and eating basic food costs a few bucks a day.  Keeping your game running would drain your finances, or worse if you implement a "Fed" and "Rested" meter that your trainer needs to keep up to stay alive (which I think would add a lot to the immersion, but I get if that's too much for the game's first conception).
>>>>>> 
>>>>>> >Hell, I'm not even sure I'll ever implement Wailord just for the sheer amount of problems something that large brings to the table. But size will be something that is tracked and enforced; your pokemon will take up X number of hexes depending on its size, and if there's not enough hexes in an area to support your pokemon, your pokeball errors out and refuses to open.
>>>>>> 
>>>>>> Makes sense. Also, you should probably start with just the original 151 anyway, or if you're doing it by region then do what I did and go by just the pokemon available in the latest version of whatever region the game is originally set in.
>>>>>> 
>>>>>> >Thanks for the feedback and idea dump!
>>>>>> 
>>>>>> No problem! I continue to think about these things for a pokemon tabletop RPG anyway :)

>>>>>>> **u/UltraRedSpectrum** [+2]  (2 days later)
>>>>>>> 
>>>>>>> >No problem! I continue to think about these things for a pokemon tabletop RPG anyway :)
>>>>>>> 
>>>>>>> I feel obliged to link the r/rational tabletop gaming Discord server: https://discord.gg/3H5cNcq.

>>>>>>>> **u/DaystarEld** [+1]  *Pokémon Professor* (2 days later)
>>>>>>>> 
>>>>>>>> Neat, just made an account, thanks :)

>>>>>>> **u/ketura** [+1]  *Organizer* (2 days later)
>>>>>>> 
>>>>>>> >Rationally I feel like delaying evolution should only be possible with exposure to an Everstone, which is probably going to be a pretty rare item, or at least not a widely available one.
>>>>>>> 
>>>>>>> That's a good point, actually, for the level evolutions.  My original idea was that you had to attack or order one of your pokemon to attack your evolving pokemon as they were going through metamorphosis, which would interrupt it but severely put a damper on your relationship.  Pros and cons, and maybe you *don't* want to risk pissing off your high-level Dragonair too much...but the Everstone idea is simpler, and supported by canon to boot.
>>>>>>> 
>>>>>>> >Even without a pokemon limit of 6 in your game, having so many repeats wouldn't be all that advantageous. Though if pokemon die realistically often, that might be a good justification not to put all your stones into one pokemon.
>>>>>>> 
>>>>>>> The more I put into the design, the more it makes me think of the days when I played Nethack nonstop, and it's definitely taken on more roguelike elements.  I was ambivalent before, but I'm now leaning towards allowing permadeath in rare-ish circumstances.  This is probably triggered from me watching a dude do a 1 hour 54-minute speedrun of Yellow using essentially only a Nidoking and HM slaves.  It was interesting, for sure, but I couldn't stop thinking about how screwed this trainer would be if he lost his one powerhouse, in a more realistic setting. 
>>>>>>> 
>>>>>>> >Easiest way I can think to do this is to make there be real life money constraints. If time passes in day-night and weekly cycles, just have your trainer incur living expenses. Even staying at a Trainer House and eating basic food costs a few bucks a day. Keeping your game running would drain your finances, or worse if you implement a "Fed" and "Rested" meter that your trainer needs to keep up to stay alive (which I think would add a lot to the immersion, but I get if that's too much for the game's first conception).
>>>>>>> 
>>>>>>> My ideal game would in fact have the fed/rested meters for both you and pokemon team alike, but you're right, it's definitely pie-in-the-sky.  The financial drain is a good start, and combined with permadeath would prevent one from just camping on route 1 with your strongest pokemon out, too.  Man, I need to think more about how the cities themselves will be built; that's a whole nother can of worms.
>>>>>>> 
>>>>>>> >Makes sense. Also, you should probably start with just the original 151 anyway, or if you're doing it by region then do what I did and go by just the pokemon available in the latest version of whatever region the game is originally set in.
>>>>>>> 
>>>>>>> Yeah, /u/UlraRedSpectrum expressed interest in doing the art, so we'll probably start with the canon types that are between Pallet and Pewter, then their evolutions, then add "extra" pokemon that make sense to have in that area, and branch out from there.  Personally I will probably only ever look at the first two generations and then add any pokemon I think are well-designed beyond that.  I refuse to force myself to implement floating chandeliers and ice cream cones for the sake of completeness.

>>>>>>>> **u/DaystarEld** [+1]  *Pokémon Professor* (2 days later)
>>>>>>>> 
>>>>>>>> > I refuse to force myself to implement floating chandeliers and ice cream cones for the sake of completeness.
>>>>>>>> 
>>>>>>>> Ahh, but are those all that more irrational than sentient pokeballs or piles of sludge?

>>>>>>>>> **u/ketura** [+1]  *Organizer* (2 days later)
>>>>>>>>> 
>>>>>>>>> Perhaps not.  I sadly live in a world where my project motivation is fueled by Rule of Cool, however.

>>>>>>>>>> **u/DaystarEld** [+1]  *Pokémon Professor* (2 days later)
>>>>>>>>>> 
>>>>>>>>>> Yeah, I don't blame you. They're not nearly as fun to think about, and I don't know anyone whose favorite pokemon is voltorb or vanilluxe.

>> **u/UltraRedSpectrum** [+3]  (9 hours later)
>> 
>> This is really interesting. The way you broke down bodies into parts that can be separately damaged reminds me a lot of Dwarf Fortress, but I'm not sure the added depth is worth the complexity. Any plans for other changes, like making Caterpie and Weedle evolutions based on time instead of level?

>>> **u/ketura** [+5]  *Organizer* (11 hours later)
>>> 
>>> I was initially planning on just supporting DF raw files straight out, but I really don't think the game is enhanced by simulating muscle and fat layers...not this game, anyway. The attribute system is pretty much pulled straight from there, though.
>>> 
>>> The anatomy system has two reasons to exist: first, it cuts down on needing to list every move on every pokemon, or needing to list every pokemon on every move. I can simply give moves anatomical requirements, like "any pokemon with a Tail with an ATK stat can learn Iron Tail", or "any pokemon with at least two Grasp or four Grapple limbs can learn Pin". This reinforces the rationality aspect and reduces workload simultaneously.
>>> 
>>> Second, it allows some moves to be used to target specific body parts at a hit disadvantage. Do I aim at the body for damage and a higher hit chance? Or do I aim for the wings and try to ground him? Imagine a fight between a Blastoise with one cannon out of commission against an Umbreon with a broken leg. Situations like this create dilemmas and force hard choices, and it's honestly the real reason I introduced it; other reasons just fell into place as I went.
>>> 
>>>  It should also be mentioned that most of this will be hidden by default from the player...until a more advanced pokedex is acquired with a readout of the pokemon in question *and* an accurate move is learned by your team, you might not even encounter the system at all. Complexity, yes, but as a reward as the player digs deeper.
>>> 
>>> I hadn't thought of that particular Metapod/Kakuna change, but I'll throw it in the list! Makes sense to me. I have tons of small ideas like that, such as enforcing the shellder/slowpoke evolution requirement, adopting the pokeball capture method from Origin of Species, pokemon not listening to you based on their temperament and your training skill rather than just level, pokedexes being used in battle for triage and individual scanning, evolutionary stones requiring sustained doses to encourage a more powerful evolution, etc etc etc etc. The first link in my OP is to a discussion and a document with most of the big changes and some of the smaller ones I'd like. The aim truly is to make a rational game that happens to be set in the pokemon world, rather than a pokemon game that happens to be rational.

>>>> **u/UltraRedSpectrum** [+2]  (12 hours later)
>>>> 
>>>> Reading through that older discussion, I ran into this:
>>>> 
>>>> >(Not to mention my skill set: I'm a programmer and an alright animator, but standard art is right out, so my mind is already automatically filtering scopes that can't be covered by just those two skills.)
>>>> 
>>>> If you do ever wind up needing any art for your game, I'd be really interested in contributing. I'm either finished or nearly finished with the icons for hackerkiba's Factorio mod, and I don't think he needs the textures done, so I'll be in the market for a new pet project.
>>>> 
>>>> (For the record, I'm not as good as the artists for the original pokemon games.)

>>>>> **u/ketura** [+2]  *Organizer* (14 hours later)
>>>>> 
>>>>> Well for the record I'm not as good a programmer!  (I'd like to think I'm as good a designer, but we all have our vices, don't we.)
>>>>> 
>>>>> I'm totally down to collaborate.  I only have the faintest of ideas for what the art design needs to be: hex grid, probably top-down, probably 2-D.  But hey--if you want to start spitballing ideas or trying things out, let me know.  I'll PM you contact details for whenever you're free.

>> **u/traverseda** [+4]  *With dread but cautious optimism* (3 hours later)
>> 
>> Huh. What do you expect to gain from this? Nintendo historically sues the pants off of any fan games.
>> 
>> Why aren't you releasing the source code?
>> 
>> Doesn't run under wine.

>>> **u/ToaKraka** [+11]  *https://i.imgur.com/OQGHleQ.png* (3 hours later)
>>> 
>>> > Nintendo historically sues the pants off of any fan games.
>>> 
>>> \*any fan games *that get a lot of attention.*
>>> 
>>> See r/pokemonzetaomicron, r/pokemoninsurgence, and r/pokeepsilon for some of the *many* projects that *haven't* been taken down--to say nothing of [Pokémon Tabletop United](http://pokemontabletop.com).

>>> **u/ketura** [+8]  *Organizer* (3 hours later)
>>> 
>>> Experience in building complex mechanical game systems is what I hope to gain. Do it first using the base of someone else's system as a proof of concept while working out the technical bits without needing to worry about the design so much, then make my own. Commander Keen was prototyped by John Carmack building Super Mario for the PC, and this is the same basic idea. The actual game implementation will likely not encompass more than pallet to pewter + an arena (if I even get that far), and if released it would be to no fanfare in an obviously incomplete, if playable, state.
>>> 
>>> [Code is here](https://bitbucket.org/ketura/billspc), didn't think it'd be useful in code form before the game libraries themselves were integrated (not to mention the code is an ugly SOB). Until then it's a glorified limited JSON editor.
>>> 
>>> It's built using WPF and hasn't been tested in any OS besides Windows 10, so it doesn't surprise me that wine craps out on it. Sorry to hear it, though.

>>> **u/Fresh_C** [+3]  (3 hours later)
>>> 
>>> Do they actually sue them? All I've heard of is DMCA takedown notices and Cease and Desist letters, which are basically a prelude to legal action.
>>> 
>>> I don't think I've heard of a situation where Nintendo has ever actually sued or requested compensation from a fan game.
>>> 
>>> Also, the games are usually distributed enough by the time these notices are sent that a sufficiently determined person could still find them online.

>>>> **u/callmebrotherg** [+8]  *now posting as /u/callmesalticidae* (3 hours later)
>>>> 
>>>> > Also, the games are usually distributed enough by the time these notices are sent that a sufficiently determined person could still find them online.
>>>> 
>>>> Which, if I'm not mistaken, is the basic strategy of these fangames: you know that Nintendo is going to send DMCA notices, but because this is the internet it doesn't matter if the original source is gone. The game lives on.

>>>>> **u/Cariyaga** [+3]  *Kyubey did nothing wrong* (6 hours later)
>>>>> 
>>>>> Which is perfectly acceptable to them, because the only reason (beyond vanity) that they care is because they are legally required to DMCA folks if they want to keep their trademark, IIRC. It works out in a weird way.

> **u/Sagebrysh** [+11]  *Rank 7 Pragmatist* (4 hours later)
> 
> I'd like to share the fictional roleplay civilisation/government that I participate in inside the EVE Online space MMO.
> 
> I run a corporation called the Alexylva Paradox that have colonised a solar system they named Origin. We live in Origin ingame and over the years have created a large amount of lore surrounding the government, people, technology, and values that Origin has. I thought you guys might be interested in what we've created, since our characters are all rationalist transhumanists, and we're trying to make the most stable/functional/optimal government possible. We use science to determine the objectively best policies, or at least, attempt to. Our highest rank is called a 'Coordinator' and Meditations on Moloch is required reading for those applying for the position. 
> 
> Here are three wikipedia style articles that provide the core of the information about Origin to inform our roleplay:
> 
> [Origin](http://wiki.eve-inspiracy.com/index.php?title=Origin)
> 
> [Government of Origin](http://wiki.eve-inspiracy.com/index.php?title=Government_of_Origin)
> 
> [People of Origin](http://wiki.eve-inspiracy.com/index.php?title=People_of_Origin)
> 
> Its all totally hypothetical of course, and there's probably several ways that this government could just rapidly collapse due to corruption in the real world, but I'm curious what the thoughts are on what we've built.

>> **u/GaBeRockKing** [+3]  *Horizon Breach: http://archiveofourown.org/works/6785857* (10 hours later)
>> 
>> Man, EVE is so fascinating to me, but I hate the subscription model and enough of its game mechanics piss me off to prevent me from playing.
>> 
>> Hopefully Star Citizen matches up (and is released before the heat death of the universe.)

>>> **u/ToaKraka** [+7]  *https://i.imgur.com/OQGHleQ.png* (11 hours later)
>>> 
>>> > I hate the subscription model
>>> 
>>> [The ability to play for free (with some limits) will soon be instituted.](https://community.eveonline.com/news/dev-blogs/introducing-clone-states-and-the-future-of-access-to-eve-online)

>>>> **u/GaBeRockKing** [+1]  *Horizon Breach: http://archiveofourown.org/works/6785857* (11 hours later)
>>>> 
>>>> Huh, I might try it out, then.
>>>> 
>>>> Though to be honest, my biggest issue would still be there-- that the combat is gear based, rather than skill-based, and tab-targeting rather than an actual flight model.
>>>> 
>>>> I'm almost certainly going to end up trying EVE valkyrie eventually, though (that is, if I end up caving and buying an oculus rift or vive).

>>>>> **u/ketura** [+2]  *Organizer* (12 hours later)
>>>>> 
>>>>> Eh?  If you're in 1000-man fleets, or doing PvE, then yeah, it's going to come down to the richer fits and pressing f1, but I can assure you that in solo flight or small groups, how you fly is very important.  Combine speed tanking with range control and you have a complex dance of getting shots in while you're within your optimal range but outside the optimal range of your opponent. 
>>>>> 
>>>>> I remember one time that some dude in a Stabber came out to harass us while we lived out in Se7erance space, and he just completely picked us apart like we were made of paper.  Six of us died repeatedly to him as he lazily ripped us to shreds.  A Stabber is not an expensive ship, and if the six of us hadn't've been completely hopeless we would have wrecked him...if we could just touch him.  But he held us all at arm's length, popped those of us that posed a threat and toyed with the rest of us. In a fit that probably cost 20 mil.
>>>>> 
>>>>> That's not to say that what you fly is unimportant--but if you know what you're doing (and you pick the right fight), it comes down to skill and skill alone.

>>>>>> **u/GaBeRockKing** [+1]  *Horizon Breach: http://archiveofourown.org/works/6785857* (13 hours later)
>>>>>> 
>>>>>> >That's not to say that what you fly is unimportant--but if you know what you're doing (and you pick the right fight), it comes down to skill and skill alone.
>>>>>> 
>>>>>> Obviously, I've never played EVE, and am therefore not the best judge of how it works. But the skills EVE requires seem more strategic in nature-- less like, say, juggling, and more like playing a chess game. As someone who almost exclusively plays planetside 2, with a little bit of warthunder, although EVE definitely has the *scale* I crave (why I'm interested in it in the first place), it lacks dogfighting mechanics as I'm used to them. Even in Planeside 2, nominally a shooter, I spend more than a fifth of my time in a fighter, and non-negligible amounts of time in the bomber, repairing my aircraft, or running from enemy fire after I've bailed from the flaming wreck of my aircraft.
>>>>>> 
>>>>>> EVE is still a really cool game, but by the time PS2 dies I'm hoping SC will fulfill my dogfighting and scale cravings at the same time.

>>>>>>> **u/ketura** [+2]  *Organizer* (13 hours later)
>>>>>>> 
>>>>>>> Oh!  Another planetmans.  
>>>>>>> 
>>>>>>> You're right, it's more speed chess and less twitch shooting.  Different skills at play for different games, I suppose.  The older I get, the more I appreciate the strategic elements at play, rather than the rote execution needed to enact those strategies, but I suppose it's amiss for me to forget that there are skills besides tactics.  
>>>>>>> 
>>>>>>> (Speaking of scale, I love Planetside for that and that alone.  I wish MMOFPS was more of a thing.)

>>>>>>>> **u/GaBeRockKing** [+3]  *Horizon Breach: http://archiveofourown.org/works/6785857* (13 hours later)
>>>>>>>> 
>>>>>>>> >(Speaking of scale, I love Planetside for that and that alone. I wish MMOFPS was more of a thing.)
>>>>>>>> 
>>>>>>>> Oh yeah. I just can't play other FPS games anymore :(. For most people, 32v32 is large fight. For me, I can't stop thinking "I could be farming a skirmish this size with my rocketpods, *right now*."
>>>>>>>> 
>>>>>>>> EVE and PS2 are the sort of games that really skew your expectations of what a video game should be like :P

>>>>>>>>> **u/ketura** [+3]  *Organizer* (13 hours later)
>>>>>>>>> 
>>>>>>>>> Add Dwarf Fortress and you have a straight up Kotaku article.
>>>>>>>>> 
>>>>>>>>> LIST OF GAMES THAT WILL RUIN GAMES FOR YOU FOREVER:
>>>>>>>>> 
>>>>>>>>> 1- EVE
>>>>>>>>> 
>>>>>>>>> 2- Planetside 2
>>>>>>>>> 
>>>>>>>>> 3- Dwarf Fortress
>>>>>>>>> 
>>>>>>>>> It's funny how all of these open your mind so far that you seriously can't ever go back.  I tried to play MMOs after EVE and they were all trite in comparison.  NOTHING gets you the adrenaline high like a gank with 1 billion ISK on the line, or robbing your corpmates blind, or running a blockade with a hundred goons on your tail, or, or, or...

>>>>>>>>>> **u/-main** [+1]  (a day later)
>>>>>>>>>> 
>>>>>>>>>> Go ahead and add Supreme Commander to that list. Once you've gotten used to zooming out, minimaps in other RTSs start to seem like a horrible idea.

>>>>>>>>> **u/rhaps0dy4** [+1]  (2 days later)
>>>>>>>>> 
>>>>>>>>> Another planetman? And a fellow pilot at that! And another one! What a wonderful day!
>>>>>>>>> 
>>>>>>>>> [](#s "Live free in the NC!")

>>>>>>>>>> **u/GaBeRockKing** [+1]  *Horizon Breach: http://archiveofourown.org/works/6785857* (2 days later)
>>>>>>>>>> 
>>>>>>>>>> Heh, it's always nice to find another [person](#s "terrorist scumsucker") who plays PS2.

>> **u/ketura** [+1]  *Organizer* (6 hours later)
>> 
>> Sounds interesting! I'll have to remember this once I resub.

>> **u/rhaps0dy4** [+1]  (2 days later)
>> 
>> This looks pretty cool. In particular I enjoyed the star system description, even though I was constantly wondering how planets with such different ages came to be in the same system. But good stuff!

>>> **u/Sagebrysh** [+2]  *Rank 7 Pragmatist* (2 days later)
>>> 
>>> Part of that was that I was working with the existing ingame descriptions of the planets, which are randomly generated, and trying to come up with a coherent way that such an arrangement of worlds could actually exist in nature.

>>>> **u/rhaps0dy4** [+1]  (2 days later)
>>>> 
>>>> Oh, alright. I thought "it's optimised for fantasy-fun, not realism". I guess that explanation applies to the EVE generation algorithm, not to the writing, now.

>> **u/None** [+1]  (3 days later)
>> 
>> Reminds me of some of scott alexander's worldbuilding stuff. Here's a few random thoughts on how I'd break it:
>> 
>> I think hte biggest point of failure is the cellular democracy, as that seems very open to gerrymandering, etc. For example I put 55 blue neighbourhoods in one second order council, and the same within councils, or designate neighbourhood councils in such a way that people I agree with control the areas with the best stuff. Basically whoever sets the boundaries has enormous political power. 
>> 
>> I don't know the setting, but with sufficiently advanced tech you can handwave some of those problems by making it easy to move between constituencies,. You also have the problem of how disputes between rthem are resolved, or what to do when an individual of one jurisdiction commits a crime against one from another. For story purposes that could be a useful source of conflict,  have two normally mutually indifferent groups in conflict, and have a third party drawn in as a mediator. 
>> 
>> IF you want to gain supreme power in the scientific conclave, just make sure you are friends with the people who determine the "meritocratic" promotion criteria

> **u/ToaKraka** [+13]  *https://i.imgur.com/OQGHleQ.png* (5 hours later)
> 
> [Mr. Yudkowsky seems to have some *very* strong opinions on onions...](http://i.imgur.com/15IKxba.png)
> 
> ([Source](https://www.facebook.com/yudkowsky/posts/10154559641209228))

>> **u/blazinghand** [+32]  *Chaos Undivided* (6 hours later)
>> 
>> [Or so he thought...](http://i.imgur.com/xJchfIx.png)

>>> **u/Cariyaga** [+21]  *Kyubey did nothing wrong* (6 hours later)
>>> 
>>> The soup thickens...

>>> **u/Timewinders** [+5]  (11 hours later)
>>> 
>>> I also hate onions but am fine with them if they're blended and used in cooking. It's the texture honestly, they're slimy and gross and the taste isn't that great either by themselves. They're basically just a seasoning.

>>> **u/zarraha** [+1]  (2 days later)
>>> 
>>> Onions are a flavor, not a food.  This is their proper place.  If society took half of all recipes that contain cinnamon and replaced the powder with chunks of cinnamon sticks, it would taste bad and many people would go around claiming that they hate cinnamon because of how many bad experiences they had.

>> **u/gods_fear_me** [+9]  *The Culture* (11 hours later)
>> 
>> As a perfectly rational person, I strongly disagree with Mr. Yudkowsky on this matter. I love onions.

>>> **u/eniteris** [+7]  (12 hours later)
>>> 
>>> Aumann's agreement theorem says one of you must be wrong.

>>>> **u/BadGoyWithAGun** [+6]  (18 hours later)
>>>> 
>>>> However, it gives no indication as to which, since the orthogonality thesis clearly states that onion preference and intelligence level are unrelated.

>>>>> **u/Frommerman** [+3]  (a day later)
>>>>> 
>>>>> We should design an AI to tell us objectively whether onions are putrid or amazing. I anticipate zero possible problems with this. We should ensure that its primary objective is the above, and not worry about limimitations.

>>> **u/Fresh_C** [+2]  (13 hours later)
>>> 
>>> I wish I was a perfectly rational person...

>>> **u/VanPeer** [+2]  *The shard made me do it* (a day later)
>>> 
>>> As an imperfectly rational person, I too love onions.

> **u/gbear605** [+19]  *history’s greatest story* (9 hours later)
> 
> Not quite off-topic and certainly not big enough for its own thread, but I found this entertaining.
> 
> > Different approaches to rationality, as illustrated by the margarine brand "I Can't Believe It's Not Butter".
> > 
> > * Eliezer Yudkowsky can believe it's not butter if, and only if, it is not in fact butter. He feels that this ought not to be difficult. He considers the existence of the brand to be a minor, yet symbolic, Civilisational Fail.
> > * Scott Alexander, after a thorough literature review and ten thousand words on the results, is tentatively inclined to believe it's not butter. However, his epistemic status remains "Dairy is not my field, I may be missing something important". He is working on a blog post on the implications for neoreaction.
> > * Brienne Yudkowsky is installing a trigger action pattern to decide whether any given substance is or is not butter; she is currently wiggling her ears whenever the question occurs to her. The next CFAR retreat may include a seminar on her results, if there is enough interest. It is very likely that there will be enough interest.
> > * Gwern hasn't had time to form an actual belief on the point, but he has a five-thousand-word blog post outlining the self-blinding mechanism he will use to test whether he can distinguish it from butter.
> > * Topher Hallquist notes that the important question is not whether it's butter, but whether the production method is an ethical disaster of biblical proportions. He advises people to eat the stuff if, and only if, they believe it was not produced by torturing cows.
> > * Alicorn has written a story in which the protagonist discovers that, actually, it is butter. She is unable to make his civilisation agree that this is an ethical disaster of codexical proportions, but she does manage to arrange his life, and that of her polycule, in such a way that he doesn't have to eat the horrible stuff, and also she gets laid.
> > * Alyssa Vance knows exactly what regulations prevent it from being marketed as "I Do Believe It's Butter", and the precise effects the dairy lobby's nut-grip on Congress has had on American obesity.
> 
> -- https://www.facebook.com/groups/144017955332/permalink/10155985860800333/?comment_id=10155985898315333&comment_tracking=%7B%22tn%22%3A%22R9%22%7D&hc_location=ufi

>> **u/None** [+3]  (3 days later)
>> 
>> /r/rational has no position but has generated a number of short stories riffing on butter related themes, and a long running serial exploring the consequences of a butterless society,

>>> **u/GaBeRockKing** [+1]  *Horizon Breach: http://archiveofourown.org/works/6785857* (5 days later)
>>> 
>>> [Spacebattles](https://forums.spacebattles.com/) has determined that the question of whether or not it's "butter" was implanted by filthy xenos to distract us. Half of the board plans to unleash gigatons of nuclear force in retaliation. The other half has determined through an internal, highly convoluted process, that it not being butter somehow implies human beings can survive antimatter explosions, and therefore plans to launch the entire planet at our enemies.

> **u/None** [+6]  (7 hours later)
> 
> [deleted]

>> **u/gods_fear_me** [+8]  *The Culture* (13 hours later)
>> 
>> There is nothing that horrifies me as much as the idea of not... being anymore. It sometimes makes me physically I'll that one day I simply won't be anymore. No thought, no idea, no discovering stuff, none of my knowledge, the things I value most would just be gone.

>>> **u/Iconochasm** [+3]  (a day later)
>>> 
>>> If it helps, at least you won't be around to be bothered by your non-existence.  It's literally a stressor that is only relevant once you can't be stressed any more.

>> **u/Sailor_Vulcan** [+3]  *Champion of Justice and Reason* (10 hours later)
>> 
>> there's no way this is a real phobia in and of itself. notice the wording of the person who was quoted in the article
>> 
>> >the idea of living forever was even more unsettling than the idea of no longer existing after death.
>> 
>> In other words, he still finds the idea of no longer existing after death to be unsettling. I'm going to taboo the words life and death and immortality so that I can speak perfectly clearly. As we should all know by now, if he doesn't want to cease to exist, it means he wants to continue existing forever.
>> 
>> This "fear of eternity" could just be a fear of the unknown. Maybe fear of things that are very large-scale and impossible to comprehend. Because something that is that large, like the distance between galaxies, is bigger than you are. And there is no way to feasibly plan out and organize schedules around an infinite number days. With an infinite number of days to exist, a person might have no real deadlines or time-constraints on anything they do, except that which they themselves decide to enforce on themselves. Not saying that it's a bad thing, but people would have to put in a bit of work and soul-searching to figure out what they want to do with their time, and a lot of people don't like having to think much.
>> 
>> I mean, I suppose if you're faced with a choice between putting in the effort to figure out what you want to do so that you can live a more active lifestyle, versus lazing about doing nothing and being bored out of your mind, you'd choose to put in the effort so that you're not bored. It would mean that, i.e., if someone invites you to a party on the other side of the milky way once the whole thing has been explored, you need to actually make it to that party *on time* before the party ends. Otherwise you miss the party.
>> 
>> But most people are not that rational, and so they would not think of breaking eternity down into manageable chunks of time for scheduling/organization purposes. They would just look at the astronomical amount of time they have and get overwhelmed.
>> 
>> Or at least that's one possible explanation.

>> **u/trekie140** [+2]  (8 hours later)
>> 
>> I doubt I have an actual phobia, but despite everything I've learned from rationalists and agreeing with nearly all of it I still instinctively shudder at the thought of living forever. I understand that it's a good thing for everyone to become immortal, yet I still don't feel that way. Of course, I'm a theist, so my perspective might be different.

>>> **u/whywhisperwhy** [+2]  (8 hours later)
>>> 
>>> So by "live forever" you mean on Earth, right? That would make some sense to me because it's keeping you from heaven. But in the article it references a Reddit thread where the OP talks about being disturbed by living forever in either heaven or hell without really explaining that point of view (I would think by definition, existing in heaven would take care of the problem).
>>> 
>>> Also, if it makes you feel better, even the "rationalist" version of immortality probably won't truly let people exist for eternity imo.

>>>> **u/trekie140** [+1]  (11 hours later)
>>>> 
>>>> It would if consciousness turns out to be computable, in which case we'd all end up as living digital information. The afterlife I believe in most resembles that of Buddhism where you get to reincarnate until you achieve enlightenment. The utopia rationalists are out to build could end up like that, but it still feels off. [My religious beliefs are in kind an unusual position right now, though.](https://www.reddit.com/r/rational/comments/4mda32/d_friday_offtopic_thread/d3umkmc)

>>>>> **u/whywhisperwhy** [+1]  (14 hours later)
>>>>> 
>>>>> Does anyone have any good discussions on the likelihood of simulated consciousnesses being likely in the near (~60 years of so) future?
>>>>> 
>>>>> I've seen many articles discuss it as if it's very likely, because in theory it sounds easy. But all of the progress in real life I've seen makes it sound extremely difficult in practice.

>>>>>> **u/trekie140** [+1]  (23 hours later)
>>>>>> 
>>>>>> It's easy to predict how it will work when you subscribe to a certain theory of consciousness, which are usually associated with different philosophical views, but none of them are currently falsifiable so they're all equally likely. If you can create a digital copy of a person's mind just by simulating the position of every atom in their brain, then it's only a matter of waiting until we have a computer that can process that information. However, we can't know if that's how consciousness works until the technology exists to test that theory.

> **u/None** [+4]  (3 hours later)
> 
> [deleted]

>> **u/ToaKraka** [+3]  *https://i.imgur.com/OQGHleQ.png* (3 hours later)
>> 
>> *Eco* ([website](https://www.strangeloopgames.com/eco), [Kickstarter](https://www.kickstarter.com/projects/1037798999/eco-global-survival-game), [Steam](http://store.steampowered.com/app/382310)) already has a similar premise.

>>> **u/traverseda** [+1]  *With dread but cautious optimism* (3 hours later)
>>> 
>>> I'm still not entirely sure how their government thing is supposed to work.
>>> 
>>> My idea we to provide a web-service, and the ability to sign things.

>>> **u/gbear605** [+1]  *history’s greatest story* (6 hours later)
>>> 
>>> Have you played this? If so, is it worth the alpha cost or should I wait longer to buy it or not buy it at all?

>>>> **u/ToaKraka** [+2]  *https://i.imgur.com/OQGHleQ.png* (6 hours later)
>>>> 
>>>> > Have you played this?
>>>> 
>>>> No--I only saw some advertisements for it on Facebook.

> **u/None** [+5]  (7 hours later)
> 
> A note on writing: I find my goal of writing 400 words a day more of a relentless driver than the goal of writing for an hour a day, especially when I am destroying whole paragraphs to rewrite it again.

>> **u/Cariyaga** [+1]  *Kyubey did nothing wrong* (8 hours later)
>> 
>> Having a word-goal works well for me. It usually ends up making me waaaay outpace the goal, and when I fail to hit it I don't feel as bad because of that.

> **u/DataPacRat** [+3]  *Amateur Immortalist* (11 hours later)
> 
> **Matrix multiplication**
> 
> Could somebody explain to me, in a way I'd actually understand, how to (remember how to) go about multiplying a pair of matrixes? I've looked at [Wikipedia](https://en.wikipedia.org/wiki/Matrix_multiplication#Rectangular_matrices), I've read linear algebra books up to where they supposedly explain matrixes, and I keep bouncing up against a mental wall where I can't seem to remember how to figure out how to get the answer.

>> **u/somerandomguy2008** [+7]  (14 hours later)
>> 
>> Disclaimer: I didn't know how to do matrix multiplication prior to answering this question. I thought it might help to hear how someone who doesn't grok linear algebra would remember the algorithm.
>> 
>> Personally, I found the first page of [this](http://www.embedded.com/electronics-blogs/programmer-s-toolbox/4007495/Why-multiply-matrices-) to be a fairly intuitive explanation.
>> 
>> Basically, it takes a look at one use for matrices - representing linear equations in a way that clearly separates the different components of the equation (coefficients, unknowns and constants in this case). It then asks one simple question - how do you turn the matrix representation of the linear equations back into a more standard form? Matrix multiplication.
>> 
>> Do this:
>> 
>> 1) Make up three linear equations, each using the same three unknowns, and line them up in three rows. 
>> 
>>     2x + 3y + 4z = 100
>>     3x + 4y + 5z = 126
>>     4x + 5y + 6z = 152
>> 
>> 2) Go ahead and ignore the right half of the equation - it's not important for remembering how to do this.
>> 
>>     2x + 3y + 4z
>>     3x + 4y + 5z
>>     4x + 5y + 6z
>> 
>> 3) Convert this into two matrices (coefficients in one, unknowns in the other).
>> 
>>     [2 3 4][x]
>>     [3 4 5][y]
>>     [4 5 6][z]
>> 
>> 4) Ask yourself - how can you revert from step 3 back to 2? Answering this question reinvents matrix multiplication.
>> 
>>     [2x + 3y + 4z]
>>     [3x + 4y + 5z]
>>     [4x + 5y + 6z]
>> 
>> 5) If you have more columns in your second matrix (step three only has one column), just remember to multiply one column at a time.
>> 
>>     [2 3 4][x a]   [2x+3y+4z 2a+3b+4c]
>>     [3 4 5][y b] = [3x+4y+5z 3a+4b+5c]
>>     [4 5 6][z c]   [4x+5y+6z 4a+5b+6c]

>> **u/AugSphere** [+6]  *Dark Lord of Corruption* (15 hours later)
>> 
>> I'm going to give my own perspective on it, which is symbolical, rather than visual. What we call matrix multiplication is a special case of operating on multidimensional containers.
>> 
>> You matrix is a container of numbers indexed along two dimensions: `A_{i,j}` is the number inside your container, positioned at coordinates  `i` and `j`. The numbers for all values of `i` and `j` taken together are called a 'matrix'.
>> 
>> When you do matrix multiplication you're basically mixing the containers along the shared dimension:
>> `P_{k,l} = ∑_i A_{k,i}*B_{i,l}`, the summation is along the shared index `i` and the non-shared indexes are preserved. The order on the right side doesn't matter, since the multiplication of numbers is commutative (it's better to write them in the same order as the matrices though, this way the repeated index is on the inside and the outside ones are identical on the left and right), but the shared index `i` obviously must have the same range of values in both matrices for it to make sense, which you can figure out from the formula itself.
>> 
>> If you're familiar with usual imperative programming languages (`for` loops in particular), then [this](https://obilaniu6266h16.wordpress.com/2016/02/04/einstein-summation-in-numpy/) might shed some light on how various inner and outer products in linear algebra are all basically the same thing under the hood.

>> **u/ketura** [+7]  *Organizer* (12 hours later)
>> 
>> Easy: if you're doing graphical programming, consult the documentation for the library you're using, and if you're not, change majors.
>> 
>> (Snark aside, I hate that anyone is even *taught* these concepts.  If you're not going to practically need them, there's absolutely no reason to waste everyone's time and effort trying to abstractly understand something that is done with the press of a button anyway.)
>> 
>> After a brief refresher on that wikipedia page, it's something like this:
>> 
>> You have Matrix A and Matrix B.  A has the same number of columns as B has rows, else multiplication is not possible.  Let's assume we're using a similar matrix set to that wikipedia link, so A is
>> 
>> >([a, b, c]
>> 
>> >[x, y, z])
>> 
>> while B is
>> 
>> >([e, u]
>> 
>> >[f, v]
>> 
>> >[g, w])
>> 
>> STEP 1: Start by taking the top row of A.  Rotate it clockwise:
>> 
>> >[a,
>> 
>> >b,
>> 
>> >c]
>> 
>> STEP 2: Move it to overlap the first column of B:
>> 
>> >[ae,
>> 
>> > bf,
>> 
>> > cg]
>> 
>> STEP 3:  Multiply the numbers that overlap, and then add these products together.  This sum is the first number of your product matrix:
>> 
>> >([ae + bf + cg,
>> 
>> STEP 4:
>> Scoot the rotated A row to the right and repeat steps 2 and 3, multiplying each scalar and then summing the products.  Repeat until B is out of columns (which ours is).  Our product matrix now has its first row:
>> 
>> >([ae + bf + cg, au + bv + cw]
>> 
>> STEP 5: We now return to the next (and final) row of A and repeat steps 1-4 with the new row, rotating the row clockwise:
>> 
>> >[x,
>> 
>> > y,
>> 
>> > z]
>> 
>> And lining it up with the first column of B:
>> 
>> >[xe,
>> 
>> > yf,
>> 
>> > zg]
>> 
>> and so on.  Our final matrix is thus:
>> 
>> >([ae + bf + cg, au + bv + cw]
>> 
>> > [xe + yf + zg, xu + yv + zw])
>> 
>> TL;DR I hate the American education system.

>> **u/captainNematode** [+2]  (a day later)
>> 
>> There are five common ways to solve AB = C for C: element by element (i.e. Cik = Σj Aij*Bjk -- fuckin' reddit markup...), column by column (i.e. the columns of C are linear combinations of the columns in A), row by row, breaking the matrices into individual rows and columns and then summing, and breaking the original matrices into blocks and multiplying them to solve for blocks in C. Personally, I tend to think of it in terms of the second, since in my work that's had the most application so far. Check out the first twenty minutes of Gilbert Strang's [Lecture 3](https://www.youtube.com/watch?v=FX4C-JpTFgY) for an explanation.
>> 
>> As for retaining the information, you just gotta apply it often enough for it to become second nature. I'd recommend watching Gilbert's [whole intro-to-linear-algebra lecture series](https://www.youtube.com/playlist?list=PLE7DDD91010BC51F8) -- I found it really easy to follow and a great way to build intuitions about the theory behind linear algebra (it's not super rigorous, though). You can get more course materials [here](http://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/). I've also heard [Klein's Coding the Matrix](http://codingthematrix.com/) is good for practical application, but I haven't made my way through those materials yet.

>> **u/TimTravel** [+2]  (2 days later)
>> 
>> Matrix multiplication corresponds to linear function composition. Write out two linear functions that can compose and try and compute their composition without using matrices. At some point it'll click why matrix multiplication is defined the way it is.

>> **u/DataPacRat** [+2]  *Amateur Immortalist* (3 days later)
>> 
>> I've gotten a reply at LessWrong with a mnemonic so simple I can't forget it, and which seems to do the trick: http://lesswrong.com/r/discussion/lw/nwd/stupid_questions_september_2016/dfax

> **u/xamueljones** [+3]  *My arch-enemy is entropy* (22 hours later)
> 
> Anyone got any advice for making the transition from college to graduate school (Masters or PhD) or to a career? I'm interested in hearing what the folks here have to say. Especially how to make the choice between going to grad school or just going straight for a job.

>> **u/AugSphere** [+3]  *Dark Lord of Corruption* (a day later)
>> 
>> Depends greatly on the degree of credentialism in the relevant field and on availability of independent certification for said field. 
>> 
>> I think IT/CS is one of the fields where people will care more about your actual portfolio and demonstrable skill, and not about the certs you bring, but we'd best get /u/traverseda to comment on this, since he likely has a much better grip on the actual state of affairs there.
>> 
>> If we're talking about mainstream academic institutions, then going for a PhD is pretty much mandatory, I suspect.
>> 
>> I'm finishing up a PhD and expect it to be completely useless, since I plan on switching careers anyway, so keep in mind this fact. By the time you get the degree you may no longer be interested in making use of it.

>>> **u/traverseda** [+4]  *With dread but cautious optimism* (a day later)
>>> 
>>> /u/xamueljones
>>> 
>>> Well first, it's good to keep in mind how good I actually am. You can see my resume [here](https://traverseda.github.io). It's pretty good for Halifax, NS. Which doesn't have a lot of work. It also doesn't yet reflect some of my newer contracts. But I'm not exactly working for google, either. It depends on what you're trying to do.
>>> 
>>> That's with me having dropped out of highschool, and being entirely self-taught. So I like to think I have a pretty decent grasp of turning nothing into a career.
>>> 
>>> Normally my first bit of advice would be to read the sequences and become stronger, but baring that....
>>> 
>>> Step one is to think of it from your potential employers point of view. How do you make *them* money?
>>> 
>>> For example, on my resume I say
>>> 
>>> >Directed the implementation of haystack/solr search engine integration, significantly speeding up long-running natural language processing tasks.
>>> 
>>> Which shows not only familiarity with a technology, but also the tangible improvement of "speeding up tasks". Which did decrease the cost of running and developing NLP tasks. Connect things back to the bottom line.
>>> 
>>> Often equally important, how do you make their life easier? How do you reduce their management burden (be predictable, and predictably competent).
>>> 
>>> I'm happy to talk about specifics, but without knowing more about your field/goals I can't give more specific advice.
>>> 
>>> And also, I was kind of forced into a career by being dirt-poor. I honestly can't say whether or not academia is a bad idea if you're not feeling some serious financial pressure. It might be a good position to leverage to start your own startup, or to do pure research. I don't know.

>>>> **u/xamueljones** [+1]  *My arch-enemy is entropy* (a day later)
>>>> 
>>>> Thanks for the reply.
>>>> 
>>>> I'm in my last year in college and trying to decide between taking the time and expense to go to graduate school versus going straight into a job. So I'm going to graduate with a BS in Cognitive Science and a minor in Computer Science.
>>>> 
>>>> I've been leaning towards going into work in non-academia related fields which eliminates the need for a PhD, but there's still the possibility of needing a Masters for a career.
>>>> 
>>>> What I'm currently trying to do now is make a list of potential jobs and decide what I have to do to get these jobs.
>>>> 
>>>> I appreciate the advice!

>>>>> **u/traverseda** [+5]  *With dread but cautious optimism* (a day later)
>>>>> 
>>>>> > still the possibility of needing a Masters for a career.
>>>>> 
>>>>> Eh... maybe. I'd be surprised. At least for a career in CS.
>>>>> 
>>>>> What do you expect to actually get out of a masters? Aside from credential-ism. Is there anything you can do to show you have the same skills?
>>>>> 
>>>>> Why not start doing a "masters thesis" today? Getting some open-source work under your belt is an excellent way to show potential employers that you can actually code. Something a lot of masters students seem to be unable to do.
>>>>> 
>>>>> There's a very real concern that university grads aren't actually going to be a better fit then someone fresh off-of a programming bootcamp.
>>>>> 
>>>>> http://blog.triplebyte.com/bootcamps-vs-college
>>>>> 
>>>>> The sad fact is that until you have a tens of thousands of lines of real code under your belt, you're probably still a junior programmer. No matter what your education.

>>>>>> **u/xamueljones** [+2]  *My arch-enemy is entropy* (a day later)
>>>>>> 
>>>>>> Yeah that makes sense. It's a good thing then, that I've been coding for years since high school. I'm actually working in two research labs this year. One of them as a coding monkey to get their experiments working (I'd be done by now if they didn't keep changing the task designs on me!) and the other is to get experience conducting the experiments with face-to-face interaction with subjects.
>>>>>> 
>>>>>> The main issue I actually have is direction. I have marketable skills, but I'm not certain of what I will be doing in the future. What I'm asking for is how do people figure out what jobs they know they can be happy with? I decided to ask several different sources: family, older friends, college resources, and here.

>>>>>>> **u/traverseda** [+1]  *With dread but cautious optimism* (a day later)
>>>>>>> 
>>>>>>> > What I'm asking for is how do people figure out what jobs they know they can be happy with?
>>>>>>> 
>>>>>>> Fucked if I know. I very rarely work more then 20 hours a week, and take mostly take on small-ish contracts. Good luck.

>>>>>>>> **u/xamueljones** [+3]  *My arch-enemy is entropy* (a day later)
>>>>>>>> 
>>>>>>>> Yeah...thanks for talking to me about it though. It helped to get my worries out into words for someone else to understand.
>>>>>>>> 
>>>>>>>> Thanks!

> **u/CouteauBleu** [+2]  *We are the Empire.* (an hour later)
> 
> Does anyone here know good *The Clone Wars* fanfics?

>> **u/Mbnewman19** [+2]  (8 hours later)
>> 
>> I don't know of fanfics, but there is a line of published fiction by Karen Traviss (see [here](https://www.amazon.com/Hard-Contact-Star-Wars-Republic/dp/0345478274/ref=asap_bc?ie=UTF8) for the first one), which are absolutely amazing. She personalizes the clones so well, and adds a level of backstory to episode 3 that is wonderful.

>>> **u/ToaKraka** [+3]  *https://i.imgur.com/OQGHleQ.png* (8 hours later)
>>> 
>>> She's also infamous for making the clones and Mandalorians into Gary Stus.
>>> 
>>> Discussions of the topic: [1](https://forum.rpg.net/showthread.php?469775) [2](http://np.reddit.com/r/StarWarsEU/comments/3npx0w)  
>>> [YodaKenobi's famous excoriation of Traviss's *Legacy of the Force: Revelation*](http://web.archive.org/web/20100115082418/http://boards.theforce.net/literature/b10003/28128642/p5)

> **u/Cariyaga** [+3]  *Kyubey did nothing wrong* (2 hours later)
> 
> I'm around fifteen thousand words into my Undertale fanfic and only on the second day. I'm discovering that my writing style is very verbose. I'll probably have to pester someone to help me cut the size of it, but for now I'm happy to be as lengthy in volume as I please, just for the sake of practice.
> 
> It's going well that aside, though. Not published yet, for those curious, as I haven't done any major revisions for the first chapters and want to make sure everything's consistent first.

>> **u/DaystarEld** [+5]  *Pokémon Professor* (15 hours later)
>> 
>> Remember, the first draft is always going to be verbose. Sounds like you're doing a good job of not letting that stop you from the most important thing: getting words on page :)

>>> **u/Cariyaga** [+2]  *Kyubey did nothing wrong* (18 hours later)
>>> 
>>> Yup, I've read enough of authors' musings to know many of the usual pitfalls. Picking something to write on that I know I'm exceptionally unlikely to lose interest in helps, too.

> **u/elevul** [+1]  *Cyoria Observer* (2 days later)
> 
> Sousei no Onmyouji's OP2 is absolutely awesome. Been looping it for 2 weeks already, and am still in love!
> 
> https://youtu.be/7cLXPW0iHfM

---

