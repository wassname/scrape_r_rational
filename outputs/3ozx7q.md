## [D] Friday Off-Topic Thread

### Post:

Welcome to the Friday Off-Topic Thread! Is there something that you want to talk about with /r/rational, but which isn't rational fiction, or doesn't otherwise belong as a top-level post? This is the place to post it. The idea is that while reddit is a large place, with lots of special little niches, sometimes you just want to talk with a certain group of people about certain sorts of things that aren't related to why you're all here. It's totally understandable that you might want to talk about Japanese game shows with /r/rational instead of going over to /r/japanesegameshows, but it's hopefully also understandable that this isn't really the place for that sort of thing.

So do you want to talk about how your life has been going? Non-rational and/or non-fictional stuff you've been reading? The recent album from your favourite German pop singer? The politics of Southern India? The sexual preferences of the chairman of the Ukrainian soccer league? Different ways to plot meteorological data? The cost of living in Portugal? Corner cases for siteswap notation? All these things and more could possibly be found in the comments below!


### Comments:

- u/ulyssessword:
  ```
  I've been trying to find/make an intuitive way to describe relativistic speeds, and I've come to the conclusion that it's hard to do, and everything has tradeoffs because our intuitions don't line up with reality very well.  That being said, the best system I came up with is a set of units I call the "Light" (and I need a better name for it) 1 Light is defined as "The speed at which an object has 3*10^8 as much momentum as it would have at 1m/s."  

  This has the advantage that you can simply add numbers together to see how fast something is going.  For example, let's say there's a spaceship traveling at 0.5 Lights (~0.45c) relative to a planet.  It shoots a fighter-drone out of its front at 0.5 Lights, which then shoots a railgun round out of its front at 0.5 Lights.  How fast is the railgun round going relative to the planet? 0.5+0.5+0.5=1.5 Lights (=~0.832c)

  I used [this website](http://hyperphysics.phy-astr.gsu.edu/hbase/relativ/relmom.html) for the numbers.  (enter 9.99999999999*10^-1 for mass, and whatever you want for momentum, then look at the velocity at the top)

   - 0.5 Lights = 0.45c
   - 1L = 0.71c
   - 1.5L = 0.832c
   - 2L = 0.895c
   - 3L = 0.949c
   - 4L = 0.970c
   - 5L = 0.980c
   - 10L = 0.995c
   - 20L = 0.99875c
   - 50L = 0.999800c
   - 100L = 0.999950c
   - 1000L = 0.999999501c
  ```

  - u/Anakiri:
    ```
    You want [rapidity](https://en.wikipedia.org/wiki/Rapidity), the inverse hyperbolic tangent of a fraction of the speed of light, with the symbol φ. You can convert between it and velocity/c with one button on a decent calculator. It's approximately logarithmic, so your rapidity is pretty close to your number of nines.

    * φ = 0.01; v = tanh(0.01) = 0.01c
    * φ = 0.5; v = tanh(0.5) = 0.46c
    * φ = 1; v = 0.76c
    * φ = 1.5; v = 0.91c
    * φ = 2; v = 0.96c
    * φ = 5; v = 0.9999c
    * φ = 10; v = 0.999999996c

    It has the useful property that you can add with it, like you want.

    * v1 = 0.5c
    * v2 = v1 + v1
    * v2 = (0.5 + 0.5) / (1 + (0.5*0.5)) c
    * v2 = 0.8c



    * v1 = 0.5c
    * φ1 = arctanh(0.5) = 0.55
    * φ2 = φ1 + φ1
    * φ2 = 0.55 + 0.55 = 1.10
    * v2 = tanh(1.10) = 0.8c

    Rapidity has another fun property: The hyperbolic cosine of your rapidity is your lorentz factor for length contraction and time dilation. So, by using rapidity, you can calculate the lorentz factor for any velocity by pressing two buttons on your calculator.

    * v = 0.6c
    * γ = 1/sqrt(1 - 0.6^(2)) = 1.25



    * v = 0.6c
    * φ = arctanh(0.6) = 0.693
    * γ = cosh(0.693) = 1.25
    ```

  - u/Transfuturist:
    ```
    I believe you have rediscovered logarithmic scaling. That's how I would approach it. Although I would want to make the unit speed 0.5c. It is the only actual Schelling point involved, I would think.

    As for names, call it subwarps, or sublights. (Please note that a unit of 0.5c would better be described as semilights, and that people in your setting could go around talking about how big each ship's semi is.)

    [Proper velocity,](https://en.wikipedia.org/wiki/Proper_velocity) or celerity, is an option. However, the problem you're trying to solve already has been. It's called [Einstein velocity addition.](http://hyperphysics.phy-astr.gsu.edu/hbase/relativ/einvel2.html) For your railgun addition problem, input 0.45 and 0.45 into the relativistic projectile calculator (and then add that to another 0.45). Your projectile is actually going about 0.90c relative to the planet.
    ```

