"""
Execute an Archon agent task
"""

from collections.abc import Generator
from typing import Any
import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class AgentExecute(Tool):
    """
    Execute an Archon agent task
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
            task = tool_parameters.get("task", "")
        context = tool_parameters.get("context", "")
            
            # TODO: Implement your tool logic here
            # Example: Make API call, process data, etc.
            
            # For now, return a simple response
            result = f"Processed with parameters: {task, context}"
            
            # Return text message
            yield self.create_text_message(result)
            
            # Alternative return types:
            # yield self.create_json_message({...})  # JSON response
            # yield self.create_link_message(url)  # Link response
            # yield self.create_image_message(url)  # Image response
            # yield self.create_file_message(file)  # File response
            
        except Exception as e:
            yield self.create_text_message(f"Error: {str(e)}")
