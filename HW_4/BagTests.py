#########################################################################################
# Here are some basic tests to make sure your Bag implementation runs correctly
# You can run them by running 'python BagTests.py' from the command line
#########################################################################################

from Bag import *

bag = Bag()

print "Checking basic variable initializations..."

assert bag.is_empty()

bag.print_bag()
print "done\n"

###################################

print "Checking add, contains, functions..."

bag.add(1)
bag.add(2)

assert bag.contains(1) == 1
assert bag.contains(2) == 1


bag.print_bag()
print "done\n"

###################################

print "Checking remove, function(s)..."

bag.remove(1)
bag.remove(2)

assert bag.contains(1) == 0
assert bag.contains(2) == 0

bag.print_bag()
print "done\n"

###################################

print "Checking that all of the above didn't break things"

bag.add(1)
bag.add(2)

assert bag.size() == 2

bag.remove(1)

assert bag.size() == 1
assert bag.contains(2)

bag.add(3)
bag.add(4)
bag.remove(4)
bag.add(10)

assert bag.contains(3)
assert bag.size() == 3

bag.print_bag()
print "All checks passed"