import markdown
import pandas as pd
import json
import collections, itertools
from collections import OrderedDict


def join_uniq(x: list[str]):
    return "\n".join(set(x))


def chain_lists(x: list[list[str]]):
    return [item for sublist in x for item in sublist]

def format_flair(author_flair_text):
    if author_flair_text:
        return f" <em>{author_flair_text}</em>"
    return ""

def commentmd2html(x: dict) -> str:
    """convert a comment to html"""
    body = markdown.markdown(x['body'])
    ts = pd.to_datetime(x['created_utc'], unit='s').strftime('%Y-%m-%d')
    flair = format_flair(x['author_flair_text'])
    url = prefix + x['permalink']
    s = f"""<h3><a href="{url}">{x.get('author', 'anon')} [{x['score']:+}] {flair} <sup>{ts}</sup></a></h3>
{body}
"""
    # print(s)
    return s


def collapsibe(title, body):
    """make a collapsible html element"""
    return f"""<details><summary>{title}</summary>
{body}
</details>
"""

prefix = "https://reddit.com"
def c2md(x):
    """md comment to html"""
    return collapsibe(x['id'], commentmd2html(x))


def url2a(url):
    """url to a tag"""
    text = url
    if "reddit.com/r/rational" in url:
        text = url.split("/")[-2]
        # text = url.replace('https://reddit.com/r/rational/comments/', '')

    return f'<a href="{url}">{text}</a>'




def unique_elements(lst):
    """get unique elements but unlike a set, keep them ordered."""
    return list(OrderedDict.fromkeys(lst))

def urls2a(urls, sep=None):
    """urls to a tags"""
    if isinstance(urls, str):
        urls = urls.split("\n")

    # get uniques from list, keep in same order
    urls = unique_elements(urls)

    a_els = [url2a(u) for u in urls]

    # now make into a html list
    if sep is None:
        return "<ul>" + "".join([f"<li>{x}</li>" for x in a_els]) + "</ul>"
    else:
        return sep.join(a_els)

import numpy as np

def auto_transform_to_html(d):
    for c in d.columns:
        # if the cols is a lists of strings
        is_list = d[c].apply(lambda x: isinstance(x, (list, tuple, np.ndarray))).all()
        is_list_str = is_list and d[c].apply(lambda x: (x is None) or (len(x)==0) or isinstance(x[0], str)).all()
        is_str = d[c].apply(lambda x: isinstance(x, str)).all()
        is_list_of_urls = is_list_str and d[c].apply(lambda x: (len(x)==0) or x[0].startswith("http")).all()
        is_urls = is_str and d[c].apply(lambda x: x.startswith("http")).all()
        is_url = d[c].apply(lambda x: isinstance(x, str)).all() and d[c].apply(lambda x: x.startswith("http")).all()
        is_list_obj = is_list and d[c].apply(lambda x: isinstance(x, dict)).all()

        print(f"{c}, is_list={is_list}, is_list_str={is_list_str}, is_list_url={is_list_of_urls}, is_url={is_url}, is_urls={is_urls}, is_list_obj={is_list_obj}\n")

        # if columns contains str: urls
        if is_urls:
            d[c] = d[c].apply(lambda x: url2a(x))        
        # elif c.endswith("urls"):
        #     d[c] = d[c].apply(lambda x: collapsibe('...', urls2a(x)))
        # elif c.endswith("url"):
        #     d[c] = d[c].apply(lambda x: url2a(x))
        elif is_list_of_urls:
            d[c] = d[c].apply(lambda x: collapsibe('...', urls2a(x)))
        elif is_list_str:
            d[c] = d[c].apply(lambda x: join_uniq(x))
    

        # if float, round to 2 decimal places
        elif d[c].dtype == float:
            d[c] = d[c].apply(lambda x: round(x, 2))

        # if column name ends with utc
        elif c.endswith("utc"):
            d[c] = pd.to_datetime(d[c], unit='s').dt.strftime('%Y-%m-%d')

        elif is_list:
            # TODO object to json using pandas.io.json.dumps
            # from pandas.io.json._json import to_json
            from pandas._libs.json import ujson_dumps
            d[c] = d[c].apply(lambda x: collapsibe('...', ujson_dumps(x, indent=2)))


    # make title have a link to first url
    d['title'] = d.apply(lambda x: f'<a href="{x["url"][0]}">{x["title"]}</a>', axis=1)
    return d
    
