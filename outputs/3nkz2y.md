## [D] Monday General Rationality Thread

### Post:

Welcome to the Monday thread on general rationality topics!  Do you really want to talk about something non-fictional, related to the real world?  Have you:

* Seen something interesting on /r/science?
* Found a new way to get your shit even-more together?
* Figured out how to become immortal?
* Constructed artificial general intelligence?
* Read a neat nonfiction book?
* Munchkined your way into total control of your D&D campaign?


### Comments:

- u/thecommexokid:
  ```
  **How can I improve the availability of my recall?**

  I am often frustrated with my memory ability.

  Some scenarios: I had a job interview on Friday, and my roommate asked me the next day how it went. I was able to give a general impression, but I had trouble repeating very many specific questions my interviewers had asked. Or: My sister’s wedding is coming up, and I would like to include some funny stories from our childhood in my toast. But after ruminating, no specific such stories spring to mind, only the vague sense that there have been lots.

  But on further reflection, it’s not exactly a memory problem.

  If my roommate were to ask, “Well, did they ask you about ———?”, I immediately would know the answer, and indeed if he had prepared me a whole quiz in the form of a list of sentences, some of which were spoken during the interview and some of which weren’t, I’d have no trouble identifying which were which. And when I asked my godmother for help on the wedding speech, she suggested, “What about the time when ———?” and I immediately recalled the full details of the incident in question, and could pick up the story from the half-sentence she’d spoken so far.

  So the information I want is in my head, somewhere. It’s just not available (in the “availability heuristic” sense of the word “available”) if I specify too general of a query.

  There are lots of stories involving my sister and me that I could tell you if you asked the question in such a way as to remind me of them, but just the generic search “funny stories involving my sister” turns up none of them. When my godmother asked me about that particular day, my internal sensation was not, “Oh, I’d forgotten about that until you mentioned it just now”; it was, “Duh, of course! Why didn’t I think of that until you mentioned it?!"

   Are there strategies to improve my recall to general queries? If not, are there strategies for me to self-generate more specific queries when needed?
  ```

  - u/None:
    ```
    Well there's Bacopa Monneiri, check examine.com for details on that.

    I've found it helps with recall but at the cost/benefit of making me more prone to daydreaming and reduces anxiety (which is not so good when you don't have enough to start with like me.)

     My daydreams are more vivid when I'm on it, and my sleep is a little disrupted, but my recall is definitely better. 

    In terms of cognitive strategy, try:

    1. Keeping a diary of interesting stuff that happens to you, occasionally reviewing it. If you're a big fan of story telling like me this comes naturally, since I love telling stories and this helps me recall their details better.

    2. Using space repetition software like Anki to remember random facts you often forget. I have friend's birthdays, cool ideas I've had, etc. in my "personal wisdom" deck.
    ```

  - u/whywhisperwhy:
    ```
    I sometimes feel like I have the same problem, and so I've been trying a couple things: first, like you mention if someone asks me specific questions I can then usually remember, so I try to create my own trigger words for any events worth remembering, and then the first thing I do is just recall the trigger word to get me started. More generally, whenever I'm finishing the work day, I try to recap it and the same for real life when I go to bed. 

    Seems to work okay, but of course it could just be because of the additional effort in putting into it.
    ```

- u/iamthelowercase:
  ```
  > Found a new way to get your shit even-more together?

  Is anyone here already using [Habitica](https://habitica.com)?  (Tagline: "Your life, the roleplaying game".)  I stumbled across it this past week, and it looks promising.  But I haven't signed up yet, so 1) I'm not going to plug it directly :P, and 2) usecases from real-world users wouldn't hurt.
  ```

  - u/BadGoyWithAGun:
    ```
    I used it a while ago, it turns out my lifestyle isn't static or plannable enough to make proper use of it. Or at least that's how I justified losing and quitting to myself, at any rate.
    ```

  - u/gbear605:
    ```
    I use Habitica. It's really helpful for keeping up with my obligations. There are no large problems with it, though some of it feels like you either level up too fast or too slow, but that might be my own fault
    ```

