import os
import sys

# Add the parent directory to the system path to
# allow imports from the src directory
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'src')))
