from src.application.ports.ad_source import AdSource
from src.application.ports.uow import UnitOfWork
from src.application.ports.usecases import IndexAdPort


class IndexAd(IndexAdPort):
    def __init__(self, uow: UnitOfWork, ad_source: AdSource) -> None:
        self._uow = uow
        self._ad_source = ad_source

    async def execute(self, ad_id: int) -> None:
        ad = await self._ad_source.get(ad_id)
        async with self._uow as u:
            if ad is None or ad.status != 'active':
                await u.search.delete(ad_id)

            else:
                await u.search.upsert(ad.ad_id, ad.title, ad.description, ad.price, ad.category, ad.city)
            await u.commit()
