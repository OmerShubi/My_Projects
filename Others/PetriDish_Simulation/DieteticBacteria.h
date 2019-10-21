#ifndef DIETETICBACTERIA_H_
#define DIETETICBACTERIA_H_
#include "Bacteria.h"
#define DIETETIC_FOOD_UNITS_MULTIPLIER 0.5
#define DIETETIC_CURRENT_AGE_MULTIPLIER 2
#define DIETETIC_CONSUMED_FOOD_MULTIPLIER 0.5

/* DieteticBacteria
 *
 * A Bacteria that consumes food (foodUnits) half as much as
 * how much was ate last time
 * When duplicating the currentAge is reset to 0 and consumedFood is halved.
 */
class DieteticBacteria: public Bacteria{

public:

	/*
	 * Class Constructor
	 *
	 * @param bacteriaId int the new bacteria ID
	 * @param eatingRate int the eating rate of the bacteria
	 * @param adultAge int the age in which the bacteria is eligble to clone
	 * @param foodUnits int number of food units the bacteria will consume
	 */
	DieteticBacteria( int bacteriaId, int eatingRate,
			int adultAge, int foodUnits );

	/** Copy Constructor
	 *
	 * @param  otherBacteria const DieteticBacteria & - the DieteticBacteria to be copied
	 *
	 */
	DieteticBacteria(const DieteticBacteria& otherBacteria);

	/*
	 * Class operator=
	 *Utilizes Base class operator=.
	 *
	 * @param rightHandSide const DieteticBacteria & the assigning bacteria
	 * @return DieteticBacteria& reference to this DieteticBacteria.
	 */
	DieteticBacteria& operator=(const DieteticBacteria &rightHandSide)
	{
		if (this  == &rightHandSide) return *this;
		Bacteria::operator=(rightHandSide);
		return(*this);
	}

	/*
	 * clone
	 * Used to create a duplicate bacteria
	 * according to general bacteria and specific class definitions.
	 * First checks whether bacteria is ready to clone using
	 * the Bacteria::isReadyToClone() function.
	 *
	 * If the bacteria is not ready for cloning (above check does not pass)
	 * then returns NULL.
	 *
	 * When duplicating the currentAge is reset to 0 and consumedFood is halved.
	 * The Bacteria class fields are duplicated.
	 *
	 * Gives Ownership!
	 *
	 * @return Bacteria* a pointer to new bacteria of type DieteticBacteria
	 */
	virtual Bacteria* clone();

	/*
	 * print
	 * Prints to screen _name then calls the standard Bacteria::print()
	 */
	virtual void print() const;

	/*
	 * Class Destructor
	 */
	virtual ~DieteticBacteria();

private:
	const static std::string _name; //Class display name

};

#endif 
