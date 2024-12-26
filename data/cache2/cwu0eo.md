## [Meta] WARNING, the Practical guide to evil site has been infected with malware.

* Author: u/LordSwedish  *Q Continuum**
* URL: https://www.reddit.com/r/rational/comments/cwu0eo/meta_warning_the_practical_guide_to_evil_site_has/
* Score: 127

* Created: 2019-08-29T01:22:02

### Post:

There's a link regarding tragic news about the site operator instead of the story text, according the the PGTE discord, this link will infect your computer with malware.

EDIT: It now appears that EE has regained control and has fixed the issue. The only way of getting malware was through clicking a link and that link is now gone, and the chapters have been restored. If you click on strange links that start auto-downloading files for you, do not open them. 

PS, not sure if I should delete this now or if mods want to put a "solved" mark or something on it.

### Comments:

> **u/boomfarmer** [+35]  *Trying to be helpful* (an hour later)
> 
> Wait, isn't PGTE a WordPress.com site? This sounds like either a hack of the author's account or some form of XSS attack in a plugin on the site.

>> **u/lolbifrons** [+19]  *Fifteenth Legion of Terror* (15 hours later)
>> 
>> Wordpress is notoriously vulnerable to all kinds of shit.  One of our units in my pentesting class was just about hacking wordpress.

> **u/Robert_Barlow** [+21]  (an hour later)
> 
> I don't know if this is a well known piece of malware, but googling the phrase "tragic news about the site operator" gives links to [this website](http://www.beststoryinevertold.com/) which seems to have been infected by the same thing - same link, same text, same warnings apply. Nothing else turns up with that exact phrase, and I'm not familiar enough with Wordpress history in order to know if something similar has happened to other blogs in the past.

> **u/xartab** [+15]  (14 hours later)
> 
> I swear for a moment there I thought you meant a memetic hazard. You can never tell on this subreddit.

>> **u/Frommerman** [+9]  (a day later)
>> 
>> Viruses are memetic hazards for computers.

>>> **u/xartab** [+6]  (a day later)
>>> 
>>> Every copy you make becomes an instance of the thing. Like the Angels.

> **u/TaltosDreamer** [+5]  (an hour later)
> 
> Sadness 😭
> I hope they are able to recover safely.
> 
> Do we know which virus for innoculation purposes?

>> **u/red_adair** [+10]  *{{explosive-stub}}* (an hour later)
>> 
>> Weird thing is, Virustotal doesn't think it's a virus (yet): https://www.virustotal.com/gui/url/b5d50086b6bef904b09621d75af2990e04db741059c3e71f4705629b2f0cdb5f/detection

>>> **u/red_adair** [+19]  *{{explosive-stub}}* (an hour later)
>>> 
>>> Update: Kaspersky thinks it's a virus now.

>>> **u/TaltosDreamer** [+3]  (an hour later)
>>> 
>>> I heard the french just took down an 850k botnet. I wonder if it's connected to them. It makes sense the perpetrators would create something new and branch out.

>>>> **u/red_adair** [+14]  *{{explosive-stub}}* (2 hours later)
>>>> 
>>>> When you say things like "I heard ....", especially in tech circles, **link to your sources**.

>>>>> **u/Slinkinator** [+14]  (2 hours later)
>>>>> 
>>>>> Well, it's been on the BBC for more than 12 hours, so it's not like, niche news
>>>>> 
>>>>> I mean, if anything I thought it was a bit inane to refer to it as of it wasn't heavily reported international news.

>>>>>> **u/red_adair** [+4]  *{{explosive-stub}}* (14 hours later)
>>>>>> 
>>>>>> Anecdotally: it didn't pierce my filter bubble, because I mostly read US news, and it looks like the story didn't hit the English-speaking press until after I had already checked the news for the day.
>>>>>> 
>>>>>> Speaking more generally: If you link to the news, you both help pierce other people's filter bubbles, provide a resource where people can go to learn more, and you refresh your own knowledge of the news.
>>>>>> 
>>>>>> Anyways, here's a detail-full news article, for people who have yet to read about it: https://thehackernews.com/2019/08/retadup-botnet-malware.html
>>>>>> 
>>>>>> I don't think this malicious .doc file is related to the RETADUP network, because:
>>>>>> 1. VirusTotal [initially reported](https://www.reddit.com/r/rational/comments/cwu0eo/meta_warning_the_practical_guide_to_evil_site_has/eyfc7qa/) that no antivirus detected the .doc file as malicious, which would not be the case for a known virus
>>>>>> 2. The server hosting the .doc is located in .ru netspace, not in France or the USA, which is the case with RETADUP's known command-and-control infrastructure.
>>>>>> 
>>>>>> But those are weak assertions.

>>>>>> **u/TaltosDreamer** [+0]  (4 hours later)
>>>>>> 
>>>>>> I assumed people were perfectly capable of figuring it out and that most people had heard of it.

>>>>> **u/TaltosDreamer** [+3]  (4 hours later)
>>>>> 
>>>>> Tech circles? Interesting way to refer to a discussion group about fiction.

>>>> **u/Lugnut1206** [+3]  (an hour later)
>>>> 
>>>> i'm gonna vote firm coincidence on that, unless "the french" has some deeper, PGTE-specific meaning i'm unaware of

>>>>> **u/Academic_Jellyfish** [+4]  (2 hours later)
>>>>> 
>>>>> EE is from France. Still a decent chance it's unrelated though.

>>>>>> **u/CouteauBleu** [+5]  *We are the Empire.* (20 hours later)
>>>>>> 
>>>>>> I thought he was from Quebec?

>>>> **u/red_adair** [+2]  *{{explosive-stub}}* (2 hours later)
>>>> 
>>>> I care less about attribution and more about:
>>>> 
>>>> 0. taking down the malware server
>>>> 1. securing affected accounts
>>>> 2. restoring compromised sites
>>>> 
>>>> It doesn't look like any of the attacks from today's WordFence compromise list https://www.wordfence.com/blog/2019/08/malicious-wordpress-redirect-campaign-attacking-several-plugins/ so I'm guessing someone guessed EE's password.
>>>> 
>>>> Always use unique per-site passwords, and enable 2FA when possible.

>>>>> **u/TaltosDreamer** [+2]  (4 hours later)
>>>>> 
>>>>> I would hope figuring out the particular virus would be useful since we could hunt down specific cures.
>>>>> 
>>>>> That applies to #1 and #3 on your list

> **u/None** [+3]  (2 hours later)
> 
> [deleted]

>> **u/LordSwedish** [+5]  *Q Continuum* (2 hours later)
>> 
>> The only malware comes from downloading the file from the link that has replaced the text and then presumably opening it. I don't know what browser or phone you're using or if you clicked the link so I can't say anything else.

>> **u/Academic_Jellyfish** [+4]  (2 hours later)
>> 
>> There's a download link on the table of contents and most recent few chapters. Unless you're an idiot and download the file and then open it, you should be fine. And from what I know, most viruses wouldn't work on mobile, though I'm hardly an expert on it.

> **u/ShotoGun** [+3]  (3 hours later)
> 
> Does ad block protect against the malware?

>> **u/LordSwedish** [+4]  *Q Continuum* (3 hours later)
>> 
>> I saw someone mention that it did, but mine doesn't. Unless you click the link that has replaced the text, you can't get any malware.

>> **u/MilesSand** [+2]  (20 hours later)
>> 
>> Unlikely. The only time adblock protects from malware is if the malware is being served through ad networks. As far as I remember EE never put any ad plugins on the site.

---

