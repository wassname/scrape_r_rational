## Is it possible to find a collection of Gwern's essays in an epub format?

* Author: u/raymestalez *
* URL: https://www.reddit.com/r/rational/comments/dj7zc5/is_it_possible_to_find_a_collection_of_gwerns/
* Score: 8

* Created: 2019-10-17T15:28:47

### Post:

[removed]

### Comments:

> **u/traverseda** [+8]  *With dread but cautious optimism**
> 
> Sure: https://drive.google.com/file/d/1lFpQz8bDtDP-TL1N9fTtCWoEA5fJ1L36/view?usp=sharing
> Converted with `: foreach *.html |> pandoc --toc -s "%f" -o "%o" |> %B.epub` and tup. Hopefully that works for you. Comes in to about 66M.
> 

>> **u/raymestalez** [+2] *
>> 
>> Thank you so much, this is perfect!
>> 

> **u/Escapement** [+2]  *Ankh-Morpork City Watch**
> 
> If you download e.g. his page on Modafinil and then use Calibre to convert the .html to .epub with entirely default settings with no work whatsoever, the .epub document you get as a result is poorly optimized and looks like actual garbage but is still mostly readable; hilariously the .epub looks better in Moon+ reader than Calibre's built in e-pub viewer. No clue how it would look on whatever software your tablet uses. The embedded equations don't look good at all and may be very difficult to fix though?
> You could probably make each essay look a lot better if you put work into configuring things to actually adapt the formatting better. Calibre's [ebook-convert](https://manual.calibre-ebook.com/generated/en/ebook-convert.html) has a command-line interface so you could batch download a bunch of his site with e.g. wget and then run them all through a ebook-convert command that you've customized to make Gwern's essays come out better.
> 

> **u/alexanderwales** [+1]  *Time flies like an arrow**
> 
> This would be a much better question for e.g. /r/gwern, or for the Friday Off-Topic thread (if you haven't already gotten an acceptable answer).
> 

---

