#include "DieteticBacteria.h"

const std::string DieteticBacteria::_name ("Dietetic Bact.");

DieteticBacteria::DieteticBacteria( int bacteriaId, int eatingRate,
									int adultAge, int foodUnits ):
							Bacteria(bacteriaId, eatingRate,
							adultAge, floor(foodUnits*DIETETIC_FOOD_UNITS_MULTIPLIER))
{}

DieteticBacteria::DieteticBacteria(const DieteticBacteria& otherBacteria):
									Bacteria(otherBacteria)
{}

Bacteria* DieteticBacteria::clone()
{
	if (Bacteria::isReadyToClone() == false)
	{
		return NULL;
	}
	else // duplicates the bacteria according to specific class rules
	{
		_currentAge = ZERO;
		_consumedFood = floor(_consumedFood*DIETETIC_CONSUMED_FOOD_MULTIPLIER);
		return (new DieteticBacteria(*this));
	}
}

void DieteticBacteria::print() const
{
	std::cout<<DieteticBacteria::_name;
	Bacteria::print();
}

DieteticBacteria::~DieteticBacteria()
{}
