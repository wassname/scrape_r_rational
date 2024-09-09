## [D] Friday Open Thread

### Post:

Welcome to the Friday Open Thread! Is there something that you want to talk about with /r/rational, but which isn't rational fiction, or doesn't otherwise belong as a top-level post? This is the place to post it. The idea is that while reddit is a large place, with lots of special little niches, sometimes you just want to talk with a certain group of people about certain sorts of things that aren't related to why you're all here. It's totally understandable that you might want to talk about Japanese game shows with /r/rational instead of going over to /r/japanesegameshows, but it's hopefully also understandable that this isn't really the place for that sort of thing.

So do you want to talk about how your life has been going? Non-rational and/or non-fictional stuff you've been reading? The recent album from your favourite German pop singer? The politics of Southern India? The sexual preferences of the chairman of the Ukrainian soccer league? Different ways to plot meteorological data? The cost of living in Portugal? Corner cases for siteswap notation? All these things and more could possibly be found in the comments below!

Please note that this thread has been merged with the Monday General Rationality Thread.


### Comments:

- u/None:
  ```
  Due to overflowing disappointment in my own ineptitude and my burning envy towards all the math-savvy people in the rationalsphere, I’ve been self-studying mathematics from scratch.


  My daily routine looks like this:

  * I go through a chapter in a textbook, carefully reading all the definitions and trying to connect them to what I remember from school

  * I try doing all the examples myself, before seeing the explanation

  * at the end of the chapter, I solve at least 5–10 exercises

  * in my spare time, I look up the same material on youtube/math stack exchange/reddit, seeking intuition and understanding

  * every ~10 chapters (usually taking advantage of general sections in a textbook, e.g. ‘Quadratics’ or ‘Right Angle Trigonometry’), I enter a card into Anki with a ‘Do x exercises from every chapter within section y’ instruction towards my future self.

  * I look up Anki every day, and do whatever it instructs me to do. After doing all the ‘review exercises’, I click on ‘Good’.

  * similarly, I enter hard-to-memorize formulas and theorems into it.



  The textbooks I’m currently using:

  * Beginning and Intermediate Algebra by Tyler Wallace (100% done)

  * Elementary College Geometry by Henry Africk (~80% done)

  * Trigonometry by Michael Corral

  * Precalculus by Carl Stitz and Jeff Zeager



  (...and I’m still lazily researching textbooks for calculus, linear algebra, and further maths.)


  Are there any large flaws in my methods? Similarly, are there any things I could be doing that would boost the effectiveness of my learning? I’m mostly focused on maintaining my knowledge over large periods of time—this is my primary intention with using Spaced Repetition, but Anki is clearly not designed for subjects like math and I can do only so much with it. One of my biggest fears is spending time and effort learning something only to forget it, so if you have any suggestions in this area, I would be grateful.
  ```

  - u/suyjuris:
    ```
    First of all, it seems you are doing great! Very impressive!

    In my experience, both learning mathematics and trying to help others learn, the most important part is practice, and you already do a lot of that.

    Another thing that really helps is explaining things to others. I think the biggest danger is having the feeling of understanding something, while not actually having grasped all of it. While certain kinds of knowledge, like  how to calculate the area of a polygon, can be tested easily by doing exercises, others, such as “why do the angle bisectors of a regular polygon meet at a single point” are more difficult. The further you go in mathematics, the more the latter is going to matter. Being able to explain things seems to be a pretty good indicator of understanding.

    Obviously, finding people to explain things to might be difficult. However, talking to yourself can be a fine alternative, depending on your skill to be self-critical. Another possibility is writing things down as though someone else might read it. Just having the mindset is important.

    Looking at your textbooks, it seems to me you are currently focussing on fundamental techniques and less on proofs. Exercises containing the word "prove" are really quite different from ones that do not. So, I would recommend trying to figure out what interests you and then try to move into that direction in  the long run. While proofs and logic are certainly at the heart of mathematics, they might be less important if you are looking for certain applications.

    Personally, I really like logical thinking, proving things and programming things, and these are basically the same activity for me. When I am trying to understand something, I always try to poke holes in the arguments (“Why do we need this line?”, “Does it still work if X is not Y? Where does it fail?”) and start by attempting to do it on my own. Also, I am not afraid of forgetting, because logic is something I apply all the time when thinking about whether things are true or whether an argument makes sense.

    I would not worry about forgetting facts. Things that are useful will be used and thus not be forgotten and the things you had understood at some point still helped you to get better at understanding things.

    Final point: Take care to be challenged. Solving difficult problems is a much more efficient way to improve then easy ones.

    In that sense, I leave you (and anyone else reading this) with a “simple” puzzle I have just been working on: [Image](https://imgur.com/KPptBZM) Can you fill the squares of the number pyramid with whole numbers, so that each square is the sum of the two below it? (No negative numbers.)
    ```

    - u/blobbythebobby:
      ```
      [I think I got it?](https://imgur.com/JoSbtmM)

      I felt like I should have used a diophantine equation towards the end, but I couldn't remember how to do them, so I sorta brute forced the last few steps.

      A good all-round exercise in discrete mathematics.
      ```

      - u/xamueljones:
        ```
        I got the exact same answer as you did. I basically brute forced it sorta since the entire pyramid is completely determined by the bottom row.

        The entire comment that follows is all about how to solve the problem through intelligent brute-forcing without any knowledge of advanced math!

        First I made a smaller pyramid with only 17 at the top and 7 at the bottom right corner of a row with only 4 numbers. First I tested to see how fast the top number would grow if the bottom layer goes from <1, 1, 1, 7> to <2, 2, 2, 7> so I could estimate what triple would reach 17. Funnily enough, <1, 1, 1, 7> gave 14 while <2, 2, 2, 7> gave 21 which mean the real answer was in between the two. <1, 2, 1, 7> and <1, 1, 2, 7> both worked to generate 17 as the top number. So I then moved on to the second pyramid to test while (for now) assuming the first row to be <1, 1, 2, 7>

        The second pyramid I made was simply a pyramid with 45 at the top, 6 at the bottom left corner, and whatever numbers <1, 1, 2> generates by being at the bottom right corner.

        <45>

        <?, ?>    


        <?, ?, 5>    
        <?, ?, 2, 3>    
        <6, ?, 1, 1, 2>    
        Since the number 45 was a lot higher than 17 and there was only one more row compared to the pyramid above, I knew that the number next to 6 had to be a lot higher than 1, so I decided to test by filling it in as 6 and if the top number was higher or lower than 45, I would try again with 5 or 7. <6, 6, 1, 1, 2> generated 42 and <6, 7, 1, 1, 2> generated 46.              
        Since getting 45 as the top number was clearly impossible, I knew that the answer for the first pyramid then had to be <1, 2, 1, 7>, and that the bottom row had to be <6, 7, 1, 2, 1> which resulted in 45.              
        By combining the two pyramid's bottom rows, the final answer was <6, 7, 1, 2, 1, 7> which generates 78!
        ```

        - u/blobbythebobby:
          ```
          Yeah I, too, divided it into 2 pyramids. I formulated an equation each for the 2 pyramids, assuming the big pyramid's bottom looks like this:

          <6, x1, x2, x3, x4, 7>

          Inner pyramids' equations:

          45 = 1 * 6 + 4 * x1 + 6 * x2 + 4 * x3 + 1 * x4 

          17 = 1 * x2 + 3 * x3 + 3 * x4 + 7

          (Combinatoric details: these coefficients come from the amount of paths a number can take to reach the top of their respective pyramid, and is calculated by C(layers to climb, left steps required), so for the leftmost object up to 45 it'd be C(4, 0), which is 1 because there is only 1 path that the 6 can take to reach 45: Right, right, right, right. This reasoning might seem far-fetched but it's very close to the reasoning used when relating [pascal's triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle) to combinatorics, which is why I came up with it.)

           After that it got really hard for me to continue the calculation purely formally for me though, as it's very hard to inject the info "The answer has to be a non-negative integer" into a normal equation, something a diophantine equation can do (I think, I never properly learned them. Especially not working with more than 2 variables in them). 

          So I personally explored the small pyramid's equation with this information in mind myself and managed to narrow it down to 

          <x2, x3, x4, 7> 

          where x2 = 10 - 3*(x3 + x4) and x3 + x4 <= 3 and x2, x3, x4 >= 0

          Then came the brute force method, where I inserted a few of the possible small pyramids into the large pyramid's equation until one stuck, and there I had my answer.

          Generally our solutions are quite close. I feel that my knowledge of combinatorics would've been more helpful if you scaled the exercise by a few levels, but it did help me quickly assess the relation between numbers in different levels.
          ```

          - u/xamueljones:
            ```
            Thanks for that! I wanted to know how combinatorics could be used for this problem, but I didn't know how to look that sort of thing up. Thanks for explaining.
            ```

          - u/suyjuris:
            ```
            It is so interesting to see your solutions :) I am kind of surprised how well educated guessing work. My own also gets to these equations

            > 45 = 1 * 6 + 4 * x1 + 6 * x2 + 4 * x3 + 1 * x4
            >
            > 17 = 1 * x2 + 3 * x3 + 3 * x4 + 7

            Which we can simplify to

            4 * x1 + 6 * x2 + 4 * x3 + 1 * x4 = 39

            0 * x1 + 1 * x2 + 3 * x3 + 3 * x4 = 10

            Dropping the variables gives

                x1 x2 x3 x4
                 4  6  4  1 | 39
                 0  1  3  3 | 10

            4 and 6 are even while 39 is not, so we have to use x4 at least once. So lets subtract that.

                     x1 x2 x3 x4
                      4  6  4  1 | 38
                      0  1  3  3 |  7
                     ------------+
                used  0  0  0  1

            7 cannot be divided by 3, so we have to take x2 at least once as well.

                      x1 x2 x3 x4
                      4  6  4  1 | 32
                      0  1  3  3 |  6
                     ------------+
                used  0  1  0  1

            If we were to use x4 once more, then 32-1 = 31 is odd again, so we would have to use x4 at least twice. It would look like this:

                      x1 x2 x3 x4
                      4  6  4  1 | 30
                      0  1  3  3 |  0
                     ------------+
                used  0  1  0  3

            Now the second row is zero, so we cannot use x2, x3 and x4 anymore. 30 is not divisible by 4, so this does not work, and we cannot use x4. Going back:

                      x1 x2 x3 x4
                      4  6  4  - | 32
                      0  1  3  - |  6
                     ------------+
                used  0  1  0  1

            We have to use x2 an even number of times, else the first row is not divisible by 4. It also has to be divisible by 3, else the second row does not work. But if we use it 6 times (the smallest even number divisible by 3), then the first row becomes negative. So no x2 as well.

                      x1 x2 x3 x4
                      4  -  4  - | 32
                      0  -  3  - |  6
                     ------------+
                used  0  1  0  1

            Finally, we use x3 two and x1 six times.

                      x1 x2 x3 x4
                      4  -  4  - |  0
                      0  -  3  - |  0
                     ------------+
                used  6  1  2  1

            I will admit that educated guessing is much easier. But this instance was computer-generated, so it is nice that I can tell a story at all. (Incidentally, the puzzle was created by applying this basically in reverse.)
            ```

            - u/blobbythebobby:
              ```
              To be more detailed about my guessing, I stuck the equations into a matrix as well but I didn't quite know how to algorithmically solve it like you did. I did however end up with this form:

                  x1 x2 x3 x4
                  -4  0  14  17 |  21

              Since I then knew that the sum of x3 and x4 is 3 or less, and that 14x3 + 17x4 = 21 + 4x1, I simply wrote a table of 21 + 4x1, like

              21

              25

              29

              ...

              45

              and all I had to do was test 14x3 + 17x4 against my newly made table for a maximum of 5 times to find the answer.

              I do think that these kinds of solutions are pretty unclean though. The elegancy of math is lost when you start guessing your way forward. It's like solving an algebraic exercise with a graphing calculator. You might get the answer, but your dignity takes some damage.
              ```

      - u/suyjuris:
        ```
        You did! Well done. I have to admit I did not consider using diophantine equations at all, but I will have to look into that. The two approaches I do know of are basically integer linear programming and something similar to multi-dimensional knapsack.
        ```

  - u/RetardedWabbit:
    ```
    Good on you man! I've really wanted to do something similar since I don't have a real grasp on calculus, applied or even understanding equations.

    Your method seems pretty solid as long as you can stick to it, if you can't keep with that I'd look at online lessons that offer problems online. Aside from that I enjoy Khan academy lessons for previews and reviews, but they move too fast for me to learn math from.

    I would also suggest throwing in a statistics book when you want a break, I found algebra based statistics very interesting and not mathematically challenging in the same way. That being said it's still foundational for understanding a huge amount of applied everyday math like QC, gambling, insurances, and warranties.
    ```

    - u/None:
      ```
      Ah, I'm actually dumbfounded I completely forgot about statistics and probability theory. Thanks for the remainder -- I'll make sure to include them in my future studies.

      Considering Khan Academy, I've heard a lot of good things about it, however... It might seem like a petty thing, but I absolutely can't stand their website. It just feels so bloated and opaque to me, you know? And their lectures are pretty computational in nature, from what I've seen. When it comes to this kind of educational material, I found [Eddie Woo's channel](https://www.youtube.com/user/misterwootube) somewhat more useful. 

      Other than that, I think I'll stick to traditional textbooks -- I really like how they allow me to pace myself however I want.
      ```

  - u/VanPeer:
    ```
    That's wonderful! I'd recommend [3blue1brown](https://www.3blue1brown.com/) on Youtube for the most stunningly beautiful insightful math I've seen.

    I also recommend [Calculus Made Simple](https://www.gutenberg.org/files/33283/33283-pdf.pdf) as the best way to introduce calculus, the sort of book I wish I had in highschool
    ```

