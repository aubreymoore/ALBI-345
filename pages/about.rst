.. title: About
.. slug: about
.. date: 2017-08-22 06:04:31 UTC+10:00
.. tags:
.. category:
.. link:
.. description:
.. type: text

Overview
--------

This page contains some technical notes about this site.

Reusing Posts from the F2015 Pelican Site
-----------------------------------------

Since the previous web site was written using Pelican, it was convenient to use
the Markdown metedata format. To enable this, I added **markdown.extensions.meta**
to **conf.py**::

  # What Markdown extensions to enable?
  # You will also get gist, nikola and podcast because those are
  # done in the code, hope you don't mind ;-)
  # Note: most Nikola-specific extensions are done via the Nikola plugin system,
  #       with the MarkdownExtension class and should not be added here.
  # The default is ['fenced_code', 'codehilite']
  MARKDOWN_EXTENSIONS = [
      'markdown.extensions.fenced_code',
      'markdown.extensions.codehilite',
      'markdown.extensions.extra',
      'markdown.extensions.meta'
  ]

Scheduling
----------

**calendar.csv** contains a list of dates and times for lectures and labs in a
format that can be imported into Google calendars. Start dates and times are
included in the metadata for each lecture and lab.
