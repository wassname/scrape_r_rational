## Show r/rational: Ficdb - Goodreads for fanfiction

### Post:

Hey r/rational \-

Happy to introduce [Ficdb](https://ficdb.com), my side project for the past two months.

[Ficdb](https://ficdb.com) is Goodreads for fanfiction, a platform discover, review, and share fanfics worth reading.

Still rough around the edges, still light on features, but ready for your feedback!

What is Ficdb’s short-term goal? To create a review and categorization database for popular and/or well-received fanfiction.

What is Ficdb’s long-term goal? To create a Netflix-style recommendation engine for fanfiction. With each review you provide, Ficdb gets a little smarter and little more data to work with.

Why release on r/rational? I enjoy rational literature, know that other programmers frequent this subreddit, and expect some pretty good feedback from ya’ll. Good a starting point as any.

What’s the release schedule? Everyday this week, I’ll add 10 new rational fanfics to the system. Come back again tomorrow for some more goodies. The focus for me over the next few weeks will be responding to your feedback, so fanfiction submissions from non-admins are closed for the time being.

How can I help? Sign up, find some cool new fanfics, give them a star rating. Once you’ve done that, swing on over to the [Discord community](https://discord.gg/uRrEHfV) I’ve created for feedback.

What feedback do you want? Ficdb is a wide-eyed, bushy-tailed baby of a web application. Therefore, expect some level of friction when using it. If you find a bug, definitely report that. In terms of feature feedback...

* How can I improve the filter system?
* What additional data would you like for each fanfic to have?
* What genre categories are missing?
* What fanfiction data or categorizations are incorrect?
* Are you okay with the passwordless authentication system?
* How much should I prioritize adding a main character field and pairing field to each fanfic?
* How much should I prioritize adding fandom-specific tags?
* How much should I prioritize making reviews upvotable and filterable?
* How much would it help to have a filterable page for reviews, similar to the fanfiction index page?

Cheers!

Jordan

### Comments:

- u/None:
  ```
  Sounds like a good project. I recommend seeing if you can contact knighty from [fimfiction.net](https://fimfiction.net) to get any advice. Even if you can't, I recommend modeling your site after it as much as possible. fimfiction is my favourite website; it's brilliantly designed in how easy it is to search for stories, how often new popular stories pop up on the front page, the social media aspect of it, how easy it to navigate in general. Just a generally great 9.8/10 website(there are always things to improve on, but not much).
  ```

  - u/Chousuke:
    ```
    I wish there were a non-pony fimfiction somewhere. It would make every other fanfiction site obsolete
    ```

    - u/None:
      ```
      As far as I know knighty has been working on it for the past several years, but has yet to actually release it. It's a real shame too, if it was released in like 2015 it would completely dominate and unify the web fiction community. Now there are too many inferior competitors like royalroad out there for things to completely switch over to one site I think.
      ```

- u/tehcrashxor:
  ```
  Bug report: Clicking the login link from email redirects to

  `http://localhost:4000/veil/sessions/new/[SessionID?Here]`
  ```

  - u/samosa_samsara:
    ```
    amateur hour over here...
    ```

    - u/chlorinecrown:
      ```
      I started typing a comment telling you off for mean criticism of a great project before I realized you were OP :P
      ```

  - u/samosa_samsara:
    ```
    Could you try logging in again and letting me know if it works? If not, PM me your email!
    ```

- u/xamueljones:
  ```
  If you need a list of rational fanfiction to add, there's a website call [RationalReads](http://rationalreads.com/) that might help.
  ```

- u/samosa_samsara:
  ```
  Also happy to read feedback here if Discord isn't your thing! Going to go for a hike, but I'll be back online in an hour or so
  ```

  - u/copenhagen_bram:
    ```
    Will you make it open source?
    ```

    - u/samosa_samsara:
      ```
      Maybe... I've seen both the good and the bad of managing an open-source project, and not sure I want any additional TODO items on my plate right now. Could be cool if people want to contribute some Elixir/Phoenix code though.

      I'm going to mull this one over for a bit before I decide.
      ```

      - u/copenhagen_bram:
        ```
        What is the bad of managing an open source project? Like, I've heard that managing an open source team is like herding a pack of kittens, but what if you develop the software as you would if it were close source, except the source is available and people can make their own version if they want? As in, you (and your team?) develop the software and don't accept contributions, and if anyone wants to contribute they'll have to make their own fork.

        And as someone who loves free and open source software but for some reason browses Reddit, thank you for mulling it over. lol
        ```

        - u/Almenon:
          ```
          I manage python-shell.  A lot of people don't read the readme and ask me questions instead of figuring it out themselves. Which can be annoying but it's cool seeing people are using the project so I don't mind it too much.  

          Python-shell is just a repo with ~1k stars, once you start getting to the really big repos it gets rediculous.  THOSUANDS of issues, weekly pull requests, dev infighting, etc... For example there was recently some drama in the /r/python community about removing the 'master slave' terminology for being offensive.

          But for small projects like this one I don't see any downside to open-sourcing it.
          ```

          - u/samosa_samsara:
            ```
            >Python-shell is just a repo with \~1k stars, once you start getting to the really big repos it gets rediculous.  THOSUANDS of issues, weekly pull requests, dev infighting, etc... For example there was recently some drama in the /r/python community about removing the 'master slave' terminology for being offensive.

            Yah, I think I'll try dumping all this on a Github later today, and see how it goes.
            ```

  - u/cysghost:
    ```
    There goes all my free time. I hope you’re happy with yourself!

    It looks good from a brief view of it, and I’ll certainly be using it and checking it out. Thank you!
    ```

    - u/samosa_samsara:
      ```
      Thx! Time well enjoyed is never wasted ;)

      Adding more fanfics right now...
      ```

- u/Watchful1:
  ```
  Why do you call it fanfic if you have original stories on there?
  ```

  - u/samosa_samsara:
    ```
    I guess it is fanfiction + web serials but that was a bit clunky for a motto...
    ```

    - u/CoronaPollentia:
      ```
      Webfiction?
      ```

      - u/samosa_samsara:
        ```
        Huh, sounds good. I'll use "fanfics and web serials" in the top message (on second thought, not that clunky), but "webfiction" in the FAQ.
        ```

- u/marwin42:
  ```
  I tried to sign in, but the "sign in"  button on the verification e-mail seems to fail to load. [here](https://imgur.com/a/XaItyPp) is a link to screenshots.
  ```

  - u/samosa_samsara:
    ```
    Could you try logging in again and letting me know if it works? If not, PM me your email!
    ```

    - u/marwin42:
      ```
      Tried again and is working fine now, thanks for replying.
      ```

- u/suyjuris:
  ```
  I like how quick the site feels. In the FAQ you mention that you feel that enabling people to submit works would skew the average number of reviews. Maybe you could just require users to have submitted X reviews before (or for each) work submitted.

  Also, are you planning to provide public data dumps once you start doing recommendations?
  ```

  - u/samosa_samsara:
    ```
    Getting together a moderation team atm to help filter bunk submissions - public data dumps are kosher, trying to err on the side of open source.
    ```

- u/NewDarkAgesAhead:
  ```
  This is a wonderful idea. Goodreads has been known to delete book pages with hundreds of reviews just because those were works of fanfiction.

  >In terms of feature feedback...

  If not already present: 

  1\) Please add an option of user-triggered data backup \ exporting (similar to goodreads — in xls, etc).

  >What genre categories are missing?

  2\) Please add an options for creating custom categories, tags, or both.

  > How much should I prioritize adding a main character field and pairing field to each fanfic?

  > How much should I prioritize adding fandom-specific tags?

  These could also serve as an alternative solution to these problems

  ---

  3\) Maybe add an option of importing already existing, "combed-through" data from other similar platforms (e.g. goodreads, TVtropes, wikias, etc) for quicker database accumulation.
  ```

  - u/samosa_samsara:
    ```
    Most def to export feature, working on main character fields at the moment, I do have scrapers to help import fanfics from ff, ao3, fp, sv, and sb but reviews will have to be hand-jammed... want to let the community decide what it thinks it values, not another sites.
    ```

- u/narfanator:
  ```
  This is a really nice design!

  I hope I can use this to track things that update irregularly, as well as find new fiction, as well a point people at lists of fiction I recommend.
  ```

- u/Almenon:
  ```
  I would suggest reducing the rating to 3 digits.  For example, "Flechette's Foodie Forays (Foodfic, Collab)" is 4.666666666666667 but it would be better represented as 4.67

  I would also suggest removing the visual timing information in the search (ex: .097219 seconds) in the production website - it's useful for you as a developer but so much to the casual user.

  I like your css transitions on the top menu. Cool stuff :)
  ```

---

