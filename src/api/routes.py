from fastapi import APIRouter, HTTPException

from api.schemas import ChatRequest, ChatResponse
from services.chat_service import ChatService
from utils.logger import logger

router = APIRouter()

chat_service = ChatService()


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    logger.info("API Request: %s", request.message)

    try:

        response = ""

        for chunk in chat_service.stream_response(
            request.message
        ):
            response += chunk

        return ChatResponse(
            response=response
        )

    except Exception as e:

        logger.exception(e)

        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )