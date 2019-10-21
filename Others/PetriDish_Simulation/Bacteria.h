#ifndef BACTERIA_H
#define BACTERIA_H
#include <iostream>
#include <string>
#include <cmath>
#define DAYS_WITHOUT_FOOD 3
#define ZERO 0


/**
  * Bacteria

  * Pure virtual Class which contains the properties of the relevant bacteria:
  * bacteriaId, eatingRate, adultAge, foodUnits,
  * currentAge,consumedFood, timeUnitWithoutFood.

  * The class has the following methods:
  * clone, grow, eat, print, isDead, isReadyToClone.
  * These methods determine the bacterias' status, number and behavior

  * The class can print the bacteria relevant properties
*/
class Bacteria {
public:
	/** Class Constructor
	 *
	 * @param bacteriaId int the new bacteria ID
	 * @param eatingRate int the eating rate of the bacteria
	 * @param adultAge int the age in which the bacteria is eligble to clone
	 * @param foodUnits int number of food units the bacteria will consume
	 */
	Bacteria(int the_bacteriaId, int the_eatingRate,
			 int the_adultAge, int the_foodUnits);

	/** Copy Constructor
	 *
	 * @param  original const Bacteria & - the original Bacteria to be copied
	 */
	Bacteria(const Bacteria &original);

	/** Clone
	  * Clones the bacteria
	  * Implemented by inherited classes
	  *
	  *@return Bacteria* a pointer to a new bacteria of type bacteriaType
	*/
	virtual Bacteria* clone() = 0;

	/** Class Destructor
	*/
	virtual ~Bacteria (){}

	/** Assignment Operator
	*/
	Bacteria& operator=(const Bacteria &);

	/** Grow
	  * Increases currentAge by one.
	 */
	void grow()
	{
		_currentAge++;
	}


	/** Eat
	  * Feeds the bacteria if needed

	  * First determines whether the Bacteria should eat according to
	  * whether _currentAge is modulo _eatingRate.
	  * If so, eats _foodUnits amount of food, or foodLeft,
	  * the smaller between them.
	  * Finally, updated foodLeft with updated amount left.
	  *
	  * @param foodLeft int& the amount of food remained in the PetriDish
	  *
	*/
	void eat(int& foodLeft);


	/** Print
	  * Prints the Bacteria's Id and age (age after the last period)
	 */
	virtual void print() const;

	/** IsDead
	  * Determines whether the bacteria is dead

	  * Checks whether the Bacteria is dead or alive.
	  * Bacteria dies if it hasn't eaten 3 or more times.
	  * Returns true if dead and false otherwise.
	*/
	bool isDead() const { return (_timeUnitWithoutFood >= DAYS_WITHOUT_FOOD);}

protected:
	/** IsReadyToClone
	    * Checks whether the Bacteria is ready to clone.
	    * Meaning:
	    * 		1. _currentAge is equal or higher than _adultAge
	    * 		2. _consumedFood is higher than _currentAge

	   * Helper function for Clone function.
	   * Returns true if ready, false otherwise.
	 */
	bool isReadyToClone() const
	{
		return ((_currentAge >= _adultAge) && (_consumedFood > _currentAge));
	}
	int _currentAge; // the current age of this bacteria
	int _consumedFood; // the amount of food this bacteria consumed until now

private:
	int _bacteriaId; // defines this bacteria type
	int _eatingRate; // states the time units gap in which the bacteria doesn't eat
	int _adultAge; // this bacteria can clone itself if it passed this age
	int _foodUnits; //the amount of food units consumed by the bacteria any time it eats
	int _timeUnitWithoutFood; // counts the time units this bacteria hasn't eaten
};

#endif
