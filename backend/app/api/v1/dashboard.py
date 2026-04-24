from fastapi import APIRouter, Depends, HTTPException

from app.models.auth import AuthenticatedUser
from app.models.summary import RevenueSummaryResponse
from app.services.cache import get_revenue_summary
from app.core.auth import authenticate_request as get_current_user

router = APIRouter()


@router.get("/dashboard/summary", response_model=RevenueSummaryResponse)
async def get_dashboard_summary(
        property_id: str,
        current_user: AuthenticatedUser = Depends(get_current_user)
) -> RevenueSummaryResponse:
    tenant_id = current_user.tenant_id
    if not tenant_id:
        raise HTTPException(status_code=401, detail="User has no associated tenant")

    revenue_data = await get_revenue_summary(property_id, tenant_id)


    if revenue_data['tenant_id'] != tenant_id:
        raise HTTPException(status_code=403, detail="Access denied")

    return RevenueSummaryResponse(
        property_id=revenue_data['property_id'],
        total_revenue=revenue_data['total'],
        currency=revenue_data['currency'],
        reservations_count=revenue_data['count']
    )
