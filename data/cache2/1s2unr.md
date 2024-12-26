## Spoiler tags!

* Author: u/None *
* URL: https://www.reddit.com/r/rational/comments/1s2unr/spoiler_tags/
* Score: 9

* Created: 2013-12-04T14:23:04

### Post:

We use the same system as on /r/HPMOR, so [context for spoiler] plus (#s "spoiler goes here") gives [context for spoiler](#s "spoiler goes here"). It shows the spoiler if you hover, and works on mobile. Let me know if you have any critiques.

ETA: It's 100% fixed now; thanks again for all of your help everyone!

### Comments:

> **u/None** [+3]  (35 minutes later)
> 
> It doesn't look like /r/HPMOR. There's a big blank space where we should be seeing "context for spoiler".

>> **u/None** [+1]  (41 minutes later)
>> 
>> Huh. Works for me! I'll try in a different browser, see if I can replicate what you're talking about.

>>> **u/None** [+3]  (an hour later)
>>> 
>>> [removed]

>>>> **u/bbrazil** [+2]  *NERV* (2 hours later)
>>>> 
>>>> Ditto in chrome.

>>>>> **u/None** [+1]  (4 hours later)
>>>>> 
>>>>> I see. Bb, you mod /r/hpmor; care to share the code? Since the one I'm using obviously isn't perfect, despite coming from /r/modhelp...

>>>>>> **u/bbrazil** [+2]  *NERV* (4 hours later)
>>>>>> 
>>>>>> You can look at any subreddit's stylesheet: http://www.reddit.com/r/hpmor/about/stylesheet

>>>>>> **u/noking** [+2]  (4 hours later)
>>>>>> 
>>>>>> I would guess you need to set the colours. Look at r/HPMOR's stylesheet, as bbrazil said, and fiddle with the colours in the different sections to see which is the right one. Looks like at the moment it's white text on a white background.

>>>>>>> **u/None** [+1]  (6 hours later)
>>>>>>> 
>>>>>>> Sounds good... Maybe when I'm not on mobile.

>>>>>>>> **u/None** [+1]  (21 hours later)
>>>>>>>> 
>>>>>>>> It kinda got worse. Now I can't even read the spoilered text.
>>>>>>>> 
>>>>>>>> Tried it on a Mac OS X Lion and on a Windows 8.1, with Chrome, Safari and Firefox. Same result on all combinations.

>>>>>>>>> **u/None** [+1]  (22 hours later)
>>>>>>>>> 
>>>>>>>>> Goddamn!

>>>>>>>>>> **u/Chronophilia** [+3]  *sci-fi ≠ futurology* (23 hours later)
>>>>>>>>>> 
>>>>>>>>>> As of this post, I think you can get /r/HPMOR's behaviour by replacing
>>>>>>>>>> 
>>>>>>>>>>     a[href="#s"] {
>>>>>>>>>>         visibility: hidden;
>>>>>>>>>>         display: inline-block
>>>>>>>>>>     }
>>>>>>>>>> 
>>>>>>>>>> with
>>>>>>>>>> 
>>>>>>>>>>     a[href="#s"] {
>>>>>>>>>>         display: inline-block;
>>>>>>>>>>         background: black;
>>>>>>>>>>         color: white;
>>>>>>>>>>         padding: 0px 0px 0px 10px;
>>>>>>>>>>     }
>>>>>>>>>> 
>>>>>>>>>>     a[href="#s"]:hover {
>>>>>>>>>>         color: #8F8F8F;
>>>>>>>>>>     }

>>>>>>>>>>> **u/colorcodebot** [+2]  (23 hours later)
>>>>>>>>>>> 
>>>>>>>>>>> I've detected a hexadecimal color code in your comment. Please allow me to provide visual representation. 
>>>>>>>>>>> [#8f8f8f](http://color.re/8f8f8f.png) 
>>>>>>>>>>> ***
>>>>>>>>>>> [^^Learn ^^more ^^about ^^me](http://color.re) ^^| ^^Don't ^^want ^^me ^^replying ^^on ^^your ^^comments ^^again? ^^Respond ^^to ^^this ^^comment ^^with: ^^'colorcodebot ^^leave ^^me ^^alone'

>>>>>>>>>>> **u/None** [+1]  (a day later)
>>>>>>>>>>> 
>>>>>>>>>>> Thanks! I made the change; can anyone see if it works?

---

