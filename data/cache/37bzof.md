## What features should a perfect platform for hosting fiction have? How would a perfect community website for writers look like?

### Post:

Hi! I am a web developer, and I want to build a perfect platform for writers, which they could use to post their fiction/fanfiction, discuss writing, and later - publish books.

It would be ideal if I could make it useful for authors on this subreddit, because this is the kind of community I want to develop there.

So I want to ask you some questions:

- What would you like to  see on such a website? 

- What features do you miss on fanfiction.net? 

- What do you think a perfect platform for that would look like?

- What else(besides community and publishing your stories) would you like to see there? Like competitions? Collaborative writing? Writing Prompts? Book club? Anything else?

If you have any other ideas on the subject - please share them! I want to build the perfect place for writers to hang out, practice writing, share their fiction/fanfics, and find an audince.

### Comments:

- u/alexanderwales:
  ```
  > What features do you miss on fanfiction.net?

  My problems with ff.net:

  * Inability to copy+paste text
  * Inability to do much in the way of formatting
  * Publishing is a multi-stage process from Doc Manager to publication - should just be a single screen
  * Docs go "out of date", which makes editing or reworking old stuff a pain
  * Terrible review system
  * Inability to link to a review
  * Inability to add a link within a story
  * Clunky method of doing "meta" stuff like author's notes, FAQ, etc.
  * Terrible "discovery" system

  Pretty much all those complaints apply to FictionPress as well.

  I really like how Google Docs allows comments directly on the page, but that's definitely a technical challenge (and should probably start disabled if you want to share works). Having people be able to point to a line and say "this would make it better" is a godsend.
  ```

  - u/callmebrotherg:
    ```
    Archive of Our Own solves most of those problems, but they don't like hosting original fiction.
    ```

  - u/DaystarEld:
    ```
    +1 to all this, and to add a bit more detail to my biggest grievance, the terrible review system:

    * Reviews can't be responded to if written by guest accounts.

    * Reviews are responded to as private messages in interface

    * Responses to reviews can't be seen by others.

    Would love to see a publishing platform that allowed for more dynamic and organized author-audience interaction.
    ```

    - u/eaglejarl:
      ```
      > Reviews can't be responded to if written by guest accounts.

      I would say that reviews can't be responded to, period.  As you say, the 'response' consists of sending a PM, which is not the same thing as responding in public to a statement made in public.

      I had one reviewer who read through the first ~20 or so chapters of 2YE (all that was up at the time), leaving profane and insulting reviews on every single one.  (Oddly, most of those reviews ended with something like "really enjoying it!")  The problem was that most of what he was calling out related to things that he had misunderstood, misread, or not read at all.  I would very much have liked to leave responses saying "thank you for the input, please try not to be so profane and personal, and you actually missed a bit here" so that people reading the reviews would get both sides.
      ```

    - u/alexanderwales:
      ```
      Given the maturity level displayed by the internet at large, I sort of wonder whether author-audience interactions would go so well. Even with the current system as it is, I've seen authors calling out reviewers in the header of a chapter as "haters". Hell, this has happened in the real world with best-selling authors, and the big difference is that there's almost never someone holding a (mostly) anonymous fanfic author back and telling them that it's not a good idea to start a flame war about how awesome your work of fiction is.

      I mean, I'm a pretty level-headed guy, but when I get a review that says something like, "I wish I could teleport the author to me so I could punch him in the face" I do feel the urge to say something in response.

      On the other hand, I love schadenfreude.
      ```

      - u/DaystarEld:
        ```
        I suppose to help mitigate some effects of how out of hand that could get, the author's response to a review could have to be toggled by clicking on it, so that when you're scrolling through a story's reviews you don't see author responses taking up every other sentence as they endlessly thank reviewers in best case scenario and argue with them in worst case :)
        ```

  - u/codahighland:
    ```
    >Inability to copy+paste text

    The annoying part of this is that it's done intentionally. Fortunately there are browser extensions to fix it.
    ```

    - u/boomfarmer:
      ```
      If you open dev tools, search for the equivalent of `-webkit-user-select: none;` and remove it, you'll be able to select text and copy it again. It's just some silly CSS.

      The reason that disabling JavaScript allows you to copy is because that inline style is added via Javascript that checks for a cookie. It's in combo.js:

          a.css("-webkit-touch-callout","none");
          a.css("-webkit-user-select","none");
          a.css("-khtml-user-select","none");
          a.css("-moz-user-select","none");
          a.css("-ms-user-select","none");
          a.css("user-select","none");
      ```

      - u/Zeikos:
        ```
        Or just write "m" instead of "www" go into the mobile version of the page and you can copy / paste as you like :)
        ```

      - u/ancientcampus:
        ```
        Even better, there's a bookmarklet:

        [Bookmarklet to Allow Text Selection](https://alanhogan.com/code/text-selection-bookmarklet)

        No installation or hacking necessary.
        ```

      - u/codahighland:
        ```
        Well yeah, I mean, I work for Google, I'm a professional web developer, I know these things. :P But an extension makes the process a lot less annoying.
        ```

    - u/2-4601:
      ```
      Specifically, [Stylish](https://addons.mozilla.org/en-US/firefox/addon/stylish/) with [Stylish Sync](https://addons.mozilla.org/en-US/firefox/addon/stylishsync/) does a lot to improve...basically every frequently used site, actually. Those are Firefox links, but there are other versions for different browsers.
      ```

  - u/xamueljones:
    ```
    Just pointing out that [FicSav](http://ficsave.com/) is pretty good at making pdf, epub, mobi, and text files of any story you would want to copy.
    ```

  - u/raymestalez:
    ```
    Thank you very much for your reply!

     - Copy-pasting text and adding links will not be a problem =)
     - Stoiries will be written in simple markdown, it seems to be the most elegant way. I'll think about how I can add more interesting formatting features. Is there anything you find specifically important?
     - Publishing process will be as simple as writing or copy pasting markdown. In the future I am planning to add github integration.
     - Reviews and discovery system will be similar to reddit.
     - I'm still thinking about organizing 'meta' stuff, I'll make sure to make it as good as possible.

    I'll need to think about commenting specific lines. Maybe there will be some clever way to do this.

    But yeah, I'm definitely planning to fix all the problems you've outlined.
    ```

    - u/alexanderwales:
      ```
      Markdown is great. The one thing that I'd request are keyboard shortcuts, so that `ctrl + i` will give me asterisks around my selection, or throw down two asterisks with the cursor in the middle of them (which is the current behavior of [Reddit Enhancement Suite](http://redditenhancementsuite.com/)). But then, I love keyboard shortcuts.

      Live Preview would also be a definite plus (also currently implemented by [Reddit Enhancement Suite](http://redditenhancementsuite.com/)).
      ```

