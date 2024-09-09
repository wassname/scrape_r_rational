## [D] Friday Off-Topic Thread

### Post:

Welcome to the Friday Off-Topic Thread! Is there something that you want to talk about with /r/rational, but which isn't rational fiction, or doesn't otherwise belong as a top-level post? This is the place to post it. The idea is that while reddit is a large place, with lots of special little niches, sometimes you just want to talk with a certain group of people about certain sorts of things that aren't related to why you're all here. It's totally understandable that you might want to talk about Japanese game shows with /r/rational instead of going over to /r/japanesegameshows, but it's hopefully also understandable that this isn't really the place for that sort of thing.

So do you want to talk about how your life has been going? Non-rational and/or non-fictional stuff you've been reading? The recent album from your favourite German pop singer? The politics of Southern India? The sexual preferences of the chairman of the Ukrainian soccer league? Different ways to plot meteorological data? The cost of living in Portugal? Corner cases for siteswap notation? All these things and more could possibly be found in the comments below!


### Comments:

- u/ketura:
  ```
  Weekly update on the [hopefully rational](https://docs.google.com/document/d/11QAh61C8gsL-5KbdIy5zx3IN6bv_E9UkHjwMLVQ7LHg/edit?usp=sharing) roguelike [immersive sim](https://www.youtube.com/watch?v=kbyTOAlhRHk) Pokemon Renegade, as well as the associated engine and tools. [Handy discussion links and previous threads here](https://docs.google.com/document/d/1EUSMDHdRdbvQJii5uoSezbjtvJpxdF6Da8zqvuW42bg/edit?usp=sharing).


  ----


  Many thanks for the responses to last week’s whinefest, both here and on Discord.  After considering the problem for a bit, I’ve decided to set combat aside for a little bit and work on revamping the Bill’s PC tool that was prematurely started at the beginning of this project.  Many of the issues with working on a combat system involve the sheer number of immaterial prerequisites that exist, and so hopefully by switching gears I’ll both rekindle some motivation while addressing those concerns somewhat.

  Bill’s PC (for those just tuning in) was [an app for composing Pokemon JSON files](https://imgur.com/a/pUlOy).  At the time that it was dropped, it could save and load type definitions, species definitions, and move definitions, as well as do fancy things like mass import from Bulbapedia and do a fancy [graph stat compare](https://i.imgur.com/uKh8uv8.png) to help visualize the differences between authored pokemon.

  I was actually quite happy with the way it turned out, and it would have continued to be the canonical JSON authoring tool I used if not for a fatal blunder: I had not realized at the time that WPF is an absolutely Windows-only framework, considered too complicated to be worth porting to other systems via mono and their ilk.  This was a surprise to me, and was unacceptable; I myself don’t care to use Linux or Mac, but I also don’t care to restrict the users of these programs, not when it’s reasonably easy for me to build things in a cross-platform manner.

  With that major lesson in mind, I got it into my head to make the new version of Bill’s PC web-based, which would solve some problems while bringing in a host of new ones, the first and foremost being that I don’t know hardly anything about coding for the web.  (I’ve maintained API endpoint servers before in ASP.NET where the fact that it’s a web server is basically a minor, incidental detail, but that’s practically tangential.)  I’m fairly confident that I can pick it up, based mostly on the fact that I previously picked up Lua and SupCom modding over the course of a week, but that might still turn out to be horribly arrogant of me, so I guess we’ll see.

  My starting point was “write a mostly client-based web app in javascript” and thus began a slog of blog posts and wiki diving trying to find what the best framework to do this in would be.  (I’m not interested in reinventing the wheel and building everything from scratch, why do it when the javascript community can do even that for me?  :V)  I mostly want an out-of-the-box framework that will tame the web somewhat for me without requiring oodles of frontend-specific experience.

  Finding posts appealing to my background has been surprisingly hard.  Most everything has been either for frontend gurus and so using jargon that is way over my head at this point, or targeting Babby’s First Programming Language and thus a waste of my time.  I eventually gave up and just took a stab at choosing a framework based on vague gut-level feelings, which landed on me experimenting with Ember.js.  So far it seems to be alright, from the perspective of someone with nothing else on the web to compare it to, so barring any last-minute revelations or advice, I’ll probably end up sticking with it sheerly through momentum.

  That said, any advice?  Framework, library, or tutorial recommendations?  Angular, Vue, and Backbone all came up in my searches, and I will probably look at them if ember doesn’t work out (in roughly that order of precedence), but I’m really just stabbing at shadows, here.  Feel free to help me change my mind.


  ----


  If you would like to help contribute, or if you have a question or idea that isn’t suited to comment or PM, then feel free to request access to the /r/PokemonRenegade subreddit.  If you’d prefer real-time interaction, join us [on the #pokengineering channel of the /r/rational Discord server](https://discord.gg/sM99CF3)!
  ```

  - u/reddraggone9:
    ```
    Looks like you named all of the most popular frameworks which handle frontend
    development aside from React. That omission seems kinda surprising to me since
    I've gotten the impression that it's *the* most popular. That said, I consume a
    fair amount of media related to web development and it's my impression that you
    can't really go horribly wrong by choosing any of them.

    I personally use Backbone for day-to-day development at work, but I wouldn't
    recommend it over any of the alternatives you mentioned for a few different
    reasons:

    - It seems to generally be considered outdated.
    - It's less prescriptive about *how* you do things. That's not inherently a
      downside, but it can be pretty bad when you're working in an unfamiliar area.
      It's like being tossed a box of tools and told to have at it. The end result
      can be pretty hard to maintain if you don't have the knowledge and discipline
      needed to use a consistent design throughout.
    - It's not really "batteries included", which means it's up to you to choose
      how to fill in the gaps and make sure everything works well together.

    I guess that's :+1: from this internet stranger. Good luck!
    ```

    - u/ketura:
      ```
      The reasons you list as downsides for backbone are largely the reasons I chose not to even bother persuing React, with the exception of age. It's apparently got almost no structure to it, in exchange for having the best handling for UI all things considered, to the point where some people use React *on top of* one of the other frameworks to get the best of both worlds. This isn't really a positive for me (as you point out), since I'm a beginner and prefer to have some structure to lean on. Plus, I'm a C# developer; I'm *used* to having a certain amount of prescription to go off of, and I'm not sure I'll ever really want a truly wide-open sandbox.

      Thanks for the second opinion, tho! It's good to see I haven't veered *too* far off the beaten path.
      ```

