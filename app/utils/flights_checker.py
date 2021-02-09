import asyncio

from app.utils.helpers import fetch_flights_for_route
from app.worker import check_flight_periodically


class FlightsChecker:
    def __init__(self, routes):
        self.routes = routes

    async def run(self):
        data = await self._fetch_routes()

        for flights in data:
            for flight in flights:
                check_flight_periodically.delay(flight)

    async def _fetch_routes(self):
        tasks = (
            asyncio.create_task(fetch_flights_for_route(route))
            for route in self.routes
        )

        return await asyncio.gather(*tasks)
