## A Closer Look at Time Travel and Probability

### Post:

_Abstract_ — I discuss several models for assigning probability to timelines under the assumption that time travel is possible, but paradoxes are absolutely impossible, as is the case in many fictional worlds.  The models are mathematically precise, and illuminate issues that have previously confused many people about what sort of timelines are "most likely".  I discuss an example due to /u/TimTravel in a old post on /r/HPMOR, then analyse whether time travel can be used to solve the halting problem.  I outline how timeline probability may interact with physical probabilities, often used to justify physics "conspiring" or contriving a certain outcome to prevent paradox.

Total length: ~5000 words, or about 15-20 minutes of reading.

Edit: commenters have pointed out similarities between this and the Ted Chiang story, _[What's Expected of Us](https://www.nature.com/articles/436150a)_.  The similarity was not intentional, but is undeniable.

**Note**: The text of this post has been revised in response to objections, and some commenters may be reacting to the initial version of my arguments.

--- 

##### Contents

- Introduction
  - Model A: Path Realism
  - Model B: Local Branch Realism
  - Model C: Reroll Realism (or, Bayesian Branch Realism)
  - Model D: Weighted Branch Realism
  - Which Model is Best?
- Example: The Time Thief Puzzle
  - Alice and Bob
  - Interlude: TIME FORCE
  - Back to Alice and Bob
- Example: Hypercomputers?
- Applications to More Permissive Time Travel Schemes
  - Bound Time Travel
  - Free Time Travel
- Conclusion

---

#### Introduction

Let's say you're walking down the street one day when a wizard appears in a clap of thunder, and places a strange gray device of buttons and switches into your hands.

You're looking down at it, struggling to make heads or tails of it, and then you look up and the wizard is gone.

At the top of the device, there is a slider, already set to the leftmost extreme.  Below it, two switches: a power switch already set to `ON`, and an stiff, unlabeled switch, the exact gray of the surface, rising so inconspicuously low off the surface you almost miss it.  Below _that_, two LED buttons, both inactive.  

Suddenly, the left LED glows blue.  Confused, you press the button (it goes in with a satisfying click) and the light flashes off instantly.

Furrowing your brow, you decide to press the button again.  The blue light quickly comes on while your finger's still moving, and it again winks out immediately as the button is depressed.  You try pressing the button again and again, and each time the blue light turn on, seeming to predict or anticipate the button press.

Then, the other LED button glows red.  You press it, and it turns off; several tries later, you conclude it behaves exactly the same.

You decide now to deliberately _not_ press either button, even if the lights were to shine encouragingly.  But nothing happens; neither light comes back on.  You move your finger closer to a button, determined to arrest its motion at the last possible second.  But the light doesn't come on, even when your skin is brushing the cool metal.  You forget it and press the button.  The light blinks bright blue milliseconds before you've even decided.

Now, you (_you_, dear reader, not the above character) have already read the title of this post.  This is strange device sends information backward in time.  Specifically, it sends a single bit back in time one second.

Or well, you fiddle with the slider, and notice it controls the interval; you can set it to one minute, an hour, or even a day.

All that established, it's time to test something.  "Red is heads, and blue tails," you say.  A coin from your pockets is flipping in the air until you catch it and slap it down on your wrist.

The device shines blue.  You lift your hand.  It's heads.

You push the blue button anyway, out of habit, the light flashing off.  And then it hits you: you have to commit intently to pressing the right button even when (especially when) the device is wrong.

Another test: if the device shines red again, you'll press blue.  But if it shines blue, you'll press still blue.

There's a noticeable delay before the device tentatively shines a light.

It's blue.

Call this act _forcing_.  You can force the device to be red or blue.

You try the coin flip test just a few more times.  Now, the device is always right, even if it seems to pause a random interval before shining a light.

The opposite of forcing would be _splinting_ (after 'splinterpoint').  This is, pressing the button for whichever light comes on next, with no tricks and no conditionals.  

Finally, the last thing you can do — for a broad notion of 'can' — is what we'll call _crashing_.  This is: pressing the button of whichever light _doesn't_ blink on.  It's less that you can _do_ this, and more that you can _intend_ this, and reality responds to that.

You give it a try right now: you commit to crashing if your next coin toss doesn't come up heads.

You flip the coin, anxiously watching it's path through the air, catch it, slap it down on your wrist, spend a few seconds working up the nerve and then lifting your hand.  It's tails.

You take a deep breath, and look expectantly at the device.

No light comes on.  You're waiting for a few minutes.

And then it hits you; the device isn't binary, it's _trinary_.  Sure, it can shine red or blue — but so too can it not shine at all!  And if it either light leads to paradox, why would any light come on?  The only winning move is not to play.

Is that it, then?  Are your dreams of munchkinry doomed to fail?  Was it just a coincidence that 'forcing' seemed to work earlier?

And then the red light comes on.  You grin triumphantly, with not a little dread.  You're about to destroy the universe!  Before the implications catch up to, you're flinging your hand forward, jabbing it at the device.  You don't want to lose your nerve.

You look down, and see that you missed, pressing the red button, rather than the blue like you planned.

Is this fate?  Is the world itself conspiring to prevent paradox, just like in the stories?  You want to give crashing another try, but the last thing you want is to wait those long minutes for the light to come on again.  You glare down at the device, and then you notice the second switch.  You'd almost forgotten about it.

You idly flick it, and immediately the blue light comes on.

It forces a prediction?  Maybe your plans aren't doomed.  You consider giving crashes another try, but maybe destroying the whole timeline is not worth the risk.  You decide to spare the universe, and press the blue button.

You need to understand how this device works before you can really exploit it.  And you have just the idea for another experiment.  What if you splint, and if the splint comes out blue, you force blue again, but otherwise you just splint again.  After two button presses, you turn off the device.

It's clear there are three possibilities: blue-blue, red-blue and red-red.  But which are most likely?

You run this experiment a hundred times, and keep track of the results.

Call it the double blue experiment.

There are a few ways it could turn out:

##### Model A: Path Realism

It seems that consistent timelines are the only thing that matters.  It's as if the universe has already set aside exactly the number of timelines there needs to be, and you're _already_ in a certain timeline, you just don't know which one yet.

In the double blue experiment, there are three possibilities, and every one is equally likely.  p(red,red) = p(red,blue) = p(blue,blue) = 1/3

You find it _strange_, as a follow-up experiment aptly demonstrates:

Splint once.  If it comes out blue, force blue twenty-nine times.  Otherwise, do nothing.  Turn off the device.

On the face of it, it's crazy that you can even experience the second possibility.  It's like winning the lottery half the time.  Then again, maybe it's not so crazy?  If you were to just force blue twenty-nine times, it's equally unlikely on the face of it; like flipping dozens of coins that all come up heads.

There's a weirder consequence, though.  If you splint ten times, you can see any combination of reds and blues; red-blue-blue-red-red-red-blue-red-red-red and all the others, with uniform probability.

But if you splint ten times, and _if and only if_ every splint came up blue, you splint ten _more_ times, you'll find that the first set of splints come up all blue half the time!

This is easy to reconcile with path realism.  There are 2^10 = 1024 through the ten splints.  Each is as likely as the other.

But if you commit to doing ten more splints if and only if the first set comes up all blues, then there are 2^11 = ~2048 paths down the time-tree.  If each is as likely as the other, then half of them are located under one branch!

##### Model B: Local Branch Realism

It seems that splints are basically coin tosses; it either comes up blue or it comes up red.  The exception is if one of those options always leads to paradox.  If you commit to causing paradox when the light shines blue, then it will always shine red.  If you commit to splinting then crashing when the first splint comes out blue, then the splint will similarly always shine red.

The intermediate is more interesting: if you, as in the original experiment, splint and then splint again and crash if both splints come out blue, then half the time the first splint will come out red, but if the first splint comes out blue, the next one always comes out red.  In numbers, the possibilities are p(red,red) = p(red,blue) = 1/4, and p(blue,red) = 1/2.

It's like the universe is a savescumming gamer: it saves to a slot to every time a time travel event is about to happen.  If a paradox happens, it reloads from its saves on after another, finding newest one that lets it avoid the paradox.


##### Model C: Reroll Realism (or, Bayesian Branch Realism)

Edit: a commenter pointed out that this resembles Tim's model.

You're not sure if paradoxes really don't happen.  You've looked at the numbers.  What it suggests is that, rather than avoiding paradoxes, paradoxes could simply cause the universe to restart.

The stats from the double blue experiment don't lie: p(red) = 2/3, p(blue,blue) = 1/3.

Imagine you were simulating the universe.  1/2 the time, red comes up and you're just fine.  1/2 the time, blue comes up.  1/2 the time after that (for a total of 1/4 the time), blue comes _again_, and you've got a paradox on your hands.

What if you just, restarted the universe, and hoped it didn't happen again?

Well, there's a 1/4 chance it will.  Since you have a 1/4 chance of restarting in the first place, that's 1/16 of the time you'll restart twice.  Luckily, it's getting exponentially less likely.

Looked at another way, the odds of it coming up red is the limit of the infinite sum: 1/2 + 1/4 * 1/2 + 1/16 * 1/2 + 1/64 * 1/2 + 1/256 * 1/2 ...

This series converges on 2/3.

But there's another interpretation, with seems less like the work of a lazy programmer and more like something a statistician would come up with.

Suppose, as we must, that the timeline is consistent.  What is the posterior probability of that timeline being red, given that 100% of red timelines are consistent, and 50% of blue timelines are consistent?

Or, in symbols:

    P(red | consistency) = (P(consistency | red) * P(red)) / P(consistency)
    P(red | consistency) = (1 * .5 / .75) = 2/3

Even more intuitively: you have four balls (timelines) you paint half of the balls red and half blue (splinterpoint), and you take away one blue ball (paradox).  2/3 of the remainder is red.

You'll recognize this as Bayes' Theorem.

##### Model D: Weighted Branch Realism

The reality is more subtle than you thought.  It seems that, while you've never seen a paradox, if a branch has a path through splinterpoints that ends in paradox, that fact subtracts probability from the branch and gives it to its counterfactual sibling.  This happens in Local Branch Realism too, but not to this degree: the very possibility that a time-path has a paradox however many days or years down the line always shaves _some_ degree of probability, if only just a sliver; but naturally, that sliver increases as the paradox gets closer.

Thus, the results of the experiment are: p(red, red) = p(red, blue) = 3/8, while p(blue, blue) = 1/4 = 2/8.

You can see it clearer with a more involved experiment.  Take your device and a sheet of paper and:

Splint, call this splint **A**:

  - if A is red, write "foo" on the paper
  - if A is blue, splint and call it splint **B**
    - if B is red, write "bar" on the paper
    - if B is blue, splint and call it **C**:
      - if C is red, write "baz" on the paper
      - if C is blue, crash

According to weighted branch realism, the probabilities look like: P(foo) = 20/32 = 5/8, P(bar) = 9/32, P(baz) = 3/32.

To understand this result, we have to define a notion of "static paradox fraction", or spf.  If you intend to force blue, then the spf is 1/2.  Why?  To force blue you must (intend to) cause a paradox in the event that not-blue happens.  Despite that fact that paradoxes never happen, static paradox fractions seems be a real quantity in Weighted Branch Realism.  It is as if the device is looking at every possible and impossible timeline, and measuring which ones are paradoxical.

(Note that static paradox fractions are diminuted by splints.  So if you splint and when the splint is blue you then force red, the spf of the first splint is 1/4, _even if_ there is no second splint whenever the first is red.  This distinguishes it from simply counting paradoxical timelines; 1/3 of the timelines are paradoxical, but a paradox behind a splinterpoint has lesser weight.)

Furthermore, let's have a notion of "intrinsic probability" or ip.  The ip of both splint outcomes is 1/2, _even if one of them is paradoxical_.  

Thus:

    P(C = red) = 1/2 (ip) + 1 (sibling's spf) * 1/2 (sibling's ip) = 1/2
    P(B = red) = 1/2 (ip) + 1/2 (sibling's spf) * 1/2 (sibling's ip) = 3/4
    P(A = red) = 1/2 (ip) + 1/4 (sibling's spf) * 1/2 (sibling's ip) = 5/8

To reiterate:

    p(foo) = p(A = red) = 5/8, and
    p(bar) = p(A = blue)) * p(B = red) = 3/8 * 3/4 = 18/64 = 9/32, and
    p(baz) = p(A = blue) * p(B = blue) * p(C = red) = 3/8 * 1/4 * 1 = 6 / 64 = 3/32

