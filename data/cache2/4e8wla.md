## I finished building my CYOA! Build & optimize your own character in a world where ability-granting gems can be traded like commodities.

* Author: u/luminarium *
* URL: https://www.reddit.com/r/rational/comments/4e8wla/i_finished_building_my_cyoa_build_optimize_your/
* Score: 17

* Created: 2016-04-11T02:49:37

### Post:

Hi everyone,

A week back I saw a CYOA (create-your-own-adventure) [here](https://www.reddit.com/r/rational/comments/4augy6/c_i_finished_making_that_cyoa/) and asked /u/Rhamni how to set one up, and was graciously sent three files to work off. 

What followed was one week of what felt like a fever dream. I first learned HTML, then learned CSS, and then learned JavaScript, creating original text and images and functionality along the way, and at the end of it produced the work below. It took me around 50 hours (and hundreds of versions) to put it all together. I found it to be an amazingly immersive and edifying learning experience. I'm eager to help out if anyone wants to make one too.

This is the first input I'll be getting from anyone. Any bugs? Any new options you want to see added? Suggestions for improving presentation or mechanics? I'm eager to know what feedback you have!

----

**[Here's the Link.](https://0a8cf07c6917b11a60c81f6f03f984dc194395ca.googledrive.com/host/0B-uYtW6inz_aNU9IbGo1QWl4SzA/index.html)** Thanks everyone for your time!

### Comments:

> **u/TennisMaster2** [+5] *
> 
> > You grew up an orphan on the streets of a town or city. You have nothing to your name. You travel from village to village, singing of epic tales and great deeds done. Along the way you start to learn from them, and become a sort of jack of all trades. 
> > As a reborn god of Luminara, you have pure divine essence invested within you. Unbridled power radiates from your very skin. Your family acquired you the services of a tutor in the magical arts. From youth you had learned the ways of spellcasting, and now it flows from you with almost instinctive ease.
> There doesn't seem to be any disadvantages to purely picking options that give the most resources.  If certain opportunities were only accessible by a slave, for instance, people might be incentivized to try for characters of weaker backgrounds.
> Unique take on the concept!  Feels like a good beginning to a fun text-based adventure game.
> 

>> **u/vakusdrake** [+1] *
>> 
>> I suppose choosing a worse background makes it harder which increases difficulty as it were. It's something of a challenge figuring out how to make a peasant thief with mediocre magical power take over the world.
>> 

> **u/gabbalis** [+5] *
> 
> Pfft. I don't know what everyone else is whining about [seems balanced to me](https://i.imgur.com/o7UxDBR.png) I wasn't even able to buy everything! only like, half.
> Edit: Oh also, I found myself unable to buy Sigil Invention or Magicite Discovery for some reason. I had the prerequisites, no box came up telling me I needed something, I just clicked to no effect.
> Edit2: Also, from a story perspective, why was I only able to find one virgin maiden to sacrifice? Surely I couldve extorted a yearly tithe of virgin maidens out of the nobles of the land to continuously increase my power. Speaking of which, I start with 250 cash for being royalty, but extorting the royals only gives me an additional 125! What gives! I'm assasinating these cheapasses first thing.
> 

>> **u/luminarium** [+1] *
>> 
>> Thanks! Fixed the bug w/ Sigil Invention and Magicite Discovery.
>> Not enough blood slaves eh? You should play Mictlan in Dominions (Illwinter), and run a blood economy :) Anyway, I've updated it to give 3 now. And yea, I realized that Astral Assassination was way too powerful (lore-wise).
>> 

>>> **u/gabbalis** [+2] *
>>> 
>>> One other thing. The purple numbers are Spiritite required to actually cast your spells as I understand it. (I assume this doesn't use up the spiritite but that isn't explicit.) Do I have to actually carry it all around? How heavy will my bag have to be to cast temporal alteration 2?
>>> AHEM, sorry distracted, I was saying, the CYOA prevents you from buying an ability if you would have less Spiritite than the purple number after buying it. But what you can do is buy an ability that requires Spiritite... and then sell it all, or use it all on mental things, etc.
>>> The CYOA should either not let you do that, or specify in the final synopsis that you can't actually cast any of your spells until you come across more Spiritite.
>>> Also out of pure curiosity... Vitalite is concentrated life and blood. Spiritite comes from trapped souls according to Soul Entrapment. Magicite... well, Soul Trapping does mention trapping souls in Magicite, but that feels like it might be a typo. Other than that the only mention is finding Magicite in ruins. Where does it actually come from? Mysteries upon mysteries....
>>> 

>>>> **u/luminarium** [+1] *
>>>> 
>>>> Thanks, you have no idea how happy I am that you thought deeply enough about the lore and worldbuilding to notice these issues!
>>>> The idea is supposed to be
>>>> * Ruby + the blood of the ritually slain = vitalite
>>>> * Vitalite is a measure of life force; it is the sum total of 1) your innate life force, 2) any loose vitalite you're carrying; 3) any vitalite you've swallowed; 4) any vitalite inset in artifacts you're carrying.
>>>> * Sapphire + luminaria = magicite
>>>> * Magicite is a measure of skill versatility; it is the sum total of 1) your bloodline's versatility, 2) any loose magicite you're carrying; 3) any magicite you've swallowed; 4) any luminaria you've taken into yourself; 5) any magicite inset in artifacts you're carrying; 6) any spells you've learned.
>>>> * Onyx + the soul trapped within it = spiritite
>>>> * Spiritite is a measure of magical power; it is the sum total of 1) your bloodline's power, 2) any loose spiritite you're carrying; 3) any spiritite you've swallowed; 4) any spiritite inset in artfacts you're carrying; 5) power gains from spellcasting practice. But it is *also* a measure of intellectual power, since it's spiritual/mental power; *and* it can be inset into your minions (which 'reserves' your spiritite).
>>>> * You can also extract your own innate life force / bloodline power etc, and put it into gems (though obviously not learned spells / power gain from spellcasting practice).
>>>> The underlying problem is that 
>>>> * I don't want there to be too many numbers at the top of the page (Age of Empires 2 has 4 resources, and that's already a hassle, etc);
>>>> * I want the numbers to be something concrete and physical as it's easier to relate to and easier to depict (gemstones) and which make sense as something tradable;
>>>> * I want to include a lot of variety and comprehensive worldbuilding, which involves a wide variety of aspects, much of which can't be condensed into 'gems'.
>>>> But because I can only use 4 numbers (3 gem types + gold), these different things have to get aggregated. So you wind up with like 30 spiritite when maybe 10 of that is coming from spellcasting experience and another 10 from bloodline potency, etc. 
>>>> There's also the issue that yes, I need to somehow identify/deactivate those skills you don't have sufficient spiritite for.
>>>> Also, thanks for catching that, I'll have to update the Soul Trapping description.
>>>> 

