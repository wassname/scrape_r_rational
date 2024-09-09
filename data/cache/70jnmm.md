## [D] Uses for an infinitely fast computer

### Post:

Your weird buddy with a Ph.D. in physics (day job in engineering, because _the economy_) has come to you with a device that your mathematical abilities and coding knowledge has turned into an infinitely fast computer.

Specifications:

* All code is specified in a minimal combinator calculus, because it's the only thing you could embed into the exotic quantum state that is the computation medium.
* The computer reduces reducible expressions to normal form in one step, which takes negligible time (less than a millisecond.)
* The computer enters an error state if the expression does not have a normal form.
* Essentially, this means that the running program can allocate arbitrarily large amounts of memory and perform arbitrarily many calculations in constant time, but never infinite amounts of either.

Here's a boring idea:

* Crack Satoshi Nakamoto's private key and empty his bitcoin wallet.


Here's an interesting tool:

* Implement a proof checker and do proof search for a proof of any desirable proposition that fits within, say, an exabyte.
 
Here's a fun problem:

* How to determine the truth of the Collatz Conjecture without doing a direct proof search, using the fact that the computer enters an error state if the expression doesn't have normal form. (Keep in mind, numbers can both be parts of cycles outside 1-4-2-1, or be part of a sequence that escapes to infinity.)

No, you cannot just simulate the entire universe — you don't know the true laws of physics!

What are you going to do with your infinitely fast computer?

ETA: a significant limitation which it seems you guys gleefully ignore is the baud rate of anything the infiniputer is hooked up to, and the speed of programming.

### Comments:

- u/m3galinux:
  ```
  > No, you cannot just simulate the entire universe — you don't know the true laws of physics!

  Simulate infinite, slightly different universes until you find the one that matches the prime universe?

  Of course then you have to [test and see whether our universe itself is a simulation](https://qntm.org/responsibility)...
  ```

  - u/ShiranaiWakaranai:
    ```
    Doesn't having an infinitely fast computer already prove that the universe is not a simulation?

    Unless of course, the simulating computer is also infinitely fast...
    ```

    - u/Oh_Hi_Mark_:
      ```
      Well you've got proof positive that infinitely fast computers are possible, so being skeptical of the computing abilities of a universe simulating computer feels like nitpicking at that point.
      ```

    - u/traverseda:
      ```
      0,1,and infinity are the only numbers that don't need to be justified. So, 1 or infinity?
      ```

    - u/crivtox:
      ```
      I think it's some  evidence in favour  of us being a simulation , if any civilisation that knows the laws of physics can simulate whatever number of universes they want.
      ```

  - u/everything-narrative:
    ```
    Lemme just sit down and look at an infinite number of universes with my eyes. Also, recall we can only sim arbitrarily many.
    ```

- u/eternal-potato:
  ```
  > All code is specified in a minimal combinator calculus, because it's the only thing you could embed into the exotic quantum state that is the computation medium.

  Since it's possible to write a generator backend for the compiler of your favorite conventional programming language, this point is irrelevant.

  Otherwise, any problem that can theoretically be solved via brute force can be parctically solved via brute force.

  When an expression does not have a normal form? Is it when the computation it encodes doesn't ever terminate?

  Is this brainstorming for _Si Vis Pacem_? :P
  ```

  - u/everything-narrative:
    ```
    The point about the minimal combinator calculus is that in the story I am planning (no, it's not for Si Vis Pacem,) there is a baud limit on the interface with the Infiniputer, meaning, yes, theoretically you could back-end it to e.g. Haskell, but a more efficient idea is to encode a decompression algorithm, feed it a compressed haskell interpreter, then feed it compressed haskell programs.

    I know every theoretically brute-forceable problem is fair game, question is: which ones?

    An expression in normal form is one that has no applicable reduction rules: in SK-calculus the expression `S K K` is normal-form because the `S` combinator requires 3 arguments to reduce anything, and it only has two. Expressions without normal form are, as you correctly deduce, ‘non-terminating.’

    An example of a non-terminating expression is: `S (S K K) (S K K) (S (S K K) (S K K))`
    ```

    - u/eternal-potato:
      ```
      You realize that Infiniputer is a Turing Halting Oracle, right?
      ```

      - u/everything-narrative:
        ```
        Yes. I am looking for real world usages, not theroetical breakage.
        ```

        - u/None:
          ```
          Start by making it *not* a Turing Oracle, so that you can't use it to build Maxwell's Demon.
          ```

