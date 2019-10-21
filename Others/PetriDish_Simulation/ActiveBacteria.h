#ifndef ACTIVEBACTERIA_H_
#define ACTIVEBACTERIA_H_
#include "Bacteria.h"
#define ACTIVE_ADULT_AGE_MULTIPLIER 0.5
#define ACTIVE_CURRENT_AGE_MULTIPLIER 2
#define ACTIVE_EATING_RATE_MULTIPLIER 0.5


/* ActiveBacteria
 *
 * A bacteria that consumes food twice as fast as the eatingRate
 * and its actual adult age is half of adultAge.
 * When duplicating the currentAge of this bacteria is doubled
 * and the consumedFood is reset to 0.
 */
class ActiveBacteria: public Bacteria{

public:

	/*
	 * Class Constructor
	 *
	 * @param bacteriaId int the new bacteria ID
	 * @param eatingRate int the eating rate of the bacteria
	 * @param adultAge int the age in which the bacteria is eligible to clone
	 * @param foodUnits int number of food units the bacteria will consume
	 *
	 */
	ActiveBacteria( int bacteriaId, int eatingRate,
			int adultAge, int foodUnits );

	/** Copy Constructor
	 *
	 * @param  otherBacteria const ActiveBacteria & - the ActiveBacteria to be copied
	 */
	ActiveBacteria(const ActiveBacteria& otherBacteria);

	/*
	 * Class operator=
	 *Utilizes Base class operator=.
	 *
	 * @param rightHandSide const ActiveBacteria & the assigning bacteria
	 * @return ActiveBacteria& reference to this ActiveBacteria.
	 */
	ActiveBacteria& operator=(const ActiveBacteria &rightHandSide)
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
	 * the Bacteria::isReadyToClone function.
	 *
	 * If the bacteria is not ready for cloning (above check does not pass)
	 * then returns NULL.
	 *
	 * When duplicating the currentAge is doubled and consumedFood is reset to 0.
	 * The Bacteria class fields are duplicated.
	 *
	 * Gives Ownership!
	 *
	 * @return Bacteria* a pointer to new bacteria of type ActiveBacteria
	 */
	virtual Bacteria* clone();

	/*
	 * print
	 * Prints to screen _name then calls the standard Bacteria::print()
	 *
	 * @return Bacteria* a pointer to a new bacteria of type ActiveBacteria
	 *
	 */
	virtual void print() const;

	/*
	 * Class Destructor
	 */
	virtual ~ActiveBacteria();

private:
	const static std::string _name; //Class display name

};


#endif
