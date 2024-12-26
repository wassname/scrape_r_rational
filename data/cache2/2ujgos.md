## If I Just Proved That P = NP, How Do I Start Taking Over the World?

* Author: u/itisike  *Dragon Army**
* URL: https://www.quora.com/If-I-just-proved-that-P-NP-how-do-I-start-taking-over-the-world
* Score: 14

* Created: 2015-02-02T18:18:21

### Post:

[Link to content](https://www.quora.com/If-I-just-proved-that-P-NP-how-do-I-start-taking-over-the-world)

### Comments:

> **u/None** [+12]  (2 hours later)
> 
> You aren't really guaranteed anything practically useful just from P=NP. Suppose you find an algorithm to (efficiently) transform any NP-Complete problem into a problem that can be solved with time complexity O(n^(3|||3)), but which cannot be optimized further. That algorithm is squarely in P, and you have just proved P=NP. But good luck actually getting anything done with that.

> **u/None** [+8]  (33 minutes later)
> 
> This assumes you won't get easily caught by tracing the transactions or that you'll instantly know how to use the proof to make an algorithm to solve all those problems. Proving P=NP publicly would probably make you insanely famous from the start anyway.

>> **u/itisike** [+3]  *Dragon Army* (37 minutes later)
>> 
>> If you're smart enough to prove it, you probably have enough knowledge to make the algorithm. And obviously you don't prove it publically.

>>> **u/CthulhuIsTheBestGod** [+9]  (2 hours later)
>>> 
>>> Not necessarily, it could be a non-constructive proof, and the actual algorithm might not even be suggested by the proof.

>>>> **u/itisike** [+1]  *Dragon Army* (2 hours later)
>>>> 
>>>> As an aside, do you know that there are algorithms that take P time on NP complete problems iff P=NP? The wikipedia page on the P versus NP problem has one.

> **u/Qwertzcrystal** [+5]  *assume a clever flair* (2 hours later)
> 
> Nice try.
> 
> Well, I guess you could keep quiet and develop efficient algorithms for many problems used in cryptography, finance/trading, logistics and simulation research, if you are actually able to derive these from your proof. Then patent them all, sell on a provisional basis by their profitability and somehow use all the money to take over the world. And hire some bodyguards.

>> **u/MoralRelativity** [+2]  (2 hours later)
>> 
>> And some very good lawyers.

>> **u/derefr** [+2]  (a day later)
>> 
>> I choose to believe this would be Lex Luthor's path in a rationalist!Superman story.

> **u/TimTravel** [+3]  (2 days later)
> 
> There are probably some brokenly powerful AI things you can do, to give the universal answer this sub usually gives.

> **u/Sparkwitch** [+1]  (23 hours later)
> 
> First of all collect your millennium prize money. Next, implement whichever world conquering you had before you proved P = NP. The world just got a little less strange, but nothing much has changed yet.

>> **u/itisike** [+2]  *Dragon Army* (23 hours later)
>> 
>> So throw away your biggest chance at world takeover. Sorry, not happening.

>>> **u/xamueljones** [+2]  *My arch-enemy is entropy* (a day later)
>>> 
>>> Most stories I read where someone successfully takes over the world *always* involves some chaotic event occurring at the same time to give our protagonist precious opportunities.
>>> 
>>> It might not be the most rational plan, but you can release a nonconstructive version of the proof and target companies with a poor understanding of the time complexities involved who are demanding an expensive change in their cryptographic systems. They'll be the easiest to attack and steal from.
>>> 
>>> In addition, you'll be a high profile celebrity on the same level as Einstein and now have the sufficient status to talk to the richest and most powerful people in the world who you *might* be able to convince to work for you. Be careful of wounding their pride though.

>>>> **u/itisike** [+2]  *Dragon Army* (a day later)
>>>> 
>>>> I don't think the celebrity status matters unless you're going to do it legally. You can get just as much cred by hacking Google (which is trivial after ssl is cracked).
>>>> 
>>>> And I think even a non-constructive version should not be released. Most companies would immediately switch to using codes that you can't break, and the knowledge that it must be possible would make finding it a lot easier. You wouldn't be able to use it for long. Even a zero-knowledge proof would be a bad idea.

>>>>> **u/khafra** [+1]  (2 days later)
>>>>> 
>>>>> > And I think even a non-constructive version should not be released. Most companies would immediately switch to using codes that you can't break
>>>>> 
>>>>> I think you're thinking of an efficient factorization algorithm, such as would be provided by a quantum computer that could handle a useful number of qubits. Cryptographers like Daniel J. Bernstein have been working on post-quantum cryptography for years.
>>>>> 
>>>>> But factorization is not NP-hard. A polynomial time (with a reasonably low constant factor) algorithm for solving NP-hard problems would break all *possible* crypto with keys smaller than the message, not just existing crypto. 
>>>>> 
>>>>> Things would break in opposite directions: The expense of painstakingly finding heuristics for optimization problems in fields like logistics, IC design, and protein folding would be gone.  However, needing physically isolated equipment for electronic transactions would make large-scale cooperation much more difficult. 
>>>>> 
>>>>> You might end up with something like large numbers of small guilds, in a relatively high-tech society with even more income disparity than today's.  Or whatever else, there's too many butterflies for me to really predict.

>>>>>> **u/itisike** [+2]  *Dragon Army* (2 days later)
>>>>>> 
>>>>>> First of all, factorization is not *known* to be NP-hard. Second, companies could use shared random quantum generators.
>>>>>> 
>>>>>> Also, NP-hard includes things that aren't in NP. Look up the definition again; a P=NP solution only helps for things in PSPACE=P.

>>>>>>> **u/khafra** [+1]  (2 days later)
>>>>>>> 
>>>>>>> > Second, companies could use shared random quantum generators.
>>>>>>> 
>>>>>>> Right, which would enable a small number of B2B transactions amongst dedicated partners; the guildlike structure I suggested. Or is Amazon really going to purchase and maintain a separate pair of quantumboxes for each of its quarter-billion customers?
>>>>>>> 
>>>>>>> >  factorization is not known to be NP-hard...a P=NP solution only helps for things in PSPACE=P.
>>>>>>> 
>>>>>>> You know complexity classes better than I do, which I hadn't realized when I wrote my comment; and I should have used "NP complete" in place of "NP hard." However, factorization certainly does seem to be in BQP, and stuff like knapsack, traveling salesman, etc. certainly don't seem to be in BQP. So, while it's not *proven*, I believe it's overwhelmingly likely that the examples I gave are good.

>>>>>>>> **u/itisike** [+2]  *Dragon Army* (3 days later)
>>>>>>>> 
>>>>>>>> If P=NP, then factorization is like any other NP problem, and it would also be NP-complete. We're talking about a counterfactual on what most people don't think is true (P=NP).
>>>>>>>> 
>>>>>>>> And a quantum box could be a standard install with every computer, and have some system like WOT to make it secure in a decentralized manner. I really don't know how feasible this is, but I don't know that it's impossible. I'm just not so sure that all possible cryptos would be broken in a post=NP world.

>>>>>>>>> **u/khafra** [+1]  (3 days later)
>>>>>>>>> 
>>>>>>>>> > If P=NP, then factorization is like any other NP problem, and it would also be NP-complete.
>>>>>>>>> 
>>>>>>>>> It does sense that that's part of the polynomial heirarchy that would collapse.
>>>>>>>>> 
>>>>>>>>> > And a quantum box could be a standard install with every computer, and have some system like WOT to make it secure in a decentralized manner.
>>>>>>>>> 
>>>>>>>>> Public key can't be done using quantum crypto; asymmetric crypto as we know it--whether it's based on algebraic rings, or elliptic curves, or lattices, or whatever else--isn't something that can "ride on top of" symmetric crypto. You'd need an Amazon Qbox, a Paypal Qbox, a $your\_bank Qbox, etc.; and each of those institutions would need to maintain a gazillion qboxes. So there's no WOT.

>>>>>>>>>> **u/itisike** [+1]  *Dragon Army* (3 days later)
>>>>>>>>>> 
>>>>>>>>>> If I have an Amazon box, and Amazon has a Paypal box, then I can get Amazon to "sign" that I'm really connected to Paypal. That's what I meant by WOT. You only need a chain of people you trust, and the more chains, the stronger the trust. I'm sure people have thought about this in more depth, but I don't know too much about it.

>>>>>>>>>>> **u/khafra** [+2]  (3 days later)
>>>>>>>>>>> 
>>>>>>>>>>> > If I have an Amazon box, and Amazon has a Paypal box, then I can get Amazon to "sign" that I'm really connected to Paypal. That's what I meant by WOT.
>>>>>>>>>>> 
>>>>>>>>>>> This is, indeed, a broad overview of the way a WOT works.  The hidden complexity under the words "sign" and "I," though, is what requires asymmetric crypto.  
>>>>>>>>>>> 
>>>>>>>>>>> For Alice to endorse Bob's identity, Bob has to *have* a public identity--some way to say "I am Bob" in such a way that Mallory cannot also say "I am Bob."  The only way I know of to do that is with a [trapdoor function](http://en.wikipedia.org/wiki/Trapdoor_function). P=NP implies that true trapdoor functions do not exist.

>>>>>>>>>>>> **u/itisike** [+2]  *Dragon Army* (3 days later)
>>>>>>>>>>>> 
>>>>>>>>>>>> If Alice and Bob share a box, then Bob can prove to Alice who he is, and Bob and consumer should be able to generate a random single-use pad through Alice. The problem with this is that Alice has access to the message, while now (before P=NP is proven) she only has access to perform an MITM (and even that can only be done once if Bob's key is stored). This is basically what http://blog.computationalcomplexity.org/2010/08/cryptography-if-p-np.html says, which is sufficient to show your point here is wrong.
>>>>>>>>>>>> 
>>>>>>>>>>>> However, that problem I mentioned? Something along the lines of Bob and consumer each generating their own random pad, which Alice shares. Then they can securely communicate with each other through Alice (by sending all messages to Alice), and they *might* be able to use that to generate a random pad which Alice doesn't share. I'm still thinking on that one. May be totally off.

>>>>>>>>>>>>> **u/khafra** [+1]  (3 days later)
>>>>>>>>>>>>> 
>>>>>>>>>>>>> I might be biased, but I wouldn't say I'm "wrong," exactly--a WOT is different from "unrestricted access to read and generate messages on behalf of whomever's identity you authenticate." All the tricks for generating a shared random pad not discoverable by the intermediary depend on P!=NP. 
>>>>>>>>>>>>> 
>>>>>>>>>>>>> In a pragmatic sense, though, it's true that Bob and Amazon depending only on the good will and incorruptedness of Alice is a step up from no security at all, and from geometrically increasing hardware requirements.

>>>>>>>>>>>>>> **u/itisike** [+2]  *Dragon Army* (3 days later)
>>>>>>>>>>>>>> 
>>>>>>>>>>>>>> > For Alice to endorse Bob's identity, Bob has to have a public identity--some way to say "I am Bob" in such a way that Mallory cannot also say "I am Bob." The only way I know of to do that is with a trapdoor function . P=NP implies that true trapdoor functions do not exist.
>>>>>>>>>>>>>> 
>>>>>>>>>>>>>> My point here was that the middleman can auth both users.
>>>>>>>>>>>>>> 
>>>>>>>>>>>>>> Anyway, I did some more research on my proposal above, and apparently it's [not possible with only one middleman to communicate without the middleman having access](https://crypto.stackexchange.com/questions/22783/can-you-exchange-a-shared-key-without-any-hardness-assumptions).
>>>>>>>>>>>>>> 
>>>>>>>>>>>>>> However, you *can* do it with multiple middlemen, which could be different CAs. In our world, we already trust CAs not to mitm us. In my model, you could share an otp with someone you don't already have one with, by using middlemen who you do share otps with, and only someone with access to *all* of the middlemens' otps can read your message.
>>>>>>>>>>>>>> 
>>>>>>>>>>>>>> See [this comment of mine](https://crypto.stackexchange.com/questions/22783/can-you-exchange-a-shared-key-without-any-hardness-assumptions#comment52841_22783).
>>>>>>>>>>>>>> 
>>>>>>>>>>>>>> That seems like a plausible way to communicate after P=NP.
>>>>>>>>>>>>>> 
>>>>>>>>>>>>>> Also, there's no need to use quantum; you just have random data shared from each CA. Quantum added security would only be if you set up new channels, but we want to work with legacy internet.

>>>>>>> **u/Uncaffeinated** [+1]  (16 days later)
>>>>>>> 
>>>>>>> In fact, P=NP implies that factorization is NP-hard.

---

