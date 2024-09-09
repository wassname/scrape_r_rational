## [D] Friday Off-Topic Thread

### Post:

Welcome to the Friday Off-Topic Thread! Is there something that you want to talk about with /r/rational, but which isn't rational fiction, or doesn't otherwise belong as a top-level post? This is the place to post it. The idea is that while reddit is a large place, with lots of special little niches, sometimes you just want to talk with a certain group of people about certain sorts of things that aren't related to why you're all here. It's totally understandable that you might want to talk about Japanese game shows with /r/rational instead of going over to /r/japanesegameshows, but it's hopefully also understandable that this isn't really the place for that sort of thing.

So do you want to talk about how your life has been going? Non-rational and/or non-fictional stuff you've been reading? The recent album from your favourite German pop singer? The politics of Southern India? The sexual preferences of the chairman of the Ukrainian soccer league? Different ways to plot meteorological data? The cost of living in Portugal? Corner cases for siteswap notation? All these things and more could possibly be found in the comments below!


### Comments:

- u/phylogenik:
  ```
  Is there any good evidence for a relationship between mattress price and quality (of sleep, back health, longevity-of-mattress-construction, etc.)? In response to questions of what it's best not to skimp on*, people often respond that mattress quality doesn't diminish too much marginally with cost until you get to the ~$1k range. Is this actually the case? Personally, I've slept on two 12" queen memory foam mattresses the last ~5y (the first one we had to toss after a badbug infestation), each [costing around ~$150 new and shipped](https://slickdeals.net/newsearch.php?src=SearchBarV2&q=mattress&mode=frontpage), and they've been the comfiest mattresses I've ever slept on. Admittedly I've never consistently slept on $1k+ mattresses, but I have stayed in lots of hotels of varying price and quality, as well as at rich friends'/relatives' places (with fancy, multimillion $ homes and designer this and thats, etc. so I imagine they sprung for a fancy mattress), and also briefly tried the expensive mattresses at dept/furniture stores -- and I still find that I prefer my cheap mattress. Supposedly "[a bed with a retail price point of $1,000 probably costs about $250 to make](http://freakonomics.com/podcast/mattress-store-bubble/)", so are the cheaper online stores just operating under much narrow margins (with fewer e.g. advertising, real estate, storage, labor, etc. expenses)? 

  This seems like a really straightforward (if expensive) experiment to carry out, so has anyone done it yet?

  *incidentally, people also say this about shoes, where I've also found it to not really be the case -- e.g. my dressier chippewa boots are comfier than my much more expensive, equivalently styled red wings, my AE strands are decidedly not comfy to wear for long periods of time, I've had ~$50 hiking shoes completely outperform $200 hiking shoes, etc. But shoes are much more personalized, so I think they're harder to compare.
  ```

- u/MagicWeasel:
  ```
  People might recall a few weeks ago I was talking about the application/interview process for what amounted for, well, my own job. I'm pleased to be able to announce that I've been identified as the "preferred candidate" which means that the people who weren't picked have a week to file a complaint and if they don't I get my own job!! Yay!!!

  Someone who congratulated me said "it must be a relief" and I think that's the best way to put it: if I hadn't got the job I'd made plans to leave the building and take a long walk to get my head together, have a long lunch, and leave early so I could mope the rest of the day. Getting the job just... feels like nothing though, the relief at the bad thing not happening. 

  But ah well, at least I got to demonstrate to my Evil Boss in no uncertain terms that I am fucking amazing, have qualifications he probably had no idea about, and so on.
  ```

