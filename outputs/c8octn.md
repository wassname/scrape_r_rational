## Unsong Easter Egg Spoiler Log (Finally) Released!

### Post:

[Link to content](https://unsongbook.com/tosefta/)

### Comments:

- u/None:
  ```
  [deleted]
  ```

  - u/fubo:
    ```
    Since this is the spoiler thread, I'll point out this little bit of code lives about two-thirds down in this file:

    https://bakkot.github.io/SlateStarComments/ssc.js

    (For those who speak even less JavaScript than me: It goes through the HTML structure of the page, finds instances of either spelling in the text, then for each one it picks one spelling or the other half the time.)
    ```

    - u/SeekingImmortality:
      ```
      That's fantastic.
      ```

    - u/Crimethinker:
      ```
      Specifically this chunk of code:

          if(location.host==='unsongbook.com'){(function(){var n,walk=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT,null,false);
          while(n=walk.nextNode())
              n.textContent=n.textContent.replace(/Berenst(a|e)in/g,function(m){
                  return Math.random()<.1?m:(Math.random()<.5?'Berenstain':'Berenstein');
              }).replace(/BERENST(A|E)IN/g,function(m){
                  return Math.random()<.1?m:(Math.random()<.5?'BERENSTAIN':'BERENSTEIN');
             });
          }());}

      which randomly picks between `BERENSTAIN` and `BERENSTEIN`
      ```

  - u/lumenwrites:
    ```
    I don't know if you're aware of this, but there's a fascinating conspiracy theory based on that - https://old.reddit.com/r/MandelaEffect/

    A bunch of people believe we crossed over to a parallel universe because their memories about stuff like Berenstain Bears don't match the reality.

    >  The Mandela Effect. The theory states that shared false memories are in fact glimpses into parallel worlds with different timelines and was named by writer and "paranormal consultant" Fiona Broome based on the fact that thousands of people apparently remember Nelson Mandela dying in prison in the '80s despite having been released from prison in 1990 and going on to become president of South Africa. Mandela didn't actually pass away until 2013.
    ```

- u/jimbarino:
  ```
  > After I published this chapter I got an email from a reader who lived in Palo Alto in a group house called Ithaca and who was really freaked out and wanted to know if I was writing about her. I had to convince her it was just a coincidence.

  lol
  ```

- u/Shemetz:
  ```
  The name of Magdebuena was probably supposed to be Maduegbuna, and is taken from [this great list](http://www.babynology.com/nigerian_babynames.html), which he [reblogged](http://slatestarscratchpad.tumblr.com/post/120974740041/very-strangely-translated-nigerian-baby-names) at some point.
  ```

---

