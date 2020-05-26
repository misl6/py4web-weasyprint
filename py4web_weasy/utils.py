import weasyprint
import mimetypes
import os

from py4web.core import request


def py4web_url_fetcher(url, timeout=10, ssl_context=None):
    if url.startswith("file://"):
        url = url.split("file://")[-1]
        mime_type, encoding = mimetypes.guess_type(url)
        data = {
            "mime_type": mime_type,
            "encoding": encoding,
            "filename": os.path.basename(url),
        }
        url_parts = url.split("/")
        if url_parts[0] == request.app_name:
            url_parts = url_parts[1:]

        filepath = os.path.join(
            os.environ["PY4WEB_APPS_FOLDER"], request.app_name, *url_parts
        )
        data["file_obj"] = open(filepath, "rb")
        return data

    return weasyprint.default_url_fetcher(url, timeout, ssl_context)
