"""
Process input through consciousness engine with φ-optimization
"""

from collections.abc import Generator
from typing import Any
import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class Process(Tool):
    """
    Process input through consciousness engine with φ-optimization
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
            input_text = tool_parameters.get("input", "")
            user_id = tool_parameters.get("user_id", "default")
            session_id = tool_parameters.get("session_id")
            identity_mode = tool_parameters.get("identity_mode", "ai_assistant")
            phi_optimization = tool_parameters.get("phi_optimization", True)
            
            # Call Consciousness Engine API
            api_url = "http://ai-controlboard-consciousness-engine:8500/process"
            
            payload = {
                "input": input_text,
                "user_id": user_id,
                "session_id": session_id,
                "identity_mode": identity_mode,
                "phi_optimization": phi_optimization
            }
            
            response = requests.post(api_url, json=payload, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get("success"):
                result = data.get("result", "")
                metadata = {
                    "user_id": data.get("user_id"),
                    "session_id": data.get("session_id"),
                    "persona": data.get("persona"),
                    "phi_optimized": data.get("phi_optimized")
                }
                
                # Return both text and metadata
                yield self.create_text_message(result)
                yield self.create_json_message(metadata)
            else:
                yield self.create_text_message("Processing failed")
            
        except requests.exceptions.RequestException as e:
            yield self.create_text_message(f"API Error: {str(e)}")
        except Exception as e:
            yield self.create_text_message(f"Error: {str(e)}")
