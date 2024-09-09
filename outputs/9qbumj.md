## URGENT: Be Advised; FFN Profiles compromised and may carry Javascript Exploit.

### Post:

[Link to content](https://forums.spacebattles.com/threads/urgent-be-advised-ffn-profiles-compromised-and-may-carry-javascript-exploit.692300/)

### Comments:

- u/eaglejarl:
  ```
  For some time now I've been recommending using any site other than FFN for publishing.  My personal recommendation is [SufficientVelocity.com](https://SufficientVelocity.com), although check the TOS if you're going to be posting mature content.

  IMO, FFN has the following pros:

  * Large readership
  * Really detailed and interesting stats about your readership

  It has the following cons:

  * Non-responsive admins
  * It will mangle your text, including:
     * No links allowed.  
     * No use of the word 'Patreon' allowed
     * No use of the word 'Kickstarter' allowed (I might be wrong about this one)
  * You cannot copy/paste from the page, because they have javascript that disables that
  * If you disable javascript so that you can copy/paste, you will find that everything is centered
  * It is not possible to reply to a review inline, only via PM.  This means that: 
     * You cannot develop a mutually-interacting community among your readership\[1\] 
     * Future readers cannot see your response to reviews
     * You cannot reply to guest reviews
  * Screenplay format is a violation of TOS, which is annoying because screeplay is an excellent format for parody
  * You cannot edit reviews that you leave
  * You cannot review a given chapter more than once, so if you submit a review and then want to add something, or if you re-read something a year later...too bad!
  * The interface for uploading/updating chapters is absolute shite.
  * When you update a chapter it does not actually show the changes for an indeterminate period of time.

  \[1\] FFN actually does have a 'community' feature, but it requires taking a positive action to create, then readers have to actively join it, and there's no direct access from the story to the community.
  ```

  - u/SimoneNonvelodico:
    ```
    While FFN has limitations and this exploit is bad news, I really don't think a forum like Sufficient Velocity can come close to even approximating the same functionality. The forum format is horrible for writing and reading fanfiction, it comes with a lot of distractions, fragments the content interspersing it with the comments/answers and is hard to parse out. FFN has a smartphone app and there's a complimentary site that compiles EPUB and MOBI files out of a given fanfiction, that's a lot of convenience right there. Archive Of Our Own if anything would be the only alternative that's really even in the same ballpark.
    ```

    - u/eaglejarl:
      ```
      Press the "Reader mode" button on SV and it will show you only the story posts without the discussion.

      Reading SV in your phone browser works fine -- it's quite mobile friendly. I see zero value add from a specialized app and noticeable downside.

      Parsing SV is pretty trivial; I've done it.

      If you want offline-readable versions, your browser comes with a "download" button, so the fact that it's not epub or mobi carries no water with me.

      Maybe you have some specialized workflow that isn't met, but I stand by my statement: aside from the question of stats, SV is strictly superior to FFN.
      ```

      - u/Croktopus:
        ```
        ive really been enjoying ao3, from the perspective of a casual reader that just wants shit to be simple and easy
        ```

        - u/eaglejarl:
          ```
          AO3 is a great site, and I recommend it. It's a fine publishing platform, probably my #2 choice behind SV.

          Actually, now that I think about it, I should look into Royal Road. They have one killer feature for an author, which is that they make it easy to monetize by including Patreon links directly into the chapters for you. I'm not sure about the rest of their functionality, though.
          ```

  - u/ToaKraka:
    ```
    > You cannot copy/paste from the page, because they have javascript that disables that

    It's CSS, not Javascript. You can easily override it by adding `div.nocopy{user-select:text!important;}` to your custom CSS in [Stylus](https://chrome.google.com/webstore/detail/stylus/clngdbkpkpeebahjckkjfobafhncgmne). Even without custom CSS, there's nothing stopping you from simply copying text directly from the code of the page (in Chrome, press Ctrl-U).
    ```

- u/Sailor_Vulcan:
  ```
  could someone please explain why it isn't safe to look at the profiles? I didn't quite understand that part.
  ```

  - u/SimoneNonvelodico:
    ```
    Basically, someone found a way to inject a virus of sorts in the profile bios. The virus is JavaScript, aka it runs in your browser when you open the page, and it instantly adds itself to *your* bio (plus does a few other things). Now the problem is, there's a message inside the virus that suggests it's just someone trying to show off this exploit as a way to tell the admins to fix it. Which if true is the best scenario, but it STILL means that they need to fix it, and apparently FictionPress admins are just sleeping on this. I can confirm their Twitter has said nothing yet.
    ```

    - u/CouteauBleu:
      ```
      Well, worst case scenario, the attacker can affect your fanfiction.net data and pretty much nothing else. (eg they can't access your non-ffnet passwords or bank credentials or whatever)

      So I wouldn't completely freak out. But yeah, FictionPress sucks.
      ```

      - u/SimoneNonvelodico:
        ```
        Well, a number of people may recycle their password, for example. Hopefully not on their bank accounts, for which you should definitely use a unique one (and also any good bank should give you additional layers of security), but you never know.
        ```

        - u/nicholaslaux:
          ```
          Just to clarify - access to javascript and the ability to perform actions on your behalf on FFN indicate that it's highly unlikely that the attacker would be able to gain access to your password, since that isn't actually used/accessed by JS during non-authentication tasks.

          Worst-case scenario (in terms of potential damage) would involve the attacker sending a copy of your session cookie to a remote drop, in order to imitate anyone they want. However, to foil this, even if you've been affected, all you would need to do is... log out, and log back in again, without viewing the virus a second time.

          For authors, there's a higher risk of malicious code automagically deleting all of your stories or something similar, but otherwise, it's best not to overstate the possible risks without cause, so that when larger incidents do happen, people don't underreact to them.
          ```

          - u/SimoneNonvelodico:
            ```
            Yeah, I couldn't figure out a specific way to steal the *password* unless it somehow tricks you into re-inputting it and keylogs it. But you never know, and there may be actions in your profile which require you to confirm your password.
            ```

- u/oliwhail:
  ```
  u/Velorien , u/eaglejarl
  - just in case, might be good to check?
  ```

  - u/Ardvarkeating101:
    ```
    and /u/boomvroomshroom
    ```

    - u/None:
      ```
      [deleted]
      ```

      - u/Ardvarkeating101:
        ```
        <3 baby
        ```

- u/trambelus:
  ```
  I'll copy what I said on the SB thread.

  If you think you might have been affected by this exploit, **go to your account settings immediately** and look at your backup email addresses. If there's anything there you don't recognize, get rid of it right now, and you should be fine. If your own email address is missing, re-add it. It might also be a good idea to change your password, just to be safe.
  ```

- u/GhostWriter52025:
  ```
  Could a mod please sticky this or something? Seems rather important for this community.
  ```

  - u/alexanderwales:
    ```
    Done. I really thought that the turn-around time for this would be a lot faster, but apparently not.
    ```

    - u/Ardvarkeating101:
      ```
      First time dealing with FF.net issues?
      ```

---

