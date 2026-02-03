"""
Query Archon knowledge base via MCP integration
"""

from collections.abc import Generator
from typing import Any
import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class ArchonQuery(Tool):
    """
    Query Archon knowledge base via MCP integration
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
            query_text = tool_parameters.get("query", "")
            limit = tool_parameters.get("limit", 5)
            
            # Call Consciousness Engine API (Archon integration endpoint)
            api_url = "http://ai-controlboard-consciousness-engine:8500/archon/query"
            
            payload = {
                "query": query_text,
                "limit": int(limit)
            }
            
            response = requests.post(api_url, json=payload, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get("success"):
                results = data.get("results", [])
                
                if results:
                    result_text = f"Found {len(results)} results from Archon knowledge base:\n\n"
                    for i, result in enumerate(results, 1):
                        result_text += f"{i}. {result}\n"
                    yield self.create_text_message(result_text)
                    yield self.create_json_message({"results": results, "count": len(results)})
                else:
                    yield self.create_text_message("No results found in Archon knowledge base")
            else:
                yield self.create_text_message("Archon query failed")
            
        except requests.exceptions.RequestException as e:
            yield self.create_text_message(f"API Error: {str(e)}")
        except Exception as e:
            yield self.create_text_message(f"Error: {str(e)}")
