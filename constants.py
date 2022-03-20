ONE_MAP_API = 'https://developers.onemap.sg/commonapi/search?searchVal={ searchVal }&returnGeom=Y&getAddrDetails=N'
URA_API = 'https://maps.ura.gov.sg/arcgis/rest/services/MP19/Landuse_gaz/MapServer/46/query?returnGeometry=true&where=1=1&outSR=4326&outFields=*&inSr=4326&geometry={"x":{ lng },"y":{ lat },"spatialReference":{"wkid":4326}}&geometryType=esriGeometryPoint&spatialRel=esriSpatialRelWithin&f=json'
POSTAL_CODE_PREFIX_URL = 'https://www.ura.gov.sg/realEstateIIWeb/resources/misc/list_of_postal_districts.htm'
POSTAL_CODE_SUFFIX_RANGE = range(3010, 3011)
POSTAL_CODE_SUFFIX_LEADING_ZERO = 4
CALLS_PER_MINUTE = 250
MINUTE = 60