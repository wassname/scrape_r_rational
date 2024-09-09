## [META] WebFictionGuide, the webfic catalog behind topwebfiction, considers shutting down

### Post:

[Link to content](http://forums.webfictionguide.com/topic/to-move-or-close-thats-the-question)

### Comments:

- u/darkardengeno:
  ```
  I think a rebuild is probably the best move. The top response is a developer proposing building it in Flask on a public github repo. If that moves forward I'd probably contribute and I suspect others would as well.
  ```

  - u/muns4colleg:
    ```
    This kind of website really, really doesn't warrant that kind of complexity. Honestly making it WordPress 5 compatable shouldn't be that difficult in comparision.
    ```

  - u/RedSheepCole:
    ```
    I understand "contribute" in this sense would mean contributions of coding time?  I ask as someone who's useless at all things technical.  My main concern would be having the project start and then suddenly evaporate as everybody realized the project was bigger than anticipated (and key people discovered new demands on their time, etc.).
    ```

    - u/wizzwizz4:
      ```
      It'll probably go like this:

        * A lot of people volunteer.
        * It starts off, with a bottleneck.
        * People drift off and away, as they can't help.
        * More opportunities to contribute arise.
        * Somebody advertises here again, this time explicitly.
        * A lot of people come to help.
        * A few new people submit pull requests.
        * Some of them stick around.

      This prediction is loose; I only assign roughly a 30% probability to this happening, conditional on somebody posting on /r/rational at that point in development. But I reckon something _like_ this will probably happen.
      ```

    - u/RetardedWabbit:
      ```
      Essentially yes, but public coding projects do pretty well at not "evaporating" they usually just grind to a halt if they lose support. If things are well outlined non invested people can chip in and do the smaller projects then leave, letting the people who are devoted focus on putting everything together. How good this is depends on the volunteer quality and style but ideally it shifts the workload away from very skilled people so all they can focus on complicated parts and tying things together.
      ```

- u/AmeteurOpinions:
  ```
  *WHAT*
  ```

- u/eroticas:
  ```
  That would be a shame. I don't think there are really any equivalents to it anywhere else?
  ```

  - u/Mountebank:
    ```
    There's scribblehub, made by the same people behind novelupdates, but I haven't used it much to know how comprehensive it is. And since it's related to novelupdates, the user base might be related so the tastes of the reviewers will probably beer towards things similar to your usual Asian webnovel.
    ```

    - u/endlessmoth:
      ```
      Scribblehub, from my experience, is just Royalroad except worse.  Lower quality submissions, and smaller, less active community.  You merely have to glance at the front page to see it's just the usual webnovel schlock.

      If you're considering Scribblehub, Royalroad is better in about all aspects.  Which isn't an endorsement; Royalroad is pretty bad.
      ```

      - u/RedSheepCole:
        ```
        I just Googled Scribblehub, and I think that's a fair assessment.
        ```

- u/RedSheepCole:
  ```
  Crossposting my proposed solution from the forum:

  "Revised suggestion: create r/topwebfiction.  New entries for the  queue are posted to it by authors.  Moderators index the posts as  entries on topwebfiction--meaning that, when you click the info button  next to The Wandering Inn on topwebfiction, it takes you to its original  submission post on r/twf.  Anything but index submissions as top-level  posts on the reddit would be deleted by moderation.  Reviews are posted  as comments.  Possibly a secondary subreddit would be needed for update  announcements and ongoing discussion of the stories in progress.

  This is an extremely hacky solution, but uses in-place architecture  that requires no maintenance and minimal pay (just to maintain  topwebfiction's domain), and will avoid the annoyance, disruption, and  debugging involved in a custom coding effort.  The big disadvantage  would be a period of anarchy as we transition from the old site to the  subreddit, but once the dust settled we'd have a perfectly functional  system that will last until Reddit goes bust."
  ```

  - u/wizzwizz4:
    ```
    It'd rely on Reddit pretty much permanently; you would never really be able to migrate from Reddit afterwards, and control would pass to Reddit, etc..
    ```

  - u/TacticalTable:
    ```
    Seems like a pretty big downgrade, tbh. Part of twf's charm is that it's a great barometer of what people are currently reading. Unless all the posts were cleared every week, and the authors reposted their fiction and updated the links, it would be a one-time popularity list. 

    The alternative is that fictions more than a 6 months to a year old (whatever reddit's archival time period is) would also be unable to be voted on, the front page would just be whatever the 25 newest fictions are, and the community would be very bad for good fiction listing (because reddit's algorithm is far from equal voting weight over time).

    At this point, a weekly strawpoll would be similarly sustainable alternative.
    ```

    - u/RedSheepCole:
      ```
      Sorry, not following you.  I'm new at Reddit; do old posts simply disappear entirely/get erased?  The original ad for PB from two months back is still searchable and open to comment, so I assumed not.  If that's not correct, then yeah, this whole scheme goes bust.

      Just in case it's not clear (don't mean to condescend, just not understanding your objection and want to eliminate uncertainty) I'm thinking of using Reddit purely as an index here, with the upvote/downvote system irrelevant to TWF's existing voting system.  TWF's info link points you to the original Reddit post even if it's four years old and listed at -27.  Community aspects (update announcements, discussion, etc.) would go in a separate forum and function normally.

      Again, this is kludgy as hell, and one major downside I've heard is that Reddit's search function isn't terrific; however, I have little faith in crowdsourced volunteer programming efforts, based on past experience, and the important thing seems to be preserving TWF, not WFG which is already pretty well dead.
      ```

      - u/TacticalTable:
        ```
        > the upvote/downvote system irrelevant to TWF's existing voting system

        * You cannot vote/comment on posts older than 6 months
        * Votes themselves are weighted by recency. If you see a post with 400 karma, that could be either 600 or 200 people upvoting it, depending on how old the post was at vote time.

        Unfortunately, it wouldn't just be kludgy, it would be non functional
        ```

        - u/RedSheepCole:
          ```
          Both would be irrelevant for TWF voting purposes, though the commenting restriction would dash my hopes of attaching reviews to the entries themselves.  I'm talking about using Reddit as a simple heap of index cards, a database.  You can downvote "Bob's Elf Story" till the crack of doom, and it will still exist and be linkable as the info page for "Bob's Elf Story" on TWF.  A bigger issue would be that you'd need a proper database for the links of TWF themselves.

          Now, on reflection, a simple out-of-the-box forum would work better for that anyway, without the weird restrictions; I'm spitballing here.  The advantage of Reddit would be sidestepping the maintenance-costs issue, which I could see being a problem.

          Ultimately, this may not have a solution, because WFG is a bit old and decrepit to save and the people helped most by TWF at this point are giants like Wildbow, or Royal Roaders, who have long-established fanbases and don't need it.  It's very nice, and more important, for little fish like me, too, but I for one don't have the spare time or skills to set up and maintain a real solution.  So we're all sitting around talking about all the different ways somebody else might bell the cat.
          ```

          - u/TacticalTable:
            ```
            Ah, I see what you mean. I assumed you were trying to create the voting aspect of twf.
            ```

            - u/RedSheepCole:
              ```
              No, Reddit's a totally different animal designed to capture a much more ephemeral kind of opinion, and besides, it requires logins.  The beauty of TWF is that it takes two seconds and no effort to vote, and the stakes are too low to be worth elaborate rigging with IP spoofing or whatever.

              But I do think I'm back to square one here, and I'm not confident that anyone has a lot of skin in this game.  There'd also be the issue of coordinating with WFG's owners to implement any solution.  Probably some sort of replacement will emerge organically in the coming months or years to fit demand.  Or maybe that's magical thinking on my part.
              ```

---

