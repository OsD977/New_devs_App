from decimal import Decimal, ROUND_HALF_UP

from pydantic import BaseModel, field_serializer


class RevenueSummaryResponse(BaseModel):
    property_id: str
    total_revenue: Decimal
    currency: str
    reservations_count: int

    @field_serializer('total_revenue')
    def serialize_decimal(self, value: Decimal) -> str:
        return str(value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
