# from https://github.dev/JosefAlbers/rd2md

from praw.models import Comment, Submission
import textwrap
import re
import pandas as pd
from datetime import datetime

def format_flair(obj):
    if obj.author_flair_text is not None:
        return f" *{obj.author_flair_text}*"
    return ""

import humanize

def format_comment(comment, depth=0, upvote_threshold=2, t0=None):
    if comment.score < upvote_threshold:
        return ""
    
    ts = pd.to_datetime(comment.created, unit='s')
    if t0 is not None:
        delta = ts - t0
        delta = humanize.naturaldelta(delta.total_seconds() )
    else:
        delta = ""

    indent = ">" * (depth+1) + " "
    author_line = f"{indent}**u/{comment.author}** [{comment.score:+}] {format_flair(comment)} ({delta} later)\n"
    dedented_body = textwrap.dedent(comment.body)
    # use re to replace multiple newlines with a single newline
    
    indented_body = textwrap.indent(dedented_body, indent)
    indented_body = re.sub(r'\n\n+', f'\n{indent}\n', indented_body.strip())
    comment_block = f"{indent}\n{indented_body}\n\n"
    formatted = author_line + comment_block
    for reply in comment.replies:
        formatted += format_comment(reply, depth + 1, upvote_threshold, t0)

    return formatted


def submission_to_markdown(post: Submission, comment_score_threshold=0, verbose=False) -> str:
    post_content = []
    post_content.append(f"## {post.title}\n\n")
    if verbose:
        ts = pd.to_datetime(post.created, unit='s')
        post_content.append(f"* Author: u/{post.author} {format_flair(post)}*\n")
        post_content.append(f"* URL: {post.url}\n")
        post_content.append(f"* Score: {post.score}\n\n")
        post_content.append(f"* Created: {ts.isoformat()}\n\n")
    post_content.append("### Post:\n\n")
    if post.is_self:
        content = post.selftext
        content = content.replace('\n#', '\n####') # md headings
        post_content.append(f"{content}\n\n")
    else:
        post_content.append(f"[Link to content]({post.url})\n\n")
    post_content.append("### Comments:\n\n")
    post.comments.replace_more(limit=None)
    for comment in post.comments:
        post_content.append(format_comment(comment, upvote_threshold=comment_score_threshold, t0=ts))
    post_content.append("---\n\n")
    return ''.join(post_content)
 

# m = submission_to_markdown(submission, -100, verbose=True)
# print(m)
