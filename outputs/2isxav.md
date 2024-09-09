## [Q] Formatting stories - any good evidence?

### Post:

I've started toying around with setting up my story at its permanent website, and have put a test page of the first chapter at [this page](http://www.datapacrat.com/SI/01-01.html) (NSFW due to image of tasteful female nudity). I find myself faced with all sorts of options - font? line width? dark on light or light on dark? inline style or CSS? spot colors? hyphens or em-dashes? straight or curly quotes? etc, etc? - and I don't have a lot of evidence to base any answers on.

As a preliminary set of answers, I've drawn on [Butterick's Practical Typography](http://practicaltypography.com/), even though I don't have any particular reasons to favour that set of advice over any other, other than that it's a concentrated dose of a /lot/ of advice. I don't know how to set up formatting for multiple viewing devices, I've never touched CSS, and my budget for fonts or professional advice is pretty much zero.

Does anyone reading this know where I can find evidence that any changes I could make to my preliminary formatting would do any better than what I already have?

### Comments:

- u/None:
  ```
  I like it so far. Butterick is a fantastic source, and it's good to see someone else using it. But about that picture at the top ... Does it really belong at the top? Or does another picture work? I know it's relevant (sorta), but not gonna lie, when I saw it my first reaction was to roll my eyes and move to close the tab. It was only when I saw the url that I stopped and scrolled.

  Or maybe I'm just unfairly prejudiced against furries, or something. [I'll review my biases.](https://www.reddit.com/r/LessWrongLounge/comments/2itef3/time_for_spiders_freedom_of_identity/)
  ```

  - u/DataPacRat:
    ```
    The only other image I have that's suitable for the beginning is http://www.datapacrat.com/SI/SI-cover-page.png , which I'm planning on putting on the index/table-of-contents page instead of the first chapter.

    I could certainly move the image down a few sections, such as to shortly after the brain transplant, if having it at the /very/ start is that off-putting.
    ```

    - u/_brightwing:
      ```
      I didn't see the first version, but that works great thematically. Right at the end of the section when he faints seeing the mass of fur. Very much adds to the hilarity of the moment. Sets precedent for future illustrations too.  

      Liking the triangle theme of the title as well. Looks nice and minimalistic. Consider changing  “Book One: Re- / Chapter One: Re-Awakening” to a slightly lighter shade of blue though. Maybe colour #0162e1 ? It looked alright in photoshop when I messed around with a screenshot of yours..

      If you're looking into heading font choices, Tahoma, Cambria or Georgia could go well with the Calibri body text. It's fine as it is though. And for some reason authors I find always use a very dark shade of grey like #0f0f0f instead of plain black. Must be an aesthetic thing.

      Oh, I found [this bookmarklet](http://www.fount.artequalswork.com/) the other day. Something if you wanted to identify font structures in places that particularly caught your eye. Hope you find it useful.
      ```

      - u/DataPacRat:
        ```
        You're not the only one who's suggested lightening the title; so I have.

        For fonts, I've used [this list](http://cssfontstack.com/) as listing fonts that are most likely to exist on a user's system, sorted by [this list](http://practicaltypography.com/system-fonts.html) for which are to be preferred; and at least for the moment, am trying out Cambria for the headers (with Georgia as a fallback).
        ```

- u/qznc:
  ```
  Butterick's advice about buying your own font seems weird to me. Especially, since he is selling fonts himself. I never saw the need to buy a font. There is nothing wrong with standard fonts.

  In your concrete case, I'd say increase line-height or decrease the width of lines. Are lines like "First Awakening" considered section titles? Then you should style them somewhat differently than the main text. Maybe center or right align or italic.

  Another nice resource: http://webtypography.net/
  ```

- u/i_dont_know:
  ```
  Dark blue text on a black background (your chapter titles) is generally inadvisable. When I'm reading a story, I tend to prefer dark text on a lighter background, but there are plenty of scripts that will allow people to have the option.

  I'm glad that you don't have the nude furry picture at the top of the page. I might hide the picture by default and have a "click here to see NSFW picture" where the picture should go in the text, and have some javascript show the picture.

  For typography, *please do* use hyphens, em-, and en-dashes correctly. If you use a hyphen where an em-dash should be, on first read-through I will often read it as a hyphenated word, and it will take me a moment to realize that there should be a break in the sentence—confusing!

  [Here's a good reference on the different types of dashes](http://alistapart.com/article/emen/#section5)

  I prefer to write in pandoc-styled markdown, then use the cross-platform, free, and absolutely amazing [pandoc](http://johnmacfarlane.net/pandoc/) utility to convert to [practically any format under the sun](http://johnmacfarlane.net/pandoc/README.html), including html and epub. Pandoc even supports custom templates for all of its output file formats!

  When using pandoc, I use the `-S` (uppercase S) or `--smart` flags (they're the same) which:

  > Produce typographically correct output, converting straight quotes to curly quotes, --- to em-dashes, -- to en-dashes, and ... to ellipses.

  Writing in markdown means writing in plaintext, which means that I am not tied to a proprietary or closed-source application. It's safer even than ODF in that I expect computers will still be able to read the same `.txt` file 10 years from now, with no loss of fidelity! I can also manage my story through source control such as git, out of which I get versions and (free) backups through github if I want them.

  Anyway, that's my advice—thanks for writing!
  ```

---

