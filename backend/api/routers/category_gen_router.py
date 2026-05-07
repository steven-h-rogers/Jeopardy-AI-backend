from fastapi import APIRouter, Depends

from backend.src.CategoryGenerator import CategoryGenerator
from backend.models.api_models import CategoryPayload

router = APIRouter(prefix='/category-generator',
                   tags=['category-generation'])

category_generator = CategoryGenerator()

@router.get('/')
async def health():
    return{'status':'category_generator is functional'}

# ! will need to restructure this endpoint
@router.post('/generate-categories/')
async def generate_categories(category_payload: CategoryPayload):
    num_categories = category_payload.num_categories
    # browser will handle custom categories
    category_list = category_generator.generate_categories_direct_structured(num_categories).categories
    return {'category-list': category_list}