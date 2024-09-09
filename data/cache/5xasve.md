## [D] Friday Off-Topic Thread

### Post:

Welcome to the Friday Off-Topic Thread! Is there something that you want to talk about with /r/rational, but which isn't rational fiction, or doesn't otherwise belong as a top-level post? This is the place to post it. The idea is that while reddit is a large place, with lots of special little niches, sometimes you just want to talk with a certain group of people about certain sorts of things that aren't related to why you're all here. It's totally understandable that you might want to talk about Japanese game shows with /r/rational instead of going over to /r/japanesegameshows, but it's hopefully also understandable that this isn't really the place for that sort of thing.

So do you want to talk about how your life has been going? Non-rational and/or non-fictional stuff you've been reading? The recent album from your favourite German pop singer? The politics of Southern India? The sexual preferences of the chairman of the Ukrainian soccer league? Different ways to plot meteorological data? The cost of living in Portugal? Corner cases for siteswap notation? All these things and more could possibly be found in the comments below!


### Comments:

- u/ketura:
  ```
  Weekly update on the [hopefully rational](https://docs.google.com/document/d/11QAh61C8gsL-5KbdIy5zx3IN6bv_E9UkHjwMLVQ7LHg/edit?usp=sharing) roguelike [immersive sim](https://www.youtube.com/watch?v=kbyTOAlhRHk) Pokemon Renegade, as well as the associated engine and tools. [Handy discussion links and previous threads here](https://docs.google.com/document/d/1EUSMDHdRdbvQJii5uoSezbjtvJpxdF6Da8zqvuW42bg/edit?usp=sharing).


  ----


  So I don’t have anything to show this week.  A combination of factors led to me getting practically nothing done until last night, where I at least got a chunk object able to spawn hexes in a rhombus shape. 

  In Unity, sadly.  I think due to my late start, I’m not going to be able to give Xenko a reasonable look, and so I’ll leave that for later.  Word is they’re releasing in April.


  My truncated goals for the voxel prototype are as follows:


  * voxels are saved and loaded

  * voxels are organized into chunks of a variable size

  * chunks are organized into a cylindrical shape, so that the map wraps both horizontally and vertically

  And that’s it.  Assuming I don’t have another progress-less week ahead of me, this ought to be reasonably achievable.


  ----


  We had a lot of debate in the \#pokengineering channel about types.  


  I’m starting to get pushback over having typing be mutually exclusive, i.e. all of your typing has to add up to 100%.  The issue being brought up is, if a 100% Fire type pokemon is the absolute pinnacle of Fire potential, then it’s impossible to have full potential for more than one type.

  That’s a feature, not a bug, says I.

  Still, I can see where it might be an issue in some cases, such as Moltres having a smaller and smaller Flying affinity the more Fire we give it.  One would think, at first glance, that giving Moltres 40% Flying and 60% Fire should be good enough, but then we have creatures like Slugma.  If Slugma is 80% Fire due to pretty much just being a lump of sapient lava, does this make sense?  I would indeed expect Slugma to be hurt by a Water move more than Moltres would be, but that would *also* mean that Slugma’s offensive prowess at fire moves is potentially much higher than Moltres’ due to the way that one’s typing affects STAB.


  The system that was proposed to me involved removing the cap and permitting all types to go up to 100%, so Moltres might be 100% Fire 50% Flying, while Slugma would be 80% Fire.  However, I don’t like the ramifications that this would have on things such as breeding or HM type manipulation: if you make yourself more Ice, you won’t have to exchange some other typing for it.  I prefer the simple 100% total cap, which makes it so any advantage you gain in one area *automatically* reduces advantage from some other area, without needing to police it constantly.


  So if that’s off the table, then there must be some other way to address this issue.  After arguing about it for a few days, it was brought up that having typing be both an offensive and a defensive system is perhaps doing too many things.  We haven’t fully identified what effect this will have, but we’ll probably end up dividing Type into something like Offensive Typing and Defensive Typing.  


  Charizard, for instance, would defensively be something like 40% Dragon, 30% Flying, 20% Fire, 10% Normal, while offensively being 40% Fire, 30% Flying, 20% Dragon, 10% Normal.  After all, you’d have to hit it in the mouth or the tail to actually get reasonable mileage out of your Water damage, but it’s also a *literal fire-breathing dragon*, so it’s got a bit more punch than might be initially obvious.

  We’re still working through the ramifications of this, so if you have anything to say, please speak up!


  ----  

  If you would like to help contribute, or if you have a question or idea that isn’t suited to comment or PM, then feel free to request access to the /r/PokemonRenegade subreddit.  If you’d prefer real-time interaction, join us [on the #pokengineering channel of the /r/rational Discord server](https://discord.gg/sM99CF3)!
  ```

  - u/ZeroNihilist:
    ```
    I think the breeding ramifications are interesting here. It makes perfect sense for the defensive typing to sum to 1, since there's a corresponding physical effect. If a pokemon was 50% and 50% fire, it could be literally half fire and half ice.

    It's the offensive typing where the problem comes in. If you breed a Charizard to have hotter fire, does it also fly worse?

    If so, why? After all, if all mutations necessarily came with an equal reduction then organisms couldn't really evolve. There are obviously trade-offs in evolution, but it's not 1:1 and not always sacrificing like for like. Sometimes the downside is just increased energy costs for growing, using, and maintaining the feature.

    To put it in reverse, if you surgically removed a Charizard's ability to produce flame, surely it wouldn't become a better dragon by magic.
    ```

    - u/ketura:
      ```
      This is actually a great point. Having the defenses capped and the offenses independent sounds much more reasonable than all or nothing. 

      Also, the concept you brought up of increased energy costs is intriguing to me (even if you didn't mean it as a mechanical proposal) ...something like, for every point in an offensive type past, say 30%, have a corresponding increase in endurance usage of moves of that type? There feels like there's *something* there. 

      Thanks!
      ```

  - u/callmebrotherg:
    ```
    I definitely prefer either of the two solutions that don't involve removing the 100% cap.
    ```

