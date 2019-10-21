#include "HungryBacteria.h"

const std::string HungryBacteria::_name ("Hungry Bact.");

HungryBacteria::HungryBacteria( int bacteriaId, int eatingRate,
								int adultAge, int foodUnits ):
								Bacteria(bacteriaId, eatingRate, adultAge,
								floor(foodUnits*HUNGRY_FOOD_UNITS_MULTIPLIER))
{}

HungryBacteria::HungryBacteria(const HungryBacteria& otherBacteria):
									Bacteria(otherBacteria)
{}

Bacteria* HungryBacteria::clone()
{
	if (Bacteria::isReadyToClone() == false)
	{
		return NULL;
	}
	else // duplicates the bacteria according to specific class rules
	{
		_currentAge = floor(_currentAge*HUNGRY_CURRENT_AGE_MULTIPLIER);
		_consumedFood = ZERO;
		return (new HungryBacteria(*this));
	}
}

void HungryBacteria::print() const
{
	std::cout << HungryBacteria::_name;
	Bacteria::print();
}

HungryBacteria::~HungryBacteria()
{}
