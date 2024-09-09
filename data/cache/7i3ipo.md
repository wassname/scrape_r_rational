## DeepMind neural network beats top engines within hours of being exposed to the game of chess [EDU] [HSF]

### Post:

[removed]

### Comments:

- u/Flag_Red:
  ```
  It should be noted that the DeepMind AI was playing on vastly superior hardware than stock fish and at its ideal time control. Evening out the processing power available to the AIs or shortening the time control would definitely put the game in Stockfish's favour.
  ```

  - u/thrawnca:
    ```
    There were graphs for that in the paper. Yes, at very short turn lengths, Stockfish performed better. However, 1 minute was enough time for AlphaZero to win convincingly, and that's not long for chess.

    I also didn't see any indication that Stockfish was particularly underpowered; what's your source for that? Would Stockfish have been capable of properly utilising the type of hardware that powered AlphaZero? Because if not, then that's an important finding in itself, just as GPUs have replaced CPUs for cryptography.
    ```

    - u/Flag_Red:
      ```
      AlphaZero played on 4 TPUs. Stockfish's played on 64CPU cores, they don't say what model processor but I'll assume a modern high end processor. 

      1TPU can do 180TFLOPs according to Google and a typical high end, 8 core CPU can barely manage 1 usually. If AlphaZero were playing on a 64 core CPU (which it can, because it uses Tensorflow) it would have roughly 1/90th of it's current processing power going off my numbers above. For reference, Stockfish playing against itself with 1/90th of the processing power is a stomp.

      Edit: And this doesn't even go into how badly configured Stockfish was. A 1GB hash is nothing for 64 cores of processing power. You're looking at more like 25GB normally. Meanwhile, IIRC AlphaZero had 250GB of memory to use.
      ```

      - u/696e6372656469626c65:
        ```
        Tensor processing units are application-specific integrated circuits, and as such are not directly comparable to CPUs. You're attempting to draw a comparison between apples and oranges. Moreover, even if we accept that Stockfish was at a hardware "disadvantage", the absolute number of positions searched per second was still far higher for Stockfish (70 million positions per second) than for AlphaZero (80 thousand). Clearly search speed isn't the bottleneck here, so trying to draw all the focus to the hardware is a red herring in and of itself.

        As far as low hash size goes, you have a point there, but since hash tables are mainly used to speed up search by cutting subtrees off of the main search tree, it hardly makes much of a difference since, as I already pointed out, Stockfish already had a tremendous advantage in terms of search speed. After pointing out that SF's hash was abnormally small, however, you again go astray by attempting to compare the SF's 1GB *hash* to AlphaZero's 250GB *memory*, which it could have been using for anything. Apples and oranges.

        Moreover, *even if everything you said were true*, this still does not validate your initial statement that "evening out the processing power" (whatever that actually *means*, considering that the number of FLOPs per second isn't a good measurement when comparing general-purpose CPUs to ASICs) would "definitely put the game in Stockfish's favour". You have no evidence in favor of that or any other conclusion; the best you could say is that it *might* favor Stockfish more. (Though personally I'd bet against that as well.)

        **EDIT**: Moreover, this

        > For reference, Stockfish playing against itself with 1/90th of the processing power is a stomp.

        is a context-dependent statement that may or may not be true. Stockfish with 1 core playing against Stockfish with 90 cores is indeed, as you say, a "stomp", but computational power faces diminishing returns in playing strength. Stockfish with 100 cores, for instance, would draw most of its games against Stockfish with 9000 cores.
        ```

        - u/Flag_Red:
          ```
          You seem to be equating computing power used to positions searched. The reason AlphaZero searches so few positions is because it uses boatloads of processing power elsewhere (in the NN calculations).

          A very simple way to even out the computational power they have is by putting them on the same hardware, just like we do in every major computer chess tournament. Put AlphaZero on a 64 cores of the same CPU given to Stockfish and you'll see that reducing an engine's processing power to 1/90th of what it was severely hinders the engine's performance. 

          Neural networks are great and all (I'm an AI researcher, I build them all the time) but they only became viable recently because of the abundance of processing power available now. The fact remains that they require far more processing power than any other classification or regression algorithm used today.
          ```

          - u/Ilverin:
            ```
            Just a note that processing power is slightly more complicated. Google's tensor processing unit uses something similar to minifloat (8-bit float) so FLOPs aren't the same as with normal hardware. Personally my favorite comparison is with total hardware cost when comparing 2 different kinds of data type. 

            Unfortunately we don't know how much Google TPUs costs. According to http://www.cdrinfo.com/Sections/News/Details.aspx?NewsId=62788 AlphaZero only ran on 4 TPUs (less than 1 TPU pod). According to this comment this is less power consumption than Stockfish: https://www.reddit.com/r/chess/comments/7i8419/cb_article_on_alphazero_suggests_alphazero_is/dqxbimp/

            Datatype used in tensor flow (not learning part, the performing part): https://www.tensorflow.org/performance/quantization
            ```

      - u/Veedrac:
        ```
        The two were playing under roughly similar thermal envelopes, which is effectively the important measure for potentially-commodity hardware. That a TPU does more TOPS (*not* TFLOPS; it doesn't do float) is simply a trade in hardware design; a CPU handles inhomogeneous control flow and complex instruction, whereas a TPU is specialised for purpose. That the TPUs were more expensive is mostly a product of their low production volume.

        Stockfish could no more run fast on AlphaZero's hardware than AlphaZero could run fast on Stockfish's.

        E: Second generation TPUs can do float. I don't know how fast.
        ```

  - u/Veedrac:
    ```
    > https://i.imgur.com/JQQXl9J.png
    >
    > Figure 2: Scalability of AlphaZero with thinking time, measured on an Elo scale. **a** Performance of AlphaZero and Stockfish in chess, plotted against thinking time per move.

    As you can see, the asymptotes are different. Since the x-axis is a log plot, a constant factor difference in hardware throughput corresponds to a horizontal translation. You can see that you would presumably need a translation of much greater than 100x (about  2/3 the width of the graph) for Stockfish to catch up in this range, and because the asymptotes are different this would not hold for long.

    I am not sure how hash tables come into this, but I believe making it larger would only act as a small linear speed improvement, so the above analysis holds.

    In other words, AlphaZero is intrinsically stronger in the limit of feasible computation.
    ```

  - u/696e6372656469626c65:
    ```
    > would definitely put the game in Stockfish's favour.

    I do wish people would be less eager to make sweeping claims like this with no evidence whatsoever to back them up.
    ```

