from fastapi import APIRouter

from backend.src.QuestionSummarizer import QuestionSummarizer

from backend.models.api_models import QuestionSummaryPayload, QuestionTopicPayload

router = APIRouter(prefix='/summarizer',
                   tags=['summarizer'])

question_summarizer = QuestionSummarizer()


@router.get('/')
async def health():
    return{'status':'summarizer is functional'}

@router.post('/summarize-question/')
async def summarize_question(question_summary_payload: QuestionSummaryPayload):
    question = question_summary_payload.question
    summary = question_summarizer.summarize_question(question)
    return {'summary': summary.summary}

@router.post('/extract-topic/')
async def summarize_question(question_topic_payload: QuestionTopicPayload):
    question = question_topic_payload.question
    topic = question_summarizer.extract_topic(question)
    return {'topic': topic.summary}