- u/callmesalticidae:
  ```
  I'm looking to get back into learning code, and the first major project that I'd like to keep in mind (since "working toward a particular goal" is probably going to be more fruitful, and less scattered, than "just open a book") is building a random generator, preferably one that can work independently (rather than something that's embedded into a webpage). 

  Does anyone have a programming language to suggest for building a random generator? Googling mostly turns up random *number* generators, but I'm looking for something that can, at a bare minimum, pick something from a list of plots that I've already written out, when I want to write something but can't pick one.
  ```

  - u/buckykat:
    ```
    Random number generators are actually a Big Deal in computing. Do you want an RNG or a pRNG? The former needs an outside entropy source like atmospheric noise or temperature fluctuations or something. The latter exists in software and gives random-ish results which are generally good enough if you're not doing anything cryptographic with them.

    > Googling mostly turns up random number generators, but I'm looking for something that can, at a bare minimum, pick something from a list of plots that I've already written out, when I want to write something but can't pick one.

    Number your list. To a computer, everything is numbers.
    ```

  - u/GaBeRockKing:
    ```
    Basically every (serious) language can do what you want-- having a build-in random number generator is a pretty standard language feature. For example, in Java, you just

        import Java.util.Random.*;

    at the begining of your file, then later say

        Random variable_name = new Random();

    And generate, say, a random number from 3-25 using

        int variable_name_2 = variable_name.nextInt(0, 21) + 3;

    How did I know to do that? Every language has some sort of documentation, so I just looked up "java random" and went here: https://docs.oracle.com/javase/8/docs/api/java/util/Random.html

    How does that help with your program? Imagine if you had 25 pre-written plots in an array, but didn't want to choose any of the first three. Then you run this program to get an int, access the index of the array in question, and print its value out. Here's all the moving pieces in a short program:

        import Java.util.Random.*;

        String[] arr = {"plot 1", "plot 2", "plot 3"};

        public static void main (String[] args) {
        Random r = new Random();
        int i = r.nextInt(arr.length - 1); //lets "arr" be an arbitrary length, and still pick the string properly
        System.out.println(arr[i]);
        }

    which will print out, to console, either "plot 1", "plot 2",  or "plot 3". (Unless I've made some dumb syntax mistake.)

    From there, I'm sure you can think of how to extend that-- generating multiple arrays, each of which contain a part of a plot, then picking them together and assembling them at random, for example.

    Now, I used Java for this example, but as I said, every serious language will have the ability to do this. Here's a short rundown:

    Compiled languages: (i.e., you write your code, you compile your code, then you run it from a binary.)

    Java -- good for beginners, usually taught in introductory CS courses. Has a massive, easy to use library of built-in functions. You'll want to download [eclipse](https://www.eclipse.org/ide/) to serve as your IDE (on windows). I don't know what mac and linux do. People complain that it's a bit slow and bloated, though, and is a little difficult to just have compiled program sitting around that you can run from wherever. Programs also tend to have a lot of filler or boilerplate that might get annoying.

    C/C++ -- While not the same language, people usually learn a bit of C before getting into C++. C++ is faster than java, and "more powerful" in the sense that it's a bit closer to the metal (you can do everything it can do with java, but it's a bit more difficult.) It's also significantly more difficult, however, and constantly seeing unexplainable "segfault" errors will get annoying fast. If you're on windows, you'd want to use [Visual Studio](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwiN28fm0-TYAhVK7FMKHZsACI4QFgguMAA&url=https%3A%2F%2Fwww.visualstudio.com%2F&usg=AOvVaw3oneBl4aXUx_gzRe4LtuAN) or [VS Code](https://code.visualstudio.com/). I don't know what IDE's linux has, but personally I just write everything in a text editor (i.e., notepad) then compile with the command line utilities gcc (for C) and g++ (for C++)

    Scripting languages: (you write your code, and then can immediatelly run it. Code execution is singificantly slower than compiled languages, but you don't need to go through compilation)

    Python -- I don't actually know this language, but reportedly it's incredibly easy to use and read, has an expansive default library, and has a number of elegant features. Popular for introductory CS classes, as well as for "coding for engineers" classes. Downsides? I wouldn't know-- I've never tried it.

    Javascript -- Don't use javascript if you can help it. As far as languages go, it has a lot of bizarre features and intuitiveness. That being said, if you plan to run your code from a webpage, then you don't really have a choice, so suck it up, read the www.w3schools.com tutorials (including the HTML and CSS tutorials) and get to it.

    PHP -- bad for the same reasons Javascript is. Necessary for the same reasons javascript is. If you want a simple web server serving your code, PHP is probably your best choice. Web servers can run other languages to, but PHP is specifically built for the purpose of being a backend language, so it's easiest for beginners for that purpose.

    Hopefully this helps!

    (Incidentally, I wrote the example in Java because I'm used to using it when my coding is timed. Don't take it as an endorsement of java.)
    ```

    - u/PeridexisErrant:
      ```
      Great summary! I'll expand on two points:

      Python is my favourite language, and I'd strongly recommend it as a first language to learn - the syntax is straightforward and there are many good tutorials. *Think Python 2e* (Green Tea press) is a very good introduction and entirely free, so no loss if it doesn't suit you. 

      The only downsides of Python are that it's not suited to low-level tasks (eg hardware control, operating systems), and that distributing your code to non-programmers can be more complicated than in compiled languages (but it's possible!)

      Re JavaScript: if you want to write Web stuff, use Typescript instead - it's a language from Microsoft which is basically "JS, without the stuff that makes that awful" and compiles back to JS very easily. There are actually many languages that compile to JavaScript (or Web assembly now!), but few are widely use for Web development.
      ```

      - u/GaBeRockKing:
        ```
        >Re JavaScript: if you want to write Web stuff, use Typescript instead - it's a language from Microsoft which is basically "JS, without the stuff that makes that awful" and compiles back to JS very easily. There are actually many languages that compile to JavaScript (or Web assembly now!), but few are widely use for Web development.

        I was personally thinking of recommending CoffeeScript, but then I figured having trying to teach a coding beginner a scripting language that *also* has to be compiles is a bit overkill.
        ```

    - u/narfanator:
      ```
      I would heartily disagree about Javascript and PHP.

      Sinatra (http://sinatrarb.com/) is pretty much the simplest/easiest you can get for a web server. I think at this point everyone has microframeworks, but Sinatra remains my gold standard.

      Javascript is a different style of thinking (callbacks/promises) that takes a minute to get your head around, but is really cool when you get into it. It's a blessing and curse that you can pull the shenanigans that are possible in the language, since it allows for really inventive exploration, but results in a fair amount of fragmentation and crazy sauce (look up "transpiling").

      I'm working almost entirely with Python right now, and I'd say it's major downside is that it's very opinionated about the "correct" way to do things. The language itself fights you if you're not doing it the "right" way, but doesn't do a great job of explaining that "right way".
      ```

  - u/CouteauBleu:
    ```
    There's like a billion different factors that go in deciding which programming language to use.

    It depends on what you want to do, how much experience you have, etc. I'm not sure what project you have in mind exactly. Do you want to do something in a window? On a Linux-style terminal? What are its inputs and its outputs? Do you want to generate the pseudo-randomness from a seed yourself, or just hook into some pre-defined "getRandomNumber()" function?

    Anyway, I'd probably recommend Python if you're starting out. It's one of the most beginner-friendly languages out there.
    ```

  - u/narfanator:
    ```
    Ruby is possibly the best language out there if you want to do stuff with strings, and it's consistently the only non-frustrating language I work with. 

    For example, Python is explicitly designed to be correct; Ruby is explicitly designed to be enjoyable. You might think this is not all that important, but these attitudes underly the tooling, communities, and documentation styles. It's just easiest to *play* in Ruby compared to every other language (IMO)... simply because that's such a core value to the language, and thus the community that grew from it. 

    In terms of learning - Almost all programming tutorials are written for people who already think like a programmer, even if they don't yet know how to program. Ruby has the only two I've come across that aren't like that - _why's poignant guide, and the SonicPi tutorials.

    That all said, the second biggest factor in choosing a language is library support for what you want to be doing; for example, Python has Numpy, which makes machine learning programming really easy.
    ```

- u/ShiranaiWakaranai:
  ```
  I have been thinking about utilitarianism and villainy, and am starting to think we need to pre-commit to a very irrational course of action even if we choose to be utilitarians.

  Let me explain the thought process: imagine a villain constructs a doomsday device, and threatens to activate it unless his/her selfish demands are met, which may include all kinds of things like money and slavery and rape and murder, but only affect a tiny fraction of the population. 

  In the current world, this course of action is stupid. There's too many irrational people that will rebel even with the threat of doomsday. Even those that don't take up arms will still treat this as a moral dilemma and be unsure about whether to obey or rebel. So the villain will most likely just get him/herself killed.

  But what if utilitarians became the majority of the population? In this situation, the utilitarian thing to do seems to be obey. And not just obey, but help put down any rebels, deliver the slaves, carry out the murders, etc. etc. After all, the more rebels, the more likely it is that the villain will simply activate the device and kill everyone, which results in an absolute minimal utility that is irrecoverable, since everyone is dead. The relatively small number of sacrifices needed to appease the villain is insignificant in comparison. And whatever other actions and outcomes are possible, they aren't worth the risk of human extinction in pretty much every utilitarian system of utility calculation. 

  Therefore, if utilitarianism ever becomes the dominant ethical system, every villain gains a perverse incentive to construct doomsday devices. After all, most of the population will jump to serve them, and even put down the crazies that try to rebel. This is terrible, because the more doomsday devices are built, the more likely one of them is to be activated (possibly by malfunction). Then we all die.

  So, as strange as it sounds, it seems that in order to avoid human extinction, we should pre-commit to the irrational act of rebelling against anyone who makes a doomsday device even if it risks killing us all.

  More generally, it seems that by the same logic, we should pre-commit to essentially defying any kind of utilitarianism-exploiting villainous threat. For example, if some villain creates a bomb that will kill X people and demands we kill or enslave some targets to prevent the bomb exploding, we should pre-commit to rebelling and attacking the villain anyway even if it kills the X people. Otherwise every villain gains perverse incentives to create all kinds of bombs and we end up with a lot more dead people. 

  Does this thought process make sense? I have a number of bias concerning ethical systems, so I need a second opinion.
  ```

  - u/sicutumbo:
    ```
    I think it would be short sighted of the population of utilitarians to obey the person holding the Doomsday device. It's similar to the logic of not negotiating with terrorists, which this basically is just on a different scale. If the terrorist is smart, they will make it so the cost to you of the thing you are to give up is less than the cost of losing whatever it is the terrorist is holding hostage. The child's safety is traded for a large but achievable amount of money, for example. From the parent's or a government's point of view, this should be an easy trade. Money for a parent is replaceable while the child isn't, and for a government letting a child die to a terrorist is such a huge negative that it's worth it. Under your analysis, this is the right solution, right?

    Well, IRL, this doesn't happen in a vacuum. Unless the parent has a strong incentive to keep the entire thing hidden, they will tell the police, and if the government gets involved then a lot of people will know about it. Capitulating to the demands in a hostage situation signals to every potential terrorist that this is a strategy that works, and pays off well since the government doesn't want to risk someone's life in such a public manner. So then everyone does it, and everything's terrible. IRL, you preempt this cycle by never giving in in the first place. Not only do you not agree to the demands, you meet every hostage situation with disproportionate, overwhelming force. You make it public knowledge that any attempted hostage situation has such a small chance of payout, such a huge chance of you ending up dead or in prison for life, that it never becomes a sensible option. The government even goes so far as to not even bother with communicating with the hostage taker in the first place, because a threat that you never hear can't be used against you. You make this reality by sharing it publically, and we call the phrase "We do not negotiate with terrorists."

    Where this doesn't apply fully is in your scenario, where the terrorist takes a city or state hostage with the threat of destruction. A single individual, or even a large crowd of individuals, is worth the sacrifice so that taking hostages does not become something that people expect to work. But losing a city or state is another thing entirely. And you're right, there isn't a good solution to this problem. Obeying the commands is the sensible option for the government and populace, even going so far as to force compliance from those who might rebel.

    However, what governments can do is try to never allow the situation to arrive in the first place. Nuclear weapons, just about the only practical way of taking a city hostage, are extremely heavily restricted. I haven't looked into this issue specifically, but I imagine that if a government credibly thought that you had a nuclear weapon, you wouldn't be greeted by a SWAT team, you'd be met with a missile. I do not feel like putting myself on a list just to confirm this.

    Luckily, nuclear weapons are so resource intensive to design and make that individuals and even most organizations can't afford to make them. Some countries did, however. To get an idea of what your scenario looks like played out in real life, research the Cold War and MAD.
    ```

  - u/hh26:
    ```
    This is a pretty standard Game Theory sequential game dilemma.  In certain sequential games, there are cases where committing to an irrational decision would lead to an increased payoff as a deterrant.  In such cases, there is a Nash Equilibrium where the player promises such an irrational decision but never has to follow through with it, but it is not a Subgame Perfect Equilibrium because such a promise cannot be followed through on.  In such circumstances, we can say that an irrational player who can precommit would score higher than a purely rational player, assuming that their status as irrational is common knowledge.

    However, such idealized scenarios rarely if ever occur in real life.  I think it is highly likely that any irrational tendencies which would score higher in a specific situation like this would score lower in similar situations with only a few details changed.  Are we sure that rebellion will always lead to the device going off rather than succesfully disarming it and leading to a higher utility?

      Does the villain have some method of avoiding dying from his own doomsday device?  Or does this necessitate him being irrational enough to follow through with his threat?  Perhaps your policy of keeping around a population of irrational people willing to sacrifice themselves for credible threats would causes such villains to be possible.  Maybe some or most villains make empty threats and we can rebel without risk of being annihilated because they are too rational to follow through.  Even if these isn't always this case, if it's common knowledge that it's possible to safely rebel with high enough probability then it might be rational to rebel and we can have a detterant effect even without irrational policy.

    Maybe we do our best to study possible doomsday devices that can be made, control the supply and knowledge needed to make them, and rely on our own doomsday devices to point back at anyone who manages to get one anyway.  That's what we're doing now and so far the world hasn't been nuked to death, and I don't think it will be in the near future.

    I don't think blindly rebelling increases global utility, otherwise we'd have invaded North Korea by now.  Diplomacy and physical prevention seem much more productive given the much smaller chance of nuclear annihilation than some vague "motivation deterrance".  I think everyone would still want nukes even if there were a 100% rebellion policy because rebellions have a smaller than 100% success rate and the nukes would still be useful in fighting them.
    ```

  - u/space_fountain:
    ```
    I think something that may be relevant here is [Rule Utilitarianism](https://en.wikipedia.org/wiki/Rule_utilitarianism). Basically it's the idea that the goal should not be to take each action based on maximizing utility but rather to come up with rules of life that if followed universally would maximize utility. It attempts to solve many of the problems with utilitarianism and at least accord to Wikipedia represents the dominate ethical theory among utilitarians.
    ```

  - u/gbear605:
    ```
    People often think of utilitarianism in a weird way.

    Utilitarianism is, simply, do whatever produces the best result, where best is defined by how much happiness there is.

    So, given all your assumptions, it sounds like the utilitarian thing to do in those cases is to rebel, not to obey.
    ```