> **u/callmebrotherg** [+4]  *now posting as /u/callmesalticidae**
> 
> > What followed was one week of what felt like a fever dream. I first learned HTML, then learned CSS, and then learned JavaScript, creating original text and images and functionality along the way, and at the end of it produced the work below. It took me around 50 hours (and hundreds of versions) to put it all together. I found it to be an amazingly immersive and edifying learning experience.
> This, more than anything else, seems like a good reason for me to come up with a CYOA. 
> EDIT: FYI, the tab still says "Interactive Magical Realm CYOA."
> 

>> **u/luminarium** [+1] *
>> 
>> You totally should! I can walk you through the process if you'd like.
>> 

>>> **u/callmebrotherg** [+2]  *now posting as /u/callmesalticidae**
>>> 
>>> Thanks! I am busy in the near future but will definitely hit you up on that offer. >:]
>>> 

> **u/LeonCross** [+3] *
> 
> Probably a stupid question, but is there a game or is this just an exercise in min/maxing character concepts within a system?
> Not that I mind doing so as I've already spent a few hours playing with options.
> 

>> **u/luminarium** [+1] *
>> 
>> No, no game. I *wish* there were one though!
>> 

> **u/MrCogmor** [+2] *
> 
> Depending on your starting resources it seems either horribly broken or ridiculously weak. 
> Given that you can freely convert between gold and the magic gems having multiple resources is just annoying because of having to convert between them to meet prerequisites. Choosing magical blood gives you magicite and spiricite but nothing stops you from going to the conversion area and converting it into gold and then into vitalite. The simplest way to fix the problem in the short term would be to change the error code to perform automatic conversions of your resources to obtain whatever is missing
> There is way too many options. You have 20 categories of abilities for goodness sake. The mistform, flameform, earthform and so on abilities render most other regeneration and physical durability enhancements irrelevant.
> I think the abilities should be divided into three main categories based on whether they are physical, spiritual or magical enhancements. 
> Physical would contain the regeneration, immortality, shapeshifting, sensory options (excluding mage sight universal communication and animal communication.). It would also contain the resistance abilities and transformative abilities (excluding transmutation)
> Mental would contain all the intellectual abilities, psychic abilities, soul abilities, command abilities and some eldritch abilities.
> Magic would contain the vorpal, metamagic, abjuration, corporeal, temporal and elemental abilities, universal communication and animal communication
> Life stealing kiss and life granting kiss are excessive. You only need the touch options. I'm also not sure how the youth stealing works with eternal youth and regeneration.
> Doom marking, unhealing, Pain wracking and blood parasitism don't really deserve to be separate options. You only really need one excruciating death curse. (The biological options would render blood parasitism redundant anyway). The same thing with Banishment, Reality Tearing and Annihilation. You only need one erase from existence spell and they are kind of redundant with disintegration from energy casting. ( I understand that they are different in that planar travel counters banishment but it's still a boring choice for a player to make. If someone is immune to conventional attacks and banishment then you are probably out of your league in any case (particularly with the high cost of planar travel) 
> The illusion abilities seem largely useless compared to the other options, especially with how cheap true sight is. The camouflage option only lets you camouflage your skin which is blatantly useless and embarrassing. The telekinesis options are similarly boring.
> Water walking should be in the same category as water breathing not in telekinesis with the other option.
> I do like the art though and the design of the layout, it's quite nice. I have noticed the background image stutters when I scroll with the mouse. It might just be my browser but I think it might be that you are respositioning it using javascript in which case I'd suggest you change it to use CSS with background-attachment:fixed;
> 