(Note for the pedants: normally, the ip is _actually_ 1/3, and ditto for spf; we're ignoring that the device can _not_ shine a light, because you can just flip a switch and force a light on.  Even without the switching, committing to either turning the device off, or splinting endlessly once the the experiment is over means the probability of the device choosing to not shine drops exponentially while the alternatives remain constant.)

This model is somewhat unintuitive, because despite the name, it has more in common with Path Realism than the other two \_ Branch Realisms.  You can't emulate the probability distribution of WBR by running one timeline and restarting (either from the beginning (Bayesian), or from the nearest viable alternate splint (Local)). This is entirely the fault of a phenomena we can call "paradox by association"; in the foo-bar-baz experiment, in a certain sense, just as 1/8 of quasi-timelines are paradoxical because they end in crashing, 1/4 of the quasi-timelines ending in baz are paradoxical _just because baz timelines are near to the paradox_.

This accounts for the numbers: p(foo) is 5/8, 4/8 intrinsic + 1/8 from the paradox.  p(bar) is 9/32: 8/32 intrinsic + 1/32 from baz's paradox by association.  p(baz), lastly is 3/32 owing to loosing 1/32 from paradox by association.

(Why 1/4?  Good question.  There must be a reason, and it's clear this is the number that comes out of the equations.  Alas, I'm not smart enough provide a reason in words and not symbols.)

##### Which Model is Best?

Path Realism and Local Branch Realism are both pretty wack.  Path Realism discards all local information about plausibility, and allows munchkins to blow up the probability of their favorite timelines arbitrarily high.  Local Branch Realism does the same thing from the opposite direction; wanton invocation of paradoxes intuitively _should_ be penalized, but Branch Realism simply says I don't mind.

Between Weighted Branch Realism and Reroll Realism, I'm inclined to prefer the latter.  WBR is the first I thought up, but RR is just more natural.  It has two obvious interpretations, both things that anyone would come up with after thinking about it for a little while.  WBR, in the other hand, is harder to conceptualize in terms of what mechanism would actually cause the probabilities to look like that (I've tried; the results are not pretty).  "Paradox by association", while potential a fresh concept to use in a story, is a truly strange mechanism.

