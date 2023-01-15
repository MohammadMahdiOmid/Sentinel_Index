from datetime import date

from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt

api = SentinelAPI('mahdiomid', 'mahdi21376')
footprint = geojson_to_wkt(read_geojson('./test2.geojson'))
products = api.query(footprint,
                     date=('20151219', date(2015, 12, 29)),
                     platformname='Sentinel-2',
                     cloudcoverpercentage=(0, 30))
api.download_all(products)

print("DONE")
