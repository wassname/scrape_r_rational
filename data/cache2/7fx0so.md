## [RT][WIP] Worth the Candle, ch 62 (Drift)

* Author: u/cthulhuraejepsen  *Fruit flies like a banana**
* URL: http://archiveofourown.org/works/11478249/chapters/29330487
* Score: 105

* Created: 2017-11-27T17:59:34

### Post:

[Link to content](http://archiveofourown.org/works/11478249/chapters/29330487)

### Comments:

> **u/narfanator** [+36]  (4 hours later)
> 
> Wow. [Null pointer exception], if it's not simply a joke, is the first exposed vulnerability in the game layer. With time and experimentation, could be a way to escalate user privileges from there.

>> **u/GeeJo** [+26]  *Custom Flair* (5 hours later)
>> 
>> I'd say the intelligence overflow from MEN-upping probably counts as  exposure, too, in that it laid bare the upper meta-level for a moment. Even if the failure was handled gracefully by the system.

>> **u/MultipartiteMind** [+10]  (14 hours later)
>> 
>> My thoughts indeed!  Whether it's how the System handles demons or beings without souls, it looks like a big glaring blindspot--
>> 
>> --Actually, scratch that.  That was my first thought, and would be really exciting (as well as scary) if so, but I'm replacing it with my new first hypothesis that the System is identifying her fine, but *she doesn't have a name*.  In that case, with the System just not having a name to put in that position, it should be replaced by a name as soon as someone (the protagonist?) gives it to her (and it's accepted).  Not being able to display her name because she doesn't have a name is unfortunately less exciting than not being able to display her name because she doesn't have a soul (or because she's a possessing demon).
>> 
>> Edit:  When checking about whether any name was mentioned, I was reminded that Amaryllis is not going to be happy about him choosing to save her, perhaps mollifiable by the Companion status revelation.

>>> **u/Quetzhal** [+13]  (22 hours later)
>>> 
>>> I don't know about that. There's a few ways you could potentially get a null pointer, at least in C:
>>> 
>>> 1) You left your pointer uninitialized, in which case it could be a null pointer or any other random number. You might get a null pointer, but you might also get some random person on the other side of the continent.
>>> 
>>> 2) You tried to allocate memory to store the name, and the memory allocation failed. This is kind of a really weird possibility, because if you're at the point where you can't store a simple string of bytes, there should be a lot of other problems with the simulation.
>>> 
>>> 3) You actually set your pointer as a null pointer. 
>>> 
>>> I actually think 3) is most likely in his instance. If souls themselves are pointers, then the lack of one is arguably a null pointer. The system tried to access the 'soul' pointer and retrieved 0, then tripped the null pointer exception.

>> **u/entropizer** [+8]  (5 hours later)
>> 
>> Sounds like begging for rollback. You'd need to move very fast in taking control.

>> **u/serge_cell** [+1]  (a day later)
>> 
>> Why would System even use pointers? One explanation (assuming it is not a joke) is that System is some far-future human originated system wich built on top of megatons of legacy code. But that's is not how tech developing in our timeline.

> **u/wnoise** [+25]  (14 hours later)
> 
> Has anyone mentioned that "Fallatehr" is an anagram for "All Father"?

>> **u/eternal-potato** [+21]  *he who vegetates* (a day later)
>> 
>> Also for "Earth Fall", "Alert Half" and "A Fart Hell".

>>> **u/jaghataikhan** [+5]  *Primarch of the White Scars* (2 days later)
>>> 
>>> >9000 hells - last anagram is all but confirmed to be plot relevant :D

>>> **u/Tetrikitty** [+3]  (2 days later)
>>> 
>>> TINACBNIEAC.

> **u/SvalbardCaretaker** [+29]  *Mouse Army* (6 hours later)
> 
> >“She’s innocent,” I said.
> >“Shit,” Fenn swore. “She’s fucking Joon-bait.”
> 
> Muahahaha

> **u/None** [+15]  (2 hours later)
> 
> [deleted]

>> **u/Kerbal_NASA** [+8]  (16 hours later)
>> 
>> She was mentioned as one of the non-elf people they met in the gymnasium full of Fallatehr's "associates". I don't think there's any other reference to her.

>> **u/rafaelhr** [+4]  (5 hours later)
>> 
>> I would also like to know that.

> **u/kraryal** [+30]  (an hour later)
> 
> I loved the null pointer exception

