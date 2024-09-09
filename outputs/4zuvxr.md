## First weekly munchkinry and problem solving thread!

### Post:

Let's do something simple for today! You have the power to perfectly fool someone into thinking that you are someone else. But only once and only for fifteen consecutive minutes before your power leaves you, forever. There is no upper limit on how many people the power can affect at once.

What's the worse you can do?

Or alternatively here is a challenge a character might face in a fictional world. This character, let's call them A. A has two doors before them. One leads to death and the other to riches. There is a guard before each door. One guard always lies and the other always tell the truth. A doesn't know which is which. What should A do?

I apologize for the rather rushed challenges. I was supposed to prepare them beforehand but something came up. Sorry.

Edit: I'm an idiot who forgot to specify the rules for the knight and knave puzzle. You only get two questions and you can't ask the following questions.

If I asked you if the door you're guarding leads to where I want to go, would you say 'yes'?

If I asked the other guy if the door he is guarding leads to where I want to go, what would he sat?

### Comments:

- u/None:
  ```
  [deleted]
  ```

  - u/vakusdrake:
    ```
    I was just about to say that but you beat me to it. Though you might be able to do better claiming to be some super intelligent alien from some ill-defined higher plane or something like that.     
    Picking a figure from a preexisting religion would basically confirm that religion and would likely stunt societies ideological development.
    Plus confirming a fundamentally unreasonable belief system would not do great things to people's rationality even with all the stuff you try to stick into the new new testament.
    ```

  - u/ansible:
    ```
    "When I said 'created in God's image', I was talking about your mind. And I expect you to use it to the fullest extent. And not just blindly follow rules that don't have a solid and rational justification."
    ```

- u/Zephyr1011:
  ```
  Surely giving two questions to the knights and knaves puzzle makes it trivial? Ask a question like "Is 1-1=0?" and the response tells you which guard it is, then ask which door to go to.

  It's a moot point anyway, as you can ask: "If I asked you if I should go through your door, what would you say?" and the answer is always truthful
  ```

  - u/gods_fear_me:
    ```
    You know what, I fucked up. The next week I will make proper scenarios. Just ignore the knights and knaves puzzle for now.
    ```

- u/xamueljones:
  ```
  I'll post a challenge of my own here. It's an interesting computer science problem disguised as a logic problem. I'll post the answer late on Sunday or Monday morning.

  > You are someone who works for a company who needs to find out how durable a new container actually is. But you're bored enough that for kicks and giggles, you're going to find out by throwing the containers out of the windows of 200-floor skyscraper you work in. If it survives the fall from the Nth floor and not from the N+1th floor, it's a good enough measure of it's durability for your company. Unfortunately, someone screwed up your order and you only got 2 containers instead of the 200 you needed and time is short.

  > You only have the two containers in your hands and you are standing in front of the 200 floor building. You want to know the highest possible floor the containers can handle falling from before breaking. But you need to minimize the number of tries you have to save on time before the very important meeting in 4 hours (it's going to be time-consuming going up and down stairs to retrieve the containers you're dropping out the windows).

  UPDATE: You don't know which floor the containers will break on, so while you can skip testing the first few bottom floors to save on time, it's a risk. So assume that the containers are equally likely to break on any floor.

  Also, I worded the problems slightly poorly. You want to minimize the number of tries since it's very stressful to worry if the containers will break or not. You prefer two tries throwing the containers from the 200th floor than three tries from the 1st floor. Going up and down the stairs is not a problem.
  ```

  - u/None:
    ```
    [deleted]
    ```

  - u/TwoxMachina:
    ```
    An important point to use: Cycle your containers.

    Say, drop 1st container at 20th floor. Drop 2nd at higher floor before going down to grab both at once. Cuts your movement by half.

    EDIT: I'd say to attach a chain for quick retrieval, but will probably affect the results/
    ```

  - u/PlaneOfInfiniteCats:
    ```
    We need to know an *exact* breaking threshold at the end of an experiment.

    Therefore, if we only have 1 container, our only choice would be trying to throw the container from every window starting from first floor, incrementally.

    However, we have two containers.

    I have already shown that no optimization is possible for 1-container case. With two containers, once our first container breaks, we will be stuck with 1-container case. So, all optimization must be in use of first container.

    There is some floor number N that lies between upper bound (200) and lower bound (1)
    If we throw our container from i-th floor, either it doesn't break and we know N>=i (and can try throwing again), or it breaks and we know N<i (and have to resort to iterative testing with remaining one container)

    Now, we need some more clarifications.

    * Do we think that breaking threshold is equally probable on every floor?
    * Is time cost of floors proportional to floor number? (does throwing container from 30th floor take 3 times longer than throwing it from 10th floor?)

    We should try maximizing average reduction of range where N lies with first container, then do iterative tasting of entire range with second container. The specific algorithm for first container depends on the answers to questions above.
    ```

  - u/gods_fear_me:
    ```
    How much time does it take to retrieve an undamaged container dropped from say, 100th floor?
    ```

- u/Jiro_T:
  ```
  http://tvtropes.org/pmwiki/pmwiki.php/Main/KnightsAndKnaves
  ```

