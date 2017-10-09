# ade25.sitecontent

## Sitecontent package containing folderish content pages

* `Source code @ GitHub <https://github.com/ade25/ade25.sitecontent>`_
* `Releases @ PyPI <http://pypi.python.org/pypi/ade25.sitecontent>`_
* `Docubfatation @ ReadTheDocs <http://ade25sitecontent.readthedocs.org>`_
* `Continuous Integration @ Travis-CI <http://travis-ci.org/ade25/ade25.sitecontent>`_


## How it works

This package aims to simplify content editing and organistation by breaking the
separation between folders and pages by providing a container based content.

### Content Types included

- Content Page
- Section Folder

### Provided behaviors

- Gallery toggle
- Display Options (content preview width, layout)

### Provided views


- Section Folder with automatic content listings
- Content Page Plain View (title, description, rich text)
- Content Page Card (Preview Card for Content Pages)
- Content Page Gallery View (Slider based gallery)


*Note:*

All styling and layouting is intentionally left up to the actual site theme. Therfore
the features are carefully selected in order to not overload the pacakge with
seldomly needed display options etc.


## Installation

To install `ade25.sitecontent` you simply add ``ade25.sitecontent``
to the list of eggs in your buildout, run buildout and restart Plone.
Then, install `ade25.sitecontent` using the Add-ons control panel.
