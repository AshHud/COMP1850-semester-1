# Week 1.7, Session 1: Task 2 - unit test for comfort_level() 

# Fill in the blank spaces in the calls to comfort_level() below, using
# the values you've chosen for testing the function

# Then write a test_ok() function that tests the other equivalence class

from weather import comfort_level

def test_cold():
    assert comfort_level(6.4) == "COLD"
    assert comfort_level(15.0) == "COLD"

def test_hot():
    assert comfort_level(25.1) == "HOT"
    assert comfort_level(34.6) == "HOT"

def test_OK():
    assert comfort_level(15.1) == "OK"
    assert comfort_level(19.4) == "OK"
    assert comfort_level(25.0) == "OK"
    