- u/alexanderwales:
  ```
  This is mildly on-topic (since it's been about writing fiction) but I really wish that there were a better way of getting metrics for the written word. As an author, the best way that I can measure productivity is by "words per day" ... but this is about as helpful of a measurement as "lines of code per day" is for a software engineer. (I have been under managers who seemed to be of the opinion that cleaning 500 lines of code down to 50 represented negative velocity.)

  There are two reasons that this comes to mind. The first is that I just finished up a book (minus a few tangential bits) and wanted to see how well I kept my pace. The second is that National Novel Writing Month starts in about two weeks. NaNo pushes word count hard, which is one of the things that's begun to annoy me about it; once you set word count as the one and only goal, that's what everyone focuses on to the detriment of everything else. You start getting advice like "well, if you don't know where things are going, just have someone come in shooting!" which is decent for getting more words in place but terrible for writing something that anyone would want to read.

  I'm left wondering whether there's a better way to qualify authorial output. Reviews are probably one way, if you could get enough of them, but that assumes that you can even get *one* person to read what you've written, which can by itself be difficult. You could maybe make a new metric that takes into account word choice, integrating the Fleisch-Kinkaid Grade Level or Reading Ease Score, but that follows the same problem of having a metric that's not really indicative of quality, only this time instead of *quantity* we'd be emphasizing *complexity*. Anytime you introduce a metric that doesn't precisely measure what you want, you risk shooting for the thing that's being measured rather than the original goal.

  What I'd really like (and what I'd try to write if I thought it was remotely possible using existing linguistics libraries, which I don't think it is) is a computer program that would at least look for things like Characterization or Plot or Setting. I *don't* think doing this is a problem you'd need general AI for, at least if all you wanted was an actually-useful result, but I do think it's complex enough that it's a great deal of man-hours away (and beyond my programming and linguistics skills, which are only at a bachelor's level).
  ```

  - u/LiteralHeadCannon:
    ```
    >(I have been under managers who seemed to be of the opinion that cleaning 500 lines of code down to 50 represented negative velocity.)

    I'm not even an experienced programmer and this is insane.
    ```

    - u/alexanderwales:
      ```
      I work in consulting, so I've had a lot of managers, which means a fair amount of exposure to *bad* managers. You tend to get problems like this when you have managers that don't understand code. The manager needs to have some way of measuring progress, so he has to latch onto *something* in order to make sure that progress is being made. There are a lot of easy numerical things in programming which aren't representative of actually making the program do what's in the business requirements.

      So some idiot manager gets it into his head that programmers produce code, which can be measured in lines. This is true, but it's not too helpful. Because the idiot manager thinks that lines of code are the *one true way* of measuring progress, he doesn't understand that sometimes *removing* lines of code can *also* be progress. Which is sort of like someone thinking that lowering word count is the opposite of progress when writing a book instead of a crucial part of editing. The real problem with the idiot manager, aside from his idiot method of measuring progress, is that even if you explain what you did and why it was good, he basically just has to trust that you're right about what you did and why, since he has no way of checking it himself.

      So yes, it's insane, but the idiot manager doesn't know enough to know that it's insane. It just looks perfectly reasonable to him, because all he can look at are the metrics.
      ```

      - u/LiteralHeadCannon:
        ```
        I seriously can't code for shit and it still boggles my mind that someone would be incapable of understanding that less code doing the same thing is an objective improvement.  The length of a piece of software is equivalent to the *weight* of a piece of hardware, and a programmer is equivalent to an engineer, not a factory worker.
        ```

        - u/PeridexisErrant:
          ```
          > less code doing the same thing is an objective improvement.

          To make things worse, this isn't always true either!  You'd want to think about how easy it is to understand and change later, adjust for the probability that this will be required, and so on.  I often prefer a longer, more explicit program that is clearly correct to a short and optimized one I don't understand without significant work.

          Then there's the problem of execution *outcomes* (what objective the code achieves when [compiled and] run), execution *properties* (time, RAM, etc), and all the other messy non-execution stuff is not fungible!  So you have to understand that "what the code does" is not only the movement of bytes in silicon, but also it's influence on human systems.
          ```

        - u/MugaSofer:
          ```
          Now I'm reminded of that Soviet Union tale of the factory that, having had it's quota declared to be "1,000 lbs of screws", devoted all their efforts to making a single massive screw weighting 1000lbs.
          ```

    - u/blazinghand:
      ```
      This happens a lot more than you think in a lot of fields. A lot of times, metrics are chosen because they can be measured, rather than because they actually correspond to something useful. I'm reminded of an example from an [SSC article on communism](http://slatestarcodex.com/2014/09/24/book-review-red-plenty/):

      >A tire factory had been assigned a tire-making machine that could make 100,000 tires a year, but the government had gotten confused and assigned them a production quota of 150,000 tires a year. The factory leaders were stuck, because if they tried to correct the government they would look like they were challenging their superiors and get in trouble, but if they failed to meet the impossible quota, they would all get demoted and their careers would come to an end. They learned that the tire-making-machine-making company had recently invented a new model that really could make 150,000 tires a year. In the spirit of Chen Sheng, they decided that since the penalty for missing their quota was something terrible and the penalty for sabotage was also something terrible, they might as well take their chances and destroy their own machinery in the hopes the government sent them the new improved machine as a replacement. To their delight, the government believed their story about an “accident” and allotted them a new tire-making machine. However, the tire-making-machine-making company had decided to cancel production of their new model. You see, the new model, although more powerful, weighed less than the old machine, and the government was measuring their production by kilogram of machine. So it was easier for them to just continue making the old less powerful machine. The tire factory was allocated another machine that could only make 100,000 tires a year and was back in the same quandary they’d started with.
      ```

      - u/alexanderwales:
        ```
        The problem of metrification also explains a number of problems in the current American educational system. Bubble tests are super easy and relatively cheap, so we use them to measure whether students have learned anything (and consequently, whether teachers have done their jobs).
        ```

  - u/eaglejarl:
    ```
    > The second is that National Novel Writing Month starts in about two weeks. NaNo pushes word count hard, which is one of the things that's begun to annoy me about it; once you set word count as the one and only goal, that's what everyone focuses on to the detriment of everything else. 

    The point of NaNoWriMo is to get people to complete the draft.  The biggest hurdle most new writers have is that they don't finish the project -- they either just abandon it, or they keep polishing and polishing instead of writing.  NaNoWriMo says "write it first, edit it later."
    ```

    - u/alexanderwales:
      ```
      The problem is that there's a lot of shitty advice floating around which emphasizes word count over having a usable draft. Advice like:

      * If you're stuck, switch viewpoints to a new character
      * If you're stuck, have someone enter the room with a gun
      * If you're stuck, skip ahead to the next thing you know happens
      * If you're stuck, write out a dream sequence

      And these are all great pieces of advice for meeting that 1,667 word per day target, but they're *terrible* for actually producing a draft. Worse, advice like that helps to train in bad habits. But if you chime in on the NaNo boards to say, "We can't just sacrifice quality entirely, and if you just introduce new plots while forgetting the old ones, you're not any better off than if you'd just dropped one story and began another" then people give you the stink eye.

      This will be my fifth year doing NaNo. I do like the concept of getting things out there. I just feel like there's a segment of it that just so of revels in word count and word count alone. People will post things like "here's my great strategy for padding word count" and it just goes unremarked on even though padding word count with filler does nothing more than creating more work in editing while not actually accomplishing anything that gets the text closer to being a first draft.

      I do understand the point of NaNo, I just think that focusing solely on word count can severely undercut it.
      ```

      - u/eaglejarl:
        ```
        > I do understand the point of NaNo, I just think that focusing solely on word count can severely undercut it.

        Sure, no argument; there are definitely people over-focusing on word count.  I would say that's on the people, though. They've lost track of the fact that the goal is (should be) to write a *good* novel. NaNo could maybe do more to remind people of that, but it's still ultimately on the writer to care about quality, with NaNo there to help provide motivation.
        ```

      - u/Farmerbob1:
        ```
        I tend to agree with you on a personal level, but a lot of writers who are successful generate a lot of scenes that never get used.  They free write and then come back later and pick and choose what they want to keep.  For free-writing authors, having the guy enter the room with a gun is just to get things moving.  It might never make it into the final cut.

        Personally, I do not do this much.  When I write a scene, it generally stays in the story, though it might get altered significantly.
        ```

        - u/Transfuturist:
          ```
          > For free-writing authors, having the guy enter the room with a gun is just to get things moving. It might never make it into the final cut.

          I'm pretty sure NaNo actively discourages letting this stuff in. They have two months in January and February for editing and revising, IIRC.
          ```

  - u/GaBeRockKing:
    ```
    try using SMBC's filler-finding method- just count up the nouns. Generally speaking, the more nouns you have, the more things are happening (As more subjects are involved.) On its own this won't produce much useful data, but you can compare your writing in terms of noun density to books you respect to see if you're in the same ballpark. It'll at least stop you from spending too long telling instead of showing.

    It should be codable with just a simple script and word bank.
    ```

    - u/alexanderwales:
      ```
      With due respect to /u/mrweiner, the [nurbling method](http://www.smbc-comics.com/?id=2779) of measuring complexity is a terrible one.

      There *are* ways of measuring propositional density, which seems to correlate well with information density. You'd want to pull in a parts-of-speech tagger instead of a word bank, and do some exception handling, then figure out a way to cut down on (or at least measure) redundancy.

      The idea is that a sentence like:

      > The quick brown dog jumps over the lazy fox.

      Is giving us *lots* of information which we could break down into:

      > The dog jumps over the fox.  
      > The dog was brown.  
      > The dog was quick.  
      > The fox was lazy.

      So that sentence has (at least) four propositions in it -- four discrete pieces of information. The problem with using "nurble" is that it reduces the sentence "The dog was brown" to "nurble dog nurble nurble" which doesn't preserve information.

      I'm on board with computationally measuring propositional density ([as this paper suggests](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2423207/)) but don't know that it would actually be a *useful* metric rather than an *interesting* metric.
      ```

      - u/GaBeRockKing:
        ```
        Relatively speaking, however, it's a lot less important to know

        >The dog was brown.  
        The dog was quick.  
        The fox was lazy.  

        Than to know

        >The dog jumps over the fox.

        In fact, a summary of what a reader would find most important with the sentence could merely mention that there was a fox and a dog. So what fundamentally happens in the sentence (the showing, rather than the telling) can be summed up as an interaction between the two nouns.

        Nurbling therefore isn't in any way a perfect or even optimal way to gauge text quality, but it quickly and dirtily gives an estimate of what the readers actually care about-- how often tangible things are mentioned or exist, and therefore how likely they are to interact.
        ```

  - u/Farmerbob1:
    ```
    For most people, the primary problem for fiction writing is word count.  An experienced, successful writer is doing work a LOT like a coder does.  Scenes are modules.  Everything is put together in this way or that to make a story as opposed to a compiled project.

    That said, writing variables are a lot more slippery than coding variables, and code is far more exact than writing.

    [Chandler's Law](http://tvtropes.org/pmwiki/pmwiki.php/Main/ChandlersLaw) isn't that bad because if your lead is doing things to make them enemies, it's entirely plausible for enemies to attack them.

    As for a program to recognize plot, characterization, setting...  I would say that this would need something very close to a general AI, unless you are talking about 'Tip & Spot' children's books.
    ```

