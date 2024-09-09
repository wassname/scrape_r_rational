## Google's AI Kill switch - Thoughts?

### Post:

[Link to content](http://intelligence.org/files/Interruptibility.pdf)

### Comments:

- u/Charlie___:
  ```
  This is basically Stuart Armstrong's M.O. Figure out ideas that one could implement in idealized situations that will cause idealized AIs to allow themselves to be turned off. I think it is absolutely great that there is someone doing this.
  ```

- u/Sailor_Vulcan:
  ```
  is it at all likely for the kill switch to *actually* work?
  ```

  - u/rhaps0dy4:
    ```
    This is what I understand so far:

    * They define a criteria for which a policy (roughly, the action the agent will take in each state) is "safe", that is, it does not think that killswitch will be pressed
        * They prove that the optimal policy when there are no interruptions always fits this criterion
        * That the optimal policy accounting for interruptions does not *necessarily* fill this criterion
    * They design agents based on current RL algorithms (Sarsa, DeepMind's Atari player's algorithm is basically a neural network tacked on to Sarsa) and on hypothetical superintelligences (some variation of AIXI)
        * They prove that these agents only consider policies that fill the criterion (am unsure, didn't read yet)

    So now you have a maximiser that will *not necessarily* impede the function of the button. If, say, it needs to demolish the building the button is in to put computronium, it still will. But it will not attempt to prevent humans from pressing the button, because it assumes the button will never be pressed again.

    It's not enough, but it's a good step.
    ```

- u/CouteauBleu:
  ```
  I didn't understand the math, but beside that, I'm not sure I understood the underlying reasoning either.

  The example they give is "A robot can choose between working inside which has a low payoff, or working outside, which has a high payoff unless it rains, in which case we may need to interrupt it. We don't want it to take that fact into account, so we need to change the structure of the program so that the robot always forgets it's been turned off". Unless I misunderstood the example (for instance, maybe they want the robot to take the rain into account, but not the switching off?), extracting the turn off from the robot's utility function is counter-productive, because it will encourage the robot to always go outside, instead of considering "going outside" as the high-risk, high-reward task it is.
  ```

  - u/MultipartiteMind:
    ```
    If I understand correctly, they want the robot to always try to carry boxes outside as though nothing would interfere (they're relying on a human to stop it when there's rain) instead of always hiding inside, which would get more done (but nothing done outside) if no humans were involved.  There's also the perspective of wanting to manually switch it from high-throughput 'outside' to lower-throughput 'inside' only when there's rain, which they're assuming the robot can't detect by itself.  (I'd prefer to just give the robot rain-detection functionality, or a wireless connection to a rain detector.)

    I remember a similar concept before regarding self-copying:  if the robot knows about the killswitch, then it may use shady methods to stop it from being used.  If it doesn't know about the killswitch, then it won't reproduce the killswitch went making new agents.  One approach there is to allow self-modification of pretty much everything except for an unknowable 'black box' which contains both the killswitch and a critical component, and has to be copied exactly without comprehension.  The failure path there is for the robot to (through trial and error, or reverse-engineering) design something knowable that can replace the black box's critical component, then use it to replace the entire black box for efficiency.

    Thinking about the imagined scenario in this case gives me an amusing mental image of a factory worker, about to leave on Friday night, captured and chained to a wall because the robots have realised they would be left turned off during the weekend otherwise (and so only dismally satisfy their utility function!  Oh no!  *laughs*).

    More generally, there's the perspective of 'Don't give agents such simplistic utility functions!', like a certain book's AI that sent a payload of ore flying through the air because it would be faster than by railway, but maybe it's appropriate if it's an agent designed to function in only a very specific niche.
    ```

---

