## [RT][WIP] Worth the Candle, ch 62 (Drift)

### Post:

[Link to content](http://archiveofourown.org/works/11478249/chapters/29330487)

### Comments:

- u/narfanator:
  ```
  Wow. [Null pointer exception], if it's not simply a joke, is the first exposed vulnerability in the game layer. With time and experimentation, could be a way to escalate user privileges from there.
  ```

  - u/GeeJo:
    ```
    I'd say the intelligence overflow from MEN-upping probably counts as  exposure, too, in that it laid bare the upper meta-level for a moment. Even if the failure was handled gracefully by the system.
    ```

  - u/MultipartiteMind:
    ```
    My thoughts indeed!  Whether it's how the System handles demons or beings without souls, it looks like a big glaring blindspot--

    --Actually, scratch that.  That was my first thought, and would be really exciting (as well as scary) if so, but I'm replacing it with my new first hypothesis that the System is identifying her fine, but *she doesn't have a name*.  In that case, with the System just not having a name to put in that position, it should be replaced by a name as soon as someone (the protagonist?) gives it to her (and it's accepted).  Not being able to display her name because she doesn't have a name is unfortunately less exciting than not being able to display her name because she doesn't have a soul (or because she's a possessing demon).

    Edit:  When checking about whether any name was mentioned, I was reminded that Amaryllis is not going to be happy about him choosing to save her, perhaps mollifiable by the Companion status revelation.
    ```

    - u/Quetzhal:
      ```
      I don't know about that. There's a few ways you could potentially get a null pointer, at least in C:

      1) You left your pointer uninitialized, in which case it could be a null pointer or any other random number. You might get a null pointer, but you might also get some random person on the other side of the continent.

      2) You tried to allocate memory to store the name, and the memory allocation failed. This is kind of a really weird possibility, because if you're at the point where you can't store a simple string of bytes, there should be a lot of other problems with the simulation.

      3) You actually set your pointer as a null pointer. 

      I actually think 3) is most likely in his instance. If souls themselves are pointers, then the lack of one is arguably a null pointer. The system tried to access the 'soul' pointer and retrieved 0, then tripped the null pointer exception.
      ```

  - u/entropizer:
    ```
    Sounds like begging for rollback. You'd need to move very fast in taking control.
    ```

- u/wnoise:
  ```
  Has anyone mentioned that "Fallatehr" is an anagram for "All Father"?
  ```

  - u/eternal-potato:
    ```
    Also for "Earth Fall", "Alert Half" and "A Fart Hell".
    ```

    - u/jaghataikhan:
      ```
      >9000 hells - last anagram is all but confirmed to be plot relevant :D
      ```

    - u/Tetrikitty:
      ```
      TINACBNIEAC.
      ```

- u/SvalbardCaretaker:
  ```
  >“She’s innocent,” I said.
  >“Shit,” Fenn swore. “She’s fucking Joon-bait.”

  Muahahaha
  ```

- u/None:
  ```
  [deleted]
  ```

  - u/Kerbal_NASA:
    ```
    She was mentioned as one of the non-elf people they met in the gymnasium full of Fallatehr's "associates". I don't think there's any other reference to her.
    ```

  - u/rafaelhr:
    ```
    I would also like to know that.
    ```

- u/kraryal:
  ```
  I loved the null pointer exception
  ```

  - u/FudgeOff:
    ```
    There's a possibility that by increasing his loyalty level with the nonanima Juniper will raise his loyalty level with every other entity that lacks a soul/is a null pointer. Which may or may not be powerful and useful.  

    Also, this means that souls act as pointers for the computer system that runs reality, which is very interesting and makes soul magic sound really powerful. I'm beginning to think that soul magic will end up just being computer programming.
    ```

    - u/narfanator:
      ```
      > raise his loyalty level with every other entity that lacks a soul/is a null pointer

      Unlikely. It's not the value of the pointer that matters*, it's the values at the address to which they point. So it could matter what's at the null memory address, or near it, in the case of pointer arithmetic; this is (AFAIK) part of how common security attacks can work.

      * Outside of pointer arithmetic, etc.

      If we're presuming that this is an actual error in the game layer, and not a joke/reference, then this would imply that loyalty is NOT a property of whatever object type the pointer is for; but that where the companion title/name comes from *is*. Which is interesting. It also implies that the game layer will catch exceptions and handle them gracefully, instead of crashing. Also interesting.
      ```

      - u/ajuc:
        ```
        The fact that accessing null causes NPE means that it's probably a managed memory language, and pointer arthimethic is right out.
        ```

    - u/kraryal:
      ```
      Do golems have souls? Now I have a funny mental image of all the free golems following him around
      ```

    - u/Noumero:
      ```
      > I'm beginning to think that soul magic will end up just being computer programming.

      Well, [I'll take that compromise option](https://www.reddit.com/r/rational/comments/72iul3/rtwip_worth_the_candle_chapter_40_in_which_the/dnj3brm/?context=3).
      ```

- u/valeskas:
  ```
  Interesting. Maybe you can temporary stuff any soul into nonanima, so she would be immediately useful.
  ```

  - u/sharikak54:
    ```
    I was wondering if they could stuff Solace in her, maybe for healing or druid-specific knowledge.
    ```

  - u/Makin-:
    ```
    I think that would be counterproductive and just "kill" the nonanima, replacing her with someone else. Getting her original soul would help her, but not sure beyond that.
    ```

    - u/Izeinwinter:
      ```
      That is the sort of thing where one should ask the handy expert, not wonder.
      ```

- u/Izeinwinter:
  ```
  Theory: Based on the conversation before he turned the elves into fighting machines, I am making a guess that the method Fallatehr is using to control the shaped is that he has rendered their souls unstable - without a soul mage to maintain them, they will decay and eventually turn soul-less. The non-anima is the result of those experiments, and also a reminder what happens to you if you cross him, which is why he kept it around. 

  ... Which in turn implies the non-anima was the sort of person who would rather go into oblivion than obey Fallatehr. Yhea, if I am right, definitely companion material, tough reconstructing a soul is a tall ask. 

  Other things soul-magic is very likely to be useful for. Fallatehr edited fear out of himself. The fact that this is possible implies that self-directed soul magic can render Joon zen about the whole leveling process - That is, just straight up carve it out of himself as a value, making his attitude one of "it happens, it happens". That is very good news, because Experience-point addict Joon is not a story line I want to see.
  ```

- u/TempAccountIgnorePls:
  ```
  So the system can glitch. This is good news on the "avoiding the narrative" front.
  ```

- u/dalitt:
  ```
  I wonder why the chapter title is "Drift"?  Value drift, maybe?
  ```

  - u/None:
    ```
    Drift from the paths predicted by the game layer?
    ```

- u/cthulhuraejepsen:
  ```
  Typos here, please.
  ```

  - u/HomotoWat:
    ```
    > her scarlet-colored eyed 

    should be "her scarlet-colored eyes"
    ```

    - u/kraryal:
      ```
      Since scarlet is in fact only a colour, should it not just be "her scarlet eyes"? I wouldn't expect to see someone write "her blue-coloured eyes" either.
      ```

    - u/cthulhuraejepsen:
      ```
      Fixed, thank you. (Also, removed "colored", as it's cleaner that way.)
      ```

  - u/Kerbal_NASA:
    ```
    >I will remain imprisoned with a fewer resources

    with a fewer -> with fewer

    >It was twenty feet to the ground when were I was

    when -> from

    edit: Thought I'd mention that the first seven foot tall woman reference:
    >We kept moving as they talked, with the conversation carried out over the rustling of clothes and the echoing sound of our footfalls. Each step of the seven-foot-tall woman was almost thunderously loud, and she was breathing heavily, putting by far the most effort into moving quickly.

    confused me a bit and I saw [elsewhere in the thread](https://www.reddit.com/r/rational/comments/7fx0so/rtwip_worth_the_candle_ch_62_drift/dqf6liq/) other people were confused to. You did mention her at the beginning of the last chapter in the sentence:
    >Most of them were elves, but there were other races too, an insectoid with a multi-hued carapace that had been scored with lines, a man with bumpy grey skin I recognized as one of the vlere-gur, and a woman who stood nearly seven feet tall and didn’t belong to any race I could recall making or reading about.

    Maybe if I was reading it all at once it'd feel more natural, but I think it might have been a little too off-hand a mention to stick.
    ```

---

