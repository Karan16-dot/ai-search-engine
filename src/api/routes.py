from fastapi import APIRouter, HTTPException


from fastapi.responses import StreamingResponse

from api.stream import generate_stream


from api.schemas import ChatRequest, ChatResponse
from services.chat_service import ChatService
from utils.logger import logger

router = APIRouter()

chat_service = ChatService()


@router.post(
    "/chat",
    response_model=ChatResponse,
    summary="Chat with AI",
    description="Send a prompt to the AI model and receive a response."
)
async def chat(request: ChatRequest):

    logger.info("API Request: %s", request.message)

    try:
        response = await chat_service.chat(request.message)

        return ChatResponse(
            response=response
        )

    except Exception:
        logger.exception("Error while processing API request.")

        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )


@router.post("/stream")
async def stream_chat(request: ChatRequest):

    return StreamingResponse(
        generate_stream(request.message),
        media_type="text/event-stream",
    )