- u/CouteauBleu:
  ```
  Today, my father, who is a roofer (he builds roofs), asked me to install Google Earth on his computer, because his is being repaired. I asked him why he wanted Google Earth. He said it helped him check the advancement of his construction sites, take measures, see if the gutters had been placed, etc.

  Holy shit, guys. We're in the future.

  EDIT: Okay so I asked him to clarify, and he doesn't actually use it for his own projects? More to check the long term advancement and changes to existing buildings. Way less awesome.
  ```

  - u/trekie140:
    ```
    Does it actually update often enough to be useful? I didn't think it could be used to track daily changes. If so, that is really cool.
    ```

    - u/SvalbardCaretaker:
      ```
      Maybe if they are living right nearby some area of interest, Mountain View or somesuch? In Germany you get aerial pics that are >4 years out of date.
      ```

    - u/callmebrotherg:
      ```
      Google Earth updates every 1-3 years, but Google *Maps* updates on a daily basis with a three week delay.
      ```

    - u/MagicWeasel:
      ```
      I'm a traffic engineer and even having a photo every few months is great. You can see when things were put in, what an intersection looked like around the time of an accident, etc.

      And taking measures is a godsend. Seeing sightlines. Without google earth and streetview I don't know *how* we did this job without going on site visits constantly. I mean, we still go on site and that's still vital, but if we need to know the lane width real quick we can measure it from the desk.
      ```

  - u/Sparkwitch:
    ```
    I supervise a delivery department, and the Google maps version of Earth is my go-to resource for giving directions. Seeing the area in 3D makes my descriptions of where to park the trucks and how to find paths to entryways make a lot more sense to my people when they can see them from the side rather than from above.

    Certainly more sense than when they could only see streets and I had to draw any more detailed maps.

    Surrogate spatial concepts!

    That said, as Svalbard points out, I do live in a part of California that Google pays more attention to than, say, rural Wyoming.
    ```

