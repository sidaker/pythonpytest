from src.tasks import namedtuples_deafults

from collections import namedtuple
Task = namedtuple('Task',['summary','owner','done','eid'])
Task.__new__.__defaults__ = (None,None,False,None)

''' Test file  -> test_<>.py
    Test method -> test_<>
    Test Classes -> Test<Something>.
'''

def test_defaults():
    t1 = Task()
    t2 = Task(None,None,False,None)
    assert t1 == t2

# demonstrate how you can access members by name instead of index unlik tuples.
def test_members():
    t3 = Task('Learn Pytest','Sid', False,22)
    assert t3.summary == 'Learn Pytest'
    assert t3.owner == 'Sid'
    assert t3.done == False

def test_asdict():
    t4 = Task('Pytest', 'Sid', True, 21)
    t_dict = t4._asdict()
    expected = {'summary' : 'Pytest', 'owner' : 'Sid' ,'done' : True, 'eid' : 21}
    assert t_dict == expected