- u/sickening_sprawl:
  ```
  So I've been playing Destiny 2 recently. Quite a lot, in fact - I basically played it for like a week straight at first, and have now settled down into only occasional 5+ hour stints now that I've hit endgame.

  Something that I've noticed is that the lore is very, very bad. I don't know why so many people like it. It's almost entirely dependent on rule-of-cool handwavium, poorly explained in very badly written lore snippets you have to hunt down from secrets. It has neat *ideas*, but basically doesn't do anything with it.

  The main characters are Guardians, who are given space magic and lichdom from a giant world-travelling acasual entity called the Traveller; they can do weird effects and are raised from the dead as long as their Ghost (small machine thing) exists. They basically just do fuck all for the past several thousand years out of kinda-religious feelings of not wanting to be proactive, allowing humanity to backslide out of a "Golden Age" until the entire solar system is overrun by aliens and humans only have a single city left. The Fallen are galaxy-wide scavaging pirates who are commonly portrayed as dumb as bricks, and mysteriously have left any machine you'd need working just fine despite their scavanging. The Hive as death worshipping omnicidal wizard aliens trying to summon elder gods, and are actually pretty cool except for all their out-of-context magic never actually do anything. The Vex managed to convert an entire planetoid to Computanium to simulate timelines and have a portal nexus spanning an infinite web of parallel realities but don't do anything and basically fall over to a breeze. The Awoken were members on a colonyship expedition, ran into a fight between the Light and Dark acasual entities and were trapped in a timewarped singularity universe where they were postscarcity and immortal, and then the queen reincarnated everyone to a mortal body because they needed to "evolve and live meaningful lives" and because we didn't have enough pro-death JRPG tropes in video games, I guess.

  The entire thing just feels terrible. Even the actual storylines are bad - the entire first arc is diaspora analog that basically amounts to Deus ex machina trust your god bullshit, the first expansion is fighting against post-singularity infinite computation power timeline simulating Vex and winning because the Vex can't simulate Handwavium, the second is waffling AI security that could have been interesting if it felt like there were any stakes and you didn't already activate a Golden Age AI in the first arc, or the AI actually had any character, and the third is a drawn out revenge story after one of your friends is perma-killed that fails to actually hit any of the "are we the baddies" note it was trying to hit, and then switches into a completely unexplained arc with the Awoken that ends with a "ah, I wanted you to kill me! All according to kaikaku" and conscious-of-but-cant-change-events timeloop.

  I'm not even upset about the story. It's just so *disappointing*. If I played Destiny 1 maybe it would make more sense, or if I spent the time reading into the scarce worldbuilding they drip to people so they feel invested like Overwatch and other properties do.

  I'm, uh, not entirely sure where I'm going with this. I'm still gonna play it. Just wanted to rant.
  ```