>> **u/FudgeOff** [+33]  (2 hours later)
>> 
>> There's a possibility that by increasing his loyalty level with the nonanima Juniper will raise his loyalty level with every other entity that lacks a soul/is a null pointer. Which may or may not be powerful and useful.  
>> 
>> Also, this means that souls act as pointers for the computer system that runs reality, which is very interesting and makes soul magic sound really powerful. I'm beginning to think that soul magic will end up just being computer programming.

>>> **u/narfanator** [+19]  (4 hours later)
>>> 
>>> > raise his loyalty level with every other entity that lacks a soul/is a null pointer
>>> 
>>> Unlikely. It's not the value of the pointer that matters*, it's the values at the address to which they point. So it could matter what's at the null memory address, or near it, in the case of pointer arithmetic; this is (AFAIK) part of how common security attacks can work.
>>> 
>>> * Outside of pointer arithmetic, etc.
>>> 
>>> If we're presuming that this is an actual error in the game layer, and not a joke/reference, then this would imply that loyalty is NOT a property of whatever object type the pointer is for; but that where the companion title/name comes from *is*. Which is interesting. It also implies that the game layer will catch exceptions and handle them gracefully, instead of crashing. Also interesting.

>>>> **u/ajuc** [+2]  (3 days later)
>>>> 
>>>> The fact that accessing null causes NPE means that it's probably a managed memory language, and pointer arthimethic is right out.

>>> **u/kraryal** [+6]  (3 hours later)
>>> 
>>> Do golems have souls? Now I have a funny mental image of all the free golems following him around

