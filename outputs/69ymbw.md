## [D] Monday General Rationality Thread

### Post:

Welcome to the Monday thread on general rationality topics!  Do you really want to talk about something non-fictional, related to the real world?  Have you:

* Seen something interesting on /r/science?
* Found a new way to get your shit even-more together?
* Figured out how to become immortal?
* Constructed artificial general intelligence?
* Read a neat nonfiction book?
* Munchkined your way into total control of your D&D campaign?


### Comments:

- u/lsparrish:
  ```
  Just a quick plug for my favorite space elevator concept. An [Orbital Ring](https://en.wikipedia.org/wiki/Orbital_ring) is a type of space elevator that we could build today, needing only the strength of (non-tapered) Kevlar to work, although stronger materials are better. This would be unthinkable for the geosynchronous tether idea that everyone is familiar with, which is over 10 times as long.

  It generally isn't a single tether, but generally at least two tethers on each side of the world (or one plus a dummy weight) and works better if there are more tethers. If there are just two, the mass of the ring goes around in a shape that looks like a football (but still very nearly circular). It remains in free fall most of the way, and accelerates slightly towards the earth when it reaches the deflection point, which is what keeps the tether up.

  So the ring itself would possibly just be discontinuous mass -- bolts of short lengths of wire, buckshot, or perhaps longer lengths of something like braided aluminum -- not necessarily a cable, as the diagram at wikipedia depicts. It is just ballast, so it isn't really a structure in the classical sense (although you can consider it part of the "dynamic structure" that holds up the tethers).

  Birch's papers: [#1](http://www.orionsarm.com/fm_store/OrbitalRings-I.pdf), [#2](http://www.orionsarm.com/fm_store/OrbitalRings-II.pdf), [#3](http://www.orionsarm.com/fm_store/OrbitalRings-III.pdf)  

  It is an example of [Super-Orbital Mass Stream](/Space_Transport_and_Engineering_Methods/Structural_Methods#7._Super-Orbital_Mass_Stream), which the [Launch Loop](http://launchloop.com/) is another example. Launch Loop can be considered a partial orbital ring system, or what Birch would call a PORS. A high acceleration PORS or Launch Loop could potentially be used to get enough materials to orbit to create whatever the minimum viable ORS happens to be. Other possible approaches would be light gas guns and mass drivers. Once you have a full ORS, you can use it to get people to orbit via tether.

  Wikipedia quotes a nominal cost of 31 trillion, but this is based on a pretty clear misreading of the paper (i.e. it would be a non-bootstrapped cost which the author was trying to show to be impractical in order to demonstrate better methods). According to paper #2, a likely starter ring would be 180,000 tons, 1/1000th of the one quoted at 31 trillion, so it would be 31 billion in consistent numbers. He doesn't go into why this would be the most minimal, but assuming it is, the cost would more likely be around 400 billion dollars to launch at today's rates, because his assumption was heavy lift (which is cheaper). Using a Launch Loop or other cheaper method to get the materials up there would cut this down substantially.

  It could also be possible to use an even smaller starter ring, if the self doubling rate can be preserved (around 8 hours, enough to go to 1000x the original mass in 80 hours if you make use of it right away). Smaller rings possibly wouldn't support as heavy of tethers, and might need payloads delivered to the upper atmosphere. Without a tether to the ground, some other method of adding velocity to the ring is needed, such as interaction with the magnetosphere, ion drives, or interaction with the atmosphere. For reference, it's 40 million meters around the earth at that height, so it would be 40 tons if you keep the mass to 1 gram per meter (which would give you about a kilogram payload assuming consistent numbers to the 180,000 ton example).

  Note that, as with Launch Loop, payloads actually reach orbit by "riding" the mass stream, gaining momentum by interacting magnetically with it. It's fairly similar in concept to a maglev train.
  ```

  - u/Anakiri:
    ```
    So, if I'm reading this right, any failure of the ring, or of the tether's connection to the ring, or of the tether's acceleration system, or of the tether's power supply, or of the material structure of the tether - any failure of any one component of this active system will result in the ring station falling from a thousand kilometers up and impacting *somewhere* in a million square kilometer area around its base, followed shortly by all the other ring stations also falling?
    ```

    - u/lsparrish:
      ```
      I don't think so. First, it's only a couple hundred kilometres high, so maybe a forty thousand square kilometer area around each tether. Second, for a system with trillions per year in economic value, you'd easily be putting in all kinds of fail safe mechanisms to keep it from failing catastrophically, because even a few minutes of being down is super expensive.

      People would want to live near a tether base to benefit from the transit opportunities, so rather than keeping the base clear and uninhabited, we'd probably over engineer everything to be as safe as possible. There'd be parachutes, a controlled descent path, emergency rockets capable of ensuring stability of the ring for a number of minutes, backup tethers and weights in orbit ready to deploy, and so on. It takes a while to fail, so there is time for corrective measures and redundancies to kick in.
      ```

      - u/Anakiri:
        ```
        I generally don't think that adding complexity to a fundamentally unstable system is a good idea, but it is sometimes unavoidable. However, I'm still not clear on how you actually get to orbit once you're on top of the unstable tether. You're only going, like, 0.5 km/s up there, and you need to reach 7 km/s to be in orbit. Where do you get that delta-v?

        If you steal momentum from the ring of remass that the tethers are tossing back and forth, then that momentum is no longer available to hold up the death platforms. Worse, pushing off from a fragment of the ring puts that fragment into a lower orbit, which sounds like a good way to hit the tether on the other side. Even if you take just a little bit of energy from a huge portion of the ring (without just falling to Earth partway through, when you're not actually in orbit... and how much more massive do the ring fragments need to be than the payload?), you would still eventually need to re-accelerate the ring before it loses enough energy to kill everyone. And if you have to replace the energy in the ring anyway, why not just launch vehicles with whatever you're using for that? 

        Clearly I'm missing something. So... what remass do you use to actually go to space, without destabilizing the orbital ring?
        ```

        - u/Chronophilia:
          ```
          Presumably the station will contain some sort of system for accelerating the ring fragments, to compensate for losses in the deflection system and air friction (200km is not high enough to ignore atmospheric drag). You could use that. It would push the station backwards, but it could correct by launching the next payload in the other direction.

          Or the payloads could bring their own reaction mass, like you suggest.

          Or - if you'll pardon a completely bonkers suggestion - you could build a second loop at a higher altitude, to lift the payload into an even higher orbit. Higher altitude loops go slower, so they would need less energy to maintain (but more mass to build in the first place). With enough of these, you could lift a payload all the way to geostationary orbit.

          ... not to say that any of this is remotely practical. For one thing, spaceflight this cheap is an invitation to drop tungsten rods on cities you don't like.
          ```

          - u/lsparrish:
            ```
            > With enough of these, you could lift a payload all the way to geostationary orbit.

            An easier way to get to geosynchronous is to put up some fuel and use a cheap chemical rocket or electric thrusters... it's only a few thousand km/'s worth of delta vee, and you can change your velocity slowly.

            Just saying, the bulk of the utility of the system is being able to get to LEO inexpensively. I'm not sure it would be worth getting more elaborate for purposes other than safety and greater capacity to LEO.

            But there are some interesting thought experiments for these kinds of ring structures... you could in principle have a space station around a planet that has a spinning side facing in, and a stationary side facing out, separated by magnetic forces. If you were to put one in LEO, the outer side would be nearly a full earth gee. Unlike Niven rings, these would not experience unreasonable tensile stress, due to the influence of gravity on the stationary mass.

            > For one thing, spaceflight this cheap is an invitation to drop tungsten rods on cities you don't like.

            Isn't that more a problem for the military to worry about rather than a practical issue with the proposal? It's not like you can't counter that particular threat relatively easily with conventional missiles, and presumably the military would be among the first customers, so you'd have space based counters too.
            ```

- u/dalitt:
  ```
  I just ran across [this short video](https://vimeo.com/88035957), called "#PostModem," which touches on several preoccupations of rationalist fiction.  It premiered at Sundance 2013, apprently.  Thoughts?

  Warning:  it's very weird and NSFW.
  ```

---

