from io import BytesIO
import base64
import gzip
import jinja2
import pandas as pd
from pathlib import Path
import json
from IPython.display import HTML, display

def base64_gzip_encode(data: str) -> str:
    """because there is a lot of uncompressed text data, we can compress it to gzip and store as base64. This isn't perfect but it's simple and works with a single static page"""
    buf = BytesIO()
    compressGzip = gzip.GzipFile(fileobj=buf, mode="wb")
    compressGzip.write(data.encode())
    compressGzip.close()
    buf.seek(0)

    b64str = base64.b64encode(buf.getvalue()).decode()
    return b64str


def export_df_2_html(df: pd.DataFrame = None, template: Path=Path( "../index.jinja2.html"), output: Path = Path("../index.html"), columns:list = None, hidden_columns: list = []):
    """
    """

    environment = jinja2.Environment()
    template_o = open("../index.jinja2.html").read()
    template_o = environment.from_string(template_o)

    columns = [
        {
            "title": c,
            "visible": c not in hidden_columns,
            "searchable": c not in hidden_columns,
            "footer": c,
            "name": c+"2",
        }
        for c in df.columns
    ]
    columns = json.dumps(columns)

    b64str = base64_gzip_encode(df.to_json(orient="values"))

    html = template_o.render(
        data=b64str,
        columns=columns,
    )
    html_out = Path(output).resolve()
    open(html_out, "w").write(html)

    htmla = f'<a href="{html_out}">View the page {html_out}</a>'
    display(HTML(htmla))
