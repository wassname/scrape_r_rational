## [Q] Where would I find the best known good AI Utility Functions?

### Post:

I've been doing some story planning/world building and the recent self-post 'Really Bad AI Utility Functions' made me wonder, what is the best known set of 'good' utility functions? (From a friendly AI perspective)

I expect the research community is structured similarly to the crypto community, in that approaches are publicly published, scrutinised and weaknesses that are discovered are identified, so that they can be improved on.

So pardon my ignorance, but is there a canonical place where this does happen? I'd love to do some reading into this area, so I can use it to better inform my writing.

### Comments:

- u/Empiricist_or_not:
  ```
  I'm not all the way up to speed on this academically, but I think we are a ways of from there yet.  I've got a way to go in my own professional work before I can start looking in this direction.  I would recommend Yudkwski's interesting, but not peer reviewed, and a bit fluffy papers on the topic as good entry points:

  General intelligence and seed AI  (which I can't find a copy of ATM, so will not be re-posting mine)

  [Creating Friendly AI 1.0:
  The Analysis and Design of
  Benevolent Goal Architectures](https://intelligence.org/files/CFAI.pdf)


  In more general terms you've got some gross conceptual errors from fiction if you think a utility function will be in human readable terms.   How will the AI define "human" after all?  How will it define "life"?  Or lets just get to the scary one, how will it define "good?"

  To use a politically spidery hand grenade, if an AI has some value that collaborates to promoting the survival of each individual within it's power to affect,(without driving it mad), what will it's actions be in the domains of abortion, capital punishment, suicide, hospice care, and do not resuscitate orders?  All of which will depend on it's conceptual definitions, and humanity has some interesting disagreements on these edge cases as it is.
  ```

- u/ArgentStonecutter:
  ```
  "Maximizing human values with friendship and ponies" is literally the least worst I've seen. And it's not good.

  Look, we can't come up with a definition of a machine gun that humans can't subvert, so trying to constrain an AI smarter than humans?
  ```

  - u/justanotherlaw:
    ```
    The "human values" part is the tricky part of the AI utility function. Honestly, if you could specify that, you could just specify "maximize human values" and be done with it. :)
    ```

