## URGENT: Be Advised; FFN Profiles compromised and may carry Javascript Exploit.

* Author: u/eternal-potato  *he who vegetates**
* URL: https://forums.spacebattles.com/threads/urgent-be-advised-ffn-profiles-compromised-and-may-carry-javascript-exploit.692300/
* Score: 32

* Created: 2018-10-22T08:28:57

### Post:

[Link to content](https://forums.spacebattles.com/threads/urgent-be-advised-ffn-profiles-compromised-and-may-carry-javascript-exploit.692300/)

### Comments:

> **u/eaglejarl** [+7]  (a day later)
> 
> For some time now I've been recommending using any site other than FFN for publishing.  My personal recommendation is [SufficientVelocity.com](https://SufficientVelocity.com), although check the TOS if you're going to be posting mature content.
> 
> IMO, FFN has the following pros:
> 
> * Large readership
> * Really detailed and interesting stats about your readership
> 
> It has the following cons:
> 
> * Non-responsive admins
> * It will mangle your text, including:
>    * No links allowed.  
>    * No use of the word 'Patreon' allowed
>    * No use of the word 'Kickstarter' allowed (I might be wrong about this one)
> * You cannot copy/paste from the page, because they have javascript that disables that
> * If you disable javascript so that you can copy/paste, you will find that everything is centered
> * It is not possible to reply to a review inline, only via PM.  This means that: 
>    * You cannot develop a mutually-interacting community among your readership\[1\] 
>    * Future readers cannot see your response to reviews
>    * You cannot reply to guest reviews
> * Screenplay format is a violation of TOS, which is annoying because screeplay is an excellent format for parody
> * You cannot edit reviews that you leave
> * You cannot review a given chapter more than once, so if you submit a review and then want to add something, or if you re-read something a year later...too bad!
> * The interface for uploading/updating chapters is absolute shite.
> * When you update a chapter it does not actually show the changes for an indeterminate period of time.
> 
> \[1\] FFN actually does have a 'community' feature, but it requires taking a positive action to create, then readers have to actively join it, and there's no direct access from the story to the community.

>> **u/SimoneNonvelodico** [+7]  *Dai-Gurren Brigade* (2 days later)
>> 
>> While FFN has limitations and this exploit is bad news, I really don't think a forum like Sufficient Velocity can come close to even approximating the same functionality. The forum format is horrible for writing and reading fanfiction, it comes with a lot of distractions, fragments the content interspersing it with the comments/answers and is hard to parse out. FFN has a smartphone app and there's a complimentary site that compiles EPUB and MOBI files out of a given fanfiction, that's a lot of convenience right there. Archive Of Our Own if anything would be the only alternative that's really even in the same ballpark.

>>> **u/eaglejarl** [+4]  (2 days later)
>>> 
>>> Press the "Reader mode" button on SV and it will show you only the story posts without the discussion.
>>> 
>>> Reading SV in your phone browser works fine -- it's quite mobile friendly. I see zero value add from a specialized app and noticeable downside.
>>> 
>>> Parsing SV is pretty trivial; I've done it.
>>> 
>>> If you want offline-readable versions, your browser comes with a "download" button, so the fact that it's not epub or mobi carries no water with me.
>>> 
>>> Maybe you have some specialized workflow that isn't met, but I stand by my statement: aside from the question of stats, SV is strictly superior to FFN.

>>>> **u/Croktopus** [+4]  (3 days later)
>>>> 
>>>> ive really been enjoying ao3, from the perspective of a casual reader that just wants shit to be simple and easy

>>>>> **u/eaglejarl** [+2]  (4 days later)
>>>>> 
>>>>> AO3 is a great site, and I recommend it. It's a fine publishing platform, probably my #2 choice behind SV.
>>>>> 
>>>>> Actually, now that I think about it, I should look into Royal Road. They have one killer feature for an author, which is that they make it easy to monetize by including Patreon links directly into the chapters for you. I'm not sure about the rest of their functionality, though.

>>> **u/kraryal** [+1]  (2 days later)
>>> 
>>> Sufficient Velocity has "reader mode" now, which removes all non-story content from the thread. It's very nice.

>> **u/ToaKraka** [+2]  *https://i.imgur.com/OQGHleQ.png* (4 days later)
>> 
>> > You cannot copy/paste from the page, because they have javascript that disables that
>> 
>> It's CSS, not Javascript. You can easily override it by adding `div.nocopy{user-select:text!important;}` to your custom CSS in [Stylus](https://chrome.google.com/webstore/detail/stylus/clngdbkpkpeebahjckkjfobafhncgmne). Even without custom CSS, there's nothing stopping you from simply copying text directly from the code of the page (in Chrome, press Ctrl-U).

>>> **u/eaglejarl** [+1]  (4 days later)
>>> 
>>> Ah, the people of assumption! Thanks for letting me know. 
>>> 
>>> I note that I'm confused, though -- when I turned off JavaScript I was able to copy from the page. I hadn't realized that doing so changed anything about the CSS. Weird.
>>> 
>>> And yes, I'm aware that I can copy from the source. That's not the point; I shouldn't needed to apply workarounds for such basic functionality, and they shouldn't disable such unless they can do so effectively.

>>>> **u/ToaKraka** [+2]  *https://i.imgur.com/OQGHleQ.png* (4 days later)
>>>> 
>>>> > when I turned off JavaScript I was able to copy from the page. I hadn't realized that doing so changed anything about the CSS. 
>>>> 
>>>> Presumably, the page's CSS is the default "copying allowed", but the site's Javascript changes the CSS to "no copying allowed" when you load the page. However, your browser's custom CSS can change it back to "copying allowed".

> **u/Sailor_Vulcan** [+7]  *Champion of Justice and Reason* (6 hours later)
> 
> could someone please explain why it isn't safe to look at the profiles? I didn't quite understand that part.

>> **u/SimoneNonvelodico** [+17]  *Dai-Gurren Brigade* (6 hours later)
>> 
>> Basically, someone found a way to inject a virus of sorts in the profile bios. The virus is JavaScript, aka it runs in your browser when you open the page, and it instantly adds itself to *your* bio (plus does a few other things). Now the problem is, there's a message inside the virus that suggests it's just someone trying to show off this exploit as a way to tell the admins to fix it. Which if true is the best scenario, but it STILL means that they need to fix it, and apparently FictionPress admins are just sleeping on this. I can confirm their Twitter has said nothing yet.

>>> **u/CouteauBleu** [+7]  *We are the Empire.* (11 hours later)
>>> 
>>> Well, worst case scenario, the attacker can affect your fanfiction.net data and pretty much nothing else. (eg they can't access your non-ffnet passwords or bank credentials or whatever)
>>> 
>>> So I wouldn't completely freak out. But yeah, FictionPress sucks.

>>>> **u/SimoneNonvelodico** [+4]  *Dai-Gurren Brigade* (a day later)
>>>> 
>>>> Well, a number of people may recycle their password, for example. Hopefully not on their bank accounts, for which you should definitely use a unique one (and also any good bank should give you additional layers of security), but you never know.

>>>>> **u/nicholaslaux** [+2]  (2 days later)
>>>>> 
>>>>> Just to clarify - access to javascript and the ability to perform actions on your behalf on FFN indicate that it's highly unlikely that the attacker would be able to gain access to your password, since that isn't actually used/accessed by JS during non-authentication tasks.
>>>>> 
>>>>> Worst-case scenario (in terms of potential damage) would involve the attacker sending a copy of your session cookie to a remote drop, in order to imitate anyone they want. However, to foil this, even if you've been affected, all you would need to do is... log out, and log back in again, without viewing the virus a second time.
>>>>> 
>>>>> For authors, there's a higher risk of malicious code automagically deleting all of your stories or something similar, but otherwise, it's best not to overstate the possible risks without cause, so that when larger incidents do happen, people don't underreact to them.

>>>>>> **u/SimoneNonvelodico** [+2]  *Dai-Gurren Brigade* (2 days later)
>>>>>> 
>>>>>> Yeah, I couldn't figure out a specific way to steal the *password* unless it somehow tricks you into re-inputting it and keylogs it. But you never know, and there may be actions in your profile which require you to confirm your password.

> **u/oliwhail** [+4]  *Omake-Maximizing AGI* (16 hours later)
> 
> u/Velorien , u/eaglejarl
> - just in case, might be good to check?

>> **u/Ardvarkeating101** [+2]  *Father of Learning* (18 hours later)
>> 
>> and /u/boomvroomshroom

>>> **u/None** [+6]  (22 hours later)
>>> 
>>> [deleted]

>>>> **u/Ardvarkeating101** [+2]  *Father of Learning* (a day later)
>>>> 
>>>> <3 baby

> **u/trambelus** [+3]  (10 hours later)
> 
> I'll copy what I said on the SB thread.
> 
> If you think you might have been affected by this exploit, **go to your account settings immediately** and look at your backup email addresses. If there's anything there you don't recognize, get rid of it right now, and you should be fine. If your own email address is missing, re-add it. It might also be a good idea to change your password, just to be safe.

>> **u/Sailor_Vulcan** [+1]  *Champion of Justice and Reason* (15 hours later)
>> 
>> is there a way to tell without looking at one's own profile?

> **u/GhostWriter52025** [+3]  (14 hours later)
> 
> Could a mod please sticky this or something? Seems rather important for this community.

>> **u/alexanderwales** [+7]  *Time flies like an arrow* (17 hours later)
>> 
>> Done. I really thought that the turn-around time for this would be a lot faster, but apparently not.

>>> **u/Ardvarkeating101** [+7]  *Father of Learning* (18 hours later)
>>> 
>>> First time dealing with FF.net issues?

>>> **u/GhostWriter52025** [+1]  (a day later)
>>> 
>>> Thanks! And yeah, it's going well past laziness and soaring in the clouds of pure negligence at this point.

> **u/alexanderwales** [+1]  *Time flies like an arrow* (3 days later)
> 
> [Per FictionPress Twitter:](https://twitter.com/FictionPress/status/1055293042092109827)
> 
> > We have plugged the current known attack vector which combined csrf attacks with a html injection bug within the user profile page when access via a web browser. App users are not effected. A security review of the entire system is underway.
> 
> I'll leave this here for another few days, then remove this announcement if there are no further updates.

> **u/Teulisch** [+1]  *Space Tech Support* (7 hours later)
> 
> that sounds bad... so, malicious code huh?

> **u/dinoseen** [+1]  (a day later)
> 
> Are we fine if we don't have a FFN account?

>> **u/SimoneNonvelodico** [+1]  *Dai-Gurren Brigade* (2 days later)
>> 
>> Should be safe, yes.

---

