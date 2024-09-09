## How would you stop a Man-in-the-Middle attack in a Fantasy setting?

### Post:

Inspired by The Wandering Inn's latest chapter, what would you do If you are the 5th Wall's Bastion-General? Assume you have all the resources that the Kingdom Rhir provides, the irregulars from the other kingdoms and the Champions that was isekai'd from Earth.

Backstory [here](https://wanderinginn.com/2020/07/12/7-34-c/) and [here](https://wanderinginn.com/2020/07/15/7-35-c/), actual attack [here](https://wanderinginn.com/2020/07/19/7-36-c/). Don't worry, these all happens at the literal other side of the world from the main characters, and **can be read as a standalone three part story**.

### Comments:

- u/Se7enworlds:
  ```
  I don't understand why you wouldn't have different sign in and out codes for different situations. 

  This is a world with various ways to compromise people, Seliphids being a race that exists for that purpose, so why not have a code that says 'It's me and everything is fine' and a seperate code for 'it's me and everything is going to shit'.

  Even this villain is a historically recorded entity and her name seems to indicated some idea of their powers, so it's not excessively paranoid for this to be in place.

  Giving a code that IDs, but doesn't correspond to this situation would then raise alarms
  ```

  - u/Brell4Evar:
    ```
    Something as simple as returning the correct code out of sequence would help. Multiple countersigns being scrambled is a big red flag, especially if the sequence is modified in a specific way that differs with each end point.
    ```

    - u/Se7enworlds:
      ```
      The issue is not being aware at the time of giving the signal that it's being intercepted. Situational codes would work regardless.
      ```

      - u/Brell4Evar:
        ```
        I don't disagree. I'm just suggesting reordering the code in a specific way during a crisis so that officers don't need to memorize additional codes.
        ```

        - u/Se7enworlds:
          ```
          Oh yeah, that's fair, or some other minor change
          ```

- u/The_Wingless:
  ```
  As much as I love The Wandering Inn, I never expected it to be mentioned in this subreddit :-)

  As for blue teaming this type of thing, I feel like there should have been another set of codes in the middle of each statement. The initial code was good to confirm identity, but then ol' Death of Magic could hijack the stream and do all of what she was doing. But if, midway through, she had to verify again, she'd be screwed.

  Also, and this specific situation might not work out since I think DoM is an [Archmage] equivalent if she is not one outright, they shouldn't be using items that are so mundane. Look at Pisces and Ceria's little home brewed message spell; It's custom, does not conform to standard spell methodology, and is therefore far more secure. With the kind of resources that the Kingdom of Rhir has it their disposal, each communication item should be bespoke and unique.
  ```

  - u/lecupra:
    ```
    > “Commander Cirille. Report in. Night code is Invinctel-Surreptitious—”
    > 
    > “Bastion-General! We’re under attack! Er—Code Viridian-Adamantium-Salazsar-Terrium!”
    > 
    > The Drake shouted into the stone. She heard nothing from the other side for a second.
    > 
    > “Bastion-General, the spell is widespread and there are Demons on the walls. Unknown number; they had suborned command of undead forces and—”
    > 
    > “—this is Commander Cirille. Code Viridian-Adamantium-Salazsar-Terrium. Nothing of note to report, Bastion-General.”
    > 
    > Cirille heard her voice, coming from the speaking stone. The Drake froze.

    It sounds like rather than a hijack, Silvenia is muting the victim response, then transmitting her own illusion.  So as long as she knows the code to give (by listening to the victim's intended response) she wins.  More authentication codes might help in that her replacement transmission might need to be delayed enough (waiting for the victim to say them) to be suspicious--assuming she can't multi-task and begin her replacement transmission before the victim is finished (and keep them from hearing it).

    I think the easiest approach is the authentication code needs to be tied to the message in some way.  For example, you have separate authentication codes for all-quiet / routine-combat / emergency which would warn the receiver if the content of the message doesn't match up with the meaning of the code.  Still vulnerable in more subtle cases, but at least you couldn't hide an all-out attack.

    Ideally, you'd want to luck out an have an earther with cryptographic experience.  Given that the only computers in the world are a handful of laptops and smartphones even a trivial encryption or MAC algorithm (for example, an enigma machine should be possible) would be safe for a while.
    ```

    - u/FeepingCreature:
      ```
      >      
      > 
      > It sounds like rather than a hijack, Silvenia is muting the victim response, then transmitting her own illusion. So as long as she knows the code to give (by listening to the victim's intended response) she wins. 

      You need prearranged challenges per message. Can't intercept because you won't get the right response.
      ```

  - u/Lord_Zane:
    ```
    >  It's custom, does not conform to standard spell methodology, and is therefore far more secure.

    The Bastion-General _almost_ had this. It's clever, because at the start you think he's dumb for asking questions like "how many arrows to the ones place do you have stockpiled", and then it turns out to be useful later on. When the Bastion-General asked for it again during the attack, Cirille could've given a wrong answer, Silvenia would repeat it, and the Bastion-General would've known something was up, except that he frustratingly changed his mind about it at the last second.
    ```

- u/Mountebank:
  ```
  The codes to verify identity should have had an alternative distress version, sort of like the “blink twice if you’re under distress” signal. Silvenia only started copying the voice in the transmission after the commanders gave their personal ID code, so she can’t read minds— thus she wouldn’t know what the codes actually meant.
  ```

- u/GET_A_LAWYER:
  ```
  Per Wikipedia, stopping MITM attacks requires encrypting the message, and each recipient having the sender’s public key. 

  If for some reason the attacker can’t mute their own transmissions (“sender hears her own voice make a false transmission”), then you can require a three part handshake:
  Sending party: Code1 plus message.
  Receiving party: Code2 plus echo message.
  Sending party: Code3.

  If the sending party hears the MITM they don’t send the final handshake code, and the recipient knows the message was compromised. 
  This method abstracts out to an arbitrary number of messages where each message echoes the previous message plus it’s response.
  ```

- u/Norseman2:
  ```
  I haven't read The Wandering Inn, though it looks interesting. As for this particular question, there's a few key approaches that could've been used to prevent this from becoming a problem.

  To start with, it sounds like they may have neglected penetration testing. Having a reasonably competent spellcaster try to interfere with their communication system (among other security measures) may have helped to prepare them for the level of disruption they could face in an attack. Obviously, this doesn't help against immensely-capable assailants who manage pull off completely unimagined attacks, but for attacks which are at least conceivable, it could help immensely. If they had done penetration testing and this threat was raised as a possibility, they might have been able to plan for workarounds, like alternative communication methods, two-factor authentication options, and no-communications backup plans.

  Another potential issue is the lack of dedicated communications specialists. Commanders have enough on their plates already, so even if there was a two-factor authentication protocol, they'd be tempted to rush and ignore it. A dedicated communications specialist whose one job is to follow proper communication protocol with a variety of available communication methods will be much more likely to achieve secure and reliable communications.

  In an alternate scenario, this could've played out with five (?) signallers checking in with each other signaller on 15-minute intervals. They'd initiate the contact with two-factor authentication, giving a memorized code that they always use, plus a code read from a sheet of random codes which is generated and distributed daily for each signaller pair, and the other signaller would reply likewise. The code sheets would include a sequential list of the 15-minute interval codes, plus an additional sequence of codes to be used for sending any actual messages. With the contact times spread out, this would mean authenticated communication is happening at least every 3-4 minutes, so any wall that goes dark would, by protocol, be discovered by the others within that time frame. Alternate communication measures might include signal fires, smoke signals, messenger riders, signal drums and horns, semaphore, heliostats, homing pigeons, and various magical means. All of these would need to be shut down to actually disable communications, which would be quite difficult for any attacker who isn't already able to overwhelm the defenses with ease.

  Even if such a complete communications failure were possible, it would nonetheless alert all of the walls of the issue within 3-4 minutes, resulting in each wall independently executing their backup plans. In this case, it doesn't sound like there are any inner defenses they could fall back to, but that would be preferred approach during a blackout - bring all forces close together so that there's no longer a need for long-distance communication. Force concentration is rarely a bad choice, at least as long as the enemy isn't heavy on area-of-effect attacks, although hopefully the defenses would mitigate those sorts of attacks.
  ```

  - u/PeridexisErrant:
    ```
    This gets you up to a roughly *Enigma*-level of security, and key distribution is a serious challenge for such programs.
    ```

- u/Izeinwinter:
  ```
  The ideal solve is one time pads, which gets you absolute immunity to this kind of thing. For actual military units, only downside is the risk of running out of pads, though a properly done setup will have the unit carrying an entire book worth of code sheets. (This gets labor intensive in scribe time if you do not have a non-manual way of generating them, but.. well. Worth it.) 
  ,
   For spies, there is the issue that anyone caught with a code book can be summarily executed as a spy, which leads to the next best thing: 

  The Book Code. Works for any literary culture. First you run your message through a very rudimentary cipher, then you pick a random novel you can get hold of in any convenient book store, and  use that as the one time pad. 

  To crack this, your adversary has to guess the correct novel, and the correct cipher, both, which is very difficult. (The cipher is required to stop people from just brute forcing their way down the list of widely spread books. Decoding with the correct book will still yield apparent nonsense even if you just did a basic Cesar substitution. Brute forcing the full list of best sellers and trying to crack each deciphered message is just... not feasible.
  ```

  - u/Norseman2:
    ```
    One-time pads (and other encryption methods) would be tricky when you have humans doing the encryption and decryption, and you need messages processed in real-time for quick responses in combat. However, it could actually be viable in this situation if they were combined with no more than a few dozen predetermined codes to shorten the message length. Imagine a conversation like:

    >"FLAG-1, this is COBALT-312, message 87, over."

    >(Ten seconds later) "COBALT-1, this is FLAG-693, acknowledged, message 27, over."

    >(Ten seconds later) "FLAG-1, this is COBALT-328, acknowledged, message 10, over."

    >(Ten seconds later) "COBALT-1, this is FLAG-705, acknowledged, message 62, out."

    Cobalt might be the expected callsign of the messenger who works on Wall 4 during weekday night shifts, for example. Flag might be the expected callsign for the messenger working alongside the bastion commander on weekday night shifts.

    The numbers following the callsign could be used to indicate both sender/intended recipient as well as message number and truthfulness of the message. A single digit after the callsign indicates a specific officer at an outpost, so FLAG-1 would be the bastion commander. Two digits or greater after the callsign means we have a message number and a parity digit, so Cobalt-312 tells us that the following message is the 31st message that Cobalt has sent to Flag during this shift, the message is to be delivered directly to the bastion commander, and the message is to be understood as a lie likely sent under duress.

    The way we identify the lie is to check if the overall number is divisible by three, and there's an easy math trick to do this. If the sum of a number's digits is divisible by three, then the number is divisible by three. 3+1+2 = 6, which *is* divisible by three, so Cobalt-312 could indicate the message which follows is a lie sent under duress, whereas Cobalt-310, Cobalt-311, Cobalt-314, etc. are not divisible by three and would all indicate a truthful message. In typical practice, these might easily look like random digits added to the end of the message, so it would help to keep an attacker from realizing there's a tell.

    After Flag receives the message, they check for the correct location on their pad sheet for the night and find the pad number that should be used for the 31st message; let's say 57. 87-57=20, which might mean "Routine fifteen-minute check in, all clear, nothing to report". However, this is a lie, so the bastion commander is notified that Cobalt is in trouble.

    Flag replies using 693 indicating it's the 69th message, and their reply is a lie. The pad at 69 might show 83, so 83-27=-56, which is negative so we add 100 and get 44. Message 44 might be written down on the message sheet as "We are putting out a fire, please confirm it has not spread to your location and ensure fire-safety at your location". Since this is a lie, what it might actually mean could be closer to "We're sending reinforcements immediately, we're going to use smoke to conceal our approach, try to buy time."

    Cobalt replies with an authenticated message again lying about things being all clear. Flag replies with an authenticated and truthful message simply acknowledging receipt of Cobalt's reply and ending the conversation.
    ```

    - u/Izeinwinter:
      ```
      Way too complicated, especially since both writing and decryption of one time pad messages can be made blindingly fast. If you use a binary pad, the only step from "Mathematically unbreakable ciphered message" to "Clean Morse" is xor against the book, which you can do as fast as you receive or send the message.
      ```

- u/tobias3:
  ```
  Duplicate + use the Earther iPhones/Androids as communcation devices ;)

  The problem was that the messages were not authenticated, so Eve could modify them without detection. To prevent this append a [message authentication code](https://en.wikipedia.org/wiki/Message_authentication_code) (MAC) with the message itself and a secret as input. The problem is designing this such that it is usable without computation devices. A simple (bad) method would e.g. be to use a different secret as mac depending on how many words the message has.

  Maybe, like others have said, it is only feasible to have a different MAC depending on if the message conveys all-clear/emergency.
  ```

- u/ConscientiousPath:
  ```
  I haven't read that, but the easy answer to MITM attack is asymmetric encryption--even in a fantasy setting. Your encryption algorithms might be much more rudimentary in settings without computers, but the same principle--that a MITM can't decrypt/read messages and therefore can't make believable replies--still applies.
  ```

- u/clawclawbite:
  ```
  One time pads. As long as the ends are not corrupted, a one use cypher hides the message and confirms the other person has access to it. Slower, but fine for ok check-ins.
  ```

- u/fljared:
  ```
  Talk in a language that the MTM can't speak, and use that, ala the Navajo Code talkers. 

  There's a lot of ways for Silvenia to get around this- for instance, by learning the language, or capturing a speaker and using them as a translator. 

  It also requires having such a speaker in each unit, and the more there are, the easier it would be for one to be captured or the language identified.
  ```

  - u/Luminous_Lead:
    ```
    That would be pretty unconventional for the Innverse, given that there's one primary verbal language(English) and *maybe* one ethnic group that might speak something different.  Some of the multilingual isekai'd might be able to pull off a code talker act but but they're not exactly commonplace.
    ```

- u/Cantih:
  ```
  There's actually a Pen & Paper RPG that has this stuff as a focus, Cryptomancer. Might find something there.
  ```

- u/Luminous_Lead:
  ```
  Because [Message] is inherently vulnerable to interception, I seem to remember one character coming up with some kind of morse-code/colour code.
  ```

  - u/None:
    ```
    [removed]
    ```

    - u/Luminous_Lead:
      ```
      Yeah, that's the one. I was trying not to name names but it happens relatively early in the story.
      ```

---

