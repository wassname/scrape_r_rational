## Help in Finding a Story

* Author: u/xamueljones  *My arch-enemy is entropy**
* URL: https://www.reddit.com/r/rational/comments/4fein3/help_in_finding_a_story/
* Score: 7

* Created: 2016-04-18T22:44:43

### Post:

Does anyone remember a story from royalroadl.com that was posted a few times here? It was about a Virtual Reality where the main character is trying to develop nature affinity by living in the wilds as a bear beastman.

I already tried asking people in the Off Topic Friday Thread, but nobody who responded knew. I couldn't find it by using the search bar in the top right corner of the subreddit and tried Googling for it. So now I'm asking the subreddit at large.

The author of the story actually posted it here himself (I remember the name being masculine), and I think the main character is named Charlie, Chuck, or some other name starting with 'Ch'.

Thanks!

### Comments:

> **u/alexanderwales** [+10]  *Time flies like an arrow**
> 
> Probably [Wanderlust](http://royalroadl.com/fiction/3670) by /u/Lunitan?
> The secret to finding it was querying every single instance of royalroadl in the comments of /r/rational with Google's BigQuery. Google searches through the text, not the links, and the naked link was never posted, so there wasn't any other way to find it.
>     SELECT
>       *
>     FROM
>       [fh-bigquery:reddit_comments.2015_10] a
>     WHERE
>       a.subreddit='rational'
>       AND a.body CONTAINS 'royalroadl'
>     LIMIT
>       1000
> 

>> **u/Kuratius** [+2] *
>> 
>> This is the sort of meta-knowledge about search engines I'd like to learn more about. 
>> Do you know of any resources where I can learn more about this?
>> 

>>> **u/alexanderwales** [+3]  *Time flies like an arrow**
>>> 
>>> This is database stuff, not search engine stuff. All Reddit comments are scraped and stored in Google's BigQuery ([What is BigQuery?](https://cloud.google.com/bigquery/what-is-bigquery)), which is a cloud solution for extremely large datasets. You can see [here](https://www.reddit.com/r/bigquery/comments/3cej2b/17_billion_reddit_comments_loaded_on_bigquery/) for more information and some examples of the neat stuff you can do with it. (Seven months ago [I queried up a list of everyone who had ever commented, along with some fun stats.](https://www.reddit.com/r/rational/comments/3kjt60/d_friday_offtopic_thread/cuxyvle))
>>> If you want to do neat stuff like this, you need to learn SQL (Simple Query Language) which is super useful for lots of stuff related to programming and datasets. If you want to learn that, [w3schools has a pretty long tutorial with the ability to try it yourself](http://www.w3schools.com/sql/) and [Khan Academy has an intro to SQL](https://www.khanacademy.org/computing/computer-programming/sql), both are good places to gain more knowledge.
>>> 

>>>> **u/Kuratius** [+1] *
>>>> 
>>>> So I can't use SQL queries for Google normally? That's a bit disappointing, albeit understandable.
>>>> 

>> **u/xamueljones** [+1]  *My arch-enemy is entropy**
>> 
>> That was it. Thanks!
>> 

> **u/wtfbbc** [+2] *
> 
> [This will hopefully help narrow it down](https://www.reddit.com/domain/royalroadl.com/)
> 

>> **u/xamueljones** [+1]  *My arch-enemy is entropy**
>> 
>> That's a good idea, but I have no guarentee it was posted to that subreddit. Either way, alexanderwales just found it so it's all good.
>> 

>>> **u/wtfbbc** [+1] *
>>> 
>>> That's a reddit-wide search of all royalroadl.com links submitted to any subreddit. I didn't realize it was posted in a comment 😅
>>> 

>>>> **u/xamueljones** [+1]  *My arch-enemy is entropy**
>>>> 
>>>> Oh! How do you do searching like that? I thought it was a subreddit like /r/royalroadl (which doesn't exist) or something like that.
>>>> 

>>>>> **u/alexanderwales** [+2]  *Time flies like an arrow**
>>>>> 
>>>>> https://www.reddit.com/domain/royalroadl.com/
>>>>> Will show you all of the submissions to reddit for that domain.
>>>>> So for example, if I wanted to see all submissions to my website, I would just go to:
>>>>> https://www.reddit.com/domain/alexanderwales.com/
>>>>> It's not really a search, just a chronological list.
>>>>> 

>>>>>> **u/wtfbbc** [+1] *
>>>>>> 
>>>>>> I'll add that you can see the submitted from a domain by clicking on the little gray parenthetical link after the title – for this thread, it's self.rational, which is boring, but try one at /r/news for a more interesting result.
>>>>>> 

---

