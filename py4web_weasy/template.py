import weasyprint
import yatl

from py4web.core import Fixture, Template, response

from py4web_weasy.utils import py4web_url_fetcher


class WeasyTemplate(Fixture):

    def __init__(self, filename, path=None, delimiters="[[ ]]"):
        self.filename = filename
        self.path = path
        self.delimiters = delimiters

    def transform(self, output):
        output = Template(self.filename, self.path,
                          self.delimiters).transform(output)
        html = weasyprint.HTML(
            string=output,
            url_fetcher=py4web_url_fetcher,
        )
        rendered_doc = html.render()
        response.headers["Content-Type"] = "application/pdf"
        return rendered_doc.write_pdf()
