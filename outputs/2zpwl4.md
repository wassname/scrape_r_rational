## GEB Discussion #3 - Chapter #2: Meaning and Form in Mathematics

### Post:

**Gödel, Escher, Bach: An Eternal Golden Braid**

This is a discussion of the themes and questions concerning the **Chapter 2: Meaning and Form in Mathematics**, and its dialogue, **Sonata for Unaccompanied Achilles**.

**Formal Systems**

How is the pq- system isomorphic to addition? Can we say that all laws of addition are preserved?

* Law of Commutativity: a + b  =  b + a

* Law of Associativity: (a + b) + c  =  a + (b + c)

* Law of Distributivity: a × (b + c)  =  a × b  +  a × c

We notice immediately that Distributivity doesn't hold, because there is no multiplication operation in the pq- system. Why can't we extend the system like we do with the addition to multiplication. Why isn't this ability part of the isomorphism?

......

**Isomorphism**

Isomorphisms are only perceived when two systems seem to have the same *meaning*. Yet the meaning of the two systems don't appear subjective (or something wholly in our mind), but rather as if they reflect an inherent property of an underlying, deeper system containing the two simpler systems.

Is meaning subjective or objective (or some mixture of both)? 

How does this idea relate to the earlier chapters of 'Strange Loops' and intelligence's ability to 'jump' out of a system?

It appears to be part of our ability to understand the world as an abstract system when we use language and when we think abstractly. Remember, the map is not the territory!

If we think of an isomorphism from one system to a second system, and then think of another isomorphism from the second to a third system, would the first system be isomorphic to the third system? Wouldn't there be problems where details are lost in translation like when translating a passage from one language to a second and then to a third language? 

In mathematics, how does isomorphism relate to the [notion of a proof](http://projectwordsworth.com/the-paradox-of-the-proof/) especially when proofs are a social construct?

......

**Dialogue**

1) What was Tortoise doing that caused Achilles to twist his neck?

2) What was Tortoise's ingenious but degenerate solution to the HE puzzle?

3) What was Tortoise's second solution to the HE puzzle?

4) What is the solution to the ADAC puzzle?

5) What is the concept of 'figure and ground'? How does it appear in Escher's artwork and in the dialogue? Who is the 'figure' and who is the 'ground'? How can we relate the 'figure and ground' concept to the answer to both puzzles?

Wikia links:

