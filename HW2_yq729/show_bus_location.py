import sys
import json

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


def show_bus_location(key, line_name):
    url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key={}&VehicleMonitoringDetailLevel=calls&LineRef={}".format(
        key, line_name)

    # open the url and load as dictionary using json
    opened_url = urllib.urlopen(url)
    decoded_data = opened_url.read().decode("utf-8")
    dict_data = json.loads(decoded_data)

    # parse the dictionary to get the list of bus activity
    bus_activity_list = dict_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

    # total number of active buses is the length of this list
    num_active_bus = len(bus_activity_list)

    # below are the desired printed outputs
    print('Bus Line : {}'.format(line_name))
    print('Number of Active Buses : {}'.format(num_active_bus))

    for i in range(num_active_bus):
        location = bus_activity_list[i]['MonitoredVehicleJourney']['VehicleLocation']
        print('Bus {} is at latitude {} and longitude {}'.format(i, location['Latitude'], location['Longitude']))


if __name__ == '__main__':

    assert len(sys.argv) == 3, "Expect exactly 3 system arguments."

    key = sys.argv[1]
    line_name = sys.argv[2]

    show_bus_location(key, line_name)