- u/None:
  ```
  I actually had a really, really, *really* long post on this almost entirely typed up... and then a keyboard slip made my browser go "Back".  FFFFFFFFFFFFFFFFUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU

  The easy TL;DR is, "A computational implementation of Railton's *Moral Realism*", but that's not necessarily supported by everyone, because it's only one level less hand-wavy than trying to directly specify a code of ethics in English words, and only two levels less hand-wavy than "Pick something nice-sounding, throw it at a Magic Genie, and hope things come out well".

  So here's a completely bullshit theory that's *sorta* based on reading some stuff Nate (/u/So8res on LW) wrote, and *sorta* based on my own studies, and *actually* needs *several metric fucktons* more evidence behind it before anyone should put serious stock in it.  But it's a start?

  We think that the human mind learns big, recursive hierarchies of models of the world in order to function.  As in, you'd be surprised how many "layers" of models are needed to just understand and apply basic arithmetic; you are a *ludicrously* deep, well-trained neural net, by the standards of our current science of neural networks.  Each of these models will have some variables about it called "features".  Some of these models, call them concepts since Nate's writing agrees with my reading there, are "feature-governed" concepts, like "Santa Claus" (a *specific combination* of appearance, sound, and texture are necessary to make an object be Santa Claus).  Others are more sophisticated: "causal role" concepts defined by what the object thus classified causes to happen.  Even seemingly simple things like "uncle" can be role-governed, in the sense that while yes, an object does have to be a *male human* to be your uncle, it also has to be *your parent's brother*; "uncleness" is a *relationship* involving three different objects.  These concepts are harder to learn, but human minds do tend to form them once we've got sufficiently much training data and a vocabulary of feature-governed concepts to bootstrap relationships between.

  Well, according to the Nate article I remember reading, the human mind learns not only perceptual features and causal structure, but *evaluative* features -- things about the modelled pieces of reality that can be rewarding or punishing for the human agent.  The mind then does not make choices in order to maximize expected reward as a causal function of the world-state - which would be computationally intractable since the mind rarely knows the real causal structure of the world in sufficient detail to maximize reward - but instead to maximize expected reward as a function of the evaluative features, which thus function as variables-correlated-with-reward.

  Of course, in actuality, there may be multiple "reward" variables, and we distinctly care not only about the evaluative features, but about the process for learning them.  We've managed to vaguely hypothesize such a thing as "human preferences", but not yet to talk about "Under full information and full reflective rationality", let alone talk about such utilities for massive numbers of people in ways that include the relationships between those people and thus capture *socially rational* evaluation (ie: the relationships between members of an in-group and each-other, the relationships between members of an in-group and the abstracted group identity or goals as a whole, in-groups versus out-groups, etc.).  Or we can bullshit ourselves and say, yeah, socially rational evaluation is just evaluative features of the human mind's models of social relationships, but that again involves knowing roughly how the human mind is modelling the world, especially as applied to a special category where special-purpose social cognition kicks in instead of all-purpose causal modelling.  But the bullshit theory would be ever-so-elegant if it were true.  Alas: I would need a lot more reading and some actual professional would probably have to run a bunch of experiments, with well-developed alternative hypotheses and decades of cognitive-psychology literature under their belt, to treat this seriously.

  So how do we address "full information"?  Well, that's just a matter of "porting" the human evaluative features from the human world-models (and person-models) over to the AI's (presumably more accurate) world-models, and then making damn sure the AI's models are genuinely more accurate.  That "porting", though, is a massive ball of unsolved transfer-learning problems.  The upside is that this kind of transfer learning (translating features and parameter values from one model to another, when both models capture the same objective phenomenon at different levels) is a can of worms you more-or-less *have to* open in order to get a software learner that can think about its environment in a reductionistic, scientific way when necessary, while remaining tractable for its own scale of environment when not necessary.  At least, to my knowledge it is.  There's also no general-case guarantee, short of requiring the evaluative-feature functions over model-states (settings for the model's non-observable variables) to be cheaply invertible, that we *can* translate back from evaluative features to model-states to other-model-states to "port" features from one model to another.  But it's at least a stab at "full information".

  Ok, now how to talk about "full rationality"?  That's a biiiiiiig can of worms, and not just because "rationality" is a normatively-loaded term in common discourse.  We can say "reflective equilibrium", the state of having resolved all conflicts among one's merely factual beliefs, and that reduces it one step, but it only addresses factual beliefs.  Presumably, if we have some way to port evaluative features while maintaining their relationship to the original reward levels, we'll have some way to "do the arithmetic" on conflicts between evaluative features (since some will be negative, representing "neg-reward" or "punishment", since AFAIK, the brain has "good stuff" and "bad stuff" in separate neurotransmitters and quantities, rather than on one real-number line like economists enjoy pretending).  But then we need some way to talk about the causal roles and valuable causal relationships *between* the environment and the human agent.  A naive value-learning algorithm might accidentally learn, "Find a causal path that maximizes the human's reward signal and does that", and this will be something like wireheading or some other drugging.  A slightly less naive one might learn, "Find the causal paths that maximize the human's learned evaluative features, and do that", and if this doesn't take the causal relationship between the human and the environment into account, it will be a Lotus Eater Machine.  You need some way to learn evaluative features *of the two-way relationship between the human and the environment*, so that you can separately capture preference-concepts like "freedom" (from having some external force optimize the human's choices in ways they didn't deliberately cause) or "meaningfulness" (in the sense of having causal access to as much of reality as possible, rather than being "trapped", knowingly or unknowingly, or simply being unable to affect one's environment) or "a bit of $YOUR_FAVORITE_WEAK_DRUG is actually ok sometimes" (because sure it *slightly* wireheads the human, but even its long-term effects are balanced out by their remaining desires for other things).

  Once you've figured out a remotely sane way to talk about that human-environment causal relation, and in fact about the past-present-future human causal relation, such that you can evaluate prospects like "Should I take up an addictive but pleasurable drug?" or "Should I rewrite my basic emotional cognition to have a higher baseline happiness?", *then* you can *maybe* even *begin* to talk about, "Human preferences under full information and full [reflective] rationality", and attempt to build a proper "Do What I Mean" agent whose judgements you'll be able to *trust*.

  And then there are doubtless endless weaknesses I haven't managed to think of, because it's late and I'm tired.  Oh, and this whole thing is probably built on utter sand, since I haven't read *nearly* as many papers on evaluative cognition as I'd like.  Such papers *do* exist, though, including papers on the basics of "morality" as a kind of social cognition.  So it's not as if the material isn't out there for the professionals to go through and use.

  **TL;DR: Ask /u/xamueljones, as he actually studies human cognition and thus might actually know something where the rest of us are just building castles in the clouds for the fun of speculation.**
  ```

  - u/alexanderwales:
    ```
    If you use Chrome, you might have an interest in installing the ["Lazarus"](https://chrome.google.com/webstore/detail/lazarus-form-recovery/loljledaigphbcpfhfmgopdkppkifgno?hl=en) plug-in, which puts a little Ankh in the upper right-hand corner of text fields and saves as you type. It basically eliminated the "crap I just typed all that up and then lost it all" thing for me. Most of the time I don't notice it, but it's exceptionally nice to have when I need it.
    ```