- u/traverseda:
  ```
  So, I have some complaints about how software is done. I'm a big proponent of the unix way, but I think it falls apart these days, for a number of reasons.

   * You can't simultaneously edit files.

  Sure, back when programs were pipe-able it worked great. But these days a lot of what we do involves live visualization. Think image editing. All of your filters have to be built into your graphics program, or become annoyingly cumbersome.

  We've broken the whole "write one program that does one thing well" in favour of monolithic programs that do live interaction well.

   * Flat text data structures are bad

  Alright, maybe no bad, they're good for a lot of things. But imagine a 3D scene, like blender. It's composed of a number of sub formats, meshes (stl's), csg data, textures (png's), scene positioning, etc.

  These are complex datastructures made up out of simple blocks, but they don't typically show those simple datastructures without a cumbersome export/import loop.

  ---

  I propose a solution where, essentially, a state synchronized data tree replaces the file system. You subscribe to objects, and are alerted whenever they change.

  We implement something a lot like FUSE on top of that. So your png can appear to be an non-compressed n-dimensional array.

  Any of the other hundred or so software developers have any thoughts? Anywhere where I should clarify?
  ```

  - u/eaglejarl:
    ```
    > You can't simultaneously edit files.

    Depends on your definition of "simultaneously". I can have multiple files open in my browser and freely switch between them to make edits. If I'm making identical edits to a number of files (eg, adding some text at the bottom), then my editor can easily loop over all the files, applying my edits to them. From my perspective it's simultaneous. What exactly is your use case here?

    (EDIT: it just dawned on me that you probably simultaneous as in multiple people on one file, not multiple files by one person. If so, merge methods exist -- google docs proves that this is doable.)

    > Sure, back when programs were pipe-able it worked great. 

    You've got some typical-man bias going on here. The vast majority of what I do as a web programmer and author is pipeable, as is the work of most email handling, archive handling, web spidering, and a lot of other stuff. 

    > I propose a solution where, essentially, a state synchronized data tree replaces the file system. You subscribe to objects, and are alerted whenever they change.

    By "state synchronized", you're talking about what the Unity game engine does, right? The way it stores the entire state of the world in deltas?

    > You subscribe to objects, and are alerted whenever they change.

    I'd caution against making the file system object based. Objects are a decent programming abstraction, but they aren't well aligned with the needs of data storage. Objects are about expressing functionality with self-contained state -- code enforcing access to a chunk of data. 
    Programs are about actions expressed in code, so this makes sense. File systems, on the other hand, are about data first and function second. The reason Unix was so successful is that it designed a very minimal set of operations that could be performed on the data -- basically just CRUD -- and left the sophisticated actions (the code) to programs. 

    I think /r/trishume is on a good track here -- define some minimal CRUD operations for accessing data, and then have the rest defined as separate function . Things I would like to see in that:

    * All data handling is managed by function blocks 
    * There are basic blocks defined by the system (Ring 0)
    * Users can install new function blocks
    * Function blocks (including the Ring 0 set)  are ACL'd to manage security
    * Data is transactionally managed on the Ring 0 level


    If you want observer/responder mechanics, just set up the "subscribe" block and point it at the piece of data you want. If you want your system to be state-synchronized, chain a "snapshot" block to the Ring 0 functions. If you want full drive encryption, chain (de|en)crypt blocks to your Ring 0 functions. And so on. 

    The beauty of this is that you can have an encrypted drive segment for privacy, I can have a non-encrypted segment for speed, and neither of us has to think about it -- we both see the same system interface, yours just works differently because at one point you told it to.
    ```

  - u/AmeteurOpinions:
    ```
    How do you transition from oe to the other, without creating your own OS and going head-to-head with, say, Windows?
    ```

    - u/traverseda:
      ```
      There's no particular reason you couldn't run this, and this-enabled apps along side traditional stuff. Just like a bunch of apps have their own sqlite database for storing stuff.

      It doesn't have to run at the kernel level, so it can be just another database service.

      ---

      Don't target windows users, target people who like cool technology.

      So that's the hacker/programmer contingent. Rethinkdb is doing a bunch of similar stuff with their change feeds, this is like that to the extreme.

      One of the big advantages to this approach would be that it would make creating collaborative software much easier. Coupled with a *good* scene graph, it would be an excellent platform for emerging vr/ar stuff.

      Other then that, it could be a great platform for creating collaborative web apps like google docs.

      In short, it's just another service, like dbus or postgres.
      ```

  - u/trishume:
    ```
    Some good points and ideas here. I've been thinking that a framework of strongly typed functions might be a better new model. Easier for programs to use and graphical terminals could add nice interaction widgets depending on types (calendars for dates, etc...)

    Would also allow better data structures like you are talking about. Publish a PNG data structure/type description and then also a function from PNG to 2d byte array and back.

    Edit: I meant static types, not strong
    ```

    - u/traverseda:
      ```
      Is it really strongly types if it's at the framework level? I presume you're building more complicated types out of some (strongly typed) basic types, but really whether they remain strongly typed depends on the clients language, no? 

      You'll have to excuse my, I dropped out of highschool so my actual computer science might be a bit weak.

      Not entirely sure what you mean by a "strongly typed function". A function written in a strongly typed language?

      > to use and graphical terminals could add nice interaction widgets depending on types (calendars for dates, etc...)

      Xonsh is nice to play with. It's python frankensteined onto bash, so you get bash with python types. Is lots of fun, doesn't have widgets like you describe but it could.
      ```

      - u/trishume:
        ```
        Oops I used the wrong term, I meant static types, although they could also be strong depending on the language as you say.

        In terms of the type system I was thinking something like the type specs of capnproto for structure and convention/names for semantics.
        ```

        - u/traverseda:
          ```
          >capnproto

          Very cool. Thanks for sharing. I'll have to look into it more in depth. I'm afraid I was going to serialize using rpyc's brine protocol, and fall back to json. This looks cool.

          I think even standard json is statically typed. It really does depend on what language is reading the data, be it json or whatever. Unless you're suggesting that a schema enforces particular types? I was imagining you'd be able to add random attributes to an "object", or random keys to a hashmap/dict.

          You have an stl, and you can add arbitrary metadata.

              stl:{
                  vertexes:[ ... ],
                  faces:[ ... ], #Standard stl stuff
                  authors:[ ... ] #not part of standard stl spec, metadata that only some programs know how to use
              },
              png:{
                  ...
              }

          Which implies duck typing at least, I think? If we want different programs to be able to work on the same data, we need to be flexible in what attributes exist.

          Low level types definitely need to be static, but I think the types built on top of that need flexibility. Most programs would completely ignore the author field, so it's not true static typing. I mean, it's not really duck-typing either because these aren't functions, they're attributes/keys. Describing programming concepts is hard, but I think we're on a pretty similar page.
          ```

          - u/trishume:
            ```
            Capnproto is stronger than JSON because it uses pre-defined schemas but in such a way that you can add new things in a backwards compatible way. Which gives you stronger safety guarantees than JSON style but extensibility must be linear, which has upsides and downsides.
            ```

            - u/traverseda:
              ```
              Hm, that counts as strong typing, definitely.

              I like capnproto's obvious speed, but coming from a duck typing language that is a bit of a turnoff. Makes it a lot easier to treat it like a file system. 

              For example, I was imagining the following

                  #Python!
                  stateTree['home']['traverseda']['.vimrc'].subscribe(callback=reloadvimrc)

              capnproto is definitely going to be faster. Just so much faster. 

              It's not as good over a network, because it's not a state synchronization protocol, and isn't "diffing" to decide what data to send. We want to only send changes to data that clients are subscribed to, so it works well over the network...

              That's something I suspect could be implement for canpnproto though. It also provides an RPC mechanism, which is nice.

              I think that in order to be reasonably network transparent, we might need to abandon speed anyway. You'd going do be dealing with ~120ms pings at the worst end, so that's already out of the bag.

              Limiting the scope to *just* a state synchronized data store might be better, because it sets expectations. This isn't suitable for real time anything, you need to do stuff in parallel and distributed as much as possible.

              At that point instead of and RPC mechanism, we have a distributed task queue, and the results get stored in the state synchronized task queue like everything else, where they then call a callback function on the client's that are subscribed to it.

              Not convinced of capnproto for this, but I'd like to be. The speed is *very* appealing.
              ```

  - u/nicholaslaux:
    ```
    > You can't simultaneously edit files

    This heavily is dependent upon the file type you're talking about. Images and videos are two specific types of files that do not play well with simultaneous editing, in large part because most formats are proprietary (psd quickly comes to mind since you mentioned layers and filters, and I assume most video formats are the same way) and/or don't easily lend themselves to easy merge functions. 

    However, a much more common example of a file that users are likely to want to simultaneously modify would be a spreadsheet or a text document.

    In both of these cases, there are existing and obvious merge methods which are easily shown/applied. Additionally, the few formats of these files that exist are either public/open source, or have merge methods built in to their proprietary software. 

    It's possible that I simply don't understand your issue due to not working in an industry that uses the types of files you're talking about much (I'm a programmer myself), but between tools like Dropbox and its competitors, git and similar services, and various relational databases, I don't see a large motivation for a generalized solution to this issue, and the specifics mentioned seem more to lead me to a specialized solution. Nothing about this tells me that a psd merge tool is likely to have more than superficial similarities with a blender file merge. Additionally, I don't forsee a great number of people wanting to handle merge issues in either of those formats external to their respective programs, or else there would be more competitors to modifying files of that format (rather than competing tools simply utilizing their own proprietary file formats).
    ```

    - u/traverseda:
      ```
      >to handle merge issues

      The idea is that by keeping data-structures up to date, you minimize merge conflicts. Where there are merge conflicts, they should mostly be due to simultaneous user edits, which is up to the user to resolve.

      It's important to note that it's *not* a flat file, where you have to merge things. It's a data structure. Instead of merge issues, you get collisions or race conditions when two clients/users edit something at the same time.
      ```

      - u/nicholaslaux:
        ```
        So you effectively explode the file format away from a single file and into a file structure, the individual components of which need to be merged, but if you aren't working on the same components in the structure then they can auto merge, right? 

        So if I modify layer 1 and you modify layer 2, there's no collisions, but if we both modify layer 1, then there is and you need to merge those changes somehow.

        Inherently, you're allowing for modification of the same document simultaneously (otherwise you could just sync via any of the existing solutions and just say "don't edit at the same time" or lock the file down while someone else is editing it). So you ultimately still need to determine some sort of merge process for whatever components might collide or else you're simply pushing the problem to a lower level and saying "you can both edit just one person gets access to this layer first" rather than "whoever gets to the file as a whole gets access and the others must wait".

        (Also, having never worked with photoshop, blender, or anything similar in anything other than a personal hobby capacity, is simultaneous editing of different parts of the same document/scene/file common? It's possibly just my lack of knowledge on how these tools are being used in real world scenarios that is preventing me from understanding the full scope of the problem and this solution.)
        ```

        - u/traverseda:
          ```
          > but if we both modify layer 1, then there is and you need to merge those changes somehow.

          Only if you both do it at exactly the same time, where exactly is probably around 500ms. If that's happening, you'd see the other user editing your file in real time, like you do on google docs. If someone is overwriting the text as you write it, the problem is obvious.

          > "you can both edit just one person gets access to this layer first" 

          Works when it's obvious who's editing what (because it's realtime) and when the slices are small enough. Don't think layers, think individual pixels. If you're not both editing the same pixels at the same time then it should be fine.

          >simultaneous editing of different parts of the same document/scene/file common

          Nope, not really common. Those examples are more to illustrate what it is then how I think it would be used. Imagine an augmented reality office, and you both want to interact with the same visualization. Or imagine you're a programmer, and you want to write tools to do voronoi simplification to a mesh, but don't want to write a plugin that's specific to only one CAD program.

          The unix way says "write programs that do one thing and one thing well". That's not how most modern software works. It's all monolithic. This could enable you to write software that only does one thing.

          It's more a different style of programming. One focused around microservices and task queues.
          ```

