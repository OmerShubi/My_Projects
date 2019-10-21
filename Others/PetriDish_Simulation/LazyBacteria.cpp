#include "LazyBacteria.h"

const std::string LazyBacteria::_name ("Lazy Bact.");


LazyBacteria::LazyBacteria( int bacteriaId, int eatingRate,
							int adultAge, int foodUnits ):
					Bacteria(bacteriaId, floor(eatingRate*LAZY_EATING_RATE_MULTIPLIER),
					floor(adultAge*LAZY_ADULT_AGE_MULTIPLIER), foodUnits)
{}

LazyBacteria::LazyBacteria(const LazyBacteria& otherBacteria):
							Bacteria(otherBacteria)
{}

Bacteria* LazyBacteria::clone()
{
	if (Bacteria::isReadyToClone() == false)
	{
		return NULL;
	}
	else // duplicates the bacteria according to specific class rules
	{
		return (new LazyBacteria(*this));
	}
}


void LazyBacteria::print() const
{
	std::cout<<LazyBacteria::_name;
	Bacteria::print();
}

LazyBacteria::~LazyBacteria()
{}
