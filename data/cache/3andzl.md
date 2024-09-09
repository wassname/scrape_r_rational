## GEB Discussion #17 - Chapter 16: Self-Ref and Self-Rep

### Post:

**Gödel, Escher, Bach: An Eternal Golden Braid**

This is a discussion of the themes and questions concerning the **Chapter 16: Self-Ref and Self-Rep** and its dialogue, **The Magnificrab, Indeed**.

**Self-Reference and Self-Representation**

This is one of the longest chapter in the book as Hofstadter delves into the numerous forms self-reference and self-representation can take as well as showing how they can apply to our very own biology.

Hofstadter starts by talking about how easy self-reference is when using language, because language is about communication and once the idea of self-reference can be articulated, it is done.

Talking about self-reference *is* self-reference, especially with examples involving the phrase “this sentence”.

However, due to the ease we experience when using self-referential examples, it is not immediately obvious th machinery or the mental processing we are using to understand the sentence. It requires:

* The ability to understand which word is a reference or a non-reference. Is the word pointing to something else, or is it demonstrating/communicating a concrete idea.

* The ability to understand where the reference words are pointing to.

* The ability to handle the case when referential words point to itself.

Hofstadter illustrates with his figures how all three abilities above are combined to understand self-referential sentences. To be sure of understanding this concept, try writing your own self-referential sentences. Bonus points if you don’t explicitly refer to the sentence using the phrase “this sentence”.

Now that we understand self-reference, how about self-representation where a sentence represents itself perfectly? This is impossible (unless the sentence is infinite in length) because no sentence can quote itself in its entirety even though it can quote any other sentences. The quine, “Yields falsehood when preceded by its quotation” yields falsehood when preceded by its quotation, only works because it refers to representing a shorter sentence in the quotation marks and not the double copy of itself. It is only a method of self-reference which avoids the phrase “this sentence”. It seems as if self-representation is more about producing a copy of itself rather than being its own self-reference (which is a very confusing concept).