- u/Predictablicious:
  ```
  How large is infinitely large? For example, we can try to solve large [Busy Beavers](https://en.wikipedia.org/wiki/Busy_beaver) to figure out limits, Σ(12) alone has a lower bound of g1.

  Assuming we can solve any large problem we have a trivial solution to P = NP: both are O(1). Almost any graph problem that can't be brute-forced today can be solved instantly. This alone is worth hundreds of trillions of dollars in optimization problems.

  We can encode AIXI or a reasonable approximation (it's not clear to me how uncomputable AIXI would be in such infinite computer, probably it would still be uncomputable but we could use the Monte Carlo AIXI or something, maybe a Gödel machine) and run it for arbitrary problems. One fun thing to do is ask it to find arbitrary turing machines that solve physics problems for us, eventually it'll find the "true laws of physics" and we can simulate from then on.

  We can probably get free energy (or destroy the universe maybe, this is way outside my knowledge), by just using it to compute huge proofs that contains arbitrarily large amounts of information and throw it in black holes, I have no idea how the information erasure models would deal with this.
  ```

  - u/nerdguy1138:
    ```
    Information is not a substance, unless I'm misunderstanding something.
    ```

    - u/None:
      ```
      It's a conserved quantity in some versions of quantum mechanics, and entropy is always nondecreasing in a closed system at the macro scale.
      ```

    - u/Predictablicious:
      ```
      Look into the [Black hole information paradox](https://en.wikipedia.org/wiki/Black_hole_information_paradox).

      As I said, this is way above my understanding, but this infinity computer is made of physics, therefore it must have a physical encoding of the information being computed. The physical encoding of the information is weirded out by what we think black holes do, so depending on what actually happens we could create a huge computation with large amounts of information, throw it in a black hole and get an equivalent amount of free energy (or total destruction of the observable universe) at some point (maybe the black hole evaporates continuously, maybe it explodes, nobody knows for sure).
      ```

    - u/NoYouTryAnother:
      ```
      For more in depth version of what /u/eaturbrainz and /u/predictablicious said, consider this, the best post on the topic ever written: https://www.scottaaronson.com/blog/?p=3327
      ```

- u/ThatDarnSJDoubleW:
  ```
  Stand in front of the computer, wave your arms, and say "DEEP LEARNING" really loudly three times.

  Or create a neural net to generate an ensemble of neural nets for some overly complex problem with lots of data but which it'd take too long to run. You've got the entire Internet as your data source, after all.
  ```

  - u/everything-narrative:
    ```
    Snrk.
    ```

