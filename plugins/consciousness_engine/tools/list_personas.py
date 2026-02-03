"""
List available AI personas/identity modes
"""

from collections.abc import Generator
from typing import Any
import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class ListPersonas(Tool):
    """
    List available AI personas/identity modes
    """
    
    def _invoke(
        self,
        tool_parameters: dict[str, Any]
    ) -> Generator[ToolInvokeMessage]:
        """
        Invoke the tool
        
        Args:
            tool_parameters: Tool parameters
            
        Yields:
            ToolInvokeMessage: Tool response messages
        """
        try:
            # Extract parameters
            include_details = tool_parameters.get("include_details", False)
            
            # Call Consciousness Engine API
            api_url = "http://ai-controlboard-consciousness-engine:8500/personas"
            
            response = requests.get(api_url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            personas = data.get("personas", [])
            default_persona = data.get("default", "ai_assistant")
            
            if include_details:
                # Return detailed JSON
                yield self.create_json_message({
                    "personas": personas,
                    "default": default_persona,
                    "count": len(personas)
                })
            else:
                # Return simple text list
                persona_names = [p["key"] for p in personas]
                result = f"Available personas ({len(personas)}): {', '.join(persona_names)}\nDefault: {default_persona}"
                yield self.create_text_message(result)
            
        except requests.exceptions.RequestException as e:
            yield self.create_text_message(f"API Error: {str(e)}")
        except Exception as e:
            yield self.create_text_message(f"Error: {str(e)}")
