## [D] what is the best way to display unusual fonts like Dwarven Runes on a blog?

* Author: u/notmy2ndopinion  *Concent of Saunt Edhar**
* URL: https://www.reddit.com/r/rational/comments/3xpgja/d_what_is_the_best_way_to_display_unusual_fonts/
* Score: 0

* Created: 2015-12-21T14:37:45

### Post:

[removed]

### Comments:

> **u/alexanderwales** [+4]  *Time flies like an arrow* (19 minutes later)
> 
> Use characters that are compatible with Unicode. This will ensure that web browsers will be able to see them and ff.net will be able to display them (note that you probably want to test this to make sure ff.net *actually* supports them). Using a font file just introduces complications that makes it difficult if not impossible to translate onto the web.
> 
> [Here's the runic Unicode block.](https://en.wikipedia.org/wiki/Runic_(Unicode_block\))

>> **u/ArgentStonecutter** [+3]  *Emergency Mustelid Hologram* (29 minutes later)
>> 
>> You will probably need to provide a web font for them, since this block is not included in common web fonts, or let people know they need to install [one of these fonts](https://en.wikipedia.org/wiki/Runic_%28Unicode_block%29#Fonts).

>>> **u/alexanderwales** [+1]  *Time flies like an arrow* (4 hours later)
>>> 
>>> Segoe UI comes installed on Windows 7 (and later) and supports runic Unicode.
>>> 
>>> > ᚠ ᚡ ᚢ ᚣ ᚤ ᚥ ᚦ ᚧ ᚨ ᚩ ᚪ ᚫ ᚬ ᚭ ᚮ ᚯ ᚰ ᚱ ᚲ ᚳ ᚴ ᚵ ᚶ ᚷ ᚸ ᚹ ᚺ ᚻ ᚼ ᚽ ᚾ ᚿ ᛀ ᛁ ᛂ ᛃ ᛄ ᛅ ᛆ ᛇ ᛈ ᛉ ᛊ ᛋ ᛌ ᛍ ᛎ ᛏ ᛐ ᛑ ᛒ ᛓ ᛔ ᛕ ᛖ ᛗ ᛘ ᛙ ᛚ ᛛ ᛜ ᛝ ᛞ ᛟ ᛠ ᛡ ᛢ ᛣ ᛤ ᛥ ᛦ ᛧ ᛨ ᛩ ᛪ ᛫ ᛬ ᛭ ᛮ ᛯ ᛰ
>>> 
>>> That's the full runic alphabet (minus the eight variants) and didn't require any changes on my end to see. I think it might create problems with Mac though.

>>>> **u/omgimpwned** [+4]  *Sunshine Regiment* (4 hours later)
>>>> 
>>>> For what it's worth, I'm not seeing anything but a bunch of white boxes.

>>>> **u/HereticalRants** [+2]  (6 hours later)
>>>> 
>>>> I am on a chromebook and those characters display properly for me.

>>>> **u/ArgentStonecutter** [+1]  *Emergency Mustelid Hologram* (5 hours later)
>>>> 
>>>> Mac, Android, probably iOS and most Linux distros as well. You're basically locking out mobile completely.

>>>>> **u/Transfuturist** [+1]  *Carthago delenda est.* (7 hours later)
>>>>> 
>>>>> > most Linux distros
>>>>> 
>>>>> Works fine here.
>>>>> 
>>>>> Why exactly doesn't everyone support Unicode yet?

>>>>>> **u/ArgentStonecutter** [+1]  *Emergency Mustelid Hologram* (9 hours later)
>>>>>> 
>>>>>> OK, how are you at Ogham or Cherokee or Shavian? There's dozens of obscure languages only found in CODE2000 or Junicode.

>>>>>>> **u/Transfuturist** [+1]  *Carthago delenda est.* (9 hours later)
>>>>>>> 
>>>>>>> And? What are you saying is the difficulty? Open fonts?

>>>>>>>> **u/ArgentStonecutter** [+2]  *Emergency Mustelid Hologram* (9 hours later)
>>>>>>>> 
>>>>>>>> There's always gaps in the coverage. No platform covers all of Unicode by default.

>>>>>>>>> **u/Transfuturist** [+1]  *Carthago delenda est.* (9 hours later)
>>>>>>>>> 
>>>>>>>>> What do you mean 'platform'? Unicode is a character encoding, the data looks the same here as it does anywhere else. If it isn't displaying, the problem is the fonts and layout system. No *font* covers all of Unicode, but that's why you have different fonts for different codepoint regions. So what are you saying is the difficulty? Are the fonts available to open source not covering Unicode well? Are they not distributed widely? Do the text rendering systems not support Unicode broadly? Why are these things not already fixed?

>>>>>>>>>> **u/ArgentStonecutter** [+2]  *Emergency Mustelid Hologram* (9 hours later)
>>>>>>>>>> 
>>>>>>>>>> > What do you mean 'platform'?
>>>>>>>>>> 
>>>>>>>>>> Windows, OSX, Android, iOS, etcetera.
>>>>>>>>>> 
>>>>>>>>>> > If it isn't displaying, the problem is the fonts and layout system.
>>>>>>>>>> 
>>>>>>>>>> Yes, generally the fonts.
>>>>>>>>>> 
>>>>>>>>>> > No font covers all of Unicode, but that's why you have different fonts for different codepoint regions.
>>>>>>>>>> 
>>>>>>>>>> Which I do, and I keep adding them as I discover gaps in the default distribution on my platform. But I doubt one percent of the user base of any platform does that. They just use what's shipped by default.
>>>>>>>>>> 
>>>>>>>>>> > Are they not distributed widely?
>>>>>>>>>> 
>>>>>>>>>> They're not distributed _by default_.

>>>>>>>>>>> **u/Transfuturist** [+1]  *Carthago delenda est.* (10 hours later)
>>>>>>>>>>> 
>>>>>>>>>>> > They're not distributed by *default.*
>>>>>>>>>>> 
>>>>>>>>>>> That only makes my question of why it's not already fixed even more stupefied. Are you certain that they aren't? Xubuntu apparently does, because I can't remember the last time I saw a broken character and I don't remember installing extra fonts.

>>>>>>>>>>>> **u/ArgentStonecutter** [+1]  *Emergency Mustelid Hologram* (11 hours later)
>>>>>>>>>>>> 
>>>>>>>>>>>> > Are you certain that they aren't? 
>>>>>>>>>>>> 
>>>>>>>>>>>> By observation, the default distribution of Mac OS X, Android, and iOS do not include the runic code pages in any of their fonts. Between iOS and Android that's basically _all_ mobile platforms (Blackberry and Windows have negligible market share).

>>>>>>> **u/adiabatic** [+1]  (17 hours later)
>>>>>>> 
>>>>>>> Dunno about Ogham, but the other two are fine on iOS 9, OS X 10.11, and Windows 10.

>>>> **u/adiabatic** [+1]  (17 hours later)
>>>> 
>>>> I can see those fine on my iPhone (iOS 9) and Mac (OS X 10.11 El Capitan).

>> **u/notmy2ndopinion** [+1]  *Concent of Saunt Edhar* (4 hours later)
>> 
>> Perfect. It doesn't display anything on my iPad which is my primary reader so I think I'll use the Runic unicode and make a graphic upload too.

>>> **u/adiabatic** [+1]  (17 hours later)
>>> 
>>> Is your iPad too old for iOS 9? It looks fine here.

---

