## Would any of you be interested in a website -> e-book converter?

### Post:

I dislike reading in a web browser on my phone and prefer reading on a kindle While searching online I could not find a good service to create ebooks from a website such as fanfiction.net. So i wrote myself a small script that scrapes the websites and outputs a format which I can read on my kindle.

Would any of you be interested in a online service with similar functionality?

**edit: Thanks for your extensive input. I got a clearer vision for the service now and will write up a design document or similar.**

To give you a broad overview:

- Backend FanFicFare + leech + custom scripts for maximum compatability with sites
- Frontend will be mobile-first (with PWA support)
- Main feature will be to just convert an URL to an ebook
- Additional Feature to "subscribe" to updates which get automatically pushed to your device of choice (e.g. kindle) -- open question: how to update ebooks on kindle?
- Additional Feature to add support for custom sites -> User tries to convert a site which is not supported -> Provide a wizard with which the user can build a converter

I have a lot of open questions still such as:

- Name for the service?
- How to get input on development? Should I post a "monthly development update" thread on reddit or similar?
- How to pay for server costs? Patreon?

I got to go now, so sorry if my edit seems rushed. Thanks again for the discussions and input!

### Comments:

- u/Asviloka:
  ```
  Calibre + fanficfare is what I generally use. It works for a wide variety of sites, including ffnet and ao3. Very convenient.
  ```

  - u/wederer42:
    ```
    I just took a closer look at fanficfare. It would probably be a good base for the website.
    ```

- u/None:
  ```
  [deleted]
  ```

  - u/CaramilkThief:
    ```
    Do your scripts work with wordpress? That's the only website that I can't find a scraper for.
    ```

- u/derefr:
  ```
  Other than FanFicFare, another such already-existing program is [leech](https://github.com/kemayo/leech). It seems designed more specifically for the kinds of long-form independent web-novels that get linked here, as it focuses more on making it quick and easy to configure their generic scraper plugins for custom one-off sites (the kind of "novel as WordPress blog on its own domain" works we see a lot of here.)

  This contrasts with FanFicFare's focus on explicit preprogrammed support for fiction-hosting websites, blogging engines and forums, at the expense of requiring you to sit down and write a plugin from scratch if you want it to scrape anything more bespoke.

  Amusingly, in leech's example on how to configure a job for its "custom" plugin, the developer has chosen to use *Practical Guide to Evil* as the scrape target. :)
  ```

  - u/ConnorF42:
    ```
    I’d second leech. I use it quite a bit, and it cleans up web text nicely to more traditional book style (indented paragraphs instead of line breaks for example.) 

    It isn’t very hard to create new entries for one off sites (Wordpress, or really anything that has a discrete table of contents page). I haven’t had the need to create a new web service (RoyalRoad, ao3, etc) since it already has the ones I need, but I figure it wouldn’t be that bad.

    Updating existing ebooks is pretty fast, but does take a few minutes (I keep my kindle offline and transfer with Calibre, maybe faster way)
    ```

- u/ahasuerus_isfdb:
  ```
  Is the proposed functionality similar to [FanFicFares](https://www.mobileread.com/forums/showthread.php?p=3084025&postcount=2)'s (previously known as FanFictionDownLoader)? Or is it more like [WebToEpub](https://chrome.google.com/webstore/detail/webtoepub/akiljllkbielkidmammnifcnibaigelm?hl=en)?
  ```

  - u/wederer42:
    ```
    Similar to WebToEpub, but with support for custom sites. I would give the user a way to parse e.g. forums such as sufficientvelocity.com or wordpress sites.
    ```

    - u/rdalex:
      ```
      In this case, it would be more useful to work on adding to FanFicFare's functionality, rather than building a competing product.

      FFF already solved this problem for basically all major fiction repositories and a long list of minor ones, and as a bonus integrates well into Calibre, arguably the best ebook management tool at this time. There's no point in reinventing a wheel that's been polished for more than ten years. (Except for the joy of programming it yourself, in which case I understand it completely, go for it!)

      If it's a webservice you need, FFF also supports that. The dev [did maintain one](https://github.com/JimmXinu/FanFicFare/wiki#web-service-version) for a while before Google (his host at the time) made it too expensive to run.

      What FFF lacks is [adapters for custom sites](https://github.com/JimmXinu/FanFicFare/wiki/FAQs#why-doesnt-fanficfare-support-livejournal-and-many-other-popular-fan-fiction-websites) that don't integrate semantic clues or metadata in their pages, which obviously makes parsing them a scripting nightmare. If you have the will and skills to do that kind of work and resolve that difficulty, please consider contributing code to FFF.
      ```

    - u/Areign:
      ```
      does WebToEpub not do that in the advanced options? I've frequently used it for non supported sites by identifying the CSS elements containing text...etc

      Am I missing the core of your proposal or is it supposed to be more user friendly or something along those lines?
      ```

    - u/callmesalticidae:
      ```
      Yeah, that'd be super useful.
      ```

- u/thomas_m_k:
  ```
  I use http://ficsave.xyz/ but it's a bit finicky, so I would be very glad to have something more robust available!
  ```

- u/xland44:
  ```
  The problem with scripts and plugins is that you need a PC for that still. Would it be possible to create an app for this? If it indeed has the versatality of WebToEpub and works for multiple sites (e.g wordpress  royalroad, spacebattles, etc.) I wouldn't mind paying for such an app, and probably others would be willing too.

  The reason? Even if you use WebToEpub, you're going to need to use that from your PC, and then use *another* app (Send to Kindle) to actually be able to read it. As a person who reads only from my phone and doesnt have access to a PC, an app that A) can scrape serials into an epub and B) add any downloaded epubs to your Kindle library would be a great lifesaver and something I'd gladly pay for.

  That's my two cents. WebToEpub stopped being useful when I no longer had access to a PC ;-;
  ```

- u/uwu-bob:
  ```
  This already exists. There are FF.net downloaders and browser extensions, and I've used bloxp for wordpress sites.

  What I'd pay money for is a service that keeps an up-to-date ebook of a web serial synced to my kindle, so I don't have to start up a download/conversion manually every time there's an update.
  ```

- u/Geminii27:
  ```
  While I probably wouldn't use such a thing myself, there's always a demand for format converters. And while (as people mentioned) there are existing things like FFF, it never hurts to have alternate channels in case something unfortunate (service outage, legal trouble, site DDOS etc) happens to one of them.

  Plus, I guess, you could always add additional functionality like the creation of ebooks with customizable covers, title pages, and so on. Make those kinds of services cheap enough and fans of various works may well be prepared to drop a couple of dollars to create a fancied-up version of their favorites.
  ```

- u/Toastybob42:
  ```
  I use the browser extensions Web2epub (for works) and dotepub (for individual chapters).
  ```

- u/waylandertheslayer:
  ```
  If you start a github project and advertise it on here, I'd be happy to contribute.
  ```

- u/ahasuerus_isfdb:
  ```
  A bit of background info about FFF. To quote a recent post by the developer:

  > ... the **mobi output**.  Honestly, that code is ancient and
  it is reverse engineered from Amazon's proprietary binary format.  It
  predates my involvement in the project and I don't understand that code.

  > I recommend downloading to epub and using Calibre to convert to mobi if
  you really need mobi (I use azw3 for Kindle myself).  You'll also get
  better mobi output with chapter marks.

  > That also gives you the advantage of being able to update and add new
  chapters without downloading every chapter every time.
  ```

---

