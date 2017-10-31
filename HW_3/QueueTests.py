#########################################################################################
# Here you need to write some basic tests to make sure your Queue implementation runs correctly
# You can run them by running 'python QueueTests.py' from the command line
#########################################################################################

from Queue import Queue

queue = Queue()

print "Checking basic variable initializations..."
assert queue.size() == 0

queue.print_queue()
print "done\n"

###################################

print "Checking is_empty and size..."

assert queue.size() == 0
assert queue.is_empty()

queue.print_queue()
print "done\n"

###################################

print "Checking front, removeFront..."

queue.addBack(1)
queue.addBack(2)

assert queue.front() == 1

queue.removeFront()
assert queue.front() == 2

queue.print_queue()
print "done\n"

###################################

print "Checking back, addBack..."

queue.addBack(3)
assert queue.back() == 3

queue.print_queue()
print "done\n"

###################################

queue.print_queue()
print "All checks passed"