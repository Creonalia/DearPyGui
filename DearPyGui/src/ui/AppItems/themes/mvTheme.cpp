#include "mvTheme.h"
#include "mvContext.h"
#include <array>
#include "mvItemRegistry.h"
#include "mvLog.h"
#include "mvPythonExceptions.h"
#include "mvThemeComponent.h"

namespace Marvel {

	mvTheme::mvTheme(mvUUID uuid)
		:
		mvAppItem(uuid)
	{
		_show = false;
	}

	void mvTheme::draw(ImDrawList* drawlist, float x, float y)
	{
		for (auto& child : _children[1])
		{
			auto comp = static_cast<mvThemeComponent*>(child.get());
			if (comp->_specificType == (int)mvAppItemType::All || comp->_specificType == _specificType)
			{
				if (_specificEnabled == comp->_specificEnabled)
				{
					child->draw(drawlist, x, y);
				}
				
			}
			if(comp->_specificType != _specificType)
			{
				if (_specificEnabled == comp->_specificEnabled)
				{
					comp->_oldComponent = *comp->_specificComponentPtr;
					*comp->_specificComponentPtr = child;
				}
				else
				{
					comp->_oldComponent = *comp->_specificDisabledComponentPtr;
					*comp->_specificDisabledComponentPtr = child;
				}
			}
		}
	}

	void mvTheme::customAction(void* data)
	{

		for (auto& child : _children[1])
		{
			auto comp = static_cast<mvThemeComponent*>(child.get());
			if (comp->_specificType == (int)mvAppItemType::All || comp->_specificType == _specificType)
			{
				if (_specificEnabled == comp->_specificEnabled)
				{
					child->customAction(data);
				}
			}
			if (comp->_specificType != _specificType)
			{
				if (_specificEnabled == comp->_specificEnabled)
				{
					*comp->_specificComponentPtr = comp->_oldComponent;
				}
				else
				{
					*comp->_specificDisabledComponentPtr = comp->_oldComponent;
				}
			}
		}
	}
}