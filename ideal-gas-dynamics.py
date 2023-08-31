#### Imports
import os
import sys
import time
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Molecule(object):
    #Constructor
    def __init__(self, molecule, position, velocity, mass, color="black"):
        self.molecule = molecule
        self.position = np.array([x_i for x_i in position])
        self.velocity = np.array([v_i for v_i in velocity])
        self.mass = mass
        self.color = color
    #-------------------------------------------------------------------------------- 
    #Setters for position, velocity, mass and color
    def set_position(self, position):
        self.position = np.array([x_i for x_i in position])
    #-------------------------------------------------------------------------------- 
    def set_velocity(self,velocity):
        self.velocity = np.array([v_i for v_i in velocity])
    #--------------------------------------------------------------------------------   
    def set_color(self, color):
        self.color = color
    #--------------------------------------------------------------------------------
    def set_mass(self, mass):
        self.mass = mass
    #--------------------------------------------------------------------------------   
    #Getters for position, velocity, mass and color of the particle
    def get_position(self):
        return self.position
    #--------------------------------------------------------------------------------
    def get_velocity(self):
        return self.velocity
    #--------------------------------------------------------------------------------    
    def get_color(self):
        return self.color
    #--------------------------------------------------------------------------------    
    def get_mass(self):
        return self.mass