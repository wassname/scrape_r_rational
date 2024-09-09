## GPT-2 - Ticker-Tape Method for Idea Generation

### Post:

At this point, I'm sure we're all aware of https://transformer.huggingface.co

I've been messing around with it a lot, and to the surprise of approximately none of you, I've found it's really, frighteningly advanced. I think using it as an autocomplete is probably suboptimal. This thing has pretty solid spelling and syntax, but it's clearly looking at our world like we look at Gostak.

Having said that, there are other use-cases which GPT-2 excels at, for the creative writer, the worldbuilder, or the GM.  One that I've stumbled across is what I think of as the ticker tape method. Using this method, you can control GPT-2's behaviour to implement things like the combinatoric power generator that /u/alexanderwales posted a a few years ago ([blogpost](https://thingswhichborepeople.blogspot.com/2016/01/creating-superpowers-through-yes-and.html), [direct link](http://alexanderwales.com/generator.html)). And far more. 

The key, here, is giving GPT-2 a pattern to work with. The more regular, the better, but the system knows enough that it can recognise most conceptual classes given enough to start with. Ticker-tape is what I call this sort of structured input.

Here's an example of Ticker-tape:

    1
    2
    3
    4

It's output:
    
    4
    5
    6
    7
    8
    9
    10
    11

GPT-2 can count arbitrarily far, as far as I can tell. It can also count down, but doesn't understand negative numbers. GPT-2 can also correctly continue a sequence that [in/de]crements by 2 - but *only* with even numbers, and only with many, many lines to establish the pattern. All of this is interesting for people trying to learn about GPT-2's, er, "cognitive limits", but is not germane to the topic of this post. So, moving on...

Another  example of Ticker-tape:

    List of Superpowers
    Flight.
    Ability to fire coins at mach 47.
    Invulnerability.
    Power to turn chewing gum into lava.
    Heat vision.
    Insect control.
    Transformation into invulnerable skeleton.
    Summoning demons.
    Immortality.

Output from this tape:

    Telekinesis.
    The ability to teleport himself between planets.
    Teleportation (using electricity) or transformation (using fire).
    The ability to move through water at speeds not seen before.
    Matter Manipulation.
    Can turn on fire or turn on electricity at will.
    Aether manipulation.
    Mana Manipulation.
    Flexibility.
    Can manipulate matter to create any effect he desires.
    Can create energy fields from nothing.
    Transformation of energy.
    Energy Shield Manipulation.
    Energy Manipulation/Resistance.
    Strength and endurance, and flight/water manipulation.
    Transformation abilities: Shapechange (from solid into liquid), energy manipulation/Resistance (from liquid to gas)
    Superior Strength.

In this case, I let a pronoun slip in, and GPT-2 inferred that these were powers belonging to that pronoun. In an earlier session (which included "THE WORLD" as a superpower output, thereby implying GPT-2 knows what JoJo is), the list was of a higher quality because I suppressed pronouns when they appeared. You need to watch out for the network making that sort of innovation when using a simple prompt with variable structure (as above), because once the topic is some person's powerset, or attributes, GPT-2 tends to produce less diverse suggestions.

Here's ticker-tape that gets GPT-2 to implement Alexander Wales' power idea generator - this is an example of a simple prompt with invariant structure. Generally, these are easier to work with because the odds of GPT-2 inserting something that lowers the quality of the suggestions provided is itself lower due to how rigid the guidelines are. Since we already have Alaxander Wales' generator, the ticker tape is output taken directly from that generator:
    
    Super speed. Yes, but happiness.
    Water manipulation. Yes, and happiness.
    Air manipulation. Yes, and range.
    Shapeshifting. Yes, but movement.
    Flight. Yes, but absorption.
    Shields. Yes, and crowds.
    Time travel. Yes, but age.
    
Example output:
    
    Insects. Yes, but flying.
    Time travel. Yes, but speed.
    Sonic Boom. No, I don't like that one.
    Chromatic powers. Yes, but light.
    Drones. Yes, but water.
    Curse of the Void. Yes, but a curse.
    Power armor. Yes, and range.
    Speed. Yes, but darkness.
    Amorphous. Yes, and light.
    Banishment. Yes, and the moon.
    Death. Yes, but the sun.
    Celerity. Yes, but death.
    Teleportation. Yes, but air.
    Frost. Yes, and a curse.
    Eidolon. Yes, but a death.

The sonic boom line was saved in a text editor, but kept out of the feedback loop: because it would have poisoned GPT-2 with an out-of-format entry. One of the benefits of Huggingface's implementation is that the system will (usually) provide suggestions in one sentence chunks. The dovetails nicely with the format, since you can randomly generate an interesting left side, then an interesting right side match. The main reason why it can be worthwhile to take the output of an already-written thing generator and place it in GPT-2 is because most if not all combinatoric thing generators work along a principle of having finite, coder-curated lists of valid options. GPT-2 has a vocabulary nearly as large and the entirety of the english language. And, if you nudge things in the right direction, it also knows words from various foreign languages - no guarantee of even nominal coherence there though. Once thing to note here is that, though my list of seven outputs was enough to get suggestions, when you have a combinatoric thing generator to harvest from, it's usually best to get a lot of examples. Another thing to note is that GPT-2 likes using things that it used before, or that are on the ticker-tape. There parameters you can use to remove that bias, but it's less likely to get stuck in a rut if it already sees a lot of variety. In this case, death, curse, and light all got re-used due to this bias.

Finally, just to show that this concept actually is suitable for more complex content, here's something different:

> PRIME OUTER GODS: THE NEVERBORN, KIN OF VOID
>     
> Yog-Sothoth is described as a spirit that is the embodiment of the void in the universe, or rather that is the void. It is a spirit from the very bottom of space. Its existence is implied to be a part of the fabric of reality itself. The world as we know it begins as an illusion created by the gods, and as it continues through the ages the world becomes less and less real.
>     
> Azathoth is the first and only manifestation of the void. It is a spirit that has existed as the first aspect of the cosmos and has always existed in its present form as the second aspect of the cosmos. Azathoth is always present in the universe; there is no alternative.
>     
> Nyarlathotep has the potential to cause destruction, but there is no alternative to him. Therefore, there is no reason to fear him. He is always present in our world. He does not interfere in our affairs; he is always in control. He is also the spirit of truth and of peace.
>     
> TzHaar, the last echo of the void in the universe, is the spirit of chaos. This is the spirit that holds the universe in place by bringing about the destruction of everything. He is constantly in conflict with the forces of good and evil. He is the spirit that holds the void in its current state.

This ticker tape is unique: I wrote the allcaps section header, and "Yog-Sothoth". Then, I built the rest of the segment out of GPT-2 suggestions. Entirely. After that, I wrote another section header, and got this - with the exception of Xexanoth, which I ended up writing parts of, because I wasn't really thinking in terms of ticker-tape, yet, at the point that I did this - out:

>SECONDARY OUTER GODS: THE FIRSTBORN, KIN OF THE REAL
>     
> Kathrena, the world of the dead, is a shadow of life. She is the life of every being on this earth. There is nothing that she has not seen, felt and experienced. She knows her own place and time. She has not been born yet but is the only one who will determine what is to be or is not, among the lesser races.
>     
> Shub-Niggurath, the black goat with a thousand young, is the great mother, nurturer and protector of the world. She has the ability to create the material forms of every species. Her name derives from her ability to make herself into a material being. She gives birth to the first human, the first bird, and the first animal. She is also the embodiment of love. She is the love of her world, for the sake of her people she creates the heavens and earth in her own image.
>     
> Koth, the demon who holds the dead and the spirits, is the protector and guide of the world. He brings about the final creation that will be the final death of the entire cosmos. He is the greatest being of all time, a being who is immortal in all eternity and who is bound to the physical world in order to keep it from being destroyed until the promised time. In ancient legends, he is said to dwell in the heavens.
>     
> Xexanoth, whose lies hold the world in thrall, is the guardian of the future and the keeper of everything. She watches over all things, even those that don't need her. She creates the new world and takes away the old. Azathoth provides the fuel, and her deception causes the sky to burn. All the warmth of the world flows from her mouth, and when she dies, the world shall be filled only with the ashes and dust that have already been created.

Then, I gave the thing another section header. The following was written entirely by GPT-2, with the exception of that header, and the phrase "given sanction to speak".

> THE LESSER GODS: THE SECONDBORN, KIN OF THE COSMOS
>     
> Agnus Dei, the God of Heaven, is the most sacred and powerful god of the ancient gods. He is the one with the most important and powerful presence in the pantheon of gods and has the power to transform all of creation, making it beautiful and pure, so that it would serve him.
>     
> Sheb, the God of the Dead, is the keeper of the dead and a god of the earth. She takes the form of a beautiful dead thing and guides the dead to their new bodies so that they may be united with their creator.
>     
> Ereshkigal, the God of Life, is the God of Creation, the Creator of all that is not governed by the other deities. She provides us with all of the vital energy needed to survive and grow.
>     
> Atom, the God of the Cosmos, is the Mother Goddess of Creation. She is the first daughter of Shub-Niggurath. She holds a special place in the pantheon, and was given sanction to speak the Word of Creation by the Outer Gods, who alone existed in the universe before creation.
>     
> Satan, the God of Evil, was created as an evil manifestation of the Goddess Ereshkigal and was created for the purpose of torturing and tormenting humankind. He will continue to be a source of great pain for the righteous until the end of time.
>     
> Yavanna, the God of Earth, is the Goddess of the Land and works with the gods to keep everything in order. She is represented by a mountain that is believed to contain the souls of the departed. Her name means "to be good."
>     
> Yahweh, the Burning God, is the God of Genoah, the Garden of Eden. He is depicted as a fiery man in a white suit, sitting on a burning log in the heavens. He is a fierce deity who protects the faithful.
>     
> Elo, the Eternal One, is the God of Law, the final arbiter of all disputes. He is depicted as an older man with a thick beard, seated on a stone, leaning against it with his head turned towards heaven. He holds the key that binds order.
>     
> Yehweh, the God of the Great Basin, has a great number of different titles, each one of which has its own meaning. The first title is the "great name." This is the name given to the God when he comes to Earth and talks to people in the future. This name is "Kernekah," which means "the King of the Kings" and is used by the people of Eden when speaking with him. 

This is really where GPT-2 - at least, the medium size model - shines for creating worldbuilding leads. Because while there are plenty of combinatoric thing generators - persons, artwork (dorf fortress), powersets, etc -  out there, they generally can't produce output as varied in *form* as what GPT-2 is shown to produce right here. It's never *impossible* for them to, of course, but when they do, it's *always* highly specific, and requires a *lot* of work on the part of the person putting them together. I've made my own simple thing generator ([this](https://namegens.wuxiaworld.com/issthdao/)), and it's not wholly trivial to get something with high quality, even when you're working on something as simple as I was.

While much more computationally expensive than classical thing generators, anyone, regardless of knowledge or programming experience, can create ticker tape for GPT-2 that sets it up as a thing generator so long as they understand english spelling and grammar. Which is fantastically useful if the generator you want doesn't exist. There is, however, one sort of thing that GPT-2 definitely can't do. You can see it failing to do it right in the example above.

GPT-2 does *not* come up with original proper names. I've tried to create namegen ticker-tape; it doesn't work. GPT-2 is perfectly happy to give you a list of names, a list of male names, a list of female names, a list of english surnames, a list of japanese placenames - all of that will work, but it cannot generate new names. Even "Yehweh" in the list is a real - though obscure - variant of Yahweh.


------


**EDIT: Also, just want to add that huggingface defaults to the small model, but this entire post and all of its examples were generated with the medium model. There's a semi-hidden settings panel; only visible if the aspect ratio of your browser is landscape, not portrait, where you can change to medium if small isn't working for your needs.**

### Comments:

- u/Iwasahipsterbefore:
  ```
  >Sonic boom, no I don't like that one.

  Lol
  ```

  - u/Toastybob42:
    ```
    Nothing personnel.
    ```

- u/traverseda:
  ```
  Time to boot up warehouse 23 I suppose.

  http://basement.warehouse23.com/box/index.html
  ```

- u/SimoneNonvelodico:
  ```
  At least if *this* AI ever gets out of control we know its weak point. It fears sonic booms.
  ```

---

