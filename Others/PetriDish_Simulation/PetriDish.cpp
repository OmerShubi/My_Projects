#include "PetriDish.h"
typedef enum
{
	OUT_ID = 0, OUT_AGE, OUT_FOOD
} OutputEnum;
const std::string OUTPUT_FIELDS[] = { "Bacteria ID: ", "Age: ", "Food left: " };

PetriDish::PetriDish():_foodLeft(0){}

PetriDish::PetriDish(const PetriDish &original) : _foodLeft(original._foodLeft)
{
	for (std::vector<Bacteria*>::size_type i = 0; i < original._bacterias.size(); i++)
	{
		Bacteria* _newBacteria(original._bacterias[i]);
		_bacterias.push_back(_newBacteria);
	}
}

PetriDish& PetriDish::operator=(const PetriDish &rightHandSide)
{
	if (this  == &rightHandSide) return *this; //check for self assignment
	_foodLeft = rightHandSide._foodLeft;
	for (std::vector<Bacteria*>::size_type i = 0;
			 i < rightHandSide._bacterias.size(); i++)
	{
			Bacteria* _newBacteria(rightHandSide._bacterias[i]);
			_bacterias.push_back(_newBacteria);
	}
	return *this;
}

void PetriDish::clean()
{
	_foodLeft = 0;
	for (std::vector< Bacteria* >::iterator it = _bacterias.begin() ;
			it != _bacterias.end(); ++it)
	   {
	     delete (*it);
	   }
	_bacterias.clear();
}

void PetriDish::print() const
{
	for (std::vector<Bacteria*>::size_type i = 0; i < _bacterias.size(); i++)
	{
		_bacterias[i]->print();
	}
	std::cout << OUTPUT_FIELDS[OUT_FOOD] << _foodLeft << std::endl;
}

void PetriDish::updatePopulation(int timeUnits)
{
	for (int j = 0; j < timeUnits; j++)
	{
		std::vector<Bacteria*> temp_bacterias;
		for (std::vector<Bacteria*>::size_type i = 0; i < _bacterias.size();
				i++)
		{
			_bacterias[i]->eat(_foodLeft);
			Bacteria* temp_bacteria(_bacterias[i]->clone());
			if (temp_bacteria != NULL) // add the new bacteria to the temporary vector
			{
				temp_bacterias.push_back(temp_bacteria);
			}
			else
			{
				_bacterias[i]->grow();
			}
		}
		this->removeDeadBacteria();
		for (std::vector<Bacteria*>::size_type k = 0; k < temp_bacterias.size();
				k++) {
			this->addBacteria(temp_bacterias[k]);
		}
	}
}

void PetriDish::removeDeadBacteria()
{
	for (std::vector<Bacteria*>::iterator iter = _bacterias.begin();
			iter != _bacterias.end();)
	{
		if ((*iter)->isDead() == true)
		{
			delete (*iter);
			iter = _bacterias.erase((iter));
		}
		else
		{
			iter++;
		}
	}
}