- u/eaglejarl:
  ```
  Second everything /u/alexanderwales said.  In addition, FFN is missing:

  The ability to reply inline to a review.  

  A decent mobile interface.  I can go to the desktop version but it periodically forgets that that's what I'm choosing to do and tells me that it can't find that page on the mobile site.
  ```

  - u/None:
    ```
    > The ability to reply inline to a review. 

    Oh god yes. If I never read another chapter that's half review replies, it'll be too soon.
    ```

- u/IWantUsToMerge:
  ```
  Inline error reporting, or at least inline commenting. Most fics would be error-free by now if this was a thing.
  ```

  - u/alexanderwales:
    ```
    Yup. I have stuff on ff.net at this very moment which contains errors I've never fixed, because the process for it is basically:

    * Read review that points out error.
    * Go into doc manager, load up the chapter.
    * Find error.
    * Fix error.
    * Save.
    * Go into story manager.
    * Update chapter.

    This is fine if there are one or two things, but if there are more, it makes the unpleasant-but-necessary janitorial work of writing really arduous. In Google Docs, it's literally a single click to fix something that's wrong.
    ```

- u/ArgentStonecutter:
  ```
  I'd like something that did wiki markup, automatic forward and back links from an automatically generated table of contents page... but the author should be able to edit the ToC as well (perhaps with metadata on the chapter) so you can get things like:

  <image> Chapter 23, Rational Cannibals
  (wherein our heroes discover that they taste really good with ketchup)

  Intra-story links should be maintained contextually, so if the author needs to rearrange chapters they stay consistent.

  Minimal decoration, or the ability for the reader to request a minimally decorated view. Because some of us have eyes that aren't as young as they used to be.
  ```

- u/RMcD94:
  ```
  Comment section per chapter, review section per chapter, reviews should be commentable, preferably acting like it itself is a chapter in terms of keeping consistent look. 

  Comment section should be sortable, as should reviews. Comment section should be like reddit, not sure if you need downvotes, but the default sorting should be age. Comment trees should be possible.
  ```

- u/traverseda:
  ```
  Open source
  ```

  - u/raymestalez:
    ```
    Absolutely!
    ```

- u/Thinker6:
  ```
  Look at Archive Of Our Own (www.archiveofourown.org) for a good example. It has a much, much easier interface than fanfiction.net, its tagging system is rich and has a lot of advantages, it has nice features like letting you group stories into collections, you can reply to reader comments with proper discussion threads, etc. 

  Some features I'd like:
  * For readers: a feature to auto-recommend stories based on the currently viewed story or your pattern of likes, sort of like Amazon does. ("people who liked this story also like", "people who liked works you like also liked this new story", etc.)
  * For authors: a way to upload chapters and have them published automatically at preset dates/times. Good for serial fiction. AO3 lets you upload chapters in advance, but you have to manually press a button when you want to publish them (and manually edit the publish date for it to be the pub date rather than the upload date).
  ```

