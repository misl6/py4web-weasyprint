# py4web-weasyprint

Easely generate PDF outputs via [WeasyPrint](https://github.com/Kozea/WeasyPrint) on top of [py4web](https://github.com/web2py/py4web).


## Usage / Example


```python
from py4web_weasy import WeasyTemplate

@action('mypdfpage')
@action.uses(WeasyTemplate("mypdfpage.html"))
def mypdfpage():
    return {}

```
