## [Meta] WARNING, the Practical guide to evil site has been infected with malware.

### Post:

There's a link regarding tragic news about the site operator instead of the story text, according the the PGTE discord, this link will infect your computer with malware.

EDIT: It now appears that EE has regained control and has fixed the issue. The only way of getting malware was through clicking a link and that link is now gone, and the chapters have been restored. If you click on strange links that start auto-downloading files for you, do not open them. 

PS, not sure if I should delete this now or if mods want to put a "solved" mark or something on it.

### Comments:

- u/boomfarmer:
  ```
  Wait, isn't PGTE a WordPress.com site? This sounds like either a hack of the author's account or some form of XSS attack in a plugin on the site.
  ```

  - u/lolbifrons:
    ```
    Wordpress is notoriously vulnerable to all kinds of shit.  One of our units in my pentesting class was just about hacking wordpress.
    ```

- u/Robert_Barlow:
  ```
  I don't know if this is a well known piece of malware, but googling the phrase "tragic news about the site operator" gives links to [this website](http://www.beststoryinevertold.com/) which seems to have been infected by the same thing - same link, same text, same warnings apply. Nothing else turns up with that exact phrase, and I'm not familiar enough with Wordpress history in order to know if something similar has happened to other blogs in the past.
  ```

- u/xartab:
  ```
  I swear for a moment there I thought you meant a memetic hazard. You can never tell on this subreddit.
  ```

  - u/Frommerman:
    ```
    Viruses are memetic hazards for computers.
    ```

    - u/xartab:
      ```
      Every copy you make becomes an instance of the thing. Like the Angels.
      ```

- u/TaltosDreamer:
  ```
  Sadness 😭
  I hope they are able to recover safely.

  Do we know which virus for innoculation purposes?
  ```

  - u/red_adair:
    ```
    Weird thing is, Virustotal doesn't think it's a virus (yet): https://www.virustotal.com/gui/url/b5d50086b6bef904b09621d75af2990e04db741059c3e71f4705629b2f0cdb5f/detection
    ```

    - u/red_adair:
      ```
      Update: Kaspersky thinks it's a virus now.
      ```

    - u/TaltosDreamer:
      ```
      I heard the french just took down an 850k botnet. I wonder if it's connected to them. It makes sense the perpetrators would create something new and branch out.
      ```

      - u/red_adair:
        ```
        When you say things like "I heard ....", especially in tech circles, **link to your sources**.
        ```

        - u/Slinkinator:
          ```
          Well, it's been on the BBC for more than 12 hours, so it's not like, niche news

          I mean, if anything I thought it was a bit inane to refer to it as of it wasn't heavily reported international news.
          ```

          - u/red_adair:
            ```
            Anecdotally: it didn't pierce my filter bubble, because I mostly read US news, and it looks like the story didn't hit the English-speaking press until after I had already checked the news for the day.

            Speaking more generally: If you link to the news, you both help pierce other people's filter bubbles, provide a resource where people can go to learn more, and you refresh your own knowledge of the news.

            Anyways, here's a detail-full news article, for people who have yet to read about it: https://thehackernews.com/2019/08/retadup-botnet-malware.html

            I don't think this malicious .doc file is related to the RETADUP network, because:
            1. VirusTotal [initially reported](https://www.reddit.com/r/rational/comments/cwu0eo/meta_warning_the_practical_guide_to_evil_site_has/eyfc7qa/) that no antivirus detected the .doc file as malicious, which would not be the case for a known virus
            2. The server hosting the .doc is located in .ru netspace, not in France or the USA, which is the case with RETADUP's known command-and-control infrastructure.

            But those are weak assertions.
            ```

        - u/TaltosDreamer:
          ```
          Tech circles? Interesting way to refer to a discussion group about fiction.
          ```

      - u/Lugnut1206:
        ```
        i'm gonna vote firm coincidence on that, unless "the french" has some deeper, PGTE-specific meaning i'm unaware of
        ```

        - u/Academic_Jellyfish:
          ```
          EE is from France. Still a decent chance it's unrelated though.
          ```

          - u/CouteauBleu:
            ```
            I thought he was from Quebec?
            ```

      - u/red_adair:
        ```
        I care less about attribution and more about:

        0. taking down the malware server
        1. securing affected accounts
        2. restoring compromised sites

        It doesn't look like any of the attacks from today's WordFence compromise list https://www.wordfence.com/blog/2019/08/malicious-wordpress-redirect-campaign-attacking-several-plugins/ so I'm guessing someone guessed EE's password.

        Always use unique per-site passwords, and enable 2FA when possible.
        ```

        - u/TaltosDreamer:
          ```
          I would hope figuring out the particular virus would be useful since we could hunt down specific cures.

          That applies to #1 and #3 on your list
          ```

- u/None:
  ```
  [deleted]
  ```

  - u/LordSwedish:
    ```
    The only malware comes from downloading the file from the link that has replaced the text and then presumably opening it. I don't know what browser or phone you're using or if you clicked the link so I can't say anything else.
    ```

  - u/Academic_Jellyfish:
    ```
    There's a download link on the table of contents and most recent few chapters. Unless you're an idiot and download the file and then open it, you should be fine. And from what I know, most viruses wouldn't work on mobile, though I'm hardly an expert on it.
    ```

- u/ShotoGun:
  ```
  Does ad block protect against the malware?
  ```

  - u/LordSwedish:
    ```
    I saw someone mention that it did, but mine doesn't. Unless you click the link that has replaced the text, you can't get any malware.
    ```

  - u/MilesSand:
    ```
    Unlikely. The only time adblock protects from malware is if the malware is being served through ad networks. As far as I remember EE never put any ad plugins on the site.
    ```

---