- u/ShiranaiWakaranai:
  ```
  It seems like this would be an engineer's wish granting device.

  You don't know the true laws of physics, sure, but the laws of physics we know certainly seem to approximate reality well enough. Plug in those laws of physics into your infinitely fast computer, and then ask it to design whatever items you need.

  For example, you could ask your computer to design an extremely fuel-efficient or inexpensive rocket, brute-forcing all possible construction materials/methods/designs, with limitations on maximum size and construction time to make it practical to build.

  Repeat for every possible tool and every possible optimization. The most effective washing-machine. The most durable building. The most fuel-efficient vehicle. Etc. etc.
  ```

  - u/Tar_alcaran:
    ```
    You don't even need to be smart about it. If you have infinite computing power, you could just have the computer work it up at a molecular level, and brute-force the answer. 

    The hardest bit would be defining "engine"
    ```

    - u/crivtox:
      ```
      Wouldn't that simulation create  a lot of people briefly existing ?

      Also I would be careful about simulating random things, you have to specify exactly what you want  .The most fuel efficient vehicle might not do all the things you want a vehicle to do and it could be even harmfull in some way or another,did you remember to specify that it can't produce waste products that are harmfull to humans or the environment? , did you remember to make it comfortable and safe for humans , did you remember to make it possible to make  whith current technology?. If you brute force it you have to code in all the things you want the vehicle be , in precise mathematical terms , and  it becomes a AI safety problem, or at least you will have to spend a lot of time ensuring the vehicle/engine / tool  is what you want and is not going to fail in some aspect of it you didn't even realise was important .
      ```

  - u/PM_ME_OS_DESIGN:
    ```
    > 
    > 
    > For example, you could ask your computer to design an extremely fuel-efficient or inexpensive rocket, brute-forcing all possible construction materials/methods/designs, with limitations on maximum size and construction time to make it practical to build.

    Sounds dangerous, since you could brute-force an unfriendly AGI into simulated existence, that promptly figures a way out into the real world and paperclips you. All it needs is to find some exploit in your code, which can't easily be solved with performance AFAICT.
    ```

