>>> help(xml.etree.ElementTree)
Help on module xml.etree.ElementTree in xml.etree:

NAME
    xml.etree.ElementTree - Lightweight XML support for Python.

DESCRIPTION
    XML is an inherently hierarchical data format, and the most natural way to
    represent it is with a tree.  This module has two classes for this purpose:

       1. ElementTree represents the whole XML document as a tree and

       2. Element represents a single node in this tree.

    Interactions with the whole document (reading and writing to/from files) are
    usually done on the ElementTree level.  Interactions with a single XML element
    and its sub-elements are done on the Element level.

    Element is a flexible container object designed to store hierarchical data
    structures in memory. It can be described as a cross between a list and a
    dictionary.  Each Element has a number of properties associated with it:

       'tag' - a string containing the element's name.

       'attributes' - a Python dictionary storing the element's attributes.

       'text' - a string containing the element's text content.

       'tail' - an optional string containing text after the element's end tag.

       And a number of child elements stored in a Python sequence.

    To create an element instance, use the Element constructor,
    or the SubElement factory function.

    You can also use the ElementTree class to wrap an element structure
    and convert it to and from XML.

CLASSES
    builtins.SyntaxError(builtins.Exception)
        ParseError
    builtins.object
        Element
        ElementTree
        QName
        TreeBuilder
        XMLParser

    class Element(builtins.object)
     |  Methods defined here:
     |
     |  __copy__(...)
     |
     |  __deepcopy__(...)
     |
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |
     |  __delitem__(self, key, /)
     |      Delete self[key].
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __getitem__(self, key, /)
     |      Return self[key].
     |
     |  __getstate__(...)
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __len__(self, /)
     |      Return len(self).
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  __setitem__(self, key, value, /)
     |      Set self[key] to value.
     |
     |  __setstate__(...)
     |
     |  __sizeof__(...)
     |
     |  append(...)
     |
     |  clear(...)
     |
     |  extend(...)
     |
     |  find(...)
     |
     |  findall(...)
     |
     |  findtext(...)
     |
     |  get(...)
     |
     |  getchildren(...)
     |
     |  getiterator(...)
     |
     |  insert(...)
     |
     |  items(...)
     |
     |  iter(...)
     |
     |  iterfind(...)
     |
     |  itertext(...)
     |
     |  keys(...)
     |
     |  makeelement(...)
     |
     |  remove(...)
     |
     |  set(...)

    class ElementTree(builtins.object)
     |  An XML element hierarchy.
     |
     |  This class also provides support for serialization to and from
     |  standard XML.
     |
     |  *element* is an optional root element node,
     |  *file* is an optional file handle or file name of an XML file whose
     |  contents will be used to initialize the tree with.
     |
     |  Methods defined here:
     |
     |  __init__(self, element=None, file=None)
     |
     |  find(self, path, namespaces=None)
     |      Find first matching element by tag name or path.
     |
     |      Same as getroot().find(path), which is Element.find()
     |
     |      *path* is a string having either an element tag or an XPath,
     |      *namespaces* is an optional mapping from namespace prefix to full name.
     |
     |      Return the first matching element, or None if no element was found.
     |
     |  findall(self, path, namespaces=None)
     |      Find all matching subelements by tag name or path.
     |
     |      Same as getroot().findall(path), which is Element.findall().
     |
     |      *path* is a string having either an element tag or an XPath,
     |      *namespaces* is an optional mapping from namespace prefix to full name.
     |
     |      Return list containing all matching elements in document order.
     |
     |  findtext(self, path, default=None, namespaces=None)
     |      Find first matching element by tag name or path.
     |
     |      Same as getroot().findtext(path),  which is Element.findtext()
     |
     |      *path* is a string having either an element tag or an XPath,
     |      *namespaces* is an optional mapping from namespace prefix to full name.
     |
     |      Return the first matching element, or None if no element was found.
     |
     |  getiterator(self, tag=None)
     |      # compatibility
     |
     |  getroot(self)
     |      Return root element of this tree.
     |
     |  iter(self, tag=None)
     |      Create and return tree iterator for the root element.
     |
     |      The iterator loops over all elements in this tree, in document order.
     |
     |      *tag* is a string with the tag name to iterate over
     |      (default is to return all elements).
     |
     |  iterfind(self, path, namespaces=None)
     |      Find all matching subelements by tag name or path.
     |
     |      Same as getroot().iterfind(path), which is element.iterfind()
     |
     |      *path* is a string having either an element tag or an XPath,
     |      *namespaces* is an optional mapping from namespace prefix to full name.
     |
     |      Return an iterable yielding all matching elements in document order.
     |
     |  parse(self, source, parser=None)
     |      Load external XML document into element tree.
     |
     |      *source* is a file name or file object, *parser* is an optional parser
     |      instance that defaults to XMLParser.
     |
     |      ParseError is raised if the parser fails to parse the document.
     |
     |      Returns the root element of the given source document.
     |
     |  write(self, file_or_filename, encoding=None, xml_declaration=None, default_namesp
hod=None, *, short_empty_elements=True)
     |      Write element tree to a file as XML.
     |
     |      Arguments:
     |        *file_or_filename* -- file name or a file object opened for writing
     |
     |        *encoding* -- the output encoding (default: US-ASCII)
     |
     |        *xml_declaration* -- bool indicating if an XML declaration should be
     |                             added to the output. If None, an XML declaration
     |                             is added if encoding IS NOT either of:
     |                             US-ASCII, UTF-8, or Unicode
     |
     |        *default_namespace* -- sets the default XML namespace (for "xmlns")
     |
     |        *method* -- either "xml" (default), "html, "text", or "c14n"
     |
     |        *short_empty_elements* -- controls the formatting of elements
     |                                  that contain no content. If True (default)
     |                                  they are emitted as a single self-closed
     |                                  tag, otherwise they are emitted as a pair
     |                                  of start/end tags
     |
     |  write_c14n(self, file)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)

    class ParseError(builtins.SyntaxError)
     |  Method resolution order:
     |      ParseError
     |      builtins.SyntaxError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Data descriptors defined here:
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.SyntaxError:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.SyntaxError:
     |
     |  filename
     |      exception filename
     |
     |  lineno
     |      exception lineno
     |
     |  msg
     |      exception msg
     |
     |  offset
     |      exception offset
     |
     |  print_file_and_line
     |      exception print_file_and_line
     |
     |  text
     |      exception text
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __reduce__(...)
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  __setstate__(...)
     |
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |
     |  __cause__
     |      exception cause
     |
     |  __context__
     |      exception context
     |
     |  __dict__
     |
     |  __suppress_context__
     |
     |  __traceback__
     |
     |  args

    class QName(builtins.object)
     |  Qualified name wrapper.
     |
     |  This class can be used to wrap a QName attribute value in order to get
     |  proper namespace handing on output.
     |
     |  *text_or_uri* is a string containing the QName value either in the form
     |  {uri}local, or if the tag argument is given, the URI part of a QName.
     |
     |  *tag* is an optional argument which if given, will make the first
     |  argument (text_or_uri) be interpreted as a URI, and this argument (tag)
     |  be interpreted as a local name.
     |
     |  Methods defined here:
     |
     |  __eq__(self, other)
     |
     |  __ge__(self, other)
     |
     |  __gt__(self, other)
     |
     |  __hash__(self)
     |
     |  __init__(self, text_or_uri, tag=None)
     |
     |  __le__(self, other)
     |
     |  __lt__(self, other)
     |
     |  __ne__(self, other)
     |
     |  __repr__(self)
     |
     |  __str__(self)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)

    class TreeBuilder(builtins.object)
     |  Methods defined here:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  close(...)
     |
     |  data(...)
     |
     |  end(...)
     |
     |  start(...)

    class XMLParser(builtins.object)
     |  # also see ElementTree and TreeBuilder
     |
     |  Methods defined here:
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  close(...)
     |
     |  doctype(...)
     |
     |  feed(...)