- u/Magodo:
  ```
  [The Backwards Brain Bicycle](https://www.youtube.com/watch?v=MFzDaBzBlL0)
  ```

  - u/BoilingLeadBath:
    ```
    I liked this video. The reminder that slight distractions easily break us out of "deliberate" courses of action, reverting us to the techniques we've trained the most, rings particularly true. (Is this because a deliberate substitute for our fast technique requires an overide signal by the prefrontal cortex, which is dropped when startled or otherwise stressed? Dunno.)

    ***

    On the other hand... *8 months* to learn how to ride the backwards bike, "20 minutes" to switch to the other control scheme?

    I have quite a bit of experience swapping control schemes around: I'm on my third keyboard layout, and in analog-in for games I've tried X axis inversion, Y axis inversion, 90 degree rotations, handedness changes, combinations of the above,... and those numbers just don't jive. (My experience is that a switch in one direction takes nearly as long as switching back, and about (20) 30-minute sessions to get high-score beating good with any given scheme)

    Having not tried it, I don't think this can be much more than a suspicion, but the timescales suggest that the backwards bike probably mostly requires learning new skills, with the suppression of existing ingrained fast responses playing a fairly minor role.

    Thinking about the physics of it, the backwards bike is dynamically unstable due to the influence of physical inertia and bits of fundamental physiology like the stretch reflex. IMO, this dynamic instability explains why it takes so long to learn to do it - and, perhaps, explains why riding the backwards bike is such a separate skill from riding a normal bike that you can "unlearn" it in 20 minutes. (The major competing hypothesis is probably "the guy just never got good at riding the backwards bike - I mean, just look at him; he's barely staying upright.")
    ```

  - u/eternal-potato:
    ```
    For a moment there I was afraid he was irreversibly sabotaging his kid's bike riding skills. It turned out pretty easily reversible, but he didn't know that.
    ```

  - u/ayrvin:
    ```
    I'm curious how well one can ride the backwards bike without using hands, if the balance is such that you can do it like you ride normal bikes without using hands.
    ```