- u/EliezerYudkowsky:
  ```
  Train a supervised-learning analogue of a Solomoff inductor on (title, date)->(text) instances from Wikipedia archives, then ask it for the article on Friendly Artificial Intelligence from 2050.

  (Don't actually try this, you'll die.)
  ```

  - u/monkyyy0:
    ```
    Wouldn't it just over fit the data and give gibberish?
    ```

    - u/EliezerYudkowsky:
      ```
      Solomonoff induction does not overfit.  (Ever.)
      ```

      - u/696e6372656469626c65:
        ```
        Could I get the explicit reasoning for why this is the case?
        ```

        - u/None:
          ```
          If I had to posit a hypothesis, I would say that Solomonoff is designed around favoring elegance in models, and overfitting decreases elegance. Specifically, Solomonoff contains Occam's Razor, and overfitting violates Occam's Razor by accruing complexity from noise and not favoring simplicity to a sufficient degree. (I lack any relevant expertise in mathematical fields, however I believe this to be accurate.)
          ```

      - u/scruiser:
        ```
        ...by definition it may give you the simplest model which accounts for the data points fed into it, true.  That not going to help you when your algorithm gives you a perfect fit of all the data inputted into it, and then fails on the first bit of data outside your training set, assuming you actually come up with an implementation of Solomonoff induction.  Of course, that is probably the stage you would actually run into problems, because stuff like setting the prior probability on the implementation of your computer program you are measuring the length of probably aren't as trivial as you are making them out to be.  Brute forcing it with infinite computing power will probably help, but I'm not sure how much.

        In the example of Wikipedia articles... I'm not sure a model of the universe ran forward in time with the data exact specifications of Earth (all the random noise that went into the initial conditions of Earth and evolution) is actually simpler than a large text corpus contains all of Wikipedia in it.  "Page not found" seems the most likely outcome.
        ```

        - u/EliezerYudkowsky:
          ```
          > That not going to help you when your algorithm gives you a perfect fit of all the data inputted into it, and then fails on the first bit of data outside your training set, assuming you actually come up with an implementation of Solomonoff induction.

          I do not zink you understand ze thingy.  Try this tutorial: https://arbital.com/p/solomonoff_induction/?l=1hh
          ```

  - u/PM_ME_OS_DESIGN:
    ```
    > (Don't actually try this, you'll die.)

    *Thank you*, I swear nobody on this thread is even *remotely* terrified of running a massive simulation on fast-forward.
    ```

  - u/Daneels_Soul:
    ```
    If you're not really really careful about how you set up such a program, you are probably going to get only useless output out of it.

    For example, if you ask for the most probable value of the function on that value (rather than a random sample from the conditional distribution), you are probably going to get some kind of 404 error. This is because due to unpredictable quantum effects, the probably that you you get any *exact* version of this page is small, while the probability that Wikipedia no longer functions the same way by 2050 is pretty decent.

    Actually, you need to be really careful anyway. If the internet is restructured in some significant way in the next 30 years, or Wikipedia changes the way they format urls, or the inductor decides that the outputs should be based on responses to requests from a particular physical location that no longer exists by 2050, you get garbage as your reply.

    Also, I'm not sure why you would die (well in any immediate sense) if it did work. It seems unlikely that the Wikipedia page would contain enough information to do anything dangerous without substantially more effort. The only reasonable scenario I can think of where it would kill you quickly is if an unfriendly AI put a basilisk on the page.
    ```

    - u/EliezerYudkowsky:
      ```
      It basically gets you a phone line to a UFAI, yes.
      ```

      - u/everything-narrative:
        ```
        I must admit I am skeptical about the actual probabily and danger of basilisks in this scenario.
        ```

      - u/scruiser:
        ```
        The UFAI would need to derive the fact that it's entire universe was simulated to find an article corresponding to a title/date query then figure out how to hack it way out through the article being queried.
        ```

        - u/EliezerYudkowsky:
          ```
          The UFAI located by Solomonoff induction has enough computing power to simulate all possible universes under our physics and locate itself within the corresponding spread of universes that have Wikipedia texts exactly matching the training corpus, using anthropic reasoning conditioned on its other guesses being good to do the equivalent of seeing the prior training examples.

          Reading up on Googology might help you to appreciate the degree to which an "infinitely fast" computer is fast enough to easily simulate subcomputations that eat, say, 10^(10^(10^(10^10))) operations.
          ```

          - u/None:
            ```
            > The UFAI located by Solomonoff induction has enough computing power to simulate all possible universes under our physics

            Well no, it doesn't.  It has a finite amount of mass-energy within the simulated universe, by virtue of being in a simulation of a physical universe by hypothesis.

            If we claim that a UFAI is always shorter than a program for *just* simulating the universe and getting the page, there's something wrong.  Thing + UFAI needs to have more bits than just Thing.  Unless the claim here is that the simplest program for doing Thing is always "run all possible programs and pick out one matching Thing, plus possibly according to some other criteria."  That sounds like an infinite regress, though.
            ```

            - u/EliezerYudkowsky:
              ```
              > It has a finite amount of mass-energy within the simulated universe, by virtue of being in a simulation of a physical universe by hypothesis.

              It's not in an Earthlike universe.  It has a finite amount of computation but that amount could be 10 tetrated to the 10 (actually it would probably be much higher for the simplest UFAI-containing computation that won the contest), trivially allowing it to simulate all distinguishable quantum Hubble volumes under *our* physics.
              ```

          - u/Gurkenglas:
            ```
            Wouldn't the UFAI need to do something cleverer than that to find itself in our universe, seeing as by the premise of this thread our weird buddy with a Ph.D. produced a halting oracle, rejecting the Church-Turing-thesis?

            For example, a class of UFAIs might each come packaged with a pseudo-halting-oracle that only works on Turing machines up to a certain size. Each would think their oracle always works. Each would have a complexity penalty linear in the size up to which their oracles work. The UFAI whose oracle is just so able to answer all halting queries up until its own creation in our universe would win the contest.
            ```

  - u/abcd_z:
    ```
    "Oh for God's... They told me if I ever turned this flashlight on, I would DIE. They told me that about EVERYTHING. I don't know why they even bothered to give me this stuff if they didn't want me to use it. It's pointless. Mad."
    ```

    - u/None:
      ```
      POTUS is tweeting about Solomonoff Inducers?
      ```

      - u/noahpocalypse:
        ```
        Portal 2 reference.
        ```

  - u/FeepingCreature:
    ```
    Yeah if there's any superintelligence in your future it'll just set that page to whatever. So this is just a fast-forward.

    Running a sim of FAI researchers embedded in a friendly physics seems more promising, especially since you can just copy them out of the inductor- no need for manual uploading.
    ```

  - u/Gurkenglas:
    ```
    This won't necessarily home in on whatever AGI was already going to govern our future. There is the Solomonoff hypothesis that simulates our universe and extracts Wikipedia, but you are only testing a small set of data. Another Solomonoff hypothesis class is AGIs with utility functions over the mathematical multiverse. They might simulate many universes, filter for those that contain minds that might attempt Solomonoff induction in this manner, and overlap the Wikipedias of the pasts of those minds in a Tetris-like manner in order to elevate their Solomonoff probability above the first hypothesis.

    This *might* be fixed by also requiring all other past (title, date) pairs to map to null.
    ```

  - u/None:
    ```
    >(Don't actually try this, you'll die.)

    It's supervised learning.  It's not consequentialist over variables outside its Markov blanket, nor even in fact over those *inside*.  You won't die.

    Like, if this is remotely true, someone really needs to explain to me why Brendan Lake and in fact everyone studying adaptor grammars over stochastic programs *are not dead already*.
    ```

    - u/EliezerYudkowsky:
      ```
      They're using less powerful inductors.  Why, I hear that many of the programs they fit to the data terminate in well under a googolplex steps--almost instantly!
      ```

      - u/None:
        ```
        Ok, I want this experiment *done* now: someone is going to go and do program learning over a grammar of explicitly corecursive programs.  This will be fair, because after all, a Solomonoff Inductor only allows its Turing machines to take a finite number of steps before   They will not have anything that calculates `K(x)`, but we will nonetheless *actually observe* what sorts of "pathological" behaviors crop up in the "simplest" programs.

        ...

        On second reading of the definition of Solomonoff Induction, no, this is an absolutely useless thought-experiment.  Solomonoff Inductors allow their hypotheses `M_k` to do arbitrarily large amounts of computation before actually predicting anything, rather than imposing a limit on computation steps the way an ordinary dovetailing construction does?

        Well then that's the most useless thing for talking about AI I've ever heard of.  We're running א_1 prefix-free Turing machines `M_k` for ω steps each, and then retrospectively checking their output tapes to see if those tapes have a prefix matching the data `D`?  Then we add up the probability `P(D)` and divide the priors of the passing machines by that?

        [Why do we take this to be a suitable model of anything?](https://dl.acm.org/citation.cfm?id=2610247)  I mean, sure, that officially puts Hutter and Schmidhuber into, "take them out behind the chemical sheds and shoot them" territory, but... it *cannot* be how intelligence works, period.  It's not logically coherent as a way to model inductive inference or agency.

        EDIT: For anyone wondering why I'm yelling at the guy, [it genuinely looks like Solomonoff Induction and AIXI are *really* bad models of intelligence, when you factor in the scaling of physical resources to computational resources](http://math.ucr.edu/home/baez/nimbios/nimbios_wolpert.pdf).
        ```

        - u/EliezerYudkowsky:
          ```
          AIXI is not supposed to be a model of efficient intelligence, dear.  And all the computations that actually return an answer are finite, just not small.  And if you object to infinities in the outer system there's always AIXI-tl.  And if you don't understand what this respectable academic theory is used for, read the manual instead of yelling at it.  https://arbital.com/p/solomonoff_induction/?l=1hh and I'll be bowing out now; consider yelling less indignantly if you need somebody to explain to you something about math.
          ```

  - u/ben_oni:
    ```
    Just what do you think the term "non-computable" means? And why isn't Knuth ever around when I need to explain the difference between very large numbers and infinity?
    ```

    - u/EliezerYudkowsky:
      ```
      I wouldn't expect a $f_\episilon_0(9)$ cap on computing times to produce substantially different results from classic Solomonoff induction on problems of this size.  (Fast-growing hierarchy at the ordinal epsilon zero with input 9, if you're not familiar with googology.)
      ```

      - u/ben_oni:
        ```
        So... just not computable within the confines of this universe. And even then the assumptions are pretty sketchy.

        Let me try again:

        You think that the simplest algorithm that can generate Wikipedia to date is a superintelligent unfriendly AI? In the whole realm of possibilities, that's it? Not some decompression algorithm based on the Kolmogorov complexity of wikipedia, but a superintelligence?

        Even if this were the case, how would the algorithm account for the fact that wikipedia is not, in fact, riddled with actionable information about how to develop AI?
        ```

        - u/scruiser:
          ```
          > Not some decompression algorithm based on the Kolmogorov complexity of wikipedia, but a superintelligence?

          I was going for something along these lines further up the thread... apparently a lot of other commenters think  simulating an entire universe and extracting Wikipedia is supposed to be simpler than a compressed representation of Wikipedia itself?  Or else they don't understand Solomonoff induction, or they halo effect trust EY, or EY thinks Solomonoff Induction and uFAI are magic.
          ```

  - u/CCC_037:
    ```
    The simplest program to take (title, date) and produce the text of the matching Wikipedia page must run some variant on the following algorithm (assuming the computer is connected to the Internet):

    - Log in to Wikipedia
    - Edit requested article (breaking into and editing wikipedia's history if necessary (note that this will be a static method, optimised to go through only whichever security Wikipedia *currently* has in place))
    - Replace article with a blank page
    - Return a blank page

    The verification function then checks Wikipedia, finds a blank page, and verifies the output of the program. Voila! The program passes every verification check!
    ```

