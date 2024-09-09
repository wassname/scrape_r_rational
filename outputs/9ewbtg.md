## What Would You Ask an Oracle?

### Post:

You have access to an Oracle Machine and can present it with any valid decision lproblem (yes or no question with a valid answer) in natural language. The Oracle Machine will invariably give you the correct answer. What question(s) do you ask to maximise your utility? (Once you finish your question(s) the Oracle banishes itself from existence and forbids it (or a similar oracle from ever existing again).    
   
There are a few ways to interpret the premise, so I'll define two axes along which the question can be interpreted:   
  
1. You can only ask the oracle **one** question.    
2. You can ask the Oracle one question every hour (arbitrarily chosen to prevent access to the Oracle from being too broken, while being significantly more powerful than in the first scenario).    
  
a. The Oracle is omniscient and can answer correctly even in questions involving truly random phenomena.    
b. The Oracle is only nigh omniscient and cannot predict truly random phenomena, but can completely predict all deterministic phenomena.   
   
A question like this has been done before, but I thought it was too I'll defined when I read it and with too much potential for abuse (author added several extra patches to prevent certain kinds of munchkinry). I thought of this as a more sensible version but never got around to posting it, before a certain fic I read made me revisit the question.   
&nbsp;    
Answers format should be prefixed by "**Scenario (x,y):**" (where x is from {1,2} and y is from {a,b}).   

Scenario (1,a) is the scenario that I find most interesting.    

### Comments:

- u/SkeletonRuined:
  ```
  Scenario (1, a): Since it's natural language, maybe try for some linguistic tricks. "Is the following true: I will win the lottery tomorrow if and only if you answer my question with 'yes'?"

  Scenario (2, b): You can probably get pretty far just asking a series of "Is the first bit of the smallest possible computer program to accomplish X a 1?", "Is the second bit of the smallest possible computer program to accomplish X a 1?", etc. This only transfers data to you at 24 bytes per day, but might work depending on how small truly optimal programs are. (We have some reason to suspect they are tiny but unfindable - finding the smallest version of a program is provably uncomputable in general. But the Oracle could know it!)
  ```

  - u/None:
    ```
    (1,a): The oracle wouldn't answer if the question doesn't have a truth value. This isn't a hack but is part of the specification of Oracle machines in general. They can solve every decision problem but not all problems qualify as decision problems. That said, I don't really get the question I guess. Supposing you were going to win the lottery anyway it would answer "yes", and if you were going to lose, the oracle would answer "no"? That sounds too simple a resolution, so I suspect I'm not fully understanding the question.  
    &nbsp;    
    (2,b): I made it a 1h limit to prevent this, but it seems I wasn't sceptical enough. Also, what would the program run on? Software that run on modern computers are pretty bloated aren't they? Can a few KB software usefully run on a modern computer? There's also the fact that payoff would most likely be in years. I think I'll update to a question a day if this is still possible.   
    &nbsp;
    ```

    - u/VirtueOrderDignity:
      ```
      > Also, what would the program run on? Software that run on modern computers are pretty bloated aren't they?

      You could make up a virtual machine with arbitrarily small and terse instructions to get around this, then specify an optimal program on said virtual machine. As a first attempt, you might include an algorithmic random number generator that can provably reach a number of arbitrary-length sequences exponential to the length of the seed, then use the oracle to guess the seed of a much longer program.
      ```

    - u/Ristridin1:
      ```
      (1,a): The trick is in the "if and only if". Let X be the statement "I will win the lottery tomorrow", and let Y be the statement "you will answer my question with 'yes'". Then X if and only if Y means that if X is true, then Y is true, and conversely, if Y is true, then X is true. In other words, X if and only if Y means that both have to be true, or that both have to be false.

      Now, if the answer to the question is 'yes', then this answer says that X is true if and only if Y is true. On the other hand, Y is true, and therefore X is true, so you will win the lottery.

      Conversely, if the answer to the question is 'no', then Y is false. If X were also false, then the answer to the question should be yes (since FALSE <=> FALSE is a TRUE statement), but since it is not, the only remaining case is that X must be true.

      In either situation, X is true. You basically force the oracle to answer the question in a way that implies you win the lottery.


      ...


      Or at least, that's what Scenario (1,a) is intended to do. It actually breaks if the oracle does not assume X is completely determined and always answers 'no' to this question. Namely: If you win the lottery, the oracle answers with no, and if you don't win the lottery, the oracle also answers with no. Then certainly Y will be false regardless of whether or not X is true.

      I think that issue can be fixed by changing your question: "Is the following true: I will win the lottery tomorrow OR you will answer this question with 'no'" (revised from a comment by Yudkowski in a similar thread). If the answer is 'yes', then the second statement is false, therefore the first has to be true (an OR-statement is true if at least one of the statements is true). The answer 'no' cannot be given, since if 'no' is given, at least one of the statements is true, meaning the answer would have to be 'yes'.
      ```

  - u/Linearts:
    ```
    24 bits per day, not bytes.
    ```

  - u/Ozymandias195:
    ```
    If there’s 26 characters in the English alphabet, plus a space, could you not just use your method to create a program to output a textual answer to a question with a non yes/no answer? Like if you asked  “If I created a program that outputs the name of the substance that can cure cancer, would the first character of the output message be A?” And repeat every hour, you’d get approximately 11-12 characters a day. Depending on how you frame the question you could probably get full sentence answers in a few days. I also don’t understand computers too well so please tell me if this is totally stupid
    ```

    - u/ddejong42:
      ```
      You could speed this up with a binary search - start with the question of "Is the first character something between A and M inclusive?" and narrow it down that way.
      ```

      - u/Ozymandias195:
        ```
        That’s smart, there’s probably ways to make it go even quicker by analyzing which letters are more likely to proceed others
        ```

        - u/None:
          ```
          Yeah, and that sort of analysis shouldn't be too difficult. I think this is a nice, new solution.
          ```

          - u/Ozymandias195:
            ```
            Also going on, if we ask if FTL travel is possible, and the answer is yes, we could get our program to write a step by step guide on how to achieve it. It could take millennia with this method but we could also ask if humans could possibly achieve FTL autonomously and if so if it would take longer than using the oracle, and if yes the oracle method would be worth it despite taking so long
            ```

    - u/None:
      ```
      The truly optimal approach is to ask the oracle to generate the bits of a piece of compressed text. For example, a very simple form of compression is dictionary compression where the oracle just outputs the offset of the word within a dictionary. In practice we would probably use one of our more sophisticated text compression methods, which can achieve very low bit per word rates.
      ```

  - u/SkinnyTy:
    ```
    Make X a precise model of existance. It would be slow, but you might learn a lot about the nature of our universe which may reveal shortcuts to infinite energy or some other important game breaking piece of info.
    ```

- u/CCC_037:
  ```
  (1, a)

  Hmmm. You want maximum beneficial effect from a single bit of information - in effect, a single yes/no answer.

  So, first of all, let's consider how to maximise the effect. The biggest thing that you can do - the thing that will have the most far-reaching effect - is to completely change the direction of your life.

  Therefore, ideally, you need two possible lives. For example, you might consider life as an author, writing inspirational stories that encourage others to action; or you might consider life as a scientist, expanding and exploring the realms of knowledge. There are thousands of potential paths a life can take; so you pick the two options most suited towards your personal talents and abilities.

  Of these two potential life paths, pick one. Doesn't matter too much which one. (Let us say that, for example, I pick 'novelist').

  Then the question is, "Will it be more beneficial for humanity in general, over the long term, if I were to spend the rest of my life as a novelist?"

  If the answer is yes, I become a novelist and attempt to write and publish stories.

  If the answer is no, I become a scientist and work on expanding the bounds of what knowledge is known.

  Since the oracle can predict even random phenomena directly, the oracle can therefore see which of these two options is more beneficial to humanity in the long term and thus allows me to pick the best option; and the potential scope of the consequences is huge...
  ```

  - u/None:
    ```
    That's a different route than others have suggested, and I like it. Not sure I'd ask that question personally myself.
    ```

- u/hyphenomicon:
  ```
  Even in scenario 1, preserving indirect access to the Oracle Machine for future questions, perhaps through controlling other people's questions, would be an obvious goal. So let's further specify that the Oracle disappears from existence, and forbids itself or a similar Oracle from ever existing again, after you finish your question.
  ```

  - u/None:
    ```
    Thanks, I will add that.
    ```

- u/ashinator92:
  ```
  There was a biweekly prompt that was related to this, i think :). It uses a time machine instead of an oracle, but close:

  [https://www.reddit.com/r/rational/comments/8daskl/biweekly\_challenge\_complexity/](https://www.reddit.com/r/rational/comments/8daskl/biweekly_challenge_complexity/)

  &#x200B;

  &#x200B;

  Shamelessly copying from /u/xamueljones post:

   [For God-like power, all I need is one bit](https://docs.google.com/document/d/1UiGUYFm3CfO_6Z_dDIZUsU3P4izjY6FAOq6BGLbeIMk/edit#heading=h.b3ly0s8pl1qo) (5405 words)
  ```

- u/SimoneNonvelodico:
  ```
  "Are you really a perfect Oracle?"

  No, seriously. Uhm. Being just a Yes/No question it's kinda hard. You can't crack any serious problems unless you already have a very good hypothesis in version 1), and version 2) still limits you a lot due to the one hour interval. And with a lot of questions ("Is immortality possible?" "Can we travel FTL?") I suspect the answer would be a discouraging and rather bleak "No", which far from being very useful, might in fact be something I'd just rather not know for sure. You can't even use this damned thing to, say, prove Riemann's hypothesis, because it's not like it will give you the demonstration, and no mathematics journal will accept "the Oracle told me" as a viable "Methods" section in a paper.
  ```

  - u/Ozymandias195:
    ```
    I think as far as benefitting humanity, it would be extremely beneficial to know whether FTL is possible. Why pour massive resources into something when we can definitely prove it doesn’t exist? Similarly for asking whether certain diseases can be cured
    ```

    - u/SimoneNonvelodico:
      ```
      Asking "can cancer be cured" would probably produce a pointless answer. Cancer isn't a single disease, and of course it *can* be cured - we cure it already, it's just not 100% reliable (but then, what is?). Knowing if FTL signalling is possible would certainly be an interesting constraint to any theories in the future, but it suffers from the problem of many other such questions - it's much more useful if the answer is "yes" than "no". Ideally, I think I'd want to ask one question where knowing is *always* useful, either way.
      ```

      - u/Ozymandias195:
        ```
        Asking if there’s a cure for cancer is a bit too simple, but something like “is there a universal treatment for all cancers with a 90% or higher success rate” might prove useful. And it’s indirectly useful to know whether certain things are impossible, despite not having direct utility like if they are
        ```

        - u/SimoneNonvelodico:
          ```
          I think that might be valuable for the "one question per hour" Oracle. But I wouldn't make it my only question ever. Also because, at a difference with knowing that FTL signalling is possible (which at least implies there is something fundamentally wrong with our knowledge of physics), such a cure isn't intrinsically impossible, so knowing that it exists tells us nothing really interesting or that can help us find it.
          ```

- u/CreationBlues:
  ```
  Can the Oracle control the timing of it's response? Ex answer yes at 1 am for 0, answer yest at 1:01 for 1, answer yes at 1:02 for 2, etc.
  ```

  - u/None:
    ```
    Nope. You're supposed to extract maximum utility from a single bit of information.
    ```

  - u/alan_wade:
    ```
    Holy fuck that's brilliant.
    ```

- u/Caliburn0:
  ```
  Scenario 1.a and b

  Well, first off I would consult with a whole bunch of people about what I should ask it. And when enough people have come to a consensus I would ask the question we came up with, but since that is kind of the point here, my question would be:

  *Is the universe (and by universe, I mean all of existence) infinite?*

  Scenario 2.a and b

  I'm a bit of philosophy and physics geek, so I would probably continue asking it questions about the universe in general.

  In order to earn money from it, I would offer people to ask their questions to me so I can ask the oracle.
  ```

- u/meangreenking:
  ```
  Senario (1,a): This one is pretty tough. It shouldn't be too hard to use the question to make a bunch of money via a onetime bet on some future event, but that's about the best I could do with it.

  I could use it to satisfy some scientific question, but then the issue is that no one would ever believe me so all it would do is satisfy my curiosity. I could use it to answer some personal question (eg. will I live to be 100) but that would be meaningless given that with a mere 1 bit of information I would be unable to even attempt to change the results in any way.

  So honestly, I would probably just use it for making money. I would take out a bunch of loans and heavily overextend myself to make a bunch of money on sports event.

  Senario (2,a, b): This one is much more interesting, and far easier to exploit.

  The first thing I would do is ask some questions to ensure I don't die in the time leading up to getting my more important questions done. The chance of death over the time it would take for them to be answered to be answered is fairly small but nontrivial, especially when the rewards would eventually end up with me immortal and by far the most powerful person on earth.

  After that I would basically just ask it what the best question for me to ask it would be. Doing so would of course have to be changed a bit for the format of a yes/no oracle, but could fairly easily be done with "What is the [xth] bit of the ideal question set for me to ask you under 100 characters done in this same format for me to ask you translated from english into bits with yes being 1 and no being 0?"

  Since its omniscent it would logically know what the best question set for me to ask it better then I ever could. Getting the result back of the question it would give me to ask it would take a while but the return would be far better then anything I could think up on my own.
  ```

  - u/None:
    ```
    Well I guess you solved scenario 2. I'm Scenario 1 isn't the best you can do around doubling your money? You'd be able to half your search space in any problem, but that's the best a single bit gives you. To reliably profit on bets that involve more than 2 outcomes you'd need to have pruned your search space already.
    ```

    - u/meangreenking:
      ```
      Without loans yes, the best you are functionally do is doubling your money.


      However if you are willing to take what would otherwise be crippling amounts of debt that would otherwise be utterly impossible to repay you could do quite a bit better.

      For instance I would take out a mortgage loan for a house that the bank would be barley willing to let me get with my current salary (and that would represent decades worth of my income) and then use it for the bet instead of buying the house. On top of that I would take out tens of thousands of dollars in credit card debt and as many other less reputable loans (payday loans, loansharks) as I could.

      Finally I would use leverage (which is basically using other people's money to invest in the stock market/bet at a ratio of your own money) to increase my return even further.

      Honestly as long as you aren't currently in debt and people are willing to lend to you it shouldn't be all that hard to get a 10-20x return on your current annual income even if you had no hard money on hand.

      Plus thanks to the fact that the oracle can tell the future, you don't even need the money or a job now, all you would need is to get it by the time your answer to the question happens.
      ```

      - u/None:
        ```
        Fair enough. If I could partner with someone much richer than me, I could give them a chance to double their money (say even bet of several million dollars), and they would give me a cut (which would still be in the millions). Convincing them of the Oracle's power would be quite difficult though.
        ```

---

