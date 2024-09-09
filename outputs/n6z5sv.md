## [D] Friday Open Thread

### Post:

Welcome to the Friday Open Thread! Is there something that you want to talk about with /r/rational, but which isn't rational fiction, or doesn't otherwise belong as a top-level post? This is the place to post it. The idea is that while reddit is a large place, with lots of special little niches, sometimes you just want to talk with a certain group of people about certain sorts of things that aren't related to why you're all here. It's totally understandable that you might want to talk about Japanese game shows with /r/rational instead of going over to /r/japanesegameshows, but it's hopefully also understandable that this isn't really the place for that sort of thing.

So do you want to talk about how your life has been going? Non-rational and/or non-fictional stuff you've been reading? The recent album from your favourite German pop singer? The politics of Southern India? Different ways to plot meteorological data? The cost of living in Portugal? Corner cases for siteswap notation? All these things and more could (possibly) be found in the comments below!

Please note that this thread has been merged with the Monday General Rationality Thread.

### Comments:

- u/PastafarianGames:
  ```
  It is often said that quantum entanglement is not capable of permitting FTL communication. The reason I most often see given for it is the somewhat circular logic of "because the laws of physics forbid FTL communication"; that is, instead of explaining why quantum entanglement can't do it, the person instead explains why it is forbidden for quantum entanglement to be able to do it.

  I find this somewhat dissatisfying. I've read a bit about what the mechanical reason is, and it seems to boil down to "entangled particles don't actually affect each other, they merely behave exactly the same way as each other; so you can't use them to communicate". Is that about as accurate a statement as I'm going to get/understand as a layperson, or would someone care to correct me here?
  ```

  - u/Radioterrill:
    ```
    Sort of, here's how I'd put it:

    When a particle is in an unknown quantum state, the only way to get information about that state out of it is to perform a measurement on the particle. That forces the particle into one of the measurement states and tells you which one it ends up in. However, you can't control which measurement state it goes to. Once a particle is in a measurement state, performing the same measurement on it will get the same result.

    With quantum entanglement, two particles share the same state. That means a measurement of one of the particles will be a measurement of the shared state, and so it forces both particles into that measurement state even if they're physically separate. 

    That means you can have one of the particles and send the other to a friend, and when you measure yours, your friend's particle is also put into the measurement state. However, you can't do anything with that because when you take the measurement you can't control what state it ends up in. In fact, your friend won't even be able to tell that you made a measurement at all, because when they take a measurement of their particle it'll look the same as if they were the one to measure it first.

    [The Wikipedia page for the No-Communication Theorem](https://en.m.wikipedia.org/wiki/No-communication_theorem) is a good summary of the mathematics behind this.
    ```

    - u/ArmokGoB:
      ```
      Another way of summarizing this I'd say is: While other experiments rule out hidden variable theories, and we very much know there's no such thing as hidden variable, the reason for why this *particular* exploit fails is the same as the one that'd be intuitively obvious is the case for hidden variables.
      ```

    - u/PastafarianGames:
      ```
      Hm. So the central tenet here mechanically, if I'm understanding correctly, is that there is no way to perform a measurement in such a way that it will change an unknown-state particle to A but not change a B particle to A?
      ```

      - u/Radioterrill:
        ```
        I'll try to clarify how the measurements work. The usual example is of the polarization of light. 

        In an unknown state, the polarization can be in any direction. 

        Possible polarisations: | / - \ 

        When you measure the polarization, you choose what basis you want to measure it in. Let's say we use the vertical and horizontal basis.

        Measurement basis: + (rather than the diagonal basis X)

        In this basis, the measurement states are horizonal polarization or vertical polarization. If the unknown state corresponds to one of those, it will stay in that state. Otherwise, it collapses into one of those states, with the closer one being more likely. You can think of it as snapping into one of them, like prodding a Phillips screw with a flathead screwdriver.

        | -> |

        / -> | or - at random

        \- -> -

        \ -> | or - at random

        So if you measure the polarization as vertical, that doesn't mean it was vertical to begin with, it could've been a diagonal state that was forced into the vertical measurement state when you took the measurement. 

        Let's say you invite your friend to measure the particle too. If they use the horizonal and vertical basis, they'll get the same result as you, but they have no way of telling whether you made a measurement before them - the probability of it coming up horizonal or vertical is unchanged. There's no way to communicate information just by taking a measurement.

        When you have two entangled particles, you can measure the state with either of them even if they're in different places, but the same rules apply - you still can't communicate just by taking a measurement. 

        Does that make sense? Apologies if I misunderstood your question
        ```

        - u/PastafarianGames:
          ```
          This is great and we're making progress, but I still have questions, and I hope you don't mind answering them.

          Is it possible to measure in such a way that the random distribution you get from the / \ collapse is skewed? Hypothetically, if you could, it seems that you could have a million of them and a pre-set time, and use it to transmit a probabilistic bit. So I'm guessing you can't?
          ```

          - u/Radioterrill:
            ```
            No problem, it's a good opportunity for me to refresh my memory of how it all works. 

            You guess correctly, there's a couple of factors at play here. 

            Firstly, there's only one way to measure in a given basis, so you can't change the measurement to bias it towards a particular result. If you measure in a different basis, the same problems apply. 

            (Let's say you measure in the diagonal basis instead. Then the state changes to the diagonal measurement states, / or \\. When your friend measures in the horizonal and vertical basis, there's still the same 50-50 odds of them measuring each result.)

            In addition to measurements, the other way of interacting with states is to transform them, such as with a rotation. This doesn't collapse them like a measurement does, and can be used to communicate. 

            If you and your friend have access to the same state and agree that | = 1 and - = 0, you can measure the state to collapse it into one of those and then transform it with a rotation if it's not the one you want your friend to measure.

            However, transformations are local. That means that if you have separate entangled particles, you can transform yours all you like but it won't affect your friend's one, and so you can't use that to communicate.

            Say you've got an entangled state that can be either | - or - |, where you have the particle on the left and your friend has the particle on the right. If you apply a 90° rotation transform to your particle, that means that the entangled state becomes - - or | |. Your friend still gets the same results when they measure their particle, because their half of the state is unchanged. If you only rotate the particle if you measure |, the state ends up as - - or - |, and your friend still doesn't get any information out of it.

            Lastly, the talk of probability can make it sound similar to the problem of communicating over a noisy classical channel, but it's mathematically impossible to send any information with a single entangled pair so you can't do any better by using more of them - a million times zero is still zero.
            ```

            - u/PastafarianGames:
              ```
              Okay, that makes a ton of sense. If there isn't a way to measure something and bias the uncollapsed state's collapse in response, I can see how you mechanically can't get any information out of the system.

              Thank you!
              ```

              - u/Radioterrill:
                ```
                You're welcome, happy to help!
                ```

  - u/grekhaus:
    ```
    It's a standard-but-boring correlation/causation thing that popsci articles blew way out of proportion. To offer an analogy, it's like trying to communicate by establishing a special office where they make outwardly identical pairs of envelopes where the word "yes" is written on a slip inside one envelope and "no" is written on a slip inside the other, then mailing someone one of the two envelopes at random along with instructions to take the out the current slip, cross out the current word on it, write down the opposite of their actual response (which still has to be yes or no) and then throw it into the fireplace so that your envelope back home will magically transmute itself to have their reply, because "durrr, the magic slips always have the opposite words in them, the paper office makes sure of it". Obviously that doesn't work, and the reason why quantum communicators can't work is basically the same logic, except with an extra layer of quantum physics explaining how exactly the "envelopes" are being produced, shipped and altered.
    ```

    - u/RetardedWabbit:
      ```
      Wait, so all of the "entangled/quantum particle linked FTL Communication" in fiction would functionally be space ships with those letter pairs? I feel so betrayed. I always thought they were a theoretically possible material that might be practically impossible, like warp drives and huge amounts of antimatter.

      Edit: Read the wiki entry for action at a distance. Turns out my understanding of quantum entanglement via 50 year old Einstein quotes criticizing it as "spooky action at a distance" wasn't a good foundation
      ```

      - u/grekhaus:
        ```
        Correct. You'd have a huge box that somehow contains a bunch of particle pairs, and every time you ran out of bits to send messages with, you'd need to have some more particles shipped in from the place you're trying to talk to.

        The impossible magic supermaterial would be some sort of super-particle pair where wiggling one instantly wiggles the other. That would indeed allow for FTL communication (and, interestingly enough, time travel) but as far as we're aware that isn't a thing and can't physically exist.
        ```

        - u/callmesalticidae:
          ```
          I remember reading about a book which tried to address this, and the main commodity of (physical) interstellar trade was "entangled qubits," because they're expended as they're used, but are vital for FTL interstellar communication (and interstellar trade in knowledge).

          EDIT: It was Iron Sunrise, by Charles Stross.
          ```

        - u/RetardedWabbit:
          ```
          Wait, so logistics/supply aside you can send messages with them? My understanding is that checking your particles let's you know/deduce properties about their pair particles, but that doesn't transmit information and isn't observable on the pair particle?

          Yeah, I thought the wiggle one wiggle another was magic, but measure/flip one once flips the other was "real".
          ```

          - u/grekhaus:
            ```
            No, you can't. But if the "measure/flip one once flips the other" thing WERE how it worked, then the logistics of using it for communications would look like the thing that I described in the post above. But it doesn't work like that in real life, so there's no need for great  big crates of qbits.
            ```

