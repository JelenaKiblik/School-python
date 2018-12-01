"""Retrieve stops and departures info from REST service."""
import requests

API_BASE = "https://public-transport-api.herokuapp.com"
REGION = "tallinn"


def get_nearby_stops(api_base, lat, lng):
    """
    Get nearby stops.

    :param api_base: Base URL that the endpoint gets appended to
    :param lat: Latitude
    :param lng: Longitude
    :return: List of all nearby stops
    """
    api = api_base + "/stops/" + str(lat) + "/" + str(lng)
    distance_data = requests.get(api).json()
    distance_list = sorted(distance_data, key=lambda k: int(k['distance'].replace(" m", "")))
    return distance_list


def get_nearest_stop(api_base, lat, lng):
    """
    Get nearest stop.

    :param api_base: Base URL that the endpoint gets appended to
    :param lat: Latitude
    :param lng: Longitude
    :return: Nearest stop
    """
    api = api_base + "/stops/" + str(lat) + "/" + str(lng)
    distance_data = requests.get(api).json()
    if not distance_data:
        return None
    min_distance = min(distance_data, key=lambda x: int(x['distance'].replace(" m", "")))
    return min_distance


def get_next_departures(api_base, region, stop_id):
    """
    Get next departures from stop.

    :param api_base: Base URL that the endpoint gets appended to
    :param region: Region
    :param stop_id: Stop ID
    :return: List of next departures from stop
    """
    return None


def get_next_departure(api_base, region, stop_id):
    """
    Get next departure from stop.

    :param api_base: Base URL that the endpoint gets appended to
    :param region: Region
    :param stop_id: Stop ID
    :return: Next departure from stop
    """
    return None


if __name__ == '__main__':
    print(get_nearby_stops(API_BASE, 59.3977111, 24.660198))
    print(get_nearest_stop(API_BASE, 59.3977111, 24.660198))
    print(get_next_departures(API_BASE, REGION, get_nearest_stop(API_BASE, 59.3977111, 24.660198)["id"]))
    print(get_next_departure(API_BASE, REGION, get_nearest_stop(API_BASE, 59.3977111, 24.660198)["id"]))