- u/veruchai:
  ```
  After AlphaGo came out, there were obvious questions about chess and as a (lower class) chess player I was waiting for something like this to be obviously good. I *was* however expecting a NN to optimize using the far larger electronic infrastructure of chess in contrast to Go. Surpisingly it seems they have gone for the complete from scratch method which I suppose is the more interesting method. Throwing away years of documented optimization, not even using it as a kickstart, in favor of avoiding local minima is not something I would have chosen with my hardware to say the least. 

  Looking forward to seeing how this pans out.
  ```

- u/monkyyy0:
  ```
  Friendly reminder, alphago was still mostly a min max algorithm.

  I would bet money that fairly low elo human networks using the same minmax tree systems would still beat it. Given that is against the hype that experiment wouldn't happen, but eh. What you going to do.
  ```

  - u/EliezerYudkowsky:
    ```
    False.  AlphaGo Lee playing at zero depth played at an extremely strong level, I forget what exactly.
    ```

    - u/monkyyy0:
      ```
      If your talking about the expert move prediction that's not quite my criticism; knowing the top 5 best moves is not the same as picking the best of them because of something that can happen 5 moves from now.
      ```

      - u/thrawnca:
        ```
        If you iterate enough times, the distinction between the two becomes quite narrow.
        ```

    - u/None:
      ```
      I think it was about 3 or 5 dan amateur, so it was strong but not pro level (for Alpha Lee at least). I'd guess Zero with no search would still be pro level.
      ```

  - u/serge_cell:
    ```
    No. It use tree evalution to train neural network and use the same neural network for evaluation on the leafs of the tree recursively.
    ```

---