>> **u/luminarium** [+3] *
>> 
>> You raise a lot of good points!
>> I really should make the exchange have a bid-ask spread, like 4 gold to sell but 5 to buy, for each of the three gems. 
>> I want to give users the opportunity to build characters the way they want, not just min/max the hell out of it. Lore-wise, it makes perfect sense that nobility will have more opportunities and thus get more powers than orphans, etc. But if users want to create an orphan character for more of a challenge / a character with weaker abilities, they have the option to do that too. Same with the abilities - some are more powerful per unit cost than others, but the point is to give users the opportunity to discover this for themselves. But I should have all those spellcasting sections start collapsed be expandable.
>> Having just three sections for abilities won't look good - the spellcasting abilities are far too extensive, and it'll be more overwhelming if I turned it into a single list. 
>> I'm using background-attachment:fixed; . I never saw any stuttering. Could be a slow computer or something? :/
>> 

>>> **u/MrCogmor** [+1] *
>>> 
>>> Lore wise I don't see how your medieval society avoids becoming a technologically advanced transhumanism mess ruled by warring god kings that horde all the magical enhancement stones. Having some abilities more powerful per unit cost is fine the problem is that it's just the more expensive abilities that give more bang for your buck. For example acute hearing is one vitacite and eternal youth is nine when acute hearing is nowhere near ninth the value that eternal youth is.  The pattern holds true for other things as well such that a little bit of additional wealth can make a character an order of magnitude more powerful. It would be much more balanced if the earlier and cheaper upgrades were more powerful and getting additional advantages provided diminishing returns.
>>> There are also so many abilities that you have no idea of the value of because you don't know the local meta-game. For example if there are a lot of stealthy people then 360 vision increases in value. If there are a lot of guards with 360 degree vision then buying stealth massively decreases in usefulness. A player cannot really make an informed choice without more knowledge about your setting. A number of other choices have similar issues banishment/planar travel, mental protection/mind altering, true sight/illusions and so on.
>>> Choosing a challenge is perfectly fine though I find it odd that some starting backgrounds don't give you anything or only let you afford a single shard of vitacite.
>>> You can further subdivide them if you want. The main purpose of the division is to allow players to focus on defensive, offensive or cognitive / trump-card abilities.
>>> I've found out the stuttering was actually just the browser I was using at the time.
>>> 

