import weasyprint
import mimetypes
import os

from py4web.core import request


def py4web_url_fetcher(url, timeout=10, ssl_context=None):
    if url.startswith(f'/{request.app_name}'):
        mime_type, encoding = mimetypes.guess_type(url)
        data = {
            'mime_type': mime_type,
            'encoding': encoding,
            'filename': os.path.basename(url),
        }

        filepath = os.path.join(
            os.environ["PY4WEB_APPS_FOLDER"], *url.split('/'))
        data['file_obj'] = open(filepath, 'rb')
        return data

    return weasyprint.default_url_fetcher(url, timeout, ssl_context)