- u/None:
  ```
  So I want to write all this fanfiction because my brain hates being productive but I don't have time to write them all SO if I had to write one it would be [one of these three](http://goo.gl/CC8sUY) vote for one.

  Also, anyone want to volunteer to be a beta reader for whatever ends up happening? Then it'll almost feel like I'm producing content on a schedule for an audience and not just wasting my time with ridiculous crap. ;_;
  ```

  - u/None:
    ```
    You were drunk when you wrote that poll, right?
    ```

    - u/None:
      ```
      Just one of many ways my writing is often compared to Hemingway's.
      ```

  - u/alexanderwales:
    ```
    Reddit hates link shorteners (and there's little reason to use them on reddit anyway). I rescued this comment from the spam can.
    ```

    - u/None:
      ```
      Thaaaaanks. *internet hug*
      ```

- u/None:
  ```
  [AS IT WAS PROMISED, SO MUST IT BE.](http://imgur.com/a/5LH1i)  Graphs have been produced.
  ```

  - u/FuguofAnotherWorld:
    ```
    So, uh, what exactly am I looking at here? Because I have no idea what you're graphing.
    ```

    - u/AugSphere:
      ```
      Samples from two-dimensional probability distribution by the looks of it. Different pictures demonstrate different relationships between the pair of random variables.

      EDIT: Also, /u/eaturbrainz, can I have a look at the code and then steal it for my own use?
      ```

      - u/None:
        ```
        >Samples from two-dimensional probability distribution by the looks of it. Different pictures demonstrate different relationships between the pair of random variables.

        Yep.  I finally fixed the code to "clamp"/condition on a single value for the top-level hyperparameter so that I'm actually graphing *joint likelihoods*, as I'd really wanted to test my hypothesis.

        (It's weakly confirmed, but really needs more examination since the precise details of the hypothesis aren't at all clear yet.)

        >EDIT: Also, /u/eaturbrainz[1] , can I have a look at the code and then steal it for my own use?

        Which bit?  I literally just generate some arrays via sampling and then feed them into Seaborn's `jointdist()` function to generate the graphs.
        ```

        - u/PeridexisErrant:
          ```
          > I literally just feed some arrays into Seaborn's jointdist() function to generate the graphs.

          Isn't Python wonderful?  I regularly play with other languages, but I've never found something I like more.

          (count this as another code-request though, it sounds interesting)
          ```

