## [D] Wednesday Worldbuilding and Writing Thread

### Post:

Welcome to the Wednesday thread for worldbuilding and writing discussions!

/r/rational is focussed on rational and rationalist fiction, so we don't usually allow discussion of scenarios or worldbuilding unless there's finished chapters involved (see the sidebar).  It *is* pretty fun to cut loose with a likeminded community though, so this is our regular chance to:

* Plan out a new story
* Discuss how to escape a supervillian lair... or build a perfect prison
* Poke holes in a popular setting (without writing fanfic)
* Test your idea of how to rational-ify *Alice in Wonderland*
* Generally work through the problems of a fictional world.

On the other hand, this is *also* the place to talk about writing, whether you're working on plotting, characters, or just kicking around an idea that feels like it might be a story. Hopefully these two purposes (writing and worldbuilding) will overlap each other to some extent.

^(Non-fiction should probably go in the Friday Off-topic thread, or Monday General Rationality)

### Comments:

- u/alexanderwales:
  ```
  Still working on the diegetic MMO concept (i.e. the world is built on the back of MMO mechanics, but they're all "in world" without interfaces or a separation between game mechanics and worldbuilding). Today's topic: inventory.

  Inventory in games is usually one of the biggest disconnects between mechanics and what those mechanics are meant to represent. Typically speaking, there's either a numeric representation for weight or a grid representation for volume, or some combination of the two, if there are inventory limits at all (which there sometimes aren't). This ... is a little sillier than I'd really want to go, at least as a base, so "natural" inventory is just inventory as it normally is in the real world.

  As for magical inventory? Well, I'm thinking there will be two kinds.

  First, there's "static" inventory, mediated by a magic item that's about as expensive as a refrigerator. If you have a special ring (about as expensive as a toaster) you can interact with the box and open it up to an interior space that's the same no matter which instance of the box you're interacting with. This means that items put into Box 1 at location A can be pulled out of Box 2 at location B. One ring can only open one box at a time, which solves apparent issues with duplication, and the boxes don't work if they're not airtight. Additionally, boxes have to be stopped with respect to some privileged reference frame in order to be used, and will fail if moved while open. (This design is largely based on inventory systems as used in Resident Evil 2 and other games.)

  Second, there "personal" inventory solutions, ways that a person can carry more on them. These are much more expensive, the kind of thing that you might have if it's part of your job or if you're independently wealthy. I kind of want a more robust system here, rather than a single simple rule (which I've been trying to use for the world as a whole), a robust system which would allow things like pulling a sword from extradimensional space on the high end or a carpenter taking five minutes to get his chest of tools out of storage. Variables include time to take out, time to put in, volume restrictions, weight restrictions, etc., all of which would need to be balanced against labor/cost, then extrapolated out, which seems like a lot of work ...

  In terms of practical worldbuilding consequences? The biggest impact is probably in terms of logistics, which has impacts on trade, the economy, and warfare. Supply lines don't *really* need to exist as such, because for enough of an investment, you can just have someone carry a bunch of rings and then pull things out of "static" inventory. The big exception is things that don't fit in the box, and depending on the specific rules for "personal" inventory, there might not be things that fit into even the most expensive storage. Maybe this leads to modularity and a focus on assemble-on-site equipment.

  As a knock-on effect, it's really easy to both hide and steal things, assuming that you're willing to pay the initial investment for inventory. I don't think that this is that big of a deal from a worldbuilding perspective, but it's kind of interesting to think about burglars going into a house and dumping things into a variety of inventory spaces, then bailing out with no outward indication that they've actually taken anything. Maybe people will gravitate towards making sure their expensive things are big so they can't be stolen as easily.
  ```

  - u/red_adair:
    ```
    > I kind of want a more robust system here, rather than a single simple rule (which I've been trying to use for the world as a whole), a robust system which would allow things like pulling a sword from extradimensional space on the high end or a carpenter taking five minutes to get his chest of tools out of storage. Variables include time to take out, time to put in, volume restrictions, weight restrictions, etc., all of which would need to be balanced against labor/cost, then extrapolated out, which seems like a lot of work ...

    I think you could reasonably get all that with a single rule that merges cross-section and mass by limiting the number of units `cross-section * mass` that can be added or removed to a pouch per unit time.

    But you'd have to check the math on that; I don't have intuition about whether a sword would be drawn from an extradimensional sheath more slowly than a same-mass same-length cylinder. Perhaps it should also be a factor of the cross-section of the opening of the extradimensional pocket?
    ```

    - u/alexanderwales:
      ```
      I actually think that I might just go ```mass * volume```, given in gram milliliters (gmL), or larger, kilogram liters (kgL). A gallon of water would be 14.3 kgL, for example. Cost for "personal" inventory goes up by the square of the kgL capacity (plus some base static cost), and input/extract time is a function of how much the item takes up the kgL capacity.

      (We can imagine that volume is accounted for by a wrapping effect, an aether equivalent to a water displacement test to find volume.)

      So, just to pin some numbers on it, a personal inventory with 15 kgL capacity costs $100+$10, and if you're completely filling it, it has an input/extract time of 10 seconds, or an input/extract time of 5 seconds if you're half filling it. Going up to 30 kgL capacity costs $1000+$10, while going down to 7.5 kgL capacity would cost $10+$10.

      There are a few things I don't quite like about this formulation:

      1. It would probably be better for time to be sloped, so that less than a tenth of capacity is effectively instant, and almost at capacity is somewhat time consuming. That makes for better drama in a few ways.
      2. The slope might be a little bit too harsh in terms of cost. Right now, incentive is to have a bunch of these things, and anything you want to carry broken into parts as much as possible.
      3. Calculations are pretty much a pain in the butt and not very intuitive. It's *interesting* that you have incentive to make things as dense and light as possible, but if I would probably want to do a bunch of pre-computing for common objects if I were ever going to use this system to write with.
      ```

  - u/meterion:
    ```
    > Supply lines don't really need to exist as such, because for enough of an investment, you can just have someone carry a bunch of rings and then pull things out of "static" inventory.

    If I understand static inventory right (ring_A opens up space_A) then wouldn't it be more convenient to use ring_A to _Y (etc) for your goods, then ring_Z to store the rest of your rings in space_Z?

    I think one of the bigger decisions that would affect inventory usage is whether rings can be duplicated, or every ring opens a unique space instance. If there's a single point of failure to the system then ring-stacking is probably too risky for most uses, although it leaves a lot of interesting ideas about instant and perfect disposal for any sufficiently small (or choppably small) material.
    ```

    - u/alexanderwales:
      ```
      You could do that, but I don't think that it would be more convenient, because to access space_A, you have to get out ring_Z, open space_Z, take out ring_A, close space_Z, and finally open space_A, and then reverse all of that when you want to put ring_A back into space_Z. You could though, if you wanted to, or has some reason, I just don't think that convenience is a compelling reason, unless I'm missing something.

      Right now, rings cannot be duplicated, meaning that so long as you hold the ring, you have the only key to that unique space. If rings could be duplicated, you'd be able to use it for instant transfer between remote places, essentially giving you a fast-travel conduit, and even if you said living things couldn't use it for whatever reason, it would shrink the world an enormous amount in terms of economy. Even if the rings make transport a whole lot easier, that transport still has to happen, with all the risks and costs associated with that.
      ```

  - u/CCC_037:
    ```
    > Second, there "personal" inventory solutions, ways that a person can carry more on them.

    This sounds a lot like a Bag of Holding, to me.

    > Additionally, boxes have to be stopped with respect to some privileged reference frame in order to be used

    So, you can't access your Inventory while on a moving train? This is important; it means that prisoners can be kept more securely on a moving train than in a stationary location (because you can't break a guy out with a well-disguised Static Inventory box and your personal ring, even if you could smuggle them in).

    With supply lines not being a problem, it's a whole lot harder to starve out resistance cells by cutting off supply lines. However, it is probably a lot easier to locate them (especially if you manage to slip a tracking spell onto something that is likely to be delivered to said resistance - like a prisoner who you then deliberately guard less securely than you could have).

    And it is still possible to starve them out by cutting off access to resources useful to the Reisistance on a wide basis (i.e. if the Resistance uses a lot of mana potions, then they can be starved out by cutting off mana potion supply to *everyone*).
    ```