- u/Murska1FIN:
  ```
  As for the obvious solution to the latter one, ask both guards 'If I asked the other guard which door holds the riches, what would he say?'. Then pick the other door.
  ```

  - u/Sparkwitch:
    ```
    As guards, both are theoretically meant to protect the riches. There are a lot of unrelated things either guard could say that are true or that are false which would protect the identity of what's behind which door.

    Capable security, even stuck with only one truth-telling and one lying guard, would make sure they're instructed not to answer questions.
    ```

- u/Sparkwitch:
  ```
  On the first, it's important what happens after the fifteen minutes is up.

  Does the belief disappear afterwards, or only your ability to continue influencing? If it lasts, then when people meet you again after your fifteen minutes, do they recognize you as the pretend person (only to be dissuaded as they get a chance to interact with you) or do they recognize you and not know why, do they recognize you as a giant fraud, or do they not recognize you at all?

  Does the power work over video or audio broadcasting channels... and (if so) does that broadcast then work as a believable fifteen minutes forever or does it immediately seem absurd afterwards?

  Also: Do you have to be a specific individual or can you be a generalized ideal: The Creator of the Universe, your most trusted friend, your own great-grandchild time traveling from the future?
  ```

  - u/gods_fear_me:
    ```
    Generally lasts but there are exceptions. You can't convince everyone forever that you are a giant fire breathing dragon unless you establish while using your power that said dragon has shapeshifting capabilities. Abusable I know but that's exactly what this thread is supposed to be, albeit things may get significantly less broken in the future.
    ```

- u/Nighzmarquls:
  ```
  Does this power work over broadcasts and recordings?

  Can it be adaptive to the person such as "I am the person you respect most in the whole world?"

  There is a lot of possibilities if it's more flexible or adaptive
  ```

  - u/gods_fear_me:
    ```
    Adaptive.
    ```

    - u/Nighzmarquls:
      ```
      Then I think the most powerful thing I could say is "hello In this moment I am the one who will tell you the most important truth about yourself. You have always wanted to work together to make the world a better place. You have not always succeeded. You can't always know what will make the world better. But multiple points of view will help. Even ones you disagree with. Even ones you hate. After I am done talking I will not be able to yell you more truths about yourself. And will just be another person trying to work together to make things better" getting that broadcast to as many people as possible would be good.  If it works in recordings using it as a viral meme tic contagion would be best otherwise I need to get myself broad cast to the majority of China or india.
      ```

      - u/gods_fear_me:
        ```
        Recordings would still work. And I declare you the winner.
        ```

        - u/Nighzmarquls:
          ```
          To be fair this particular question is the kind of thing I've been playing with for one of my stories so I kind of had a lot of cached brain work to pull on to bring to bat for this.
          ```

- u/None:
  ```
  A more interesting variant of the knights and knaves puzzle I once heard runs as follows:

  There are three statues.  You know that when asked a yes-no question, one responds truthfully, one lies, and one produces a random response (say based on some long ago recorded data).  Unfortunately, they respond in a language that you do not speak, using the words Da or Ja.  Given three questions, solve which statue is which (and ideally also what Da and Ja mean, though I do not remember if this is part of the problem).

  Silly tricks like asking non-yes-no questions (which only the random statue can respond to) or paradoxical questions (same) should probably not be required.
  ```

- u/xavion:
  ```
  What's the worst you can do?

  Well there was no limitation you could only fool someone into thinking you're a real person, so presumably you could make them think you were Harry Potter or Superman or whoever, and there's no limitation that you need proximity, so can you just make everyone in the city you're in or whatever assume you're Obama or the like. Useful as you can only use it once so being able to indiscriminately use it on everyone prevents people being missed even if they miss the start of your message.

  So what's the worst you can do? Choose some super well known being that means the apocalypse is happening, or just fool people into that. For fifteen consecutive minutes everyone in the world think you are the nigh-omnipotent 15min mark herald of the apocalypse and that anyone alive then will be tortured for eternity or whatever. Now the catch is, if people don't know you exist wouldn't they not know the herald-you exists? Except you've fooled everyone so everyone believes you are them, by the nature of the character and the prompt everyone should know they exist.

  Note if the power is based off something like super social skills it's not as effective at all. As is that requires exploiting some vagueness but in theory it could result in most of the world killing themselves and as many others as possible within the 15mins, since they all now believe the world will end in fifteen minutes and eternal torturefest for the living. Abusing it to basically turn it into a limited power to make everyone on earth believe one thing for fifteen minutes is kinda cheating though.
  ```

- u/masterax2000:
  ```
  I would make people think my name is a list of instructions that describe how to easily and cheaply make a elixir of life (or something like that). I would then ask someone to write down my name for me.
  ```

- u/GaBeRockKing:
  ```
  A gets infinite questions, so fuck the room. Determine which charachter tells the truth, and ask them everything from "does p=np" to "is there a god."
  ```

  - u/Murska1FIN:
    ```
    He can truthfully say 'I don't know'.
    ```

---