- u/callmebrotherg:
  ```
  To start with you might want to check out Archive of Our Own. They are a *lot* better than FFnet/Fictionpress, and I don't really have much to complain about with them.
  ```

  - u/raymestalez:
    ```
    Thanks, I will do that!
    ```

- u/tomintheconer:
  ```
  i always wish there was a talk page. to discuss and clarify things. per chapter, per story. whichever.
  Book clubs and tags are good. It can be hard to find certain types of writing when looking for stories.
  ```

- u/torac:
  ```
  I like the design of fimfiction.net and think it would be a far better baseline to strive for than fanfiction.net’s. I recommend checking it out. Really wish it contained more than just pony stuff. Some features:

  * great search function
  * each fic can be downloaded in a selection of formats
  * bookmarks can be set within chapters of each fic, which is really neat if you have to stop in the middle of a huge chapter.
  * If you view a story, on the side are a lot of recommendations of stories that are similar, by the same author or also read by others who read this one
  * You get feeds from authors you follow, which you can divide into getting just stories, or blog posts etc. 
  * Probably a few more nifty things I don’t think of at the moment
  * I’m pretty sure I read a story where part of it was written in crayon by Pinkie Pie, but that might have been a dream.

  Here’s a story you can check it out with. On the bottom right you will notice that it is featured in the lesswrong group.

  Edit: Forgot link: https://www.fimfiction.net/story/6515/days-of-wasp-and-spider
  ```

  - u/GaBeRockKing:
    ```
    Yep. My position on the ideal fanfiction website would be "fimfiction, but general purpose."

    Plus, fimfiction already has a large audience, so it wouldn't be as hard to move people onto there.
    ```

  - u/raymestalez:
    ```
    Whoah, thank you for a great link! I didn't know about this website, it is extremely well done. This will be *very* helpful.
    ```

- u/mns2:
  ```
  Netflix style recommendation, downvotes, chapter visit count info for readers, history tool
  ```

- u/ancientcampus:
  ```
  Don't know if this would be good for a "professional" fiction site, but I've long wished Fanfiction.net or ArchiveOfOurOwn had a sorting algorithm that would factor "favs per total viewers", possibly adjusted for length too. As it stands, fics that are older, longer, and "more mainstream" are the ones that sort to the top when sorted by favs.
  ```

- u/None:
  ```
  **As an author:**

  When uploading a story, something to automatically split out a large document into chapters would be awesome. I'd rather upload one document than manually split out each chapter. That requires people to format their documents properly, though.

  Make the "upload a new version of a chapter / story" workflow as blindingly obvious and simple as possible.

  Google Docs integration would be nice. If I could share a story with your service and have it be automatically ingested, that would be pretty cool. I'd want to manually control when it updated, of course. In practice, this isn't much different from just uploading files, but it suggests a particular technology that's good for beta readers. Low priority.

  (Unless you make something as good as Google Docs, I don't want to edit my work in your interface.)

  A preview system for a new story or new chapter. I've had stories that I had to republish four times to get it right. Not terribly professional. If I could preview them instead, that would be a lot nicer for me.

  Horizontal rules. I understand that LibreOffice doesn't do real horizontal rules; it just does paragraphs with a "horizontal rule" style. Whatever you can do.

  **As a reader:**

  RSS feeds for each story and author. (I'm such a big fan of RSS that I made my own RSS reader.)

  Ability to download epubs. I had to write my own script to do this eventually (which, on a good day, works on portkey.org, fanfiction.net, and spacebattles forums).

  Failing that, semantic CSS classes. I don't want to find the first H1 tag, grab the story name from that, look for the third <select>, get the chapter list from that, etc. I want to be able to search for "div.story" and "h1.title" and "select.chapter" or something simple like that. Also, predictable (or at least discoverable) URLs for each chapter in a story. No Javascript to look up the document ID of chapter N+1.

  A dedicated space for author's notes. I want to be able to include them or exclude them from epub generation, or at least have them in a standardized format.

  Something better than "sort by number of reviews". If I review a story, it might be to give feedback to the author about a chapter. It might be because the story is terrible and I want to warn people away. ffnet has the "favorite" button to handle this, but I think it would be more effective if it had a "review and favorite" option in addition.

  Roll up a succession of chapter reviews by one person into one effective post. I go to fanfiction.net or portkey.org reviews, and I see one person with fifty one-line reviews, one for each chapter. It's a nuisance. Alternatively, only show the reviews for one chapter at a time, but that would be kind of annoying too. Or separate chapter reviews from story reviews, but that's troublesome too.
  ```

  - u/callmebrotherg:
    ```
    What about being able to upvote/downvote stories, with the ability to search by number of upvotes and/or percentage of upvotes?
    ```

