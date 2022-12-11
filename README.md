# Project Title : Infection Mushroom
Infection Mushroom is a tool that simulates the spread of an infection in a mushroom colony. This can be useful for studying the spread of diseases in populations. The purpose of this project was to mimic how a ringworm infection would spread over a skin area of size N x N cells. An initial infected cell will be selected randomly. The infected cell has a chance of infecting any healthy cells nearby at each time interval, depending on user's input and an infected equation. Each infected cell will also have a probability of healing using the healing equation.



## Key Outcome
This is a simulation of an infection on a two-dimensional surface, such as skin. The simulation is performed by creating an instance of the `Skin` class, which has a size attribute that determines the dimensions of the surface (e.g. 10x10). The `Skin` class also has two other attributes, `infected_rate` and `healing_rate`, which determine the probability that a healthy cell becomes infected and the probability that an infected cell recover, respectively. The simulation starts with one randomly chosen cell that is infected. Then, for each iteration of the simulation, the `get_infected()` method is called, which updates the state of each cell on the surface according to the following rules:

•	If a cell is healthy and has at least one infected neighbor, there is a chance that it becomes infected, with a probability determined by the `infected_rate` attribute of the `Skin` instance.

•	If a cell is infected, there is a chance that it recovers, with a probability determined by the `healing_rate` attribute of the `Skin` instance. The probability of recovery increases by 0.05 for each day that the cell is infected.

•	If a cell is infected and its infected score (which starts at 6 and decreases by 1 each time the cell recovers) becomes 0, the cell becomes immune and cannot be infected again.
 The `visualize()` method of the `Skin` class uses matplotlib to display the current state.
 
 
 
### Implementation Backend.py
•	`Cell` : Represent a single cell on the skin. It has a single attribute, status, which is a string representing the status of the cell. It can be one of three values: ".", "#", or "*", representing a healthy cell, an immune cell, and an infected cell, respectively. 

•	`HealthyCell`: is a subclass of the `Cell` class, so it inherits all the attributes and methods of the `Cell` class. The `HealthyCell` class has one additional attribute status which is set to '.'. The `HealthyCell` object represents a healthy cell in the skin.

•	`ImmuneCell` : class has a status attribute that is set to '#'. These classes can be used to represent cells which are immune.

•	`InfectedCell` : The `InfectedCell` class is a subclass of the `Cell` class and has additional attributes and methods specific to infected cells. The `infected` attribute represents the severity of the infection that the cell has suffered, and the `infectedDay` attribute keeps track of the total number of days the cell has been infected. These are the methods in this cell.

        o   heal(): The function `heal` is a method of the `InfectedCell` class, which is intended to decrease the `infected` attribute of an instance of the `InfectedCell` class by 1. When it reaches 0, the cell is considered to be healed and its status changes to '#' (immune).
        o   get_infected_day(): This returns the value of the `infectedDay` attribute of the `InfectedCell` instance. The `infectedDay` attribute is to measure how long the cell has been infected.
        o	increment_infected_day(): method increases the value of the `infectedDay` attribute by one. This indicates that one more day has passed since the cell was infected.
        o	get_infected_day(): method returns the number of days the infected cell has been infected for. This value is incremented by one every day using the `increment_infected_day()` method.
      
•	`Skin`: has a constructor that takes three parameters - `size`, `infected_rate`, and `healing_rate`. The constructor creates an empty grid of size x size that is filled with healthy cells, then it selects a random cell in the grid and infects it. It also initializes instance variables `infected_rate` and `healing_rate` with the given `infected_rate` and `healing_rate`, respectively.

•	Methods

        o   get_skin() returns the grid of cells that represent the skin as a 2D array.
        o	get_visual() returns a visual representation of the skin as a 2D array.
        o	get_infected_matrix() returns the infected score of the infected cells as a 2D array.
        o	get_infected_day_matrix() returns the number of days that each infected cell has been infected as a 2D array.
        o	get_infected() applies the infection and healing rules to each cell in the grid to determine the next state of the skin.
        o	visualize() visualizes the current state of the skin.

### Complexity Of Backend.py:
Let n x n or $n^2$ be the size of the skin.