- u/HeirToGallifrey:
  ```
  Suppose you found that you were going to die in a set amount of time: one year. The cause of this death is absolute, and can be neither avoided nor delayed. Until your death you will experience no symptoms nor inconveniences from your condition. In exactly one year you will die immediately and painlessly.

  What do you do? Does your answer change if the timeframe is two years? Five?
  ```

  - u/alexanderwales:
    ```
    1. Tell wife.
    2. Take out gobs and gobs of life insurance.
    3. Work on leaving behind as much of a legacy as possible.
    ```

    - u/Rhamni:
      ```
      Don't forget: 4. Die with an *excellent* alibi. Life insurance providers are assholes. My aunt got diagnosed with metastasized cancer of the gall bladder a few years back and given three months to live. Insurance company tried to weasel out of paying before she was even dead, from calling up to offer a Great Deal if she changed her policy (although of course the new policy wouldn't cover any pre-existing conditions) to 'accidentally' sending her bill to the wrong address for the first time. She died after four months and they had to pay out, but they seriously tried to back out of the policy the second they found out that a customer they had had for three decades had inoperable cancer.
      ```

  - u/eaglejarl:
    ```
    Well, I know the time of my death to the second, so I can be lying on the table in the cryonics facility when the time comes.
    ```

    - u/Rhamni:
      ```
      They might not be super happy with that. I mean 'accidentally' be down the street having coffee with a representative, sure, but if you're actually *in* the building that might make some well meaning DA suspicious that they might have 'helped' ensure a smooth freeze.
      ```

      - u/eaglejarl:
        ```
        Leave a notarized will well in advance, registered with the police, saying "I have had a vision that I will die at X time and I therefore intend to be on the table."

        Of course, that may not play well with the "take out gobs of life insurance" someone proposed below, which seems like a great plan. 

        Oh, I should also be sure that my will leaves a chunk in an account for me in case I manage to come back.
        ```

