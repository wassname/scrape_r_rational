## [RT, HSF] Programmer at Large Chapter 4: Are you serious?

### Post:

[Link to content](http://www.drmaciver.com/2017/01/programmer-at-large-are-you-serious/)

### Comments:

- u/MaddoScientisto:
  ```
  It's millennias into the future and humanity still hasn't solved death? What have they been doing?
  ```

  - u/DRMacIver:
    ```
    > It's millennias into the future and humanity still hasn't solved death? 

    The basic premise of this setting (and the Vernor Vinge novels it was loosely based on) is that we're much closer to the point where what's possible plateaus than one might optimistically expect. No FTL. AI is limited or impossible. No magic nanotech. No neural transfers. 

    Depending on how you count things (basically, whether you count time spent asleep or not. The crew don't), the average crew lifespan is anywhere between about 200 and about 1000 years. They push that up gradually over time, but towards the end of that they're hitting some fairly major limitations on human neural architecture which are hard to resolve without causing major damage, and the body has been repaired so many times that it starts to become extremely fragile.

    > What have they been doing?

    Periodically self-destructing at a global level, or sleeping through most of it amidst the stars.
    ```

- u/traverseda:
  ```
  https://github.com/akashic-os/akashic-core for what amount to my doodles for an "os" with some interesting properties. Our discussion on how logging works inspired me to work a bit more on it.

  Written in python.

  It uses a json-store called rethinkdb, which has one really interesting property, that you can subscribe to a query, and get an object when it changes, or any document in it changes. That makes a lot of things a lot easier, like remote-procedure calls, log monitoring, etc.

  There's a lot of work that needs to be done before it's usable for anything. Right now the only thing that really works is "rq", an editor that converts the data into a more pleasant format (yaml). Right now it only support vim for the actual editor component.

  I've been working on helper classes. Like akashic.db.ExitHandler which is a class that will add a heartbeat to every object you put in it, and delete any object you put it it from the database on clean-ish (not -9) exit.

  My next big project is a tagged file system layer using fuse, and patching pythons logging to support arbitrary data so it can use more complicated errors.

  After that is an RPC system, which I can use as part of an init system, which I can use to run things like dead-object cleanup daemons. Probably extending python-hug.

  After that is daemons, like something that generates thumbnails for any file that matches a certain query.
  ```

  - u/Gurkenglas:
    ```
    Did you mean to post this elsewhere?
    ```

    - u/traverseda:
      ```
      No. It's marginally relevant to a conversation we had had about how software works in the trade fleet.
      ```

- u/rhaps0dy4:
  ```
  I like the syllable IDs ! jad-nic, vic-taf, nod-sid... Are you inspired by Urbit in this, or you both draw from another source, or is it independent?

  Also, is nod-sid 1 not the same as Tulela? Did Tulela adopt the nod-sid ID when they were born?
  ```

  - u/DRMacIver:
    ```
    > I like the syllable IDs ! jad-nic, vic-taf, nod-sid... Are you inspired by Urbit in this, or you both draw from another source, or is it independent?

    I'm only aware of Urbit in the vaguest sense, so it's not inspired by it but there might be a common source. The syllables are byte representations from a UUID, with crew-members chosen to have the two least significant bytes from their UUID unique amongst living crew on the same ship. The byte->syllable mapping [comes from here](http://hewo.xedoloh.com/2015/04/base-256/) 

    > Also, is nod-sid 1 not the same as Tulela? Did Tulela adopt the nod-sid ID when they were born?

    Tulela is a use name. It's globally unique amongst living crew, but when its user either dies or manually relinquishes it it comes up for grabs by other users.

    So in this case although Arthur is referring to nod-sid 1 as "Tulela" this is technically incorrect. Tulela is the living crew member who currently claims that use name. nod-sid 1 simply happened to be identified as Tulela at the point at which the message was left.

    This is a fairly common source of confusion with historical records.

    Similarly the nod-sid ID becomes available when its holder dies (two bytes isn't enough for uniqueness across history!), and the dead holder gets a digit after their ID to uniquely identify them (this can technically be used for living crew, but generally you don't and if you don't use a numeral it's assumed you're referring to a live crew).

    If you're not bored yet [there are more details on how all of this works in the world building notes](https://github.com/DRMacIver/programmer-at-large-notes/blob/master/names.md).
    ```

- u/bassicallyboss:
  ```
  Why does the computer keep recommending socialization for Arthur, when it's clearly unpleasant for them?  I imagine that some level of socialization is necessary for the proper functioning of a crew, and that for most members, the preferred level of socialization exceeds this minimum.  Is the computer insisting on (and Arthur being frustrated by) the minimum level, or are its recommendations based on what an average crew member would enjoy?
  ```

  - u/DRMacIver:
    ```
    The ship's software is not a hedonic utilitarian and it's only really interested in Arthur's happiness to a certain base level (above the bare minimum needed for them to be productively functioning as a member of the crew, but not a *lot* above that).

    The goal of the socialisation program is primarily to keep the crew society well integrated and stable, not because the ship thinks people enjoy it. Normally the suggestions are less "you should socialise more" and more "it would be useful for you to socialise outside your current ingroup".

    Fortunately most of the crew *do* enjoy it. Arthur is just unlucky in that they have a social anxiety disorder and live in a hypersocial society, so they tend to be constantly bumping into the danger zone where the ship thinks they might be failing to integrate properly and gets quite pushy.
    ```

    - u/bassicallyboss:
      ```
      Okay.  That's sort of what I was thinking.  I'm assuming that genetic engineering is not available, or Arthur probably wouldn't have social anxiety in the first place.  It seems like there might be some optimization left to perform here--Arthur seems to freak out when social interaction is required, and I can't imagine that's good for either their job performance or crew stability and integration.

      I enjoy socializing (though I do find it tiring to meet and be friendly with new people), and I don't really have a good model of the social needs of socially anxious people.  Does Arthur actually benefit much from socializing, despite their distaste for it?  Or is this mostly for the rest of the crew's benefit, so they can get to know and trust their fellow crewmember?
      ```

      - u/DRMacIver:
        ```
        > I'm assuming that genetic engineering is not available, or Arthur probably wouldn't have social anxiety in the first place.

        Genetic engineering and screening are available but tricky when it comes to behaviour - too many useful things are too close to too many problem things. Cases like Arthur are rare but not absurdly so.

        (Significant modification of the human mind may be possible in reality, but in this setting 21st century technology is posited to be much closer to the plateau of what's possible than one might hope)

        > It seems like there might be some optimization left to perform here--Arthur seems to freak out when social interaction is required, 

        Arthur doesn't usually freak out when socialisation is required, they freak out when they perceive socialisation to be going wrong (and have an extremely exaggerated sense of when that is). Normally they just find it slightly overwhelming. Unfortunately they anticipate both these things, so are rather scared of it and try to avoid it where possible.

        > and I can't imagine that's good for either their job performance or crew stability and integration.

        There's a reason Arthur has an atypically solitary job.

        > Does Arthur actually benefit much from socializing, despite their distaste for it?

        Arthur (and a lot of people with social anxiety in general) actually quite likes socialising as long as it's going well, and will feel sad like most people if they don't get enough of it. It's just that they also find it scary and difficult, and would prefer to stick to more familiar people and situations that they're better able to navigate.

        Sometimes when they avoid it it's genuinely because they can't cope with it right now, sometimes they're just letting fear overcome them. In that sense having the ship giving them a constant nudge towards socialisation is actually quite helpful for them, even if they hate it, but it can also go wrong and the ship is not particularly able to distinguish the difference.

        > Or is this mostly for the rest of the crew's benefit, so they can get to know and trust their fellow crewmember?

        It's not so much about knowing and trusting any individual crewmember (though that is part of it) as creating an extremely tightly knit society that is very resistant to factionalisation and other forms of breakdown. The ship's social software pays a lot of attention to the shape of the friendship network and tries to make sure that it's well mixed and everyone is a fairly low social distance from everyone else.
        ```

---