- u/GlueBoy:
  ```
  Louis CK :(
  ```

  - u/None:
    ```
    If it makes you feel any better, pretty soon it'll be memed enough that the pain dulls. Same thing happened to Cosby.
    ```

    - u/ben_oni:
      ```
      I was actually really impressed with his [response](https://pagesix.com/2017/11/10/louis-c-k-admits-to-sexual-misconduct-these-stories-are-true/). As if, unlike some other people, he feels remorse.
      ```

- u/MagicWeasel:
  ```
  So, I'm applying for a job - give myself a 10% chance of getting it, 50% chance of being interviewed. Deadline's Monday at midday, at which point the job I'm currently doing will be advertised (I've been told) and I'll have to apply for *that* (I'm currently doing that job but being paid for a lower level job, it's more complicated than that but it's close enough). 

  Anyway, to apply for government jobs in Australia, you have to write basically a 1 page essay on 3 different "selection criteria" - so basically, 3 long answer questions about why you are good at things, with examples (my three are road and bridge design, construction and maintenance; project and contract management; and managing financial and other resources). I *also* need to submit a resume but it's not nearly as important. They'll use my selection criteria to work out if they want to interview me, the resume will be a tiebreaker/sanity check (e.g. if I said I managed a road project but my resume only shows me working at McDonald's), and they'll interview me, if they like me they'll contact my referees, my referees will have to *fill out a form* that it is *illegal to lie on* saying I can do all the things that are on their list of job requirements, and then if I'm in the top after all that, I'll get offered the job! Yay! (and the $15/week payrise!! DOLLA DOLLA BILLS Y'ALL).

  People in the [lesswrong productivity chatroom](https://complice.co/room/lesswrong) (recommended, shameless plug) are quite surprised at this process; they're more used to the more typical process (that is used for most jobs here; it's the government that's weird) where you submit your resume, they contact your referees, you go through a few rounds of interviews, and you're offered the job or not. (Or: your uncle's friend needs a software engineer and you get the job through sheer nepotism). 

  But surely, there must be other "standard procedures" for applying for certain jobs in your neck of the woods, dear reader? Or is it just the Australian government that is weird?

  (btw the stated reason for this process is it's meant to be less discriminatory because you're judging them on their ability to do work rather than judging which school they went to, who they worked for, etc)

  (aside: I asked my current manager if he'd be one of my referees. I gave him the list of job requirements and said please make sure he can endorse me for all of those because if a referee can't endorse you that's kind of bad. I've been working for this guy a good 10 months. He says he can't endorse me for having skills in e.g. road and bridge design because the road and bridge design I do isn't *identical* to the type of road and bridge design I'd be doing in the new job. He did this for a bunch of items on the list. This was rather shocking as the job is open to the general public, so they are quite willing to hire someone who doesn't even have experience doing work in the same organisation, but apparently my manager thinks that because I design $9 million road projects I'm completely unqualified to ever design $100 million road projects! /rant)
  ```

  - u/CouteauBleu:
    ```
    > So, I'm applying for a job - give myself a 10% chance of getting it, 50% chance of being interviewed

    May the uncontrollable chaos of the universe which we can't reliably predict be with you as opposed to the other candidates, random stranger on the internet!
    ```

    - u/MagicWeasel:
      ```
      Thanks! I am glad that other random strangers on the internet are somewhat invested in my outcomes!
      ```

  - u/ben_oni:
    ```
    Uncivil engineers are better. They don't depend on government to get a job.

    But yeah, that process is real screwed up. I understand that government processes are driven by a CYA mentality, and every screw-up is answered by more WTFery. Hence the laws penalizing references for lying.

    So, job hunting. An employer puts out an advertisement with all the skills they want an employee to have, and maybe advertise a salary for someone who has a quarter of those skills. Then people with none (or very few) of the skills apply, and try to fool the interviewers into hiring them. Maybe some of them even believe they have the skills.

    In order to stand out, you need to show not only that you can do the work, but that you can do it better than other people. Usually that means showing your knowledge of process and risk mitigation. Personally, I like hearing about people's mistakes: what went wrong, how did you deal with it, what did you learn? If someone says they never make mistakes, or that they learned the wrong lessons from them... you get the idea.

    Anyways, good luck!
    ```