>>>> **u/luminarium** [+1] *
>>>> 
>>>> > Lore wise I don't see how your medieval society avoids becoming a technologically advanced transhumanism mess ruled by warring god kings that horde all the magical enhancement stones.
>>>> Yeah, I don't know either. :(
>>>> I didn't want magicite cost to be a min/maxing reflection of the utility of an ability, but rather the number of different subabilities making up that ability. For example firecasting is 3 because you can create, snuff out, and move fire; soul trapping is 2 because you can trap a soul and you can free it, etc. It also means firecasting 2 only costs 1 magicite and not say 10. Or, that's the general idea. Clearly didn't work out all that well since eternal youth is 9 when it should have just been 1. It makes sense from a lore wise approach (in the setting there's different kinds of magicite each granting its own distinct ability, and they wouldn't be priced the same; but that's far too complex to present in the website). I just don't know how to balance it. 
>>>> > A player cannot really make an informed choice without more knowledge about your setting.
>>>> Good point! Any idea how I can get this into the website unobtrusively (ie lore)? 
>>>> Some backgrounds are very poor because once again it makes sense from a lore perspective. Given how expensive powers are, being an orphan and being a laborer doesn't really make much of a difference, you aren't getting gems either way.
>>>> I updated the website with bid-ask spreads, and made the spellcasting sections start off collapsed. I also inserted a few pieces of writing to break up the monotony of the spellcasting lists, but I clearly need more lore.
>>>> 

>>>>> **u/MrCogmor** [+1] *
>>>>> 
>>>>> This is a good article on game balance. http://www.gamasutra.com/view/feature/134768/understanding_balance_in_video_.php?print=1
>>>>> 

>> **u/callmebrotherg** [+1]  *now posting as /u/callmesalticidae**
>> 
>> > There is way too many options. You have 20 categories of abilities for goodness sake.
>> I'd say that this is a problem with the last interactive CYOA that I saw as well. Hopefully it doesn't become a trend.
>> 

> **u/None** [+1] *
> 
> WAY too many options and not enough drawbacks. Would go more into detail, but previous posts seem to already have.
> 

> **u/vakusdrake** [+1] *
> 
> I'm not sure why you set the sell rate for crystals different to the buy rate. I'm not sure it serves any purpose, and it really only serves to make micromanagement slightly more inconvenient. 
> Having to reload the page and start over any time you want to slightly tweak something is a bit annoying, i'm not really sure why you changed it.
> Unless you have a really good reason to keep it the way it is I would recommend you change it back, for ease of use.
> 

>> **u/luminarium** [+1] *
>> 
>> Sure. Well, if it were all just perfectly interchangeable then there'd be no difference between the 4 resources, and everything then just simplifies into being a single cost. This way I make the distribution of the 4 resources you get actually matter in a small way. Much the same way as the market in AoE 2 having a bid-ask spread makes you consider your options more carefully, I think this makes for more careful consideration of options before making a decision. I've noticed that in the games I've played, I tend to pay closer attention to the details of each option, and weigh things in my mind more, when I can't respec costlessly.
>> 

