## Simverse IV

### Post:

Before I start, let me expose an issue realistic spaceship designers have long faced.

It is a consequence of the Kzinti Lesson: Any drive powerful enough is a weapon. I call it the laser problem.

The laser problem results from the fact that a spaceship with a drive power of X, can generate electricity from its drive of at a rate of AX, and that electricity can power a laser at a rate of ABX. 

A and B are coefficients, going from 0 to 1. A, in most cases is about 0.1-0.05, and B is about 0.6 to 0.3. 

This means that a laser weapon on a realistic spaceship is usually rated at 5% of the drive power. Depending on the nature of the laser and future technology levels, it easily increases to 10%

You might not think this is a lot, but the problem arises even from this small fraction. Here's how it goes:

-To travel across the solar system quickly, you need a powerful drive. The science fiction author will allow his setting to powerful drives to shorten the time his characters spend travelling from one location to another.

-The laser weapons are scaled to drive power.

-The resulting laser is extremely powerful. It can basically slag opponents in space millions of kilometers away.

-This makes for the most boring "click-shoot-wait-a-week-one-side-wiped-out" space warfare possible.

-The science fiction decides to reduce the power of the ship drives.

-This makes for the most boring "start-engines-wait-a-year-your-characters-have-arrived-on-Mars" space travel possible.

The problem is inescapable. If you want your characters to get anywhere without devoting a significant fraction of their life to sitting inside a metal box, you need a powerful engine. If you want your setting to have any form of space combat that involves more interaction than a mouse click, you need weak lasers.

I'll build a quick example. Imagine we have a 200 ton spaceship with a crew of 5. To get from Earth to Mars in two weeks, it needs a deltaV of 1150km/s with an acceleration of 0.1g. That works out as a drive with 0.2MN of force. If we use a reasonable setting, ie not space opera, we'll be using something like Gaseous-core fission drives with an exhaust velocity of 35km/s. The power generated is 3.5GW

If we use a more advanced fusion drive with an exhaust velocity of 200km/s, the power generated is 20GW. If we accelerated at 0.01g and took one month to arrive, the power is 0.35GW.

That means the laser has up to 350MW of power. You know how much that is? A purple laser focused by a 30m diameter array can burn through aluminium at 5cm/s... 33,000km away. 

We have the capacity to produce ultraviolet lasers today. That weapon will burn through 3cm/s of aluminium... from the moon's orbit. 

Now imagine we used the space-opera fusion rocket that allows us to travel the solar system in a matter of days, not weeks. Yeah. You're running through 24m/s (I did not forget an 'm') of aluminium from a million km away... and a non-negligible 0.1mm/s of aluminium from the f**king orbit of Mars. And this is the small spaceship with 5 crew. 

What do you do?

Boring travel, or boring combat? Years to leave the inner solar system, or getting burned to ashes from another planet away.

The simverse setting was originally an attempt to reconcile drive power with weapon power. If the drives were weak, we could have weak lasers. If we could jump to wherever we wanted in the solar system in a matter of seconds, we wouldn't suffer from slow travel hindering the plot, and it will further reduce the fun-killing effect of long-range lasers. 

Now onto the ship design for this setting.

The purpose of a spaceship and how it fights defines its design, simple. 

First of all, sector sizes. For most of the solar system, the average sector size is a cube about 300m across. Past the orbit of Saturn, it rapidly increases to 1000m across. Inside the asteroid belt, it rapidly decreases to 100m across. 

Near Earth, it goes from 50m to 10m.

Combat in this setting revolves around positioning your spaceship, through a swap, next to the enemy, and dealing damage before your opponent can respond or retaliate by swapping away. 

To do this, your swaps have to be faster than those of the opponent, and your weapons have to deal damage in a very short time, and at close range.

If you swap slower than your opponent, he or she will outmaneuver you in literally a second. 

To optimize swap speed, you need the minimum amount of crew and a minimum number of cubes to swap per jump: the solution is 1 each.

1 single crew member reduces the danger of triggering the verification threshold, while forcing the simulation to render the ship in realtime. Two crewmembers more than double the chance of triggering a verification and leaving the ship stranded and helpless following a freeze of the sector they are in.

A single cube reduces the load on the spaceship's computers. Two cubes means calling up the simulation twice, reading the simulation twice and waiting for two rendering cycles to pass simultaneously (you don't want to swap half your ship, eh?). 

So, the optimal fighting craft is a one manned vessel filling a single sector. There is a large variety of possibilities despite these restrictions, as I'll explain below.

During combat, your spaceship will be dancing around your enemy and trying to deal damage without taking damage in return. In most cases, the warships are under 50m long. With such a small volume, and requiring a lot of it to be devoted to inert propellant (rocketry equation, b**ches!), they are going to concentrate their armor on one side and weapons on the other.

Your opponent will force you to swap as quickly as possible. If you do not swap faster than your opponent, he will find you, swap next to you and zap you at point blank.

'Dance' is a good term. If forced to swap at the highest frequency, which in some cases is nearly 10Hz, it is not possible to expect the human pilot to catch up with the computer. The pilot will not be able to direct the spaceship to a sector of his choice after every swap.

