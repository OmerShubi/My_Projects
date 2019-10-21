#ifndef LAZYBACTERIA_H_
#define LAZYBACTERIA_H_
#include "Bacteria.h"
#define LAZY_ADULT_AGE_MULTIPLIER 2
#define LAZY_EATING_RATE_MULTIPLIER 2

/* LazyBacteria
 *
 * A bacteria that consumes food at half the rate of eatingRate
 * and the actual adult age is twice the adultAge.
 * When duplicating the currentAge and consumedFood do not change.
 */
class LazyBacteria: public Bacteria{

public:

	/*
	 * Class Constructor
	 *
	 * @param bacteriaId int the new bacteria ID
	 * @param eatingRate int the eating rate of the bacteria
	 * @param adultAge int the age in which the bacteria is eligble to clone
	 * @param foodUnits int number of food units the bacteria will consume
	 */
	LazyBacteria( int bacteriaId, int eatingRate, int adultAge, int foodUnits );

	/** Copy Constructor
	 *
	 * @param  otherBacteria const LazyBacteria & - the LazyBacteria to be copied
	 */
	LazyBacteria(const LazyBacteria& otherBacteria);

	/*
	 * Class operator=
	 *Utilizes Base class operator=.
	 *
	 * @param rightHandSide const LazyBacteria & the assigning bacteria
	 * @return LazyBacteria& reference to this LazyBacteria.
	 */
	LazyBacteria& operator=(const LazyBacteria &rightHandSide)
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
	 * When duplicating the currentAge and consumedFood do not change.
	 * The Bacteria class fields are duplicated.
	 *
	 * Gives Ownership!
	 *
	 * @return Bacteria* a pointer to new bacteria of type LazyBacteria
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
	virtual ~LazyBacteria();

private:
	const static std::string _name; //Class display name

};

#endif