- u/Kishoto:
  ```
  Sociopathy. Mostly characterized as a distinct lack of empathy or moral founding Portrayed in popular media mostly through serial killers, the crazier the better. Here's my question/discussion point. Have you ever met a real sociopath? Someone who exhibited what seemed to be sociopathic traits? I know the media would have us think all sociopaths are psycho serial killers, but that isn't so. 

  So please, if you will, regale me of your findings on sociopathy, whether you've researched it, watched tons of fiction, or, preferably, are (or have met) real life socio/psychopaths. :)
  ```

  - u/xamueljones:
    ```
    Yes.

    It's an insanely aggravating story and while I'm grateful to have the skill to handle any sociopaths I may meet in the future, I wish I never met the guy and I am thankful that he's gone without causing too much trouble.

    Let me just say the guy was a brilliant actor who put up like four different facades to four (I think) different women at the same time over a span of years. It finally came crashing down when one of them found out about the other women and started accusing them of stealing him away from her and her daughter.

    The other women started realizing he was a rather toxic relationship and tossed him out of their lives and one even had a police escort to watch over him moving his stuff out. At least one women went to therapy for a while and is much more positive now.

    He was concluded to be a narcissist due to how often he only showed up and did activities with the women when it directly centered on himself. The sociopathy was deduced based on how he would act apologetic for hurting someone's feelings and quickly move on without a shred of regretfulness. It was almost bipolar how quickly his emotions would change. He was often described as having multiple personalities and a lot of clutter left behind was found such as having several different dishes and other supplies for multiple households. He even left presents from his daughter behind.

    One women even said, "Who the hell was this guy? I don't know anything about him!"

    The defining hallmarks is the ability to show a lot of different faces to different people. So you won't necessarily notice anything unusual until you get the chance to meet the sociopath in a dramatically different place/occasion from when they normally meet you. They will also be very controlling about everything. For example, this guy had a job in construction and engineering, so he could control when he wanted to drop by and whenever someone wanted to reach him, they only could get to him through his cell and he'd never respond until *he* choose to text back. He wanted control over how people perceived who he was. In addition, he never spent more than a few days in company with anyone. I think he would reach a point where he couldn't maintain the facade any longer and needed to be alone.

    I noticed that he had a very strong 'moral' code, but I think it was mostly rules he followed to ensure that he stayed out of jail and fit into society. For example, he never hit a woman for the public image of being chivalrous, and he never told a lie (or never was definitively caught in one) to seem trustworthy.

    If you want to get a sociopath out of your life, get help from other people for the support. Give very clear demands on what you want them to leave with and if at all possible, get police help. Don't give into even the most simple change to your demands. When dealing with sociopaths, the saying "Give an inch, and they'll take a mile." is very true.

    If you are in severe trouble and don't know how to deal with a sociopath, I recommend talking to a therapist/psychologist. One of the women got very good advice from her therapist on how to get rid of the sociopathic boyfriend and it worked to get him to leave without causing trouble.

    If I sounded very angry or disgusted about sociopaths, it's because I have very good reasons to feel angry at people who would have ruined other lives without a second thought for even the slightest benefit for themselves.
    ```

  - u/ToaKraka:
    ```
    [It's been suggested that I myself am sociopathic,](http://i.imgur.com/VCZSnwZ.png) but I'm not all *that* inclined to believe those anons--not least because I'm absolutely terrible at lying, due to [an utter lack of originality.](http://np.reddit.com/r/rational/comments/3n8fep/d_friday_offtopic_thread/cvlyiau)

    On the other hand, though, I haven't got much in the way of morals, [I haven't yet met anyone for whom I've felt much real affection,](http://i.imgur.com/Sxjgmd0.png) and [I constantly fantasize about having people under my (totally undeserved) control.](http://np.reddit.com/r/AskReddit/comments/3m7f4e/what_do_you_fantasize_about_regularly_that_doesnt/cvd6f63)
    ```

    - u/electrace:
      ```
      > It's been suggested that I myself am sociopathic,  but I'm not all that inclined to believe those anons--not least because I'm absolutely terrible at lying, due to an utter lack of originality.

      If you're only terrible at lying because you can't think of an alternative scenario that explains what the other person already knows, then that has no bearing on you being a sociopath.

      I'm a bad liar, not because I can't think of an alternative explanation (for most scenarios, I can; seeking alternative explanations is basically how I organize my thoughts), but instead, it's because my body, against my will, reacts to my guilt (Ironically, the same reactions also happen if someone *thinks* I'm lying, which I guess technically makes me a great liar, as long as people know that about me).

      That being said, you're probably a high-functioning autistic. A sociopath would have picked up on the (honestly, pretty obvious) implications of the other posters. For example: a sociopath would never have assumed that non-verbal meant emoticons. 

      You also don't seem to be very arrogant, and under-react when your character is being attacked, the opposite of a sociopath. You're ambivalent towards things that matter to most people (like family and friends), but care about things that most people don't even bother to think about (like a singular "they"). It practically screams autism.

      However, "I constantly fantasize about having people under my (totally undeserved) control" sounds extremely sociopathic. But when you look at the link, it seems like the fantasy is actually to get your own specialized fanfiction, which I gather is your obsession. I'd guess that if you could control, say, a general AI to get that same fanfiction, you would.
      ```

    - u/eaglejarl:
      ```
      If I may ask, why are you outing yourself on this? It seems like it comes with a reputational hit with no upside.
      ```

    - u/Kishoto:
      ```
      What about family? Parents? Siblings?
      ```

  - u/eaglejarl:
    ```
    Yes, I have. 

    He was charming and smooth and very likeable. He lied fluidly and without effort. Examples:

    "Tell $important_person that I can't make the meeting because I'm sick." He had forgotten about the meeting.

    "If my girlfriend calls, you and I were riding bikes today."  I assume he was cheating on her again. He was amazed when I said I wouldn't lie for him -- it was as though this were an unimaginable concept, that lying would be something to avoid. 

    He didn't show up for work one day.  When I finally called him to see if he was okay, it turned out that he'd gone on a junket to a nearby vacation spot...oh, but it was business-related, really! It was a gathering of ad execs and he was going to be doing a 5-minute presentation to them!  And spending two days there, but hey. 

    He lied about things that were easily verified, which I thought was weird. 

    On the phone, I asked him to hold off on doing $X until tomorrow and he agreed. We hung up, I walked across the room to my desk, and he had already done $X. 

    He cheated on his girlfriend at least twice that I'm aware of. He was living with her at the time, so when she threw him out it was a problem, so you'd think that enlightened self-interest would have been enough to keep him from cheating even if integrity wasn't. Nope; I don't think it occurred to him that he might get caught. 
    Somehow, he managed to talk his way back into her house and her bed each time she threw him out. 

    He stalled off things he didn't want to do for literally weeks or months by "forgetting", and would get angry when called on it. 

    He would get his way through relentless pushing -- it wasn't possible to come to a compromise or make an agreement about something that wasn't the way he wanted. He'd make the agreement, then just raise the issue again the next day and keep after it until he got exactly what he wanted. 

    He freely mixed intimidation with smooth charm to get his way. 

    The list goes on and on. Co-founding with him was a miserable experience.
    ```

---