- u/MugaSofer:
  ```
  There are no known good utility functions.

  Eliezer, who founded the Machine Intelligence Research Institute IIRC, wrote up [this](http://intelligence.org/files/CEV.pdf); but that's more of a *definition* of "a good utility function" than an *example*, and it's not considered that important for practical purposes.

  I believe most research in the area these days is more into keeping goals *stable*, dealing with self-modification, that sort of thing. With a vague eye toward some way of putting in [safeguards](http://lesswrong.com/lw/v1/ethical_injunctions/) that an AI wouldn't *want* to work around; ways of having the AI shut down a plan if you don't like it that don't result in the AI just not telling you it's plans, that sort of thing.

  If you want to see the *papers*, a lot of them deal with "tiling agents", and I can't understand a word of them beyond that point.
  ```

  - u/None:
    ```
    Yudkowsky even discouraged people to talk about utopias because it's such a fun subject to argue about and you can waste a lot of time doing it. And whatever suggestions you may have will probably turn out to be useless later on and trying to guess what is good for humans is really hard to do in advance. Trying to work on stable goal-keeping and how to align AI's values with humans is probably much more fruitful when you are trying to do it years before the actual implementation.
    ```

  - u/folconred:
    ```
    Thank you, I'll certainly read through those. Also thank you for referencing "tiling agents", [found this](http://lesswrong.com/lw/jca/walkthrough_of_the_tiling_agents_for/), which is a starting point.

    There aren't any good ideas of approaches that if well refined might lead to a "good" utility function? Not even a roadmap?
    ```

    - u/PeridexisErrant:
      ```
      None that are worth the risk of attempting implementation, no.

      Imagine cavemen studying chemistry:  we're pretty sure that things are made of smaller things and this is important - but that's about it.
      ```

      - u/None:
        ```
        > Imagine cavemen studying chemistry:

        It's not nearly that bad.  We do actually have professionals capable of addressing the issue competently; it's just that they're currently spread across disciplines and not necessarily aiming to solve "the FAI problem".  Only recently has that come to be considered a problem that we need to address decades before "the AGI problem" gets solved, and there are still contentious disagreements about whether more knowledge of "the AGI problem" helps or hurts "the FAI problem".
        ```

- u/justanotherlaw:
  ```
  Like most people on the thread have said, there are no known "good" utility functions, and it seems extremely unlikely that we can hand code a "good" utility function without messing it up. It's at least as hard to code a utility function as it is to manually code into a computer the distinguishing feature of pictures that contain cats, that is to say, it is basically impossible. 

  Most serious proposals seem to involve the AI learning a utility function from humans; the canonical one is Yudkowsky's Coherent Extrapolated Volition. Drawing on the cat example, we can get systems to recognize cat images through learning algorithms. The main problems in FAI research right now seem to be A) how to make an AI that actually coherently executes the goals it has, even if through self-modification, B) how to make an AI that's able to learn human values even through all the incoherent choices we make, and C) how to make an AI that is willing to cooperate with its human operators when they try to change its utility function (for example, to fix a mistake).
  ```

  - u/Transfuturist:
    ```
    I don't believe CEV has an actual coherent definition from composition of individual utility functions, so the closest proposal we actually have is indirect normativity.
    ```

- u/MadScientist14159:
  ```
  "Maximise your own friendliness towards us."

  Since we don't know how to code that, however...
  ```

- u/LiteralHeadCannon:
  ```
  Have you tried "minimize tiling"?
  ```

- u/TimTravel:
  ```
  Are there any known good ones (or at least known-not-terrible ones), or just known-to-be-bad ones and unknown-if-bad-or-good ones?
  ```

---

