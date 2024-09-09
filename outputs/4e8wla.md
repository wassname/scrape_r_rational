## I finished building my CYOA! Build & optimize your own character in a world where ability-granting gems can be traded like commodities.

### Post:

Hi everyone,

A week back I saw a CYOA (create-your-own-adventure) [here](https://www.reddit.com/r/rational/comments/4augy6/c_i_finished_making_that_cyoa/) and asked /u/Rhamni how to set one up, and was graciously sent three files to work off. 

What followed was one week of what felt like a fever dream. I first learned HTML, then learned CSS, and then learned JavaScript, creating original text and images and functionality along the way, and at the end of it produced the work below. It took me around 50 hours (and hundreds of versions) to put it all together. I found it to be an amazingly immersive and edifying learning experience. I'm eager to help out if anyone wants to make one too.

This is the first input I'll be getting from anyone. Any bugs? Any new options you want to see added? Suggestions for improving presentation or mechanics? I'm eager to know what feedback you have!

----

**[Here's the Link.](https://0a8cf07c6917b11a60c81f6f03f984dc194395ca.googledrive.com/host/0B-uYtW6inz_aNU9IbGo1QWl4SzA/index.html)** Thanks everyone for your time!

### Comments:

- u/TennisMaster2:
  ```
  > You grew up an orphan on the streets of a town or city. You have nothing to your name. You travel from village to village, singing of epic tales and great deeds done. Along the way you start to learn from them, and become a sort of jack of all trades. 

  > As a reborn god of Luminara, you have pure divine essence invested within you. Unbridled power radiates from your very skin. Your family acquired you the services of a tutor in the magical arts. From youth you had learned the ways of spellcasting, and now it flows from you with almost instinctive ease.

  There doesn't seem to be any disadvantages to purely picking options that give the most resources.  If certain opportunities were only accessible by a slave, for instance, people might be incentivized to try for characters of weaker backgrounds.

  Unique take on the concept!  Feels like a good beginning to a fun text-based adventure game.
  ```

- u/gabbalis:
  ```
  Pfft. I don't know what everyone else is whining about [seems balanced to me](https://i.imgur.com/o7UxDBR.png) I wasn't even able to buy everything! only like, half.

  Edit: Oh also, I found myself unable to buy Sigil Invention or Magicite Discovery for some reason. I had the prerequisites, no box came up telling me I needed something, I just clicked to no effect.

  Edit2: Also, from a story perspective, why was I only able to find one virgin maiden to sacrifice? Surely I couldve extorted a yearly tithe of virgin maidens out of the nobles of the land to continuously increase my power. Speaking of which, I start with 250 cash for being royalty, but extorting the royals only gives me an additional 125! What gives! I'm assasinating these cheapasses first thing.
  ```

- u/callmebrotherg:
  ```
  > What followed was one week of what felt like a fever dream. I first learned HTML, then learned CSS, and then learned JavaScript, creating original text and images and functionality along the way, and at the end of it produced the work below. It took me around 50 hours (and hundreds of versions) to put it all together. I found it to be an amazingly immersive and edifying learning experience.

  This, more than anything else, seems like a good reason for me to come up with a CYOA. 

  EDIT: FYI, the tab still says "Interactive Magical Realm CYOA."
  ```

- u/LeonCross:
  ```
  Probably a stupid question, but is there a game or is this just an exercise in min/maxing character concepts within a system?

  Not that I mind doing so as I've already spent a few hours playing with options.
  ```

- u/MrCogmor:
  ```
  Depending on your starting resources it seems either horribly broken or ridiculously weak. 

  Given that you can freely convert between gold and the magic gems having multiple resources is just annoying because of having to convert between them to meet prerequisites. Choosing magical blood gives you magicite and spiricite but nothing stops you from going to the conversion area and converting it into gold and then into vitalite. The simplest way to fix the problem in the short term would be to change the error code to perform automatic conversions of your resources to obtain whatever is missing

  There is way too many options. You have 20 categories of abilities for goodness sake. The mistform, flameform, earthform and so on abilities render most other regeneration and physical durability enhancements irrelevant.

  I think the abilities should be divided into three main categories based on whether they are physical, spiritual or magical enhancements. 

  Physical would contain the regeneration, immortality, shapeshifting, sensory options (excluding mage sight universal communication and animal communication.). It would also contain the resistance abilities and transformative abilities (excluding transmutation)

  Mental would contain all the intellectual abilities, psychic abilities, soul abilities, command abilities and some eldritch abilities.

  Magic would contain the vorpal, metamagic, abjuration, corporeal, temporal and elemental abilities, universal communication and animal communication

  Life stealing kiss and life granting kiss are excessive. You only need the touch options. I'm also not sure how the youth stealing works with eternal youth and regeneration.

  Doom marking, unhealing, Pain wracking and blood parasitism don't really deserve to be separate options. You only really need one excruciating death curse. (The biological options would render blood parasitism redundant anyway). The same thing with Banishment, Reality Tearing and Annihilation. You only need one erase from existence spell and they are kind of redundant with disintegration from energy casting. ( I understand that they are different in that planar travel counters banishment but it's still a boring choice for a player to make. If someone is immune to conventional attacks and banishment then you are probably out of your league in any case (particularly with the high cost of planar travel) 

  The illusion abilities seem largely useless compared to the other options, especially with how cheap true sight is. The camouflage option only lets you camouflage your skin which is blatantly useless and embarrassing. The telekinesis options are similarly boring.

  Water walking should be in the same category as water breathing not in telekinesis with the other option.

  I do like the art though and the design of the layout, it's quite nice. I have noticed the background image stutters when I scroll with the mouse. It might just be my browser but I think it might be that you are respositioning it using javascript in which case I'd suggest you change it to use CSS with background-attachment:fixed;
  ```

  - u/luminarium:
    ```
    You raise a lot of good points!

    I really should make the exchange have a bid-ask spread, like 4 gold to sell but 5 to buy, for each of the three gems. 

    I want to give users the opportunity to build characters the way they want, not just min/max the hell out of it. Lore-wise, it makes perfect sense that nobility will have more opportunities and thus get more powers than orphans, etc. But if users want to create an orphan character for more of a challenge / a character with weaker abilities, they have the option to do that too. Same with the abilities - some are more powerful per unit cost than others, but the point is to give users the opportunity to discover this for themselves. But I should have all those spellcasting sections start collapsed be expandable.

    Having just three sections for abilities won't look good - the spellcasting abilities are far too extensive, and it'll be more overwhelming if I turned it into a single list. 

    I'm using background-attachment:fixed; . I never saw any stuttering. Could be a slow computer or something? :/
    ```

---