- u/callmesalticidae:
  ```
  I got my second COVID vaccination last week. No "flu-like symptoms," but it turns out that if you get migraines, that can trigger them. 

  I don't know if anybody else on here gets migraines, but I thought I should mention it just in case. Obviously do get vaccinated anyway, but make sure you're prepared (I can work through the flu but can't do much with a migraine, so it sorta threw my workflow out of whack).
  ```

  - u/CCC_037:
    ```
    I would *love* to get vaccinated, and fully intend to do so as soon as reasonably possible. As I'm below 60 and not afflicted with any comorbidities, though, I'm down on the end of my country's priority list; and we aren't getting the vaccines in anywhere near fast enough...
    ```

- u/--MCMC--:
  ```
  Is anyone here familiar with (I guess) both basic stats and set theory? I'm OK at the former but well out of my depth in the latter and looking for a way to complete the following analogy:

      Correlation :: Jaccard Similarity
      Partial Correlation :: ?

  More details in a thread I posted yesterday here: https://www.reddit.com/r/AskStatistics/comments/n6krb5/partial_correlation_equivalent_of_a_jaccard_index/

  Any suggestions would be appreciated!
  ```

  - u/None:
    ```
    [deleted]
    ```

    - u/--MCMC--:
      ```
      yeah it involves more basic stats than anything (hence the question being in /r/askstatistics), but in my unfamiliarity with set theory I mistook a question of set intersects as falling under its remit but I guess not?
      ```

