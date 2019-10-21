#include <cstdlib>
#include <iostream>
#include <string>
#include "PetriDish.h"
#include "LazyBacteria.h"
#include "ActiveBacteria.h"
#include "HungryBacteria.h"
#include "DieteticBacteria.h"


typedef enum { ADD_BACTERIA=0, ADD_FOOD, CLEAN_PETRI, PRINT,
	UPDATE_TIME, QUIT_CODE } CommandsEnum;
const std::string consoleCommands[]= {"add_bacteria",
		"add_food", "clean_petri", "print","update_time", "quit" };

typedef enum { ACTIVE_BACTERIA=0, LAZY_BACTERIA, HUNGRY_BACTERIA
	, DIETETIC_BACTERIA } BacteriaTypes;

const int NUM_OF_BACTERIA_TYPES = 4;


/**
 * createBacteria
 * Creates new bacteria, where the type of the bacteria is cyclicly
 * determined by the order of creation, using BacteriaTypes enum.
 *
 * @param bacteriaId int the new bacteria ID
 * @param eatingRate int the eating rate of the bacteria
 * @param adultAge int the age in which the bacteria is eligble to clone
 * @param bacteriaType int& newly created bacteria type (changed in function)
 * @param foodUnits int number of food units the bacteria will consume
 * @return Bacteria* a pointer to new bacteria of type bacteriaType
 *
 */
Bacteria* createBacteria(int bacteriaId, int eatingRate, int adultAge,
		int& bacteriaType, int foodUnits);

int main()
{
    std::string input;
    std::cin >> input;
    PetriDish bioPerti;
    
    int bacteriaType(ACTIVE_BACTERIA);

    while ( input != consoleCommands[QUIT_CODE] )
    {
      if (  input == consoleCommands[ADD_BACTERIA] )
      {
            int bacteriaId(0), eatingRate(0), adultAge(0), foodUnits(0);
            std::cin >> bacteriaId >> eatingRate >> adultAge >> foodUnits;
            
            Bacteria* pBacteria = createBacteria(bacteriaId, eatingRate, adultAge,
					bacteriaType, foodUnits);
            bioPerti.addBacteria( pBacteria );
      }  
      else if (  input == consoleCommands[ADD_FOOD] )
      {
            int iFoodCount(0);
            std::cin >> iFoodCount;
            bioPerti.addFood( iFoodCount );
      }     
      else if (  input == consoleCommands[CLEAN_PETRI] )
      {
            bioPerti.clean();
      }     
      else if (  input == consoleCommands[PRINT] )
      {
            bioPerti.print();
      }   
      else if (  input == consoleCommands[UPDATE_TIME] )
      {
            int iTime(0);
            std::cin >> iTime;
            bioPerti.updatePopulation( iTime );
      }    
      std::cin >> input;
    }

    return EXIT_SUCCESS;
}

Bacteria* createBacteria(int bacteriaId, int eatingRate, int adultAge,
		int& bacteriaType, int foodUnits)
{
	Bacteria* pBacteria = NULL;
	// cycle on types of bacteria in order of creation,
	// and cycle the indicator to next type
	switch ((bacteriaType++) % NUM_OF_BACTERIA_TYPES) {
	case ACTIVE_BACTERIA:
		pBacteria = new ActiveBacteria(bacteriaId, eatingRate, adultAge,
				foodUnits);
		break;
	case LAZY_BACTERIA:
		pBacteria = new LazyBacteria(bacteriaId, eatingRate, adultAge,
				foodUnits);
		break;
	case HUNGRY_BACTERIA:
		pBacteria = new HungryBacteria(bacteriaId, eatingRate, adultAge,
				foodUnits);
		break;
	case DIETETIC_BACTERIA:
		pBacteria = new DieteticBacteria(bacteriaId, eatingRate, adultAge,
				foodUnits);
		break;
	}
	return pBacteria;
}
