
from praw.models import Comment, Submission

post_fields = ('id', 'title', 'permalink', 'score', 'created_utc', 'num_comments', 'permalink', 'selftext', 'is_self', 'author_flair_text', 'upvote_ratio')
comment_fields = ('id',  'score', 'created_utc', 'body', 'permalink', 'author_flair_text')

def comment_to_json(comment):
    d =  {k: v for k, v in comment.__dict__.items() if k in comment_fields}
    d['author'] = comment.author.name if comment.author is not None else None
    return d

def submission_to_json(submission: Submission) -> dict:
    post_json = {k: v for k, v in submission.__dict__.items() if k in post_fields}
    post_json['comments'] = [comment_to_json(x) for x in submission.comments.list()]
    post_json['author'] = submission.author.name if submission.author is not None else None
    return post_json
