import requests


def get_stations(url='https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/', offset=0):
    args = {'offset' : offset} if offset else {}

    response = requests.get(url, params=args)

    if response.status_code == 200:

        payload = response.json()
        results = payload.get('ListaEESSPrecio', [])

        if results:
            for station in results:
                provincia = station['Provincia']
                print(provincia)

        next = input('Continuar listando? [Y/N]').lower()
        if next == 'y':
            get_stations(offset=offset+10)
if __name__ == '__main__':
    url = 'https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/'
    get_stations()