- u/cthulhuraejepsen:
  ```
  Physics question:

  The gravitational strength on the ISS is something like 89% compared to the gravitational strength on the surface of the Earth. An astronaut inside the ISS is subject to 0.89g. However, they don't actually feel the effect of this because the ISS itself is accelerating "downward" at 0.89g. These effectively cancel out, so the astronaut experiences weightlessness as a consequence of perpetual freefall (same as you'd experience on the vomit comet).

  That I mostly understand.

  However, I was trying to wrap my head around the idea of a (counterfactual) object with negative gravitational mass but positive inertial mass. If you're holding onto that object on the surface of the Earth and let go, it would accelerate away from Earth at a rate of 1g, subject to air friction. But on the ISS ... my guess is that an object with negative gravitational mass would "fall" opposite the direction that the ISS was traveling. A hypothetical negative gravity apple would appear to the "floating" astronaut to be accelerating at 0.89g (or possibly 1.78g?) until eventually it hit an interior wall of the ISS, where it would stay pinned in a similar way to how a positive mass apple would stay pinned to the surface of the Earth.

  But I have no idea whether I'm working this problem out in the right way or whether what I'm imagining lines up with what physics has to say on the subject (I know that negative gravitational mass isn't really a thing, but the equations must give some sort of output if you include a minus sign on that term).

  All that aside, let's say that you're sitting at your computer one day and all of your gravitational mass suddenly has a minus sign in front of it. I would think that gravity's not really holding things together much, so you wouldn't immediately explode. If two molecules have negative gravitational mass do they repel or attract? Assume for the sake of argument that inertial mass stays the same. Are there any other effects (aside from falling towards the ceiling) that I'm missing?
  ```

  - u/Transfuturist:
    ```
    A negatively massed apple would accelerate at 1.78g (the antigravity, and then the centrifugal acceleration of the orbit), with whatever (little?) Coriolis effect there is, to the space-side wall of the ISS.

    Gravity does not hold together small objects like humans, and it does not pull together individual molecules. Magnetism, the strong force, and the weak force are ridiculously powerful compared to gravity. It's safe to say the effects would be negligible (although I wouldn't want to test this without a good theory of quantum gravity).

    Negative masses would attract each other. F = G ⋅ m_1 ⋅ m_2 / r^2  . Change one mass, and you have a repulsion. Change both, and you have an attraction. So it's really not *negative* mass, it's more like left-hand vs. right-hand mass.
    ```

    - u/cthulhuraejepsen:
      ```
      Okay, so if my story starts with:

      > One day, all humans had their gravitational mass become negative.

      Then things pretty much follow from that as I would expect? People accelerating up into the sky, landing on the ceiling if they're indoors, etc.? We *probably* don't end up with them dying for other reasons or some weird stuff I was reading on Wikipedia about infinite acceleration?

      (Appreciate the help, by the way. Physics is not my strong suit.)
      ```

      - u/Transfuturist:
        ```
        A massive (heheh) chunk of people would die, some from falling up into the sky, others then starving from being unable to go outside. Think in terms of one billion and more.

        On the dayside of the planet, people may simply be crushed from the sun's antigravity, and people watching a sunrise or sunset might be thrown sideways. It depends on the strength of the sun's gravity (this is exactly like an apple and the ISS: we don't feel the sun's gravity because we are in orbit), which I would have to calculate. On the nightside, anyone outside would definitely fall into the sky.

        The acceleration alone may be enough to kill everyone immediately, and then there's the sun's part, not to *mention* the galactic center's. You can handwave that away for the sake of the setting; after all, you already have negative mass and spontaneous human sign-swapping. However, 'infinite acceleration' is not at all a problem. Many humans would very swiftly become dead astronauts.

        Given survival of anyone inside, carports with roofs would be the only viable method of transport, and the only means of getting food. Any conceivable way of weighting yourself down or tethering yourself to terra firma would be used. Mountaineers would have an advantage. :o) The third world definitely would not. There would definitely be people surviving for months afterward, but long-term does not look good. There would probably be small pockets of people surviving for years afterward, but I would have to think harder to figure out who. Robots would become very popular, assuming research and development could continue.

        There is a story about spontaneous weird gravity, sideways gravity, posted here. It was very good.
        ```

        - u/cthulhuraejepsen:
          ```
          Oh man, I hadn't even thought about the Sun. Some quick math:

              f=g(m*m/d^2)
              f=(gravitational constant)(((mass of the sun)*(mass of a person))/(distance from the sun to the earth)^2)

          [WolframAlpha spits out the unhelpful](http://www.wolframalpha.com/input/?i=f%3D%28gravitational+constant%29%28%28%28mass+of+the+sun%29*%28mass+of+a+person%29%29%2F%28distance+from+the+sun+to+the+earth%29%5E2%29)

              f = 1.2 x 10^32 kg^2 G/au^2

          [Which turns out to be](http://www.wolframalpha.com/input/?i=1.2%C3%9710%5E32+kilogram+squared+Newtonian+gravitational+constants+per+astronomical+unit+squared&lk=1)

              0.36 N

          So that's not too troublesome, unless my math is terrible, which it might be, or my good friend Wolfram has done me wrong, which he might have.

          And yeah, lots of people die and life gets hard. But what better way to set up for a "humanity, fuck yeah" story?
          ```

          - u/None:
            ```
            On that note, I really enjoy your username
            ```

