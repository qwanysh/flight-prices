from datetime import timedelta, date
from urllib.parse import urlencode

import httpx

from app.models import Route, Flight


def sort_flights_by_price(flights):
    return sorted(flights, key=lambda flight: flight['price'])


def get_date_to(date_from):
    DAYS_IN_MONTH = 31

    return date_from + timedelta(days=DAYS_IN_MONTH)


def make_url(base_url, query_params):
    return base_url + '?' + urlencode(query_params)


def get_flight_url(route):
    DATE_FORMAT = '%d/%m/%Y'

    date_from = date.today()
    fly_from, fly_to = route

    query_params = {
        'partner': 'picky',
        'adults': 1,
        'date_from': date_from.strftime(DATE_FORMAT),
        'date_to': get_date_to(date_from).strftime(DATE_FORMAT),
        'fly_from': fly_from,
        'fly_to': fly_to,
    }

    return make_url('https://api.skypicker.com/flights', query_params)


def get_check_url(booking_token):
    query_params = {
        'v': 2,
        'booking_token': booking_token,
        'bnum': 1,
        'pnum': 1,
    }

    return make_url(
        'https://booking-api.skypicker.com/api/v0.1/check_flights',
        query_params,
    )


async def fetch_flights_for_route(route):
    url = get_flight_url(route)

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        flights = [{
            'route': route,
            'booking_token': item['booking_token'],
            'price': item['price'],
        } for item in response.json()['data']]

        return flights


def fetch_flight_check(flight):
    url = get_check_url(flight['booking_token'])
    response = httpx.get(url).json()

    return {
        'checked': response['flights_checked'],
        'invalid': response['flights_invalid'],
    }


def save_flight(flight):
    fly_from, fly_to = flight['route']
    route, is_created = Route.get_or_create(fly_from=fly_from, fly_to=fly_to)
    Flight.create(route=route, price=flight['price'])
