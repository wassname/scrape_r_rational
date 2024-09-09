## [D] Saturday Munchkinry Thread

### Post:

Welcome to the Saturday Munchkinry and Problem Solving Thread! This thread is designed to be a place for us to abuse fictional powers and to solve fictional puzzles. Feel free to bounce ideas off each other and to let out your inner evil mastermind! 

Guidelines:

* Ideally any power to be munchkined should have *consistent* and *clearly defined* rules. It may be original or may be from an already realised story.
* The power to be munchkined can not be something "broken" like omniscience or absolute control over every living human.
* Reverse Munchkin scenarios: we find ways to beat someone or something  *powerful*.
* We solve problems posed by other users. Use all your intelligence and creativity, and expect other users to do the same.

Note: All top level comments must be problems to solve and/or powers to munchkin/reverse munchkin.

Good Luck and Have Fun!


### Comments:

- u/alexanderwales:
  ```
  Mostly posting here to see whether I've missed a trick. Possible mild spoilers for *Worth the Candle*.

  You're sitting in a room with a text terminal in front of you. Text typed into the terminal goes into the next room, where your friend is (and vice versa for their own terminal). The terminal is insecure, and in fact, presumed compromised, such that whatever is transmitted between rooms is captured, whatever appears on the screen might be from your friend or a third party, and whatever you type might be changed en route, if the message isn't denied by the third party entirely.

  You need to communicate with your friend without the third party knowing what's communicated. Luckily, the third party that's compromised the system has some incentive to keep you talking to each other, so won't just shut down communication between the two of you, even if you begin transmitting data that it doesn't understand (probably, anyway).

  There are two types of information to transmit. The first is information that you're comfortable with the third party knowing, the second is information that you're *not* comfortable with the third party knowing. **How do you talk to your friend?**

  * You and your friend have a pre-arranged authentication system in place, but it won't work in this scenario, because the third party can allow authentication to take place, then proceed as normal with capturing and manipulating the information.
  * You and your friend both previously memorized a fairly substantial table of information, where each number X is associated with either a 0, 1, or 2. The third party has no knowledge of this table, but the table length is limited, and there are obvious risks associated with re-using numbers.
  * You and your friend know each other fairly well, and have a shared history to draw on if you need more information.

  I've been looking at [Diffie-Helman key exchange](https://security.stackexchange.com/questions/45963/diffie-hellman-key-exchange-in-plain-english) but I'm not quite sure how that would work in practical terms for two people who don't have access to a computer.

  (Note that the pre-existing authentication system *can* be used to transmit bits, because you can say to your friend "fail the next part of the authentication for 1, pass it for 0", and whatever your friend says, the third party won't know if you're going to interpret it as 1 or 0. But the table is probably more effective.)
  ```

  - u/munkeegutz:
    ```
    Usually for cryptography, we call the two users Alice and Bob, but in this scenario, I think I'll call them Val and Joon...just random names I came up with ;-)

    I think that a key exchange is overkill -- the reason we use key exchange in modern society is that you want your computer to talk to Amazon, but you don't have any safe way to get Amazon information in the first place, and Amazon can't get you secure information.  Sending that first piece -- the cryptographic key -- securely is the emphasis of key exchange.  In this case, that table that Val and Joon arranged fills this need.  All they need to do is agree on an algorithm which makes cracking this hidden key impractical for an attacker.

    If we were dealing with a computer, I would be worried about cryptographic strength. In this case I'm going to assume the following:

    * Both the users and attacker have access to pen-and-paper math but no sophisticated computing devices. The attacker has, say, 100 people working under him (so more resources than the users) though
    * The attacker is content with trying to learn what was said after-the-fact.  Otherwise, the encryption becomes trivial, but as soon as it becomes clear that the attacker cannot follow the communication, he would shut down the channel
    * They can't see each other's work
    * The table is known to Joon and Val, not to the attacker, and is of useful length, but substantially shorter than the content of their communication

    Even in this scenario, the encryption is pretty trivial.  As Joern314 said, a one-time pad is an easy and effective tool.

    Treat the table of numbers as an ordered list (from lowest table index to highest). Take each triplet of numbers (each in base-3) and encode them together -- now each grouping of numbers encodes one of 27 values -- enough for the 26 letters plus a space!

    Your table is a third as long now, but each letter can be mapped to any other letter -- treat it like a Caesar Cipher, but with a rolling code.

    If you made the total length of your communication no longer than the one-time-pad, then you would have a truly unbreakable code. As you get longer messages, this technique becomes imperfect -- you could guess the \*length\* of the cipher after the message is several times the length of the cipher, after which you would be able to start collecting statistical information about the message.  But all of that is pretty computationally intensive and probably beyond the means of a bunch of humans in the five years before the world ends.

    With a reasonable-length pad (say, 60 base-3 digits or 20 letters long), you would probably be fine (because Intel does not exist in Worth the Candle)

    There are systems which are harder to crack than what I described, but that one works with pen and paper

    [https://en.wikipedia.org/wiki/Caesar\_cipher](https://en.wikipedia.org/wiki/Caesar_cipher)

    If you are patient and want an even simpler system, just write down a bunch of false (or irrelevant statements), each of which is a sentence long, and then match the true one with correct answers to the table.
    ```

  - u/Joern314:
    ```
    Just to clarify: using the authentication system you can communicate arbitrary amounts of independent bits the third party doesn't know? 

    Then you just need more bits than your secret message contains. Using the table as well, of course. https://en.m.wikipedia.org/wiki/One-time_pad

    There are some weaknesses humans will cause, i.e. timing attacks (counting how long you need to encrypt something) or changing one bit the two friends exchange, just to see if the message becomes unreadable, etc. Latter might count as blocking communication, though.
    ```

  - u/ceegheim:
    ```
    As others said, Alice and Bob don't need no modern asymmetric crypto. They already have exchanged key material.

    If they had access to calculator, they could now go on using e.g. AES-GCM. The problem is: They don't have this.

    [Small PRNG](http://burtleburtle.net/bob/rand/smallprng.html) was a good naive suggestion for a RNG that can be abused as a cipher (you XOR the output-stream with the cleartext). Authentication needs a hash function, not just a simple checksum; something like Murmurhash could work. (you don't want to be susceptible to bitflip attacks)

    [Bruce Schneier does not need a computer](https://en.wikipedia.org/wiki/Solitaire_(cipher%29) to do his crypto. Extra relevant because the cipher was designed as a prop of the Cryptonomicon. More modern, one could look at [LC4](https://eprint.iacr.org/2017/339.pdf), which is also authenticated and looks significantly faster to me; I really recommend at least skimming that paper and looking at the pictures at the end. Also, it is funny:

    >I made a simple appliance to help a human perform the LC4 encryption and decryption algorithms by hand. The appliance consists of 36 wooden tiles plus a small plastic game marker,
    which I carry around in a bag (Figure 2). Each tile is marked at the top with one of the characters
    of the alphabet; at the right, the value (c mod 6); and at the bottom, the value (c / 6), where c is
    the character’s integer value. The bag also is used to generate a random key: put all the tiles in
    the bag, shake it well, and draw tiles one by one

    Apart from this, I would think hard about other assets and priority: Is it really the case that both directions are completely insecure? And I would put more emphasis on authentication / MAC than on confidentiality, at least in Joon's situation, whatever it is. My take on it was [here](https://www.reddit.com/r/rational/comments/8vkomq/rt_worth_the_candle_ch_108109_dreamveil/e1pp3gn/?context=3).

    edit: Because that stuff is fascinating, apparently even almost trivial ciphers like [VIC](https://en.wikipedia.org/wiki/VIC_cipher) survived shockingly long, due to good OPSEC. But all this does not really matter, because Joon failed to properly prepare, as far as I can tell.
    ```