- u/None:
  ```
  A better mobile app to act more like a library/sync, than a reader. Fanfiction has a terrible one.
  ```

- u/benthor:
  ```
  I miss something like github-style forking and pull requests. A lot of fanfics I enjoy have little to no editorial support and it shows. Being able to easily help fix things like typos, misapplied/misrepresented concepts or grammatical idiosyncrasies would be awesome. Not to mention having a decent way to actually collaborate on a story. There are people good at dishing out amazing concepts and others who are good at turning those into elegant prose. The system could be designed to very visibly highlight the heritage of each story, maybe even on paragraph-level.
  ```

- u/passcod:
  ```
  **As a reader**

  * Having a digest sent every week (with the day selectable, for me that would be friday or saturday) of all updates that occurred (story updates, new stories in collections I follow, new stories by authors I follow, etc) in that past week.
  * FF.net theming controls are fine, could afford to be more obvious and have more / better fonts.
  * A clean reading UI.
  * A lot of stories have very long chapters, which is great, but I'd love to be able to keep my place *within* a chapter (page scroll) when switching computers/devices.
  * A way to hide the authors' notes, and also a way to read only the authors' notes.
  * Good search within the entire site, with a rich syntax and some kind of "relevancy index" and/or "quality index" (think Github/Google/ElasticSearch).
  * Full text search within a story. This is something I'm really missing right now, and relying on google/extraction tools for.
  * Related to the above, full text search with the story *except the stuff I haven't already read*.
  * Blacklisting of entire categories, for example harry-ron romance, or Fate/Stay fanfic for the spoilers...
  * *Reader tags.* So instead of the author having full control over (forgetting to) tag their story, delegate a bit of that to the community. Mark author tags as special/immutable, but allow the readers to add stuff. There would need to be some kind of restriction or control on this, so maybe...
  * Reputation a la Stack Overflow. Certainly not for ranking authors (let reviews/comments/favs/stats/etc do that) but for allowing good readers/reviewers/community members to have access to some tag editing and moderation tools.

  **As a writer**

  * Simple formatting, but more than FF.net and also more than Medium. I don't want the full range of formatting options, but bold, italic, underline, alignment, section separators, whitespace control (for poetry, mostly) as a minimum.
  * **Stable** formatting. FF.net had the reputation of changing formatting rules without notice at some point, making many stories' formatting implode. Medium mangles some formatting, most often I observe it has trouble with whitespace.
  * If writing my stories directly on the site, I like to have a "distraction-free" environment, maybe behind a button/setting, and optionally a "Hemingway" mode that doesn't allow editing until you finish writing a draft.
  * Also related to writing directly on the site, a good autosave that never lets me lose anything. See Medium, for example: if my computer is hit by lightning, I expect to at most loose a paragraph.
  * Still related to that, an offline mode, for obvious reasons.
  * As expressed by others, an easy way to add metadata (author notes) to a story, and differentiate between displaying some "before chapter" and "after chapter" if required.
  * Links within metadata.
  * Syndication to other sites, as audiences won't move so easily... so being able to publish once on the service, and have it syndicated to FF.net/AO3/Fictionaut (for short pieces)/etc.
  * Easy licensing options (Creative Commons, Public Domain, All Right Reserved, others?)
  * Import from other sites.
  * Ability to host and sell access to *paid* stories.
  * A queue to post things at certain times without manual intervention.

  **Generally**

  * Competent moderators.
  * Maybe separate comment and review systems? I'd love a site where there is a culture of critical and/or constructive *reviews*, but also "I like it"-style *comments* and questions.
  * QA sections for each story, at the author's opt-in, to provide an out-of-story but well-organised way to answer reader questions.
  * QA events, AMA-style but maybe more organised, with a group of authors, or authors in a genre, or inversely, with select readers/reviewers/etc.
  * Collaborative writing is Hard™ but if someone can figure out a good UX for it, that would be neat.
  * Open source.
  * Ability to donate to authors, possibly through a partnership or integration with Patreon or Gratipay.
  ```

- u/PeridexisErrant:
  ```
  There's a lot of good suggestions about interface and features for both readers and authors, so I'll add something different.

  With the TPP coming up and copyright generally being an enormous pain, I'd love to see some clarity around sharing rules.  Specifically, instead of the usual garbage terms of service - just make works pick a creative commons license.

  CC-BY-NC-ND is actually a better deal than most hosts offer, to start with!  Others encourage more community interaction, promote openness, and there's the advantage that unlike normal terms people actually understand what these options mean.
  ```

- u/passcod:
  ```
  Vanity URLs / custom domains could also be interesting. Having all one's stories under fiction.mydomain.com, for example, while still having a full platform behind it, would be grand.
  ```

---

