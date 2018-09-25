import sys
import json

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


def get_bus_information(key, line_name,csv_path):
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

    with open(csv_path, 'w') as f:
        f.writelines("Latitude,Longitude,Stop Name,Stop Status\n")
        for i in range(num_active_bus):
            Latitude = str(bus_activity_list[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
            Longitude = str(bus_activity_list[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
            if bus_activity_list[i]['MonitoredVehicleJourney']['OnwardCalls'] == {}:
                StopPointName = "N/A"
                PresentableDistance = "N/A"
            else:
                StopPointName = bus_activity_list[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0][
                    'StopPointName']
                PresentableDistance = \
                bus_activity_list[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances'][
                    'PresentableDistance']
            f.writelines(Latitude + ',' + Longitude + ',' + StopPointName + ',' + PresentableDistance + '\n')


if __name__ == '__main__':

    assert len(sys.argv) == 4, "Expect exactly 3 system arguments."

    key = sys.argv[1]
    line_name = sys.argv[2]
    csv_path = sys.argv[3]

    get_bus_information(key,line_name,csv_path)
