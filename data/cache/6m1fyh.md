## [D] Saturday Munchkinry Thread

### Post:

Welcome to the Saturday Munchkinry and Problem Solving Thread! This thread is designed to be a place for us to abuse fictional powers and to solve fictional puzzles. Feel free to bounce ideas off each other and to let out your inner evil mastermind! 

Guidelines:

* Ideally any power to be munchkined should have *consistent* and *clearly defined* rules. It may be original or may be from an already realised story.
* The power to be munchkined can not be something "broken" like omniscience or absolute control over every living human.
* Reverse Munchkin scenarios: we find ways to beat someone or something  *powerful*.
* We solve problems posed by other users. Use all your intelligence and creativity, and expect other users to do the same.

Note: All top level comments must be problems to solve and/or powers to munchkin/reverse munchkin.

Good Luck and Have Fun!


### Comments:

- u/erenthia:
  ```
  So, I think I've found the *one* Shrink Item abuse that hasn't been explored before.  It should be possible to shrink down a 5-foot cube of air into a clothlike form that is effectively under 4096 atmospheres of pressure.  

  I've been trying to do the math, but not being an engineer, I haven't been able to determine if a D&D style world would be able to produce a system capable of utilizing that much pressure.  

  So would pneumatic cannons be feasible?  Would you have to make them out of adamantine?  You could probably bleed off some of that pressure so your materials could handle it, but how much would you have left.  

  Lastly, if you created magic items that produced tiny balls of shrunken air at various equivalent pressures, what technologies could you create using this as a power source?
  ```

  - u/Daneels_Soul:
    ```
    Of course shrink item cannot actually work like this. If it did, the spell would be called "fireball" instead, because that would be the observable effect.

    I mean, if you are trying to create an explosion by magically compressing something, why restrict yourself to gasses? Water is usually modeled as incompressible because the energy required to compress it even a little bit is well beyond the scales that typically show up.

    Going to extremes, Osmium has a Young's modulus of about 500GPa, which if I understand correctly, means that if you shrink it to substantially less than it's usual size, it should be at about 500GPa of pressure (of course it becomes non-linear at some point, so this is a crappy approximation). This means that the total energy of decompression is about
    500 GPa*2 ft^3 ~ 2.8*10^10 J, or about 5 tons of TNT, which I guess is a pretty large bomb.

    But the point is that if shrink item actually worked like this, you would get a similar result from shrinking basically *any* solid item.
    ```

  - u/Norseman2:
    ```
    The rules do not specify how rapidly the item is shrunk, or how rapidly it returns to normal size. At most, I could see a DM justifying a 3 second shrink/expansion time. That gives you your standard action to cast the spell, shrink something, and then pick it up with a move action. Obviously, this still means that any shrunken object placed inside of a sealed container will create a bomb, but at least it's not a bomb of unspecified and potentially infinite magnitude.

    Assume that the volume and mass increases linearly over 3 seconds, so you're adding about 41 cubic feet of gas at standard temperature and pressure per second. You should now be able to work out your options in terms of exploiting a contained, pressurized gas system.
    ```

  - u/Gurkenglas:
    ```
    Note that if you can contain air at 4096 atmospheres of pressure, gathering 4096 doses of clothgas and unshrinking them should let you target the lot with a single shrink item spell.

    Shrink item is a third level spell slot and thus worth about 150 gp per cast from a hired wizard.
    ```

    - u/erenthia:
      ```
      My initial back-of-the-envelope math told me that the energy release from 4096 atm suddenly decompressing would be enormous.  Enough to launch cannon balls at suborbital velocities.  

      Also, a magic item that created tiny balls of shrunken air would probably allow for selling them at arbitrarily low prices.  Since D&D/Pathfinder magic items have no maintenance and in this case, the units would have no material cost the marginal cost of the compressed airballs would be zero.
      ```

      - u/vakusdrake:
        ```
        Something your calculation is missing is that an air powered gun cannot propel something faster than the speed of sound of the gas pushing it. So either try to do electrolysis of water via electric damage to get hydrogen, or use really heavy projectiles that are devastating even at subsonic speeds.
        ```

        - u/CreationBlues:
          ```
          Don't forget that the speed of sound increases with density. So "subsonic" for 4096 atmospheres is a lot different than for one atmosphere.
          ```

      - u/Daneels_Soul:
        ```
        Hmm... I get something different.

        Released energy is the integral of pdV, right? Unfortunately, p scales like 1/V. So we really have the integral from 2ft^3/4096 to 2ft^3 of 1atm /V dV. But the dV/V integrates to a log(4096), which isn't all that large. My calculation puts the total energy at

        1 atm*2ft^3 * log(4096), which Google tells me is about 47kJ, or about the energy of 10 grams of TNT, which is a bit more than whatever this page calls a heavy firearm: https://en.wikipedia.org/wiki/Muzzle_energy.

        Also, as for cost, you need a 5th level or higher wizard to cast the spell, and they will only get a couple castings a day. Training a wizard is expensive, and since there are relatively few of them (and a lot of other uses for their spell slots), it may well end up being pretty expensive. I mean maybe the marginal cost is 0 in some sense, but the opportunity cost is large, as is the cost of the initial investment.
        ```

- u/MagicWeasel:
  ```
  OK guys, indulge me here:

  In Animorphs, Rachel morphs an alligator and then all of a sudden she starts morphing at random, out-of-control times and in out of control ways (e.g. she'll be a half-elephant half-wolf monstrosity). This culminates in her essentially having a *full size, live alligator* bud off of her body like she's a yeast or something. 

  According to the author, Animorphs: The Reckoning won't include this in its plot. Your task, should you choose to accept it, is to work out how a rational animorphs team could use Rachel's "condition" in an advantageous way. I'm not sure there's much use for it, but I know you lot are as crafty as they come.
  ```

  - u/vakusdrake:
    ```
    Depending on how much control she has over which animals she turns into she might be able to bud off as many copies of herself or other allies as she wants.
    ```

    - u/mg115ca:
      ```
      Assuming it's the same mechanism as in the books, it's analogous to an allergy. Most people have zero, but some people have one or more (I don't recall the term the books used, so let's call them) "morph allergies". When you acquire a morph you are allergic to, the mechanism you use to morph freaks out as described above eventually spawning a clone of the morph in an attempt to (if I recall the books correctly) expunge the DNA that you're allergic to. I don't recall exactly how specific the allergy is (that specific alligator, any of its family, alligators as a species, etc) but it's specific enough that you can't prompt "allergic reactions" for arbitrary morphs. There is no guarantee that the other animorphs will have an allergy at all, let alone one you could eventually discover, or a useful one. Rachel can probably create an unlimited number of alligators, assuming she's willing to go through the whole unpleasant process each time, including risking her life when an adult alligator appears in close proximity to her.
      ```

- u/None:
  ```
  From the last CYOA:

  >You can ask any "yes or no" question that could be answered by a non-Thinker. The question must have a clear answer and cannot be used to predict the future. You are limited to five questions a day.
  ```

  - u/Gurkenglas:
    ```
    What if some person "knows" the wrong answer to a question I ask? "Is Napoleon alive?" would be affirmed by some guy in a mental institution. What if two people are convinced of respectively a mathematical fact like P=NP and its negation?
    ```

---