- u/trekie140:
  ```
  Is anyone else questioning their belief in traditional democratic values like freedom of speech? I was always of the opinion that "sunlight is the best disinfectant" so that the surest way to stop bad ideas from spreading was for public discourse to prove them wrong. However, lately I have seen many ideas I consider evil gain massive support that rejects alternatives they're made aware of.

  The result of this is when I see people critique Bill Maher for even allowing Yiannopoulos a platform to speak or Anti-Fascist groups that openly promote censorship of hate speech, I find I can't disagree with them the way I used to. I've seen hatred become normalized in spite, and sometimes because, of opposition to it so I worry allowing people to share these ideas at all will cause it to spread further no matter what.

  At the same time, another part of me hates myself for being so utilitarian that I don't remain committed to the principles I've always held dear. I'm supposed to seek to optimize the values I cherish, not change those values in response to irrational opposition. I don't want to hate evil more than I love good, but the more I see evil win the less I care about being good. 

  It was so easy to have faith in goodness when I believed good was winning overall, but now that I feel like progress has been halted or reversed I'm considering means that I once considered evil in to reach an end that's even a little more good than today's world. What does that say about me? What does that say about the state of the world?
  ```

  - u/CthulhuIsTheBestGod:
    ```
    Re: Freedom of Speech, Yiannopoulos, and Maher.  I haven't watch Bill Maher in a while, but there is a difference between liking freedom of speech and giving ridiculous ideas like fascism screen/mind time.  I even think that arguing and debating over them may is some cases contribute to their normalization.

    Re: Evil winning vs. good.  Maybe I'm too optimistic, but I do still think that the world is generally getting better, and if anything we are just in a temporary downward spike.  All this means is that we need to try harder using 'good' methods of optimizing the world.

    That's all I have to say now (my first point was my main one), but I may have more later.
    ```

    - u/CCC_037:
      ```
      The world is generally getting better. But a lot of the getting-better-ness happens quietly, behind the scenes and out of sight, while a lot of pretty terrible people are standing front and center saying some pretty terrible stuff.
      ```

      - u/trekie140:
        ```
        My problem isn't that the improvements are quiet, it's that they're so slow due to resistance from bigots, anti-intellectuals, and people who think they aren't members of those group but rationalize supporting them.
        ```

    - u/Terkala:
      ```
      Denying free speech just says that you have no rational argument to debate them on.

      You're allowed to disagree, or even to ignore or scorn people with differing opinions. But a democracy does not function when one group can mandate that another is not allowed to speak. Especially because that will imply that the silenced party has something so powerful to say that the majority party has no rational argument against it.
      ```

      - u/ZeroNihilist:
        ```
        > Denying free speech just says that you have no rational argument to debate them on.

        Is it? Imagine there was some harmful idea that was extremely persuasive because of quirks of human psychology, but not actually right. Teaching such an idea to vulnerable groups could lead to it being adopted despite the harm it causes.

        Obviously if you train people to avoid those quirks, the problem is sufficiently reduced in magnitude that it may as well have disappeared. But the population we have isn't trained. They're eminently susceptible. Even rationalists are, though ideally we'd be able to notice and correct those negative beliefs in ourselves and others.

        I don't think it's beyond the realm of possibility that there might be things which should not be given a platform. Unfortunately, I can think of no way to prevent the expression of such ideas without enabling the suppression of whatever ideas the government (or whichever group) doesn't like.

        Essentially, my preferences would be (in order):

        1. Eliminate the issues with human psychology that lead to people holding irrational beliefs.
        2. Prevent the spread of irrational beliefs without affecting the spread of arational or rational beliefs.
        3. Allow all beliefs to compete freely.

        1 and 2 are both, as far as I can see, infeasible. 1 is a massive, multi-generational undertaking in the best case, and 2 might just be impossible. That leaves 3, and theoretically 1 & 3 implies 2 (since these harmful memes only spread because people aren't sufficiently rational).
        ```

      - u/Sagebrysh:
        ```
        I hear what you're saying here, and I largely agree with it, I *want* it to be true. 

        However, that being said, lets look at meme theory. There are clearly certain memes with negative social utility that are extremely good at self-replicating and propagating themselves in our culture. If these sorts of memes are allowed to take hold, then they act like a supervirus and spread rapidly through the population. Yes, this directly implies that the silenced party has something powerful to say, but that's the problem. We know from meme theory that power and ability to spread through a population are *orthogonal* to the truth-value of a given meme. So you can have these incredibly infectious, powerful memes, that are societally-harmful but very difficult to eradicate, especially since many of these memes foster the creation of ingroups around themselves as defense mechanisms against competing ideas. 

        Now, trying to fix that quirk of human nature, on the whole, is a very difficult task, but given the existence of these memetic equivalents to biological warfare, maybe we should reconsider giving all memes an equally rich substrate to develop within.

        The other problem I see with unrestricted free speech is this, quote is from Slatestarcodex, bolding mine:

        >Liberalism is a new form of Hobbesian equilibrium where the government enforces not only a ban on killing and stealing from people you don’t like, but also a ban on tyrannizing them out of existence. This is the famous “freedom of religion” and “freedom of speech” and so on, as well as the “freedom of what happens in the bedroom between consenting adults”. The Catholics don’t try to ban Protestantism, the Protestants don’t try to ban Catholicism, and everyone is happy.
        > **Liberalism only works when it’s clear to everyone on all sides that there’s a certain neutral principle everyone has to stick to.** The neutral principle can’t be the Bible, or Atlas Shrugged, or anything that makes it look like one philosophy is allowed to judge the others. Right now that principle is the Principle of Harm: you can do whatever you like unless it harms other people, in which case stop. We seem to have inelegantly tacked on an “also, we can collect taxes and use them for a social safety net and occasional attempts at social progress”, but it seems to be working pretty okay too.

        My fear is that a group will claim to adhere to the neutral principle, take power, and then use that power to ban Catholicism anyway. [This post](https://np.reddit.com/r/AdviceAnimals/comments/5ntjh2/all_this_fake_news/dceozzo/) covers that playbook pretty well. If everyone involved isn't acting in good faith, it's easy to undermine the principles we hold dear. It's not particularly easy to identify when people aren't acting in good faith all the time, but if we don't make the attempt, then we leave the door open for people to use freedom of speech to destroy freedom of speech, who'll use democracy to destroy democracy, that's definitely a concern of mine.
        ```

      - u/CthulhuIsTheBestGod:
        ```
        I agree.  Was there something in my comment that you were disagreeing with?
        ```

      - u/None:
        ```
        > Denying free speech just says that you have no rational argument to debate them on.

        Of course, that's not evidence against your position, nor in favor of theirs.  It's mostly just evidence you're a bad persuader.
        ```

        - u/Iconochasm:
          ```
          It's at least weak evidence that you have no faith in your argument.
          ```

          - u/None:
            ```
            But it is *weak*.  If a superintelligence can persuade you of X regardless of its falsity, a relatively unintelligent person, or perhaps merely one utterly untrained in persuasion, might likewise fail to persuade you of X regardless of its truth.
            ```

  - u/InfernoVulpix:
    ```
    I think I understand what it must feel like, seeing good ideas fail to prevail and wondering if free speech actually does lead to the success of good ideas, but even if free speech has failure states like this, I'd argue that the alternative is still much worse.

    Free speech or no free speech, the marketplace of ideas is symmetric.  There's no Idea God to tell us which ideas are actually superior to others, and every proponent of an idea will assert that theirs is the only one that's true among competing ideas.  Even when you *know* your methodologies were superior and yours is the only honest conclusion with the data available, the situations are rarely so straightforward that people can be reliably convinced that their methodology was wrong, even when they're being open-minded.  *They* probably also know their methodologies are the most sound and that theirs is the only honest conclusion, too.

    As such, there is no way for advocate for obviously wrong ideas to be suppressed while also being safe from suppression yourself.  Even if free speech doesn't get the right ideas propagating, it *keeps the ideas propagating*, which is so incredibly important I can't begin to describe it.

    The true failure state here is not that bad ideas gain popularity, even though that is a failure state.  The true failure state is when ideas die because others disliked them, because without an Idea God there is no person, group, or ideology fit to dictate whether those ideas for certain deserved to die or not, because after all, they could be your ideas.

    tl;dr free speech may not be perfect, but it keeps good ideas alive even if bad ideas never die either.  Since we are only human, we have to accept that there's no way to forcibly cull the bad ideas and keep the good ones.
    ```

    - u/CouteauBleu:
      ```
      > There's no Idea God to tell us which ideas are actually superior to others, and every proponent of an idea will assert that theirs is the only one that's true among competing ideas. 

      Oh my Idea God, this, this, so hard. You get the thing.
      ```

  - u/narfanator:
    ```
    I think two things:

    a) Genocide is not an opinion (this draws a nice, if typically fuzzy line, regarding free speech)

    b) Any given system will have a faulting situation. Do not restrict yourself to one; life doesn't. 

    Let's dive into *b* a little more: Utility monsters, Pascal's Wager - these are good examples of fault situations for value systems and methodologies. They are rescued by comparing their output to other value systems, including "gut" feeling. Look at Ethereum and the debate about forking it after the "theft".

    Think about your own brain and existence: You have a logical system for thinking, and an emotional one. Some people experience existential systems. Your brain uses may different systems (electrical, hormonal) which in turn are not restricted to the brain (the gut has a substantial effect).

    All in all - Don't feel conflicted that you have multiple active value systems. When your value systems disagree, that's a sign you should examine the situation in more detail. Maybe one system is in a fault situation, and you can't rely on it; maybe they're legit disagreeing and you need a larger principle to decide between systems (which itself is a system... yay fractals!)

    Does that make any kind of sense?

    (PS - My "larger principle" is: act to make there be more of what you want in the world.)
    ```

    - u/trekie140:
      ```
      I've always been a pragmatist on some controversies and an idealist on others, it's just that I've never considered taking away rights from people just because I think they don't deserve them. I actually oppose the idea of banning human drivers even though I know it would make the road safer because it feels like compelling someone to sacrifice control over themselves. However, right now, if I knew for sure that censoring hate speech would reduce the prevalence of bigotry then I would support it regardless of my own objections.
      ```

  - u/Polycephal_Lee:
    ```
    >When you tear out a man's tongue, you are not proving him a liar, you're only telling the world that you fear what he might say.

    George RRMartin
    ```

  - u/Timewinders:
    ```
    I'm still in favor of free speech. The real danger right now is people like Trump doing everything they can to suppress and discredit all opposing voices. I do think the education standards of this country needs to be raised so people don't buy into this white supremacist shit that's gaining traction recently. These people have always been there at the fringes of society, the problem is that the backlash to globalism is making them more popular.
    ```

    - u/trekie140:
      ```
      The thing I'm worried about is that educating these people won't persuade them. Every Trump supporter I've spoken to has rejected all the evidence I present as biased against them or outright false without presenting any evidence of their own that I consider credible. They remain steadfastly committed to their current beliefs and seek out any rationalization they can despite being confronted by demands to think critically.
      ```

      - u/None:
        ```
        Psychology says that you can't just change people's beliefs by showing them *mere* counterevidence.  You have to actually give them an alternative narrative or analysis, then show them how the evidence supports that new possibility.
        ```

        - u/trekie140:
          ```
          I doubt it will be any easier for them to accept a narrative that portrays the heroes of their narrative in a bad light.
          ```

      - u/Timewinders:
        ```
        Of course most people stupid enough to vote for Trump can't be helped. But their children don't have to turn out the same way.
        ```

        - u/trekie140:
          ```
          I'd rather the world their children inherit be less bad than it is likely to turn out right now. The longer they continue this delusional course of action while denying the negative consequences the harder it will be fix things. Or in the case of climate change, may be pushed past the point of no return.
          ```

    - u/zarraha:
      ```
      Is there actually white supremacist stuff gaining traction?  Because I have only heard accusations and condemnations of it, not anyone actually supporting it.  Although perhaps since I've mostly been on Reddit I'm not in the best position to encounter it.  And the accusations I have actually looked into, like the idea that Milo or Trump are themselves white supremacists, are so blatantly false that I hesitate to believe the other claims.
      ```

      - u/Timewinders:
        ```
        As an Indian person, I have to say that there have been quite a few attacks on Indian people during Trump's campaign and afterward by people thinking we're Muslim. It's like the days after 9/11 all over again. Trump's rhetoric demonizing and excluding Muslim and Hispanic people and his legitimizing previously fringe far right people like Bannon has emboldened racists across the country. I know many other minorities I know don't feel as safe in America as we used to.
        ```

        - u/zarraha:
          ```
          This appears to be true, and I can see your point, although I'm not certain that anti-Muslim and white supremacy are the same thing.  White supremacists would be anti-Muslim, and anti-Indian, but they would also be anti-everyone-except-whites.

          The statistics seem to show a recent increase in anti-Muslim hate crimes, but not a significant increase in other hate crimes.  They also show a significant increase in Islamic terrorist attacks in Europe recently, which could easily explain this trend as the cause of the emboldening.

          Given that Trump's rhetoric is negative towards Muslims and Illegal immigrants from Mexico, but makes little to no mention of race except occasionally to promote equality rather than oppose it, it would be more accurate to describe it as anti-Islamic, which is a religious category, not a racial one.

          The fact that Indians and other people of certain ethnicity are being targeted without their religion being known detracts from this argument, but last time I checked bigots weren't particularly intelligent and probably don't care about the difference.
          ```

          - u/Timewinders:
            ```
            Come on. Are you really only going to consider Trump a racist if he is explicitly so? Being explicitly racist would be political suicide, but banning travelers from Muslim countries while giving exceptions for Christians, decrying only Muslim terrorist attacks while ignoring recent hate crimes, making up fake terrorist attacks to attribute to Muslims, etc. all accomplish the same thing as explicitly as a politician can get away with. And the point about mistaking Indian people for Muslims is important because it's not really just about religion and ideology or terrorism, it's also about race.  Anyway, I didn't say Trump himself is a white supremacist, but he's certainly currying their support and legitimizing their views. These people like Bannon target anyone they don't consider white, including Hispanic, black, and Jewish people. Maybe it's because I've spent time on 4chan and altright subs but the trend here is pretty obvious.
            ```

          - u/None:
            ```
            > The statistics seem to show a recent increase in anti-Muslim hate crimes, but not a significant increase in other hate crimes.

            They also show an increase in anti-Jewish hate crimes.  Nu?  What have Jews done to justify attacking us?
            ```

      - u/None:
        ```
        >Is there actually white supremacist stuff gaining traction?

        Yes.  My alma mater has had Identity Europa flyers show up on parked cars.
        ```

  - u/None:
    ```
    Honestly, I think it means you and me too are confused about how things are working.  Remember, there have been times Communists and fascists fought each-other in the streets, and the fascists won, and the Communists (and liberals, and moderates, etc.) got sent to concentration camps.  There have also been times when neo-Nazis tried to march through a largely Jewish village, defended by the ACLU, and yet gained little to no power from it.

    The real question is: what's the underlying causal factor that makes Card Carrying Evil win in some circumstances, but not others?  Does that factor really match up to *our* personal instinct, as aspiring fighters against Evil in general, to directly confront and fight people we believe are Evil?

    If it does, then we should support tactics which Fight Evil.  If the causal factor is something else, we need to work on that.  If traditional Deontological Principles of Good are helpful to attaining Good and fighting Evil, we should keep them.  If they're detrimental, we can change them: Chesterton's Fence is only helpful if it actually keeps foxes out of the damned henhouse.
    ```

    - u/trekie140:
      ```
      I think my internal debate ultimately comes down to whether a preemptive strike against evil is justified in this case. Are they deserving of coercion if they don't resort to coercion before we do or has the war of ideologies already begun and I'm just avoiding fighting it? All I know is that bad things are happening and the people causing them won't listen to me when I explain why they should stop.
      ```

      - u/None:
        ```
        What preemption?  They're in government, more or less.
        ```

        - u/BadGoyWithAGun:
          ```
          Yeah, I find it hilarious how leftists are still calling for a hate speech ban.

          You people realise that /ourguys/ would be the ones defining "hate speech" this time around, right?
          ```

  - u/ToaKraka:
    ```
    > I was always of the opinion that "sunlight is the best disinfectant" so that the surest way to stop bad ideas from spreading was for public discourse to prove them wrong. 

    That doesn't work if the authorities in charge of "proving" things (whether [scientists](https://www.google.com/search?q=replication+crisis), [journalists](http://www.reddit.com/r/kotakuinaction), or [government recordkeepers](http://thehill.com/homenews/administration/320320-report-trump-administration-eyes-changes-to-trade-deficit)) have thrown away their credibility--or if the item in question has such long-term effects than *any* "proof" must be tenuous and disputable.
    ```

    - u/trekie140:
      ```
      What did they do to lose credibility to the point where opposition to them could be considered more rational than reforming them?
      ```

      - u/ToaKraka:
        ```
        *I* never said that it *was.* Many people, however, are not so optimistic.
        ```

        - u/trekie140:
          ```
          So how do we stop them from dismantling institutions we believe in if they aren't listening to reason?
          ```

  - u/CouteauBleu:
    ```
    > What does that say about me?

    By this point I'm pretty sure it means you have some sort of pronounced confirmation bias, where you look for the most exciting, negative, terrifying news you can find and intepret them as deep, coded philosophical messages about life itself.

    More developed answer tomorrow when I have some time.
    ```

    - u/trekie140:
      ```
      It's not bias if the fear is rational. I am afraid of bigotry, authoritarianism, and anti-intellectualism. All of which have gained huge popularity over the past year or so and I see represented at r/AskTrumpSupporters from people who defend words and actions I consider indefensible. I won't pretend that things are okay when they are not and show no sign of getting better.

      The question isn't whether I should be afraid that the owner of a white nationalist rag is my President's chief of staff, the only foreign leader the President hasn't criticized is the autocrat ruling Russia, or that millions of people believe a travel ban on Muslims isn't unconstitutional. The question is what do I do to stop things from getting worse?
      ```

      - u/CouteauBleu:
        ```
        I don't think you really understand what "confirmation bias" is. If I (as a rational person trying to help you) think you're being biased and focusing too much on exciting negative things, then you telling me you're really really sure that you're right and citing a bunch of exciting negative things kind of demonstrates my point.

        I'm not saying the awfulness doesn't exist, I'm saying STOP STARING AT THE AWFULNESS, and stop persuading yourself it's all there is.
        ```

        - u/trekie140:
          ```
          I'm not convinced that's all there is, I'm worried there's no way to stop the awfulness accept to do something that I also consider awful and is looking more attractive to me as time passes.
          ```

      - u/sneakpeekbot:
        ```
        **Here's a sneak peek of [/r/AskTrumpSupporters](https://np.reddit.com/r/AskTrumpSupporters) using the [top posts](https://np.reddit.com/r/AskTrumpSupporters/top/?sort=top&t=all) of all time!**

        \#1: [ModPost: PSA Collection Found Here: Muslim Immigration, The Wall, and Trump Being Pro Women, Pro LGBT, and More](https://np.reddit.com/r/AskTrumpSupporters/comments/4c67vk/modpost_psa_collection_found_here_muslim/)  
        \#2: [Not a Trump supporter, but I'm impressed](https://np.reddit.com/r/AskTrumpSupporters/comments/4v1f3m/not_a_trump_supporter_but_im_impressed/)  
        \#3: [I didn't vote for HRC because of cronyism and pay-to-play. How is DeVos not the epitome of that??](https://np.reddit.com/r/AskTrumpSupporters/comments/5snu4l/i_didnt_vote_for_hrc_because_of_cronyism_and/)

        ----
        ^^I'm ^^a ^^bot, ^^beep ^^boop ^^| ^^Downvote ^^to ^^remove ^^| [^^Contact ^^me](https://www.reddit.com/message/compose/?to=sneakpeekbot) ^^| [^^Info](https://np.reddit.com/r/sneakpeekbot/) ^^| [^^Opt-out](https://np.reddit.com/r/sneakpeekbot/comments/5lveo6/blacklist/)
        ```

  - u/Sparkwitch:
    ```
    On Truth:

    Hate speech, self-righteous falsehood, and proud ignorance are frustrating but- in my opinion -better to suffer them all than to throw the proverbial baby out with the bathwater.

    Truths can hurt, every bit as much as fantasies can, but they're true. They may be denied, they may be devalued, they may be undermined, but they can never be destroyed.

    When necessary, it must be spoken no matter how much it hurts. That may feel like hate to the person who hears it, it may feel like falsehood, it may feel like ignorance and, indeed, *it may truly be any one of those or all three*. Who's to know? But if it remains unsaid, then the speaker's truth remains unknown... or the speaker's untruth remains uncorrected.

    On Evil:

    There is so much good in the world that seeing it is as blinding as the sun. Every minute of every day billions of people are gentle, kind, trusting, and giving. Their decisions trend towards health, community, and hope. Were that not true in aggregate, every minute of every day, anything resembling society would have failed before it began.

    Evil is so rare that every insignificant bit of it stands out in stark, obvious contrast. When we're crowded together, or when the internet and the media bring us together, evil can grow common and we can feel apathetic. If that starts to hurt too much, shade your squinting eyes with your hand and notice some of the good. It's not easy, but it's worth a look.

    To paraphrase a pair of detectives under the stars:

    "How do those tiny lights stand up against all that darkness?"

    "Used to be nothing but dark. Looks to me like the light is winning."
    ```

  - u/Polycephal_Lee:
    ```
    I see this liberal attitude along with identity politics more and more. Safe spaces need to exist, but unsafe places also need to exist in order to have real discourse.

    The alternative to free speech is using violence when people merely talk about something. It's only 1 step away from thoughtcrime or precrime.
    ```

