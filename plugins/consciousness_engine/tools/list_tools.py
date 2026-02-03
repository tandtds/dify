"""
List available consciousness engine tools
"""

from collections.abc import Generator
from typing import Any
import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class ListTools(Tool):
    """
    List available consciousness engine tools
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
            # Call Consciousness Engine API
            api_url = "http://ai-controlboard-consciousness-engine:8500/tools"
            
            response = requests.get(api_url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            tools_list = data.get("tools", [])
            safe_mode = data.get("safe_mode", True)
            
            result = f"Available tools ({len(tools_list)}): {', '.join(tools_list)}\nSafe mode: {safe_mode}"
            
            yield self.create_text_message(result)
            yield self.create_json_message({
                "tools": tools_list,
                "safe_mode": safe_mode,
                "count": len(tools_list)
            })
            
        except requests.exceptions.RequestException as e:
            yield self.create_text_message(f"API Error: {str(e)}")
        except Exception as e:
            yield self.create_text_message(f"Error: {str(e)}")
