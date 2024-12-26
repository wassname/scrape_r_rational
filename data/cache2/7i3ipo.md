## DeepMind neural network beats top engines within hours of being exposed to the game of chess [EDU] [HSF]

* Author: u/LeifCarrotson *
* URL: https://www.reddit.com/r/rational/comments/7i3ipo/deepmind_neural_network_beats_top_engines_within/
* Score: 50

* Created: 2017-12-07T03:09:40

### Post:

[removed]

### Comments:

> **u/Flag_Red** [+22]  (3 hours later)
> 
> It should be noted that the DeepMind AI was playing on vastly superior hardware than stock fish and at its ideal time control. Evening out the processing power available to the AIs or shortening the time control would definitely put the game in Stockfish's favour.

>> **u/thrawnca** [+10]  *Carbon-based biped* (7 hours later)
>> 
>> There were graphs for that in the paper. Yes, at very short turn lengths, Stockfish performed better. However, 1 minute was enough time for AlphaZero to win convincingly, and that's not long for chess.
>> 
>> I also didn't see any indication that Stockfish was particularly underpowered; what's your source for that? Would Stockfish have been capable of properly utilising the type of hardware that powered AlphaZero? Because if not, then that's an important finding in itself, just as GPUs have replaced CPUs for cryptography.

>>> **u/Flag_Red** [+6]  (7 hours later)
>>> 
>>> AlphaZero played on 4 TPUs. Stockfish's played on 64CPU cores, they don't say what model processor but I'll assume a modern high end processor. 
>>> 
>>> 1TPU can do 180TFLOPs according to Google and a typical high end, 8 core CPU can barely manage 1 usually. If AlphaZero were playing on a 64 core CPU (which it can, because it uses Tensorflow) it would have roughly 1/90th of it's current processing power going off my numbers above. For reference, Stockfish playing against itself with 1/90th of the processing power is a stomp.
>>> 
>>> Edit: And this doesn't even go into how badly configured Stockfish was. A 1GB hash is nothing for 64 cores of processing power. You're looking at more like 25GB normally. Meanwhile, IIRC AlphaZero had 250GB of memory to use.

