# py4web-weasyprint

Easely generate PDF outputs via [WeasyPrint](https://github.com/Kozea/WeasyPrint) on top of [py4web](https://github.com/web2py/py4web).

## Installation

Considering that this plugin works on top of `weasyprint`, it needs some external dependencies as weasyprint does.

### Step 1)
Follow [these install instructions](https://weasyprint.readthedocs.io/en/latest/install.html#linux) if you're on a **Linux** distro.

Follow [these install instructions](https://weasyprint.readthedocs.io/en/latest/install.html#macos) if you're on **MacOS**.

Follow [these install instructions](https://weasyprint.readthedocs.io/en/latest/install.html#windows) if you're on **Windows**.

### Step 2)

#### Building from source:

`python setup.py install`

#### Installing from pip:

`pip install py4web-weasyprint` (still not available)



## Example


```python
from py4web_weasy import WeasyTemplate

@action('mypdfpage')
@action.uses(WeasyTemplate("mypdfpage.html"))
def mypdfpage():
    return {}

```
