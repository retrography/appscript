"""py-appscript -- High-level Mac OS X application scripting support for Python 2.x.

(C) 2004-2009 HAS
"""

__version__ = '0.21.1'

__all__ = ['ApplicationNotFoundError', 'CommandError', 'CantLaunchApplicationError', 
		'app','con', 'its', 'k','mactypes']

from aem.findapp import ApplicationNotFoundError
from aem import CantLaunchApplicationError
from reference import app, CommandError
from genericreference import con, its
from keywordwrapper import k
from aem import mactypes

# The following classes are exposed for occasional typechecking purposes. To avoid excess 
# namespace pollution they aren't added to the parent namespace when 'from appscript import *'
#  is used, so must be referred to like this [e.g.]:
#
# import appscript
# isinstance(obj, appscript.Reference)

from reference import Command, Reference, Application, GenericApp
from genericreference import GenericReference
from keywordwrapper import Keyword