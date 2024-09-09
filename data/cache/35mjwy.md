## GEB Discussion #15 - Chapter 14: On Formally Undecidable Propositions of TNT and Related Systems

### Post:

**Gödel, Escher, Bach: An Eternal Golden Braid**

This is a discussion of the themes and questions concerning the **Chapter 14: On Formally Undecidable Propositions of TNT and Related Systems** and its dialogue, **Birthday Cantatatata...**.

**Proof of Gödel’s Theorem**

The first half of this chapter is rather difficult to read because Hofstadter is trying to give a through sketch of the proof behind Gödel’s Theorems by showing why TNT can’t prove its own consistency. To help explain things, I will try to give a high-level view of the proof and merely point out that Hofstadter’s proof wouldn’t be accepted as a mathematically rigorous proof. Gödel’s proof followed a similar pattern, but he had to construct a far more complex and confusing formal system. It makes the TNT-system look like the MIU-system.

The paper is called [On Formally Undecidable Propositions of Principia Mathematica and Related Systems](http://en.wikipedia.org/wiki/On_Formally_Undecidable_Propositions_of_Principia_Mathematica_and_Related_Systems), and here is a link to the [PDF of the paper](http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0CB4QFjAA&url=http%3A%2F%2Fwww.ursuletz.com%2Fcs150-fall2005%2Flectures%2Fgoedel.pdf&ei=gj9QVcmFO4jisATRsoCQDQ&usg=AFQjCNHWc__ytbAzXixGYVioipazPm42Mg&sig2=hliPNPrhJNtYkZ48NX_Frg&bvm=bv.92885102,d.cWc).

If you want to skip reviewing the proof, just scroll down to the line where “G is not a theorem of TNT” for the conclusion.

The proof demonstrates two key facts: certain TNT theorem-strings can be interpreted as talking about other theorem-strings in TNT, and there exists a theorem-string, G, which talks about itself (or more specifically its negation).

Hofstadter starts with the idea of proof-pairs such as (m, n) where m is the Gödel number of a TNT derivation which ends in a TNT string whose Gödel number is n. Basically m encodes the proof of the string encoded by n. Remember that it has already been shown that certain TNT strings can be written (in Gödel numbers) as the entire proof to derive another TNT string. Hofstadter shows a nice example as applied to the MIU-system.

To reiterate previous chapters:

* Given a formal system, change the rules to rules of arithmetic.
* Take a theorem and express a derivation of it in arithmetic which will be a very large number.
* Make a proof-pair out of the two numbers: The first number is from above and the second one is what we are trying to prove.


Since it is very easy to check if a derivation is valid (will m lead to n?), a given proof-pair can be checked by a BlooP program (guaranteed to finish in finite time) which means it’s primitive-recursive and implies everything we spent previous chapters learning about.

Unfortunately while we can check very easily if (m, n) makes a proof-pair, we can’t check in finite time if there is any possible m for a given n. It’s the problem of being given a string and knowing if it’s a theorem or non-theorem.

Hofstadter says that if a certain property is testable by a BlooP program, then as a primitive recursive, it can be represented in TNT by a formula which accepts two free variables. There is a string in TNT which can be interpreted as PROOF_PAIR(m, n) even if we don’t know it. Hofstadter elaborates by saying that this applies to **all** formal systems.

If the difference between the two ways to write about the proof of a theorem-string is confusing, think of it as:

Proof-pair = This is a proof of N.        vs        Theorem-string = N can be proven.

With the idea of a proof-pair worked out, we can now try checking if self-reference is possible, or PROOF_PAIR(x, x) where x is a derivation proof for itself. Hofstadter goes through a short section on substitution to show the steps for why the self-referencing proof-pair is possible. We have created a system of quines in TNT.

The final step is to construct G, “This TNT string is not a theorem of TNT”. Hofstadter uses arithmoquining to embed a given formula’s Gödel number in itself. Hence ARITHMOQUINE(m, n) means that n is the Gödel number of the string m when m embedded its Gödel number in itself.

Hofstadter then goes another level combining the two important formulas, PROOF-PAIR(m, n) with ARITHMOQUINE(l, n) where m is the derivation of n and l is the Gödel number of n after n embedded its Gödel number in itself. Hofstadter is trying to quine a string which is talking about quining.

So the given formula reads as: there doesn’t exist a variable m and there exists a variable n such that PROOF-PAIR(m, n) and ARITHMOQUINE(l, n). Let u be the Gödel number of this TNT-string and G be the TNT-string itself. (I’m using more variables than Hofstadter did to help clear things up.)

G is simply ARITHMOQUINE(G, g) where g is the Gödel number of the string G after u is embedded in G.

To sum up, 

Hofstadter notes how confusing this statement is and translates it into plain English very neatly as:

"There do not exist numbers m and n such that both they form a proof-pair and n is the arithmoquinification of u."

“There is no number m that forms a proof-pair with the arithmoquinification of u.”

“The formula, G, whose Gödel number, g, is the arithmoquinification of u is not a theorem of TNT.”

“G is not a theorem of TNT.” / “I am not a theorem of TNT.”

These [two](http://www.felderbooks.com/papers/godel.html) [guys](http://www.dailykos.com/story/2009/05/31/736946/-Godel-Escher-Bach-series-On-formally-undecidable-propositions-of-TNT-and-related-systems#) do a better job explaining than I ever could.

……

**G and Going Beyond G**

The consequences of this string is obvious, 

If G is a true TNT-theorem, then G is saying that it’s a false TNT-theorem which leads to contradiction!

If G is a false TNT-theorem, then G asserts its own truth about not belonging in TNT which is perfectly fine and doesn’t lead to a contradiction. Yay! But it means that there is a truth which ***cannot*** be derived from the axioms!

Therefore the TNT-system is incomplete; it cannot prove all possible truths.

About ~G, ………

G is “I am not a theorem of TNT”. Let’s look at ~G which is “I am a theorem of TNT”. Since G is a truth, ~G must be a false statement. But any possible derivation in TNT will be true and proclaims its own truth. Since no derivation can lead to a false statement, then just like G is an unprovable truth, ~G is an unprovable lie.

……

**Omega and Extending Axioms**

Remember that Hofstadter defined [w-incomplete](http://en.wikipedia.org/wiki/%CE%A9-consistent_theory) to mean that a system can’t state any generalizable theorems about all numbers, even when the theorem applies to all numbers.

Now if we tried extending the axioms of TNT with G we have higher order logics as G allows the TNT-system to make statements about itself to a greater degree than possible before.

However, adding ~G must also be a possibility because a system with an [independent statement](http://en.wikipedia.org/wiki/Independence_%28mathematical_logic%29) can always be extended with the statement or its negation. This results in the [supernatural numbers](http://en.wikipedia.org/wiki/Supernatural_numbers) which are rather difficult to understand or explain, but I did find an interesting [essay](http://www.hoge-essays.com/incompleteness.html) which seems to explain them in terms of infinity.

……

**Dialogue**

This seems like a very straight-forward dialogue where Tortoise continually ask Achilles the same question over and over. Tortoise is being repetitive due to a failure in not being sure that Achilles would answer the same way to his questions and not making any assumptions about any future answers. This is similar to the TNT-system which could only reason out theorems relating to each number, but fail to have any theorems generalize to all of the numbers at once. Fortunately, the addition of G is similar to Achilles replying with a meta-answer about all past and future questions. In a similar way, first-order logic has a similar problem until the addition of certain rules to allow for second-order logic.

Then Tortoise goes on to talk about omega (w) which stands for the set of all natural numbers or nonnegative integers which is the ‘smallest’ infinity, or the first level as it were. Further levels can be built up into 2w, 3w, 4w… and then w^2, w^3, w^4… and then w^w, w^(ww), w^(www)… which all invoke the idea of [Aleph Numbers](http://en.wikipedia.org/wiki/Aleph_number).


Wikia Links:

* [Chapter 14](http://godel-escher-bach.wikia.com/wiki/Chapter_14)

* [Birthday Cantatatata…](http://godel-escher-bach.wikia.com/wiki/Birthday_Cantatatata...)

Coming up next on May 14th is Chapter XV: Jumping out of the System.

The discussion for the previous chapter is posted [here](http://www.reddit.com/r/rational/comments/33o97k/geb_discussion_14_chapter_13_bloop_and_floop_and/).

The discussion for the next chapter is posted [here](http://www.reddit.com/r/rational/comments/364gsj/geb_discussion_16_chapter_15_jumping_out_of_the/).

[Official Schedule](http://www.reddit.com/r/rational/comments/2yys1i/lets_start_the_read_through/).

### Comments:

- u/None:
  ```
  I have not the slightest fucking idea why the post got removed, but it did.  Very sorry.
  ```

- u/avret:
  ```
  This comment is meant to test whether adding comments to this post will return it to the front page.  It contains no information relevant to GEB.
  ```

- u/markus1189:
  ```
  Glad you're back ;)

  I found the chapter rather difficult to read and it took me several tries until I think I got most of it.  Nevertheless the supernatural numbers were very interesting.

  The dialogue also was rather strange for me, maybe I'll need to read it again...
  ```

---

