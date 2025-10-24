import os
import asyncio
from dotenv import load_dotenv

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.contents import ChatHistory
from semantic_kernel.connectors.ai.open_ai import OpenAIChatPromptExecutionSettings

async def main():
    # Carrega .env
    load_dotenv()

    # Configurar chave de API da OpenAI
    os.environ["OPENAI_API_KEY"] = os.getenv("OPEN_AIKEY")

    # Inicializa Kernel
    kernel = Kernel()

    # Configura o serviço de chat
    service = OpenAIChatCompletion(ai_model_id="gpt-4o-mini")
    kernel.add_service(service)

    # Define prompt
    history = ChatHistory(system_message="Você é um assistente prestativo.")
    history.add_user_message("Olá, como posso usar o Semantic Kernel com a OpenAI?")

    # Executa chamada
    response = await service.get_chat_message_content(
        chat_history=history,
        settings=OpenAIChatPromptExecutionSettings()
    )

    # Exibe resposta
    print(response.content)

if __name__ == "__main__":
    asyncio.run(main())