FUNCTIONS
    Comment(text=None)
        Comment element factory.

        This function creates a special element which the standard serializer
        serializes as an XML comment.

        *text* is a string containing the comment string.

    PI = ProcessingInstruction(target, text=None)
        Processing Instruction element factory.

        This function creates a special element which the standard serializer
        serializes as an XML comment.

        *target* is a string containing the processing instruction, *text* is a
        string containing the processing instruction contents, if any.

    ProcessingInstruction(target, text=None)
        Processing Instruction element factory.

        This function creates a special element which the standard serializer
        serializes as an XML comment.

        *target* is a string containing the processing instruction, *text* is a
        string containing the processing instruction contents, if any.

    SubElement(...)

    XML(text, parser=None)
        Parse XML document from string constant.

        This function can be used to embed "XML Literals" in Python code.

        *text* is a string containing XML data, *parser* is an
        optional parser instance, defaulting to the standard XMLParser.

        Returns an Element instance.

    XMLID(text, parser=None)
        Parse XML document from string constant for its IDs.

        *text* is a string containing XML data, *parser* is an
        optional parser instance, defaulting to the standard XMLParser.

        Returns an (Element, dict) tuple, in which the
        dict maps element id:s to elements.

    dump(elem)
        Write element tree or element structure to sys.stdout.

        This function should be used for debugging only.

        *elem* is either an ElementTree, or a single Element.  The exact output
        format is implementation dependent.  In this version, it's written as an
        ordinary XML file.

    fromstring = XML(text, parser=None)
        Parse XML document from string constant.

        This function can be used to embed "XML Literals" in Python code.

        *text* is a string containing XML data, *parser* is an
        optional parser instance, defaulting to the standard XMLParser.

        Returns an Element instance.

    fromstringlist(sequence, parser=None)
        Parse XML document from sequence of string fragments.

        *sequence* is a list of other sequence, *parser* is an optional parser
        instance, defaulting to the standard XMLParser.

        Returns an Element instance.

    iselement(element)
        Return True if *element* appears to be an Element.

    iterparse(source, events=None, parser=None)
        Incrementally parse XML document into ElementTree.

        This class also reports what's going on to the user based on the
        *events* it is initialized with.  The supported events are the strings
        "start", "end", "start-ns" and "end-ns" (the "ns" events are used to get
        detailed namespace information).  If *events* is omitted, only
        "end" events are reported.

        *source* is a filename or file object containing XML data, *events* is
        a list of events to report back, *parser* is an optional parser instance.

        Returns an iterator providing (event, elem) pairs.

    parse(source, parser=None)
        Parse XML document into element tree.

        *source* is a filename or file object containing XML data,
        *parser* is an optional parser instance defaulting to XMLParser.

        Return an ElementTree instance.

    register_namespace(prefix, uri)
        Register a namespace prefix.

        The registry is global, and any existing mapping for either the
        given prefix or the namespace URI will be removed.

        *prefix* is the namespace prefix, *uri* is a namespace uri. Tags and
        attributes in this namespace will be serialized with prefix if possible.

        ValueError is raised if prefix is reserved or is invalid.

    tostring(element, encoding=None, method=None, *, short_empty_elements=True)
        Generate string representation of XML element.

        All subelements are included.  If encoding is "unicode", a string
        is returned. Otherwise a bytestring is returned.

        *element* is an Element instance, *encoding* is an optional output
        encoding defaulting to US-ASCII, *method* is an optional output which can
        be one of "xml" (default), "html", "text" or "c14n".

        Returns an (optionally) encoded string containing the XML data.

    tostringlist(element, encoding=None, method=None, *, short_empty_elements=True)

DATA
    VERSION = '1.3.0'
    __all__ = ['Comment', 'dump', 'Element', 'ElementTree', 'fromstring', ...

FILE
    c:\util\python34\lib\xml\etree\elementtree.py