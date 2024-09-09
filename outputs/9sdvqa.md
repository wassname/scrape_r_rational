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

- u/None:
  ```
  [deleted]
  ```

  - u/Gurkenglas:
    ```
    Have you tried inverting screen colors so the text is white on black?
    ```

  - u/MagicWeasel:
    ```
    I really enjoyed [Dragon's Egg](https://en.wikipedia.org/wiki/Dragon%27s_Egg), by Forward.
    ```

  - u/MistahTimn:
    ```
    I've also been re-reading Pratchett lately, specifically through the lens of this [interview with Neil Gaiman](https://www.theguardian.com/books/2014/sep/24/terry-pratchett-angry-not-jolly-neil-gaiman) about his writing being motivated by anger. Lately I've been finding myself drawn to reading things that are written with a certain end goal in mind, which I think is a great way of describing a lot of rationalist works as well as Pratchett's works. Pratchett's stuff is often satirical in bent which I think is an interesting counterpoint to rationalism.

    My other suggestion for older fiction or sci-fi that provides interesting insight would be Douglas Adams. The Hitchhikers' Guide to the Galaxy, while certainly not rationalist in any way, still is a very insightful look into the human condition. In many ways, I think it's a argument against the nihilism that seems to have seeped into public discourse. Adams' work is all about a simple man working his way through a series of fantastical and terrible events while maintaining his humanity throughout, and I find myself really empathizing with Arthur Dent all throughout.
    ```

- u/babalook:
  ```
  So, I'm reading through a worm fanfiction known as Memorial and at one point in the story, Taylor begins using her insects to form an array telescope which greatly increases the range she can observe things from. Can someone explain how this would work or why it wouldn't given her abilities? I'm just not seeing how you can get telescopic vision from looking through bugs.
  ```

  - u/levoi:
    ```
    She could use the bugs to create a [Pinhole](https://en.m.wikipedia.org/wiki/Pinhole_(optics). 

    See also this physics stack exchange [question](https://physics.stackexchange.com/questions/322798/is-a-mirror-less-telescope-possible).
    ```

  - u/suyjuris:
    ```
    Disclaimer: I have not read that work, so I can only comment on how things work in reality. Also, my knowledge is limited. With that said, you might find the Wikipedia article on [Radio Telescopes](https://en.wikipedia.org/wiki/Radio_telescope) interesting, which is what I would first think of when I hear the term array telescope.

    > The angular resolution of a dish antenna is determined by the ratio of the diameter of the dish to the wavelength of the radio waves being observed

    So, by building a larger dish you have a higher angular resolution, which determines how small the details that you observe can be. (A separate issue is how sensitive your instrument is, i.e. how intense the detail has to be for you to observe it.)

    Interestingly, what you can do for radio telescopes is building multiple ones and combining their signals, such that the resulting telescope array has angular resolution as though it were a single large telescope. (One that would be much too large to built as single dish.) So that's great. But I guess Taylor is not especially interested in only detecting radio waves, as that would only tell her the location of the nearest radio station.

    For optical signals building an array is much more complicated, as you cannot measure them using electronics and have to do the 'combining' (interferometry) directly on the optical waves. As I do not see Taylor connecting her bugs via optical fiber and installing interferometers, at which point you could also just dispense with the bugs, I do not think that doing this using interferometry is feasible.

    (Also, the information biological eyes collect is not enough anyway.)

    So, let's leave astrophysics and consider approaches more suited to optical instruments. Once again, [Wikipedia](https://en.wikipedia.org/wiki/Super-resolution_imaging) has us covered. 

    > Multiple-frame [Superresolution] uses the sub-pixel shifts between multiple low resolution images of the same scene. It creates an improved resolution image fusing information from all low resolution images, and the created higher resolution images are better descriptions of the scene.

    Basically, if you collect more data you can resolve more detail, it is only a matter of how you combine the data. If your perspective moves slightly, and you know how much it moves, you can reconstruct a higher quality image. (Also the motion can be detected from the image.) You could even do this using multiple cameras at different positions, like a swarm of insects, though that is more difficult as you need to correct for perspective. In conclusion, there is no fundamental obstacle to obtaining telescope-like vision by combining information from a multitude of sources. However, this would already work using only a single camera (say, Taylor's own eyes) and the fact that information is captured over time. While our brain is good at a lot of things, high resolution computations are not one of them, so there is lots of room to improve.

    Still, it would require Taylor to do an extraordinary amount of computation.

    Given recent research on extracting unintended information out of an image based on indirect light effects (e.g. [looking out of windows which are not visible](http://people.csail.mit.edu/billf/publications/Accidental_Pinhole.pdf) or [seeing around corners](https://people.csail.mit.edu/klbouman/pw/papers_and_presentations/cornercam_iccv2017.pdf) or even [seeing around corners WITH LASERS](https://news.stanford.edu/2018/03/05/technique-can-see-objects-hidden-around-corners/)) I'd guess that, given this much computational power, Taylor would do better to focus on indirect information. You do not need a lot of bug cameras running around for that, though it would probably help.
    ```

    - u/kraryal:
      ```
      Taylor functionally has tremendous amounts of computation available, and can gather data from bugs in a radius of something like three blocks. 

      This means she can have multiple eye-equivalent viewpoints using that superresolution method you mentioned, look around buildings, see things on the street next to her, etc.
      ```

---