- u/CouteauBleu:
  ```
  Increasingly weekly update on [The Tesseract Engine](https://docs.google.com/document/d/1vIWf3Nqudgh18j4RK8bm4zOTSKUFl6l9Igvdg1adzGE/edit), my ongoing game engine project.

  ---

  Last week, I decided I would use the Minetest engine as a base for my own voxel engine. A bit of context I didn't provide then, was that I'd already tried to this exact thing one year ago, and quickly abandoned it on the grounds of the Minetest engine code being a nightmare to read.

  The reasoning of me-minus-a-week was that he had become way better at reading code and refactoring projects than me-minus-a-year, after spending an internship doing mostly that, so he'd have an easier time. Well, after spending a few days immersed in Minetest code, I'd say both my "past-me"s were right: I've gotten better at reading code and *my god* the Minetest code is messy and unreadable. I think I can use it as a source of inspiration, but it will still be faster to do my thing from the ground up.

  For those of you who have a limited understanding of programming (which I'm guessing is roughly 0 people), what I mean by messy code is mostly "code that isn't properly compartmentalized". So the part which deals with update the player's movement also deals with a bit of drawing the UI, a bit of updating the sounds depending on their position, a bit of updating the displayed position of the pickaxe you're holding, etc.

  The problem with working with messy code (especially for refactoring) is that it's way harder to think about it. If a piece of code only deals with a single concept, then you only need to think about that concept when writing the code. If a piece of code deals with 12 concepts... you get the idea. Any modification you make is more likely to have consequences you didn't foresee, to break in ways you might not even detect until you've forgotten you even rewrote that code, etc.

  Minetest is a particularly bad offender; it's an open source project, which means everyone can and does propose modifications to the code, which obviously makes having a coherent vision harder; the project creator mostly left years ago, which means no centralized decision-making, and the code is littered with "// Note to self: maybe this feature is deprecated?" type of comments.

  ---

  Anyway, refactoring Minetest is out. I guess what that leaves me with is "Make my own project from the ground up", which kind of feels like a step back.

  Last week I was worrying about my lack of progress, I said I was bike-shedding, and now my plan is "do the same as before except with more planning, and using this failed thing as an inspiration". Hurraaaaay.

  Seriously, though, I'm weirdly not worried about this. I've opened a text editor, compiled some things, got into the "What does this code do and what should it do?" mentality, which is closer to coding than I was before.

  I feel like I've progressed in some abstract way that's invisible everywhere except in my head, but it's still concrete progress. Seeing how someone else does the thing, even if I don't like their approach, gives me inspiration and ideas on how to do the thing.

  I guess I should probably make a plan of what I intend to get done before next week, but I have no idea what I can or will do except "Have a plan". Well, I'm confident anyway. Mostly.
  ```

  - u/ketura:
    ```
    Have you taken a glance at some of the other alternatives, such as [Craft](https://github.com/fogleman/Craft)? That one in particular looks fairly clean and at least gets the bare bones out of the way.
    ```