- u/AurelianoTampa:
  ```
  A shoutout to /u/DaystarEld, who posts here regularly. I was reading posts about the Aziz Ansari situation in Change My View yesterday and had been feeling really uncomfortable. I was feeling like Ansari had behaved inappropriately, but I wasn't able to articulate properly what exactly was the problem; and it was getting me really down, as many comments seemed to express he did nothing out of line. Then i stumbled across [a post](https://www.reddit.com/r/changemyview/comments/7re6fh/cmv_the_aziz_situation_is_showing_a_double/) from our own resident Pokemon Professor which perfectly explained the issue and detailed step-by-step what Ansari did wrong. And the way he responded to the comments were really well done as well.

  Sadly the post was removed for (what feels to me like) a pretty lousy application of the sub's rules, but the comments and responses can still be found there. They did actually help me clarify my thoughts, and I really appreciated the effort he put into them.

  (Sorry if this is a bit controversial!)
  ```

  - u/DaystarEld:
    ```
    Thanks for the shoutout! You actually made me realize that it was removed: it was still showing up on my browser. Particularly frustrating since I kept referring people back to the OP in discussions :P

    I sent the mods a message and they said it was automod removed, and they'll review it manually soon.
    ```

- u/None:
  ```
  [deleted]
  ```

  - u/MagicWeasel:
    ```
    I've heard some unsavory types share 5e pdfs online for free, I think you might even be able to get them with a google search! I just wanted to let you know they were out there, so you could avoid doing anything illegal.
    ```

  - u/Loiathal:
    ```
    I'd check local bookstores-- I bought my 3.5 books back in high school used there. Obviously local bookstores aren't anywhere near as common, and 5E is newer than 3.5 was then, so you may not find anything.

    That said, if you don't find it I'd probably recommend you do the bad thing and torrent a PDF of the player's handbook. It's not functionally much different from you borrowing it from another member of the table, and it's inconvenient enough to have to use the PDF (especially if you're a casting class, while at the table), that if D&D ends up being something you play semi-regularly you'll still be pretty incentivized to purchase a copy when your financial situation improves.
    ```

  - u/CCC_037:
    ```
    Most of the DnD rules were released under an Open Game License, which (in short) means that the rules (but *not* the published settings) can be freely reproduced by others.

    In other words, you can find the rules [on a wiki at no cost](http://www.d20srd.org/index.htm), if that's what you're interested in looking for.
    ```