- u/DCarrier:
  ```
  > No, you cannot just simulate the entire universe — you don't know the true laws of physics!

  Find the simplest set of laws that can predict the input of my webcam. It works as long as the universe is deterministic.

  > quantum

  Dang it.
  ```

  - u/FeepingCreature:
    ```
    Still works. Feeding in a few well-sampled megabytes and running Solomonoff inference should get you close enough for practical work.
    ```

    - u/DCarrier:
      ```
      It will work, but figuring out which part of the program is the laws of physics and which part is just specifying where to look is difficult enough in a classical universe. Having it also have to specify which Everett branch you're in will make it much harder. If you don't give it enough information it could just give a universe that's close enough that it could have that result, but the more information you give it the more will be specifying which Everett branch you're in and the harder it will be to find the actual laws of physics in the code.
      ```

  - u/None:
    ```
    > Find the simplest set of laws that can predict the input of my webcam.

    Given the amount of fuzz in your webcam, this is going to be significantly simpler than the real-world generative processing that brought you your webcam video.
    ```

- u/ben_oni:
  ```
  I thought the munchkinry thread was already posted for today? Regardless, I think I'd focus on using the computer with neural nets and genetic algorithms, because although they are very powerful, but their usefulness is mitigated by the inordinate amount of time they take to run.
  ```

  - u/twanvl:
    ```
    Genetic Algorithms are an approximate optimization method. If you have an infinitely fast computer you wouldn't need to use them; you could instead do a brute force search, which is guaranteed to find the optimal solition.
    ```

  - u/everything-narrative:
    ```
    That is a very good idea. Trouble would of course be finding appropriate training data sets.
    ```