- u/None:
  ```
  [deleted]
  ```

  - u/None:
    ```
    'Magitech', maybe? It describes almost the same thing as 'Science Fantasy', but I've come across it far more often in the context of High Fantasy with magic-based contemporary technology (magic cars, magic guns, and so on) as opposed to 'Magic in Space' like *Star Wars*.
    ```

  - u/GaBeRockKing:
    ```
    "Science Fantasy" is indeed the term you're looking for. The genre mixes the aesthetic trappings of both scifi and fantasy. There's no reason to exclude star wars from the genre, because the setting does indeed focus on technology and the advancement of science. There's no particular reason space needs to imply technology, but most works that include space travel have some sort of technological focus. I think the only exception is the *Larklight* series, where the british empire expands through the solar system because they have an effectively magical formula.
    ```

    - u/ToaKraka:
      ```
      > There's no reason to exclude star wars from the genre, because the setting does indeed focus on technology and the advancement of science.

      Star Wars focuses *far* more on Jedi and Sith than on Sienar and Incom. Thirty years after the Galactic Civil War, X-wings and (basic) TIE fighters are still being used with only minor modifications (both in the EU and in Disney's canon, IIRC). One-off superweapons and spy tricks that are forgotten immediately after their introduction and whose innovations aren't exploited for other purposes hardly count as technological advancements, either.
      ```

    - u/None:
      ```
      [deleted]
      ```

      - u/GaBeRockKing:
        ```
        If you want the main characters to specifically be doing science as /r/rational readers understand it, then the term you're looking for is "rationalist." If you want the main character to be doinh science as a layman audience would understand it, you're not looking for a genre, you're looking for a character archetype. You can have the MC do science in the context of a murder mystery, a space opera, an epic fantasy work, or what have you.
        ```

