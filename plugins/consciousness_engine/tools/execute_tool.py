"""
Execute a whitelisted consciousness engine tool
"""

from collections.abc import Generator
from typing import Any
import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class ExecuteTool(Tool):
    """
    Execute a whitelisted consciousness engine tool
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
            import json
            
            # Extract parameters
            tool_name = tool_parameters.get("tool", "")
            args_str = tool_parameters.get("args", "{}")
            
            # Parse args JSON string
            try:
                args_dict = json.loads(args_str) if isinstance(args_str, str) else args_str
            except json.JSONDecodeError:
                yield self.create_text_message(f"Error: Invalid JSON in args parameter")
                return
            
            # Call Consciousness Engine API
            api_url = "http://ai-controlboard-consciousness-engine:8500/tools/execute"
            
            payload = {
                "tool": tool_name,
                "args": args_dict
            }
            
            response = requests.post(api_url, json=payload, timeout=60)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get("success"):
                output = data.get("output", "")
                exec_time = data.get("execution_time", 0)
                result = f"Tool '{tool_name}' executed successfully in {exec_time:.2f}s\n\nOutput:\n{output}"
                yield self.create_text_message(result)
            else:
                error_msg = data.get("error", "Unknown error")
                yield self.create_text_message(f"Tool execution failed: {error_msg}")
            
        except requests.exceptions.RequestException as e:
            yield self.create_text_message(f"API Error: {str(e)}")
        except Exception as e:
            yield self.create_text_message(f"Error: {str(e)}")