- Once the skin is initialized, the time complexity for the initialization will be O( $n^2$ ) to simulate the skin. It will also create a 2D array to store $n^n$ cells, leading to a space complexity of O( $n^2$ ).
- Each method among `get_visual()`, `get_infected_matrix()`, `get_infected_day_matrix()`, `visualize()` costs O( $n^2$ ) time and space to loop through each cell and return the representation of the skin. 
- About `get_infected()`, since each cell has the maximum of eight neighbors (except the edge cells), the time and space complexity to update the state of the skin are also O( $n^2$ ).

### Complexity Of Backend.py:
One way to improve the complexity of this code would be to only update the state of cells that are in proximity to infected cells, rather than looping over the entire grid. This would reduce the number of cells that need to be updated each time, reducing the overall complexity to O(k), where k is the number of infected cells. 
In the `get_infected()` method of the `Skin` class, the 'nbrs' list is defined and looped through multiple times. We could move this list outside the nested for loops and just loop through it once, which would reduce the time complexity of this method. We could also use data structures that have faster search and access times, such as dictionaries and sets, in place of lists and arrays.



### Implementation Frontend.py
•	`Gui` Class: represents the GUI for an infection simulator.The __init__ method initializes a new Gui object by creating a new Tkinter window, setting it to full screen.

      o	drawWindow(): function creates an infection simulator's GUI. The function takes a root parameter, likely the GUI's root window, and creates widgets in it. It creates a window title, a parameter frame, a simulation canvas, and a simulation start button. Function sets object's graph attribute to canvas. When the "Simulate" button is clicked, the startsimulation function is called with the sample size, healing rate, infection rate, and number of days entered by the user. The code snippet doesn't define startsimulation, so it's unclear what it does.
      o	update_animate(): Method animates simulation. It accepts a 2D list of the simulation's state and the current day. It converts the 2D list into a numpy array, sets each cell's color based on its value, and displays the array on the canvas. It also updates the image's date.
      o	startsimulation():function is called when the user clicks the "Simulate" button in the GUI. It takes five parameters: the size of the simulation, the healing rate, the infection rate, the Gui object, and the number of days to simulate.

### Complexity of Frontend:
The complexity of this code is O(days * $size^2$). The update_animate() method has a nested for loop that runs through each element of the `visual_skin` list, which has length size and is called days times in the `startSimulation()` method. This means that the `update_animate()` method will be called *days * $size^2$* times, which is the complexity of the code.

# How to Improve the complexity of Frontend code:
•	Use a data structures and algorithms that have better time complexity. For example, alternate using nested for loops to iterate through the elements of the `visual_skin` array. We could use a single loop to iterate through all the elements. Also, we could use a dictionary to store the corresponding integer values for each skin cell instead of using multiple if-else statements.

•	Simplify our Computations: instead of creating a new figure and axes object for each update, you could create these objects once and then update their properties as needed.


# Enhancement of Code:

•	Initialize the 2D skin matrix using the np.empty method instead of using a nested list comprehension. This should make the initialization faster because it pre-allocates the memory for the array and doesn't have to go through the process of creating each element in the array.

•	In the `get_infected()` method, instead of looping through each cell in the skin matrix to find the number of infected cells around it, you can use the scipy.ndimage.generic_filter method to apply a filter to the skin matrix that counts the number of infected cells around each cell. This should be much faster than looping through each cell individually.

•	In the `get_visual()`, `get_infected_matrix()`, and `get_infected_day_matrix()` methods, you can use the np.vectorize method to apply a function to each element in the skin matrix to get the desired information. This will be much faster than using a nested for loop.


# Learnings:



# Conclusions and Discussion:







### Dependencies
Matplotlib 3.5.1
NumPy 1.22.1
Python 3.10


### Known Issues
InfectionMushroom does not currently support the simulation of multiple infected mushrooms.

## Authors
```
Anh N. Ngo
```
```
Anish Kharel
```
```
Ebenezer Ayisi
```







## Acknowledgments
Eliza Matveeva-(https://github.com/eliza-mat/ringworm-infection)
```
Patrick Sheperd 