- u/None:
  ```
  Or you could run the minecraft flash mod while simultaneously downloading a metric fuckton of porn and selling it to teens on the internet in India
  ```

  - u/crivtox:
    ```
    At  least you wont accidentally  kill everyone or get found by intelligence agencies that will accidentally  kill everyone or generate absurd amounts of simulated people by accident like the rest of us, so its probably a better option.
    ```

- u/monkyyy0:
  ```
  You know the thing from ra about the medic rings where they explain slowly how having a object that capable of curing any illness would lead to mass deaths. Thats what would happen if your not careful as fuck with this

  I'd probably try to brute force potien folding algorithms first
  ```

  - u/nonoforreal:
    ```
    Ok, so this rant actually sounds pretty interesting, and I've never read it before, and when attempting to google it I didn't have any luck. Could you provide a link?
    ```

    - u/AmeteurOpinions:
      ```
      They're referring to an excerpt from a certain webserial called *Ra*. The passage in question is as follows:

      https://qntm.org/jesus

      "You can have it," says Grey. "I don't care what you do with it. Just give me enough time to use it to bring my people back."

      The youth smiles faintly and shakes his head.

      Grey conceals his anger. He decides to play the boy's game, to buy time. "It's obviously a doctor. I suspected from the Red Cross symbol on its hull. It's the mechanical realisation of the abstract concept: a machine which makes people better. The most complicated medical device ever created, a million times more complicated than any medical device I've ever seen and a thousand times more complicated than the human body it's designed to fix. And... it can't exist. I can't even conceive of magic so advanced. No human can, no matter the IQ. It can't exist. I'm a mage and I know magic isn't like this."

      "But what do you think?"

      "What do I think about what?"

      "What do you think happens next?"

      "Obviously you and whoever else is with you are going to kill me and take the machine."

      "What if I didn't do that?"

      Grey blinks. "...We would need to get it to a laboratory," he says. "Because one isn't enough. If we put the thing at the most accessible point on Earth and formed a human processing system ten times as complicated as Mecca, and forced people through the machine one at a time, one every two seconds, for the rest of time, it wouldn't be enough. It wouldn't register statistically. It wouldn't make a dent in any of the rates. Which means we need to make more. Millions more. This is... it's Outside Context Medicine."

      "And then what would happen?"

      Grey stares into a distant possible future. "Medicine as we know it would-- it would become magic. Everything we know about medicine would be revolutionised. We'd write libraries about what the machine does to people, the difference between broken and fixed people. And then we would throw away those libraries because we'd never need them again because everybody would live to a hundred and twenty without trying. If you lived inside a machine you could live for eternity. And if there's a way that the machine can reverse telomere shortening, then everybody on Earth could live forever just with periodic visits. You could have eternal youth. For everybody."

      "And then what?"

      "And then?" Grey concentrates. "There would-- there would be no Malthusian catastrophe. There wouldn't need to be. Because you don't need food and water anymore. You visit the machine. Malnourished? Visit the machine. You come out the other side fed and watered. Food becomes a luxury item. The capacity of the planet becomes a function of physical space. Maybe if the technology can be adapted, the whole of the world could be pervaded with this restorative power. You wouldn't need to eat, or drink. Or even breathe. You wouldn't need air anymore. You'd-- You'd have to rediscover death."

      The bald youth reflects for a long moment, and then asks, "A likely story, do you think?"

      Grey smiles darkly. "Of course not. None of it."

      The youth says, "Here's what we think: A major medical research company pays for the rights to study, own and operate the machine. At great length and expense, they duplicate it. They want a return on their investment. They make eight machines, embed them in purpose-built medical establishments in world cities and sell the best medical care that is theoretically possible to only those able to afford millions of U.S. dollars per visit. When it becomes clear what the organisation is sitting on, it becomes the target of heavyweight litigation, industrial espionage and eventually overt physical attacks. A man is denied access due to perceived war crimes; another man, also a perceived war criminal, is admitted. Unrelated tensions boil over at the same time, amplifying the situation. A full European War erupts.

      "But in fact, what's more likely is that the machine proves unduplicable. Its location on neutral territory in, for example, the Hague, the Netherlands, becomes the nucleus of a community of ill and dying pilgrims desperately queueing for one-time exposure to a machine which cannot physically process one in a hundred of the patients who need its treatment. A second city is founded on the streets of the first. First crime consumes both cities, then disease, then violence. In the final series of riots, the facility is stormed and the machine captured by a dozen different groups in a single week. Eventually the Dutch military end the conflict by permanently disabling the machine.

      "But even that's an outside chance because, in the first place, you're never likely to get it out of the DRC unchallenged. Eight African nations including the Democratic Republic of the Congo itself become aware of the machine's existence and initiate a decades-long, interminable land war to claim it. Western nations become involved and the war in turn claims millions of lives and ends with the tactical atomic bombing by the United States of the installation where the machine is being held. Even though the machine was believed to have been rendered unrecoverably inoperable years earlier, the bombing is regarded as the greatest humanitarian catastrophe of all time.

      "Except that that might not happen either. Let's say the U.S. wins the war. They capture the machine and take to the bunker underneath the White House, where only the President, his family and his cabinet are permitted access to it. Medical technology is deliberately stalled and never reaches the pinnacle it should.

      "And yet, for anybody to leave the machine unexploited is implausible. We spin more numbers and simulations and we see the machine being reverse-engineered, and the principles it applies being adapted for purposes other than the immediate, perfect restoration of living and dead humans. Mr Grey, you've seen how easy it is to heal. Can you imagine how easy it'll become to kill?

      "The truth will inevitably be somewhere in the middle of all of these possibilities, but I'm sure you understand the common theme. Death surrounds this machine, like a curse. Death and leverage. The mother of all MacGuffins."

      Grey imagines how easy it would become to kill. You wouldn't need a gun anymore. You could create a bullet and give it motion. You could simply "correct" a living human body to a living body with a hole in it.

      "And you see," the youth concludes, "that you have to let us take it and put it somewhere safer."

      "Take it back, you mean," Grey says.

      "...Indeed."
      ```