Now, how does the connect with TimTravel's ideas?  Just as he proposed, it is, in some models the case that the most probable timelines are the ones in which time machines are never invented.  In Local Branch Realism, this is not true (unless some bad actor arises in _every single timeline_ and causes paradox.  Time Beast, anyone?).  In Path Realism, this is again never true without positing a Time Beast.  However in WBR and RR, it's more or less true.  In general, timelines with fewer instances of retrocausation are more likely, only because instances of retrocausation are a proxy for instances of paradox.  Now, if paradoxes are rare, this argument would be weak.  (But to be fair, most meaningful uses of time travel require copious paradox; it's the oil in the engine.)

That said, I believe it is admissible for a work to posit that the characters find themselves in the (slightly unlikely) timeline where retrocausation happens.  After that, though, the principles constrain the probability space.

#### Example: The Time Thief Puzzle

In the [somewhat flawed](https://old.reddit.com/r/HPMOR/comments/2xie39/time_travel_and_why_everyone_gets_it_wrong/) post which inspired this, /u/TimTravel outlines a paradoxical puzzle:

> Suppose Alice has a bag of money with a dollar on it. If anyone steals it, she'll go back in time and see who did it. Bob wants to steal it. He knows she has this policy. He decides he'll give himself the thumbs up just before he leaves the future if all goes well stealing it and she doesn't see him. If these policies are followed then it leads to a paradox, so something must prevent them both from simultaneously following their policies. Either Alice wins because Bob goes to the past without getting an honest thumbs up from himself or Bob wins because Bob sees the honest thumbs up and Alice doesn't go back and check who stole the money for some reason, or some third possibility prevents both.
>
> **There is no reason to think that either of them automatically wins in this situation.** Timelines in which Alice wins should be about equally frequent as timelines in which Bob wins. Numerous characters have implicitly assumed that there is a reason to think one of them automatically wins in such situations.

We'll have to change this scenario a little bit to fit with the schema we've been using so far.  (Besides, Tim's example is kind of unclear and it's not even obvious that paradox must occur in all permutations.  If Bob doesn't get the thumbs up, wouldn't he not steal?  Puzzle solved.)

##### Alice and Bob

Let's say that in the morning Alice has acquired a bag full of money from sources unknown, and has come to an arrangement with a shadowy individual: leave a dufflebag full of money with a dollar sign on it at a dropoff location, and in exchange, the individual will leave a limited print run of all eleven books of _Worth the Candle_ at the same location.

Alice knows people want to steal that money, but part of the arrangement is that she can't be there guarding it when the shadowy individual arrives.

On Tuesday morning, the deal is still in its negotiation stage, and there are two places Alice can think of to arrange for dropoffs: atop the looming mountains outside of town, or deep into the mysterious catacombs below it.  Both of these hiding places will take two hours to enter and two to leave.  (Pretend the mountains have a rogue paramilitary that shoots down helicopters or something.)

Due to work obligations, Alice can only make the dropoff in the early morning, and return that evening to pick up the books.

Meanwhile, Bob, the thief, knows all this and certainly doesn't want to get caught.  He can't go into either location until Alice has left, else he'll be seen.  Lucky for him, that leaves a large window for him to do the deed.

Both of these characters have the same magical devices from the earlier section, and they'll naturally use them to ensure success; except, for obvious reasons, we'll call their predictions "catacombs" and "mountains".

Before she goes to hide the money at 5:00 AM, Alice consults her device for where to hide it.

Four hours after he has seen Alice leave, at 9:00, Bob consults his device to determine where she hid it.  If the predict is wrong, he forces a paradox.

When Alice returns to get the money, at 17:00, if it's there, she confirms the location that the device advised.  Otherwise, she presses the opposite button, forcing a crash via paradox.

What happens?

This requires introducing yet another notion.

##### Interlude: TIME FORCE

The TIME FORCE is any one in a billion freak accident that happens 100% of the time to prevent a paradox from occurring.

TIME FORCE is a quantum fluctuation that causes right neuron to misfire which butterflies into changing your whole decision.  TIME FORCE is random air currents that causes a bird to fly by and drop a rock on the right button of the time-device.  TIME FORCE is the lightning in the clear blue sky which spells out **Do not mess with time** in typographically perfect serifs.

There are a few things we can say about TIME FORCE.

Let's say that the general odds of TIME FORCE acting on a given person in a given second is extremely, astronomically unlikely.  One in a billion, or one in a trillion sounds about right.

But from that, it follows that the odds of TIME FORCE acting over an interval of time is proportional to the length of that interval.  (It's at least monotonic.  Difficult/impossible to say how fast it grows.)

It also follows that the odds of TIME FORCE acting is increased if an agent is acting in concert with it, and decreased if they are acting in opposition, proportional to the efficacy of that agent.  I.e., an agent is defending against TIME FORCE, or attempting to utilize TIME FORCE.

(consider: if Bob, after stealing, were to proceed to try to also steal Alice's device or persuade her to cancel her prediction herself (e.g., by faking a dire emergency which requires her foreknowledge to solve), then TIME FORCE would provide some boost to the probability of success.)

An obvious corollary to all this is that TIME FORCE is almost never relevant.  If you had a bigger device that spat out 32 red/blue pairs at a time, you could predict the lottery without seriously worrying about TIME FORCE.

One common confusion which leads people to overstate the importance of TIME FORCE is the fact that parallel universes and timelines aren't necessarily the same thing.

Let's say you wanted to force a coin to come up heads.  Turn on your device.  Then, splint.  If the result was blue, flip the coin.  If the result was red, splint again.  The idea is to have the device spawn as many timelines as possible.  Pressing buttons (subtly) alters the configuration of your brain and muscles and the microcurrents of air in the room, and the hope is a certain combination of buttons at a certain rhythm is prod you into the right configuration to flip the coin heads.  This is almost certainly true in this specific example, but if the coin is flipped before the device is turned on, time cannot help you.  And if you don't have intimate control over the outcome, time cannot save you.  E.g., if a meteor is flying towards your town, forcing a paradox if it hits true cannot avert its course.  Of course, if you splint long enough, maybe the branches describe a powerful, quickly-createable, meteor-destroying technology in morse code.  Or maybe it just spells out "You needed worth opponents," and you give up and let the asteroid take you.

(There is one slight exception, and this is where the different formulations of Bayesian Branch Realism and Reroll Realism differ.  In BBR, the universe is posited to either A) know before splintering the posterior probabilities of each branch or equivalently, B) have so many timelines that destroy paradoxical ones leaves the distribution looking as it should.  However, in RR, paradoxes are posited to cause the universe to restart from the beginning (or when the device was turned on).   This means that in RR, simply flipping a coin and forcing a paradox if it's tails is all you need.  That is, assuming quantum fluctuations making the coin heads is more likely than quantum making you decide not to crash, or failing to crash.  Or dying instantly and having the wizard return to push the button.)

There's one last possibility, and that's if you posit that quantum randomness itself are biased by time travel, so each quantum measurement counts as a splinterpoint.  I'm reluctant to do such, because the edict I've heard over and over again is that when worldbuilding, Do Not Mess With Physics.

I'm going to continue writing this article with the assumption that physical randomness is not biased by timelines.  Extreme improbabilities are still extremely improbable, but, to mangle the quote, when you have eliminated the impossible, whatever remains, however improbable, must happen.

#### Back to Alice and Bob

So, with TIME FORCE in mind, what happens to Alice and Bob?

It's 4:50.  Alice is sitting beside her bag of money with a dollar sign on it, her device in front of her.  If the device shows 'catacombs', she intends to, when she returns from work, press 'mountains' in case her bag was stolen and she doesn't have her book, or otherwise she will confirm 'catacombs' (and vice versa).

She waits.  And the device doesn't say anything at all!

It's well known that sometimes there are random delays before the devices spit out answers.  Some users interpret it as an omen, suggesting that whatever you're asking is so likely to lead to paradox, time itself has to work up the nerve to allow it to happen; the theorized mechanism is 'paradox aversion', where in some models, the odds turn against timelines long before the paradox is even nigh.  (But as far as Alice knows, no one has never proved which model they live in.)

She decides to buck superstition and conjecture, and reaches out to flip the switch which forces an output.

Record scratch, freeze frame.  What happens next?

A) TIME FORCE intervenes before Alice can flip the switch.

B) Alice flips the switch, but TIME FORCE subverts the resulting prophecy.  (I.e., the bag is stolen, but events contrive to have the incorrect button on the device pressed anyway.)

C) Alice flips the switch, and TIME FORCE subverts Bob's prophecy instead, sending him to the wrong location.  Her bag is not stolen, and she happily reads the ending of WtC.

