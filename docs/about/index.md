What is Project Aries?
======================

Project Aries is a about delivering a networked journaling solution.  It is a process as much as a product, but it's purpose is to provide an interface so that documents can be created, stored, editied, retrieved, commented on and searched.  The document base is assumed to be a directory structure of plain-text ASCII files, initially, written in Markdown.  Aries creates and serves a Git repository of these documents and also provides a web-based GUI environment in which to do the editing via a Tornado server.

In short, Project Aries aims to deliver a software package that contains both an executable, stand-alone Aries server and the associated Python packages since it is our goal to implement a simple RESTful interface to the server so that other software can work with a journal as well.