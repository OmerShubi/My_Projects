#include "Bacteria.h"

typedef enum
{
	OUT_ID = 0, OUT_AGE, OUT_FOOD
} OutputEnum;
const std::string OUTPUT_FIELDS[] = { "Bacteria ID: ", "Age: ", "Food left: " };

Bacteria::Bacteria(int the_bacteriaId, int the_eatingRate, int the_adultAge,
	        	int the_foodUnits) : _currentAge(0), _consumedFood(0),
	        	_bacteriaId(the_bacteriaId),_eatingRate(the_eatingRate),
				_adultAge(the_adultAge),_foodUnits(the_foodUnits),
				_timeUnitWithoutFood(0)
{}

Bacteria::Bacteria(const Bacteria &original) : _currentAge(0),_consumedFood(0),
		_bacteriaId(original._bacteriaId),   _eatingRate(original._eatingRate),
		_adultAge(original._adultAge),
				   _foodUnits(original._foodUnits), _timeUnitWithoutFood(0)
{}

Bacteria& Bacteria::operator=(const Bacteria &rightHandSide)
{
  if (this  == &rightHandSide) return *this;    //check for self assignment
  _bacteriaId = rightHandSide._bacteriaId;
  _eatingRate = rightHandSide._eatingRate;
  _adultAge = rightHandSide._adultAge;
  _foodUnits = rightHandSide._foodUnits;
  _currentAge = rightHandSide._currentAge;
  _consumedFood = rightHandSide._consumedFood;
  _timeUnitWithoutFood = rightHandSide._timeUnitWithoutFood;
  return *this;
}

void Bacteria::eat(int& foodLeft)
{
	if (_currentAge % _eatingRate == ZERO) // time to eat
	{
		if (foodLeft == ZERO)
		{
			_timeUnitWithoutFood++;
		}
		else if (_foodUnits <= foodLeft) // the bacteria can eat according to its need
		{
			_consumedFood += _foodUnits;
			foodLeft -= _foodUnits;
			//_timeUnitWithoutFood = ZERO;
		}
		else /** the bacteria can eat only the food that remained and not according to
				 its need*/
		{
			_consumedFood += foodLeft;
			foodLeft = ZERO;
			//_timeUnitWithoutFood = ZERO;
		}
	}
}

void Bacteria::print() const
{
	std::cout << OUTPUT_FIELDS[OUT_ID] << _bacteriaId << " "
			<< OUTPUT_FIELDS[OUT_AGE] << _currentAge << std::endl;
}