- u/HantuAnggara:
  ```
  There are people calling Eliezer Yudkowsky a cult leader and someone that doesn't qualify to be an ethical AI theorist/artificial intelligence researcher, prime example being /r/sneerclub. What does /r/rational think of this?

  Personally, I don't know much of the guy and his works; I dropped HPMOR as I disliked Harry (not that it makes the story bad, just not my taste). I don't think I can accept calling him an ethical AI theorist/artificial intelligence researcher if he didn't go to college for it. Or at least, no more than I can call Rolf Dobelli of "The Art of Thinking Clearly" a Cognitive Scientist. Rolf Dobelli is a well-respected author even if he isn't.
  ```

  - u/WhispersOfSeaSpiders:
    ```
    It's been several years and I'm a layman to computer science, but I remember looking into MIRI and reviewing some of their research papers on the topics you mentioned (which seemed pretty par for research papers). 

    Based on that, if Eliezer's still contributing to that work then I don't see why he couldn't be called an ethical AI theorist/artificial intelligence researcher. You don't need a degree to conduct research, after all.
    ```

  - u/GriffTheJack:
    ```
    All opinion:

    To my lay knowledge and outsider perspective to his rational community, Yudkowsky is an ambitious self-taught philosopher. His research has a very narrow focus ("humanity might create a godlike intelligence at some point in the future, the most likely avenue for that is AI, and when we do it we'd better know how to not fuck it up"). The fact that the godlike intelligence is likely to be an AI is almost inconsequential to the core of the work (as far as I can tell), but he isn't willfully ignorant about developments in AI. He might not be in "the club" of AI researchers, but his work is dependent on the field.

    And crucially, you don't have to have an academic background to be a philosopher. But also crucially, most philosophy is ridiculous and useless. It's a fine line to walk. On utilitarian grounds, I would say it's better than not to have *someone* thinking about this problem, and Yudkowsky seems intelligent enough to put some actual creative thinking into it. There are a lot of other existential risks out there, though, and balancing resources between them intelligently is difficult. On the whole, I would rather donate to the old standard Effective Altruism causes, like cheap long-lasting mosquito nets to prevent malaria, but I don't think it's a bad thing that MIRI exists.

    One reason people have cultish vibes from some of his writings is because the idea of the big, shining Singularity with a capital S smacks of a pro-science atheist version of a doomsday cult. And he is definitely a charismatic writer, judging by the fervent following he has gained in the communities he founded. I would argue against him being a true cult leader based on the lack of separation rhetoric. As far as I know, Yudkowsky does not want his followers to separate from the rest of the world and become completely reliant on his supposed "cult". He's more like Ayn Rand: a charismatic writer who speaks to and is believed by a certain sort of person.

    I read at some point that his ulterior motive for HPMOR was to attract that particular sort of person and get their help on his AI alignment project, but I don't think it was particularly successful. BUT if his writings have inspired people to try to be smarter, and to think more deeply about the world, that's at least a better track record than someone like Ayn Rand.

    Bottom line, I don't worship the guy, but I appreciate him for what he is and what he's trying to do. I also do not agree with the modern academic system, and do not think it is the end-all-be-all of qualification, so I am biased in that regard.
    ```

---