>>> **u/vakusdrake** [+1] *
>>> 
>>> The problem with that is that, you don't have any way to reverse your decisions regarding allocation, and as a result since you will probably want to squeeze every last point into something, it makes it so that to get a optimal build you would have to work everything out separately on a piece of paper.
>>> 

>>>> **u/luminarium** [+1] *
>>>> 
>>>> Yea, well if someone gets *that* into-it, I'd be honored :)
>>>> 

>>>>> **u/vakusdrake** [+1] *
>>>>> 
>>>>> Well yes I suppose this won't be a problem for everybody. However someone like me can't rest, until I have achieved the maximum efficiency! 
>>>>> And if getting the best build requires using pen and paper then it kind of renders the whole code kind of pointless, because if you are doing the math yourself then you might as well just consult a written list of the options.
>>>>> Also I'm not sure what you mean when you worry about them being interchangeable, I'm just not sure what specific scenario you hope to avert?
>>>>> 

>>>>>> **u/luminarium** [+1] *
>>>>>> 
>>>>>> well, the situation where someone picks options that add a lot of vitalite to start them off, then instead of getting physical abilities they roll it all over into magicite and get spellcasting abilities instead... or where someone picks up a prereq for an opportunity to get the extra points then rolls their points into another ability to get extra points from a different opportunity, etc. 
>>>>>> The point isn't exactly to get the most min/maxed build, though I'm sure that's a major interest to people on r/rational. It's also to build a character according to how you'd want them to be; in other words, qualitative rather than quantitative.
>>>>>> 

>>>>>>> **u/vakusdrake** [+1] *
>>>>>>> 
>>>>>>> Hmm it does see though that since so few things actually grant you vitalite (compared to the other gems) if you want to succeed that route it would make sense to go all out and punishing refunds isn't going to make a difference. 
>>>>>>> As for the refunding things after you used them to get a skill, well that's a blatant exploit/cheat, and if they are willing to do that then I can't imagine why they wouldn't just pick a more powerful background starting out, it's not like there's a penalty. Also even with the refund penalty that doesn't in theory make that exploit no longer effective, it just makes it slightly less efficient.
>>>>>>> Honestly the only way I can think of to exploit the system if refunds weren't penalized, would be to refund a bunch of magicite (since so many things give you that) and then use that to get a bunch of vitalite. 
>>>>>>> The problem with trying to do that is that magicite is just more valuable than vitalite. You can do more with magicite than you can with vitalite, for instance indestructibility and other such abilities render most of the highest tier vitalite abilities pointless. 
>>>>>>> This is hardly something I would blame you for however, in pretty much every rpg at high levels magic always outstrips brawn. 
>>>>>>> So yeah to reiterate: refunding penalties only make a difference, if the game gives you a whole bunch of one resource, and another resource is more valuable. However your game gives you mostly magicite and and spiritite which are also the resources you need for any remotely optimized build. So in reality I see the refund penalty as kind of a unnecessary annoyance.
>>>>>>> 

>>>>>>>> **u/luminarium** [+1] *
>>>>>>>> 
>>>>>>>> Yea all good points... I think I need to work on balancing the gems and ability costs and everything.
>>>>>>>> The other main purpose of vitalite is for healing afflictions, which is a feature I haven't implemented. Basic idea would be that opportunities have a chance of causing afflictions, which could cost more to heal than the benefits of the opportunity; so that everything you choose is a gamble. Could also be extended to getting skills, ie. picking up teleporting could get you splinched, etc. The more opportunities you pick up, the more afflictions you'd wind up getting. This would also act to counterbalance unscrupulous characters simply picking up all the opportunities.
>>>>>>>> 

>>>>>>>>> **u/vakusdrake** [+1] *
>>>>>>>>> 
>>>>>>>>> Yeah see as it stands healing's not really worth it, in order for healing to ever be more effective than regen or other personal powers, you need to implement npc companions or something else that makes it worthwhile to be thinking about healing other people.
>>>>>>>>> 

---

