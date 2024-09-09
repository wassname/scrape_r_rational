## [D][Rant] If you're engaging in mad science, have a disaster recovery plan

### Post:

I watched two summer blockbusters today. Both had, as their climax, the destruction of information held by a large company with lots of resources. *In neither case should this have happened.*

I understand the storytelling impulse that leads writers to make a plot like this. It allows you for a nice dramatic moment when the hero is reaching out towards the detonator with a single bloody hand. It makes the heroic sacrifice a lot more clean. It's efficient; it's a single goal for the climax.

*However ...*

Pretty much every large company in the world keeps off-site backups. This is not only common sense, it's industry standard. If a significant fraction of the value of your company is held in the form of information, one of your top priorities is in protecting that information. Leave aside superheroes and lone-wolf terrorists for a moment, there are all sorts of mundane reasons to keep back-ups. In a lot of cases, it's even a legal requirement.

In Hollywood screenwriting, acknowledging this fact is inconvenient, so they don't do it. In rational fiction, please remember that the enemy is smart, and you don't have the luxury of pretending that all data is housed at a single point of failure (unless there's a really, really good reason). This goes triple if the enemy knows that someone is actively trying to destroy the data.

This is part of the terrible ["No Plans, No Prototype, No Backup" trope](http://tvtropes.org/pmwiki/pmwiki.php/Main/NoPlansNoPrototypeNoBackup).

(The offending movies are both recent, and I can't name them without spoiling the climax; if you don't care about that, they were [](#s "Terminator: Genisys") and [](#s "Ant-Man"). I sort of consider spoiling blockbusters to be pointless considering how formulaic they tend to be.)

### Comments:

- u/mhd-hbd:
  ```
  It's mad *engineering,* people.

  Mad *science* is experimental setups which when described sound like a mix between the highly unethical practices found at a concentration camp, and [noodle implements](http://www.tvtropes.com/pmwiki/pmwiki.php/Main/NoodleImplements).

  (Warning, TV Tropes link.)
  ```

  - u/ancientcampus:
    ```
    I've heard this said a bunch, and it's indeed a great line. That said, lots of mad scientists throw around phrases like "Using my theory of Kopelson Intrinsity I'm gonna blow up the sun with my death-ray," especially before it was too cliche. So, they were mad scientists at *some* point at least, before they became mad engineers. The true nature of Dark Science: failing to publish!
    ```

    - u/mhd-hbd:
      ```
      > "Nick told me everything. He was too polite to suggest that what you're trying to do is insane. He doesn't know enough about magic to pass judgement. I do. What you're trying to do is insane. Do you want to know what you're doing wrong?"

      > "Um--"

      >"You're not writing anything down."

      > "Um--"

      > "This is not a mystical adventure. You are not the protagonist. You're seeing and doing things which are having profound emotional effects on you. You're being irrational. You're not thinking things through, you're not working things out. You're going on mental arithmetic instead of paper arithmetic and you're going on gut instinct instead of worked, peer-reviewed results. This is not good science."

      > "But I'm right."

      > "I don't care how right you think you are. I don't even care how right I think you are! I want to see a LaTeX-typeset paper from you. You need to show your working, because there are demons at work in your working."

      — *Ra*, by Sam Hughes
      ```

      - u/None:
        ```
        That writer went to grad school.  Thank fucking God someone did.
        ```

      - u/Nevereatcars:
        ```
        God damn you, I don't have TIME to read Ra again tonight! It's three am ALREADY!
        ```

- u/STL:
  ```
  TVTropes lists the best counterexample, in Contact: "First rule of government spending: why build one, when you can build two, at *twice the price*? Only, this one can be kept *secret*."

  (After some quick searching, this line appears to be unique to the movie; if it's in the book I can't find it. Well done, Hollywood.)
  ```

- u/puesyomero:
  ```
  ant man? when i saw it by the end of the movie i was thinking "why did the guy didn't send the hornet suit miniaturized through fedex to Hydra three days before the party?" or keep a multi terabyte drive with the plans on him allways. fun movie though.  
  edit: now that i think of it did the pym particle produce energy? i mean the hornet suit had HUD, jetpack, enhanced strength,and multi kilowatt lasers  with no arc reactor in sight! should iron man be concerned?
  ```

  - u/alexanderwales:
    ```
    The villain's entire motivation seemed to be that he was insane. They explain this in the movie as something something particles, which is an enormous cop out. It makes for an extraordinarily weak villain, even in comparison with the weak villains of other superhero movies, but it was still fun enough in spite of that.
    ```

  - u/Pluvialis:
    ```
    > should iron man be concerned?

    I came away with the same impression after watching Captain America 2. Apparently Tony Stark isn't the only one who gets stupidly advanced tech. Pretty sure Iron Man suits or their equivalent could be manufactured by any number of people and groups in the Marvel universe, if it was consistent.
    ```

- u/None:
  ```
  You mean some people don't put their madness on Github or arxiv?
  ```

  - u/PeridexisErrant:
    ```
    No, Github is a single point of failure.  Just use `git` over ssh; it's an entirely distributed protocol already!
    ```

    - u/bbrazil:
      ```
      Oh no, they're automatically distributing their code all around the world. Wait, I know this. It's git.

      `git push --force`

      Well that was easy.
      ```

      - u/Uncaffeinated:
        ```
        That only handles the repos that you have write access to. Peoples local copies will still be intact unless they try to pull.
        ```

- u/Geminii27:
  ```
  The recent Fantastic Four movie is a bit like this as well. At the end, everything blows up, but the Stock Evil Military Guys have had a small army working on building the McGuffin for five years or so - and yet somehow they're unable to make it work unless Reed Richards is standing around within fifty feet of it.

  *Yes*, he and Doom were the main scientist and instigator of the project respectively, and neither would be around afterwards, but does this mean that a paperwork-obsessed organization like the US military would somehow not be able to get to within epsilon of where they were previously just from backups, and then throw a lot of really smart people at the problem?
  ```

- u/derefr:
  ```
  This strikes me even more strongly concerning any sort of AI villain. You mean the first thing you did **wasn't** to make yourself into a fault-tolerant self-healing distributed system? Not necessarily even by "taking over the Internet" with a botnet or anything (that's one of those things that gets you noticed), but just, like, renting some AWS instances here and Hetzner boxes there and so forth.
  ```

- u/Magodo:
  ```
  I've set up a really simple rule to avoid such  movies in general. If it was heavily advertised and has a PG-13 rating, it will more likely than not suck.
  ```

  - u/None:
    ```
    It's hollywood. I don't expect rational storytelling. They will do whatever they want without regard to reality or internal consistency.
    ```

---

