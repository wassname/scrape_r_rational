## [D][HSF] How To Eat the Moon

### Post:

[Link to content](http://worldbuilding.stackexchange.com/questions/14442/how-to-eat-the-moon)

### Comments:

- u/None:
  ```
  Most people there are missing the resource extraction problems. And they're ignoring the problems of moon dust. Moon dust is sticky. The initial payload either needs a generator that doesn't require having uncovered surfaces or a generator that can easily be cleared of dust. And scratch-resistant -- moon dust doesn't have air or water to weather away sharp surfaces.

  But let's say that's solved. Your initial probe has a nuclear generator with a MTBF of, say, fifty years -- enough to get started. It has a set of tools, but those either require fuel you've brought with you or can run solely on electricity for an extended period of time. You can bring a plasma torch, but you can only carry enough fuel for a few hours of cutting with it. You can melt material with an arc welder, but you might be better off using lasers for everything.

  If you need to do 3D printing, you can use moon dust and a laser. Fuse the dust together with the laser, add another layer on top once it cools, fuse the next layer. You'll want to pulverize the dust somehow to allow for smaller feature sizes -- imagine what you could create by gluing gravel together versus gluing sand together versus gluing talc powder granules together. You also need a way to remove the excess dust later. You don't have any [volatiles](https://en.wikipedia.org/wiki/Volatiles) to wash things with -- unless you bring them with you, maintain a temperature-controlled and pressurized environment, and filter for reuse. Even then, expect losses. Brushes might work, but again, moon dust is sticky, so it might not work so well. Maybe you can move them with careful application of lasers? Uneven heating or something? I dunno. You can also cast metal using dies made with this process -- actually, that's one way you can get rid of excess dust, if you don't mind having to re-smelt some metal afterwards.

  Eventually you'll craft a sealed chamber, and you can extract volatiles from rock. (I'm not sure of the exact process you'd use to break down oxides of silicon and iron / manganese / titanium / aluminium without any reagents, but generally if you apply enough energy to a problem something goes boom.) Unfortunately, the primary volatile you'll get is oxygen, which is, well, rather volatile. It looks like there are some hydrogen deposits on the moon, so you'll probably want to hit those up and manufacture some water.

  While you're getting volatiles out of rock, you can also extract silicon and metals. This lets you create solar panels (if you can deal with the dust -- maybe put them high above the surface?) and circuits. You can also create corundum, which means you can create more lasers, which will speed up your excavation efforts. For energy storage, you can use capacitors -- they'll be easier to manufacture than batteries. But you might have trouble getting an efficient, portable energy storage medium.

  You won't just be creating a bunch of lasers. You need some sort of mechanical manipulator. That means solenoids -- a coiled wire for current and a magnet. It means some sort of lubricant -- graphite would be ideal if you could isolate it. You need cameras of some sort -- a laser rangefinder will be okay in the short term and mostly just requires a laser, which you're already manufacturing, and a way of turning light into an electric current, which you've already done. Communication between autonomous units can use a similar system, or you can use radios. Basic radios are easy enough to produce.

  Potential ongoing issues:

  * A lightweight electrical insulator. We use plastics here on Earth. You don't have those.
  * Keeping solar panels and moving surfaces clear of dust.
  * Power storage is a simple problem to solve, but with a long day/night cycle you'll need to devote a lot of space and materials to it until you find a better power source.
  * Lubricants.
  ```

  - u/lsparrish:
    ```
    To reduce the amount of abrasive moon dust around the work site, maybe create a thin layer of sintered glass over a large area. The mining robots could collect regolith at the edge and roll it back to the work area in sealed containers. Another possible option instead of sintering would be to throw down a layer of some kind of chemical binder that makes the dust clump together like a thin layer of asphalt.

    For power storage, one way would be to fill a big thermos with rocks and store the energy thermally. This would be converted to electricity using a working fluid based TEG or Seebeck based thermopile, with the cold side referenced to the night sky and/or a shaded area. Regolith itself is a pretty good insulator, and the walls could be sinter-printed. So you could actually create hot and cold "batteries", and eliminate the need for photovoltaics.

    Ceramics tend to be good electrical insulators, so if we can't get plastic, that might work. Silicone maybe?

    Iron for the magnets (and maybe structural materials, etc. too) can be collected by sending a rover out over the loose regolith with a strong magnet. There is only a little iron in the regolith (from meteor impacts), but it can be extracted relatively cheaply from a large area this way.

    Graphite could work for lubricant. Carbon isn't exactly common on the Moon, but is probably more so at the poles where the frozen volatiles (CO2, methane, etc) can exist. There are craters from C-type asteroids. At the bottom of these, there are likely to be carbon sources including diamond. This can be cut into bushings, etc. using lasers.
    ```

    - u/None:
      ```
      > To reduce the amount of abrasive moon dust around the work site, maybe create a thin layer of sintered glass over a large area.

      True -- a glass dome serves as an ablative shield that still lets solar panels work at reasonable effectiveness.

      > Regolith itself is a pretty good insulator

      Vacuum is an even better insulator. You use a thin-walled chamber made of regolith with vacuum surrounding it.

      > There is only a little iron in the regolith (from meteor impacts),

      Native iron, you mean? Or are you including all ferrous compounds?
      ```

      - u/lsparrish:
        ```
        > You use a thin-walled chamber made of regolith with vacuum surrounding it.

        That could work. Also if you go to bigger sizes, the volume to surface ratio increases, so insulation efficiency isn't that important.

        > > There is only a little iron in the regolith (from meteor impacts),
        > Native iron, you mean? Or are you including all ferrous compounds?

        I was thinking all ferrous compounds, but it turns out I was misremembering what I had read -- it's the metallic form that is 0.5% or so. In oxide form, iron is fairly common in lunar soil. Something like [15%](http://www.lunarpedia.org/index.php?title=Iron) depending where you look. However, metallic is more strongly attracted to magnets than oxides, so if you want to get pure iron with relatively little processing energy, you could magnetically [separate out](http://www.lunarpedia.org/index.php?title=Iron_Beneficiation) the metallic particles.
        ```

---