D) Alice presses the secret button, and TIME FORCE subverts _both_ prophecies.

(Stop reading now if you want to try to work out an answer yourself.)

The correct answer is B, which is about three times more likely than anything else, barring unspecified details.

A requires TIME FORCE to act in the acute interval before Alice presses the button, which is at best a few minutes long.

C requires TIME FORCE to act in the four hour interval of 9:00-13:00.

D is the conjunction of A and C, and less likely than both.

B is the winner, because it only requires the TIME FORCE to act on the long, twelve-hour interval of 5:00-17:00

I think this goes _even if_ timelines nudge physical probabilities.  Exercise for the reader, though.

(((Now, one may object that this formulation bears little resemblance to Tim's example.  My only excuse is that Tim's model was too unclear for me to formalize specifically.  When I tried, I got this scenario:

First, Alice gets a prediction from the device: stolen, or untouched.  Iff it says stolen, she waits to see who the thief is, and gets them.  Else, she goes about her day, secure knowing her money is safe.

Then, Bob consults his device as to whether his theft would be successful: if it says yes, then either 1) Alice is there, catches him, and he triggers a paradox, or 2) Alice isn't there, he gets away, and she triggers a paradox later.  However, if it says no, then he just sighs, and fucks off, no paradox to worry about.

Even if I missed something/misinterpreted TimTravel and this situation _is_ paradoxical all four ways, it still follows that Bob will probably win (if not so overwhelmingly so) because he spends less time in temporal limbo where TIME FORCE might fuck with him.)))

#### Example: Hypercomputers?

It's clear that if one were to disassemble the strange device and hook up a few wires to its circuit boards to a computer, you'd create a hybrid device capable of advanced feats of computation.  What is the exact strength of this retrocausal computer?

As mathematicians are wont to do, we will dispense with practicalities like having to use at most as much space as actually exists, or needing our computations finish before the heat death of the universe.  Given all this, if we have an idealized retrocausal computer, a la the idealized turing machine, what can we do?

Let's try the halting problem, a classic test of strength.  Say we have a computer program, and we want to know if it's ever stops running.  Well, either it does or doesn't.

Consider a slightly different device, instead of red/blue leds, it has magic screen which can display _any integer_.  (For models where it matters, the intrinsic probability of an integer n is equal to 2^(-k), where k is smallest number with 2^(k) > n and k > 0.)  It also has a numpad now, which allows the input of any integer.

With this device, to determine when a program halts, _given that it halts_, is as simple and looking at what number comes up on its screen, and running the program for that many steps.  If it halts before then, input when it halted (causing paradox).  Otherwise, input the number it gave you.  Otherwise otherwise, cause a paradox via your preferred means.

If the program might run forever, things are trickier.  What you can do is interpret the number the screen outputs as the index of a proof of (not) halting.  This isn't sufficient, however, as no computably-checkable proof system can prove that any turing machine (never) halts, essentially by definition.  But we can use the fact that if a program runs forever it doesn't halt: simply try over and over again until 1) you learn the program does not, or 2) the odds of it halting given that you found no proof is as astronomically low as satisfies you.

By construction, the odds of the screen outputing the right halting time decreases exponentially as the halting time increases.  If the halting time is in the millions, it takes a several hundred trials before you have even odds of the screen having already spat out the right answer.  If the time is in the billions, it takes several hundred thousand.

(Model-specific tricks can alleviate this quite a bit.  In Path Realism, you can use the path blowup technique to increase the probability of the correct halting time coming up.  In Weighted and Reroll, you can inflate the static paradox fraction to arbitrary heights, reducing the odds of false negatives.)

