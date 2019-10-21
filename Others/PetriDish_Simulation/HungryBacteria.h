#ifndef HUNGRYBACTERIA_H_
#define HUNGRYBACTERIA_H_
#include "Bacteria.h"
#define HUNGRY_FOOD_UNITS_MULTIPLIER 2
#define HUNGRY_CURRENT_AGE_MULTIPLIER 0.5

 /* HungryBacteria
  *
  * A bacteria that consumes food twice as much as
  * how much was ate last time.
  * When duplicating- the currentAge is halved and consumedFood reset to 0.
 */
class HungryBacteria: public Bacteria{

public:

	/*
	 * Class Constructor
	 *
	 * @param bacteriaId int the new bacteria ID
	 * @param eatingRate int the eating rate of the bacteria
	 * @param adultAge int the age in which the bacteria is eligble to clone
	 * @param foodUnits int number of food units the bacteria will consume
	 */
	HungryBacteria( int bacteriaId, int eatingRate, int adultAge, int foodUnits );

	/** Copy Constructor
	 *
	 * @param  otherBacteria const HungryBacteria & - the HungryBacteria to be copied
	 */
	HungryBacteria(const HungryBacteria& otherBacteria);

	/*
	 * Class operator=
	 *Utilizes Base class operator=.
	 *
	 * @param rightHandSide const HungryBacteria & the assigning bacteria
	 * @return HungryBacteria& reference to this HungryBacteria.
	 */
	HungryBacteria& operator=(const HungryBacteria &rightHandSide)
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
	 * When duplicating the currentAge is reset to 0 and consumedFood is halved.
	 * The Bacteria class fields are duplicated.
	 *
	 * @return Bacteria* a pointer to new bacteria of type HungryBacteria
	 *
	 * Gives Ownership!
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
	virtual ~HungryBacteria();

private:
	const static std::string _name; //Class display name

};


#endif
