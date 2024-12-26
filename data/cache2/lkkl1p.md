## "Basilisk Collection" - A Fictional Wikipedia Article About Cryptography

* Author: u/blacklemon67 *
* URL: https://suricrasia.online/unfiction/basilisk/
* Score: 70

* Created: 2021-02-15T19:08:29

### Post:

[Link to content](https://suricrasia.online/unfiction/basilisk/)

### Comments:

> **u/JohnKeel** [+23]  (2 hours later)
> 
> This is kinda neat as a fake Wikipedia article, but it doesn't really tell much of a story. Once you remove the purely factual background material on hash functions, there's only a few paragraphs that boil down to "either someone has a megaultrasupercomputer, or SHA-256 has been broken."
> 
> Also, speaking as a cryptographer: hash functions being broken is generally surprising, but not the sort of thing that shatters your view of the field. Hash functions in general are usually not based on hard computational assumptions in the way RSA depends on factoring.

>> **u/Auroch-** [+5]  *The Immortal Words* (23 hours later)
>> 
>> I think you're skipping over the interesting parts of the story. Someone found a vulnerability in SHA-256: sure, but that's just the setup. They announced this with a huge data dump of reversals for *double-*SHA-256, which were all of a particular string format with no explanation why. It was distributed via torrent and 75% went missing, and no one is sure why. The unknown method is mildly interesting; the unknown *motive* is fascinating.

>>> **u/JohnKeel** [+2]  (a day later)
>>> 
>>> My problem is that the motive has no evidence towards any particular solution. I think that the article is neat - but I wouldn't call it a story, because the only thing there is a mystery box.

>>>> **u/Auroch-** [+1]  *The Immortal Words* (a day later)
>>>> 
>>>> A mystery box is a specific thing and there is no indication this is that thing. The fact that there is no clear explanation does not make it a mystery box; a mystery box is when no clear explanation exists or even could exist. This is a story in the tradition of [Thiotimoline](https://en.wikipedia.org/wiki/Thiotimoline).

>> **u/Galap** [+2]  (a day later)
>> 
>> So, why are hash functions difficult to reverse if they aren't based on hard computational assumptions?

>>> **u/JohnKeel** [+6]  (a day later)
>>> 
>>> There are a bunch of heuristics used when creating hash functions, most of which boil down to “we’re pretty sure this defeats a known method of attacking hash functions.” In today’s commonly-used hashes (the ones that are practical to use), they’re also accepted as probably secure because a lot of skilled cryptanalysts have failed to show weaknesses, rather than because of formal proofs.

>>>> **u/PeridexisErrant** [+3]  *put aside fear for courage, and death for life* (5 days later)
>>>> 
>>>> > a lot of skilled cryptanalysts have failed to show weaknesses
>>>> 
>>>> Or have at any rate failed to publicise weaknesses, which we all pretend is basically the same thing.
>>>> 
>>>> (despite knowing that NSA et al both find *and introduce* weaknesses in common crypto...)

>> **u/None** [+1]  (a day later)
>> 
>> >Hash functions in general are usually not based on hard computational assumptions in the way RSA depends on factoring.
>> 
>> On the contrary. Hash function are entirely based on reversing them (pre-image) and colliding them being a hard problem. Even "breaking" them usually means moving some operation from "not in this universe" to "it can be computed using all the resources of the world".
>> 
>> If someone was able to generate long partial inversions easily on a modern hash function it would mean that the whole premise behind how those functions are designed is broken and the way how they're evaluated it broken. It would be a huge discovery.

>>> **u/blacklemon67** [+6]  (a day later)
>>> 
>>> Author here. A collection of partial hash inversions described in the story would only prove that doubled SHA-256 is broken, it wouldn't really say much about other hash functions. JohnKeel is right to say that hash functions aren't based on mathematically hard problems like RSA is, and there have been countless hash functions that have been broken from careful mathematical analysis. I won't to go into detail of why I wrote it this way; I want to preserve the "mystery box" of this situation.

>>>> **u/JohnKeel** [+1]  (a day later)
>>>> 
>>>> Oh, I hadn’t realized! I really appreciate that you actually went ahead and generated a few partial inversions- it’s a fun detail.

>>>>> **u/blacklemon67** [+1]  (a day later)
>>>>> 
>>>>> thanks! I had to write my own "miner" to find them so I could use the accelerated sha256 functions on my cpu

>>> **u/JohnKeel** [+6]  (a day later)
>>> 
>>> Preimage resistance is a security property that any particular hash function might (hopefully) have. The preimage resistance of SHA-256 does not have some mathematical assumption that it depends on such that we can prove SHA-256 is preimage resistant so long as a certain problem (factoring, discrete Diffie-Hellman, lattice operations are common) is hard to solve. 
>>> 
>>> This is in contrast to RSA. There are simple proofs that, so long as a large number is hard to factor, messages cannot be signed or decrypted without the corresponding private key (and in fact, if numbers are easy to factor, then also RSA is easy to break).
>>> 
>>> So, easy factoring suddenly means that all cryptosystems depending on hard factoring may have simple attacks; but a discovery that SHA-256 does not have preimage resistance does not formally translate to other hashes not having preimage resistance, except insofar as similar cryptanalysis may be applied.

> **u/GlimmervoidG** [+8]  (29 minutes later)
> 
> That was very good. There's a nice bit of humour at the very end too.
> 
> >Cryptography experts[who?] have proposed that Bitcoin creator Satoshi Nakamoto is the creator of basilisk.txt.[50][dubious – discuss]

> **u/basiliskgf** [+6]  (4 hours later)
> 
> I love this sort of fake website worldbuilding - not to mention the juxtaposition between cryptographic verification of the collection and its inexplicable, impossible origin.
> 
> rip to bitcoin tho

>> **u/fljared** [+2]  *United Federation of Planets* (a day later)
>> 
>> The resulting Bitcoin Next would appear to survive, although only time would tell if the damage from Basilisk would kill the trust and hype long-term.

> **u/serge_cell** [+5]  (12 hours later)
> 
> Mathematical cosmic horror.

> **u/everything-narrative** [+4]  *Coral, Abide with Rubicon!* (2 hours later)
> 
> This has a Mystery Flesh Pit National Park-like energy to it.

>> **u/fljared** [+2]  *United Federation of Planets* (a day later)
>> 
>> Yeah, or the better SCP articles-=. Not in being supernatural, but in telling a story without a clear answer, and only seeing the results on the outside. Very few articles that go that route do it well, but this one does.

> **u/Kimundi** [+2]  (7 days later)
> 
> Fascinating read! Also, I now learned about partial hash inversions :D

> **u/barnett9** [+1]  (5 hours later)
> 
> This is great!

> **u/Xadith** [+1]  (2 days later)
> 
> I enjoyed the other articles, too. Thanks for sharing.

---

