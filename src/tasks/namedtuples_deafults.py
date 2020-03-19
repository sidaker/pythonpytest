from collections import namedtuple

Task = namedtuple('Task',['summary','owner','done','id'])

Task.__new__.defaults__ = (None,None,False,None)