- u/FlameDragonSlayer:
  ```
  I was just watching Umbella Academy, im just halfway through, and i found it really interesting.  The rationalist billionaire training the mutant kids really reminded me of this sub and how I imagine X-men should have been in the first place.
  I wanted to recommend it here cause i thoght we could have some interesting discussions about it here and how to munchkin the powers.
  ```

- u/Palmolive3x90g:
  ```
  So there is this website useing an AI that can randomly generate human faces and it's pretty cool.

  https://thispersondoesnotexist.com/
  ```

- u/None:
  ```
  [deleted]
  ```

  - u/LucidityWaver:
    ```
    All on RRL:

    I enjoy [The Daily Grind](https://www.royalroad.com/fiction/15925/the-daily-grind) and [The Draw of the Unknown](https://www.royalroad.com/fiction/21334/the-draw-of-the-unknown), both by argusthecat. TDG has been linked to on r/rational a fair bit.

    I’ve enjoyed the first 10 chapters of [Esper: Search for Power](https://www.royalroad.com/fiction/21353/esper-search-for-power), but can’t wholly recommend it. It’s a rational-adjacent take on litrpg, played very straight / cliche. Hopefully the writer continues writing and improves. The pacing is not great, it gets too caught up in the details of the character’s thoughts and, so far, everything  has felt too easy for the protagonist. I fear the story has left itself too little room to move forward in terms of escalating challenges. There’s some acknowledgement of most of that — both in-story and in the Author’s comments — but it’s on Hiatus after 25 chapters, and within a couple months of starting.

    I enjoyed reading [The Good Student](https://www.royalroad.com/fiction/10286/the-good-student), but it switched to another site which was too bloated with tracking and ads for me to load it on my old phone. I have a better phone and a better adblocker and plan to return to reading it eventually.

    I have 3 or 4 stories on RRL next up on my read list I think will be good too. I might post about them in one of the weekly recommendation threads if they’re worthwhile, but probably not for a month or so.
    ```

- u/MagicWeasel:
  ```
  Update on my trip to Sydney: I'll be there from the 21st to the 23rd of March, near the CBD. If anyone wants to grab coffee hit me up.
  ```

---