- u/SkyTroupe:
  ```
  I need a way of changing how I think. I've been working out and will be going to a therapist once Im covered under insurance again but I keep on falling back into the same self-defeating ruts of thought. I've tried reading LessWrong articles but I just can never force myself to finish them.
  ```

  - u/Kishoto:
    ```
    This is probably super simplified advice but a simple, easy way to at least start trying to break bad habits is the rubber band method (test? Experiment? Idk). Basically, wear a rubber band on your wrist. Every time you notice that you're venturing down a self defeating line of thought, immediately grab the rubber band, pull it far and release.

    Try your best to make it reactionary (as the more time you have to think about it, the more likely you'll be too afraid of the pain to do it)

    Eventually your body will (or I guess I should say may) start associating those patterns of thought with the pain of the rubber band snap and it'll be easier to avoid because you'll naturally shy away from those thoughts. 

    Dsclaimer : this method is very simple.and basic, more for breaking a habit of eating chips after bedtime. It's no substitute for legitimate therapeutic assistance though it can serve as a supplement.
    ```

- u/None:
  ```
  [removed]
  ```

  - u/ianstlawrence:
    ```
    When I first read this, I thought of SAO (which I kinda hate) but also how often it seemed that when a large group of human beings are now in a "real" MMO they are made to look like their "real" forms. 

    I was then curious about a story where this change doesn't occur. So not only do you have people presenting as different genders but you have lots of the population looking almost exactly identical to lots of the population. 

    I wonder what kind of weird social, physical, and mental things people might go through to create distinct presentations from other people. 
    If group work might, on average, be more amicable because your physical identity isn't as unique.
    Or if you might see a rise in psychosis due to a lack of individuality.
    Maybe a greater emphasis on tribes and using group identity to create distance between yourself and others?

    Seems really interesting. And I have realized I did nothing to answer your question. Sorry. But very interesting!
    ```

---