- u/IomKg:
  ```
  Random Anime Recommendation:
  If you like Horror then i recommend you try giving [Kagewani](http://myanimelist.net/anime/30524/Kagewani) a chance.
  The animation(or lack thereof) is not too impressive, but that just makes the way the director managed to make it relatively immersive -more- impressive.
  ```

- u/eaglejarl:
  ```
  In the process of writing Induction (my superhero novel) I'm dealing with a lot of characters that can apply forces or acceleration to something in an unusual way. This got me to the question "why do things have top speeds?"

  A human can accelerate at X m/s^2, but stops accelerating long before air friction would be the limiting factor. Cars ditto -- what stops your average Toyota from accelerating past ~100 mph? (That might actually be a built-in speed limiter; not sure.)

  I feel like I should know this, but I'm not coming up with an answer.
  ```

  - u/GaBeRockKing:
    ```
    At some point, the force provided by the engine becomes equal to the  force of the various frictions (air friction, friction between the road and the car wheels, friction between internal components, friction between axles and the rest of the car, etc.)

    Plus, at high speeds, cars not built to tolerate those speeds will begin to vibrate as their internals shake, and that slows them down more as energy is transformed into oscillation.
    ```

  - u/_stoodfarback:
    ```
    Thinking of a running human, we can simplify to:

    1. Push off ground with one foot.
    2. While that foot is not in contact with the ground, move it forward.
    3. When it makes contact with the ground, push again.

    So, the foot needs to be moved forward before it makes contact with the ground. As you get moving faster, you have less time to do this.

    If you image running in lower gravity, pushing off will cause you to spend more time in the air, giving you more time to move the foot forward, increasing top speed.

    (This is conjecture).

    EDIT: Another limit: The foot can only stay in contact with the ground for a limited amount of time, during which the push needs to happen. As you go faster, time of contact decreases. If you're moving at 1000mph, and have a stride of one meter, your foot will only be in contact with the ground for 2.2ms.
    ```

    - u/eaglejarl:
      ```
      So, basically, the limit becomes muscle contraction speed. Okay, makes sense. 

      Honestly, I feel stupid for asking this question, but I was coming up blank on where the opposing forces were coming from. I figured it was air resistance for planes, but the others I didn't know.
      ```

  - u/STL:
    ```
    I believe it's engine (and drivetrain) friction, plus material limits. I don't know anything about cars, but I do know about physics. A car is not a rocket, where only air resistance and rolling resistance would need to be analyzed. The engine is pushing the car, and there are losses inside of the engine. Those losses might be nonlinear, but there's another consideration - stuff can only spin so fast before breaking apart. (CDs maxed out around 50X and hard drives maxed out at 15K, although the latter wasn't as close to material limits.) You can change the gear ratio so that the engine doesn't have to spin as fast to turn the wheels, but then it delivers less torque, and you need a certain amount to overcome the air/rolling resistance, much less to accelerate.
    ```

---

