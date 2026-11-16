
import matplotlib.pyplot as plt  # import library

x = [ k for k in range(100) ]  # create a range for the data
y = [ 2**k for k in x ]      # create a simple function y=2^x

plt.plot(x,y)  # create a 2d plot

plt.xlabel('x')
plt.ylabel('y=2^x')  # annotate

plt.show()  # display

# Test the example as is on the slides
# - Modify the data and the range
# - Plot in different ways
# Read matplotlib documentation
# - Test some other plotting functions
