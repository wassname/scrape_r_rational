## [RT, HSF] Programmer at Large Chapter 3: What’s that noise?

### Post:

[Link to content](http://www.drmaciver.com/2017/01/programmer-at-large-whats-that-noise/)

### Comments:

- u/PeridexisErrant:
  ```
  I continue to enjoy this story far more than I can explain to all but a very few of my meat-space friends.  With time it could even overtake *Stargate Physics 101*...

  (And thanks also for Hypothesis, which is still my favorite library ever :))
  ```

- u/Meneth32:
  ```
  I think the timespans here are a bit weird. A megasecond is just over 277 days. A "fifty megasecond nap" would take 37 years.
  ```

  - u/DRMacIver:
    ```
    You've got a calculation error somewhere - a megasecond is about 11.5 days. A fifty megasecond nap is only about a year and a half.

    (And yes, the timescales are weird, but they're correct)
    ```

- u/traverseda:
  ```
  I don't know how intentional is is, but I really like how the conversational interface doesn't have any consistent voice.

  I would love to hear some thoughts about better ways to organize things then file systems.
  ```

  - u/DRMacIver:
    ```
    > I don't know how intentional is is, but I really like how the conversational interface doesn't have any consistent voice.

    Mostly unintentional but intentionally not avoided. It's a specific feature that the conversational interface is something closer to cleverbot + a long history of editing and heuristic tweaking than any sort of true AI.

    It *is* deliberate that it alternates between very dry (somewhat automated) and very sarcastic (someone has probably edited this while annoyed).

    > I would love to hear some thoughts about better ways to organize things then file systems.

    I'm semi-deliberately not going to provide too many canon answers about how the shipboard computer systems actually work.

    My assumption is that they have some sort of extremely well indexed content addressable storage as their public interface for organising things and then individual processes have a private namespace of on disk data that they own and can expose parts of to clients.
    ```

    - u/traverseda:
      ```
      > I'm semi-deliberately not going to provide too many canon answers about how the shipboard computer systems actually work.

      I get that. I'd still like to hear some non-canon thoughts on the subject though. I'm working on some tools to treat rethinkdb like a filesystem, in that it fills a similar role, not in that you interact with it like a file system.

      Capnproto is also doing some interesting stuff, integrating an object store with its RPC protocol.
      ```

      - u/DRMacIver:
        ```
        OK, so informally the following is the design in my head for how things work in terms of trade fleet data organisation. It doubtless has major flaws, and exists more as a model for me to think about this than it does an actual design:

        * Everything is abstraction layer upon abstraction layer upon abstraction layer. Often there are multiple competing abstraction layers and an additional abstraction layer on top of them to paper over the differences.
        * There is a multiply redundant distributed content addressable object store threaded throughout the ship. In fact there are probably several of them with entirely independent lineages just to be sure. Can be thought of informally as a bunch of files named by hashes with replication to multiple servers, but it's probaly smarter than that.
        * There are a variety of naming systems on top of that, but there is probably one primary distributed hash table that has a bunch of canonical names that point into the CAS. Think DNS, but probably non-hierarchical. There is some complicated permissions model for how it gets updated.
        * There are also a bunch of indexing systems which are effectively very smart search engines for things in the CAS.
        * Separately, each process is localized to a server with its own disk space and may ask for private on disk "files" which are growable buffers with a fixed maximum size. Each gets a UUID of some sort associated with it. It chooses how these persist across process restarts (the default is that it is wiped each time). It may share these buffers with other processes running on the same machine through some sort of object capability model. Depending on its permissions it *may* be able to read and write data to the central storage.
        * All code and associated data lives in the CAS, including the incremental states. Dependencies are identified by hash (there is no versioning per se - everything is pinned, but there are a number of pointers that suggest things like "this code supplants that code"). Deployment consists of saying "Run the process description associated with this hash on the servers matching this query".

        Designing file systems and data organisation isn't really my forte, so I'm sure one or more of these assumptions is hopelessly naive.

        But it doesn't necessarily matter because the following are the *actual* rules for technical design of trade fleet software:

        * Any problem we could currently imagine solving with time and brute force has been solved with time and brute force to a degree that looks magical to us. e.g. search Just Works to a truly ridiculous level of DWIM.
        * Any problem we would require a really deep theoretical breakthrough to solve has not been solved and may be unsolvable. e.g. canonically P!=NP in this universe and cracking a sufficiently large 21st century SSL key would still be non-trivial to impossible.
        * trade fleet opinions about what constitutes good design are not necessarily *correct* compared to ours, merely different and optimized for a very specific environment. e.g. For all I know hierarchical file systems really are some pinnacle of good design.
        ```

- u/MaddoScientisto:
  ```
  Simply amazing, although you are evil because I had to constantly Google the values of the seconds  to get an idea of what time scale they are talking about
  ```

  - u/Escapement:
    ```
    I infer from this that you haven't read much of Vinge (A Fire On The Deep, A Deepness In The Sky)? If that is the case, you should definitely go check his stuff out.

    Not like super rational or anything, but anyone who likes the stuff this subreddit has and this story series in particular will probably love Vinge.
    ```

  - u/daydev:
    ```
    Now you know the pain of every non-American forced to deal with feet, pounds, and other such nonsense because of American cultural dominance.
    ```

- u/Gurkenglas:
  ```
  I sure hope he now goes on to publically propose to convert all old private-disk-buffer-that-have-never-been-read generators into loggers.
  ```

  - u/DRMacIver:
    ```
    You have (more or less) correctly anticipated the next chapter, yes.

    It's a bit harder than that of course.
    ```

---

