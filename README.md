# Modeling-Dynamics-Ideal-Gas-Molecules
A framework to simulate and visualize molecular collisions, and extract thermodynamic insights using Python.

# Introduction
Imagine someone constantly throwing a ball at your head. Depending upon the size and mass of the ball, you may feel anything between mild annoyance and unbearable agony. And yet, there are countless such “balls” colliding with, not only your head, but your whole body every instant and you do not feel a thing. Nitrogen, oxygen, and water molecules in the air are in constant random motion around you, even when the air appears to be stationary. The result of the collisions of these molecules with you is that air exerts a certain pressure on you (termed atmospheric pressure). Since we are “used to” the atmospheric pressure, it does not feel like anything out of the ordinary, but if you are ever in an airplane or a hyperbaric chamber, where the pressure deviates from the atmospheric pressure, you may notice different sensations, like ear-popping, that are your body’s responses to changes in pressure.

A macroscopic understanding of pressure, and how it varies with the volume that a gas occupies was given by Robert Boyle in the 17th century, that is commonly termed as Boyle’s law. However, it was only a century later that a qualitative molecular picture was provided by Daniel Bernoulli to explain pressure, and also relate it to the temperature and kinetic energy of molecules. This “kinetic theory,” however, did not find much acceptance until, in the 19th century, James Clerk Maxwell, building on the work of Rudolf Clausius, formalized it in terms of a statistical law and Ludwig Boltzmann illuminated its relationship with entropy, leading to the formulation of the Maxwell-Boltzmann distribution of velocities of molecules in a gas. This eventually led to the development of a detailed theoretical treatment of gases from the molecular point of view, which was consistent with the well-understood macroscopic view.

In this article, we will try to link the molecular picture of gases with its macroscopic properties — that is, pressure, volume, and temperature — by performing a series of numerical simulations using Python.

# Theoretical Background
## Kinetic theory of gases
The kinetic theory of gases is a model that describes a gas in terms of molecules that are in constant, random motion.

Molecules travel in straight lines until they are interrupted by elastic collisions with other molecules or the walls of the container. Elasticity implies that no kinetic energy is lost in collisions.
Molecules do not “interact” with each other, that is, they do not exert any attractive or repulsive intermolecular forces.
The volume occupied by the molecules themselves is considered to be negligible compared to the volume occupied by the gas.
If molecules following these rules are sampled and their velocities measured, they will conform to the Maxwell-Boltzmann distribution. The temperature of the gas is actually a property that we define based on the shape of the distribution. The higher the average kinetic energy is (or the flatter the distribution is), the higher the temperature of the gas is, and vice versa. It does not make sense to define a temperature of an individual molecule; rather, it is an averaged property of a collection of molecules.

Note that the kinetic theory of gases is a model, it is not necessarily a true reflection of reality (as is the case with all scientific models). Molecular collisions are not strictly elastic, and molecules do have short-range interactions. However, a model with these relatively simple assumptions is able to replicate the properties of an ideal gas very well, which is a very useful macroscopic model to predict the behavior of gases under various conditions.

## Ideal gas law
An ideal gas is a hypothetical gas whose properties are related to each other through a simple equation-of-state, called the ideal gas law: 
$$
PV = nRT,
$$
where P refers to the pressure of the gas, V refers to the volume of the container, T is the temperature, and n is the number of moles of the gas. If any of these three quantities are held constant, the fourth does not change as well, and this is reflected through R, which is the universal gas constant. The ideal gas law is an accurate model for a gas that is at a high temperature or low pressure, since most of the assumptions of the kinetic theory of gases are true in these regimes.

We will test two relationships based on the ideal gas law with our model.

At a constant temperature and number of moles, the pressure is inversely proportional to the volume.
At a constant volume and number of moles, the pressure is directly proportional to the temperature.
The former is referred to as Boyle’s law and the latter is referred to as Gay-Lussac’s law, both named after researchers that first discovered the relationships between these variables through experiments.