>>> **u/Noumero** [+3]  *Self-Appointed Court Statistician* (3 hours later)
>>> 
>>> > I'm beginning to think that soul magic will end up just being computer programming.
>>> 
>>> Well, [I'll take that compromise option](https://www.reddit.com/r/rational/comments/72iul3/rtwip_worth_the_candle_chapter_40_in_which_the/dnj3brm/?context=3).

>>> **u/derefr** [+1]  (3 days later)
>>> 
>>> My bet is simply that the "world" of the stimulation is one data structure (a matrix? heh) in the simulating computer system's simulator-process's address space; while souls are simply other data-structures in the same process's address space. By itself, that gives you no more ability to program the simulation than the existence of BLOB-typed records gives you the ability to program a RDBMS.

>>> **u/ajuc** [+1]  (3 days later)
>>> 
>>> My mental model of the WTC world is now javascript, where soul is prototype and body is properties of objects.

> **u/valeskas** [+11]  (an hour later)
> 
> Interesting. Maybe you can temporary stuff any soul into nonanima, so she would be immediately useful.

>> **u/sharikak54** [+21]  (4 hours later)
>> 
>> I was wondering if they could stuff Solace in her, maybe for healing or druid-specific knowledge.

>> **u/Makin-** [+4]  *homestuck ratfic, you can do it* (2 hours later)
>> 
>> I think that would be counterproductive and just "kill" the nonanima, replacing her with someone else. Getting her original soul would help her, but not sure beyond that.

>>> **u/Izeinwinter** [+15]  (5 hours later)
>>> 
>>> That is the sort of thing where one should ask the handy expert, not wonder.

> **u/Izeinwinter** [+11]  (19 hours later)
> 
> Theory: Based on the conversation before he turned the elves into fighting machines, I am making a guess that the method Fallatehr is using to control the shaped is that he has rendered their souls unstable - without a soul mage to maintain them, they will decay and eventually turn soul-less. The non-anima is the result of those experiments, and also a reminder what happens to you if you cross him, which is why he kept it around. 
> 
> ... Which in turn implies the non-anima was the sort of person who would rather go into oblivion than obey Fallatehr. Yhea, if I am right, definitely companion material, tough reconstructing a soul is a tall ask. 
> 
> Other things soul-magic is very likely to be useful for. Fallatehr edited fear out of himself. The fact that this is possible implies that self-directed soul magic can render Joon zen about the whole leveling process - That is, just straight up carve it out of himself as a value, making his attitude one of "it happens, it happens". That is very good news, because Experience-point addict Joon is not a story line I want to see.

> **u/TempAccountIgnorePls** [+9]  (2 hours later)
> 
> So the system can glitch. This is good news on the "avoiding the narrative" front.

> **u/dalitt** [+6]  (5 hours later)
> 
> I wonder why the chapter title is "Drift"?  Value drift, maybe?

>> **u/None** [+3]  (6 hours later)
>> 
>> Drift from the paths predicted by the game layer?

> **u/cthulhuraejepsen** [+4]  *Fruit flies like a banana* (7 minutes later)
> 
> Typos here, please.

>> **u/HomotoWat** [+3]  (47 minutes later)
>> 
>> > her scarlet-colored eyed 
>> 
>> should be "her scarlet-colored eyes"

>>> **u/kraryal** [+9]  (an hour later)
>>> 
>>> Since scarlet is in fact only a colour, should it not just be "her scarlet eyes"? I wouldn't expect to see someone write "her blue-coloured eyes" either.

>>> **u/cthulhuraejepsen** [+3]  *Fruit flies like a banana* (7 hours later)
>>> 
>>> Fixed, thank you. (Also, removed "colored", as it's cleaner that way.)

>> **u/Kerbal_NASA** [+3]  (8 hours later)
>> 
>> >I will remain imprisoned with a fewer resources
>> 
>> with a fewer -> with fewer
>> 
>> >It was twenty feet to the ground when were I was
>> 
>> when -> from
>> 
>> edit: Thought I'd mention that the first seven foot tall woman reference:
>> >We kept moving as they talked, with the conversation carried out over the rustling of clothes and the echoing sound of our footfalls. Each step of the seven-foot-tall woman was almost thunderously loud, and she was breathing heavily, putting by far the most effort into moving quickly.
>> 
>> confused me a bit and I saw [elsewhere in the thread](https://www.reddit.com/r/rational/comments/7fx0so/rtwip_worth_the_candle_ch_62_drift/dqf6liq/) other people were confused to. You did mention her at the beginning of the last chapter in the sentence:
>> >Most of them were elves, but there were other races too, an insectoid with a multi-hued carapace that had been scored with lines, a man with bumpy grey skin I recognized as one of the vlere-gur, and a woman who stood nearly seven feet tall and didn’t belong to any race I could recall making or reading about.
>> 
>> Maybe if I was reading it all at once it'd feel more natural, but I think it might have been a little too off-hand a mention to stick.

>> **u/GeeJo** [+1]  *Custom Flair* (5 hours later)
>> 
>> > Rolling was none to fun in armor
>> 
>> None too fun

>>> **u/cthulhuraejepsen** [+1]  *Fruit flies like a banana* (7 hours later)
>>> 
>>> Fixed, thanks!

>> **u/SvalbardCaretaker** [+1]  *Mouse Army* (6 hours later)
>> 
>> >trying my best to have my stomach churned by what I was doing.
>> 
>> NOT having it churned

>>> **u/cthulhuraejepsen** [+1]  *Fruit flies like a banana* (7 hours later)
>>> 
>>> Fixed, thank you.

>>> **u/SvalbardCaretaker** [+0]  *Mouse Army* (6 hours later)
>>> 
>>> >It was spectacular, under the light of Celestar and the multicolored stars.
>>> 
>>> Remove the comma

>>>> **u/cthulhuraejepsen** [+2]  *Fruit flies like a banana* (7 hours later)
>>>> 
>>>> Fixed, grudgingly, because it's one of those cases where I like a comma splice; I think the people that are averse to "commas as pauses" are *really* averse to commas as pauses, so I try to eliminate them when I realize I've used one for effect (though not always).

>>>>> **u/SvalbardCaretaker** [+4]  *Mouse Army* (15 hours later)
>>>>> 
>>>>> I am a native german speaker, we put them EVERYWHERE. Do what you want ;-)

>> **u/nytelios** [+1]  (2 days later)
>> 
>> 60
>> 
>> turned back to face the ~~gorllia~~-golem
>> 
>> that was why we ~~has~~ a lot of bones ready to go
>> 
>> 61
>> 
>> then healed myself immediately without ~~only~~ a trace of the cut remaining
>> 
>> 62
>> 
>> I will remain imprisoned with ~~a~~ fewer resources

>>> **u/cthulhuraejepsen** [+1]  *Fruit flies like a banana* (5 days later)
>>> 
>>> Fixed all those, thanks!

> **u/TheGuardianOne** [+1]  (2 days later)
> 
> > “They’re prone to demonic possession; without a soul, it’s easy to enter the body. She won’t have any magic that ties to the soul, which means most of them.”
> 
> > “We’re talking about demonic possession here?” I’d asked.
> 
> This confused me a bit. Was Mary originally saying "she's prone to possession", and that had been changed during the editing process? Or is Juniper asking something akin to "She can be possessed by a demon here and now?"

>> **u/nytelios** [+2]  (5 days later)
>> 
>> I thought Joon was asking a rhetorical question. Like: "for real? demonic possession?"

>>> **u/cthulhuraejepsen** [+1]  *Fruit flies like a banana* (5 days later)
>>> 
>>> I will affirm that as the intended reading, but it could probably be cleared up and reworded a bit.

---

