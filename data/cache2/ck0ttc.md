## I'm having trouble downloading Worth the Candle.

* Author: u/myownimaturity *
* URL: https://www.reddit.com/r/rational/comments/ck0ttc/im_having_trouble_downloading_worth_the_candle/
* Score: 14

* Created: 2019-07-31T00:38:14

### Post:

Hi, I've just mostly caught up with worth the candle, there appears to be 3 new chapters which I'm really pleased about. That said the download links on the ArchiveOfOurOwn page seem to not be working for me. I just have the endless 'Waiting for download.archiveofourown.org...' shown in the lower left. I've tried using firefox and chrome but no luck. I figured it might just be a slow download but I gave it about 15 minutes and it still hadn't started downloading. PDF and HTML works, Mobi and EPUB don't. 

I'm not sure if here is a good place to ask but I'm not sure where else to go. Thanks

### Comments:

> **u/Escapement** [+13]  *Ankh-Morpork City Watch**
> 
> From their website's [known issues](https://archiveofourown.org/known_issues#downloads):
> >Large MOBI files fail: Despite the update of our download software, some very large files with many images may still fail to download. If this happens, you might try downloading the work in another format and then converting it to MOBI.
> [Calibre](https://calibre-ebook.com/) is what I use for most of my epub/mobi/etc manipulation. It's not bad for converting from another format to e-pub or mobi.
> 

>> **u/myownimaturity** [+3] *
>> 
>> Yeah I saw that but Epub is also down. It was working for me only a few weeks ago, hopefully they'll fix it soon :)
>> 

>>> **u/nerdguy1138** [+1]  *GNU Terry Pratchett**
>>> 
>>> Fanficfare can scrape the page directly and generate its own epub, with images and formatting.
>>> 

> **u/Makin-** [+9]  *homestuck ratfic, you can do it**
> 
> I think mobi is legitimately broken for long works, but epub shouldn't be. Give it another try?
> 

> **u/None** [+4] *
> 
> Use https://github.com/kemayo/leech to get epubs from most popular story sites (even works for wordpress sites with some configuration). Then use calibre to convert between formats as needed.
> 

>> **u/myownimaturity** [+1] *
>> 
>> This is the route I went with. It was a pain to get working but I reinstalling python solved my issues. Next up, working out how to scrape Ward!
>> 

>>> **u/nerdguy1138** [+1]  *GNU Terry Pratchett**
>>> 
>>> Fanficfare for Calibre is the greatest plugin ever. It can even grab stories from your email.
>>> 

>> **u/morgf** [+1] *
>> 
>> Do you know how to use leech to only download one chapter or a range of chapters? I tried using the --offset and --limit options, but that does not seem to do what I want (it still downloaded everything).
>> 

>>> **u/None** [+1] *
>>> 
>>> I haven't used it a ton because it did exactly what I was trying to accomplish the first time. I suppose I would delete the extra stuff in calibre if leech doesn't seem to work for only 1 chapter.
>>> 

>>>> **u/morgf** [+1] *
>>>> 
>>>> I was hoping to shorten download time and reduce load on their server.
>>>> It seems like the chapter select portion of a .json file may be able to get leech to do what I want, but I do not know exactly how to do it and I cannot find any good documentation on how the .json files work with leech.
>>>> 

> **u/CraftyTrouble** [+2] *
> 
> You can use a HTML to MOBI converter. I have this one bookmarked: https://www.onlineconverter.com/html-to-mobi
> 

> **u/GET_A_LAWYER** [+1] *
> 
> It didn't work for me either.
> 

> **u/Reply_or_Not** [+1] *
> 
> You can  use chrome to make pack it into a .mobi file (and then use something like calibre to turn it into a kindle-readable .epub)
> 

---

