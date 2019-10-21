#include "ActiveBacteria.h"

const std::string ActiveBacteria::_name ("Active Bact.");

ActiveBacteria::ActiveBacteria( int bacteriaId, int eatingRate,
								int adultAge, int foodUnits ):
		Bacteria(bacteriaId, floor(eatingRate*ACTIVE_EATING_RATE_MULTIPLIER),
				floor(adultAge*ACTIVE_ADULT_AGE_MULTIPLIER), foodUnits)
{}

ActiveBacteria::ActiveBacteria(const ActiveBacteria& otherBacteria):
							   Bacteria(otherBacteria)
{}

Bacteria* ActiveBacteria::clone()
{
	if (Bacteria::isReadyToClone() == false)
	{
		return NULL;
	}
	else // duplicates the bacteria according to specific class rules
	{
		_currentAge = floor(_currentAge*ACTIVE_CURRENT_AGE_MULTIPLIER);
		_consumedFood = ZERO;
		return (new ActiveBacteria(*this));
	}
}

void ActiveBacteria::print() const
{
	std::cout<<ActiveBacteria::_name;
	Bacteria::print();
}


ActiveBacteria::~ActiveBacteria()
{}
