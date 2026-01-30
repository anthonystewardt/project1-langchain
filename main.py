from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import streamlit as st
import os
from dotenv import load_dotenv
import time

load_dotenv()


API_KEY_OPENAI = os.getenv("OPENAI_KEY")

# HumanMessage: significa un mensaje del usuario
# AIMessage: significa un mensaje generado por la IA
# SystemMessage: significa un mensaje del sistema (instrucciones iniciales)



def main():
    try:
        st.set_page_config(page_title="LangChain OpenAI Chat", page_icon="🤖")
        st.title("LangChain OpenAI Chat Example")
        st.markdown(
            """
            This is a simple chat application using LangChain and OpenAI's Chat API.
            """
        )
        with st.sidebar:
            st.header("Configuration")
            st.markdown("Configure your chat settings here.")
            # initialize chat model
            temperature_select = st.slider("Temperature", 0.0, 1.0, 0.5, 0.1)
            model_select = st.selectbox("Model", ["gpt-3.5-turbo", "gpt-4", "gpt-4o-mini"])
            
            # Configuración del streaming
            st.subheader("Streaming Settings")
            enable_streaming = st.checkbox("Enable streaming response", value=True)
            stream_speed = st.slider("Stream speed (seconds between words)", 0.01, 0.2, 0.05, 0.01) if enable_streaming else 0.05

        chat_model = ChatOpenAI(
            openai_api_key=API_KEY_OPENAI,
            model_name=model_select,
            temperature=temperature_select,
        )

        # historial de la conversación
        prompt_template = PromptTemplate(
            input_variables=["chat_history", "user_input"],
            template="""
            The following is a conversation between a human user and an AI assistant. The assistant is helpful, creative, clever, and very friendly.
            {chat_history}
            Human: {user_input}
            AI:""",
        )

        cadena = prompt_template | chat_model

        # initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []
        # generate previous chat messages
        for msg in st.session_state.messages:
            if isinstance(msg, SystemMessage):
                # No show system messages in the chat history
                continue
            role = "assistant" if isinstance(msg, AIMessage) else "user"

            with st.chat_message(role):
                st.markdown(msg.content)
        if st.button("Nueva Conversación"):
            st.session_state.messages = []
            st.rerun()
        # input text box
        question = st.chat_input("Type your message here...")
        # user input
        if question:
            # show inmediate user message
            with st.chat_message("user"):
                st.markdown(question)
            # save user message in chat history
            st.session_state.messages.append(HumanMessage(content=question))
            
            # get response from chat model with streaming
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                
                try:
                    if enable_streaming:
                        # Usar todo el historial de conversación para el contexto
                        # Usar stream para obtener la respuesta palabra por palabra
                        for chunk in chat_model.stream(st.session_state.messages):
                            if hasattr(chunk, 'content') and chunk.content:
                                full_response += chunk.content
                                message_placeholder.markdown(full_response + "▌")
                                time.sleep(stream_speed)  # Pausa configurable para efecto visual
                        
                        # Mostrar la respuesta final sin el cursor
                        message_placeholder.markdown(full_response)
                    else:
                        # Modo sin streaming (respuesta inmediata)
                        response = chat_model.invoke(st.session_state.messages)
                        full_response = response.content
                        message_placeholder.markdown(full_response)
                
                except Exception as e:
                    st.error(f"Error al generar respuesta: {str(e)}")
                    full_response = "Lo siento, hubo un error al generar la respuesta."
                    message_placeholder.markdown(full_response)
            
            # save IA message in chat history
            st.session_state.messages.append(AIMessage(content=full_response))
    
    except Exception as e:
        st.error(f"Error en la aplicación: {str(e)}")
        st.info("Por favor, verifica tu configuración y vuelve a intentar.")


if __name__ == "__main__":
    main()
