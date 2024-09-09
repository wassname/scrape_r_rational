## Help in Finding a Story

### Post:

Does anyone remember a story from royalroadl.com that was posted a few times here? It was about a Virtual Reality where the main character is trying to develop nature affinity by living in the wilds as a bear beastman.

I already tried asking people in the Off Topic Friday Thread, but nobody who responded knew. I couldn't find it by using the search bar in the top right corner of the subreddit and tried Googling for it. So now I'm asking the subreddit at large.

The author of the story actually posted it here himself (I remember the name being masculine), and I think the main character is named Charlie, Chuck, or some other name starting with 'Ch'.

Thanks!

### Comments:

- u/alexanderwales:
  ```
  Probably [Wanderlust](http://royalroadl.com/fiction/3670) by /u/Lunitan?

  The secret to finding it was querying every single instance of royalroadl in the comments of /r/rational with Google's BigQuery. Google searches through the text, not the links, and the naked link was never posted, so there wasn't any other way to find it.

      SELECT
        *
      FROM
        [fh-bigquery:reddit_comments.2015_10] a
      WHERE
        a.subreddit='rational'
        AND a.body CONTAINS 'royalroadl'
      LIMIT
        1000
  ```

  - u/Kuratius:
    ```
    This is the sort of meta-knowledge about search engines I'd like to learn more about. 

    Do you know of any resources where I can learn more about this?
    ```

    - u/alexanderwales:
      ```
      This is database stuff, not search engine stuff. All Reddit comments are scraped and stored in Google's BigQuery ([What is BigQuery?](https://cloud.google.com/bigquery/what-is-bigquery)), which is a cloud solution for extremely large datasets. You can see [here](https://www.reddit.com/r/bigquery/comments/3cej2b/17_billion_reddit_comments_loaded_on_bigquery/) for more information and some examples of the neat stuff you can do with it. (Seven months ago [I queried up a list of everyone who had ever commented, along with some fun stats.](https://www.reddit.com/r/rational/comments/3kjt60/d_friday_offtopic_thread/cuxyvle))

      If you want to do neat stuff like this, you need to learn SQL (Simple Query Language) which is super useful for lots of stuff related to programming and datasets. If you want to learn that, [w3schools has a pretty long tutorial with the ability to try it yourself](http://www.w3schools.com/sql/) and [Khan Academy has an intro to SQL](https://www.khanacademy.org/computing/computer-programming/sql), both are good places to gain more knowledge.
      ```

- u/wtfbbc:
  ```
  [This will hopefully help narrow it down](https://www.reddit.com/domain/royalroadl.com/)
  ```

---

