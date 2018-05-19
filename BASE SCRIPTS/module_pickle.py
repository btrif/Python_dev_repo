#  Created by Bogdan Trif on 16-03-2018 , 10:05 AM.
'''
The pickle module implements a fundamental, but powerful algorithm for serializing and de-serializing a Python object structure.
“Pickling” is the process whereby a Python object hierarchy is converted into a byte stream,
and “unpickling” is the inverse operation, whereby a byte stream is converted back into an object hierarchy.
Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” [1] or “flattening”, however,
to avoid confusion, the terms used here are “pickling” and “unpickling”.

This documentation describes both the pickle module and the cPickle module.

To serialize an object hierarchy, you first create a pickler, then you call the pickler’s dump() method.
To de-serialize a data stream, you first create an unpickler, then you call the unpickler’s load() method.

'''
# Save a dictionary into a pickle file.
import pickle

favorite_color = { "lion": "yellow", "kitty": "red" }

pickle.dump( favorite_color, open( "save.p", "wb" ) )

favorite_color2 = pickle.load( open( "save.p", "rb" ) )
print('favorite_color2 : ', favorite_color2)