- u/GravityHug:
  ```
  [The meme of Roko’s basilisk is gaining popularity.](http://oppressive-silence.com/wp-content/uploads/2017/10/rokosBasilisk-1024.png)
  ```

  - u/CouteauBleu:
    ```
    Just pretend you don't see it.
    ```

  - u/None:
    ```
    Is that the Chrome logo?  Grimdark.
    ```

  - u/ToaKraka:
    ```
    [Be your own basilisk!](https://i.imgur.com/s52rPaZ.png)
    ```

- u/trekie140:
  ```
  After many delays due to scheduling and waiting until I was in the mood for madcap insanity, I finally finished the first season/Battle Tendency arc of JoJo’s Bizarre Adventure. It was plenty of fun, though my [enthusiastic addiction I posted about when I started](https://www.reddit.com/r/rational/comments/6vz27p/d_friday_offtopic_thread/dm432zghttps://www.reddit.com/r/rational/comments/6vz27p/d_friday_offtopic_thread/dm432zg) has unfortunately waned. I’m definitely looking forward to Stardust Crusaders, I actually like villain of the week stories, but I’ve gone from shamelessly loving the insanity that is JoJo to *just* liking it and I can’t help but feel disappointed.

  I think it’s due to the pace at which I consumed it. I was only able to binge Phantom Blood and ended up taking a three week break before watching the climax of Battle Tendency over the course of another two weeks, so the plot lost its momentum. Since I found both arcs to lack character development or emotionally satisfying conclusions, it’s harder for the series to maintain the surreal madness high I want from it over a longer period of time.

  I still want JoJo to be a part of my life, as everyone should, so I’m faced with the quandary of how to consume it and other serial shows with my new schedule. I’m working 12-hours a day, four days a week, listening to podcasts as semi-background noise. All I can watch during the week are relaxing episodic shows while the weekend features my Mom and I binging series together when the dogs she watches for her job finally settle down.

  I’m going to have to start scheduling when to consume entertainment on my days off. I have a massive backlog of tv, movies, comics, books, and even some video games that I would like to get to. I’m used to picking what to do based on my current mindset, and failing to make a timely decision due to the sheer number of choices combined with insecurity over starting something new without finishing something else first. So I’d like some advice.
  ```

---