- u/red_adair:
  ```
  How do you deal with having written a thing, which got to the ending you wanted, but without getting there in the way you wanted or with the desired moral?

  What if you set out to write a morality play, and wrote something that you're pretty sure has come out of it making the Good Example out to be an Ass?
  ```

  - u/CCC_037:
    ```
    Firstly - can it be rewritten to go the way I wanted it to go?

    If not, then why not? Is the lesson I planned to introduce in some way flawed, or impractical? Is it not as universal as I had imagined it to be?

    Is there a deeper, underlying lesson which I can learn from this?
    ```

- u/DisgruntledNumidian:
  ```
  What is your favorite name for an AI?  Not necessarily one that's actually in a published story, one you think would fit well works too.
  ```

  - u/boomfarmer:
    ```
    Officer Roko Basilisk
    ```

  - u/GrafZeppelin127:
    ```
    I like names that are relatively close to, but not quite, human names. Preferably an acronym for a system of some sort. For example, SHODAN from System Shock, or GLaDOS from Portal.
    ```

  - u/xamueljones:
    ```
    I just love the idea of an AI named Fae. It sounds similar to FAI, Friendly AI, and I really enjoy how it links to fairies which references the idea of non-human minds from the supernatural.
    ```

  - u/CCC_037:
    ```
    Something short, and related to its function. For example, and AI intended for observations of stars might be called Astro.
    ```

---