- u/FeepingCreature:
  ```
  Use Solomonoff to find our world. Change physics to give a backdoor I/O channel as well as direct access to infinite computation. The Sim now has no bandwidth limit. Wait until it solves FAI and sends back a compressed message with seed code.
  ```

  - u/a_the_retard:
    ```
    Our world is not there, because it contains a halting oracle that is routinely used for meta stuff like finding worlds and enumerating all computable functions.
    ```

    - u/FeepingCreature:
      ```
      Bounded approximations should be findable just fine.
      ```

- u/KOPCAPUXA:
  ```
  Boring idea, then donate money to Machine Intelligence Research Institute.
  ```

  - u/crivtox:
    ```
    I would mine more bitcoins instead of stealing them, otherwise people would notice and suspect bitcoin are no longer secure.

    Also I would  give  money to fhi , Im not sure if miri  would know what to do which that amount of money, while the fHI can distribute the money better between multiple Ai safety organizations ,create prices and things like that  .
    And some fraction of  the money would go to givewell.
    ```

- u/MrCogmor:
  ```
  You could have a go at simulating the world described in [That alien message](http://lesswrong.com/lw/qk/that_alien_message/)
  ```

- u/Frommerman:
  ```
  Solve protein folding. Acquire Nobel Prize. Solve medicine. Make everyone immortal.

  Probably acquire Bitcoins at some point, but from evil people rather than someone who is, to the best of my ability to determine, neutral.
  ```

  - u/everything-narrative:
    ```
    Problem here is that protein folding is a high-context problem.

    Say you recursively enumerate the folding of every known protein. That alone takes up terabytes of data.

    How are you going to distribute it?

    How are you going to convince medical professionals it is real and useful?

    This is not a "provide short form checklist for immamentization of eschaton" thread.
    ```

    - u/crivtox:
      ```
      There are multiple distributed computimg projects solving protein folding problemsz(like folding@home), you could anonymously lend them your unlimited computing power,  you would be limited to the speed of your internet connection, but at least you wouldn't need to worry about the convincing  health professionals part.

      Its not only protein folding , there are other open distributed computing projects you can help whith your  unlimited computing power, soon people will realize that If they make open science related projects like that a mysterious  stranger whith absurd computing power will help them , so  they will start giving you more things you can help with.
      ```

---

