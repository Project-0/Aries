# Setting Up A Development Environment

## Configuring the Project Links

This is a horrible cluge.  Just wanted to get that out there.

### Eclipse
1.  Create an Eclipse workspace at the root Git folder
2.  Import the python `package` into the workspace as a PyDev project
3.  Import `/docs` as a General Project and create links to the other folders in `/`

### Virtualenv
1.  Add `package.pth` to your `/.virtualenvs/Project/lib/python2.7/site-packages/` folder so that the binary and unittest modules can import the main library.