>>>> **u/696e6372656469626c65** [+11]  *I think, therefore I am pretentious.* (7 hours later)
>>>> 
>>>> Tensor processing units are application-specific integrated circuits, and as such are not directly comparable to CPUs. You're attempting to draw a comparison between apples and oranges. Moreover, even if we accept that Stockfish was at a hardware "disadvantage", the absolute number of positions searched per second was still far higher for Stockfish (70 million positions per second) than for AlphaZero (80 thousand). Clearly search speed isn't the bottleneck here, so trying to draw all the focus to the hardware is a red herring in and of itself.
>>>> 
>>>> As far as low hash size goes, you have a point there, but since hash tables are mainly used to speed up search by cutting subtrees off of the main search tree, it hardly makes much of a difference since, as I already pointed out, Stockfish already had a tremendous advantage in terms of search speed. After pointing out that SF's hash was abnormally small, however, you again go astray by attempting to compare the SF's 1GB *hash* to AlphaZero's 250GB *memory*, which it could have been using for anything. Apples and oranges.
>>>> 
>>>> Moreover, *even if everything you said were true*, this still does not validate your initial statement that "evening out the processing power" (whatever that actually *means*, considering that the number of FLOPs per second isn't a good measurement when comparing general-purpose CPUs to ASICs) would "definitely put the game in Stockfish's favour". You have no evidence in favor of that or any other conclusion; the best you could say is that it *might* favor Stockfish more. (Though personally I'd bet against that as well.)
>>>> 
>>>> **EDIT**: Moreover, this
>>>> 
>>>> > For reference, Stockfish playing against itself with 1/90th of the processing power is a stomp.
>>>> 
>>>> is a context-dependent statement that may or may not be true. Stockfish with 1 core playing against Stockfish with 90 cores is indeed, as you say, a "stomp", but computational power faces diminishing returns in playing strength. Stockfish with 100 cores, for instance, would draw most of its games against Stockfish with 9000 cores.

>>>>> **u/Flag_Red** [+10]  (8 hours later)
>>>>> 
>>>>> You seem to be equating computing power used to positions searched. The reason AlphaZero searches so few positions is because it uses boatloads of processing power elsewhere (in the NN calculations).
>>>>> 
>>>>> A very simple way to even out the computational power they have is by putting them on the same hardware, just like we do in every major computer chess tournament. Put AlphaZero on a 64 cores of the same CPU given to Stockfish and you'll see that reducing an engine's processing power to 1/90th of what it was severely hinders the engine's performance. 
>>>>> 
>>>>> Neural networks are great and all (I'm an AI researcher, I build them all the time) but they only became viable recently because of the abundance of processing power available now. The fact remains that they require far more processing power than any other classification or regression algorithm used today.

>>>>>> **u/Ilverin** [+3]  (12 hours later)
>>>>>> 
>>>>>> Just a note that processing power is slightly more complicated. Google's tensor processing unit uses something similar to minifloat (8-bit float) so FLOPs aren't the same as with normal hardware. Personally my favorite comparison is with total hardware cost when comparing 2 different kinds of data type. 
>>>>>> 
>>>>>> Unfortunately we don't know how much Google TPUs costs. According to http://www.cdrinfo.com/Sections/News/Details.aspx?NewsId=62788 AlphaZero only ran on 4 TPUs (less than 1 TPU pod). According to this comment this is less power consumption than Stockfish: https://www.reddit.com/r/chess/comments/7i8419/cb_article_on_alphazero_suggests_alphazero_is/dqxbimp/
>>>>>> 
>>>>>> Datatype used in tensor flow (not learning part, the performing part): https://www.tensorflow.org/performance/quantization

>>>>>> **u/696e6372656469626c65** [+2]  *I think, therefore I am pretentious.* (8 hours later)
>>>>>> 
>>>>>> > You seem to be equating computing power used to positions searched. The reason AlphaZero searches so few positions is because it uses boatloads of processing power elsewhere (in the NN calculations).
>>>>>> 
>>>>>> Yes, this is the *entire point*. The majority of AlphaZero's processing power is used to carry out the neural network's calculations, *not* search. Giving Stockfish additional processing power, on the other hand, will go *exclusively* toward speeding up search. What will end up happening is that you'll get a match between a "smart" evaluator, and a "dumb" evaluator that's really fast at evaluating things--or, in other words, exactly the match we already saw, except the "dumb" evaluator will be even faster. Given the diminishing returns with search depth, the result is unlikely to be very different from what we saw here.
>>>>>> 
>>>>>> Or, to put it another way, do you demand that chess engines be reduced to evaluating only 1-2 positions per second when they play against humans, purely because humans are only able to evaluate at that speed? Of course not; the very notion is ridiculous--and yet that's the exact type of semantic leap you're attempting to pull here.

>>>>>>> **u/Flag_Red** [+7]  (8 hours later)
>>>>>>> 
>>>>>>> When you compare a chess engine to *anything*, you have to specify how much processing power you're giving it. Note that processing power *is not* positions evaluated per second. Your scenario at the end shows that.
>>>>>>> 
>>>>>>> I'll give you an example. Say we're comparing two other engines, Komodo and Houdini. When we compare them, we give them the same hardware and say "whoever wins the most games is better". We don't say "whoever processes the fewest positions is better". We also don't give one machine significantly more powerful hardware. This is like having a gladiator fight and giving one side a gun. You clearly can't say it was a fair match when one side is given a huge advantage like that. So, if you want to evaluate Stockfish and AlphaZero, you do the same. You put them on the same hardware and say "whoever wins the most games is best". You don't say "whoever evaluates positions most smartly is best" or "whowever evaluates the least positions is best". The only decider of which is better is which wins the most games.
>>>>>>> 
>>>>>>> Note, at the same time, you can't evaluate whether a human or an engine is better. This is because an engine without a computer to run on doesn't even play chess. You need to evaluate whether a human or an engine with a specified amount of hardware is better.

>>>>>>>> **u/wren42** [+4]  (13 hours later)
>>>>>>>> 
>>>>>>>> i guess the question is whether Stockfish would outperform AlphaZero using the BETTER hardware.  You've claimed AlphaZero wouldn't work well on weaker hardware, but would stockfish scale up sufficiently to compete, or is the algorithm not capable of utilizing the additional processing effectively?
>>>>>>>> 
>>>>>>>> If the answer is that Stockfish would win on worse hardware and Alphago would win on better hardware, then your scenario suggesting we just put them on the same box and see who wins breaks down.  The selection of the turf decides the outcome, like a gladiator contest with a merman fighting a centaur. 
>>>>>>>> 
>>>>>>>> Personally I'd say we should compare the two operating under the *most favorable conditions for their algorithm*, rather than *the same hardware.*  The latter isn't necessarily as pure a test as it sounds.  If one algorithm makes very good use of RAM and one is better at leveraging GPU or something, they should both just get hardware optimized for thier respective strengths.

>>>>>>>>> **u/Veedrac** [+2]  (18 hours later)
>>>>>>>>> 
>>>>>>>>> [They did analyse how well each scales with hardware](https://www.reddit.com/r/rational/comments/7i3ipo/deepmind_neural_network_beats_top_engines_within/dqwnfa1/), so you can make this projection even if you consider the current comparison unbalanced.

>>>>>>>> **u/ImNotGaySoStopAsking** [+3]  (9 hours later)
>>>>>>>> 
>>>>>>>> What are you guys talking about? I don’t understand any of this

>>>>>>>> **u/696e6372656469626c65** [+0]  *I think, therefore I am pretentious.* (18 hours later)
>>>>>>>> 
>>>>>>>> > I'll give you an example. Say we're comparing two other engines, Komodo and Houdini. When we compare them, we give them the same hardware and say "whoever wins the most games is better".
>>>>>>>> 
>>>>>>>> What you're missing is that *the only reason this sort of hardware comparison is even possible is because Komodo and Houdini have the same architecture*. Yes, there are differences in implementation (which is what leads to the difference in strength between the two), but both use alpha-beta search with null-move pruning, both use classical, hand-written evaluation functions, etc. In short, matches between traditional chess engines suffer from none of the "apples-and-oranges" issues I described earlier, because traditional chess engines are all actually *extremely similar* to each other.
>>>>>>>> 
>>>>>>>> AlphaZero, on the other hand, operates using a tremendously different architectural paradigm--one that requires it to use a *different kind of processor*. As /u/Veedrac pointed out [below](https://www.reddit.com/r/rational/comments/7i3ipo/deepmind_neural_network_beats_top_engines_within/dqwp0to/), TPUs are *not* simply "CPUs, except faster" as you seem to be making them out to be; it's more complicated than that. So at risk of sounding like a broken record, *you are still trying to compare apples and oranges*, and the Komodo-Houdini comparison you brought up doesn't address this at all, really.
>>>>>>>> 
>>>>>>>> So, with all that having been said, what do you do if you're DeepMind and you find yourself in a situation where you'd *like* to be able to compare your NN-based design against a top engine, but there's no real way to procure "equalized" hardware? You do *exactly what they ended up actually doing*: you give Stockfish strong-enough hardware that its absolute speed advantage--in terms of nodes searched per second--is far greater than AlphaZero's, in order to demonstrate that AlphaZero's competitive advantage does *not* come from superior search. You do *not* artificially handicap your NN-based design by forcing it to play using normal CPUs that don't efficiently perform the TensorFlow operations necessary to run the neural network, all because Stockfish happens to be using CPUs and you want to be "fair". (Likewise, you don't handicap *Stockfish* by forcing it to play on your proprietary TPUs, which don't natively support many of the operations *it* uses.)
>>>>>>>> 
>>>>>>>> And then you publish the games, without worrying particularly much about whether this particular version of Stockfish was "fast enough", because you've *already successfully demonstrated what you've set out to demonstrate*: that a NN-based approach is capable of yielding significantly better results than a classical engine, *even when said classical engine is evaluating many, many more positions per second*. That's all there is to it.

>>>>>>>>> **u/Veedrac** [+3]  (18 hours later)
>>>>>>>>> 
>>>>>>>>> > *You do exactly what they ended up actually doing*: you give Stockfish strong-enough hardware that its absolute speed advantage--in terms of nodes searched per second--is far greater than AlphaZero's
>>>>>>>>> 
>>>>>>>>> Not sure I agree; AlphaZero evaluates fewer moves because it uses a different algorithm, not because of a hardware deficit. They are still expected to use comparable hardware to some degree; clearly Stockfish on a Raspberry Pi is far weaker than on a 64 core monster, but it'll probably still outpace AlphaZero on a moves-evaluated basis.
>>>>>>>>> 
>>>>>>>>> I agree that the hardware shouldn't be *equal*, though, and that forcing AlphaZero to use a CPU would be silly.

>>>>>>>>>> **u/696e6372656469626c65** [+1]  *I think, therefore I am pretentious.* (18 hours later)
>>>>>>>>>> 
>>>>>>>>>> Good point. Still, given that Stockfish was actually being run on a 64-core computer, not a Raspberry Pi, it seems to me that this distinction is less relevant than it might otherwise be. Or, to cash things out in terms of an empirical prediction: I doubt that Stockfish running on, say, 128 or 256 cores would observe significantly better performance against AlphaZero than it did on 64 cores; the differences in understanding we saw in the sample games seem to me to be of a qualitative rather than quantitative nature.
>>>>>>>>>> 
>>>>>>>>>> **EDIT:** As far as "comparable hardware" goes, as I said, the comparison is made difficult by the fact that TPUs are optimized for different tasks than CPUs. The only *objective* metric for comparison I can think of would be energy consumption, but as we don't have figures for the energy consumption of TPUs, this isn't really possible for us to speculate about at the moment.

>>>>>>>>>>> **u/Veedrac** [+1]  (a day later)
>>>>>>>>>>> 
>>>>>>>>>>> > we don't have figures for the energy consumption of TPUs
>>>>>>>>>>> 
>>>>>>>>>>> We know a bunch of this stuff for first-gen TPUs.
>>>>>>>>>>> 
>>>>>>>>>>> > The TPU die area is less than half that of the Haswell eighteen core CPU and Nvidia's Tesla K80 GPUs (the preferred solutions at the time), which yields a much lower rating of 75W, compared to 145W and 150W, respectively. Idle power consumption is higher than a GPU, but lower than a CPU.
>>>>>>>>>>> 
>>>>>>>>>>> \- http://www.tomshardware.com/news/tpu-v2-google-machine-learning,35370.html
>>>>>>>>>>> 
>>>>>>>>>>> See also https://arxiv.org/pdf/1704.04760.pdf for a much more in-depth view of that older chip; I haven't read it all. I suspect that, unless they have radically modified their goals with the second generation chip, AlphaZero had a comparable thermal envelope to Stockfish.

>>>>> **u/Rouninscholar** [+1]  (11 hours later)
>>>>> 
>>>>> I agree with almost everything you said, except the last sentence.
>>>>> In chess, shogi, and go, draws are impossible on the last two, and dont happen on competitive play in chess. It would probably acheive a very close to 50% win rate, if given a 50% playing first rate.

>>>>>> **u/Mablun** [+5]  (13 hours later)
>>>>>> 
>>>>>> I'm confused by what you wrote, are you saying that draws don't happen in competitive play in chess? Because that's clearly not true

>>>>>>> **u/Rouninscholar** [+5]  (13 hours later)
>>>>>>> 
>>>>>>> Honestly, was misinformed. Went and did some research and you are right. My apologies.

>>>>>>>> **u/Mablun** [+2]  (14 hours later)
>>>>>>>> 
>>>>>>>> Just so other people don't have to go and do the research, in high level play around 50% of chess games are draws.

>>>> **u/Veedrac** [+3]  (13 hours later)
>>>> 
>>>> The two were playing under roughly similar thermal envelopes, which is effectively the important measure for potentially-commodity hardware. That a TPU does more TOPS (*not* TFLOPS; it doesn't do float) is simply a trade in hardware design; a CPU handles inhomogeneous control flow and complex instruction, whereas a TPU is specialised for purpose. That the TPUs were more expensive is mostly a product of their low production volume.
>>>> 
>>>> Stockfish could no more run fast on AlphaZero's hardware than AlphaZero could run fast on Stockfish's.
>>>> 
>>>> E: Second generation TPUs can do float. I don't know how fast.

>> **u/Veedrac** [+5]  (13 hours later)
>> 
>> > https://i.imgur.com/JQQXl9J.png
>> >
>> > Figure 2: Scalability of AlphaZero with thinking time, measured on an Elo scale. **a** Performance of AlphaZero and Stockfish in chess, plotted against thinking time per move.
>> 
>> As you can see, the asymptotes are different. Since the x-axis is a log plot, a constant factor difference in hardware throughput corresponds to a horizontal translation. You can see that you would presumably need a translation of much greater than 100x (about  2/3 the width of the graph) for Stockfish to catch up in this range, and because the asymptotes are different this would not hold for long.
>> 
>> I am not sure how hash tables come into this, but I believe making it larger would only act as a small linear speed improvement, so the above analysis holds.
>> 
>> In other words, AlphaZero is intrinsically stronger in the limit of feasible computation.

>> **u/696e6372656469626c65** [+6]  *I think, therefore I am pretentious.* (7 hours later)
>> 
>> > would definitely put the game in Stockfish's favour.
>> 
>> I do wish people would be less eager to make sweeping claims like this with no evidence whatsoever to back them up.

> **u/veruchai** [+3]  (13 hours later)
> 
> After AlphaGo came out, there were obvious questions about chess and as a (lower class) chess player I was waiting for something like this to be obviously good. I *was* however expecting a NN to optimize using the far larger electronic infrastructure of chess in contrast to Go. Surpisingly it seems they have gone for the complete from scratch method which I suppose is the more interesting method. Throwing away years of documented optimization, not even using it as a kickstart, in favor of avoiding local minima is not something I would have chosen with my hardware to say the least. 
> 
> Looking forward to seeing how this pans out.

> **u/monkyyy0** [+5]  (2 hours later)
> 
> Friendly reminder, alphago was still mostly a min max algorithm.
> 
> I would bet money that fairly low elo human networks using the same minmax tree systems would still beat it. Given that is against the hype that experiment wouldn't happen, but eh. What you going to do.

>> **u/EliezerYudkowsky** [+17]  *Godric Gryffindor* (2 hours later)
>> 
>> False.  AlphaGo Lee playing at zero depth played at an extremely strong level, I forget what exactly.

>>> **u/monkyyy0** [+4]  (3 hours later)
>>> 
>>> If your talking about the expert move prediction that's not quite my criticism; knowing the top 5 best moves is not the same as picking the best of them because of something that can happen 5 moves from now.

>>>> **u/thrawnca** [+9]  *Carbon-based biped* (7 hours later)
>>>> 
>>>> If you iterate enough times, the distinction between the two becomes quite narrow.

>>>>> **u/monkyyy0** [+0]  (15 hours later)
>>>>> 
>>>>> I disagree.
>>>>> 
>>>>> If you train a (forward fed)neural net on trying to predict the outcome of factorial on training data for 1-100; its going to be very wrong about what 1000 is.
>>>>> 
>>>>> Its a naturally recursive problem while the forward fed part of it means it can't use loops.
>>>>> 
>>>>> The minmax algorithm is recursive and a natural part of turn based games

>>>>>> **u/thrawnca** [+2]  *Carbon-based biped* (15 hours later)
>>>>>> 
>>>>>> > it's going to be very wrong about what 1000 is.
>>>>>> 
>>>>>> I don't see how this analogy applies. Maybe if AlphaZero played only partial games against itself, then that would align with what you're suggesting; however, when you run through hundreds of thousands of complete games looking for winning strategies, then "best move at this point" and "move that will best handle the situation in 5 turns" converge. In fact, it will do even better; it won't just look ahead for 5 turns, but for the entire game.

>>>>>>> **u/monkyyy0** [+1]  (16 hours later)
>>>>>>> 
>>>>>>> With exponential games and processing time and size of the net
>>>>>>> 
>>>>>>> It could at best make a lookup table of sorts. Much like factorial problem, imagine the neural net that solves factorial for 1-5; designing one by hand to solve 1-5 perfectly? what happens if you put 10 in it?
>>>>>>> 
>>>>>>> They used a min max trees for a reason; don't buy the hype, you can't solve all problem by adding numbers together; you need access to loops and real conditionals but you can't give access to those tools to the way we train neural nets.

>>>>>>>> **u/thrawnca** [+1]  *Carbon-based biped* (18 hours later)
>>>>>>>> 
>>>>>>>> > you can't solve all problem by adding numbers together; you need access to loops and real conditionals
>>>>>>>> 
>>>>>>>> First, what is your source for your assertion? AlphaZero has just placed several striking data points; if you discount them, what backs you up?
>>>>>>>> 
>>>>>>>> Second, computers implement loops and conditionals by...adding numbers together.
>>>>>>>> 
>>>>>>>> > what happens if you put 10 in it?
>>>>>>>> 
>>>>>>>> Again, this is a false equivalence. Iiuc you're basically saying that if you play a game that wasn't among the hundreds of thousands used for practice, then AlphaGo will perform poorly. But the point of that practice wasn't to memorise hundreds of thousands of potential playthroughs; it was smarter than that, using those runs to gather more generalisable guidelines for which moves tend to succeed or fail. As evidenced by its performance against new opponents.

>>>>>>>>> **u/monkyyy0** [+1]  (20 hours later)
>>>>>>>>> 
>>>>>>>>> > First, what is your source for your assertion?
>>>>>>>>> 
>>>>>>>>> Common sense, if you wish to disprove me, please point me towards a way to program fractional without loops or recursion of some kind.
>>>>>>>>> 
>>>>>>>>> There is also ackermann function if you want an impossible problem.
>>>>>>>>> 
>>>>>>>>> >Second, computers implement loops and conditionals by...adding numbers together.
>>>>>>>>> 
>>>>>>>>> ..... Are you perhaps confused on what a forward feed neural net is?
>>>>>>>>> 
>>>>>>>>> It by definition doesn't have loops; the adding numbers together is what a neural net does.
>>>>>>>>> 
>>>>>>>>> >Iiuc you're basically saying that if you play a game that wasn't among the hundreds of thousands used for practice, then AlphaGo will perform poorly
>>>>>>>>> 
>>>>>>>>> No I'm not; consider minesweeper being proven to be np-hard, that does not mean a lower complexity is unable to beat easier games. You could probably make a linear time able to beat 99% of games. It's the last percent that matters on defining its true complexity.
>>>>>>>>> 
>>>>>>>>> Being able to predict 20 moves in advance is a grand master skill in chess; but being able to avoid stupid mistakes should be possible with straight addition(add up the value of each piece, and calculate how many are "at risk" for example, take the action that maximizes this heuristic)
>>>>>>>>> 
>>>>>>>>> Lazy heuristics can get you quite far; but its the minmax trees that compete with grandmasters of any system.
>>>>>>>>> 
>>>>>>>>> >As evidenced by its performance against new opponents.
>>>>>>>>> 
>>>>>>>>> Alpha go is not a neural net, its a neural net with a minmax tree heart.
>>>>>>>>> 
>>>>>>>>> You can't point at its success in a way that separates it from the min max tree
>>>>>>>>> 
>>>>>>>>> -----
>>>>>>>>> 
>>>>>>>>> >this is a false equivalence.
>>>>>>>>> 
>>>>>>>>> Which part?
>>>>>>>>> 
>>>>>>>>> 1. Neural nets can't solve factorial because that lack recursion
>>>>>>>>> 
>>>>>>>>> 2. Min max trees are naturally recursive, like factorial
>>>>>>>>> 
>>>>>>>>> 3. min max tree's are necessary part of turn based games solutions that reach high levels
>>>>>>>>> 
>>>>>>>>> 4. alpha go is a neural net with a minmaxer; while clever isn't actual proof for the delusional hype around neural nets.
>>>>>>>>> 
>>>>>>>>> I feel only number 3 needs any defence. Its not proven, but I'd love to hear a single counterexample of any turn based game ai that works very well without a minmax tree

>>>>>>>>>> **u/thrawnca** [+1]  *Carbon-based biped* (20 hours later)
>>>>>>>>>> 
>>>>>>>>>> > There is also ackermann function if you want an impossible problem.
>>>>>>>>>> 
>>>>>>>>>> Predicting every legal chess move is impossible for today's computers, too, but apparently neural nets can still do a good job of calculating a strategy. If there is a real-world problem involving the Ackermann function, perhaps a similar approach would likewise produce a reasonable (if theoretically non-optimal) solution? Would need a concrete example to evaluate this.
>>>>>>>>>> 
>>>>>>>>>> > ..... Are you perhaps confused on what a forward feed neural net is?
>>>>>>>>>> > It by definition doesn't have loops; the adding numbers together is what a neural net does.
>>>>>>>>>> 
>>>>>>>>>> My point was that you demand loops and conditionals, while discounting "adding numbers together" - but what you demand is in fact one form of adding numbers together.
>>>>>>>>>> 
>>>>>>>>>> > Neural nets can't solve factorial because that lack recursion
>>>>>>>>>> 
>>>>>>>>>> Completely *solving* the chess game is not necessary to win. The point is, this approach produced a more general engine capable of significantly *better* strategy than previous specialised engines, in multiple games. The fact that it's not mathematically complete doesn't really detract from that, since a complete solution basically requires brute forcing the entire search space and isn't possible in 2017.
>>>>>>>>>> 
>>>>>>>>>> The stated limitation of min-max trees was inability to adapt to challenges outside their training space, but AlphaZero convincingly defeated opponents that it hadn't trained against.

>>>>>>>>>>> **u/monkyyy0** [+1]  (20 hours later)
>>>>>>>>>>> 
>>>>>>>>>>> >>There is also ackermann function if you want an impossible problem.
>>>>>>>>>>> 
>>>>>>>>>>> >Predicting every legal chess move is impossible for today's computers, too, but apparently neural nets can still do a good job of calculating a strategy. If there is a real-world problem involving the Ackermann function, perhaps a similar approach would likewise produce a reasonable (if theoretically non-optimal) solution? Would need a concrete example to evaluate this.
>>>>>>>>>>> 
>>>>>>>>>>> Not What I mean
>>>>>>>>>>> 
>>>>>>>>>>> Ackermann function/factorial, could not be correct with a neural net as a platform; while a correct solution, if impractical exist elsewhere trivially. The hype around neural nets as the general solution is wrong 
>>>>>>>>>>> 
>>>>>>>>>>> >this approach produced a more general engine capable of significantly better strategy than previous specialised engines, in multiple games.
>>>>>>>>>>> 
>>>>>>>>>>> Its not that general; I'm suggesting a heaping spoonful of pessimism needs to be part of this conversation; add some caveats.
>>>>>>>>>>> 
>>>>>>>>>>> >The stated limitation of min-max trees was inability to adapt to challenges outside their training space
>>>>>>>>>>> 
>>>>>>>>>>> That's not a limitation of min-max trees; they are a perfect solution; their limitation is computation complexity.

>>>>>>>>>> **u/Veedrac** [+1]  (a day later)
>>>>>>>>>> 
>>>>>>>>>> > Alpha go is not a neural net, its a neural net with a minmax tree heart.
>>>>>>>>>> 
>>>>>>>>>> None of the Alpha* line use minimax. They use monte-carlo.
>>>>>>>>>> 
>>>>>>>>>> This is all a silly argument, though. You can just look at the multiple data points of how strong a player AlphaGo or AlphaZero are when you limit search depth to zero. There's no advantage in trying to guess the data when it's available.

>>> **u/None** [+3]  (7 hours later)
>>> 
>>> I think it was about 3 or 5 dan amateur, so it was strong but not pro level (for Alpha Lee at least). I'd guess Zero with no search would still be pro level.

>>> **u/Veedrac** [+1]  (18 hours later)
>>> 
>>> [They analyse AlphaZero's chess skill with varying time controls](https://i.imgur.com/JQQXl9J.png); at very low time constraints it scores about 550 ELO lower, which is roughly on-par with top grandmasters IIUC.

>>>> **u/696e6372656469626c65** [+1]  *I think, therefore I am pretentious.* (19 hours later)
>>>> 
>>>> I believe EY was talking about AlphaGo's playing strength, not AlphaZero.

>>>>> **u/Veedrac** [+1]  (19 hours later)
>>>>> 
>>>>> Yes, I was stating an additional point.

>> **u/serge_cell** [+2]  (4 hours later)
>> 
>> No. It use tree evalution to train neural network and use the same neural network for evaluation on the leafs of the tree recursively.

> **u/rationalidurr** [+0]  *If fighting is sure to result in victory, then you must fight!* (a day later)
> 
> Good Lord! We are going to die!

---