* [Chapter 2](http://godel-escher-bach.wikia.com/wiki/Chapter_2)

* [Sonata for Unaccompanied Achilles](http://godel-escher-bach.wikia.com/wiki/Sonata_for_Unaccompanied_Achilles)

Coming up next on March 23th is Chapter III: Figure and Ground.

The discussion for the previous chapter is posted [here](http://www.reddit.com/r/rational/comments/2zhouc/geb_discussion_2_chapter_1_the_mupuzzle/).

The discussion for the next chapter is posted [here](http://www.reddit.com/r/rational/comments/30144c/geb_discussion_4_chapter_3_figure_and_ground/).

[Official Schedule](http://www.reddit.com/r/rational/comments/2yys1i/lets_start_the_read_through/).

P.S. Sorry if this post is a little rushed. I didn't have much time to think of more engaging explanations of the ideas in the chapter, and defaulted to using multiple questions to get your brains thinking.

### Comments:

- u/None:
  ```
  [deleted]
  ```

- u/mhd-hbd:
  ```
  The *pq* system is isomorphic to the additive Semigroup defined in Peano's original definition of Peano Arithmetic.

  If we were to include the distributive law, it would necessitate exhibiting a Ring isomorphism. Since the *pq* system is not a Ring, such a notion is absurd.

  Proof of isomorphism using informal Homotopy Type Theory to follow.

  It is so, because Peano's original definition is:

      Nat : Type
      1 : Nat
      S : Nat → Nat
      ind_Nat :
          (P : Nat → Type) →
          P 1 →
          ( (n : Nat) → P n → P (S n) ) →
          (n : Nat) → P n

      _+_ : Nat → Nat → Nat
      1 + n :≡ S n
      S n + m :≡ S (n + m)

  from which `unit_addition : (n : Nat) → 1 + n = S n` follows trivially.

  (With associativity, commutativity, and other properties of addition in this type-theoretic example, left as an exercise to the reader.)

  Going by the definition of *pq* in GEB:

      dash : Type
      - : dash
      ind_dash : (P : dash → Type) → P - → (d : dash) → P d

      string : Type → Type
      empty_string : (A : Type) → string A
      cons_string : (A : Type) → A → string A → string A 
      ind_string :
          (A : Type) →
          (P : string A → Type) →
          P (empty_string A) →
          ( (a : A) → (l : string A) → P l → P (cons_string a l) ) →
          ( (l : string A) → P l )


      _++_ : (A : Type) → string A → string A → string A
      empty_string ++ l :≡ l
      cons_string a l ++ k :≡ cons_string a (l ++ k)

      dashes : Type
      dashes :≡ string dash

      pq : Type
      _p_q_ :
          (x : dashes) → (y : dashes) → (z : dashes) →
          (x = empty_string dash → 0) →
          (y = empty_string dash → 0) →
          (z = x ++ y) →
          pq

  And then all we have to do is exhibit:

      iso : Nat ≅ (d : dashes) × (d = empty_string → 0)
      iso :≡ (Nat_to_dashes, dashes_to_Nat

      Nat_to_dashes : Nat → (d : dashes) × (d = empty_string → 0)
      Nat_to_dashes 1 :≡ cons_string - empty_string
      Nat_to_dashes (S n) :≡ cons_string - (Nat_to_dashes n)

      dashes_to_Nat : (d : dashes) × (d = empty_string → 0) → Nat
      dashes_to_Nat (cons_string - empty_string) :≡ 1
      dashes_to_Nat (cons_string - l) :≡ S (dashes_to_Nat l)

  which by univalence gives us `Nat = (d : dashes) × (dashes = empty_string → 0)`

  And then restructuring `_+_` as a relation:

      add_rel : Nat → Nat → Nat → Type
      add_rel n m o :≡ n + m = o

  which can be proven equal to `_p_q_` by functional extension.

  QED.
  ```

- u/None:
  ```
  >P.S. Sorry if this post is a little rushed. 

  That's how it begins, the awaited dropping off into oblivion ;)

  But seriously, good job on these introductions, they are more than appreciated!
  ```

- u/markus1189:
  ```
  about the dialogue questions:

  5) not yet a good idea

  [1)](#s " it was looking at all the animals inside the mosaic")

  [2)](#s " he")

  [3)](#s " headache")

  4) no clue, I am not sure if the hint about the snail has something to do with it, any tips for me without giving it away?

  ---

  About the chapter in general:
  - the pq-system is only isomorphic to addition with natural numbers **not including** 0, right?  There is no way to map

      1 + 0 = 1

  from numbers with addition to the pq-system as

      -pq-

  because this is not a theorem of the system.  Maybe it's just nitpicking or due to the fact that positive numbers does not (always) include 0?

  ---

  And aside: What I always found astonishing about *isomorphisms* is that if you have one from A to B and then discover one from B to C you can also go from A to C (transitivity) and therefore get insights about a (probably) totally unrelated domain!
  ```

- u/None:
  ```
  Wikia links:

  * [Chapter 2](http://godel-escher-bach.wikia.com/wiki/Chapter_2)
  * [Sonata for Unaccompanied Achilles](http://godel-escher-bach.wikia.com/wiki/Sonata_for_Unaccompanied_Achilles)

  xamueljones, any interest in including these in your posts? While the Wikia is far from complete, I'm trying to make sure that each page has reasonable content in advance of the /r/rational reading schedule. It's a good motivation to get the pages started.
  ```

- u/Ty-Guy9:
  ```
  I may have an insight into this quote, and I'm wondering if anyone shares the opinion.

  > If we were to delve into Euclid's proof more and more carefully, we would see that it is composed of many, many small-almost infinitesimal steps. If all those steps were written out line after line, the proof would appear incredibly complicated. To our minds it is clearest when several steps are telescoped together, to form one single sentence. If we tried to look at the proof in slow motion, we would begin to discern individual frames. In other words, the dissection can go only so far, and then we hit the "atomic" nature of reasoning processes. A proof can be broken down into a series of tiny but discontinuous jumps which seem to flow smoothly when perceived from a higher vantage point.

  Does anyone beside me have an intuition that this idea of a "ground-level" for proofs is incorrect? That there will always be another breakdown into deeper assumptions?

  See, I remember once getting a sense that if one looked closely enough at any proof, one should be able to break each logical step down into further and further levels of detail, drawing out assumption after assumption. It would not be like what the tortoise said to Achilles, in which he repeated the same single trick forever, but would be non-repeating (in the same sense that irrational numbers would be non-repeating if their digits formed a tree instead of a sequence).
  ```

  - u/None:
    ```
    So, on the one hand, you can go down a lot of levels. On MetaMath, one site that collects mathematical proofs that are fully broken down into axioms, you can find [a proof that 2+2=4](http://us.metamath.org/mpegif/2p2e4.html) that can be expanded into more basic steps up to 150 levels deep.

    But it's got to be a finite number of steps in the end. Eventually you reach your axioms and your basic rules of inference, whatever you choose them to be. 
    You could choose some other rules  that put you farther away from the thing you want to prove, but there must still be a finite number of steps. So at some point you hit the "atoms" of your proof, or else you don't actually have a proof.

    And we choose to agree on the purpose of the system, so that we can't be trolled by the Tortoise. MetaMath and similar systems, for example, make a distinction between "(2 + 2) = 4" and "⊢ (2 + 2) = 4". The first is a proposition to be manipulated by the rules, the second is an actual result that we believe, and when we firmly distinguish these, the Tortoise's paradox doesn't trip us up.
    ```

---

