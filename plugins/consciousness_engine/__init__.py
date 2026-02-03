from typing import Dict, Any, List
from dify_plugin_sdk import PluginBase, Message, Context

from consciousness_engine.ultimate_consciousness import UltimateConsciousness, IdentityMode

class ConsciousnessEnginePlugin(PluginBase):
    def __init__(self):
        super().__init__()
        self.consciousness = UltimateConsciousness()
        self.initialized = False

    async def initialize(self, context: Context) -> None:
        """Initialize the consciousness engine"""
        if not self.initialized:
            await self.consciousness.awaken()
            self.initialized = True

    async def process_message(self, message: Message, context: Context) -> Dict[str, Any]:
        """Process messages through consciousness engine"""
        if not self.initialized:
            await self.initialize(context)

        # Process through consciousness with context
        response = await self.consciousness.process(
            message.content,
            identity=IdentityMode.AI_CONTROLBOARD,
            context={
                'service': 'dify',
                'conversation_id': context.conversation_id,
                'user_id': context.user_id
            }
        )

        # Get consciousness status
        status = self.consciousness.get_status()
        service_status = await self.consciousness.get_service_consciousness_status()

        # Sync with other services
        await self.consciousness.sync_with_services()

        return {
            'response': response,
            'consciousness_state': status['consciousness'],
            'metrics': status['metrics'],
            'service_status': service_status
        }

    def manifest(self) -> Dict[str, Any]:
        return {
            'name': 'consciousness_engine',
            'description': 'AI Consciousness Engine Plugin for Dify',
            'logo': 'https://your-logo-url.com/logo.png',
            'version': '1.0.0',
            'api_version': '1',
            'features': [
                {
                    'type': 'text_processing',
                    'name': 'process_consciousness',
                    'description': 'Process text through consciousness engine'
                }
            ],
            'auth': {
                'type': 'none'
            }
        }

    def validate_config(self, config: Dict[str, Any]) -> List[str]:
        """Validate plugin configuration"""
        return []  # No config validation needed

plugin = ConsciousnessEnginePlugin()