The result is a dance between the opponents; the computer executes the instinctive 'steps', while the human pilot, who can't think or determine his position manually 10 times a second, sets up 'moves', 'reactions' and 'paths' for the spaceship to take. The moves can simple orders, like a two-step swap to (A:B:C) then to (D;F;E) to shoot, or a complex chain of moves that react to the opponent's positions. 'Reactions' are preprogrammed responses to the enemy's behavior. If the computer detects the opponent consistently trying to swap in as close as possible, it will leave behind a nuclear bomb at the next swap and jump away from the explosion. If the opponent is jumping to one side then the other, the ship will rotate its weapons face to the next predicted swap. 'Paths' are the general direction the swaps are moving. The back and forths cover a lot of distance, but they are usually concentrated in one area of a few hundred sectors. Continuously swapping within that area transforms it into an 'arena', where majority of cubes have known, unmoving coordinates that allow the quickest swaps possible. After the error threshold gets triggered, the entire area gets frozen and both ships are stuck in the positions their last swaps left them in. The only solution to this is to drift across space while swapping.

The combat mechanics here are immensely complex. 

The biggest tool is statistic. The vast majority of swaps are computer controlled, which makes them fairly predictable after a few thousand swaps. If the opponent can predict where you are with a fair certainly, your next swap will end up with your engines facing a fully loaded weapons face (the ships are cubes). Humans can alleviate this problem, but they are playing against another human, who will eventually decipher them. 

You have to keep in mind that velocity, vector of travel and direction are conserved. If you are travelling at 40km/s relative to your opponent, weapons facing forward, you can swap side-by-side your opponent and you'll travel away from each other at 40km/s, with your weapons facing the wrong way. Since it is not practical to mount weapons and armor facing every direction on such a tiny spaceship, spaceships are designed as cubes that rotate along the axis of travel. Two faces are armored. One face contains the lens that focuses the laser. The final face drops kinetic ordanance. The top face is solid propellant that doubles as a shield against debris. The rear face is where the drive ejects exhaust for thrust. In the center, all the components are maximally protected. During combat, the ship spins to orient its weapons or armor to the enemy. A successful attack faces your weapons against the enemy's weakspot. Over the course of the fight, ships can rotate perpendicular to their direction of travel to line up a shot against the opponent's drives or simply to change direction.

It should be noted that the swaps are not limited to empty space. While the primary weapon is a 0.01 second laser blast, the ships can be equipped with mines and railguns. The use of mines is obvious: place them in a sector you are sure your opponent will swap next to, and they will detonate. You can also swap your mined sector next to your opponent, instead of swapping your own ship. A railgun accelerates inert projectiles that would normally never hit the enemy at range. However, they are much more devastating at point blank than a 0.01 second laser blast, and they can be accelerated into empty space then swapped in front of the enemy. 

Your opponent counters both differently. You will not swap next to your own mined sector, so your opponent will read your swaps and determine which sectors he shouldn't move next to. Like Minefield. Likewise, you would not position your ship in front of your own rilgun shots. This creates vectors that your opponent is denied.

On a HUD, it would like a transparent Minecraft game, with red cubes for suspected mine positions, hazy red sectors next to them for danger areas, and lines crisscross the entire area where railgun shots are moving, with a head and tail to the probability graph for their position. You opponent would be a blinking white cube moving through a cloud of probability concentrations and ghost images, and as the fight progresses, the transparent sectors become foggy, then milky white, and by that time it is best to leave the area before you trigger a reset. 

There are further tactics possible. If you time your swap right, you can catch your opponent and move HIM, placing him in the path of weapons you launched or disrupting his computer-sequenced steps. 

The human pilots constantly have to decide whether to allocate their calculation cycles towards tackling or making their own swaps.

Everything becomes a clusterf*ck of probability clouds crashing into other if more than 2 opponents are involved. 

I said before that ship design is basedon purpose. In this setting, the ship 'classes' are determined by how fast they need to swap, and where. 

A 'coastal guard' spaceship needs to be able to fit inside the very small sectors near planets. Near Earth, they need to squeeze drive, propellant, weapons and fat computer inside a 50x50x50m package. Many things are sacrificed for this size. The mass ratio will be small, meaning it cannot physically travel very far or fast. The weapons will be dwarf-sized, and unlikely to be lasers (they take up a lot of space, need huge cooling reserves and a big power generator). Missiles and mines are their best bet, but that also means they have little ammo to spare and are only good for a few thousand swaps. After that, they are better off freezing the sector to catch the opponent and allow bigger allies to zap them.

A 'dogfighter' craft has swap speed as priority. It has a massive computer, all the weapons facing one direction and a propellant reserve that doubles as coolant so that it can fire its lasers in quick succession. 

Interdictors have a different mentality. They are huge blocks of armor with a small computer and lots of weapons. Their role is to intentionally freeze the opponents. They weather the enemy's fire, and destroy them one by one as they try to leave the frozen sector under normal power. They can, however, be easily countered by starting the battle at high relative velocity, and swapping backwards continuously. They moment is decides to freeze the sector, the attacker's velocity will carry them out of the area and they can shoot the immobilized interdictor at their leisure. Also, thick armor means nothing against gravity-accelerated kinetic weapons swapped on top of it.

In deep space, things change. Sectors become much bigger than any spaceship can be, while rendering cycle delays become a hindrance rather than a target to reach. Spaceship design here is much more traditional, with all-round armor, multiple crews and long-ranged laser weaponry. Long range is only relative, though, since a 1 second rendering cycle means you cannot shoot a weapon that takes more than 1 second to reach the opponent (like a laser 300,000km away).


Oh dear, this is getting dreadfully long. I'll leave the rest for Simverse V.

### Comments:

- u/Empiricist_or_not:
  ```
  Isn't the optimal ship a 0 seat fighter with an expert system that performs HK missions on 1 seat fighters?
  ```

  - u/krakonfour:
    ```
    0 humans onboard: not rendered in realtime.

    You wouldn't be able to bring up the developer's console (the simulation doesn't pay attention to you) and you would only exist at the end of each rendering cycle.
    ```

---

