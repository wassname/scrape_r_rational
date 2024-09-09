## How do I search for all youtube links in r/rational?

### Post:

\`url:youtube subreddit:rational\` gets me only top-level posts, not links in comments. Any ideas?

### Comments:

- u/Veedrac:
  ```
  If it's important enough to put in the effort, sign up to the Google Cloud Platform free tier, and run

      SELECT *
      FROM `fh-bigquery.reddit_comments.2019*`
      WHERE subreddit = 'rational'
      AND body LIKE '%youtube.%';

  Note that you might also need to search for the shortened `youtu.be`.

  Unlike most forms of searching, this is fairly exhaustive, but comes with no sort of ranking and requires exact search terms. It's also missing some more recent data.
  ```

- u/Do_Not_Go_In_There:
  ```
  Try googling `site:https://www.reddit.com/r/rational/ youtube`
  ```

  - u/Mezsch:
    ```
    Is there a way to search for last years results? Like "date:2019" or sth
    ```

    - u/Amagineer:
      ```
      Hit the "Tools" button/text just to the lower right of the search bar. It'll add a dropdown menu where you can select a time range.
      ```

    - u/Roneitis:
      ```
      Under Tools you can specify a date range
      ```

  - u/Amargosamountain:
    ```
    You mean "site:https:// www. reddit .com/r /rational/ YouTube" (without spaces or quotes) since Google doesn't know r/ links and FUCK I can't get it to display right 

    How did you do red text?
    ```

    - u/redaliman:
      ```
      “site:reddit.com/r/rational youtube“
      ```

    - u/Amagineer:
      ```
      In old reddit/markdown mode, you wrap the text in backticks \`like this\` to produce text `like this`. With the new reddit "fancypants editor", you hit the "inline code" button (which looks like </>) to style the text as you would with bold or italics.
      ```

- u/Uristqwerty:
  ```
  There's always [pushshift](https://redditsearch.io/). I believe it's run by the same guy as the google cloud dataset mentioned above, but as it's a web UI more like a classic advanced search page and doesn't require a google account, it might be more approachable for a one-off query with a reasonable output size that you don't care to export for later re-use.
  ```

---

