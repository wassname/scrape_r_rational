## [RT][MK] Delve Chapter 107: Interface

### Post:

[Link to content](https://www.royalroad.com/fiction/25225/delve/chapter/536374/107-interface)

### Comments:

- u/xamueljones:
  ```
  Back when this chapter came out on Patreon, we spent a good while analyzing it. So I claim minimal credit beyond transcribing it to here. Really most of the credit should go to a guy named Zhade on the Discord. Don't read any further if you want to try interpreting the messages yourself, or haven't read the chapter yet.

  Going through the interface messages step by step:

  >Alert: Comprehension threshold reached  
  >  
  >Hybrid Interface Boot  
  >  
  >Please Wait…  
  >  
  >Hybrid Interface Boot Complete  
  >  
  >Hybrid Interface Mode: Terminal \[User-Defined\]

  Pretty basic, it's the artifact reaching it's comprehension threshold aka figuring out how to talk to Rain, and creating the interface. It calls the interface a "terminal", but the name is coming from Rain, as it's user defined.

  >Debug Monitoring: Enabled  
  >  
  >Retrying Direct Link  
  >  
  >Link Established \[Warning: Protocol\]

  Here, the artifact retries its direct link that it was doing before; the thing that caused massive pain in Rain. This pretty much confirms that the artifact isn't sapient in any way, as its first step after creating the terminal is to retry the old method of interfacing. The protocol warning may mean that it's required to do so. Debug monitoring is interesting though, and it explains what happens next.

  >Scanning…  
  >  
  >Header Scan Complete  
  >  
  >New User Detected  
  >  
  >User Name: Richmond (Rain) Stroudwater \[Error: Format\]  
  >  
  >Coerced User Name: rain  
  >  
  >Creating User Profile  
  >  
  >Scanning…  
  >  
  >User Primary Language: \[Error: Unknown\]  
  >  
  >User Origin: \[Error: Unknown\]  
  >  
  >User System Compatibility: 64% \[Warning: Threshold\]  
  >  
  >Compatibility below threshold

  Next, the artifact tries to scan Rain. It first does a header scan, which is successful. Headers are the supplementary data prefixed to a larger block of data. In this case, Rain's header is his name, which the artifact copies, modifies to fit it's own format, and then creates a user profile. The header possibly contains other, esoteric bits of information that Rain couldn't see.

  After that, it continues it's scan, but messes up because the user's language and origin cannot be retrieved. It's not that the artifact doesn't know what English or Earth are. It can grab terms from Rain's head to substitute, like how it defined "terminal". No, something else's wrong, so it checks Rain's compatibility, which is below threshold.

  Now, threshold is obviously the limit to interface with the artifact successfully. Rain is below threshold, and he shouldn't normally be able to interface with the artifact, but his workaround managed to get through. So the artifact adapts.

  >Attempting conformance…  
  >  
  >Conformance Failed \[Error: Unknown\]  
  >  
  >Attempting System Recovery…  
  >  
  >Recovery Failed \[Error: Unknown\]  
  >  
  >Scanning…  
  >  
  >Paling Integrity: 74% \[Warning: Threshold\]  
  >  
  >Soul Fragmentation: 99% \[Warning: Threshold\]  
  >  
  >Core Rank: 18 \[Error: Threshold\]  
  >  
  >Core threshold not met  
  >  
  >Scanning attributes…  
  >  
  >Focus Adaptation: \[Error: Callback\]  
  >  
  >\[System Instability Detected\]  
  >  
  >\[Critical Scan Error\] Aborting…  
  >  
  >Scan Aborted

  The artifact tries to make Rain's compatibility increase. There is no mention of how it would have done this, or if it is even possible with the current state of the Majistraal artifacts. Irregardless, this fails and it's recovery also fails, so it backs out and continues scanning for the cause. It notes down that Rain's paling integrity and soul fragmentation (also note how it uses the paling term, which was unlikely to be in the Majistraal lexicon as it was mentioned by the Watch who existed after the Majistraal's fall).

  Looking at both now, it seems that the Warning: Threshold is a notification that something in the scan has tripped a warning flag.

  Rain's compatibility, paling integrity, and soul fragmentation all tripped warning flags.

  On the other hand, Rain's Core Rank just tripped an Error: Threshold flag. Which probably meant a much more benign error than Error: Unknown.

  So the artifact currently knows something is fucked up with Rain, but it still wants to figure out how to communicate properly.

  It tries to figure out a way through Rain's attributes, but things get real bad here. We get a callback error, which means some asynchronous timing error happened that fucked things up. Rain probably almost died here, given how loud his screams got, and the artifact realized this and backed out.

  >Contact Administrator \[Error: Not Found\]  
  >  
  >\[Error: Unknown\] Retry  
  >  
  >\[Error: Unknown\] Retry  
  >  
  >\[Error: Unknown\] Retry  
  >  
  >\[Error: Unknown\] Retry  
  >  
  >Retry Failed  
  >  
  >Direct Link Failed  
  >  
  >Reverting to Fallback  
  >  
  >Hybrid Interface Set as Primary  
  >  
  >Administrator List \[\] \[Error: Failsafe\]  
  >  
  >User Privilege Level Elevated

  So, the artifact currently has a weak user plugged in, who almost died as a result of the artifact trying to interface better with them. What does it do? It calls for an administrator. Who, of course, isn't there. It retries, don't know if it tries the exact same contact protocol or different different procedures each time, but eventually it finally gives up and uses Rain's interface method.

  And with no admins currently available, this trips a fail safe flag and Rain is elevated

  The rest is pretty self explanatory, so no need for further analysis.

  The fail safe flag is most likely referring to this passage from chapter 73.

  >The obelisk helped him, guiding his understanding. He marveled once more at the mastery of the ancient order of mages as he modified the list of residents for the city, scrolling past the names of thousands of long-dead Majistraal and adding his own to the end, as well as one other. He was only allowed to do this because of the failsafe the Majistraal added to all their technology. If there were no living users, anyone could gain control, provided that their mind could handle the strain. His could.

  So it's probably not just that no admins are available, it's also that there are no other living users registered

  TL;DR: The artifact figured out what Rain wanted it to do, started a user scan as a matter of protocol in order to create a better interface, the scan really fucked with Rain, the artifact realized this and aborted, attempted to contact admin, gave up and used Rain's crappy interface method in the end.
  ```

  - u/KDBA:
    ```
    >On the other hand, Rain's Core Rank just tripped an Error: Threshold flag. Which probably means a much more benign warning.

    Warnings are a step *lower* than errors in most programming languages. Info -> Warning -> Error -> Critical/Fatal
    ```

    - u/xamueljones:
      ```
      You're right that errors are worse than warnings. That comment was supposed to mean that it's a more benign error than Error: Unknown which was popping up a lot.

      I'll edit it now.
      ```

  - u/Watchful1:
    ```
    > We get a callback error, which means some asynchronous timing error happened that fucked things up

    Callbacks don't necessarily have to do with asynchronous calls or waiting for a response. I take this to mean that the operation/function it's trying to call doesn't exist. So it thinks it's able to do something to "adapt his focus", but whatever library/hardware isn't available/connected/set up.
    ```

    - u/xamueljones:
      ```
      You might be right and the missing library/hardware is missing from Rain's soul rather than missing from somewhere else in the obelisk. Either due to his soul issues or because he is a Dynamo.
      ```

      - u/Watchful1:
        ```
        Hmm, or because it's something all Majistraal had, but he doesn't. That makes more sense than some missing external hardware though.
        ```

    - u/Luminous_Lead:
      ```
      I'm assuming that the "focus" is the individual's ability to see their own statistics (their blue screens, runes, books, etc). In this case it might be that Rain has modified his own so extensively that it either doesn't conform to anything the artifact can interface with or that the focus has enough XP pumped into it that the artifact doesn't have enough strength to force a modification.
      ```

  - u/GWJYonder:
    ```
    >(also note how it uses the paling term, which was unlikely to be in the Majistraal lexicon as it was mentioned by the Watch who existed after the Majistraal's fall)

    The Watch and the Adventurer's Guild both come directly from a single Majistraal organization which split, so it's entirely possible that the Paling is a Majistraal term, but not necessary given that there is some sort of language and thought scanning going on here.
    ```

  - u/Ironsides1985:
    ```
    I think that the “Core Rank: 18” bit refers to Rain’s level.
    ```

    - u/Menolith:
      ```
      Now that I think of it, is it coincidence that they're called dungeon _cores_ too? He did get his first soul-look when touching one, after all.
      ```

- u/Imperialgecko:
  ```
  Really interesting chapter, kind of dissapointed that Rain modifying his subconscious to run commands was skipped over. I feel like having that capacity would be a major advantage in many ways, both for true multitasking and having preset responses to certain dangers.

  I enjoyed seeing him "ls" as his first entry.
  ```

  - u/TacticalTable:
    ```
    Something tells me this isn't going to be the last time Rain messes with scripting. Seems like the soul has a pretty good API.
    ```

    - u/Jokey665:
      ```
      inb4 this turns into the smartphone isekai anime just with his soul instead of a smartphone
      ```

      - u/Reply_or_Not:
        ```
        Do I want to know what a “smart phone isekai anime” is?
        ```

        - u/sibswagl:
          ```
          It’s honestly pretty self explanatory. The anime is named *In another world with my smart phone.*
          ```

          - u/KDBA:
            ```
            The anime adaptation has the singularly worst first episode I've seen in my life, but I hear the source LNs are much less mediocre.
            ```

    - u/Menolith:
      ```
      Something tells me that maybe DoSing yourself isn't the best idea when your soul is already leaking your id all over the place.
      ```

- u/panchoadrenalina:
  ```
  the terminal bits were awesome.
  ```

- u/Determinor:
  ```
  So, the majistraal were actually masters of programming aswell. Even if we are seeing the artifact through a strict lens of programming that rain created, they still made a system that had users, privileges, check ups, requirements and procedures involving callbacks, contingencies and backup methods. It also had the capability of self learning through input only.
  ```

  - u/iftttAcct2:
    ```
    Alternatively, it could be sentient or have a human soul trapped in the device.
    ```

    - u/baniel105:
      ```
      Or a dungeon core, as they seemed to show limited intelligence.
      ```

      - u/Luminous_Lead:
        ```
        Dungeon cores being magistral in origin makes sense, especially since they seemed to have randomly generated names.
        ```

        - u/baniel105:
          ```
          Either that or the other way around, with magistral basing their tech off of dungeons
          ```

          - u/zorianteron:
            ```
            The names aren't even necessarily an inherent property of the dungeons- you see the name with your system, after all.  It seems more likely the Majistraal were involved in creating the system, which tags and remembers dungeons based on whatever they were named.
            ```

---

