#ifndef PETRIDISH_H_
#define PETRIDISH_H_
#include <iostream>
#include "bacteria.h"
#include <vector>

 /**
  * PetriDish
  * Class which has a container of Bacteria pointers
  * It also has data about the food left in the Petridish
  *
  * The class has the following methods:
  * clean, addFood, addBacteria, print and updatePopulation.
  * These methods determine the amount of food in the PetriDish
  * and the number of bacterias in it.
  *
  * The class can print a status of the bacterias population
  * and the amount of food.
 */
class PetriDish {
public:

	/**
	 * Class Constructor.
	 * New PetriDishes are initialized empty of any food or bacteria.
	 *
	 */
	PetriDish();

	/**
	 *  Copy Constructor
	 *  @param original const Petridish & - the original petriDish to be copied
	 *
	 */
	PetriDish(const PetriDish &original);

	/**
	 *  Class Destructor
	 *
	 */
	~PetriDish()
	{
		clean();
	}

	/**
	 *  Assignment Operator
	 *
	 */
	PetriDish& operator=(const PetriDish &);

	/** Clean
	  * Removes all food and Bacteria from PetriDish
	*/
	void clean();

	/** AddFood
	  * Adds addedAmount (whole units) of food
	  * to the PetriDish
	  *
	  * @param addedAmount int the amount of food units added to the PetriDish
	  *
	*/
	void addFood(int addedAmount) {
		_foodLeft += addedAmount;
	}

	/** AddBacteria
	  * Adds a new Bacteria to the PetriDish
	  *
	  * @param newBacteriaPtr Bacteria* a pointer to new bacteria of type bacteriaType
	  *
	*/
	void addBacteria(Bacteria* newBacteriaPtr) {
		_bacterias.push_back(newBacteriaPtr);
	}

	/** Print
	  * Prints the Bacteria Colony and the amount of food
	*/
	void print() const;

	/** UpdatePopulation
	  * Update the population timeUnits times.
	  * For each update:
	  * 		- For each Bacteria (in the order the were added):
	  * 			1. The Bacteria can choose to eat.
	  * 			2. The Bacteria can choose to duplicate itself.
	  * 		- Then, all dead Bacteria are removed.
	  * 		- Finally, adds the cloned bacteria to the dish.
	  *
	  *  @param timeUnits int the number of units the time moves forward
	  *
	  * Takes ownership!
	*/
	void updatePopulation(int timeUnits);

private:
	std::vector<Bacteria*> _bacterias; /**contains all the bacterias pointers which
										  are in the PetriDish */
	int _foodLeft; // the amount of food remained in the PetriDish

	/** RemoveDeadBacteria
	  * Helper function to delete remove dead Bacteria
	*/
	void removeDeadBacteria();
};

#endif