- u/JesradSeraph:
  ```
  I have to share this short and funny example of munchkinry:

  [Dragonball Z, rational edition](https://www.youtube.com/watch?v=LRLt3hkoB2g)

  (it has english subtitles)
  ```

- u/lars_uf3:
  ```
  You are the leader (president/governer/dictator/whatever) of (insert generic 21st century first world society). Superpowers have begun to manifest in, lets say 25% of the population all over the world. Superpowers come in all shapes and sizes, it could be anything you could imagine, god like power, or something insignificant. Regardless it is sure to cause some distruption to your society. Come up with a plan (new legislation, come up with new taxes, adjust budget spending, new ministries) to maximise the benefit your society gains from its new superpowered population.
  ```

  - u/Veedrac:
    ```
    > Superpowers come in all shapes and sizes, it could be anything you could imagine, god like power, or something insignificant.

    Then somebody is going to win, and you have no idea who. Spend all your efforts finding that person, and finding people who can find that person, before you lose. Your plan of action depends drastically on who you can get working for you. You will probably still fail though.
    ```

  - u/CCC_037:
    ```
    Propaganda time. Emphasise safety, patriotism. Depict the discovery of new powers as something to be celebrated - and *registered*, so the government knows what's going on.

    Hire suitable Supers where possible, especially in law enforcement. Bear in mind that most people don't want to destabilise society, and try to sort out the ones who do. Sharply discourage vigilanteism, but encourage flashy, visible power use amongst registered law enforcement individuals.
    ```

---

