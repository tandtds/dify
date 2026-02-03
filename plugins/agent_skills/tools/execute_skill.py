"""
Execute a registered agent skill
"""

from collections.abc import Generator
from typing import Any
import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class ExecuteSkill(Tool):
    """
    Execute a registered agent skill
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
            skill_name = tool_parameters.get("skill_name", "")
        input_data = tool_parameters.get("input_data", "")
        timeout = tool_parameters.get("timeout", "")
            
            # TODO: Implement your tool logic here
            # Example: Make API call, process data, etc.
            
            # For now, return a simple response
            result = f"Processed with parameters: {skill_name, input_data, timeout}"
            
            # Return text message
            yield self.create_text_message(result)
            
            # Alternative return types:
            # yield self.create_json_message({...})  # JSON response
            # yield self.create_link_message(url)  # Link response
            # yield self.create_image_message(url)  # Image response
            # yield self.create_file_message(file)  # File response
            
        except Exception as e:
            yield self.create_text_message(f"Error: {str(e)}")