From ordinary turing machines, this is a difference in degree (retrocausal machines are better at it), but not kind (retrocausal machines can never decide whether a machine halts or doesn't).

Long story short, retrocausation can increase the efficacy of your computers, but you're still stuck at **[0](https://en.wikipedia.org/wiki/Turing_degree)**.

#### Applications to More Permissive Time Travel Models

Our device is quite limited, in the world of retrocausation.  There are at least two stronger types of models:

- Bound Time Travel: our system only sends information back in time, where most extant system allow entire persons to make the journey.  While I strongly prefer this "prophecy" scheme to proper time travel (prophecy is simpler and more physically plausible, and opens up less strange cases), the evidence suggests that's not the prevailing taste.

- Free Time Travel:  In contrast to a Primer-style system where time travel is limited to when and where a machine exists, quite a few just let you pop out at old place and time.  Again, this is not preferable to me because it doesn't allows limits to be as clear (a desirable quality for any rational system), but free time travel seems rather common.  Cf. HP Time Turners, the very things which started this discussions.

##### Bound Time Travel

It's clear how our models transfer the bound case; proper time travel is basically sending a whole bunch of information at once.  There's another hurdle though: can you tell from when a time travel comes?

With our red/blue device, the slider at the top puts an upper bound on how long the device waits for stablization.  If the system allows this, then great!  It means there's a clean cutoff point after which we know the timeline is stable or not.

Otherwise, you probably want to make probability proportional to how far in the future the traveler comes from; if you're uniformly selecting a person that could exist between now and the heat death of the universe (without grandfathering themselves, granted), it's probably not going to be you from two weeks hence, of all people.

There's a more interesting question this is avoiding though.  What can we say about what _will_ probably step out of the time machine, aside from whence it came?

Well, it's helpful to assume that there's an organization controlling and regulating time travel.  There's some failure modes that would be cripplingly common.  For instance, doppelgangers.

Temporal doppelgangers are a variation of the bootstrap paradox (i.e., self-causation), where a mutant version of your steps out of the time machine, finds current you, and forcibly alters your mind to replicate its own (anthropically, it must know how to succeed at this).

This seems pretty inevitable from the premise, and it provides a nice, fresh justification for "you can't interact with your past self".  Not out of fear that it might cause a paradox, but out of fear that it _won't_.  If your mind is randomly altered repeatedly, even by slight amounts each time, the results are quickly going to not be pretty.

Other than that, this scheme of time travel seems somewhat tractable; while the odds of any given arrangement of matter is a specific person with a specific set of memories consistent with the past and future of the extant universe is very very very low, there is some wiggle room, especially depending on the specifics of the time machine.

The assumption baked into our models is that, in effect, the time travel mechanism is plucking a random configuration of matter from possibility space.  Most arrangements of matter, even restricting to the stable ones, aren't neat blobs of protein and water.  And the most of the ones that are, are random goop!

Now, requiring that the configurations which arise in the past-time machine are exactly 1-1 equivalent to what enters the future-time machine is very tight requirement.  I doubt bodies will be too much worse for wear if a few atoms are a few picometers off.  And you can relax the requirement even further, allow what appears in the present to be "close enough" to its future equivalent, and increase the possibilities further.  Of course, this will have ramifications; cancer, prions, strange tastes in the mouth.

The organization controlling the time machines could require that everyone who walks out of a time machine undergo a medical examination, and make most crippling ailments thereby paradoxical.  (And, likewise for the dead bodies which can't walk out anyway).

##### Free Time Travel

Free Time Travel is the trickiest of all, but it has a few felicities in addition to all the extra warts.  There's not necessarily authoritative time travel device (or an immediately plausible time travel agency) that you can stick in to stealthily add in extra conditions and assert nice properties.

With FTT, a time traveler could pop up anywhere, and at any time.  Unless you add in a time agency that can monitor for new arrivals, there's nothing you can do about doppelgangers, unless you bolt 'no interacty with the past self' into the rules of the system somehow.

You probably shouldn't have location be conserved; requiring that you come out exactly where you came tightens probabilities too tightly.  Allowing leeway puffs them up a bit.  The same goes for concerns about exact molecular matching.

---

All those caveats aside, it seems as tho you can otherwise treat BTT and FTT similary to our toy examples, where they line up, showing the benefits of the simplification.

#### Conclusion

Well, that turned out **much** longer than I'd expected (or wanted).  It feels like it puttered out here at the end, but I've said everything I set out to say and then some.  

I hope this served to sharpen your intuitions regard time travel, and make precise things which were previously vague.

I would like to thank the nice people on the /r/rational discord for inspiring this line of thinking and providing the impetus to refine it.

Thank you for coming to my TED talk.

P.S.: worth mentioning that Tim [covered much of the same ground as me](https://old.reddit.com/r/HPMOR/comments/2xie39/time_travel_and_why_everyone_gets_it_wrong/) in their initial post.  My post is less a refutation to theirs than me working out my own solution to the problems they pose, as I didn't understand or believe all of their arguments.

### Comments:

- u/SilverstringstheBard:
  ```
  This is the most well thought out examination of stable time loop based time travel I've ever seen, thank you for putting all of the thought and effort into this that you did. I'm almost certainly going to be using insights from this essay thing when I include time travel in my stories. I'd also agree with your assessment of bayesian or reroll time travel making the most sense.
  ```

- u/BoxSparrow:
  ```
  Alright, lemme review this.

  First off: This is fantastic! I've been looking for a reference like this for a good while, and now here we have one. It's all very well thought out, and took me way longer than twenty minutes to get all the concepts in my head. Overall, a definite thumbs up.

  Now, for some nitpicks.

  There are some rather critical typos and ambiguous sentences in the explanation sections, namely:

  >The device flashes blue. You lift your hand. It's heads.  
  >  
  >You push the **red** button anyway, out of habit, the light flashing off.

  \*blue

  >There's a weirder consequence, though. If you splint ten times, you can see every combination of reds and blues; red-blue-blue-red-red-red-blue-red-red-red and all the others.

  Made me think that it somehow gave all the combinations at once every time. Maybe rephrase it to "you see the normal random mixture of reds and blues".

  >But if you splint ten times, and if and only if every splint came up blue, you splint ten more times, you'll find that the first set of splints come up all blue half the time!

  Also had me rereading several times until I figured out that it's not the *act* of splinting ten more times that causes it, it's the *intent*. Perhaps add "precommit that if and only if every splint..."

  >The intermediate is more interesting: if you, as in the original experiment, splint and then splint again and crash if both splints come out **red**, then half the time the first splint will come out red, but if the first splint comes out blue, the next one always comes out red.

  \*blue

  >p(foo) = p(**C** = red) = 5/8, and

  \*A

  >The correct answer is B, which is about three times more likely barring unspecified details.

  "Three times more likely **than the second most likely**"

  >**A** is the winner, because it only requires the TIME FORCE to act on the long, twelve-hour interval of 5:00-17:00

  \*B

  &#x200B;

  Next, terminology and concepts.

  One: Using "flash" as a verb for the device showing red or blue can be misleading in some situations when you actually mean "turn on and not turn off until you press the button". For example,

  >The device flashes blue. You lift your hand. It's heads.

  had me confused as to why the button only flashed and didn't stay on, until I realised that it was a problem of semantics.

  Two: Paradoxes. While it's central in your writing that there can be no paradoxes, there obviously *are* paradoxes outside of the models. For example, when first getting the device, we press the blue button because it's glowing. However, the only reason it's glowing is because we press it in the future, leading us to press it because it's glowing. Hence, paradox.

  I don't think this is a solvable issue, though, so you can probably just gloss over it. In fact, I'd argue that it's impossible for static timeline time travel to not create paradoxes. For example, when you travel to the past, you'll disrupt photons from their original path, causing a chain reaction of quantum differences that will eventually reach your current self and change you a little - maybe delaying a neutron's fire in your brain - that chaos theories itself into a macro-scale paradox. The only way to avoid that would be to spacially appear a greater distance away from your original position than light can travel in the time elapsed, and even that isn't for sure due to quantum shenanigans.

  (As an aside, I found that, rather than thinking of the device as prophetic, it was easier for me to visualise the concept by thinking of it as sending a pulse of light backwards in time whenever we press the button.)

  Three: The probability of TIME FORCE. Less of a nitpick, and more of an addendum. The chance of TF happening has to be a function of time, so it would be something like "a one in a trillion chance of happening per second" rather than just "a one in a trillion chance", since the chance of it happening in a single instant is definitionally zero.

  For the case of the relation between the time interval and probability, the chance of an event of probability P happening at least once after n tries is given by `1-(1-P)^n`. At one in a trillion per second, for the event to have a 90% chance of occurring, the time interval would be about 73 millennia. Whether or not this is rare enough for typographical lightning to form I'll leave for others to decide. And, for such a low probability per second for a time interval of only a couple dozen thousand seconds, the chance of B happening over A is indeed about three times more.

  Four: Lastly, and most importantly, I'm not convinced that Weighted Branch Realism is a thing. I do agree with the concept of redistributing paradoxed probabilities as a model, but not as you describe it. As it is now, the distribution isn't equally weighted. Looking at your example, you're taking the 1/2 chance of blue!C, splitting it in half at B, then giving one resultant 1/4 to red!B and passing the other 1/4 down to A, leaving nothing for blue!B. Now the chance has been redistributed to red!B, but not red!C. In fact, the chance of getting red!C overall is now less than it was previously, at 3/32 vs 4/32.

  An *equal* weighted distribution would be taking the new total and dividing it by the old, then multiplying each element by that ratio to get the new set of numbers. In this case, we want the chances after distribution to add up to one, up from the total of one minus the chance for the paradox element. For instance, the new probability for red!C would be `1/(1-1/8) * 1/8 = 1/7`. In fact, if we were to carry on splinting the other branches in the example, each third-order element would have a probability of 1/7 - an equal distribution. And this may seem familiar, because that's exactly what Model D is doing. It's just another version of Bayes'.

  &#x200B;

  That's some of the thoughts I had while reading this. And to reiterate the start: These are fantastic ideas, and I'm very glad you posted this. Great stuff!
  ```

  - u/endlessmoth:
    ```
    Thank you for taking the time to read and share your thoughts!

    I appreciate the typos you caught.  Clarity where clarity is due, I should mention the ones I didn't fix:

    > The device flashes blue. You lift your hand. It's heads.

    > You push the red button anyway, out of habit, the light flashing off. 


    Edit: I misread; you are right.

    ~~The prediction _is_ wrong here.  This was a deliberate choice, to illustrate that it requires concentrated intent and will.  If you aren't ironclad in your precommitment, the trick won't work, and I didn't want to gloss over that completely.  (It's plausible to me that many people could entirely fail to 'force'; either out of fear of 'ceasing to exist', or out of indecisive wills which can't ensure precommitment.)~~

    > Also had me rereading several times until I figured out that it's not the act of splinting ten more times that causes it, it's the intent. Perhaps add "precommit that if and only if every splint..."

    That's not quite it either.  "Causing" is something of a strained framing here.  In a meaningful sense, it is exactly splinting ten more times which causes it.  Specifically, what's happening here is that there's 1024 time-paths that go through that specific branch of the tree, and 1023 that don't, and thus, getting to that second batch of splints underneath the specific branch is more likely.

    Those 1024 extra paths exist _because_ you splinting ten times extra.  Now granted, you splinted ten times extra because you precommited to splinting ten times extra, so you can pass the buck there.

    That said, he most immediately plausible way to run a scheme like this is if the 2047 timelines were already pre-allocated and each one is made to instantiate a different possibility.  These timelines would exist _before_ anything actually happens.  Noting that, it would be the simulation which causes it.  Maybe it's a magical **0'** program which can statically analyse a **0** universe and determine exactly how many timepaths it will spawn.

    ---

    Those two caveats mentioned, again thank you for noting the other typos.  They've been fixed.  (I've changed positive instances of 'flash'
    (i.e. flash _on_) to 'shine'.  It's a more bit awkward, prose-wise, but I hope it's less confusing.)

    > For example, when first getting the device, we press the blue button because it's glowing. However, the only reason it's glowing is because we press it in the future, leading us to press it because it's glowing. Hence, paradox.

    It's worth distinguishing two different kinds of paradox.  For lack of better terms, let's say negative paradox and positive paradox.  Positive paradox is the sort of thing you describe.  (More generally, it has similarity to the so-called bootstrap paradox.)  Negative paradoxes, then, are what I've till now simply called paradoxes.  The distinction is that positive paradoxes permit resolution, and negative paradoxes do not.  My rule is that negative paradoxes are impossible, but positive paradoxes are just fine.

    >In fact, I'd argue that it's impossible for static timeline time travel to not create paradoxes. For example, when you travel to the past, you'll disrupt photons from their original path, causing a chain reaction of quantum differences that will eventually reach your current self and change you a little - maybe delaying a neutron's fire in your brain - that chaos theories itself into a macro-scale paradox. The only way to avoid that would be to spacially appear a greater distance away from your original position than light can travel in the time elapsed, and even that isn't for sure due to quantum shenanigans.

    This objection is vacuous.  Fixed points aren't a rare thing (in fact, the proliferation of [fix-point theorems](https://en.wikipedia.org/wiki/Fixed-point_theorem), inclines me to think it's downright inevitable. 

    Specifically, you say "when you travel to the past, you'll disrupt photons from their original path," but this isn't true.  By our very assumption, in traveling the past — _your_ past — the "disruption" isn't knocking photons _off_ their original path, it's _putting_ them on their original path, right on schedule.  The only way the notion of 'original path' as you use it makes sense is if you're conceptualizing the agent as traveling to a past which they did not exist in, which is contrary to the assumptions.  The past which they arose in must have already included their time-traveling future self, whether they were aware of it or not.  Second- and third- and nth-order effects of this meddling future-self which affect the past would be account for in the future self which arrives.

    > (As an aside, I found that, rather than thinking of the device as prophetic, it was easier for me to visualise the concept by thinking of it as sending a pulse of light backwards in time whenever we press the button.)

    Ha, I've had similar thoughts when designing my own systems.  It is easier to conceptualize that way.  I always thought there must be some sort of "time particles" to carry time-travelling information.

    > In fact, the chance of getting red!C overall is now less than it was previously, at 3/32 vs 4/32.

    Yes, this is by design.  Really, I can't speak too accurately about 'intent' (as this is something that fell out of the equations more than something I designed), but I would say the idea behind it is to model the phenomena of time "preferring" less paradoxical branches.  The reason red!C becomes less probable is in a sense to "punish" it for requiring the universe to dodge so many paradoxes.

    While I do have some appreciation for WBR, I think we have a comparable distaste for it, coming from different directions.  I so far haven't been able to think of any mechanism the WBR equations could be modelling (other than a computer blindly implementing them) where such a distribution falls out naturally.  It's a neat idea, I feel, but seems somewhat arcane and artificial.

    > That's some of the thoughts I had while reading this. And to reiterate the start: These are fantastic ideas, and I'm very glad you posted this. Great stuff!

    No problem :D.  I have to say, it really made my morning to wake up to such a positive response to my essay.

    (I may have been a little blunt in some of my replies, but I hope not too much.  I mean you no personal insult.)
    ```

- u/CreationBlues:
  ```
  You should look into PostBQP, it turns out that time travel works extremely well with quantum mechanics and gives a mechanism for how TIME FORCE works.
  ```

  - u/tjhance:
    ```
    also related: https://en.wikipedia.org/wiki/Quantum_suicide_and_immortality
    ```

- u/cthulhusleftnipple:
  ```
  > The device flashes blue. You lift your hand. It's heads.

  > You push the red button anyway, out of habit, the light flashing off. And then it hits you: you have to commit intently to pressing the right button even when (especially when) the device is wrong.

  Is this a typo?
  ```

  - u/BoxSparrow:
    ```
    Probably. Left me quite confused as well.
    ```

  - u/endlessmoth:
    ```
    Edit: I did not read the post carefully, retracted.

    ~~That was a (perhaps unnecessary, perhaps ill-advised) attempt at realism there.  I believe it requires concentrated intent and will to press the button you precommitted to, especially if it looks like that would cause the universe (_your_ universe, that you're living in!) to stop existing via paradox.  Forcing the prediction to be right only works if you can guarantee that you'll cause a paradox if the prediction is wrong.  (It's counterfactual blackmail, almost.)~~
    ```

    - u/daytodave:
      ```
      So in that case the light was just wrong? But if you can press the red button and get a blue light sometimes because the device malfunctioned, doesn't that mean crashing isn't really a paradox?
      ```

      - u/endlessmoth:
        ```
        ~~In a certain sense, it wasn't the light that was wrong, but the user.~~

        ~~Like, say someone wants to force the light to be blue, but if the light flashes red, the person gets scared and doesn't want to stop existing and can't bring themselves not to press the red button, then _both outcomes are going to be possible_, because neither way actually leads to paradox.~~

        ~~The device never malfunctions.  It is, however, possible (and indeed plausible) that people, being imperfect, can fail to exploit it correctly.~~~
        ```

        - u/daytodave:
          ```
          That example makes sense, because you're pressing red after seeing red. But in the example with the coin flip the blue light comes on and then you press the red button. How is that not a paradox or malfunction?
          ```

          - u/endlessmoth:
            ```
            Ah, that is a misreading on my part.  My apologies, I should have looked closer.  You were right, and I've corrected the OP.
            ```

- u/aeschenkarnos:
  ```
  Coming to your [Ted *Chiang*](https://www.nature.com/articles/436150a) talk. It would have been nice to have at least given him a citation.
  ```

  - u/endlessmoth:
    ```
    I've probably read that story before, but I honestly wasn't thinking of it when I wrote the post.  The /r/rational discord logs show that my original conception was in the form of a special register or variable in a programming language which stores future data.  When I decided to write this post, I thought it best to ditch the programming analogy in the interest of broadest understanding, but I wanted something that kept its cut and dried, binary simplicity.  A device with buttons was the first thing I thought of.

    I can edit a link to the story into the post, but I contend that this is a fairly obvious answer to the question, "What is the minimum viable time machine?"
    ```

    - u/aeschenkarnos:
      ```
      Fair enough, I accept that it’s coincidence of a straightforward idea, not plagiarism.

      There’s also Isaac Asimov’s [thiotimoline](https://en.m.wikipedia.org/wiki/Thiotimoline) concept from 1948.
      ```

- u/MadVaughn:
  ```
  This is lovely. I can't wait to be chewing on this for the next week.

  For anyone like me who has trouble reading non fiction, I reccomend a TTS (text to speech) reader. My brain is able to hold on to concepts better if I'm able to hear them, and better still if I listen and read at the same time.

  Thanks again for the post. I'm really excited about this :D
  ```

- u/destravous:
  ```
  This is strikingly similar to how the wavefunction collapse procedural generation algorithim works: https://github.com/mxgmn/WaveFunctionCollapse/blob/master/README.md

  Specifically this part:

  >"It may happen that during propagation all the coefficients for a certain pixel become zero. That means that the algorithm has run into a contradiction and can not continue. The problem of determining whether a certain bitmap allows other nontrivial bitmaps satisfying condition (C1) is NP-hard, so it's impossible to create a fast solution that always finishes. In practice, however, the algorithm runs into contradictions surprisingly rarely."

  It appears preventing a paradox in a universe with stable time loop based time travel is equivalent to solving an NP-hard problem every time the paradox would occur.
  ```

- u/creative_ennui:
  ```
  This post reminds me of a number of papers looking at the effect of Closed Timelike Curves on computational complexity. Especially interesting are [2] for the exact complexity class of classical and quantum computing augmented with CTC's, and [6] for a discussion of a number of paradoxes involving CTC's in both classical and quantum settings


  [1] Aaronson, Scott. “[NP-Complete Problems and Physical Reality.](http://arxiv.org/abs/quant-ph/0502072)”

  [2] Aaronson, Scott, and John Watrous. “[Closed Timelike Curves Make Quantum and Classical Computing Equivalent.](https://doi.org/10.1098/rspa.2008.0350)”. 
  arxiv [link](https://arxiv.org/abs/0808.2669)

  [3] Bacon, Dave. “[Quantum Computational Complexity in the Presence of Closed Timelike Curves.](https://doi.org/10.1103/PhysRevA.70.032309)”. 
  arxiv [link](https://arxiv.org/abs/quant-ph/0309189)

  [4] Bartkiewicz, Małgorzata, Andrzej Grudka, Ryszard Horodecki, Justyna Łodyga, and Jacek Wychowaniec. “[Closed Timelike Curves and the Second Law of Thermodynamics.](https://doi.org/10.1103/PhysRevA.99.022304)”. 
  arxiv [link](https://arxiv.org/abs/1711.08334)

  [5] Brun, Todd A. “[Computers with Closed Timelike Curves Can Solve Hard Problems.](http://arxiv.org/abs/gr-qc/0209061)”

  [6] Deutsch, David. “[Quantum Mechanics near Closed Timelike Lines.]( https://doi.org/10.1103/PhysRevD.44.3197)”. 
  pdf [link](https://pdfs.semanticscholar.org/8e99/3e3e9b0952198a51ed99c9c0af3a31f433df.pdf)
  ```

- u/ramjet_oddity:
  ```
  This is ... wow. That's a lot of thinking. I think I'll have to reread it multiple times before coming to a conclusion, but this is epic.
  ```

- u/Mr-Mister:
  ```
  For a story that combines all of these, play Deponia Doomsday.
  ```

- u/SevereCircle:
  ```
  I'm still reading, but while I'm reading, this example comes to mind:

  Turn the dial on the device so it is configured to send information back one second in the past. Flip a coin. Wait ten seconds. If it was heads, clap your hands three times. If it was tails, crash. In which of your models does this force the coin to come up heads*?

  *except with the probability that you somehow fail to crash because your hand slips or something: let's just call that probability epsilon if it becomes necessary to consider

  I'll try to answer myself if I finish reading the post before you get read and answer this comment.

  ---

  edit 1:

  I follow Path Realism. It leads to bizarre things but I understand the definition, I think.

  Local Branch Realism:
  >The intermediate is more interesting: if you, as in the original experiment, splint and then splint again and crash if both splints come out red, then half the time the first splint will come out red, but if the first splint comes out blue, the next one always comes out red. In numbers, the possibilities are p(red,red) = p(red,blue) = 1/4, and p(blue,red) = 1/2.

  I would understand if it said "if the first splint comes out red, the next splint always comes out blue" but as written I don't understand what you mean.

  ---

  edit 2: 

  Weighted Branch Realism

  Do static paradox fraction and intrinsic probability correspond to the prior and posterior probability distributions in TimTravel's post, respectively or the other way around (other way around: spf = posterior and ip = prior)? Or do they not correspond at all?

  ---

  edit 2b: No, they don't correspond. ~~Reroll realism is equivalent to TimTravel's system though. Pretty sure.~~ (later edits: it's not)

  ---

  edit 3:

  Alice and Bob: I assume Bob also consults his device to see where he should look and crashes if he looks in the wrong place. Is that the case?

  ---

  edit 4:

  Surely the "time force" effectively works differently under the different models?

  > An obvious corollary to all this is that TIME FORCE is almost never relevant. If you had a bigger device that spat out 32 red/blue pairs at a time, you could predict the lottery without worrying about time force.

  Under ~~reroll realism~~ TimTravel's system, if Old Man Wek has a policy to crash unless he win the lottery, and he has a 1% chance of death on the day he buys the ticket (he is very sickly in this hypothetical) then he will almost certainly die. See http://www.scp-wiki.net/scp-988 for a similar thought experiment.

  > That said, it's in some models the case that the most probable timelines are the ones in which time machines are never invented. In Local Branch Realism, this is not true (unless some bad actor arises in every single timeline and causes paradox. Time Beast, anyone?). In Path Realism, this is again never true without positing a Time Beast. However in WBR and RR, it's more or less true. In general, timelines with fewer instances of retrocausation are more likely, only because instances of retrocausation are a proxy for instances of paradox. Now, if paradox are rare, this argument would be weak. (But to be fair, most meaningful uses of time travel require copious paradox; it's the oil in the engine.)

  I agree. This is consistent with what I said on the r/r Discord about TimTravel's system, which is (roughly?) equivalent to reroll realism. (later edits: it seems not to be)

  ---

  edit 5: 

  > But from that, it follows that the odds of TIME FORCE acting over an interval of time is proportional to the length of that interval. (It's at least linear. It might be super-linear.)

  I think it tends to increase with the duration of the interval but it depends on how many cosmic coins are simulated in the simulation of the universe during those intervals. In practice under most fictional settings I think it would increase monotonically (but not linearly) with the duration of the interval. It *can't* increase linearly, otherwise eventually the probability it affects the interval would be greater than one.

  I only understand what "time force" means in TimTravel's system. I'm not sure what it would mean in the other models.

  > One common confusion which leads people to overstate the importance of TIME FORCE is the fact that parallel universes and timelines aren't necessarily the same thing.

  Interesting. I will end this edit now and continue reading.

  ---

  edit 6:

  > when it comes up heads, you take the strange device and force blue splints a million times

  If you mean "force blue a million times" I follow. I don't know what "force blue splints" means if not that.

  ---

  edit 7:

  > Viz. if you do a quantum coin flip and, when it comes up heads, you take the strange device and force blue splints a million times, or, when if the q-coin comes up tails, you force red only once, the odds of seeing blue/red could be 50/50. I.e., by default, half the time there's 50% chance of a 100% chance of seeing blue, and a 50% chance of a 100% chance to see red.

  I don't follow where the parentheses go on this case. Can you rephrase?

  > The story is only necessarily different if instead of a quantum coin, you flip a time coin; i.e., cause a splinterpoint. When you do this, it's the... the exact same story in Path Realism and Local Branch Realism, but in Global Branch Realism and Restart Realism, the blue branch has a vastly smaller probability.

  (I assume restart realism = reroll realism.)

  If this is true, then reroll realism is NOT equivalent to TimTravel's system, because in TimTravel's system flipping a coin and flipping a "time coin" are equivalent. Therefore if this is true then I do not understand what reroll realism is.

  ---

  edit 8:

  > She's getting impatient, and yanks out her user manual. The culprit's there: it's said the devices exhibit a phenomena called "paradox aversion"; where if the chance of paradox is too high, it's just vastly more likely for no prediction to happen. But there's a special override button at the back, pressable with a needle, which forces the device to yield a prediction, paradox be damned. Alice decides to try to press it.

  This is a different version of the device than the original, and it is unclear to me how to define the probability of a paradox in each of your models. I would appreciate clarification. Suppose you're in TimTravel's system and you have the device and you intend to straight-up always crash. Something will stop you. If the initial configuration of the universe is one where you already have the device and have that intention, your finger will slip and you'll push the wrong button, or your brain will randomly decide to break your original intention and you'll push the right one. Or somebody else will push the right one by coincidence. If the initial configuration of the universe is not one where you already have the device, you'll probably never get your hands on one. This is for the original device, without the paradox prevention feature (and I repeat that I don't know how that would work).

  ---

  edit 9: I am not sure whether I agree or disagree with your section on Bound Time Travel and Free Time Travel, because of the issues above.

  I am now done with my first pass through the post. Knowing myself, within a few minutes I will probably think of another issue to bring up in another edit, but I've at least read it all now.
  ```

  - u/endlessmoth:
    ```
    > Turn the dial on the device so it is configured to send information back one second in the past. Flip a coin. Wait ten seconds. If it was heads, clap your hands three times. If it was tails, crash. In which of your models does this force the coin to come up heads*?

    I think it's irrelevant?  The device seems to have no strong causal connection to your coin flip.  You are committing to not pressing the button at all in the ten seconds, right?  Either way, the only way I could see it matter is if, _even if the lights dont flash_, the electronics inside the device can generate heat in just the right pattern to cause variations in the air flow which affects the flight of the coin and _might_ have some effect.  But if the device is well designed and doesn't send information back and forth unless the user requests, without leaking information, I think the answer is no.  TIME FORCE will have to intervene if it comes up tails.

    > I would understand if it said "if the first splint comes out red, the next splint always comes out blue" but as written I don't understand what you mean.

    That was a typo.  Thank you for catching, but it's not there on my end.  I think what happened is you loaded an old version of the post, and I fixed the typo before you posted.

    > Do static paradox fraction and intrinsic probability correspond to the prior and posterior probability distributions in TimTravel's post, respectively or the other way around (other way around: spf = posterior and ip = prior)? Or do they not correspond at all?
    > edit 2b: No, they don't correspond. 

    I doubt it.  ip = prior sounds possible on the face of it.  But spf is It's not even a probability, but a fraction of how many children of this branch are paradoxical (weighted so that closer descendants count more than distant ones.

    > Alice and Bob: I assume Bob also consults his device to see where he should look and crashes if he looks in the wrong place. Is that the case?

    Correct.

    > Surely the "time force" effectively works differently under the different models?

    I'd presume so, yeah.  Didn't have enough think-juice left over last night to think hard about the details, unfortunately.

    > I think it would increase monotonically (but not linearly) with the duration of the interval. It can't increase linearly, otherwise eventually the probability it affects the interval would be greater than one.

    Good catch.  Sloppy use of terminology on my part.

    > If you mean "force blue a million times" I follow. I don't know what "force blue splints" means if not that.

    My bad, it's the same thing.

    > This is a different version of the device than the original, and it is unclear to me how to define the probability of a paradox in each of your models. 

    Easy, it's always 0 :^)

    But no, this is just sloppiness on my part.  The passage above assumes RR/BBR, or WBR.  In PR and LBR, it's just false.
    ```

- u/wren42:
  ```
  this is awesome. it's also not a 15-20 minute read XD  there's a lot more processing of the math that needs to happen than pure words per minute ;)
  ```

---