- u/ToaKraka:
  ```
  Theoretical question-asking...

  An asker of questions always must consider the answers that he wants to glean in formulating his inquiries. For an example, let's take a simple question:

  > What's your favorite color?

  This sentence offers up two very obvious ambiguities for our examination.

  First, *what do I mean by `color`?*  
  \- Is `white`, `black`, or `gray` an acceptable response, or must the answer have nonzero saturation?  
  \- Speaking of saturation, in what format should the response be delivered--a simple word, an RGB value (decimal or hexadecimal?), a Pantone CMYK reference, or something else?  
  \- Should the queried person respond with a *specific* color, like `RGB 0 128 0`, or with a *range* of color, like `green in general` or `bright, highly-saturated green`?

  Second, *what do I mean by `favorite`?*  
  \- Speaking of RGB vs. CMYK, *in what context* is the queried person expected to be thinking of the color? Is this his favorite color in isolation on a computer screen, or on someone else's car that he sees on the road, or on his own car, or on his casual polo shirts?  
  \- Must the receiver provide a *reason* for his preference ("I like green because I like forests and tree frogs."), or can he merely say "I like green." and have done?

  In this specific case, since all these clarifications change the meaning of the question only slightly, my opinion is that the most economical course of action is merely asking:

  > What's your favorite color? Be detailed.

  However, not all questions can be wrapped up so nicely. I recently had the pleasure of [receiving](http://np.reddit.com/r/CringeAnarchy/comments/5vpocy/neckbeard_doesnt_like_parties/de4f6np) the *hilariously*-vague question:

  > Who's your perfect girl?

  I chuckled when I saw it!  
  \- Does `girl` mean `child` (offspring, or subject of babysitting?) or `romantic partner` (or is the asker implying with such a belittling word that the person would be my *vassal* rather than my *ally* in the relationship?)?  
  \- By using `is` rather than `would be`, is the enquirer asking me to describe a current *real-life* object of greed rather than a *hypothetical* person?

  In the past (IIRC), I've posed the inquiry "Describe your ideal long-term romantic partner.", which obviously is *far* more specific.

  ---

  Randomly-placed points are fun. Triangulations are fun. Spheres are fun. [What happens when *all three components* (plus a few haphazard edges and the Mercator projection, for some *extra* spice) are *combined?*](http://i.imgur.com/dFCNy0h.png)

  ---

  [Google Keep is a cute little program.](http://i.imgur.com/ryNr7l7.png)
  ```

  - u/Magodo:
    ```
    Referring to [this](https://i.imgur.com/XqSk7fP.png) thread, I too have little to no social skills and I can count on one hand the number of close friends I have. Tbh I find your capacity to refuse a drink with friends pretty admirable.  

    I rarely refuse myself in the hope that I might finally find it fun or to explore what "normal" people do in their free time. And so far I always ended up really bored wishing I'd stayed back home. I sometimes feel like I should stop trying to change and just tell people to fuck off like you did. Telling people my opinion on why drinking and parties are stupid is also something I'd never do but would absolutely love to.
    ```

    - u/captainNematode:
      ```
      > Telling people my opinion on why drinking and parties are stupid is also something I'd never do but would absolutely love to.

      I'll bite -- why do you think drinking and parties are stupid? I've encountered the "drinking is dumb" thing in this and adjacent communities a fair bit, but then in my day-to-day life it seems drinking is popular all through the upper reaches of accomplishment/intelligence/scientific aptitude/etc. (maybe not independently of wealth, though -- usually those people are into the expensive craft beer scene, or own a vineyard, or fancy sipping their many-decades-aged scotch in the evenings, or w/e). A love of social events/dinner parties goes pretty hand-in-hand here, too (though with obvious sampling bias, of the sort where you ask "why are so many of my friends more popular than me?").

      A short while back I came up with a quick list of reasons why I'll personally consume alcohol, in no particular order:

      1. It's found in a variety of tasty beverages (and occasionally foods, e.g. in sauces). In beverage form it can enhance the taste of certain foods
      2. In mild-moderate doses it has pleasing psychoactive qualities, i.e. a pleasant buzz
      3. It can serve as a social lubricant through direct modification of your attitude and personality
      4. It can serve as a social lubricant by giving you a common ground with which to connect with someone, owing to its immense popularity -- e.g. you can talk about the production or history of wine-making, or what flavors you like and dislike, etc.
      5. It's historically and culturally important in many places and you can get a deeper appreciation of a place by sampling its drinks (e.g. by going on a tasting tour and exploring the history of wine-making in France or beer in Belgium or something, never mind local scenes)
      6. Mild consumption might be good for you, or it's at least associated with decreased mortality (a classic "j-shaped curve" is borne out in a lot of studies; e.g. https://www.ncbi.nlm.nih.gov/pubmed/17159008). Probably confounded, but there are plenty of plausible mechanisms
      7. It's something to do while bored which will make you less bored (e.g. at a noisy house party it lowers your threshold for entertainment -- flailing around on the dance floor is more fun while tipsy; related to the pleasing psychoactive qualities mentioned above)
      8. Its consumption is traditionally a symbolic/ritualistic behavior in a lot of circumstances (e.g. celebrations), and there are a lot of benefits to consistent tradition and ritual
      9. A lot of people like it, and to some you'll stand out -- not necessarily in a good way -- if you don't. There's a social stigma against not drinking, and failing to conform may rob you of some ability to resist social pressure elsewhere
      10. Many activities and games become more challenging while under the influence, so it's a good way to handicap yourself if something's become too easy -- e.g. in drinking games
      11. It can be fun to prepare alcoholic drinks and experiment with different combinations of flavors in the same way that it's fun to cook or draw or make anything else -- it can serve as an outlet for artistic expression
      12. More an absence of a - than a +, but you can easily lessen the unpleasant effects of alcohol consumption (e.g. hangovers) by drinking in moderation, staying well hydrated, not drinking on an empty stomach, getting a full night's sleep, and maybe taking a multivitamin/mineral supplement


      As for parties, I've found it *really* depends on the sort of party you're going to. I  attended dozens of house parties in undergrad and soon realized that the sorts of 50+ person parties where you stand around trying to talk over extremely loud music while nursing a beer were not for me, but that I quite enjoyed parties where I could join a smaller group engaged in lengthy discussion, with some quiet sounds serving as a background, with the occasional pre-planned activity (e.g. board games, video games, movies, dinner -- usually potluck style, and so on) to break up the evening.
      ```

      - u/ToaKraka:
        ```
        Not the person to whom you replied, but:

        > I'll bite -- why do you think drinking and parties are stupid?

        See my second reply [here](http://i.imgur.com/XqSk7fP.png).

        > 1

        I doubt that any alcohol-containing food would taste better than my favorite meal, General Tso's chicken.

        > 2

        I don't like the idea of making myself stupider on purpose, even if only temporarily.

        > 3

        I don't see the point of making myself more social only temporarily.

        > 4

        Liking the background of a beverage and liking the beverage itself are two separate items. I like General Tso's chicken, but I *definitely* wouldn't care if someone came up to me and started rambling about the history of Chinese-USAian recipes.

        > 5

        (laughs) I've traveled to enough places to know that I don't enjoy traveling. Being vaguely interested in something that the place contains (and, again, being interested in a drink's background differs immensely from being interested in the drink itself) definitely isn't enough to entice me.

        > 6

        (shrugs) Point.

        > 7

        If I'm bored, I can think about programming or video games or *Naruto* fanfiction instead.

        > 8

        (shrugs) Point.

        > 9

        The only thing worse than being talked about is not being talked about, 'ttebayo.

        > 10

        See 2.

        > 11

        I already make [art](http://i.imgur.com/dFCNy0h.png) through [programming](https://toakraka.neocities.org/2017-02-27/DelaunayRNGSpherical.pde.txt) (and [fanfiction?](https://www.fanfiction.net/u/4098737)).

        > I quite enjoyed parties where I could join a smaller group engaged in lengthy discussion

        Finding and following an interesting thread on Reddit or the Paradox modding forums is *much* easier than searching for an interesting conversation IRL.
        ```

        - u/narfanator:
          ```
          FYI: I notice a pretty huge different in experience between normal beers (budweiser, etc) and "fancy" beers (allagash, three philosophers...).

          I generally find one fancy beer to be excellent for thinking, in basically the same way as it's a social lubricant - thoughts slide around real easily, and I don't censor my internal thinking as much / at all. Prior to discovering fancy beers, beer never resulted in a good thinking experience for me. YMMV.
          ```

        - u/captainNematode:
          ```
          Fair enough! I'd initially written those points in response to someone asking why *anyone* might want to consume alcohol, so they're certainly particular to my own motivations. 

          > I doubt that any alcohol-containing food would taste better than my favorite meal, General Tso's chicken.

          Eh. Foodspace (and drinkspace) is large. I did look it up, though, and [wikipedia](https://en.wikipedia.org/wiki/General_Tso's_chicken#Recipes) tells me that *traditional basic ingredients [for Tso's Chicken] include:
          sauce: soy sauce, rice wine, rice wine vinegar, red pepper flakes*... though all the alcohol might be boiled off by the end. Still, de gustibus non est disputandum and all.

          > I don't like the idea of making myself stupider on purpose, even if only temporarily.


          That's typically incidental to the main effect, though, which to me is  more sort of a warm, friendly inner glow which can complement similar feelings from other sources (e.g. after a long day of intense hiking/biking, cuddling up with my partner and dog on the couch watching a movie with a cold beer in hand... the slight buzz only serves to enhance the experience). And your cognitive abilities aren't *that* impaired at that point (6-12 drinks in, sure, but after 1 you can still hold plenty sophisticated discourse)

          > I don't see the point of making myself more social only temporarily.

          Is it because of the *social* part or the *temporary* part? Because of course most everything's temporary, in the end. 

          > Liking the background of a beverage and liking the beverage itself are two separate items. I like General Tso's chicken, but I definitely wouldn't care if someone came up to me and started rambling about the history of Chinese-USAian recipes.

          Ah, this'd be another one of the "subject to personal preference" bits. I love knowing the history of a place or a thing, it definitely stimulates my enjoyment of it -- to use a nerdier e.g., I might like a sword because it looks cool and is sharp or w/e, but if you tell me the story of how some poor blacksmith discovered a new forging technique that enabled that sharpness, which revolutionized armed combat because now the sword could puncture previously impenetrable armor, etc. I'd certainly appreciate the sharpness more.

          > If I'm bored, I can think about programming or video games or Naruto fanfiction instead.

          Ah, but social obligation dictates that one has to stay for another two hours and it's too noisy to think about those things! Whatever will one do!

          > The only thing worse than being talked about is not being talked about, 'ttebayo.

          To make an implication a bit more explicit -- being social serves plenty of instrumental goals too, e.g. in closing business deals over drinks, connecting with your coworkers and boss after work (thereby facilitating promotion/career advancement), networking with strangers to open up opportunities down the line, even interviewing for new positions (e.g. in my experience in academia it's common to take applicants out for dinner/drinks after they give their job talk). It doesn't have to just be for the pleasure of others' company and can be thought of as a skill as any other.

          > I already make art through programming (and fanfiction?).

          Neat! I take it there's some algorithm that generated that expanding jaggy soap bubble picture?

          As for the response in the email thread, I think it's subject to what sorts of gatherings you're attending.
          ```

          - u/ToaKraka:
            ```
            > *traditional basic ingredients [for Tso's Chicken] include: rice wine*

            I expect that a restaurant would have to ask for my ID before giving an alcohol-containing meal to me.

            > Is it because of the *social* part or the *temporary* part?

            The latter. I see little value in temporary camaraderie, as opposed to [long-term relationships](http://pastebin.com/q016vjxE).

            > being social serves plenty of instrumental goals too

            [I feel rich enough for now.](https://en.wikipedia.org/wiki/Personal_income_in_the_United_States)

            > I take it there's some algorithm

            Primarily, [the relative neighborhood graph](https://en.wikipedia.org/wiki/Relative_neighborhood_graph) (which is what `RNG` stands for in [the linked code](https://toakraka.neocities.org/2017-02-27/DelaunayRNGSpherical.pde.txt)), in addition to [spherical geometry](https://en.wikipedia.org/wiki/Great-circle_distance) and [the Mercator projection](https://en.wikipedia.org/wiki/Mercator_projection).
            ```

            - u/captainNematode:
              ```
              > I expect that a restaurant would have to ask for my ID before giving an alcohol-containing meal to me.

              Depends on where you are -- I don't think I've been carded for alcohol at a restaurant since I was 18-19 (in the US, too, and for beer/wine/mixed drinks). If you're going to hole-in-the-walls I doubt they care, especially for alcohol in food and not beverage form.

              > The latter. I see little value in temporary camaraderie, as opposed to long-term relationships.

              But long-term relationships have to start somewhere, e.g. you meet over small-talk at a party.

              > I feel rich enough for now.

              Eh, not all promotions are about money (though I feel most anyone could use more of it, at least for future security). You could also negotiate to work fewer hours, take on more interesting projects, etc.

              > Primarily, the relative neighborhood graph (which is what RNG stands for in the linked code), in addition to spherical geometry and the Mercator projection.

              Nice!
              ```

            - u/gbear605:
              ```
              > I expect that a restaurant would have to ask for my ID before giving an alcohol-containing meal to me.

              I might be wrong, but a brief bit of googling says that food items that don't contain a substantial amount of alcohol are legal to have for anyone, no matter your age.
              ```

    - u/narfanator:
      ```
      So, skimmed that thread, and: You're doing it wrong, because: In the same way they're confused that you don't enjoy [ACTIVITY], you're confused that they *do* enjoy [ACTIVITY]. The "doing it wrong" comes from attacking them over it. Humaning protip: If you find yourself attacking someone, you're doing it wrong.

      Better to go "nope, not interested, have fun." and leave it at that. If pressed, sure, explain why YOU don't like it... but don't explain it as if they shouldn't like it either... although on the gripping hand, that thing there one voice of dissent lets other dissent is probably a good thing.

      In terms of JUST exploring what "normal" people do... Most of the time it's dull AF. But the act of going out for a drink isn't what makes it boring, it's what the people who're doing it end up talking about. I have had amazingly deep and meaningful conversations in all kinds of "normal" and "crazy" situations.

      Which part of the world are you in? I may be able to point you at some people.

      A somewhat harder but way more liberating thing to do is to just start doing the thing that interests you, and DGAF when people run away because they're not interested. Want to talk about rationality? Just start talking about it. Want to make something? Start making something.

      Note: It's definitely harder to, say, pull out a laptop and start coding at most parties, but still doable, and you may find a kindred soul that way.
      ```

    - u/ToaKraka:
      ```
      > Tbh I find your capacity to refuse a drink with friends pretty admirable.

      It's easier when you probably will never have to interact with them again (except at the pointless graduation ceremonies that your parents make you attend)! ;-)
      ```

---