Hofstadter goes on to talk about how to create a quine through a [BlooP-like computer programs](https://en.wikipedia.org/wiki/Quine_%28computing%29). This should be fairly intuitive since quines is like the idea of following instructions to write out the instructions themselves or following the following phrase ‘To read this sentence out loud, you must read the following phrase out loud “To read this sentence out loud, you must read the following phrase out loud”’.

I apologize for any headaches one may encounter when dealing with quines.

Hofstadter finally wraps up this section with replicating sentences/ideas/systems. For anything to be capable of self-representation (where it produces a copy of itself), it must be able to refer to itself for ‘instructions’ on how to recreate itself.

Before continuing on, try to come up with example of replication where self-reference is used.

…

**Biology**

Hofstadter suggests that there may be *classes* of self-representation where a machine or program can produce other machines/programs which will in turn produce the original version. This can get very complicated as you could have multiple stages of productions happening.

Hence self-representation is used to illustrate how self-reference can occur in number theory with Gödelian numbers to represent numerical statements referring to itself and self-reference is used to illustrate how self-representation can occur in biology with DNA referring to itself to produce copies.

When we peer into biology, the most striking thing to notice is how much like a computer program our DNA acts. Its bases (A,C, G, T) are like bytes in a computer system as the raw data recording the information of the system at the lowest possible level. Specific combinations of bases can be interpreted as enzymes to function as the most basic commands on other biological data which allows more complex enzymes which are sequences of simpler enzymes and so onto ever more complex enzyme-commands.

As a result, DNA is very much like a computer program which functions based on inputted data and since the program is also made of data, the program can easily be given itself as a possible input. Hence DNA is its own program and input to create duplicate copies of itself.

The main differences between computers and biology seems to be the fact that humans are careful to kept hardware separate from software so that no matter what computers a program is run on, the program will act the same on every possible computer. However with biology, the software, the brain, are specialized for the hardware, the body. Which is why one can’t remove a human brain and place it into a wolf’s body and expect the brain to be capable of handling the differences between species. Frankenstein’s monster is also extremely difficult since brain transplants are still not possible even with modern medical technology.


After an extended explanation on our biology, Hofstadter compares it to TNT and shows how the Central Dogma of Molecular Biology has a very strong isomorphism to the Central Dogma of Mathematical Logic. For example, proteins are meta-statements of TNT, DNA are TNT strings, and many other similarities with the most important one of all being the isomorphism between self-representation in biology to self-reference in TNT. Looking at the figure drawn by Hofstadter, self-representation is so similar to self-reference in the roles the two play that they seem like two different facets of the same concept of meta-statements.

This brings us to the question of, what does the Gödel’s Incompleteness Theorem map onto?

Hofstadter uses the Contracrostipunctus to show the effect Gödel’s Theorem has on biology. One can easily imagine a cell as a record player taking in DNA strands as records to be played. Therefore just like how the Perfect Phonograph can play any record, the Perfect Cell is one that can interpret and read any possible DNA sequence. According to Gödel’s Incompleteness Theorem and the isomorphism between biology and TNT, there must be some sequence of bases which would result in destruction of the cell. One could immediately guess that certain genetic disorders, cancers, or viruses could be possible candidates for unreadable DNA, but this is pure speculation and has no actual research (known to me) to suggest this possibility.

Viruses add another level of complexity to how cells read DNA, because not only does the cell need to carry out its normal, complicated process of replication, it also needs to know when its read a ‘bad’ sequence of DNA or a virus. This expands into a larger problem of recognition since cells also use enzymes to communicate with each other and its like receiving multiple letters in the mail and recognizing who sent which letter. This apparently relates to [Henkin sentences in mathematical logic](https://en.wikipedia.org/wiki/Leon_Henkin).

Henkin wrote a proof similar to Gödel’s proof about how [first-order logic is complete](https://en.wikipedia.org/wiki/G%C3%B6del%27s_completeness_theorem) and consistent, except he only proved that such a [proof must exist](https://en.wikipedia.org/wiki/Existence_theorem). The main advantage of his approach is that his is easier to follow and is similar to viruses being like the statement, “I Can Be Reproduced in Cells of Type X”. They both don’t explain how to reach the result they detail, but rather that the result is certain to be possible.

Hofstadter mentions how the above Henkin sentences are implicit types while Henkin sentences which do state at least part of the way to reaching the mentioned end result are explicit. Just like how Henkin demonstrates that a virus must be able to invade certain cells, Gödel demonstrates that all cells have a virus of some type which is guaranteed to ruin it

There is a follow-up section on how the cells can have such fine control over high-level features such as instincts, temperament, and behavior which I will not be commenting because I would be doing you a very poor disservice to try explaining something I can’t do more than parrot.

When Hofstadter wonders at how Life could have ever got started at all, he doesn’t know that RNA was the first replicator of since it can act both as the enzyme (readers) and as the protein (output). It was the first [instance of *directed* replication](http://lesswrong.com/lw/w0/the_first_world_takeover/).

I apologize for anyone who wished for me to explain the biology section, but all I can clarify is that Hofstadter is laboriously illustrating how biology uses self-representation and self-reference to enable cellular reproduction. His explanation is a very concise and good illustration of how DNA works with RNA and proteins to encode genetic information and to extract the information as necessary. If you wish to learn more about this fascinating topic, I recommend either reading some biology books. I will post any recommendations commenters make here:

* 

Here is a very good webpage on [summarizing the chapter and dialogue](http://www.nada.kth.se/~kai/lectures/geb.html).

……

**Dialogue**

Achilles and Tortoise start the dialogue by discussing Crab’s intelligence and how he must be smarter than any other crab alive. To prove this point, Crab comes by with some mathematical results which someone sent him, thinking very highly of his intelligence as a mathematician. Najunamar sent Crab a letter proving several trivial results, or extremely simple version of the [Four-Color Theorem](https://en.wikipedia.org/wiki/Four_color_theorem), [Goldbach’s Conjecture](https://en.wikipedia.org/wiki/Goldbach%27s_conjecture), and [Fermat’s Last Theorem](https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem).

Note that when [1729](https://en.wikipedia.org/wiki/1729_%28number%29) is mentioned, it’s significant due to being the smallest number which is the sum of two cubed numbers in two different equations, 1^3 + 12^3 = 9^3 + 10^3.

Due to Najunamar’s extremely unusual phrasing of the mathematical results convince the trio that no one could possibly have the imagination to make the results up and his intelligence can’t be replicated by non-Oriental mathematicians. Achilles then mentions the [Church-Turing Thesis](https://en.wikipedia.org/wiki/Church%E2%80%93Turing_thesis) which relates to the equivalence of statements or ideas between multiple systems. This of course means that anything Najunamar can derive within his own designed system must also have an equivalent derivation in any other system of mathematics.

The statements, in order of appearance, translate into:

* No number is the successor of zero.

* 13 is prime.

* 3^2 + 4^2 = 5^2.

* 14 is prime. Crab suggests changing it to “17 is prime”, “19 is prime”, or “14 is not prime”.

* 17 is not prime.

* This is simply a string which is not well formed. A statement in number theory by John Cage.

* b^2 = 2a^2 only if a is 0.

* 50 is the smallest number that can be written as a sum of two squares in two different ways. Note how this is similar to 1729 from before.

* Every even integer greater than 2 can be expressed as the sum of two primes. Since this is Goldbach’s Conjecture, Crab cannot say one way or another if it sounds ‘beautiful’ or ‘ugly’.

Every statement which is true, Crab finds a pleasing harmony in, while false theorems sound ‘disharmonious’. Gibberish statements, or non-well-formed strings, amusingly sound like music by John Cage.

When Achilles says “You mean this is a big bluff?”, it seems to be implied that Crab and (maybe) Tortoise had be playing a joke on him.

Wikia Links:

* [Chapter 16](http://godel-escher-bach.wikia.com/wiki/Chapter_16)

* [The Magnificrab, Indeed](http://godel-escher-bach.wikia.com/wiki/The_Magnificrab,_Indeed)
	
Coming up next is Chapter XVII: Church, Turing, Tarski, and Others

The discussion for the previous chapter is posted [here](http://www.reddit.com/r/rational/comments/364gsj/geb_discussion_16_chapter_15_jumping_out_of_the/).

The discussion for the next chapter is posted here.

[Official Schedule](http://www.reddit.com/r/rational/comments/2yys1i/lets_start_the_read_through/).

### Comments:

---

